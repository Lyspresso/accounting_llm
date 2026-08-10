#!/usr/bin/env python3
"""
Batch-composition analysis.

Answers, with numbers rather than assertion:
  2. pass rate and failure-mode mix per pack / chapter / LO
  3. SOLVER_MISMATCH figures clustered into generation families by stem
     similarity, so adjudication targets root causes not instances
  4. attribution of the batch-2 wall-clock and token drift: question-length
     composition vs harness behaviour, using real per-agent token counts
  5. cost projection stratified by chapter, with error bars, replacing the
     blended per-question extrapolation
"""

from paths import resolve
import glob
import json
import math
import os
import re
import statistics
from collections import Counter, defaultdict
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
WF = resolve("transcripts")
RUNS = {1: "wf_03c21ce5-618", 2: "wf_cca2bc4f-61f"}

ID_RE = re.compile(r'Your item id is \\?"(agent_\d+#\d+)\\?"')
USAGE_RE = re.compile(
    r'"usage":\{"input_tokens":(\d+),"cache_creation_input_tokens":(\d+),'
    r'"cache_read_input_tokens":(\d+),"output_tokens":(\d+)')
LO_RE = re.compile(r"LO\s*(\d+)-(\d+)")
WORD = re.compile(r"[a-z]{3,}")

STRUCT_KINDS = ("JE_LINE_NOT_IN_KEY", "KEY_LINE_NOT_IN_SOLVER")
NUM_KINDS = ("SOLVER_MISMATCH",)


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def agent_tokens():
    """item id -> token counts, read from the per-agent transcripts."""
    out = {}
    for batch, run in RUNS.items():
        for path in glob.glob(os.path.join(WF, run, "agent-*.jsonl")):
            if path.endswith(".meta.json"):
                continue
            try:
                txt = open(path, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            m = ID_RE.search(txt)
            if not m:
                continue
            inp = cc = cr = outp = 0
            for u in USAGE_RE.finditer(txt):
                inp += int(u.group(1)); cc += int(u.group(2))
                cr += int(u.group(3)); outp += int(u.group(4))
            out[m.group(1)] = {"batch": batch, "input": inp, "cache_creation": cc,
                               "cache_read": cr, "output": outp,
                               "billable_in": inp + cc, "total": inp + cc + cr + outp}
    return out


def chapter_of(q):
    for c in q.get("concepts") or []:
        m = LO_RE.search(c)
        if m:
            return int(m.group(1))
    m = LO_RE.search(q.get("stem", ""))
    return int(m.group(1)) if m else 0


def lo_of(q):
    for c in q.get("concepts") or []:
        m = LO_RE.search(c)
        if m:
            return f"LO {m.group(1)}-{m.group(2)}"
    return "LO ?"


def main():
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}
    man = json.load(open(os.path.join(OUT, "stage1_manifest.json"), encoding="utf-8"))
    batch_of = {i["id"]: i["batch"] for i in man["items"]}

    rows = {}
    for b in (1, 2):
        d = json.load(open(os.path.join(OUT, f"stage1_v3_batch{b}_results.json"),
                           encoding="utf-8"))
        for r in d["rows"]:
            rows[r["id"]] = r

    toks = agent_tokens()

    # ---------------- 2. by chapter -------------------------------------
    per_ch = defaultdict(lambda: {"n": 0, "pass": 0, "struct": 0, "numeric": 0,
                                  "b1": 0, "b2": 0, "ids": []})
    for qid, r in rows.items():
        q = qs[qid]
        ch = chapter_of(q)
        s = per_ch[ch]
        s["n"] += 1
        s["ids"].append(qid)
        s["pass"] += (r.get("status") == "machine_passed")
        s[f"b{batch_of[qid]}"] += 1
        for i in r.get("issues", []):
            if i["kind"] in STRUCT_KINDS:
                s["struct"] += 1
            elif i["kind"] in NUM_KINDS:
                s["numeric"] += 1

    print("=" * 78)
    print("2. BY CHAPTER — pass rate and failure-mode mix")
    print("=" * 78)
    print(f"{'ch':>3} {'n':>3} {'b1/b2':>7} {'pass':>10}  {'struct':>7} {'numeric':>8}")
    for ch in sorted(per_ch, key=lambda c: -(per_ch[c]["struct"] + per_ch[c]["numeric"])):
        s = per_ch[ch]
        lo, hi = wilson(s["pass"], s["n"])
        print(f"{ch:>3} {s['n']:>3} {s['b1']:>3}/{s['b2']:<3} "
              f"{s['pass']}/{s['n']} {lo:>4.0%}-{hi:<4.0%} {s['struct']:>7} {s['numeric']:>8}")

    print("\n  chapters driving STRUCTURAL misses:")
    for ch, s in sorted(per_ch.items(), key=lambda kv: -kv[1]["struct"])[:5]:
        if s["struct"]:
            print(f"    ch {ch:>2}: {s['struct']:>3} struct   (b1={s['b1']} b2={s['b2']})")
    print("  chapters driving NUMERIC misses:")
    for ch, s in sorted(per_ch.items(), key=lambda kv: -kv[1]["numeric"])[:5]:
        if s["numeric"]:
            print(f"    ch {ch:>2}: {s['numeric']:>3} numeric  (b1={s['b1']} b2={s['b2']})")

    # ---------------- 3. SOLVER_MISMATCH families -----------------------
    mism = []
    for qid, r in rows.items():
        n = sum(1 for i in r.get("issues", []) if i["kind"] == "SOLVER_MISMATCH")
        if n:
            mism.append((qid, n))
    toks_of = {qid: set(WORD.findall(qs[qid]["stem"].lower())) for qid, _ in mism}

    fams, used = [], set()
    for qid, n in sorted(mism, key=lambda x: -x[1]):
        if qid in used:
            continue
        fam = [(qid, n)]
        used.add(qid)
        for other, m in mism:
            if other in used:
                continue
            a, b = toks_of[qid], toks_of[other]
            jac = len(a & b) / max(1, len(a | b))
            same_lo = lo_of(qs[qid]) == lo_of(qs[other])
            if jac >= 0.45 or (same_lo and jac >= 0.30):
                fam.append((other, m))
                used.add(other)
        fams.append(fam)

    print("\n" + "=" * 78)
    print("3. SOLVER_MISMATCH FAMILIES (adjudicate families, not instances)")
    print("=" * 78)
    print(f"  {len(mism)} items carry mismatches -> {len(fams)} families")
    for f in sorted(fams, key=lambda f: -sum(n for _, n in f))[:12]:
        head = f[0][0]
        print(f"  family n={len(f):>2} figures={sum(n for _, n in f):>3}  "
              f"{lo_of(qs[head]):9s} {qs[head]['heading'][:52]}")
        if len(f) > 1:
            for qid, n in f[1:]:
                print(f"        sibling {qid:14s} {lo_of(qs[qid]):9s} figures={n}")

    # ---------------- 4. drift attribution ------------------------------
    print("\n" + "=" * 78)
    print("4. DRIFT ATTRIBUTION — batch 1 vs batch 2")
    print("=" * 78)

    def stat(b, fn):
        v = [fn(qid) for qid in rows if batch_of[qid] == b]
        v = [x for x in v if x is not None]
        return (statistics.mean(v) if v else 0,
                statistics.median(v) if v else 0, len(v))

    metrics = [
        ("stem chars", lambda qid: len(qs[qid]["stem"])),
        ("key JE lines", lambda qid: qs[qid]["n_je_lines"]),
        ("solution chars", lambda qid: len(qs[qid].get("solution", ""))),
        ("output tokens", lambda qid: toks.get(qid, {}).get("output")),
        ("billable input", lambda qid: toks.get(qid, {}).get("billable_in")),
        ("cache read", lambda qid: toks.get(qid, {}).get("cache_read")),
        ("total tokens", lambda qid: toks.get(qid, {}).get("total")),
    ]
    print(f"{'metric':>16} {'b1 mean':>12} {'b2 mean':>12} {'delta':>9}")
    for name, fn in metrics:
        m1, _, _ = stat(1, fn)
        m2, _, _ = stat(2, fn)
        d = (m2 / m1 - 1) * 100 if m1 else 0
        print(f"{name:>16} {m1:>12,.0f} {m2:>12,.0f} {d:>8.1f}%")

    # ---------------- 5. stratified cost --------------------------------
    print("\n" + "=" * 78)
    print("5. COST PROJECTION STRATIFIED BY CHAPTER")
    print("=" * 78)
    allq = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                        encoding="utf-8")]
    remaining = defaultdict(int)
    for q in allq:
        if q["type"] in ("journal_entry", "ledger", "numeric") and q["status"] != "failed":
            if q["id"] not in rows:
                remaining[chapter_of(q)] += 1

    tot_lo = tot_mid = tot_hi = 0
    unpriced = 0
    print(f"{'ch':>3} {'sampled':>8} {'mean tok':>10} {'sd':>9} {'remain':>7} {'projection':>26}")
    for ch in sorted(set(list(per_ch) + list(remaining))):
        sampled = [toks[qid]["total"] for qid in per_ch.get(ch, {}).get("ids", [])
                   if qid in toks]
        rem = remaining.get(ch, 0)
        if not sampled:
            unpriced += rem
            continue
        m = statistics.mean(sampled)
        sd = statistics.pstdev(sampled) if len(sampled) > 1 else 0
        se = sd / math.sqrt(len(sampled)) if sampled else 0
        lo, hi = (m - 1.96 * se) * rem, (m + 1.96 * se) * rem
        tot_lo += lo; tot_mid += m * rem; tot_hi += hi
        if rem:
            print(f"{ch:>3} {len(sampled):>8} {m:>10,.0f} {sd:>9,.0f} {rem:>7} "
                  f"{m*rem/1e6:>8.1f}M [{lo/1e6:.1f}-{hi/1e6:.1f}M]")
    blended = statistics.mean([t["total"] for t in toks.values()]) if toks else 0
    total_rem = sum(remaining.values())
    print(f"\n  stratified total : {tot_mid/1e6:>6.1f}M  "
          f"[{tot_lo/1e6:.1f} - {tot_hi/1e6:.1f}M]  over {total_rem-unpriced} priced questions")
    print(f"  blended estimate : {blended*total_rem/1e6:>6.1f}M  "
          f"(mean {blended:,.0f} tok/q x {total_rem})")
    print(f"  unpriced (no chapter sampled in pilot): {unpriced} questions")


if __name__ == "__main__":
    main()
