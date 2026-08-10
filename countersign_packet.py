#!/usr/bin/env python3
"""
Countersign packet — the human-tier golden nominations (ORDER-002 item 8).

Floor #2 certifies at HUMAN tier only (D6). Every existing golden is
`adjudicated` or `ai_cross_checked`, so the floor cannot be certified by any
amount of machine work — the operator's session is on the critical path, and
this file is what that session actually works through.

Two things it must get right:

1. **n.** The gate tests the Wilson UPPER bound, so at n=27 even a flawless run
   bounds at 12.5% against a 10% ceiling. n >= 35 is arithmetic, not taste. This
   nominates a MARGIN above 35, because a nomination that fails cross-check does
   not count and discovering that at n=35 exactly means going back for more.

2. **Composition.** Nominations are stratified by chapter and by item class. A
   packet drawn from whatever sorted first would certify the floor against the
   easiest corner of the corpus, and the number would be real but would not
   describe the bank. Class B (mcq) has never been through Stage 1 at all, so a
   packet with no mcq in it certifies nothing about 596 of 1,828 items.

Each nomination ships with worked evidence — the derivation that already exists,
the comparator's verdict on it, and the admissibility of the bundle that
produced it — so the session is a review, not a re-derivation.
"""

import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)

import compare_stage1_v3 as C     # noqa: E402
import preflight as PF            # noqa: E402
import provenance as P            # noqa: E402

TARGET_N = 35          # floor #2's arithmetic minimum
MARGIN = 6             # nominations beyond target: cross-check attrition


def chapter_of(q):
    for c in (q.get("concepts") or []) + [q.get("stem", "")]:
        m = re.search(r"\bLO\s*(\d+)-\d+", str(c), re.I)
        if m:
            return f"ch{int(m.group(1))}"
    return "ch?"


def main():
    qs, known, amap = PF.load()
    gold_dir = os.path.join(HERE, "goldens")
    existing = set()
    for fn in os.listdir(gold_dir):
        if fn.endswith(".json") and fn != "INDEX.json":
            existing.add(json.load(open(os.path.join(gold_dir, fn),
                                        encoding="utf-8"))["id"])
    # Class coverage is a property of the GOLDEN SET the session will certify -
    # existing goldens plus nominations - not of the nominations alone. Reading
    # it off the nominations said "numeric not represented" the moment numeric
    # goldens were minted, which is the opposite of the truth. A caveat that
    # misreports its own subject is worse than no caveat.
    existing_classes = collections.Counter(
        qs[i].get("type") for i in existing if i in qs)

    # candidates: an admissible derivation exists and the comparator is clean
    cands = []
    for qid, q in qs.items():
        if qid in existing:
            continue
        src, why = P.evidence_dir(qid, q)
        if src is None:
            continue
        sp = os.path.join(src, "solver_output.json")
        if not os.path.exists(sp):
            continue
        sol = json.load(open(sp, encoding="utf-8"))
        iss, meta = C.compare(sol, q, known, amap)
        hard = [i for i in iss if i["kind"] in C.HARD]
        cands.append({
            "id": qid, "chapter": chapter_of(q), "class": q.get("type"),
            "evidence": os.path.relpath(src, HERE),
            "harness": os.path.basename(os.path.dirname(src)),
            "key_lines": meta.get("key_lines", 0),
            "n_answers": len(sol.get("answers") or []),
            "hard_findings": len(hard),
            "routed_stage2": meta.get("routed_stage2", 0),
            "admissible": why,
            "clean": not hard,
        })

    clean = [c for c in cands if c["clean"]]
    need = max(0, TARGET_N - len(existing)) + MARGIN

    # stratify: round-robin across (chapter, class) so no single corner fills it
    buckets = collections.defaultdict(list)
    for c in clean:
        buckets[(c["chapter"], c["class"])].append(c)
    for b in buckets.values():
        b.sort(key=lambda c: (-c["key_lines"], -c["n_answers"], c["id"]))

    picked, keys = [], sorted(buckets, key=lambda k: (-len(buckets[k]), str(k)))
    i = 0
    while len(picked) < need and any(buckets[k] for k in keys):
        k = keys[i % len(keys)]
        if buckets[k]:
            picked.append(buckets[k].pop(0))
        i += 1

    have_by_class = collections.Counter(c["class"] for c in picked)
    have_by_chap = collections.Counter(c["chapter"] for c in picked)

    print("=== COUNTERSIGN PACKET (human-tier nominations) ===\n")
    print(f"existing goldens        : {len(existing)}  (all adjudicated / "
          f"ai_cross_checked; ZERO human-tier)")
    print(f"floor #2 target n       : {TARGET_N}   (Wilson upper bound <= 10%)")
    print(f"nominations needed      : {TARGET_N - len(existing)} "
          f"+ {MARGIN} margin = {need}")
    print(f"clean candidates found  : {len(clean)} of {len(cands)} with "
          f"admissible evidence\n")
    print(f"NOMINATED               : {len(picked)}")
    print(f"  by class   : {dict(have_by_class)}")
    print(f"  by chapter : {dict(sorted(have_by_chap.items()))}\n")

    if len(picked) < need:
        print(f"  ** SHORT by {need - len(picked)} — not enough clean admissible")
        print("     candidates exist. Stage 1 must run further before floor #2")
        print("     can reach n >= 35. This is a COVERAGE gap, not a quality one.\n")

    # CLASS COVERAGE is the caveat that must travel WITH the number. A floor
    # certified entirely on journal-entry items is a real measurement of
    # journal-entry items and says nothing about the 596 mcq items, which have
    # never been through Stage 1 and therefore have no derivation to nominate.
    corpus_classes = collections.Counter(q.get("type") for q in qs.values())
    certified_classes = existing_classes + have_by_class
    missing = [k for k in corpus_classes if k not in certified_classes]
    print(f"  golden set after this packet, by class: {dict(certified_classes)}")
    if missing:
        print("  ** CLASS COVERAGE WARNING **")
        for k in missing:
            print(f"     {corpus_classes[k]:>4} {k} items are NOT represented — no "
                  f"admissible derivation exists for any of them.")
        print("     Certifying floor #2 on this packet certifies it for the")
        print("     classes present, and for those ONLY. It is not a")
        print("     corpus-wide certification and must not be quoted as one.\n")

    print("nominations (worked evidence attached in the JSON):")
    for c in picked:
        print(f"  {c['id']:14s} {c['chapter']:6s} {str(c['class']):14s} "
              f"key_lines={c['key_lines']:>3} answers={c['n_answers']:>3} "
              f"{c['harness']}")

    json.dump({"target_n": TARGET_N, "existing": len(existing),
               "needed": need, "nominated": picked,
               "clean_candidates": len(clean), "considered": len(cands),
               "by_class_nominated": dict(have_by_class),
               "by_class_certified_set": dict(existing_classes + have_by_class),
               "by_chapter": dict(have_by_chap),
               "short_by": max(0, need - len(picked)),
               "classes_not_represented": {
                   k: v for k, v in collections.Counter(
                       q.get("type") for q in qs.values()).items()
                   if k not in (existing_classes + have_by_class)},
               "caveat": ("certifies floor #2 for the classes present ONLY; "
                          "classes with no admissible derivation are not "
                          "covered by this packet")},
              open(os.path.join(OUT, "countersign_packet.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(OUT, 'countersign_packet.json')}")


if __name__ == "__main__":
    main()
