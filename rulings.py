#!/usr/bin/env python3
"""
Ruling pattern GENERATOR — one function, applied uniformly to every ruling.

Hand-authored per-ruling patterns leaked four orphans in a row, each of the same
class and each found only after someone went looking. The Building ruling got
compound patterns; the Note Payable ruling did not, because I wrote them
separately and remembered differently on two occasions. Uniformity by memory is
not uniformity.

A ruling now declares only its FACTS - the winning form, the losing form, and
any prefix bases - and the pattern class is derived. A new ruling cannot have a
narrower pattern set than an old one, because there is only one generator.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.join(HERE, "out", "pair_rulings.json")

# The class every ruling must emit. Named so the meta-invariant can assert
# presence by name rather than by counting.
PATTERN_CLASS = ("exact", "word_boundary_compound", "prefix_compound")

# Prefixes that build compound accounts on top of a base account. Shared by
# every ruling: a losing form is banned in a compound wherever it is banned
# standing alone.
COMPOUND_PREFIXES = (
    "accumulated depreciation", "accumulated amortization",
    "discount on", "premium on", "allowance for", "provision for",
    "current portion of", "gain on", "loss on",
)


def banned_patterns(ruling):
    """
    The full pattern class for one ruling. Returns {name: regex}.

    exact                  - the losing form standing alone
    word_boundary_compound - the losing form leading a compound
                             ("Notes Payable (long-term)")
    prefix_compound        - a shared prefix leading the losing form
                             ("Accumulated Depreciation - Buildings")
    """
    losing = re.escape(ruling["losing_form"])
    pats = {
        "exact": rf"(?i)^{losing}$",
        "word_boundary_compound": rf"(?i)^{losing}\b.*$",
        "prefix_compound": rf"(?i)^(?:{'|'.join(re.escape(p) for p in COMPOUND_PREFIXES)})"
                           rf"\s*[-–—:]?\s*{losing}\b.*$",
    }
    assert set(pats) == set(PATTERN_CLASS), "generator drifted from the declared class"
    return pats


def load_rulings():
    if not os.path.exists(REGISTRY):
        return {}
    return json.load(open(REGISTRY, encoding="utf-8"))


def all_banned():
    """[(ruling_id, pattern_name, regex)] across every ruling. Uniform by construction."""
    out = []
    for rid, r in load_rulings().items():
        for name, pat in banned_patterns(r).items():
            out.append((rid, name, pat))
    return out


def normalize_registry():
    """
    Strip any hand-authored patterns from the registry. Facts are declared;
    patterns are derived. A stored pattern list is a place for drift to hide.
    """
    r = load_rulings()
    for rid, v in r.items():
        v.pop("banned_patterns", None)
    json.dump(r, open(REGISTRY, "w", encoding="utf-8"), indent=1)
    return r


if __name__ == "__main__":
    r = normalize_registry()
    print(f"rulings: {len(r)}   (hand-authored patterns stripped)")
    for rid, name, pat in all_banned():
        print(f"   {rid:32s} {name:24s} {pat}")
    print(f"\ntotal generated patterns: {len(all_banned())} "
          f"= {len(r)} rulings x {len(PATTERN_CLASS)} classes")
