#!/usr/bin/env python3
"""
Ledger sentinel + duplicate policy.

SENTINEL (item 2): at a fixed PIPELINE_VERSION the terminal-state count is
non-decreasing absent explicit invalidation. Any decrease halts and alerts.
This exists because the count silently went to zero three times in one session
- ledger.jsonl opened in "w" mode and every re-normalisation wiped the stage-1
verdicts other stages had appended. Nothing noticed until a migration audit.

DUPLICATE POLICY (item 3): one canonical item per byte-identical group; the rest
retire as DUPLICATE_OF with their lineage preserved. Lineages end, they never
disappear. Coverage counts each group once, so a group of three does not read as
three questions of coverage.

    python3 sentinel.py --check          # sentinel only
    python3 sentinel.py --dedupe         # apply the duplicate policy
    python3 sentinel.py --near-dup       # near-duplicate scan on top
"""

import argparse
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
STATE = os.path.join(OUT, "sentinel_state.json")
PIPELINE_VERSION = "1.2"
# ONLY two terminal states exist. `machine_passed` is a stage-PROGRESS state -
# an item that cleared Stage 1 arithmetic has not been verified, it has passed
# one layer. Counting it as terminal reported 671 "terminal" items under a RED
# gate with the taxonomy unbuilt, when the true count was ZERO. A sentinel that
# counts progress states cannot detect the loss of real terminal states, which
# is the only thing it exists to do.
TERMINAL = ("verified", "needs_human")
PROGRESS = ("machine_passed", "grounded_passed", "adversary_passed")


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def read_ledger():
    p = os.path.join(OUT, "ledger.jsonl")
    rows = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def current_hashes():
    """Content hashes of the CURRENT corpus - superseded rows are history."""
    p = os.path.join(OUT, "questions.jsonl")
    if not os.path.exists(p):
        return set()
    return {json.loads(l)["content_hash"] for l in open(p, encoding="utf-8")}



def resolve_current(rows):
    """
    content_hash -> the row that states the lineage's CURRENT state.

    The ledger is an append-only event log, so "current" is a resolution, not a
    lookup, and two earlier rules each got it wrong in opposite directions:

      "latest row wins"     - a stage-0 row appended after a stage-1 verdict
                              masked it, hiding 85 machine_passed and 14 failed
                              items behind re-normalisation rows.
      "terminal outranks"   - fixed that, but made a terminal state UNREVERTABLE:
                              the superseded `verified` row kept outvoting the
                              `machine_passed` row that ORDER-002 item 1 ordered
                              in its place, so a reviewer ruling could not land.

    The rule that is right in both directions: the highest STAGE reached for a
    lineage wins (stage-0 re-normalisation never overrides a verdict), and among
    rows at that stage the LAST one wins (so a verdict can be revised, and a
    revision is visible instead of silently ignored).
    """
    best = {}
    for i, r in enumerate(rows):
        h = r.get("content_hash")
        st = r.get("stage") or 0
        prev = best.get(h)
        if prev is None or (st, i) >= (prev[0], prev[1]):
            best[h] = (st, i, r)
    return {h: v[2] for h, v in best.items()}


def terminal_count(rows):
    """
    DISTINCT items at CURRENT content hashes. The ledger deliberately retains
    superseded rows after a repair re-keys an item, so counting rows counted the
    same lineage twice across hash generations.
    """
    cur = current_hashes()
    seen = set()
    for h, r in resolve_current(rows).items():
        if r.get("pipeline_version") != PIPELINE_VERSION:
            continue
        if cur and h not in cur:
            continue
        if r.get("status") in TERMINAL:
            seen.add(h)
    return len(seen)


def decompose(rows):
    """
    DISTINCT ITEMS at current hash x state x scope. Rows are retained for
    forensics but must never be the headline: the ledger keeps superseded rows
    after a repair re-keys an item, so a row count counts one lineage twice.
    """
    import collections
    cur = current_hashes()

    best = {}
    for h, r in resolve_current(rows).items():
        scope = "current" if (not cur or h in cur) else "superseded"
        best[h] = (r.get("status"), r.get("stage") or "-", scope)
    out = collections.Counter(best.values())
    return out, len(best), len(rows)


def status_vector(rows):
    """
    FULL status x scope count vector. Merge-only semantics make every cell
    monotone at a fixed PIPELINE_VERSION, so a decrease in ANY cell is a loss.
    A terminal-only sentinel over a zero-terminal corpus guards nothing live -
    it watches a number that cannot fall because it is already zero.
    """
    import collections
    cur = current_hashes()
    v = collections.Counter()
    for r in rows:
        if r.get("pipeline_version") != PIPELINE_VERSION:
            continue
        scope = "current" if (not cur or r.get("content_hash") in cur) else "superseded"
        v[f"{r.get('status')}|{scope}"] += 1
    return dict(v)


def _status_totals(v):
    """Collapse status|scope cells to status totals."""
    out = {}
    for k, n in v.items():
        out[k.split("|")[0]] = out.get(k.split("|")[0], 0) + n
    return out


def vector_regressions(now_v, was_v):
    """
    Cells that fell, measured at STATUS level rather than status|scope.

    Merge-only semantics make rows immortal, so a status TOTAL can only rise -
    that is the invariant worth halting on. `scope` is a derived view: it asks
    whether a row's content_hash is still current, so an authorised KEY REPAIR
    necessarily migrates that item's rows from `current` to `superseded` and
    drops a status|scope cell without destroying anything. Halting on the finer
    cell made every repair look like data loss and would have trained everyone
    to reach for --invalidate, which is how a real loss gets waved through.

    Scope migrations are still reported (see scope_migrations) - just not as a
    halt.
    """
    now_t, was_t = _status_totals(now_v), _status_totals(was_v)
    return {k: (was_t[k], now_t.get(k, 0))
            for k in was_t if now_t.get(k, 0) < was_t[k]}


def scope_migrations(now_v, was_v):
    """status|scope cells that moved while their status total held - diagnostics."""
    out = {}
    for k in set(now_v) | set(was_v):
        a, b = was_v.get(k, 0), now_v.get(k, 0)
        if a != b:
            out[k] = (a, b)
    return out


def check(invalidate=False):
    rows = read_ledger()
    now = terminal_count(rows)
    now_vec = status_vector(rows)
    prior = None
    if os.path.exists(STATE):
        try:
            prior = json.load(open(STATE, encoding="utf-8"))
        except json.JSONDecodeError:
            prior = None

    print(f"pipeline_version   : {PIPELINE_VERSION}")
    print(f"ledger rows        : {len(rows)}")
    print(f"terminal states now: {now}   (verified | needs_human, distinct current-hash items)")
    dec, n_items, n_rows = decompose(rows)
    print(f"  DISTINCT ITEMS: {n_items}   (rows {n_rows}, retained for forensics)")
    print("  items x state x stage x scope:")
    tot = 0
    for (st, stg, sc), n in sorted(dec.items(), key=lambda kv: -kv[1]):
        tot += n
        print(f"    {str(st):16s} stage={str(stg):4s} {sc:10s} {n:>5}")
    print(f"    {'PARTITION SUM':16s}                    {tot:>5}   "
          f"remainder = {n_items - tot}")
    print(f"  status vector ({len(now_vec)} cells): "
          f"{sum(now_vec.values())} rows at this pipeline_version")
    if prior and prior.get("pipeline_version") == PIPELINE_VERSION:
        regs = vector_regressions(now_vec, prior.get("status_vector", {}))
        migs = scope_migrations(now_vec, prior.get("status_vector", {}))
        if migs and not regs:
            print(f"  scope migrations (no rows lost): {len(migs)} cell(s)")
            for k, (a, b) in sorted(migs.items()):
                print(f"    {k:34s} {a} -> {b}   ({b - a:+d})")
        if regs and not invalidate:
            print("\n*** SENTINEL HALT: a status TOTAL fell (rows destroyed) ***")
            for k, (a, b) in sorted(regs.items()):
                print(f"    {k:34s} {a} -> {b}   ({a - b} lost)")
            print("    Merge-only semantics make status TOTALS monotone, so a")
            print("    fall is a destroyed row, not a scope change or a repair.")
            json.dump({"pipeline_version": PIPELINE_VERSION, "terminal_count": now,
                       "status_vector": now_vec, "ledger_rows": len(rows),
                       "recorded_at_note": "HALTED"}, open(STATE, "w"), indent=1)
            return 2
        if regs:
            print(f"  explicit invalidation accepted for {len(regs)} cell(s)")
        else:
            print(f"  OK all {len(_status_totals(now_vec))} status TOTALS non-decreasing "
                  f"({len(now_vec)} status|scope cells tracked)")
        was = prior.get("terminal_count", 0)
        print(f"terminal states was: {was}  (recorded {prior.get('recorded_at_note','-')})")
        if now < was and not invalidate:
            print(f"\n*** SENTINEL HALT: terminal states fell {was} -> {now} "
                  f"({was - now} lost) at unchanged PIPELINE_VERSION ***")
            print("    Nothing may re-run until this is explained or explicitly")
            print("    invalidated with --invalidate. This is the failure mode that")
            print("    silently zeroed the cache three times before anyone looked.")
            return 2
        if now < was:
            print(f"  explicit invalidation accepted: {was} -> {now}")
        else:
            print(f"  OK non-decreasing (+{now - was})")
    else:
        print("  no prior state at this pipeline_version - establishing baseline")

    json.dump({"pipeline_version": PIPELINE_VERSION, "terminal_count": now,
               "status_vector": now_vec, "ledger_rows": len(rows),
               "recorded_at_note": "sentinel check"},
              open(STATE, "w"), indent=1)
    return 0


def dedupe(apply_it=False):
    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                      encoding="utf-8")]
    groups = defaultdict(list)
    for q in qs:
        groups[sha(q["stem"] + json.dumps(q["options"]) + (q.get("solution") or ""))].append(q)
    dup = {h: g for h, g in groups.items() if len(g) > 1}

    retire = []
    for h, g in dup.items():
        g.sort(key=lambda q: q["id"])       # lowest id is canonical, deterministically
        canon_q, rest = g[0], g[1:]
        for r in rest:
            retire.append({"id": r["id"], "lineage_id": r["lineage_id"],
                           "pack_id": r["pack_id"],
                           "status": "DUPLICATE_OF",
                           "duplicate_of": canon_q["id"],
                           "bytes_hash": h,
                           "note": "byte-identical; lineage preserved, never deleted"})

    print(f"byte-identical groups : {len(dup)}")
    print(f"items in those groups : {sum(len(g) for g in dup.values())}")
    print(f"canonical kept        : {len(dup)}")
    print(f"retired DUPLICATE_OF  : {len(retire)}")
    print(f"coverage effect       : these groups count as {len(dup)} questions, "
          f"not {sum(len(g) for g in dup.values())}")
    for h, g in list(dup.items())[:8]:
        print(f"    {g[0]['id']} <- {[x['id'] for x in g[1:]]}")

    if apply_it:
        with open(os.path.join(OUT, "duplicates.json"), "w", encoding="utf-8") as fh:
            json.dump({"groups": {h: [q["id"] for q in g] for h, g in dup.items()},
                       "retired": retire}, fh, indent=1)
        from ledger_io import append_rows
        for r in retire:
            r["pipeline_version"] = PIPELINE_VERSION
        append_rows(retire, supersede_stage0=False)
        print(f"\napplied: {len(retire)} retirements appended to the ledger")
    else:
        print("\nnot applied (pass --dedupe to write)")
    return retire


def near_dup():
    """
    Byte-identical is the FLOOR of generator self-repetition, not the ceiling.
    Family similarity already computes the near-duplicate structure, so reuse it
    rather than recomputing a second notion of sameness.
    """
    fp = os.path.join(OUT, "families.json")
    if not os.path.exists(fp):
        print("families.json missing - run families.py first")
        return
    fams = json.load(open(fp, encoding="utf-8"))["families"]
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}
    bytes_of = {qid: sha(q["stem"] + json.dumps(q["options"]) + (q.get("solution") or ""))
                for qid, q in qs.items()}

    sizes = Counter(len(f) for f in fams)
    multi = [f for f in fams if len(f) > 1]
    # inside a family, how many members are byte-identical vs merely similar?
    exact_pairs = near_only = 0
    tight = []
    for f in multi:
        hs = Counter(bytes_of.get(x) for x in f)
        e = sum(c - 1 for c in hs.values() if c > 1)
        exact_pairs += e
        near_only += (len(f) - 1) - e
        if len(f) >= 6:
            tight.append((len(f), f[:4]))
    print(f"families            : {len(fams)}")
    print(f"multi-member        : {len(multi)}  covering "
          f"{sum(len(f) for f in multi)} questions")
    print(f"size distribution   : {dict(sorted(sizes.items()))}")
    print(f"byte-identical pairs inside families : {exact_pairs}")
    print(f"NEAR-duplicate (same family, different bytes): {near_only}")
    print(f"\nfamilies of 6+ (heaviest self-repetition):")
    for n, sample in sorted(tight, reverse=True)[:8]:
        print(f"    size {n}: {sample} ...")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dedupe", action="store_true")
    ap.add_argument("--near-dup", action="store_true")
    ap.add_argument("--invalidate", action="store_true")
    a = ap.parse_args()
    rc = 0
    if a.check or not (a.dedupe or a.near_dup):
        print("=== LEDGER SENTINEL ===")
        rc = check(a.invalidate)
    if a.dedupe:
        print("\n=== DUPLICATE POLICY ===")
        dedupe(True)
    if a.near_dup:
        print("\n=== NEAR-DUPLICATE SCAN ===")
        near_dup()
    sys.exit(rc)


if __name__ == "__main__":
    main()
