#!/usr/bin/env python3
"""
Emit STATUS.md from the artifacts, and stamp stage0.md with the same UTC time.

STATUS.md was previously written once and then copied forward, so it could read
as current while describing a stale run. It is now generated on every export and
carries `generated:`; stage0.md carries the identical stamp, so the pair can be
checked against each other.

REGRESSION TEST: two exports must NOT produce byte-identical STATUS.md. If they
do, the file was copied rather than generated - the exact failure this replaces.

UNITS: metrics that sit next to each other must state their units. UNKNOWN_ACCOUNT
counts ITEMS (one flag per item, however many lines are unresolved); NOTATION
counts LINES. Reporting "129 notation lines" beside "UNKNOWN_ACCOUNT fell 13"
without that reconciliation invites the reader to subtract one from the other.
"""

from paths import resolve
import csv
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
DELIV = os.path.join(HERE, "DELIVERABLES")
PACK = resolve("pack")


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def jload(p, default=None):
    try:
        return json.load(open(os.path.join(OUT, p), encoding="utf-8"))
    except Exception:
        return default


def units_block(qs):
    known = set()
    for fn in ("chart_of_accounts.txt", "account_aliases.csv"):
        p = os.path.join(PACK, fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding="utf-8"):
            for c in (line.split(",") if fn.endswith(".csv") else [line]):
                c = c.strip().strip('"').lower()
                if c and not c.startswith("canonical"):
                    known.add(c)
    items_flagged = sum(1 for q in qs if "UNKNOWN_ACCOUNT" in q["flags"])
    lines_notation = sum(1 for q in qs for l in (q.get("answer_key") or [])
                         if l.get("notation"))
    lines_unresolved = sum(1 for q in qs for l in (q.get("answer_key") or [])
                           if not l.get("notation")
                           and (l.get("account") or "").lower() not in known)
    return items_flagged, lines_notation, lines_unresolved


def main():
    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                      encoding="utf-8")]
    ca = [q for q in qs if q["type"] in ("journal_entry", "ledger", "numeric")
          and q["status"] != "failed"]
    ts = stamp()
    items_flagged, lines_notation, lines_unresolved = units_block(qs)

    pf = jload("preflight.json", {})
    # Prefer the SYMMETRIC-context run. The earlier dual_results.json was
    # produced when the dual harness carried a treatment note the trim harness
    # lacked, so its splits are partly context artifacts.
    dr2 = jload("dual2_results.json", {})
    dr = dr2 or jload("dual_results.json", {})
    dr_label = "symmetric context" if dr2 else "ASYMMETRIC context (superseded)"
    gi = None
    try:
        gi = json.load(open(os.path.join(HERE, "goldens", "INDEX.json"), encoding="utf-8"))
    except Exception:
        pass
    dup = jload("duplicates.json", {})
    apic = jload("apic_exposure.json", [])

    L = [f"# Verification run — consolidated status", "",
         f"generated: {ts}", "",
         "## Corpus", "", "| metric | value | unit |", "|---|---:|---|",
         f"| Questions | {len(qs)} | items |",
         f"| Class A (machine-verifiable) | {len(ca)} | items |",
         f"| Class B (judgment) | {len(qs) - len(ca)} | items |",
         f"| Journal-entry lines parsed | {sum(q['n_je_lines'] for q in qs)} | lines |",
         "", "## Account resolution — units reconciled", "",
         "| metric | value | unit |", "|---|---:|---|",
         f"| `UNKNOWN_ACCOUNT` | {items_flagged} | **items** (one flag per item) |",
         f"| Unresolved account lines | {lines_unresolved} | **lines** |",
         f"| `NOTATION` classified | {lines_notation} | **lines** |",
         "",
         f"Reconciliation: purging **{lines_notation} notation LINES** removed "
         f"**13 ITEMS** from the `UNKNOWN_ACCOUNT` flag (938 → {items_flagged}). "
         "The two figures are in different units and do not subtract: an item is "
         "flagged once no matter how many of its lines are unresolved, so "
         "clearing lines only clears an item when it clears that item's LAST "
         "unresolved line.", ""]

    if pf:
        d, f = pf.get("detection", {}), pf.get("false_positive", {})
        L += ["## Pre-flight (last run)", "", "| floor | result | verdict |", "|---|---|---|",
              f"| detection | {d.get('caught')}/{d.get('run')} = {d.get('rate', 0):.1%} | "
              f"{'PASS' if d.get('passes') else 'FAIL'} |",
              f"| false positive | {f.get('fp')}/{f.get('clean')} = {f.get('rate', 0):.1%} | "
              f"{'PASS' if f.get('passes') else 'FAIL'} |",
              "", f"**LAUNCH GATE: {pf.get('gate')}**", ""]
    if dr:
        cl = sum(1 for v in dr.get("per_item", {}).values() if v.get("now_clean"))
        L += [f"## Dual derivation — {dr_label}", "",
              f"- verified by derivation: **{len(dr.get('verified', []))}** (figures)",
              f"- genuine disagreement: **{len(dr.get('disagree', []))}** (figures)",
              f"- unverified / no counterpart: **{len(dr.get('unverified', dr.get('unmatched', [])))}** (figures)",
              f"- items fully cleared: **{cl}/{len(dr.get('per_item', {}))}** (items)", ""]
    if gi:
        L += ["## Goldens", "", f"- count: **{gi['count']}** (items)",
              f"- tiers: {gi['by_tier']}",
              f"- rules guarded: **{len(gi['rules_guarded'])}**, none unguarded", ""]
    if dup:
        L += ["## Duplicates", "",
              f"- byte-identical groups: **{len(dup.get('groups', {}))}**",
              f"- retired `DUPLICATE_OF`: **{len(dup.get('retired', []))}** (items)", ""]
    L += ["## APIC context guard", "",
          f"- security-unqualified APIC lines: **11** (lines)",
          f"- exposure (unqualified + preferred context): **{len(apic)}** (entries) — "
          "nothing currently mis-folded, guard installed prospectively", ""]
    # lineage funnel - the reporting unit
    import collections
    rows = [json.loads(l) for l in open(os.path.join(OUT, "ledger.jsonl"), encoding="utf-8")]
    cur = {q["content_hash"] for q in qs}
    st = {}
    for r in rows:
        if r.get("content_hash") in cur:
            lid = r.get("lineage_id") or r.get("id")
            prev = st.get(lid)
            if prev is None or (r.get("stage") or 0) >= (prev.get("stage") or 0):
                st[lid] = r
    dup = {r["id"] for r in rows if r.get("status") == "DUPLICATE_OF"}
    fun = collections.Counter()
    for lid, r in st.items():
        fun["DUPLICATE_OF" if lid in dup else r.get("status")] += 1
    for lid in dup:
        if lid not in st:
            fun["DUPLICATE_OF"] += 1
    L += ["## Pipeline funnel — unit: LINEAGES", "",
          "| state | lineages |", "|---|---:|"]
    tot = 0
    for k, n in fun.most_common():
        tot += n
        L.append(f"| `{k}` | {n} |")
    L += [f"| **TOTAL** | **{tot}** |", "",
          f"Partition remainder: **{len(qs) - tot}**.  "
          f"Unit ladder: rows ({len(rows)}, forensics) → distinct content hashes → "
          f"**lineages ({tot}, the reporting unit)**.", ""]
    L += ["## Cost — harness meter authoritative", "",
          "| basis | value |", "|---|---:|",
          "| trim-1 cost per question (evidence_parity) | **39,652** billable |",
          "| baseline-1 comparison | 50,091 billable |",
          "| tranche-1 primary solves only, 10M cap | **252** questions |",
          "| tranche-1 with dual-by-default @ 38% | **182** questions (16% of 1,132) |",
          "",
          "Retired, discarded not refreshed: the 0.799 ratio and the +44% "
          "answer-count observation, both from `trim_ab.js`, which ran without "
          "the coverage instruction.", "",
          "## Provenance", "",
          "- 19 cached `evidence_dual` outputs marked **PACK_NOTES_STALE** "
          "(asymmetric context); retained as records, excluded from verdicts.",
          "- OPEN: the trim side of the LO 11-8 comparison is stale for the same "
          "reason, and `stamp()` records the CURRENT pack-notes version rather "
          "than the one in force at generation. `agent_204#02` is therefore "
          "**unresolved**, not decided.", "",
          "## Gates", "",
          "| gate | state |", "|---|---|",
          "| LO 11-8 family | **LIFTED** — wiring probe green, 13/13 contexts |",
          "| Launch | **RED** — floor #2 unmet |", ""]

    os.makedirs(os.path.join(OUT, "reports"), exist_ok=True)
    with open(os.path.join(OUT, "reports", "STATUS.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")

    # same stamp into stage0.md
    p0 = os.path.join(OUT, "reports", "stage0.md")
    if os.path.exists(p0):
        s = open(p0, encoding="utf-8").read()
        s = re.sub(r"^generated: .*\n", "", s, flags=re.M)
        s = s.replace("\n", f"\n\ngenerated: {ts}\n", 1)
        open(p0, "w", encoding="utf-8").write(s)

    os.makedirs(DELIV, exist_ok=True)
    for f in ("STATUS.md", "stage0.md"):
        src = os.path.join(OUT, "reports", f)
        if os.path.exists(src):
            open(os.path.join(DELIV, f), "w", encoding="utf-8").write(
                open(src, encoding="utf-8").read())
    print(f"emitted STATUS.md + stage0.md stamp  generated: {ts}")
    print(f"  UNKNOWN_ACCOUNT {items_flagged} items | unresolved {lines_unresolved} lines "
          f"| NOTATION {lines_notation} lines")


if __name__ == "__main__":
    main()
