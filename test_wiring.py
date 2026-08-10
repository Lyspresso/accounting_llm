#!/usr/bin/env python3
"""
Wiring probe — every gated treatment note must be present in a FRESHLY GENERATED
solver context for each family it governs, every session.

The failure this exists for: the LO 11-8 note reached the dual harness and never
reached trim, because prompts were emitted by ad-hoc inline heredocs with no
shared builder. A verbal "the note is wired" was wrong for the production
harness and would have run 12 items under the treatment the note forbids.

Anchoring rule: presence is asserted against the INSTRUCTION region only. The
Cedar Ridge stem itself contains "donated" and "$3,000 cash for legal title
transfer" - a stem-satisfiable check would have passed while trim carried no
rule at all.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_solver_prompt import (  # noqa: E402
    build, instruction_region, question_region, load_notes, notes_for,
)

# Each gated note: the LO it governs and a phrase that MUST appear in the rules.
GATED = {
    "lo_11_8_donated_assets": {
        "lo_pattern": r"\bLO\s*11-8\b",
        "must_contain": ["contribution revenue", "net of those costs"],
        "must_not_be_stem_satisfiable": ["donated", "legal title transfer"],
    },
}


def main():
    qs = [json.loads(l) for l in open(os.path.join(HERE, "out", "questions.jsonl"),
                                      encoding="utf-8")]
    notes = {n["id"]: n for n in load_notes()}
    failed = []

    for note_id, spec in GATED.items():
        if note_id not in notes:
            failed.append((note_id, "note missing from treatment_notes.yaml"))
            print(f"  FAIL  {note_id}: not in the treatment library")
            continue

        fam = [q for q in qs if re.search(spec["lo_pattern"],
                                          " ".join(q.get("concepts") or []) + q["stem"], re.I)]
        if not fam:
            failed.append((note_id, "no family members found"))
            print(f"  FAIL  {note_id}: no items match {spec['lo_pattern']}")
            continue

        # EVERY solver path, not just the primary one. The dual harness carried
        # the LO 11-8 note while trim did not, and that asymmetry manufactured a
        # construal split that was reported as a solver-quality finding. A probe
        # that checks one path certifies nothing about the others.
        ROLES = ("primary", "dual", "remake")
        bad = 0
        for q in fam:
            for role in ROLES:
                prompt = build(q["id"], q["stem"], "/tmp/probe", role=role)
                ir = instruction_region(prompt).lower()
                if not all(p in ir for p in spec["must_contain"]):
                    bad += 1
        total = len(fam) * len(ROLES)
        if bad:
            failed.append((note_id, f"{bad}/{total} generated contexts missing the rule"))
            print(f"  FAIL  {note_id}: {bad}/{total} contexts missing the rule")
        else:
            print(f"  ok    {note_id}: present in {total}/{total} contexts "
                  f"({len(fam)} items x {len(ROLES)} roles)")

        # PARITY: the instruction region must be IDENTICAL across roles. A role
        # may vary its framing line; it may never vary the rules.
        sample = fam[0]
        regions = {r: instruction_region(build(sample["id"], sample["stem"],
                                               "/tmp/probe", role=r)) for r in ROLES}
        base_r = regions["primary"]
        parity = all(v == base_r for v in regions.values())
        print(f"  {'ok  ' if parity else 'FAIL'}  {note_id}: instruction region "
              f"identical across {len(ROLES)} solver roles")
        if not parity:
            failed.append((note_id, "solver-context asymmetry across roles"))

        # anti-cheat: the check must not be satisfiable by stem text alone
        sample = fam[0]
        prompt = build(sample["id"], sample["stem"], "/tmp/probe")
        qr = question_region(prompt).lower()
        stem_only = [p for p in spec["must_contain"] if p in qr]
        if stem_only:
            failed.append((note_id, f"stem-satisfiable: {stem_only}"))
            print(f"  FAIL  {note_id}: phrase(s) {stem_only} appear in the QUESTION region")
        else:
            print(f"  ok    {note_id}: not stem-satisfiable "
                  f"(stem carries {spec['must_not_be_stem_satisfiable']} but no rule)")

    print(f"\nwiring probe: {'GREEN' if not failed else 'RED'}")
    if failed:
        for n, why in failed:
            print(f"   {n}: {why}")
        sys.exit(1)


if __name__ == "__main__":
    main()
