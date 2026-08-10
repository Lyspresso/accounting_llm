#!/usr/bin/env python3
"""
Chart invariants fixture.

The Building ruling was applied to the base account and did NOT reach
"Accumulated Depreciation - Buildings" - a distinct string that no base-form
ruling touches. A follow-up verification caught it; a fixture catches the next
one. Pair rulings emit their banned patterns machine-readably, so a new ruling
extends this fixture without anyone editing it.

  (a) canonical rows pairwise distinct under the string normalizer
  (b) zero rows match any ruling's banned patterns, base AND compound
  (c) alias closure: no variant is itself a canonical elsewhere
"""
from paths import resolve
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = resolve("pack")
ALI = os.path.join(PACK, "account_aliases.csv")
CHART = os.path.join(PACK, "chart_of_accounts.txt")
RULINGS = os.path.join(HERE, "out", "pair_rulings.json")


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def main():
    rows = [r for r in csv.reader(open(ALI, encoding="utf-8")) if r]
    chart = [l.strip() for l in open(CHART, encoding="utf-8")
             if l.strip() and not l.startswith("#")]
    sys.path.insert(0, HERE)
    import rulings as R
    rulings = R.load_rulings()
    failed = []

    # (meta) every ruling emits the FULL pattern class, and no ruling carries a
    # hand-authored list. Four orphans leaked because Building got compound
    # patterns and Note Payable did not - written separately, remembered
    # differently. Uniformity is asserted here, not remembered.
    meta_bad = []
    for rid, r in rulings.items():
        if "banned_patterns" in r:
            meta_bad.append((rid, "carries a hand-authored pattern list"))
        got = set(R.banned_patterns(r))
        missing = set(R.PATTERN_CLASS) - got
        if missing:
            meta_bad.append((rid, f"missing pattern classes {sorted(missing)}"))
    print(f"  {'ok  ' if not meta_bad else 'FAIL'}  (meta) {len(rulings)} rulings x "
          f"{len(R.PATTERN_CLASS)} classes emitted uniformly by generator"
          + ("" if not meta_bad else f" — {meta_bad[:3]}"))
    if meta_bad:
        failed.append("meta")

    # (a) canonical rows pairwise distinct
    seen = {}
    dups = []
    for r in rows:
        k = norm(r[0])
        if k in seen:
            dups.append((seen[k], r[0]))
        seen[k] = r[0]
    print(f"  {'ok  ' if not dups else 'FAIL'}  (a) {len(rows)} canonicals pairwise distinct"
          + ("" if not dups else f" — {dups[:3]}"))
    if dups:
        failed.append("distinct")

    # (b) banned forms, base AND compound
    hits = []
    generated = R.all_banned()
    for rid, name, pat in generated:
        rx = re.compile(pat)
        for line in chart:
            if rx.match(line):
                hits.append((rid, name, "chart", line))
        for row in rows:
            if rx.match(row[0]):
                hits.append((rid, name, "alias-canonical", row[0]))
    n_pat = len(generated)
    print(f"  {'ok  ' if not hits else 'FAIL'}  (b) {n_pat} banned patterns from "
          f"{len(rulings)} rulings — {len(hits)} violations"
          + ("" if not hits else f" {hits[:3]}"))
    if hits:
        failed.append("banned")

    # (c) alias closure
    canon_set = {norm(r[0]) for r in rows}
    orphans = []
    for r in rows:
        for v in r[1:]:
            if norm(v) in canon_set and norm(v) != norm(r[0]):
                orphans.append((r[0], v))
    print(f"  {'ok  ' if not orphans else 'FAIL'}  (c) alias closure — "
          f"{len(orphans)} variants that are canonical elsewhere"
          + ("" if not orphans else f" {orphans[:3]}"))
    if orphans:
        failed.append("closure")

    print(f"\nchart invariants: {'GREEN' if not failed else 'RED'}")
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
