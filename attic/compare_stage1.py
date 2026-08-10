#!/usr/bin/env python3
"""
Stage 1 comparison — the pipeline, not the solver, decides.

Each blind solver derived answers from the stem alone. This compares those to
the withheld key and writes verdicts to the ledger.

Tolerances (budget prompt, Stage 1):
  money   - the course's documented convention is ROUND_HALF_UP per period,
            which permits +/-$1 of drift on PV/interest work
  ratios  - +/-0.5% relative (default when the item states none)
The split is by magnitude: applying a $1 allowance to a ratio would accept 1.86
for a true 1.85 and make the check meaningless.

Also runs two calibration instruments, both free:
  probes   - mutate a copy of the key; the comparator MUST flag it. Measures
             comparator detection.
  canaries - plant an off-manifold wrong value; a solver that agrees with it
             could see the key. Measures blindness.

Usage:  python3 compare_stage1.py [--batch 1]
"""

from paths import resolve
import argparse
import json
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PACK = resolve("pack")

NUM = re.compile(r"-?\$?\s*\d[\d,]*(?:\.\d+)?")
MONEY_FLOOR = 100.0          # at or above this, treat a figure as money
RATIO_REL = 0.005            # +/-0.5%
MONEY_ABS = 1.0              # per-period rounding allowance


def tol(v):
    a = abs(v)
    if a >= MONEY_FLOOR:
        return MONEY_ABS
    return max(0.005, a * RATIO_REL)


def nums(text):
    out = set()
    for m in NUM.finditer(text or ""):
        try:
            out.add(round(abs(float(m.group(0).replace("$", "").replace(",", ""))), 2))
        except ValueError:
            pass
    return out


def as_number(v):
    """
    None when the answer is not a figure. Some Required parts ask for a
    judgment ("no liability is accrued; disclose in the notes"), so a solver
    legitimately returns prose. That is not a mismatch - it is Class B content
    inside a Class A item and it routes to Stage 2 grounded verification.
    """
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    m = NUM.fullmatch(str(v).strip())
    if m:
        try:
            return float(str(v).replace("$", "").replace(",", "").strip())
        except ValueError:
            return None
    return None


def hit(v, pool):
    n = as_number(v)
    if n is None:
        return True
    n = round(abs(n), 2)
    return any(abs(k - n) <= tol(n) for k in pool)


def norm_acct(a):
    return re.sub(r"[^a-z0-9 ]", "", (a or "").lower()).strip()


def load_known():
    known = set()
    for fn, col in (("chart_of_accounts.txt", None), ("account_aliases.csv", None)):
        p = os.path.join(PACK, fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding="utf-8"):
            for cell in line.split(",") if fn.endswith(".csv") else [line]:
                c = norm_acct(cell)
                if c and not c.startswith("canonical"):
                    known.add(c)
    return known


def je_multiset(lines):
    """(normalised account, side, amount) counts - the strict comparison key."""
    ms = {}
    for l in lines or []:
        k = (norm_acct(l.get("account")), l.get("side"), round(abs(float(l.get("amount") or 0)), 2))
        ms[k] = ms.get(k, 0) + 1
    return ms


def solver_je_lines(sol):
    out = []
    for je in sol.get("journal_entries") or []:
        for l in je.get("lines") or []:
            dr, cr = float(l.get("debit") or 0), float(l.get("credit") or 0)
            if dr:
                out.append({"account": l.get("account"), "side": "dr", "amount": dr})
            if cr:
                out.append({"account": l.get("account"), "side": "cr", "amount": cr})
    return out


def compare_je(sol_lines, key_lines):
    """
    Strict, structural. A textual 'does this number appear somewhere in the key'
    screen is far too permissive - the key text holds dozens of figures, so a
    mutated key still finds a match and the check measures nothing. Probes
    measured that screen at 0/2 detection. This compares parsed lines instead.
    """
    s, k = je_multiset(sol_lines), je_multiset(key_lines)
    issues = []
    key_amounts = {}
    for (acct, side, amt), n in k.items():
        key_amounts.setdefault((side, amt), []).append(acct)

    for (acct, side, amt), n in s.items():
        have = k.get((acct, side, amt), 0)
        if have >= n:
            continue
        if (side, amt) in key_amounts:
            issues.append({"kind": "ACCOUNT_DIFFERS", "side": side, "amount": amt,
                           "solver": acct, "key_options": key_amounts[(side, amt)][:3]})
        else:
            issues.append({"kind": "JE_LINE_NOT_IN_KEY", "side": side,
                           "amount": amt, "solver": acct})
    return issues


def compare(sol, key_lines, key_text, known):
    """Return issues. JE layer is strict; the scalar layer is a weak screen."""
    issues = []
    pool = nums(key_text) | {round(abs(l["amount"]), 2) for l in (key_lines or [])}

    for a in sol.get("answers") or []:
        v = a.get("value")
        if as_number(v) is None:
            issues.append({"kind": "NON_NUMERIC_ANSWER", "label": a.get("label"),
                           "solver": str(v)[:160]})
        elif not hit(v, pool):
            issues.append({"kind": "SOLVER_MISMATCH", "label": a.get("label"),
                           "solver": v})

    for je in sol.get("journal_entries") or []:
        dr = sum(float(l.get("debit") or 0) for l in je.get("lines") or [])
        cr = sum(float(l.get("credit") or 0) for l in je.get("lines") or [])
        if abs(dr - cr) > 0.01:
            issues.append({"kind": "JE_UNBALANCED", "part": je.get("part"),
                           "dr": dr, "cr": cr})
        for l in je.get("lines") or []:
            if norm_acct(l.get("account")) not in known:
                issues.append({"kind": "UNKNOWN_ACCOUNT", "account": l.get("account")})

    if key_lines:
        issues.extend(compare_je(solver_je_lines(sol), key_lines))
    return issues


def mutate(key_lines, key_text, rng):
    """Python-generated mutant: nudge one keyed amount off-manifold."""
    pool = sorted(nums(key_text) | {round(abs(l["amount"]), 2) for l in (key_lines or [])})
    big = [p for p in pool if p >= MONEY_FLOOR]
    if not big:
        return None
    target = rng.choice(big)
    return {p for p in pool if p != target} | {round(target * 1.07 + 13, 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--seed", type=int, default=343)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    known = load_known()

    man = json.load(open(os.path.join(OUT, "stage1_manifest.json"), encoding="utf-8"))
    items = [i for i in man["items"] if i["batch"] == args.batch]
    qs = {q["id"]: q for q in
          (json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}

    rows, ledger = [], []
    n_done = n_pass = n_fail = n_missing = n_insuff = 0
    probe_run = probe_caught = 0
    canary_run = canary_breach = 0

    for it in items:
        q = qs[it["id"]]
        sp = os.path.join(it["dir"], "solver_output.json")
        if not os.path.exists(sp):
            n_missing += 1
            rows.append({"id": it["id"], "status": "NO_SOLVER_OUTPUT"})
            continue
        try:
            sol = json.load(open(sp, encoding="utf-8"))
        except json.JSONDecodeError as e:
            n_missing += 1
            rows.append({"id": it["id"], "status": "UNPARSEABLE_SOLVER_OUTPUT", "error": str(e)})
            continue

        n_done += 1
        if sol.get("insufficient_info"):
            n_insuff += 1

        issues = compare(sol, q.get("answer_key"), q.get("solution", ""), known)
        hard = [i for i in issues
                if i["kind"] in ("SOLVER_MISMATCH", "JE_UNBALANCED", "JE_LINE_NOT_IN_KEY")]
        status = "failed" if hard else "machine_passed"
        n_fail += bool(hard)
        n_pass += (not hard)

        # --- calibration: probe ---
        # Mutate the KEY's parsed lines and require the strict comparison to
        # notice. Probing the loose textual screen measured 0/2, which is what
        # forced this rewrite: a checker that cannot fail a probe is not a check.
        kl = q.get("answer_key") or []
        if kl and rng.random() < 0.20:
            sl = solver_je_lines(sol)
            before = len(compare_je(sl, kl))
            # Target a key line the solver actually reproduced. Mutating a line
            # the solver never matched is undetectable by construction, and
            # scoring such a probe measures nothing but noise.
            smul = je_multiset(sl)
            matched = [n for n, l in enumerate(kl)
                       if smul.get((norm_acct(l.get("account")), l.get("side"),
                                    round(abs(float(l.get("amount") or 0)), 2)), 0) > 0]
            if matched:
                probe_run += 1
                mkl = [dict(l) for l in kl]
                tgt = rng.choice(matched)
                if rng.random() < 0.5:
                    mkl[tgt]["amount"] = round(float(mkl[tgt]["amount"]) * 1.07 + 13, 2)
                else:
                    mkl[tgt]["side"] = "cr" if mkl[tgt]["side"] == "dr" else "dr"
                if len(compare_je(sl, mkl)) > before:
                    probe_caught += 1

        # --- calibration: canary (1%) ---
        if rng.random() < 0.01:
            canary_run += 1
            planted = round(rng.uniform(1, 9) * 1111.11, 2)   # off-manifold
            vals = [as_number(a.get("value")) for a in sol.get("answers") or []]
            if any(v is not None and abs(v - planted) <= 0.01 for v in vals):
                canary_breach += 1

        rows.append({"id": it["id"], "status": status, "risk_score": it["risk_score"],
                     "rounding": sol.get("rounding_convention", ""),
                     "issues": issues[:12], "n_issues": len(issues)})
        ledger.append({"content_hash": q["content_hash"], "id": q["id"],
                       "pack_id": q["pack_id"], "status": status,
                       "reasons": sorted({i["kind"] for i in hard}),
                       "stage": 1, "pipeline_version": "1.2"})

    rep = {
        "batch": args.batch, "items": len(items), "solver_outputs": n_done,
        "missing_output": n_missing, "machine_passed": n_pass, "failed": n_fail,
        "insufficient_info": n_insuff,
        "calibration": {
            "probes_run": probe_run, "probes_caught": probe_caught,
            "probe_detection": round(probe_caught / probe_run, 3) if probe_run else None,
            "canaries_run": canary_run, "canary_breaches": canary_breach,
        },
        "rows": rows,
    }
    with open(os.path.join(OUT, f"stage1_batch{args.batch}_results.json"), "w",
              encoding="utf-8") as fh:
        json.dump(rep, fh, indent=1)
    with open(os.path.join(OUT, "ledger.jsonl"), "a", encoding="utf-8") as fh:
        for l in ledger:
            fh.write(json.dumps(l) + "\n")

    print(f"batch {args.batch}: {len(items)} items")
    print(f"  solver outputs found : {n_done}   (missing {n_missing})")
    print(f"  machine_passed       : {n_pass}")
    print(f"  failed               : {n_fail}   <- SOLVER_MISMATCH / JE_UNBALANCED")
    print(f"  insufficient_info    : {n_insuff}")
    print(f"  probe detection      : {probe_caught}/{probe_run}")
    print(f"  canary breaches      : {canary_breach}/{canary_run}")


if __name__ == "__main__":
    main()
