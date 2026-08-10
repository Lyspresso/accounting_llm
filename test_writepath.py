#!/usr/bin/env python3
"""
Write-path fixture. Lint catches the PATTERN; this catches EVASION.

A direct `open(ledger, "w")` is a lint failure, but lint only sees code it can
pattern-match. An evasion - a shell redirect, a copy, an os.rename, a writer
added under a name the pattern misses - reaches the file anyway. So the fixture
tests the property rather than the syntax: after any write that is not
ledger_io.append_rows, evidence rows must be detectably gone.

Two assertions:
  1. lint reports zero direct writers
  2. an evasive truncating write IS DETECTED (evidence rows lost)
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def evidence_rows(path):
    """Rows carrying a stage - the thing a truncating write destroys."""
    n = 0
    for line in open(path, encoding="utf-8"):
        try:
            if json.loads(line).get("stage"):
                n += 1
        except json.JSONDecodeError:
            pass
    return n


def test_staged_row_does_not_eat_stage0():
    """
    Appending a STAGED row must not delete stage-0 history for the same hash.

    supersede_stage0 was armed by any incoming row carrying a content_hash, so
    one stage-1 `verified` row silently destroyed the stage-0 row beneath it.
    The write-path fixture was GREEN while that was live, because it only ever
    exercised stage-0 supersession. Only the sentinel's cell-monotonicity check
    caught it, and a sentinel is the last line, not the first.
    """
    import tempfile, json, os, importlib
    import ledger_io as L
    with tempfile.TemporaryDirectory() as tmp:
        old_out, old_led = L.OUT, L.LEDGER
        L.OUT = tmp; L.LEDGER = os.path.join(tmp, "ledger.jsonl")
        try:
            L.append_rows([{"content_hash": "H", "id": "x", "status": "unverified"}])
            L.append_rows([{"content_hash": "H", "id": "x", "status": "verified",
                            "stage": 1}])
            rows = L.read_rows()
            s0 = [r for r in rows if not r.get("stage")]
            s1 = [r for r in rows if r.get("stage") == 1]
            ok = len(s0) == 1 and len(s1) == 1
            print(f"  {'ok  ' if ok else 'FAIL'}  staged row preserves stage-0 history "
                  f"(stage0={len(s0)}, stage1={len(s1)})")
            # and the sanctioned path still works: stage-0 supersedes stage-0
            L.append_rows([{"content_hash": "H", "id": "x", "status": "unverified",
                            "reasons": ["regenerated"]}])
            s0b = [r for r in L.read_rows() if not r.get("stage")]
            ok2 = len(s0b) == 1 and s0b[0].get("reasons") == ["regenerated"]
            print(f"  {'ok  ' if ok2 else 'FAIL'}  stage-0 still supersedes stage-0 "
                  f"({len(s0b)} stage-0 row)")
            return ok and ok2
        finally:
            L.OUT, L.LEDGER = old_out, old_led


def main():
    failed = []

    # --- 1. lint ----------------------------------------------------------
    sys.path.insert(0, HERE)
    from ledger_io import lint_writers
    bad = lint_writers()
    if bad:
        failed.append(("lint", bad))
        print(f"  FAIL  lint: {len(bad)} direct ledger writers")
        for f, i, c in bad[:5]:
            print(f"          {f}:{i} {c}")
    else:
        print("  ok    lint: no direct ledger writers outside ledger_io")

    # --- 1b. staged rows must not delete stage-0 history -------------------
    if not test_staged_row_does_not_eat_stage0():
        failed.append(("staged_row_eats_stage0", None))

    # --- 2. evasion detection --------------------------------------------
    with tempfile.TemporaryDirectory() as tmp:
        lp = os.path.join(tmp, "ledger.jsonl")
        shutil.copy(os.path.join(OUT, "ledger.jsonl"), lp)
        before = evidence_rows(lp)

        # EVASION: a truncating write that no import-based guard can prevent.
        # This is what a shell redirect or a new careless writer does.
        with open(lp, "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"content_hash": "x", "id": "X#00",
                                 "status": "unverified"}) + "\n")
        after = evidence_rows(lp)

        detected = after < before
        print(f"  {'ok  ' if detected else 'FAIL'}  evasive truncating write DETECTED "
              f"(evidence rows {before} -> {after})")
        if not detected:
            failed.append(("evasion", (before, after)))

        # --- 3. the sanctioned path preserves evidence --------------------
        shutil.copy(os.path.join(OUT, "ledger.jsonl"), lp)
        import ledger_io
        real = ledger_io.LEDGER
        ledger_io.LEDGER = lp
        try:
            ledger_io.append_rows([{"content_hash": "y", "id": "Y#00",
                                    "status": "unverified"}])
            kept = evidence_rows(lp)
        finally:
            ledger_io.LEDGER = real
        ok = kept == before
        print(f"  {'ok  ' if ok else 'FAIL'}  ledger_io.append_rows preserved evidence "
              f"({before} -> {kept})")
        if not ok:
            failed.append(("append_rows", (before, kept)))

    print(f"\nwrite-path fixture: {'GREEN' if not failed else 'RED'}")
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
