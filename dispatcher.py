#!/usr/bin/env python3
"""
Dispatcher — the single gate every item passes through before it runs.

The FORMAT_DRIFT pause was advisory and enforced nothing: seven packs were
"paused" while agent_254#00 and agent_326#02 ran anyway, because Stage 1
selection drew from Class A without consulting pack status. A pause that does
not refuse work is a comment.

Every launch path calls admit() and honours the refusal. The enforcement probe
deliberately pauses a pack and asserts a refusal, so the gate cannot silently
die again.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
OVERRIDE = os.path.join(OUT, "pack_status_override.json")


def pack_status():
    """pack_id -> reason, for every pack currently refused."""
    st = {}
    p = os.path.join(OUT, "pack_profiles.json")
    if os.path.exists(p):
        prof = json.load(open(p, encoding="utf-8"))
        for pid in prof.get("format_drift", []):
            st[pid] = "FORMAT_DRIFT"
    if os.path.exists(OVERRIDE):                      # test/manual pauses
        for pid, why in json.load(open(OVERRIDE, encoding="utf-8")).items():
            st[pid] = why
    return st


_GATE_CACHE = {}


def gated_families():
    """
    Families whose treatment note must be wired before they run. Empty once the
    wiring probe is green for that note - the gate is the probe, not a date.
    """
    # Memoised: admit() is called per item, and recomputing this rebuilt every
    # prompt in the corpus on each call - O(n^2) and minutes long on 1,828 items.
    if _GATE_CACHE:
        return _GATE_CACHE["v"]
    try:
        sys.path.insert(0, HERE)
        from test_wiring import GATED
        import build_solver_prompt as B
        import re
        out = {}
        qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                          encoding="utf-8")]
        for note_id, spec in GATED.items():
            for q in qs:
                blob = " ".join(q.get("concepts") or []) + q["stem"]
                if not re.search(spec["lo_pattern"], blob, re.I):
                    continue
                ir = B.instruction_region(B.build(q["id"], q["stem"], "/tmp/g")).lower()
                if not all(t in ir for t in spec["must_contain"]):
                    out[q["id"]] = f"TREATMENT_NOTE_UNWIRED:{note_id}"
        _GATE_CACHE["v"] = out
        return out
    except Exception as e:                            # never fail open (2.6:
                                                      # DELIBERATE — any error poisons
                                                      # the gate cache and refuses work)
        _GATE_CACHE["v"] = {"__error__": f"gate check failed: {e}"}
        return _GATE_CACHE["v"]


def admit(item_id):
    """(ok, reason). A refusal is a refusal - callers must not proceed."""
    pid = item_id.split("#")[0]
    st = pack_status()
    if pid in st:
        return (False, f"pack {pid} is paused: {st[pid]}")
    g = gated_families()
    if "__error__" in g:
        return (False, g["__error__"])                # fail closed
    if item_id in g:
        return (False, g[item_id])
    return (True, "admitted")


def admit_all(item_ids):
    ok, refused = [], []
    for i in item_ids:
        a, why = admit(i)
        (ok if a else refused).append((i, why))
    return ok, refused


if __name__ == "__main__":
    ids = sys.argv[1:]
    if not ids:
        qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                          encoding="utf-8")]
        ids = [q["id"] for q in qs]
    ok, refused = admit_all(ids)
    print(f"admitted : {len(ok)}")
    print(f"refused  : {len(refused)}")
    for i, why in refused[:10]:
        print(f"   {i:14s} {why}")
