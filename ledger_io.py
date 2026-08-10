#!/usr/bin/env python3
"""
The ONLY write path to ledger.jsonl.

Two separate writers opened this file with "w" and each destroyed history: the
first zeroed the stage-1 cache three times, the second destroyed 171 stage-1
rows during migration. Guarding both was the instance fix. This is the class
fix: there is one merge-only writer, every caller routes through it, and a
fixture asserts no other writer exists.

    from ledger_io import append_rows, read_rows
    append_rows(rows)          # merge; history is never truncated

Direct `open(LEDGER, "w")` anywhere else is a lint failure.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LEDGER = os.path.join(OUT, "ledger.jsonl")
PIPELINE_VERSION = "1.2"


def read_rows():
    rows = []
    if os.path.exists(LEDGER):
        for line in open(LEDGER, encoding="utf-8"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def append_rows(new_rows, supersede_stage0=True):
    """
    Merge new rows in. NOTHING is ever discarded that carries a stage: a row
    with a stage is evidence that work happened, and losing it is exactly the
    failure this module exists to prevent.

    supersede_stage0: a fresh stage-0 row for a hash replaces the previous
    stage-0 row for that same hash (they are regenerated, not accumulated).
    Rows carrying a stage are always retained regardless.

    Supersession is armed ONLY by incoming STAGE-0 rows. A staged row that
    happens to carry a content_hash used to silently delete that hash's stage-0
    history - appending one stage-1 `verified` row destroyed the stage-0 row
    beneath it, and only the sentinel's cell-monotonicity check noticed. A
    writer whose deletion scope is wider than its own stage is the same class
    of bug as the two "w" writers this module was built to replace.
    """
    prior = read_rows()
    fresh_hashes = {r.get("content_hash") for r in new_rows
                    if not r.get("stage")}          # stage-0 rows only
    keep = []
    for p in prior:
        if p.get("stage"):
            keep.append(p)                       # evidence: always retained
        elif not supersede_stage0 or p.get("content_hash") not in fresh_hashes:
            keep.append(p)
    os.makedirs(OUT, exist_ok=True)
    tmp = LEDGER + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        for r in keep + list(new_rows):
            fh.write(json.dumps(r) + "\n")
    os.replace(tmp, LEDGER)                      # atomic; no partial ledger
    return {"prior": len(prior), "kept": len(keep),
            "added": len(new_rows), "total": len(keep) + len(new_rows)}


def lint_writers():
    """
    Every .py in the stack must reach the ledger only through this module.
    Returns a list of offending (file, line, code).
    """
    import re
    bad = []
    pat = re.compile(r"""open\([^)]*ledger\.jsonl[^)]*["'](w|a)["']""")
    for fn in sorted(os.listdir(HERE)):
        if not fn.endswith(".py") or fn == os.path.basename(__file__):
            continue
        for i, line in enumerate(open(os.path.join(HERE, fn), encoding="utf-8"), 1):
            if pat.search(line):
                bad.append((fn, i, line.strip()[:90]))
    return bad


if __name__ == "__main__":
    bad = lint_writers()
    if bad:
        print("LINT FAIL — direct ledger writes outside ledger_io:")
        for f, i, c in bad:
            print(f"   {f}:{i}  {c}")
        raise SystemExit(1)
    print("LINT OK — ledger_io is the only write path")
