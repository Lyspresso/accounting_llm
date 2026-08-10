#!/usr/bin/env python3
"""
Provenance fixture — the test that would have caught the laundering.

An output generated under an OLD pack version must be flagged inadmissible.
The previous stamper wrote the CURRENT version onto historical outputs, so a
stale trim cache passed the audit and a solver-quality conclusion was drawn
from a context-asymmetric comparison. Injecting a synthetic old-version output
is the direct test of that property.
"""
import json, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import provenance as P


def main():
    qs = P.load_questions()
    failed = []

    # a note-GOVERNED item generated before the note existed -> inadmissible
    gov = next((q for q in qs.values() if P.notes_governing(q["stem"])), None)
    if gov is None:
        print("  FAIL  no note-governed item in the corpus to test with")
        sys.exit(1)
    old = {"id": gov["id"], "harness_version": "trim-1",
           "stem_hash": P.sha(gov["stem"]),
           "pack_notes_version": "pack-OLD",
           "notes_present_at_generation": [],           # note absent then
           "notes_governing": P.notes_governing(gov["stem"]),
           "reconstructed": True}
    ok, why = P.admissible(old, gov)
    t1 = (not ok) and "PACK_NOTES_STALE" in why
    print(f"  {'ok  ' if t1 else 'FAIL'}  old-pack output on a GOVERNED item -> "
          f"{'flagged: ' + why if not ok else 'ADMITTED (laundered)'}")
    if not t1:
        failed.append("governed")

    # an UNGOVERNED item under the same old version -> admissible (not noise)
    ung = next((q for q in qs.values() if not P.notes_governing(q["stem"])), None)
    old2 = dict(old, id=ung["id"], stem_hash=P.sha(ung["stem"]),
                notes_governing=[], notes_present_at_generation=[])
    ok2, why2 = P.admissible(old2, ung)
    print(f"  {'ok  ' if ok2 else 'FAIL'}  old-pack output on an UNGOVERNED item -> "
          f"{why2}")
    if not ok2:
        failed.append("ungoverned")

    # a stem change always forfeits, regardless of notes
    bad = dict(old, stem_hash="deadbeef", notes_present_at_generation=old["notes_governing"])
    ok3, why3 = P.admissible(bad, gov)
    t3 = (not ok3) and "STEM_CHANGED" in why3
    print(f"  {'ok  ' if t3 else 'FAIL'}  changed stem -> {why3}")
    if not t3:
        failed.append("stem")

    # capture() is immutable: a second call must not overwrite
    with tempfile.TemporaryDirectory() as tmp:
        a = P.capture(tmp, gov["id"], gov["stem"], "trim-1", "pack-FIRST")
        b = P.capture(tmp, gov["id"], gov["stem"], "trim-1", "pack-SECOND")
        t4 = a["pack_notes_version"] == b["pack_notes_version"] == "pack-FIRST"
        print(f"  {'ok  ' if t4 else 'FAIL'}  capture() immutable "
              f"(second call kept {b['pack_notes_version']})")
        if not t4:
            failed.append("immutable")

    print(f"\nprovenance fixture: {'GREEN' if not failed else 'RED'}")
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
