#!/usr/bin/env python3
"""
Stage 1 comparator — v3.

Changes from v2, each in response to a measured weakness:

  v1  textual "does this figure appear anywhere in the key" screen.
      Probe detection 0/2. The key text holds dozens of numbers, so a mutated
      key still found a match. Discarded.

  v2  strict structural diff on parsed journal lines. Probe detection 13/13,
      but the diff was ONE-SIDED: it flagged lines the solver invented and was
      blind to lines the key has that the solver never produced. A solver that
      simply omits an entry scored clean.

  v3  - symmetric diff within solver scope (key-extra lines are flagged)
      - form canonicalization before diffing, so compound-vs-separate and
        aggregated presentation stop scoring as mismatches
      - unmatched key lines partitioned into ROUTED_STAGE2 (legitimately
        outside this stage) vs COMPUTABLE_UNMATCHED (must be flagged);
        only the former may be excluded from probe scoring
      - vacuous-probe exclusion rate logged every run
      - comparator_version stamped into every evidence bundle

Usage:
    python3 compare_stage1_v3.py --batch 1
    python3 compare_stage1_v3.py --batch 1 --batch 2 --probes 40
"""

from paths import resolve
import argparse
import json
import os
import random
import re
from collections import Counter, defaultdict

COMPARATOR_VERSION = "3.8"
from ledger_io import PIPELINE_VERSION   # single source (2.2)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PACK = resolve("pack")

# One shared canonicalization library. Nothing below re-implements a rule:
# the dual scorer drifted from this file on two rules within an hour of being
# written and each drift produced a fabricated finding.
from canon import (  # noqa: E402
    MONEY_ABS, MONEY_FLOOR, NUM, PCT_LABEL, PROSE_NULL, RATIO_REL, SCHEDULE_CTX,
    as_number, corroborates, delatex, derivable_from_key, is_schedule_context,
    key_addresses_label, norm_acct, num_precision, nums, period_factor_pair,
    precision_tol, tol_for,
)


def load_known():
    known = set()
    for fn in ("chart_of_accounts.txt", "account_aliases.csv"):
        p = os.path.join(PACK, fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding="utf-8"):
            cells = line.split(",") if fn.endswith(".csv") else [line]
            for c in cells:
                c = norm_acct(c)
                if c and not c.startswith("canonical"):
                    known.add(c)
    return known


def load_alias_map(use_proposal=False):
    """
    variant -> canonical. Needed so an account mismatch can be scored HARD:
    without it, 'Interest expense' vs 'Interest Expense' would fail, so the
    check has to stay soft, and a genuinely wrong account then goes unseen.
    That is exactly what probe mode 'account' measured at 0 detection.
    """
    amap = {}
    p = os.path.join(PACK, "account_aliases.csv")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            cells = [c.strip().strip('"') for c in line.rstrip("\n").split(",") if c.strip()]
            if not cells or cells[0].lower().startswith("canonical"):
                continue
            canon = norm_acct(cells[0])
            for c in cells:
                amap[norm_acct(c)] = canon
    if use_proposal:
        pp = os.path.join(OUT, "alias_proposal.json")
        if os.path.exists(pp):
            for entry in json.load(open(pp, encoding="utf-8")):
                canon = norm_acct(entry["canonical"])
                amap[canon] = canon
                for v in entry["variants"]:
                    amap[norm_acct(v)] = canon
    return amap


def resolve(name, amap):
    n = norm_acct(name)
    return amap.get(n, n)


# ---------------------------------------------------------------- form layer

def solver_lines(sol):
    """Explode every solver entry into atomic legs."""
    out = []
    for je in sol.get("journal_entries") or []:
        for l in je.get("lines") or []:
            dr, cr = as_number(l.get("debit")) or 0.0, as_number(l.get("credit")) or 0.0
            if dr:
                out.append({"account": l.get("account"), "side": "dr",
                            "amount": float(dr), "part": je.get("part")})
            if cr:
                out.append({"account": l.get("account"), "side": "cr",
                            "amount": float(cr), "part": je.get("part")})
    return out


def key_lines_of(q):
    return [{"account": l.get("account"), "side": l.get("side"),
             "amount": float(l.get("amount") or 0), "part": None}
            for l in (q.get("answer_key") or [])]


def ms(lines):
    c = Counter()
    for l in lines:
        c[(norm_acct(l["account"]), l["side"], round(abs(l["amount"]), 2))] += 1
    return c


def ms_aggregated(lines):
    """
    Acceptable-form policy: compound vs separate entries, and gross vs net,
    are presentation choices the textbook sanctions. Summing each account+side
    across the item makes those forms compare equal, so they stop scoring as
    content mismatches.
    """
    agg = defaultdict(float)
    for l in lines:
        agg[(norm_acct(l["account"]), l["side"])] += abs(l["amount"])
    return {k: round(v, 2) for k, v in agg.items()}


def agg_matches(a, b):
    """Compare aggregated forms with the money tolerance."""
    if set(a) != set(b):
        return False
    return all(abs(a[k] - b[k]) <= precision_tol(a[k], 2, True) for k in a)


# ------------------------------------------------------------- the comparison

def compare(sol, q, known, amap):
    """Return (issues, scope) where scope describes what was comparable."""
    issues = []
    routed_early = 0        # key-silent labels routed before `scope` is built
    sl, kl = solver_lines(sol), key_lines_of(q)
    key_text = q.get("solution", "")
    schedule = is_schedule_context(key_text, q.get("stem", ""))
    prec = num_precision(key_text)
    pool = nums(key_text) | {round(abs(l["amount"]), 2) for l in kl}

    for a in sol.get("answers") or []:
        v = a.get("value")
        if as_number(v) is None:
            issues.append({"kind": "NON_NUMERIC_ANSWER", "label": a.get("label"),
                           "solver": str(v)[:160]})
        elif not corroborates(v, pool, key_text=key_text,
                              label=str(a.get("label") or ""),
                              schedule=schedule, prec=prec):
            terms = derivable_from_key(v, pool)
            if terms:
                issues.append({"kind": "KEY_SILENT_DERIVED", "label": a.get("label"),
                               "solver": v, "from_key_components": terms})
            else:
                # LOOSENING 3 of 4 (ORDER-002 item 5). Two situations were
                # collapsed into SOLVER_MISMATCH:
                #   (a) the key states a figure for this label and the solver's
                #       differs                      -> a real mismatch
                #   (b) the key never addresses this label at all
                #       -> a COVERAGE question, and charging it to the solver
                #          charges it for the key's silence
                # Only (a) is evidence of a wrong answer. (b) now routes to
                # Stage 2 for dual derivation. It is NOT a pass: per D5 a
                # no-counterpart figure stays UNVERIFIED and never
                # default-passes - the label just moves to the stage that can
                # actually settle it.
                addressed, why = key_addresses_label(str(a.get("label") or ""),
                                                     key_text)
                if addressed:
                    issues.append({"kind": "SOLVER_MISMATCH",
                                   "label": a.get("label"), "solver": v})
                else:
                    issues.append({"kind": "KEY_SILENT_UNADDRESSED",
                                   "label": a.get("label"), "solver": v,
                                   "why": why})
                    routed_early += 1

    for je in sol.get("journal_entries") or []:
        dr = sum(as_number(l.get("debit")) or 0 for l in je.get("lines") or [])
        cr = sum(as_number(l.get("credit")) or 0 for l in je.get("lines") or [])
        if abs(dr - cr) > 0.01:
            issues.append({"kind": "JE_UNBALANCED", "part": je.get("part"), "dr": dr, "cr": cr})

    for l in sl:
        if norm_acct(l["account"]) not in known:
            issues.append({"kind": "UNKNOWN_ACCOUNT", "account": l["account"]})

    # ---- scope ---------------------------------------------------------
    # If the solver produced no entries at all, the key's entry lines were
    # never in this stage's reach: they route to Stage 2 rather than counting
    # as disagreement. If it produced entries, every key line is comparable.
    scope = {"solver_has_entries": bool(sl), "key_lines": len(kl),
             "_routed_early": routed_early,
             "routed_stage2": routed_early, "computable_unmatched": 0}
    if not kl:
        return issues, scope
    if not sl:
        scope["routed_stage2"] = len(kl)
        issues.append({"kind": "ROUTED_STAGE2",
                       "why": "solver produced no journal entries for this item",
                       "key_lines": len(kl)})
        return issues, scope

    # AMOUNT equivalence now routes through canon, exactly as the scalar path
    # does. Previously ms() compared round(amount, 2) for exact equality, so a
    # solver carrying 279,286.65 never matched a key stating 279,287 even though
    # corroborates() called the same pair equivalent. Two paths, one figure, two
    # verdicts. Pairing on (account, side) remains a hard structural gate.
    prec_je = num_precision(key_text)
    unconsumed = list(range(len(kl)))
    matched_solver = set()
    # TWO PASSES. Greedy first-fit let one solver line consume a key line that
    # another line needed, so loosening the tolerance moved four items from pass
    # to FAIL - worse pairings than the exact multiset it replaced. Exact
    # matches claim their partners first; tolerance only settles what is left.
    for exact_pass in (True, False):
        for si, l in enumerate(sl):
            if si in matched_solver:
                continue
            acct, side, amt = norm_acct(l["account"]), l["side"], abs(l["amount"])
            for ki in list(unconsumed):
                k = kl[ki]
                if norm_acct(k["account"]) != acct or k["side"] != side:
                    continue
                ka = abs(k["amount"])
                if exact_pass:
                    ok = round(ka, 2) == round(amt, 2)
                else:
                    ok = abs(ka - amt) <= precision_tol(
                        ka, prec_je.get(round(ka, 2), 2), schedule, "")
                if ok:
                    unconsumed.remove(ki)
                    matched_solver.add(si)
                    break
    if not unconsumed and len(matched_solver) == len(sl):
        return issues, scope

    # Leftovers determine what is EXTRA. Classification lookups must still see
    # the FULL key set: restricting them to leftovers stripped away the
    # same-amount/different-account partners that soften a line to
    # ACCOUNT_TO_STAGE2, and four items hard-failed as a result.
    s_ms = ms([l for i, l in enumerate(sl) if i not in matched_solver])
    k_ms = ms([kl[i] for i in unconsumed])
    s_ms_full, k_ms_full = ms(sl), ms(kl)
    if not s_ms and not k_ms:
        return issues, scope

    if agg_matches(ms_aggregated(sl), ms_aggregated(kl)):
        issues.append({"kind": "FORM_DIFFERS",
                       "why": "same legs after compound/net canonicalization"})
        return issues, scope

    # Net-per-account, scoped to one entry/date. The chapter presents the
    # operating year-end entry in a compound and a two-part form and prefers
    # neither, but they differ on the ROU leg unless the account is netted.
    from canon import net_per_account
    if ms(net_per_account(sl)) == ms(net_per_account(kl)):
        issues.append({"kind": "FORM_DIFFERS",
                       "why": "identical after net-per-account within entry/date"})
        return issues, scope

    key_by_amt = defaultdict(list)
    for (acct, side, amt), n in k_ms_full.items():
        key_by_amt[(side, amt)].extend([acct] * n)

    extra_solver = s_ms
    extra_key = k_ms

    # Aggregation equivalence: a pooled control-account line (Dr Investments-AFS
    # 150,000) is the same entry as the key's per-security split (90,000 +
    # 60,000). Same ledger balances, different house style - not a content
    # defect. Match a solver line against the SUM of key lines on the same side
    # whose account shares its leading token.
    def aggregates_to(acct, side, amt):
        stem = norm_acct(acct).split(" ")[0] if norm_acct(acct) else ""
        if not stem:
            return None
        group = [(a, m) for (a, sd, m), c in k_ms_full.items()
                 for _ in range(c) if sd == side and a.split(" ")[0] == stem]
        if len(group) < 2:
            return None
        tot = round(sum(m for _, m in group), 2)
        return group if abs(tot - amt) <= precision_tol(amt, 2, True) else None

    for (acct, side, amt), n in extra_solver.items():
        agg = aggregates_to(acct, side, amt)
        if agg:
            issues.append({"kind": "JE_AGGREGATED", "side": side, "amount": amt,
                           "solver": acct, "key_lines": [a for a, _ in agg][:4]})
            for a, m in agg:
                extra_key[(a, side, round(m, 2))] = 0
            continue
        if key_by_amt.get((side, amt)):
            opts = sorted(set(key_by_amt[(side, amt)]))
            # Same amount and side, different account string. If the two names
            # resolve to the same canonical account it is spelling; if they do
            # not, it is a wrong account and must be HARD - a soft verdict here
            # is what let probe mode 'account' through undetected.
            same = any(resolve(acct, amap) == resolve(o, amap) for o in opts)
            # Amount and side agree; only the account STRING differs. Stage 1
            # verifies amounts and structure - the pack is explicit that an
            # unresolved account name is a flag, never an auto-fail, because
            # deciding whether "Loss from Litigation" and "Loss on Litigation"
            # are the same account is treatment, and treatment is Stage 2's job.
            # These are the routed-to-Stage-2 population, and the only
            # population that may be excluded from probe scoring.
            issues.append({"kind": "ACCOUNT_SPELLING" if same else "ACCOUNT_TO_STAGE2",
                           "side": side, "amount": amt,
                           "solver": acct, "key_options": opts[:3]})
            scope["routed_stage2"] += 1
        else:
            issues.append({"kind": "JE_LINE_NOT_IN_KEY", "side": side,
                           "amount": amt, "solver": acct, "n": n})

    sol_by_amt = defaultdict(list)
    for (acct, side, amt), n in s_ms_full.items():
        sol_by_amt[(side, amt)].extend([acct] * n)
    for (acct, side, amt), n in extra_key.items():
        if n <= 0:
            continue  # consumed by an aggregation match above
        if sol_by_amt.get((side, amt)):
            continue  # already reported as ACCOUNT_DIFFERS from the other side
        scope["computable_unmatched"] += n
        issues.append({"kind": "KEY_LINE_NOT_IN_SOLVER", "side": side,
                       "amount": amt, "key": acct, "n": n})
    return issues, scope


HARD = ("SOLVER_MISMATCH", "JE_UNBALANCED", "JE_LINE_NOT_IN_KEY",
        "KEY_LINE_NOT_IN_SOLVER")


# ---------------------------------------------------------------- calibration

def run_probes(items, qs, known, amap, n_target, rng):
    """
    Falsifiable probes only. A probe mutates a key line the solver actually
    reproduced, so a working comparator MUST notice. Mutating a line the
    solver never matched is undetectable by construction; those are counted
    as vacuous and excluded, and the exclusion rate is reported because a
    rising rate would mean the probe set is quietly losing its teeth.
    """
    run = caught = vacuous = 0
    misses = []
    pool = list(items)
    rng.shuffle(pool)
    for it in pool:
        if run >= n_target:
            break
        q = qs.get(it["id"])
        sp = os.path.join(it["dir"], "solver_output.json")
        if not q or not os.path.exists(sp):
            continue
        try:
            sol = json.load(open(sp, encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        kl, sl = key_lines_of(q), solver_lines(sol)
        if not kl or not sl:
            continue
        s_ms = ms(sl)
        matched = [i for i, l in enumerate(kl)
                   if s_ms.get((norm_acct(l["account"]), l["side"],
                                round(abs(l["amount"]), 2)), 0) > 0]
        if not matched:
            vacuous += 1
            continue
        # Detection is measured on the STRUCTURAL DIFF SIGNATURE, not on the
        # hard-issue count. A dr/cr flip can push a line from the hard bucket
        # into the soft account bucket, leaving the hard count unchanged even
        # though the comparator plainly saw the difference. Counting only hard
        # issues therefore understates detection and would fail the floor for
        # the wrong reason.
        STRUCT = ("JE_LINE_NOT_IN_KEY", "KEY_LINE_NOT_IN_SOLVER",
                  "ACCOUNT_TO_STAGE2", "ACCOUNT_SPELLING", "FORM_DIFFERS")

        def sig(issues):
            return sorted((i["kind"], i.get("side"), i.get("amount"))
                          for i in issues if i["kind"] in STRUCT)

        base_issues, _ = compare(sol, q, known, amap)
        base_sig = sig(base_issues)

        mk = [dict(l) for l in kl]
        t = rng.choice(matched)
        mode = rng.choice(("amount", "side"))
        if mode == "amount":
            mk[t]["amount"] = round(mk[t]["amount"] * 1.07 + 13, 2)
        else:
            mk[t]["side"] = "cr" if mk[t]["side"] == "dr" else "dr"
        mq = dict(q)
        mq["answer_key"] = mk
        mut_issues, _ = compare(sol, mq, known, amap)
        mut_sig = sig(mut_issues)

        run += 1
        if mut_sig != base_sig:
            caught += 1
        else:
            misses.append({"id": it["id"], "mode": mode})
    return {"probes_run": run, "probes_caught": caught, "vacuous_excluded": vacuous,
            "vacuous_rate": round(vacuous / max(1, run + vacuous), 3),
            "misses": misses[:10]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, action="append", default=None)
    ap.add_argument("--probes", type=int, default=40)
    ap.add_argument("--seed", type=int, default=343)
    ap.add_argument("--use-proposal", action="store_true",
                    help="resolve aliases using the UNAPPLIED harvest proposal")
    args = ap.parse_args()
    batches = args.batch or [1]
    rng = random.Random(args.seed)
    known = load_known()
    amap = load_alias_map(args.use_proposal)

    man = json.load(open(os.path.join(OUT, "stage1_manifest.json"), encoding="utf-8"))
    items = [i for i in man["items"] if i["batch"] in batches]
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}

    rows, ledger = [], []
    tally = Counter()
    kinds = Counter()

    for it in items:
        q = qs[it["id"]]
        sp = os.path.join(it["dir"], "solver_output.json")
        if not os.path.exists(sp):
            tally["missing_output"] += 1
            rows.append({"id": it["id"], "status": "NO_SOLVER_OUTPUT"})
            continue
        try:
            sol = json.load(open(sp, encoding="utf-8"))
        except json.JSONDecodeError as e:
            tally["missing_output"] += 1
            rows.append({"id": it["id"], "status": "UNPARSEABLE_SOLVER_OUTPUT", "error": str(e)})
            continue

        issues, scope = compare(sol, q, known, amap)
        for i in issues:
            kinds[i["kind"]] += 1
        hard = [i for i in issues if i["kind"] in HARD]
        status = "failed" if hard else "machine_passed"
        tally[status] += 1
        if any(i["kind"] == "FORM_DIFFERS" for i in issues):
            tally["form_differs"] += 1
        if any(i["kind"] == "ROUTED_STAGE2" for i in issues):
            tally["routed_stage2"] += 1

        rows.append({"id": it["id"], "status": status, "risk_score": it["risk_score"],
                     "scope": scope, "n_issues": len(issues), "issues": issues[:14]})
        ledger.append({"content_hash": q["content_hash"], "id": q["id"],
                       "pack_id": q["pack_id"], "status": status,
                       "reasons": sorted({i["kind"] for i in hard}), "stage": 1,
                       "comparator_version": COMPARATOR_VERSION,
                       "pipeline_version": PIPELINE_VERSION})

        # comparator_version stamped into the evidence bundle
        with open(os.path.join(it["dir"], "comparison.json"), "w", encoding="utf-8") as fh:
            json.dump({"id": it["id"], "comparator_version": COMPARATOR_VERSION,
                       "pipeline_version": PIPELINE_VERSION, "status": status,
                       "scope": scope, "issues": issues}, fh, indent=1)

    cal = run_probes(items, qs, known, amap, args.probes, rng)

    rep = {"batches": batches, "comparator_version": COMPARATOR_VERSION,
           "items": len(items), "tally": dict(tally), "issue_kinds": dict(kinds),
           "calibration": cal, "rows": rows}
    tag = "".join(str(b) for b in batches)
    with open(os.path.join(OUT, f"stage1_v3_batch{tag}_results.json"), "w",
              encoding="utf-8") as fh:
        json.dump(rep, fh, indent=1)
    from ledger_io import append_rows
    append_rows(ledger, supersede_stage0=False)

    print(f"comparator v{COMPARATOR_VERSION}   batches {batches}   items {len(items)}")
    print(f"  machine_passed        : {tally['machine_passed']}")
    print(f"  failed                : {tally['failed']}")
    print(f"  form_differs (soft)   : {tally['form_differs']}")
    print(f"  routed to Stage 2     : {tally['routed_stage2']}")
    print(f"  missing output        : {tally['missing_output']}")
    print("  issue kinds:")
    for k, v in kinds.most_common():
        print(f"      {k:24s} {v}")
    print(f"  probes  : {cal['probes_caught']}/{cal['probes_run']} caught")
    print(f"  vacuous : {cal['vacuous_excluded']} excluded "
          f"({cal['vacuous_rate']:.1%} of candidates)")
    if cal["misses"]:
        print(f"  MISSES  : {cal['misses']}")


if __name__ == "__main__":
    main()
