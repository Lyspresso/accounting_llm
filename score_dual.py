#!/usr/bin/env python3
"""
Dual-derivation scoring.

Where the key speaks, solver-vs-key is the standard. Where it does not, and the
figure does not derive from the key's stated components, the standard becomes
DUAL INDEPENDENT DERIVATION: two blind solvers, decorrelated framing, no sight
of each other. Agreement verifies the figure by derivation; disagreement is a
real candidate for adjudication.

Scores the convergence prediction on record: trim corroboration should move
toward baseline once key-silent figures verify this way.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)
import canon  # noqa: E402
import compare_stage1_v3 as C  # noqa: E402

# A 3-character minimum silently deleted every single-digit period identifier:
# "Year 1"/"Year 2"/"Year 3" all collapsed to the same token set, so every row
# of a schedule paired against the FIRST year. It also dropped part letters
# ("c:", "d:") and day numbers ("Dec 31"). Seven of fifteen rows on one item
# were mis-paired, and because they scored jaccard 1.00 the zero-guard - which
# only fires below 0.70 - never saw them. The corrupted readout made the
# CORRECT derivation look internally impossible.
WORD = re.compile(r"[a-z]+|\d+")

# Synonym normalisation before tokenising: "NBV immediately before scrapping"
# scored 0.29 against "Year 3 year-end NBV", just under the 0.30 gate, so a real
# disagreement was filed as NO_COUNTERPART.
SYN = ((r"\bnbv\b", "net book value"), (r"\bcarrying amount\b", "net book value"),
       (r"\bcarrying value\b", "net book value"), (r"\bcv\b", "net book value"),
       (r"\baccum\b", "accumulated"), (r"\bdep\b", "depreciation"),
       (r"\bamort\b", "amortization"), (r"\byr\b", "year"))


def toks(s):
    t = str(s or "").lower()
    for pat, rep in SYN:
        t = re.sub(pat, rep, t)
    return set(WORD.findall(t))


def find_counterpart(label, value, dual_answers):
    """
    Best match in the second derivation. Label overlap first - a value-only
    match could pair unrelated figures that happen to coincide.
    """
    v = C.as_number(value)
    if v is None:
        return None
    lt = toks(label)
    scored = []
    for a in dual_answers:
        av = C.as_number(a.get("value"))
        if av is None:
            continue
        at = toks(a.get("label"))
        scored.append((len(lt & at) / max(1, len(lt | at)), a))
    scored.sort(key=lambda x: -x[0])
    best, best_score = (scored[0][1], scored[0][0]) if scored else (None, 0.0)
    # `if j > best_score` was strict, so ties resolved to whichever candidate
    # came first - deterministically the earliest year once ordinals were
    # stripped. A tie is ambiguity and must not be resolved by list order.
    if len(scored) > 1 and abs(scored[1][0] - best_score) < 1e-9 and best_score > 0:
        return None
    if best is not None and best_score >= 0.30:
        bv = C.as_number(best.get("value"))
        v0 = abs(v)
        # A zero paired against a materially non-zero figure is not a
        # counterpart, it is a mis-pairing: label overlap alone matched two of
        # agent_283#02's lease-liability figures against an unrelated 0.00 and
        # reported them as 208,029 vs 0 disagreements. Unless the labels are a
        # near-exact match, treat it as no counterpart - which leaves the figure
        # UNVERIFIED rather than either passing it or inventing a finding.
        if bv is not None and best_score < 0.70:
            if (abs(bv) < 1e-9) != (v0 < 1e-9):
                return None
        return (best, best_score, "label")
    # fall back to exact value presence anywhere in the second derivation
    for a in dual_answers:
        av = C.as_number(a.get("value"))
        if av is not None and abs(abs(av) - abs(v)) <= max(0.01, abs(v) * 1e-6):
            return (a, 0.0, "value")
    return None


def main():
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}
    known, amap = C.load_known(), C.load_alias_map(False)
    batch = json.load(open(os.path.join(OUT, "dual_batch.json"), encoding="utf-8"))

    verified, disagree, unmatched = [], [], []
    per_item = {}

    for b in batch:
        qid = b["id"]
        q = qs[qid]
        trim_p = os.path.join(b["dir"], "solver_output.json")
        dual_p = os.path.join(b["dual_dir"], "solver_output.json")
        if not (os.path.exists(trim_p) and os.path.exists(dual_p)):
            continue
        trim = json.load(open(trim_p, encoding="utf-8"))
        dual = json.load(open(dual_p, encoding="utf-8"))
        iss, _ = C.compare(trim, q, known, amap)
        flagged = [i for i in iss if i["kind"] == "SOLVER_MISMATCH"]
        da = dual.get("answers") or []

        item_v, item_d, item_u = 0, 0, 0
        for f in flagged:
            m = find_counterpart(f.get("label"), f.get("solver"), da)
            if not m:
                unmatched.append({"id": qid, "label": f.get("label"),
                                  "solver": f.get("solver"), "class": "NO_COUNTERPART"})
                item_u += 1
                continue
            a, score, how = m
            v1, v2 = C.as_number(f.get("solver")), C.as_number(a.get("value"))
            # Inherit the KEY's displayed precision, exactly as the main
            # comparator does. Hard-coding 2 decimals here scored 3,167.55 vs
            # 3,167 as a disagreement, which is the same whole-dollar display
            # question the comparator already settled.
            # canon owns the tolerance rule, including rounding context. This
            # scorer previously hard-coded 2 decimals AND ignored schedule
            # context, so it scored round-then-carry pairs inside rollforwards
            # as disagreements - the exact class already ruled textbook-blessed.
            prec = canon.num_precision(q.get("solution", ""))
            sched = canon.is_schedule_context(q.get("solution", ""), q.get("stem", ""))
            tolv = canon.tol_for(abs(v1), prec, sched, str(f.get("label") or ""))
            # A pair related by a whole period factor is a UNIT mismatch in my
            # label matching, not two solvers disagreeing: 1,125 monthly vs
            # 13,500 annual is the same rate. Do not score it as a finding.
            if canon.period_factor_pair(v1, v2, str(f.get("label") or ""),
                                        str(a.get("label") or "")):
                unmatched.append({"id": qid, "label": f.get("label"),
                                  "solver": v1, "counterpart": v2,
                                  "class": "PERIOD_UNIT_MISMATCH (scoring artifact)"})
                # An unresolved figure is UNVERIFIED, and an item holding one is
                # NOT cleared. Skipping both counters here reported an item with
                # zero verified figures as "fully cleared" and inflated the
                # convergence metric.
                item_u += 1
                continue
            if v2 is not None and abs(abs(v1) - abs(v2)) <= max(tolv, 0.01):
                verified.append({"id": qid, "label": f.get("label"), "value": v1,
                                 "matched_by": how, "label_overlap": round(score, 2)})
                item_v += 1
            else:
                disagree.append({"id": qid, "label": f.get("label"),
                                 "solver_1": v1, "solver_2": v2,
                                 "matched_by": how, "label_overlap": round(score, 2)})
                item_d += 1
        per_item[qid] = {"verified": item_v, "disagree": item_d,
                         "unverified": item_u,
                         # cleared requires every figure RESOLVED, not merely
                         # not-disagreeing
                         "now_clean": item_d == 0 and item_u == 0 and item_v > 0}

    with open(os.path.join(OUT, "dual_results.json"), "w", encoding="utf-8") as fh:
        json.dump({"verified": verified, "disagree": disagree,
                   "unmatched": unmatched, "per_item": per_item}, fh, indent=1)

    tot = len(verified) + len(disagree)
    print(f"figures put to dual derivation : {tot}")
    print(f"  VERIFIED BY DERIVATION       : {len(verified)} ({len(verified)/max(1,tot):.0%})")
    print(f"  genuine disagreement         : {len(disagree)}")
    print(f"    of which no counterpart    : {len(unmatched)}")
    cleared = sum(1 for v in per_item.values() if v["now_clean"])
    print(f"\nitems fully cleared by derivation: {cleared} / {len(per_item)}")

    print("\n--- CONVERGENCE PREDICTION, SCORED ---")
    print(f"  trim candidates before dual-derivation : 23")
    print(f"  items cleared                          : {cleared}")
    print(f"  trim candidates after                  : {23 - cleared}")
    print(f"  baseline candidates                    : 10")
    if 23 - cleared <= 12:
        print("  -> PREDICTION HOLDS: trim converges toward baseline")
    else:
        print("  -> PREDICTION FAILS: spread survives; residual is a solver-quality question")

    if disagree:
        print("\ngenuine disagreements (adjudication queue):")
        for d in disagree[:12]:
            print(f"   {d['id']:14s} {str(d['label'])[:42]:42s} "
                  f"s1={d['solver_1']} s2={d['solver_2']} ({d['matched_by']})")


if __name__ == "__main__":
    main()
