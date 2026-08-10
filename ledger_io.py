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



# ---------------------------------------------------------------------------
# TERMINAL WRITE GATE (ORDER-002 item 2)
# ---------------------------------------------------------------------------
# `verified` and `needs_human` are PIPELINE terminals: they mean Stage-3
# adversary has run for flagged items and the label sits under a CERTIFIED
# floor. Neither is true while the LAUNCH gate is RED, so a terminal write under
# RED is not a judgement call - it is a category error, and it happened once by
# a route nobody had thought to close.
#
# Enforcement lives HERE, in the single write path, rather than in the callers
# that mint verdicts. A rule enforced in one caller is not enforced: preflight
# and fp_taxonomy proved that by disagreeing about the same item by 32 findings.
#
# The override is a FILE, not a flag, so an exception is a committed artifact
# with an author and a diff, and never an argument someone passed once.

TERMINAL_STATES = ("verified", "needs_human")
OVERRIDE_DIR = os.path.join(HERE, "comms", "operator")
OVERRIDE_PREFIX = "OVERRIDE-terminal"


class TerminalWriteRefused(Exception):
    """Raised when a terminal row is written while the LAUNCH gate is RED."""


def launch_gate():
    """
    ("RED"|"GREEN", source). Unknown counts as RED: a gate that cannot be read
    is not a green light, and the safe default is the restrictive one.
    """
    p = os.path.join(OUT, "preflight.json")
    if not os.path.exists(p):
        return "RED", "no out/preflight.json - unknown gate treated as RED"
    try:
        return json.load(open(p, encoding="utf-8")).get("gate", "RED"), p
    except (json.JSONDecodeError, OSError):
        return "RED", f"{p} unreadable - treated as RED"


def terminal_override():
    """An explicit, committed operator override file, or None."""
    if not os.path.isdir(OVERRIDE_DIR):
        return None
    for fn in sorted(os.listdir(OVERRIDE_DIR)):
        if fn.startswith(OVERRIDE_PREFIX):
            return os.path.join(OVERRIDE_DIR, fn)
    return None


def check_terminal_writes(new_rows):
    """Refuse terminal rows under a RED gate. Returns the rows unchanged."""
    terminals = [r for r in new_rows if r.get("status") in TERMINAL_STATES]
    if not terminals:
        return new_rows
    gate, src = launch_gate()
    if gate == "GREEN":
        return new_rows
    ov = terminal_override()
    if ov:
        return new_rows
    ids = ", ".join(sorted({str(r.get("id")) for r in terminals})[:5])
    raise TerminalWriteRefused(
        f"REFUSED: {len(terminals)} terminal row(s) [{ids}] while LAUNCH gate is "
        f"{gate} (per {src}). Terminal states require a certified floor. To "
        f"override, commit a file named {OVERRIDE_PREFIX}*.md in "
        f"comms/operator/ stating the authority."
    )


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
    check_terminal_writes(new_rows)
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
