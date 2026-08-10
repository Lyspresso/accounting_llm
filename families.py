#!/usr/bin/env python3
"""
Full-corpus generation families + numeric-delta triage.

Two jobs:

1. Cluster ALL 1,232 Class A stems into families. The pilot drew one question
   per pack by design, so it could not contain family siblings - the earlier
   "25 distinct families" was a property of the sample, not the corpus. Family
   structure has to be computed over the whole corpus, then the failures joined
   against it.

2. Histogram |solver - key| for every numeric mismatch. Small systematic deltas
   are a rounding/PV-convention question - a comparator tolerance fix at zero
   remake cost - not an investigation. Only large or irregular deltas earn
   individual adjudication.
"""

import json
import math
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

LO_RE = re.compile(r"LO\s*(\d+)-(\d+)")
WORD = re.compile(r"[a-z]{4,}")
NUM = re.compile(r"-?\$?\s*\d[\d,]*(?:\.\d+)?")
# Company names and bare numbers are exactly what a "number variant twin"
# changes, so they must not drive family identity.
STOP = set("""the and for with that this from into their which when them були
value amount total company inc llc corp ltd year years january february march
april may june july august september october november december cash""".split())


def shape(stem):
    """A stem's structural fingerprint: vocabulary minus names and numbers."""
    body = NUM.sub(" ", stem.lower())
    toks = [w for w in WORD.findall(body) if w not in STOP]
    return Counter(toks)


def lo_of(q):
    for c in (q.get("concepts") or []):
        m = LO_RE.search(c)
        if m:
            return f"LO {m.group(1)}-{m.group(2)}"
    m = LO_RE.search(q.get("stem", ""))
    return f"LO {m.group(1)}-{m.group(2)}" if m else "LO ?"


def cosine(a, b):
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def main():
    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                      encoding="utf-8")]
    classA = [q for q in qs if q["type"] in ("journal_entry", "ledger", "numeric")
              and q["status"] != "failed"]
    for q in classA:
        q["_lo"] = lo_of(q)
        q["_shape"] = shape(q["stem"])

    # Families form within an LO - a different LO is a different question type
    # by construction, whatever the wording overlap.
    by_lo = defaultdict(list)
    for q in classA:
        by_lo[q["_lo"]].append(q)

    THRESH = 0.72
    families, fam_of = [], {}
    for lo, group in by_lo.items():
        group.sort(key=lambda q: q["id"])
        assigned = {}
        for q in group:
            best, best_s = None, 0.0
            for fi in set(assigned.values()):
                rep = families[fi][0]
                s = cosine(q["_shape"], rep["_shape"])
                if s > best_s:
                    best, best_s = fi, s
            if best is not None and best_s >= THRESH:
                families[best].append(q)
                assigned[q["id"]] = best
                fam_of[q["id"]] = best
            else:
                families.append([q])
                assigned[q["id"]] = len(families) - 1
                fam_of[q["id"]] = len(families) - 1

    sizes = Counter(len(f) for f in families)
    multi = [f for f in families if len(f) > 1]

    print("=" * 74)
    print("FULL-CORPUS FAMILIES (all 1,232 Class A stems)")
    print("=" * 74)
    print(f"  Class A questions : {len(classA)}")
    print(f"  families          : {len(families)}")
    print(f"  families with >1  : {len(multi)}  covering "
          f"{sum(len(f) for f in multi)} questions")
    print(f"  size distribution : {dict(sorted(sizes.items()))}")

    # ---- join the failures against full-corpus families -----------------
    rows = {}
    for b in (1, 2):
        p = os.path.join(OUT, f"stage1_v3_batch{b}_results.json")
        if os.path.exists(p):
            for r in json.load(open(p, encoding="utf-8"))["rows"]:
                rows[r["id"]] = r
    failed = [qid for qid, r in rows.items() if r.get("status") == "failed"]

    print("\n" + "=" * 74)
    print("FAILURES JOINED AGAINST FULL-CORPUS FAMILIES")
    print("=" * 74)
    singleton, with_sibs, sib_targets = 0, 0, []
    for qid in failed:
        fi = fam_of.get(qid)
        fam = families[fi] if fi is not None else [qid]
        sibs = [s["id"] for s in fam if s["id"] != qid]
        unsampled = [s for s in sibs if s not in rows]
        if sibs:
            with_sibs += 1
            sib_targets.append({"failure": qid, "lo": lo_of(next(q for q in classA if q["id"] == qid)),
                                "family_size": len(fam), "unsampled_siblings": unsampled[:3]})
        else:
            singleton += 1
    print(f"  failures            : {len(failed)}")
    print(f"  true singletons     : {singleton}")
    print(f"  with siblings       : {with_sibs}   <- replication testable")
    tot_sibs = sum(len(t["unsampled_siblings"]) for t in sib_targets)
    print(f"  sibling solves to run: {tot_sibs}")
    for t in sib_targets[:14]:
        print(f"    {t['failure']:14s} {t['lo']:9s} fam={t['family_size']:>2}  "
              f"-> {t['unsampled_siblings']}")

    json.dump({"families": [[q["id"] for q in f] for f in families],
               "sibling_targets": sib_targets},
              open(os.path.join(OUT, "families.json"), "w"), indent=1)

    # ---- numeric delta histogram ---------------------------------------
    print("\n" + "=" * 74)
    print("NUMERIC MISMATCH DELTAS  |solver - nearest key figure|")
    print("=" * 74)
    qmap = {q["id"]: q for q in qs}
    deltas = []
    for qid, r in rows.items():
        q = qmap[qid]
        pool = set()
        for m in NUM.finditer(q.get("solution", "")):
            try:
                pool.add(round(abs(float(m.group(0).replace("$", "").replace(",", ""))), 2))
            except ValueError:
                pass
        for l in q.get("answer_key") or []:
            pool.add(round(abs(float(l.get("amount") or 0)), 2))
        for i in r.get("issues", []):
            if i["kind"] != "SOLVER_MISMATCH":
                continue
            v = i.get("solver")
            try:
                v = abs(float(v))
            except (TypeError, ValueError):
                continue
            if not pool:
                continue
            near = min(pool, key=lambda k: abs(k - v))
            d = abs(near - v)
            rel = d / max(1.0, v)
            deltas.append({"id": qid, "label": str(i.get("label"))[:46],
                           "solver": v, "nearest_key": near, "delta": d, "rel": rel})

    deltas.sort(key=lambda x: x["rel"])
    buckets = [("<= $1 (rounding)", lambda d: d["delta"] <= 1.0),
               ("<= 0.5% rel", lambda d: d["rel"] <= 0.005),
               ("0.5-5% rel", lambda d: 0.005 < d["rel"] <= 0.05),
               ("5-50% rel", lambda d: 0.05 < d["rel"] <= 0.5),
               ("> 50% rel", lambda d: d["rel"] > 0.5)]
    print(f"  numeric mismatches with a comparable key figure: {len(deltas)}")
    seen = set()
    for name, fn in buckets:
        got = [d for d in deltas if fn(d) and id(d) not in seen]
        for d in got:
            seen.add(id(d))
        print(f"    {name:22s} {len(got):>4}")
    print("\n  smallest 10 (candidate tolerance/convention fixes, zero remake cost):")
    for d in deltas[:10]:
        print(f"    {d['id']:14s} {d['label']:46s} solver={d['solver']:>12,.2f} "
              f"key={d['nearest_key']:>12,.2f} d={d['delta']:>10,.2f} ({d['rel']:.3%})")
    print("\n  largest 8 (individual adjudication):")
    for d in deltas[-8:]:
        print(f"    {d['id']:14s} {d['label']:46s} solver={d['solver']:>12,.2f} "
              f"key={d['nearest_key']:>12,.2f} d={d['delta']:>10,.2f} ({d['rel']:.1%})")
    json.dump(deltas, open(os.path.join(OUT, "numeric_deltas.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
