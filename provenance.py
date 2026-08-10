#!/usr/bin/env python3
"""
Provenance — captured at WRITE time, never applied retroactively.

The previous version stamped outputs with the CURRENT pack-notes version at the
moment of stamping, not the version in force when the output was generated. It
therefore certified a stale trim cache as current, the audit could not see it,
and a solver-quality conclusion was drawn from a context-asymmetric comparison.
A provenance system that records what is true now rather than what was true at
generation launders staleness instead of catching it.

Two modes only:

    capture(...)      write-time, immutable. The generator calls this.
    reconstruct()     for outputs that predate capture(). Derives the context
                      from run logs and script history and labels the result
                      `reconstructed: true` so it is never mistaken for a
                      first-hand record.

Admissibility is PER ITEM: a pack-notes change matters only if a note that
governs THAT item changed. An item no note touches is unaffected by note
versions, and marking it stale would be noise.
"""

import argparse
import glob
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)

CURRENT_PACK_NOTES = "pack-2026-08-07b"      # LO 11-8 netting note present
CURRENT_COMPARATOR = "3.8"
CANON_VERSION = "canon-1"

# Reconstruction table: evidence dir -> the context actually in force when that
# directory's outputs were generated. Derived from the generating scripts, which
# are on disk and were inspected line by line.
RECONSTRUCTION = {
    "evidence": {
        "harness_version": "baseline-1",
        "generated_by": "stage1-batch1/batch2 scripts",
        "pack_notes_version": "pack-2026-08-07a-PRE-NOTE",
        "notes_present": [],
        "why": "read STAGE1_SOLVER_INSTRUCTIONS.md before the LO 11-8 note existed",
    },
    "evidence_parity": {
        "harness_version": "trim-1",
        "generated_by": "parity50.js",
        "pack_notes_version": "pack-2026-08-07a-PRE-NOTE",
        "notes_present": [],
        "why": "hand-written rule block; grep confirms no LO 11-8 rule string",
    },
    "evidence_trim": {
        "harness_version": "trim-1",
        "generated_by": "trim_ab.js",
        "pack_notes_version": "pack-2026-08-07a-PRE-NOTE",
        "notes_present": [],
        "why": "hand-written rule block; also lacked the coverage instruction",
    },
    "evidence_dual": {
        "harness_version": "dual-1",
        "generated_by": "dual.js",
        "pack_notes_version": "pack-2026-08-07a-ASYMMETRIC",
        "notes_present": ["lo_11_8_donated_assets"],
        "why": "hand-written rule block that DID carry the LO 11-8 note",
    },
    "evidence_dual2": {
        "harness_version": "dual-1",
        "generated_by": "dual2.js via build_solver_prompt(role='dual')",
        "pack_notes_version": CURRENT_PACK_NOTES,
        "notes_present": ["lo_11_8_donated_assets"],
        "why": "built by the shared builder; rule set invariant across roles",
    },
}


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_questions():
    return {q["id"]: q for q in (json.loads(l) for l in
            open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}


def notes_governing(stem):
    """Which treatment notes apply to this item. Empty => note versions are moot."""
    import build_solver_prompt as B
    return [n["id"] for n in B.notes_for(stem)]


def capture(evidence_dir, item_id, stem, harness_version,
            pack_notes_version=CURRENT_PACK_NOTES):
    """
    WRITE-TIME stamp. Called by the generator, at generation, once.
    Refuses to overwrite: a provenance record is immutable.
    """
    p = os.path.join(evidence_dir, "provenance.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    rec = {"id": item_id, "harness_version": harness_version,
           "stem_hash": sha(stem), "pack_notes_version": pack_notes_version,
           "comparator_version": CURRENT_COMPARATOR, "canon_version": CANON_VERSION,
           "notes_governing": notes_governing(stem),
           "captured_at_write_time": True, "reconstructed": False}
    os.makedirs(evidence_dir, exist_ok=True)
    json.dump(rec, open(p, "w", encoding="utf-8"), indent=1)
    return rec


def reconstruct(apply_it=False):
    """
    Derive provenance for pre-capture outputs from the generating script, and
    label it `reconstructed`. Never claims to be a first-hand record.
    """
    qs = load_questions()
    out, changed = [], 0
    for sub, ctx in RECONSTRUCTION.items():
        base = os.path.join(OUT, sub)
        if not os.path.isdir(base):
            continue
        for d in sorted(os.listdir(base)):
            sp = os.path.join(base, d, "solver_output.json")
            if not os.path.exists(sp):
                continue
            parts = d.rsplit("_", 1)
            qid = f"{parts[0]}#{parts[1]}" if len(parts) == 2 else d
            q = qs.get(qid)
            if not q:
                continue
            p = os.path.join(base, d, "provenance.json")
            prior = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None
            rec = {"id": qid, "harness_version": ctx["harness_version"],
                   "stem_hash": sha(q["stem"]),
                   "pack_notes_version": ctx["pack_notes_version"],
                   "notes_present_at_generation": ctx["notes_present"],
                   "notes_governing": notes_governing(q["stem"]),
                   "generated_by": ctx["generated_by"], "why": ctx["why"],
                   "captured_at_write_time": False, "reconstructed": True}
            was = (prior or {}).get("pack_notes_version")
            if was != rec["pack_notes_version"]:
                changed += 1
                rec["retroactive_stamp_replaced"] = was
            out.append((sub, qid, was, rec["pack_notes_version"]))
            if apply_it:
                json.dump(rec, open(p, "w", encoding="utf-8"), indent=1)
    return out, changed


def admissible(prov, q):
    """
    (ok, reason). Pack-notes staleness is PER ITEM: it bites only when a note
    that GOVERNS this item was absent at generation.
    """
    if prov.get("stem_hash") != sha(q["stem"]):
        return (False, "STEM_CHANGED - re-solve required")
    gov = set(prov.get("notes_governing") or [])
    present = set(prov.get("notes_present_at_generation")
                  if prov.get("reconstructed") else gov)
    missing = gov - present
    if missing:
        return (False, f"PACK_NOTES_STALE - governed by {sorted(missing)}, "
                       f"absent at generation")
    return (True, "admissible")


def audit():
    qs = load_questions()
    rows, tally = [], {"admissible": 0, "PACK_NOTES_STALE": 0,
                       "STEM_CHANGED": 0, "unstamped": 0}
    for sub in RECONSTRUCTION:
        base = os.path.join(OUT, sub)
        if not os.path.isdir(base):
            continue
        for d in sorted(os.listdir(base)):
            sp = os.path.join(base, d, "solver_output.json")
            pp = os.path.join(base, d, "provenance.json")
            if not os.path.exists(sp):
                continue
            parts = d.rsplit("_", 1)
            qid = f"{parts[0]}#{parts[1]}" if len(parts) == 2 else d
            q = qs.get(qid)
            if not q:
                continue
            if not os.path.exists(pp):
                tally["unstamped"] += 1
                continue
            prov = json.load(open(pp, encoding="utf-8"))
            ok, why = admissible(prov, q)
            key = "admissible" if ok else why.split(" ")[0]
            tally[key] = tally.get(key, 0) + 1
            if not ok:
                rows.append((sub, qid, why))
    return tally, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reconstruct", action="store_true")
    ap.add_argument("--audit", action="store_true")
    a = ap.parse_args()
    if a.reconstruct:
        out, changed = reconstruct(apply_it=True)
        print(f"reconstructed provenance for {len(out)} outputs")
        print(f"  retroactive stamps REPLACED: {changed}   <- blast radius")
        import collections
        by = collections.Counter(s for s, _, _, _ in out)
        for k, v in by.items():
            print(f"    {k:18s} {v}")
    if a.audit:
        tally, rows = audit()
        print("\n=== ADMISSIBILITY AUDIT (per-item note scoping) ===")
        for k, v in tally.items():
            print(f"  {k:18s} {v}")
        for sub, qid, why in rows[:15]:
            print(f"    {qid:14s} {sub:18s} {why}")


if __name__ == "__main__":
    main()
