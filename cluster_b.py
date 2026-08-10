#!/usr/bin/env python3
"""
Class B (MCQ) family and duplicate clustering.

596 of the 1,828 items are multiple choice. They do not go through the JE
comparator at all, so the stage-1 arithmetic pass says nothing about them and
verifying them one at a time would cost as much as the journal-entry work while
proving far less per item.

MCQ items cluster harder than JE items because the same tested idea is reissued
with the distractors reshuffled and the numbers rotated. Three tiers:

    IDENTICAL   same content hash. One is canonical, the rest retire as
                DUPLICATE_OF with their lineages preserved.
    STEM_TWIN   same stem shape and the SAME option set (order-insensitive).
                A verdict on one is a verdict on all - only the ordering moves.
    VARIANT     same stem shape and same LO, different numbers or options.
                Shares a derivation, not an answer: verifying the representative
                validates the METHOD, and each sibling still needs its own key
                checked, but against a derivation already known good.

The distinction matters for what may be propagated. A STEM_TWIN inherits the
verdict. A VARIANT inherits only the method, so counting variants as covered
would be the coverage-debt error this pipeline exists to avoid.
"""

import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)

import canon                 # noqa: E402
from families import cosine, lo_of, shape       # noqa: E402

SHAPE_TAU = 0.86        # stem-shape cosine for same-family
OPT_RE = re.compile(r"^\s*[a-eA-E][.)]\s*", re.M)


def option_set(q):
    """Order-insensitive normalised option set. Reordered distractors are the
    most common MCQ reissue and must not read as a different question."""
    opts = q.get("options") or []
    if isinstance(opts, dict):
        opts = list(opts.values())
    norm = []
    for o in opts:
        t = canon.delatex(str(o))
        t = OPT_RE.sub("", t)
        t = re.sub(r"[^a-z0-9.]+", " ", t.lower()).strip()
        if t:
            norm.append(t)
    return frozenset(norm)


def main():
    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                      encoding="utf-8")]
    mcq = [q for q in qs if q.get("type") == "mcq"]
    print(f"Class B (mcq) items: {len(mcq)}\n")

    # --- tier 1: byte-identical content -----------------------------------
    by_hash = collections.defaultdict(list)
    for q in mcq:
        by_hash[q["content_hash"]].append(q["id"])
    identical = {h: v for h, v in by_hash.items() if len(v) > 1}
    dup_items = sum(len(v) - 1 for v in identical.values())

    # --- tier 2/3: shape families within an LO ----------------------------
    by_lo = collections.defaultdict(list)
    for q in mcq:
        by_lo[lo_of(q)].append(q)

    fams, assigned = [], {}
    for lo, group in by_lo.items():
        shapes = {q["id"]: shape(q.get("stem", "")) for q in group}
        for q in group:
            if q["id"] in assigned:
                continue
            fam = [q]
            assigned[q["id"]] = True
            for other in group:
                if other["id"] in assigned:
                    continue
                if cosine(shapes[q["id"]], shapes[other["id"]]) >= SHAPE_TAU:
                    fam.append(other)
                    assigned[other["id"]] = True
            fams.append({"lo": lo, "members": fam})

    twins = variants = 0
    out_fams = []
    for f in fams:
        rep = f["members"][0]
        rep_opts = option_set(rep)
        tw = [m["id"] for m in f["members"][1:] if option_set(m) == rep_opts and rep_opts]
        va = [m["id"] for m in f["members"][1:] if m["id"] not in tw]
        twins += len(tw)
        variants += len(va)
        out_fams.append({"lo": f["lo"], "representative": rep["id"],
                         "stem_twins": tw, "variants": va,
                         "size": len(f["members"])})

    n_fam = len(out_fams)
    multi = [f for f in out_fams if f["size"] > 1]
    # what must actually be solved: one representative per family, plus every
    # VARIANT (they share a method, not an answer). Twins inherit outright.
    to_solve = n_fam + variants

    print("--- tier 1: IDENTICAL (same content hash) ---")
    print(f"  duplicate groups : {len(identical)}")
    print(f"  retirable items  : {dup_items}\n")
    print("--- tier 2/3: shape families within an LO ---")
    print(f"  families              : {n_fam}")
    print(f"  multi-member families : {len(multi)}")
    print(f"  STEM_TWIN members     : {twins}   (inherit the representative's verdict)")
    print(f"  VARIANT members       : {variants}   (inherit the METHOD only)\n")
    print(f"  largest families      : "
          f"{sorted((f['size'] for f in out_fams), reverse=True)[:8]}\n")
    print("--- verification effort ---")
    print(f"  naive, one solve per item      : {len(mcq)}")
    print(f"  representatives + variants     : {to_solve}")
    print(f"  reduction                      : {len(mcq) - to_solve} "
          f"({(len(mcq) - to_solve) / max(1, len(mcq)):.1%})")
    print("\n  COVERAGE DEBT: variants are NOT covered by their representative.")
    print(f"  Counting families alone would claim {len(mcq)} items covered by "
          f"{n_fam} solves and understate\n  the real work by {variants} items.")

    json.dump({"n_mcq": len(mcq), "identical_groups": len(identical),
               "retirable_duplicates": dup_items, "families": n_fam,
               "stem_twins": twins, "variants": variants,
               "solves_required": to_solve, "shape_tau": SHAPE_TAU,
               "detail": out_fams},
              open(os.path.join(OUT, "class_b_clusters.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(OUT, 'class_b_clusters.json')}")


if __name__ == "__main__":
    main()
