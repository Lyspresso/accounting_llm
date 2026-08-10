#!/usr/bin/env python3
"""
Production pre-flight. Both probe floors re-cleared under the EXACT production
stack - trim-1 harness outputs, comparator v3.7, canon, dual-derivation - with
statistical bounds. The old 40/40 detection figure predates most of the current
comparator, so it does not transfer.

FIRST_BATCH_GATE is armed: nothing launches unless BOTH floors clear their
bound, not their point estimate.
"""

import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)
import canon                          # noqa: E402
import compare_stage1_v3 as C
import provenance as PROV         # noqa: E402

PROBE_DET_FLOOR = 0.85
PROBE_FP_CEILING = 0.10


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def load():
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}
    return qs, C.load_known(), C.load_alias_map(False)


def detection_floor(n_target=40, seed=7):
    """Falsifiable probes against the production comparator."""
    qs, known, amap = load()
    par = {e["id"]: e["dir"] for e in
           json.load(open(os.path.join(OUT, "parity50.json"), encoding="utf-8"))}
    rng = random.Random(seed)
    ids = list(par)
    rng.shuffle(ids)
    run = caught = vacuous = 0
    misses = []
    STRUCT = ("JE_LINE_NOT_IN_KEY", "KEY_LINE_NOT_IN_SOLVER",
              "ACCOUNT_TO_STAGE2", "ACCOUNT_SPELLING", "FORM_DIFFERS",
              "JE_AGGREGATED", "SOLVER_MISMATCH", "KEY_SILENT_DERIVED")

    def sig(iss):
        return sorted((i["kind"], i.get("side"), i.get("amount"), i.get("label"))
                      for i in iss if i["kind"] in STRUCT)

    for qid in ids:
        if run >= n_target:
            break
        q = qs.get(qid)
        p = os.path.join(par[qid], "solver_output.json")
        if not q or not os.path.exists(p):
            continue
        sol = json.load(open(p, encoding="utf-8"))
        kl = C.key_lines_of(q)
        sl = C.solver_lines(sol)
        if not kl or not sl:
            continue
        s_ms = C.ms(sl)
        matched = [i for i, l in enumerate(kl)
                   if s_ms.get((canon.norm_acct(l["account"]), l["side"],
                                round(abs(l["amount"]), 2)), 0) > 0]
        if not matched:
            vacuous += 1
            continue
        base = sig(C.compare(sol, q, known, amap)[0])
        mk = [dict(l) for l in kl]
        t = rng.choice(matched)
        mode = rng.choice(("amount", "side"))
        if mode == "amount":
            mk[t]["amount"] = round(mk[t]["amount"] * 1.07 + 13, 2)
        else:
            mk[t]["side"] = "cr" if mk[t]["side"] == "dr" else "dr"
        mq = dict(q)
        mq["answer_key"] = mk
        run += 1
        if sig(C.compare(sol, mq, known, amap)[0]) != base:
            caught += 1
        else:
            misses.append({"id": qid, "mode": mode})
    lo, hi = wilson(caught, run)
    return {"run": run, "caught": caught, "vacuous": vacuous,
            "rate": caught / max(1, run), "ci": (lo, hi),
            "passes": lo >= PROBE_DET_FLOOR, "misses": misses}


def dual_verified():
    """(id, normalised label) pairs the second derivation verified."""
    p = os.path.join(OUT, "dual_results.json")
    out = set()
    if os.path.exists(p):
        d = json.load(open(p, encoding="utf-8"))
        for v in d.get("verified", []):
            out.add((v["id"], str(v.get("label") or "").strip().lower()))
    return out


def fp_floor():
    """
    False positives against goldens whose truth says PASS.

    The production stack INCLUDES dual derivation, so a figure the second
    derivation independently confirmed is corroborated and must not count as a
    hard issue here. Scoring the comparator alone and calling it the production
    stack put the false-positive rate at 38.5% by ignoring the very mechanism
    that resolves key-silent figures.
    """
    dv = dual_verified()
    qs, known, amap = load()
    gold_dir = os.path.join(HERE, "goldens")
    par = {e["id"]: e["dir"] for e in
           json.load(open(os.path.join(OUT, "parity50.json"), encoding="utf-8"))}
    clean = fp = stale = inadmissible = 0
    tiers = {}
    offenders = []
    for fn in sorted(os.listdir(gold_dir)):
        if not fn.endswith(".json") or fn == "INDEX.json":
            continue
        g = json.load(open(os.path.join(gold_dir, fn), encoding="utf-8"))
        qid = g["id"]
        q = qs.get(qid)
        if not q:
            continue
        # truth-versioning: a golden only scores against the content it was
        # verified on
        if g.get("truth_as_of_hash") and g["truth_as_of_hash"] != q["content_hash"]:
            stale += 1
            continue
        if g["expected_verdict"] != "PASS":
            continue
        # Score the newest ADMISSIBLE derivation, via the SHARED resolver in
        # provenance.py. This logic used to live here only, and fp_taxonomy.py
        # scored a different (inadmissible) bundle for the same item - the two
        # tools disagreed about agent_204#02 by 32 findings. One rule, one
        # implementation.
        src, why_src = PROV.evidence_dir(qid, q)
        if src is None:
            inadmissible += 1
            continue
        p = os.path.join(src, "solver_output.json")
        sol = json.load(open(p, encoding="utf-8"))
        iss, _ = C.compare(sol, q, known, amap)
        hard = [i for i in iss if i["kind"] in C.HARD
                and (qid, str(i.get("label") or "").strip().lower()) not in dv]
        clean += 1
        tiers[g["provenance_tier"]] = tiers.get(g["provenance_tier"], 0) + 1
        if hard:
            fp += 1
            offenders.append({"id": qid, "tier": g["provenance_tier"],
                              "kinds": sorted({i["kind"] for i in hard})})
    lo, hi = wilson(fp, clean)
    return {"clean": clean, "fp": fp, "stale": stale,
            "inadmissible": inadmissible, "rate": fp / max(1, clean),
            "ci": (lo, hi), "passes": hi <= PROBE_FP_CEILING,
            "tiers": tiers, "offenders": offenders}


def main():
    print("=== PRODUCTION PRE-FLIGHT ===")
    print(f"stack: harness trim-1 | comparator v{C.COMPARATOR_VERSION} | canon | dual-derivation\n")

    d = detection_floor()
    print("FLOOR #1 - detection (mutants must FAIL)")
    print(f"  probes run     : {d['run']}   vacuous excluded: {d['vacuous']}")
    print(f"  caught         : {d['caught']}  rate {d['rate']:.1%}")
    print(f"  95% CI         : [{d['ci'][0]:.1%}, {d['ci'][1]:.1%}]   floor {PROBE_DET_FLOOR:.0%}")
    print(f"  verdict        : {'PASS' if d['passes'] else 'FAIL (lower bound below floor)'}")
    if d["misses"]:
        print(f"  misses         : {d['misses'][:5]}")

    f = fp_floor()
    print("\nFLOOR #2 - false positive (goldens must PASS)")
    print(f"  clean goldens  : {f['clean']}   stale (content moved): {f['stale']}"
          f"   inadmissible evidence: {f.get('inadmissible', 0)}")
    print(f"  tiers          : {f['tiers']}")
    print(f"  false positives: {f['fp']}  rate {f['rate']:.1%}")
    print(f"  95% CI         : [{f['ci'][0]:.1%}, {f['ci'][1]:.1%}]   ceiling {PROBE_FP_CEILING:.0%}")
    print(f"  verdict        : {'PASS' if f['passes'] else 'FAIL (upper bound above ceiling)'}")
    if f["offenders"]:
        print(f"  offenders      : {f['offenders']}")

    green = d["passes"] and f["passes"]
    print(f"\nFIRST_BATCH_GATE : {'GREEN' if green else 'RED'}")
    if not green:
        # Solved with the SAME Wilson bound the verdict uses. The rule-of-three
        # approximation printed 30, the Wilson test the gate actually applies
        # needs 35, and a target that disagrees with its own test sends you to
        # build five goldens too few and fail again.
        need = next((n for n in range(f["clean"], 4000)
                     if wilson(0, n)[1] <= PROBE_FP_CEILING), None)
        print(f"  floor #2 needs ~{need} clean goldens with zero false positives "
              f"to bound at {PROBE_FP_CEILING:.0%}; have {f['clean']}.")
        print("  The gap is countersigned goldens, not comparator work.")
    json.dump({"detection": d, "false_positive": f, "gate": "GREEN" if green else "RED"},
              open(os.path.join(OUT, "preflight.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
