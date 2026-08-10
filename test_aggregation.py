#!/usr/bin/env python3
"""
Family-aggregation guard (ORDER-006 item 2, ships WITH loosening 5).

The loosening lets ONE pooled solver line match a SET of key lines. That is the
most dangerous shape a matcher can have, because equal money is not equal
accounting: without a linkage requirement it would certify a Cash line as
equivalent to two Investment lines that happen to sum to the same total.

So the fixture's job is not to show the rule works — the offender clearing shows
that. Its job is to pin the ways it must REFUSE:

  * not token-linked            -> must FAIL (the guard the whole rule rests on)
  * sums do not agree           -> must FAIL
  * only one candidate line     -> must FAIL (1:1 is the existing path)
  * sides differ                -> must FAIL
  * genuinely linked and exact  -> must MATCH
"""

import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import compare_stage1_v3 as C     # noqa: E402


# The rule is explicitly "across ALIAS-EQUIVALENT families", so the fixture must
# supply an alias map. With an empty one the genuine case cannot link - which is
# correct behaviour, and testing it with {} would have been testing the wrong
# thing.
AMAP = {"debt investments available for sale": "investment in afs",
        "debt investments held to maturity": "investment in htm"}


def run(pooled, keys, amap=None):
    """(matched?, absorbed) for one pooled line against a set of key lines."""
    es = Counter({(pooled[0], pooled[1], pooled[2]): 1})
    ek = Counter()
    for a, side, amt in keys:
        ek[(a, side, amt)] += 1
    out = C.aggregate_across_family(es, ek, AMAP if amap is None else amap)
    return (bool(out), out[0][1] if out else [])


def main():
    cases = []

    # 0. same account pooled into itself -> must refuse (that is per-entry
    #    netting, not family aggregation; left in, it collapsed several distinct
    #    Cash movements in agent_223#00 into one line)
    ok, _ = run(("cash", "cr", 235000.0),
                [("cash", "cr", 100000.0), ("cash", "cr", 135000.0)])
    cases.append(("SAME account absorbed into itself REFUSED", not ok))

    # 0b. linkage via an incidental SCENARIO word -> must refuse. This absorbed
    #     "Loss from Storm" into an inventory balance in agent_322#00 because
    #     both mentioned "storm". A common token must be shared by the pooled
    #     account and EVERY absorbed one.
    ok, _ = run(("inventory july 12 estimated balance before storm", "dr", 362000.0),
                [("loss from storm", "dr", 300000.0),
                 ("inventory salvage", "dr", 62000.0)])
    cases.append(("linkage via a scenario word REFUSED", not ok))

    # 1. THE GUARD: same money, unrelated accounts -> must refuse
    ok, _ = run(("cash", "dr", 150000.0),
                [("investment in afs quill bonds", "dr", 90000.0),
                 ("investment in afs dune bonds", "dr", 60000.0)])
    cases.append(("NOT token-linked (Cash vs two Investments) REFUSED", not ok))

    # 2. genuinely linked and exact -> must match
    ok, absorbed = run(("debt investments available for sale quill dune", "dr", 150000.0),
                       [("investment in afs quill bonds", "dr", 90000.0),
                        ("investment in afs dune bonds", "dr", 60000.0)])
    cases.append(("token-linked and exact MATCHED", ok and len(absorbed) == 2))

    # 3. sums disagree -> must refuse
    ok, _ = run(("debt investments available for sale quill dune", "dr", 150000.0),
                [("investment in afs quill bonds", "dr", 90000.0),
                 ("investment in afs dune bonds", "dr", 55000.0)])
    cases.append(("sum mismatch REFUSED", not ok))

    # 4. a single candidate -> must refuse (that is the 1:1 path, not this rule)
    ok, _ = run(("debt investments available for sale quill", "dr", 90000.0),
                [("investment in afs quill bonds", "dr", 90000.0)])
    cases.append(("single candidate REFUSED (1:1 is not this rule)", not ok))

    # 5. sides differ -> must refuse
    ok, _ = run(("debt investments available for sale quill dune", "dr", 150000.0),
                [("investment in afs quill bonds", "cr", 90000.0),
                 ("investment in afs dune bonds", "cr", 60000.0)])
    cases.append(("side mismatch REFUSED", not ok))

    # 6. partial linkage: one absorbed line unrelated -> must refuse
    ok, _ = run(("debt investments available for sale quill dune", "dr", 150000.0),
                [("investment in afs quill bonds", "dr", 90000.0),
                 ("prepaid rent", "dr", 60000.0)])
    cases.append(("partially linked set REFUSED", not ok))

    failed = [n for n, p in cases if not p]
    for n, p in cases:
        print(f"  {'ok  ' if p else 'FAIL'}  {n}")
    print(f"\nfamily aggregation: {'GREEN' if not failed else 'RED'}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
