#!/usr/bin/env python3
"""
Token meter — the single counting path, plus a reconciliation of every
instrument that has disagreed.

The transcripts record MULTIPLE SNAPSHOTS PER API CALL: the same message id
appears several times with identical input/cache figures and a growing
output_tokens as the response streams. Summing raw records therefore
double-counts input and cache on every call. The correct read is: group by
message id, take that call's FINAL snapshot.

    python3 meter.py --reconcile     # all four instruments, batch 1
    python3 meter.py --run <runid>   # per-item counts for one workflow run
"""

from paths import resolve
import argparse
import glob
import json
import os
import re
import statistics
from collections import defaultdict

WF = resolve("transcripts")
ID = re.compile(r"(agent_\d+#\d+)")
STRICT = re.compile(
    r'"usage":\{"input_tokens":(\d+),"cache_creation_input_tokens":(\d+),'
    r'"cache_read_input_tokens":(\d+),"output_tokens":(\d+)')

FIELDS = ("input_tokens", "cache_creation_input_tokens",
          "cache_read_input_tokens", "output_tokens")


def count_file(path):
    """Returns the four instruments for one agent transcript."""
    txt = open(path, encoding="utf-8", errors="ignore").read()
    item = ID.search(txt)

    # instrument A: naive grep of the literal key
    grep_calls = txt.count('"usage"')

    # instrument B: strict regex, summed
    strict = dict.fromkeys(FIELDS, 0)
    strict_calls = 0
    for m in STRICT.finditer(txt):
        strict_calls += 1
        for k, v in zip(FIELDS, m.groups()):
            strict[k] += int(v)

    # instrument C: JSON parse, every record summed (the double-counting one)
    naive = dict.fromkeys(FIELDS, 0)
    naive_calls = 0
    # instrument D: JSON parse, deduped by message id, final snapshot per call
    per_call = {}
    for line in txt.splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") != "assistant":
            continue
        msg = d.get("message") or {}
        u = msg.get("usage")
        if not u:
            continue
        naive_calls += 1
        for k in FIELDS:
            naive[k] += u.get(k, 0) or 0
        mid = msg.get("id") or f"anon{naive_calls}"
        prev = per_call.get(mid)
        if prev is None or (u.get("output_tokens", 0) or 0) >= (prev.get("output_tokens", 0) or 0):
            per_call[mid] = u
    dedup = dict.fromkeys(FIELDS, 0)
    for u in per_call.values():
        for k in FIELDS:
            dedup[k] += u.get(k, 0) or 0

    def totals(d):
        return {"billable": d["input_tokens"] + d["cache_creation_input_tokens"] + d["output_tokens"],
                "total": sum(d.values()), "output": d["output_tokens"],
                "cache_read": d["cache_read_input_tokens"]}

    return {"item": item.group(1) if item else None,
            "grep_calls": grep_calls, "strict_calls": strict_calls,
            "naive_calls": naive_calls, "dedup_calls": len(per_call),
            "strict": totals(strict), "naive": totals(naive), "dedup": totals(dedup)}


# Physics bound: billable OUTPUT tokens cannot exceed what the model can emit
# in the elapsed wall time. A meter that reports more than this is counting
# something that never came off the wire. Generous ceiling - this is a sanity
# bound, not a performance target.
MAX_OUTPUT_TPS_PER_AGENT = 250.0


def physics_check(total_output, elapsed_s, concurrency):
    """(ok, observed_tps, ceiling) - halts the meter when violated."""
    if elapsed_s <= 0:
        return (True, 0.0, 0.0)
    ceiling = MAX_OUTPUT_TPS_PER_AGENT * max(1, concurrency)
    observed = total_output / elapsed_s
    return (observed <= ceiling, observed, ceiling)


def retry_signals(run):
    """
    Non-blocking attribution for the D-vs-harness residual: count records that
    look like retries or errors. If billed-but-untranscribed retries explain the
    gap, this is where they show. Harness stays authoritative either way.
    """
    sig = {"error_records": 0, "stop_reason_other": 0, "agents": 0}
    for p in glob.glob(os.path.join(WF, run, "agent-*.jsonl")):
        if p.endswith(".meta.json"):
            continue
        sig["agents"] += 1
        for line in open(p, encoding="utf-8", errors="ignore"):
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if d.get("isApiErrorMessage") or d.get("type") == "error":
                sig["error_records"] += 1
            sr = ((d.get("message") or {}).get("stop_reason")
                  if isinstance(d.get("message"), dict) else None)
            if sr and sr not in ("end_turn", "tool_use", None):
                sig["stop_reason_other"] += 1
    return sig


def scan(run):
    out = {}
    for p in glob.glob(os.path.join(WF, run, "agent-*.jsonl")):
        if p.endswith(".meta.json"):
            continue
        c = count_file(p)
        # Fixture and non-item runs carry no agent_NNN#MM id; key them by file
        # so the meter can be validated on runs that aren't solving questions.
        out[c["item"] or os.path.basename(p)] = c
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reconcile", action="store_true")
    ap.add_argument("--run", default="wf_03c21ce5-618")
    ap.add_argument("--harness-total", type=int, default=2391903,
                    help="the harness's own subagent_tokens for this run")
    ap.add_argument("--elapsed", type=float, default=0.0,
                    help="run wall-clock seconds, for the physics bound")
    ap.add_argument("--concurrency", type=int, default=12)
    args = ap.parse_args()

    data = scan(args.run)
    n = len(data)
    print(f"run {args.run}   agents {n}")
    print()
    print(f"{'instrument':>28} {'calls':>7} {'billable':>14} {'total':>14}")
    for lab, ck, tk in (("A grep '\"usage\"'", "grep_calls", None),
                        ("B strict regex", "strict_calls", "strict"),
                        ("C json, all records", "naive_calls", "naive"),
                        ("D json, dedup by msg id", "dedup_calls", "dedup")):
        calls = statistics.mean(d[ck] for d in data.values())
        if tk:
            bil = sum(d[tk]["billable"] for d in data.values())
            tot = sum(d[tk]["total"] for d in data.values())
            print(f"{lab:>28} {calls:>7.1f} {bil:>14,} {tot:>14,}")
        else:
            print(f"{lab:>28} {calls:>7.1f} {'-':>14} {'-':>14}")
    print(f"{'E harness subagent_tokens':>28} {'-':>7} {args.harness_total:>14,} {'-':>14}")

    dedup_bil = sum(d["dedup"]["billable"] for d in data.values())
    dedup_tot = sum(d["dedup"]["total"] for d in data.values())
    print()
    print(f"  D vs E (harness)  : {dedup_bil/args.harness_total:.3f}x on billable")
    print(f"  C vs D            : {sum(d['naive']['total'] for d in data.values())/dedup_tot:.3f}x "
          f"(C double-counts input+cache per streamed snapshot)")
    print(f"  per question (D)  : billable {dedup_bil/n:,.0f}   total {dedup_tot/n:,.0f}   "
          f"calls {statistics.mean(d['dedup_calls'] for d in data.values()):.1f}")

    # --- authority rule -------------------------------------------------
    # The fixture halt is FIXTURE-SCOPE ONLY. A production D-vs-harness gap is
    # logged and bounded, never halted on: the harness figure is authoritative
    # for cost, D is used for structure (calls, cache/output split).
    gap = dedup_bil / args.harness_total if args.harness_total else float("nan")
    print(f"\n  [authority] harness is authoritative for cost; D/harness = {gap:.3f} "
          f"({(gap-1)*100:+.1f}% structural read, logged not halted)")

    out_tokens = sum(d["dedup"]["output"] for d in data.values())
    if args.elapsed:
        ok, obs, ceil = physics_check(out_tokens, args.elapsed, args.concurrency)
        print(f"  [physics]  output {out_tokens:,} tok / {args.elapsed:,.0f}s = {obs:,.0f} tok/s "
              f"vs ceiling {ceil:,.0f} ({args.concurrency} concurrent)")
        if not ok:
            print("  [physics]  *** VIOLATION - meter HALTED, cost reporting suspended ***")
            raise SystemExit(2)

    sig = retry_signals(args.run)
    print(f"  [retries]  error_records={sig['error_records']} "
          f"stop_reason_other={sig['stop_reason_other']} over {sig['agents']} agents")


if __name__ == "__main__":
    main()
