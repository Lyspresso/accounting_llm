#!/usr/bin/env python3
"""
Structured label grammar + matcher, replacing regex tokenizing.

Bag-of-tokens matching failed five distinct ways in one item, all because a
label's STRUCTURE was flattened into an unordered set: the period ordinal, the
part letter and the measure were all just tokens, so "b: Year 2 accumulated
depreciation" and "b: Year 1 accumulated depreciation" scored jaccard 1.00 once
a 3-character minimum dropped the digits.

A label here parses into fields, and fields must AGREE - a period mismatch is
disqualifying, not a small penalty.

    part      c        from "c:" / "(c)" / "part c"
    period    2        from "Year 2" / "Yr 2" / "Period 2" / "Y2"
    date      12-31    from "Dec 31" / "December 31"
    measure   normalised phrase, synonyms folded
"""

import re

PART = re.compile(r"^\s*\(?([a-h])\)?\s*[:.\)-]", re.I)
PERIOD = re.compile(r"\b(?:year|yr|period|y)\s*[-# ]?\s*(\d{1,2})\b", re.I)
MONTHS = ("january february march april may june july august september "
          "october november december").split()
DATE = re.compile(r"\b(" + "|".join(m[:3] for m in MONTHS) + r")[a-z]*\.?\s+(\d{1,2})\b", re.I)

SYN = (
    (r"\bnbv\b", "net book value"), (r"\bcarrying amount\b", "net book value"),
    (r"\bcarrying value\b", "net book value"), (r"\bbook value\b", "net book value"),
    (r"\baccum\b", "accumulated"), (r"\bdep\b", "depreciation"),
    (r"\bdepr\b", "depreciation"), (r"\bamort\b", "amortization"),
    (r"\bexp\b", "expense"), (r"\bliab\b", "liability"),
    (r"\bbeg\b", "beginning"), (r"\bend\b", "ending"),
)
STOP = set("the a an of for on at and to is are in from with".split())
WORD = re.compile(r"[a-z]+|\d+")
CUMULATIVE = re.compile(r"cumulative|to date|since|accumulated|total", re.I)


def parse(label):
    raw = str(label or "")
    low = raw.lower()
    part = None
    m = PART.match(raw)
    if m:
        part = m.group(1).lower()
        low = low[m.end():]
    period = None
    m = PERIOD.search(low)
    if m:
        period = int(m.group(1))
        low = low[:m.start()] + " " + low[m.end():]
    date = None
    m = DATE.search(low)
    if m:
        mon = next((i + 1 for i, x in enumerate(MONTHS)
                    if x.startswith(m.group(1).lower())), None)
        if mon:
            date = f"{mon:02d}-{int(m.group(2)):02d}"
        low = low[:m.start()] + " " + low[m.end():]
    for pat, rep in SYN:
        low = re.sub(pat, rep, low)
    measure = tuple(sorted(t for t in WORD.findall(low) if t not in STOP))
    return {"part": part, "period": period, "date": date, "measure": measure,
            "cumulative": bool(CUMULATIVE.search(raw))}


def score(a, b):
    """
    None = disqualified (a field disagrees). Otherwise measure overlap in [0,1].
    Structure is a gate, not a weight: pairing Year 2 with Year 1 is not a
    slightly worse match, it is the wrong row.
    """
    pa, pb = parse(a), parse(b)
    # Period and date DISQUALIFY: Year 2 against Year 1 is the wrong row, not a
    # weaker match, and that conflation is what corrupted a whole schedule.
    if pa["period"] is not None and pb["period"] is not None and pa["period"] != pb["period"]:
        return None
    if pa["date"] and pb["date"] and pa["date"] != pb["date"]:
        return None
    # Cumulative vs periodic is a different quantity entirely.
    if pa["cumulative"] != pb["cumulative"]:
        return None
    ma, mb = set(pa["measure"]), set(pb["measure"])
    if not ma or not mb:
        return 0.0
    s = len(ma & mb) / len(ma | mb)
    # Part only PENALISES. The same quantity is legitimately asked under two
    # parts - "d: NBV immediately before scrapping" and "b: Year 3 year-end net
    # book value before disposal" are one figure, and a hard part gate filed
    # that real disagreement as NO_COUNTERPART.
    if pa["part"] and pb["part"] and pa["part"] != pb["part"]:
        s *= 0.85
    return s


def best_match(label, candidates, key=lambda c: c, threshold=0.34):
    """
    (candidate, score) or None. A tie at the top is AMBIGUOUS and returns None -
    resolving a tie by list order is what deterministically paired every
    schedule row to the earliest year.
    """
    scored = []
    for c in candidates:
        s = score(label, key(c))
        if s is not None and s >= threshold:
            scored.append((s, c))
    if not scored:
        return None
    scored.sort(key=lambda x: -x[0])
    if len(scored) > 1 and abs(scored[1][0] - scored[0][0]) < 1e-9:
        return None
    return (scored[0][1], scored[0][0])
