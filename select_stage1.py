#!/usr/bin/env python3
"""
Stage 1 selection + evidence scaffolding.

Picks the pilot questions, scores every Class A item for risk (the full run
processes in descending risk order), and writes each selected item's STEM ONLY
into OUTPUT_DIR/evidence/{id}/stem.md.

The stem file is the solver's entire world. questions.jsonl holds the solution
and must never be handed to a solver.

Usage:
    python3 select_stage1.py --pilot 100 --batch-size 50
"""

import argparse
import json
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
EVID = os.path.join(OUT, "evidence")

STANDARD_SENSITIVE = re.compile(
    r"revenue recognition|ASC\s*606|lease|ASC\s*842|deferred tax|income tax|ASC\s*740|"
    r"stock comp|share-based|ASC\s*718|CECL|ASC\s*326",
    re.I,
)
APPENDIX = re.compile(r"appendix", re.I)


def risk_score(q, drift_packs):
    """Weights from the budget prompt's Stage 2 risk model; recorded per item."""
    s, why = 0, []
    blob = f"{q['stem']} {' '.join(q['concepts'])} {q['standard_context']}"
    if STANDARD_SENSITIVE.search(blob):
        s += 3; why.append("standard-sensitive")
    if not q["citations"]:
        s += 2; why.append("no citation")
    if q["pack_id"] in drift_packs:
        s += 1; why.append("pack FORMAT_DRIFT")
    if APPENDIX.search(blob):
        s += 1; why.append("appendix")
    if not q["standard_context"]:
        s += 1; why.append("empty standard_context")
    if "UNKNOWN_ACCOUNT" in q["flags"]:
        s += 1; why.append("unknown account")
    return s, why


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", type=int, default=100)
    ap.add_argument("--batch-size", type=int, default=50)
    ap.add_argument("--seed", type=int, default=343)
    args = ap.parse_args()

    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8")]
    profiles = json.load(open(os.path.join(OUT, "pack_profiles.json"), encoding="utf-8"))
    drift = set(profiles.get("format_drift", []))

    classA = [q for q in qs if q["type"] in ("journal_entry", "ledger", "numeric")
              and q["status"] != "failed"]

    for q in classA:
        q["risk_score"], q["risk_why"] = risk_score(q, drift)

    # The pilot's job is an unbiased cost-per-question number, so sample it
    # stratified across packs rather than risk-first. The FULL run processes in
    # descending risk order, as the budget prompt specifies.
    rng = random.Random(args.seed)
    by_pack = {}
    for q in classA:
        by_pack.setdefault(q["pack_id"], []).append(q)
    packs = sorted(by_pack)
    rng.shuffle(packs)
    picked, i = [], 0
    while len(picked) < min(args.pilot, len(classA)):
        p = packs[i % len(packs)]
        pool = by_pack[p]
        if pool:
            picked.append(pool.pop(rng.randrange(len(pool))))
        i += 1

    os.makedirs(EVID, exist_ok=True)
    manifest = []
    for n, q in enumerate(picked):
        d = os.path.join(EVID, q["id"].replace("#", "_"))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "stem.md"), "w", encoding="utf-8") as fh:
            fh.write(q["stem"].rstrip() + "\n")
        manifest.append({
            "id": q["id"], "dir": d, "pack_id": q["pack_id"], "type": q["type"],
            "risk_score": q["risk_score"], "risk_why": q["risk_why"],
            "batch": n // args.batch_size + 1,
            "n_je_lines": q["n_je_lines"], "concepts": q["concepts"][:2],
        })

    with open(os.path.join(OUT, "stage1_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump({"pilot": len(manifest), "batch_size": args.batch_size,
                   "seed": args.seed, "items": manifest}, fh, indent=1)

    # risk ranking for the eventual full run
    ranked = sorted(classA, key=lambda q: -q["risk_score"])
    with open(os.path.join(OUT, "stage1_risk_order.json"), "w", encoding="utf-8") as fh:
        json.dump([{"id": q["id"], "risk_score": q["risk_score"], "why": q["risk_why"]}
                   for q in ranked], fh, indent=1)

    nb = max(m["batch"] for m in manifest)
    print(f"Class A eligible : {len(classA)}")
    print(f"pilot selected   : {len(manifest)}  across {len(set(m['pack_id'] for m in manifest))} packs")
    print(f"batches          : {nb} x {args.batch_size}")
    print(f"risk score       : min {min(m['risk_score'] for m in manifest)} / "
          f"max {max(m['risk_score'] for m in manifest)}")
    print(f"stems written to : {EVID}/<id>/stem.md")


if __name__ == "__main__":
    main()
