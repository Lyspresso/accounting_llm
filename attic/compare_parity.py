#!/usr/bin/env python3
"""
n=50 parity test — scores BOTH harnesses under the same KEY_SILENT-aware
comparator, so the fuller reporter is not penalised for reporting more.

Adoption criteria, in rank order:
  1. zero UNADJUDICATED verdict flips
  2. canary-clean
  3. required-figure coverage >= baseline
  4. cost ratio (informational only)
"""

import json
import math
import os
import random
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compare_stage1_v3 as C  # noqa: E402

COMPARATOR_VERSION = "3.5"
HARNESS_BASE, HARNESS_TRIM = "baseline-1", "trim-1"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

REQ_BLOCK = re.compile(r"\*\*Required[^*]{0,24}:\*\*(.*?)(?=\n\*\*(?:Answer|Scenario|LO|Concept|Question)|\Z)",
                       re.S | re.I)
PART = re.compile(r"^\s*\(?([a-h])[\.\)]\s", re.M)


def required_parts(stem):
    parts = set()
    for m in REQ_BLOCK.finditer(stem):
        parts.update(x.lower() for x in PART.findall(m.group(1)))
    if not parts and re.search(r"\*\*Required", stem, re.I):
        parts.add("a")          # a single unlettered requirement
    return parts


def covered_parts(sol):
    got = set()
    for a in sol.get("answers") or []:
        m = re.match(r"\s*\(?([a-h])\b", str(a.get("label") or ""))
        if m:
            got.add(m.group(1).lower())
    for je in sol.get("journal_entries") or []:
        m = re.match(r"\s*\(?([a-h])\b", str(je.get("part") or ""))
        if m:
            got.add(m.group(1).lower())
    return got


def score(sol, q, known, amap):
    """
    Straight pass-through to comparator v3.4.

    The previous version downgraded a SOLVER_MISMATCH to KEY_SILENT_SUSPECTED
    when ANOTHER answer in the same lettered part happened to match. That was
    order-dependent and unsound: on agent_032#01 the baseline reported one
    part-(d) figure (unmatched -> hard -> failed) while the trim reported five,
    one of which matched, sweeping the identical figure into the soft bucket ->
    passed. The rule manufactured the flip on its own. v3.4 decides KEY_SILENT
    deterministically instead, by subset-sum over the key's own stated figures.
    """
    issues, _scope = C.compare(sol, q, known, amap)
    hard = [i for i in issues if i["kind"] in C.HARD]
    return issues, ("failed" if hard else "machine_passed")


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def main():
    rng = random.Random(343)
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}
    known, amap = C.load_known(), C.load_alias_map(False)
    items = json.load(open(os.path.join(OUT, "parity50.json"), encoding="utf-8"))

    flips, rows = [], []
    cov = {HARNESS_BASE: [], HARNESS_TRIM: []}
    verd = {HARNESS_BASE: [], HARNESS_TRIM: []}
    canary_run = canary_breach = 0
    silent = {HARNESS_BASE: 0, HARNESS_TRIM: 0}

    for it in items:
        qid = it["id"]
        q = qs[qid]
        req = required_parts(q["stem"])
        paths = {HARNESS_BASE: os.path.join(OUT, "evidence", qid.replace("#", "_"),
                                            "solver_output.json"),
                 HARNESS_TRIM: os.path.join(it["dir"], "solver_output.json")}
        r = {"id": qid, "ch": it["ch"], "required_parts": sorted(req)}
        for h, p in paths.items():
            if not os.path.exists(p):
                r[h] = {"verdict": "MISSING"}
                continue
            try:
                sol = json.load(open(p, encoding="utf-8"))
            except json.JSONDecodeError:
                r[h] = {"verdict": "BADJSON"}
                continue
            iss, v = score(sol, q, known, amap)
            c = covered_parts(sol)
            covfrac = len(req & c) / len(req) if req else 1.0
            cov[h].append(covfrac)
            verd[h].append(v)
            silent[h] += sum(1 for i in iss if i["kind"] in ("KEY_SILENT_DERIVED", "JE_AGGREGATED"))
            r[h] = {"verdict": v, "coverage": round(covfrac, 3),
                    "n_answers": len(sol.get("answers") or []),
                    "hard": [i for i in iss if i["kind"] in C.HARD][:6]}

            # canary: an off-manifold value no correct derivation should produce
            planted = round(rng.uniform(1, 9) * 1111.11, 2)
            canary_run += 1
            vals = [C.as_number(a.get("value")) for a in sol.get("answers") or []]
            if any(x is not None and abs(x - planted) <= 0.01 for x in vals):
                canary_breach += 1

        vb = r.get(HARNESS_BASE, {}).get("verdict")
        vt = r.get(HARNESS_TRIM, {}).get("verdict")
        if vb and vt and vb != vt:
            flips.append({"id": qid, "ch": it["ch"], "baseline": vb, "trim": vt,
                          "baseline_cov": r[HARNESS_BASE].get("coverage"),
                          "trim_cov": r[HARNESS_TRIM].get("coverage"),
                          "trim_hard": r[HARNESS_TRIM].get("hard"),
                          "baseline_hard": r[HARNESS_BASE].get("hard")})
        rows.append(r)

    json.dump({"comparator_version": COMPARATOR_VERSION, "rows": rows, "flips": flips},
              open(os.path.join(OUT, "parity50_results.json"), "w"), indent=1)

    print(f"n = {len(items)}   comparator v{COMPARATOR_VERSION}\n")
    print(f"{'':>12} {'passed':>8} {'failed':>8} {'coverage':>10} {'key_silent':>11}")
    for h in (HARNESS_BASE, HARNESS_TRIM):
        p = sum(1 for v in verd[h] if v == "machine_passed")
        f = sum(1 for v in verd[h] if v == "failed")
        mc = statistics.mean(cov[h]) if cov[h] else 0
        print(f"{h:>12} {p:>8} {f:>8} {mc:>9.1%} {silent[h]:>11}")
    lo, hi = wilson(sum(1 for v in verd[HARNESS_TRIM] if v == "machine_passed"),
                    len(verd[HARNESS_TRIM]))
    print(f"\n  trim pass-rate 95% CI : {lo:.0%} - {hi:.0%}")
    print(f"  canaries              : {canary_breach} breaches / {canary_run} run")
    print(f"  UNADJUDICATED FLIPS   : {len(flips)}")
    for fl in flips:
        print(f"    {fl['id']:14s} ch{fl['ch']:<3} base={fl['baseline']:<14s} "
              f"trim={fl['trim']:<14s} cov {fl['baseline_cov']}->{fl['trim_cov']}")


if __name__ == "__main__":
    main()
