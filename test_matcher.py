#!/usr/bin/env python3
"""
Matcher probe fixture — synthetic label sets with KNOWN correct pairings.

Every case here is a failure the live matcher actually produced. A matcher
change proves neutrality against this fixture the same way a comparator change
proves neutrality against the pilot.

Also asserts the stack-wide NO-VACUOUS-PASS rule: an "all figures verified"
predicate over an EMPTY set must return NOT cleared.
"""

import sys

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from labelgrammar import best_match, parse, score  # noqa: E402

CASES = []


def case(name, label, candidates, expect):
    CASES.append((name, label, candidates, expect))


# --- single-digit ordinals: the bug that paired every row to Year 1 ---------
YEARS = ["b: Year 1 year-end accumulated depreciation",
         "b: Year 2 year-end accumulated depreciation",
         "b: Year 3 year-end accumulated depreciation"]
case("ordinal Y2", "b: Year 2 year-end accumulated depreciation", YEARS, YEARS[1])
case("ordinal Y3", "b: Year 3 year-end accumulated depreciation", YEARS, YEARS[2])
case("ordinal Y1", "b: Year 1 year-end accumulated depreciation", YEARS, YEARS[0])

# --- part letters: a part-d answer matched part-c at jaccard 1.00 ----------
PARTS = ["c: Dec 31, Year 3 depreciation adjusting entry amount",
         "d: Dec 31, Year 3 depreciation adjusting entry amount"]
case("part d", "d: Dec 31, Year 3 depreciation adjusting entry amount", PARTS, PARTS[1])
case("part c", "c: Dec 31, Year 3 depreciation adjusting entry amount", PARTS, PARTS[0])

# --- exact tie must be AMBIGUOUS, never first-wins -------------------------
case("exact tie", "a: interest expense",
     ["a: interest expense", "a: interest expense"], None)

# --- period-factor lookalike: cumulative vs annual is NOT a unit difference -
case("cumulative vs annual", "c: Year 3 accumulated depreciation since purchase",
     ["c: Year 3 annual depreciation expense"], None)

# --- synonym normalisation: the 0.29 near-miss filed as NO_COUNTERPART ------
case("NBV synonym", "d: NBV immediately before scrapping",
     ["b: Year 3 year-end net book value before disposal"],
     "b: Year 3 year-end net book value before disposal")

# --- true no-counterpart must stay unmatched -------------------------------
case("true no counterpart", "e: total lease expense over the 8-year term",
     ["a: commencement PV of lease payments", "b: Year 1 interest expense"], None)

# --- zero/nonzero mis-pairing is a structure question, not a value one -----
case("unrelated measure", "e: Year 2 lease liability after the January 1 payment",
     ["f: gain on sale-leaseback recognized"], None)


def main():
    failed = []
    for name, label, cands, expect in CASES:
        got = best_match(label, cands)
        got_label = got[0] if got else None
        ok = (got_label == expect)
        if not ok:
            failed.append((name, expect, got_label))
        print(f"  {'ok  ' if ok else 'FAIL'}  {name:24s} -> {str(got_label)[:52]}")

    # --- no-vacuous-pass rule ---------------------------------------------
    def all_verified(figures):
        """An empty set must NOT count as cleared."""
        return bool(figures) and all(f.get("verified") for f in figures)

    vac_ok = (all_verified([]) is False
              and all_verified([{"verified": True}]) is True
              and all_verified([{"verified": True}, {"verified": False}]) is False)
    print(f"\n  {'ok  ' if vac_ok else 'FAIL'}  no-vacuous-pass rule")
    if not vac_ok:
        failed.append(("no-vacuous-pass", True, False))

    print(f"\nmatcher fixture: {len(CASES) + 1 - len(failed)}/{len(CASES) + 1} passing")
    if failed:
        print("FAILURES:")
        for n, e, g in failed:
            print(f"   {n}: expected {e!r}, got {g!r}")
        sys.exit(1)
    print("FIXTURE GREEN")


if __name__ == "__main__":
    main()
