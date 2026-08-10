#!/usr/bin/env python3
"""
Formalize tonight's adjudications into goldens/, and package the operator's
20-item hand-check sample.

Goldens are the only thing that makes a false-positive floor real: without
hand-confirmed items, a probe suite can measure detection but not whether the
comparator cries wolf. Every item adjudicated tonight becomes one, carrying
per-figure ground truth and the ruling that produced it.

Sample composition (as ordered): 10 machine-passed, 5 flips, 5 KEY_SILENT-heavy.
"""

import glob
import json
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
GOLD = os.path.join(HERE, "goldens")
TASKS = ("/private/tmp/claude-501/-Users-lyspressopro/"
         "72130472-88ff-42d4-8c91-421c401768ce/tasks")

# Adjudicated tonight, with the ruling that settled each one.
ADJUDICATED = {
    # chapter 17 lease cohort - zero genuine accounting disagreements
    "agent_022#01": ("ch17", "PASS", "no disagreement; NON_NUMERIC_ANSWER only"),
    "agent_019#00": ("ch17", "KEY_SILENT", "key states figures in LaTeX prose; extraction artifact"),
    "agent_285#00": ("ch17", "EXTRACTION_BUG", "parser lifted a 4-line optional-form table as the whole key; solver agreed on all <figure> figures"),
    "agent_151#01": ("ch17", "BOTH_DEFENSIBLE", "<figure>/<figure> round-then-carry vs carry-then-round; chapter blesses both"),
    "agent_283#02": ("ch17", "BOTH_DEFENSIBLE", "<figure> same rounding convention; plus account-name gaps"),
    "agent_150#02": ("ch17", "KEY_SILENT", "key declines to state Option 3 PV; solver correct"),
    # parity flips
    "agent_002#03": ("parity", "NEITHER", "solver pooled two securities; key splits per security; aggregation equivalence"),
    "agent_032#01": ("parity", "NEITHER", "LaTeX {,} made <figure>/<figure>/<figure> invisible; both solvers correct"),
    "agent_303#02": ("parity", "NEITHER", "comparator at fault"),
    "agent_043#00": ("parity", "NEITHER", "comparator at fault"),
    "agent_204#02": ("parity", "BASELINE", "baseline ruled right"),
    "agent_130#00": ("parity", "KEY_WRONG", "genuine key defect - the only one found tonight"),
    "agent_392#00": ("parity", "BASELINE", "baseline ruled right"),
    # the trim A/B flip
    "agent_052#01": ("trim-ab", "KEY_SILENT", "FIFO/LIFO Oct <figure> running balances <figure>/<figure> correct from key's own layers; key never totals them"),
}


def load_questions():
    return {q["id"]: q for q in (json.loads(l) for l in
            open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}


def evidence(qid):
    base = os.path.join(OUT, "evidence", qid.replace("#", "_"))
    par = os.path.join(OUT, "evidence_parity", qid.replace("#", "_"))
    out = {}
    for lab, d in (("baseline", base), ("trim", par)):
        p = os.path.join(d, "solver_output.json")
        if os.path.exists(p):
            try:
                out[lab] = json.load(open(p, encoding="utf-8"))
            except json.JSONDecodeError:
                pass
    return out


def main():
    os.makedirs(GOLD, exist_ok=True)
    qs = load_questions()

    # ---- goldens ------------------------------------------------------
    written = 0
    for qid, (source, ruling, why) in ADJUDICATED.items():
        q = qs.get(qid)
        if not q:
            continue
        ev = evidence(qid)
        g = {
            "id": qid, "pack_id": q["pack_id"], "source": source,
            "ruling": ruling, "rationale": why,
            "adjudicated": "2026-08-07",
            "comparator_version_at_adjudication": "3.4",
            "expected_verdict": "PASS" if ruling in
                ("PASS", "KEY_SILENT", "BOTH_DEFENSIBLE", "NEITHER", "EXTRACTION_BUG")
                else "FAIL",
            "is_true_defect": ruling == "KEY_WRONG",
            "stem": q["stem"],
            "key_solution": q.get("solution", ""),
            "key_lines": q.get("answer_key"),
            "solver_outputs": ev,
        }
        with open(os.path.join(GOLD, f"{qid.replace('#', '_')}.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(g, fh, indent=1)
        written += 1

    # ---- 20-item hand-check sample ------------------------------------
    rng = random.Random(343)
    res = json.load(open(os.path.join(OUT, "parity50_results.json"), encoding="utf-8"))
    rows = res["rows"]
    flips = {f["id"] for f in res["flips"]}

    passed = [r for r in rows if r.get("baseline-1", {}).get("verdict") == "machine_passed"
              and r["id"] not in flips]
    # Compute the key-silent load directly. compare_parity.py does not write
    # comparison.json into the parity evidence dirs, so reading them found
    # nothing and silently emptied this bucket.
    import sys
    sys.path.insert(0, HERE)
    import compare_stage1_v3 as C
    known, amap = C.load_known(), C.load_alias_map(False)
    silent = []
    for r in rows:
        qid = r["id"]
        q = qs.get(qid)
        p = os.path.join(OUT, "evidence_parity", qid.replace("#", "_"), "solver_output.json")
        if not q or not os.path.exists(p):
            continue
        try:
            sol = json.load(open(p, encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        iss, _ = C.compare(sol, q, known, amap)
        n = sum(1 for i in iss if i["kind"] in ("KEY_SILENT_DERIVED", "JE_AGGREGATED"))
        if n:
            silent.append((n, qid))
    silent.sort(reverse=True)

    rng.shuffle(passed)
    pick_pass = [r["id"] for r in passed[:10]]
    pick_flip = sorted(flips)[:5]
    pick_silent = [q for _, q in silent if q not in pick_pass and q not in pick_flip][:5]
    sample = ([("machine_passed", i) for i in pick_pass] +
              [("flip", i) for i in pick_flip] +
              [("key_silent_heavy", i) for i in pick_silent])

    lines = [
        "# Hand-check sample — 20 items", "",
        "Composition: 10 machine-passed, 5 parity flips, 5 KEY_SILENT-heavy.",
        "Confirmations feed `goldens/` and make the false-positive floor real.", "",
        "For each item: read the Required parts, check the solver's figures against",
        "the key, and mark the verdict. **Where you disagree with the machine verdict,",
        "that is the finding** — it is the only measurement of the comparator's",
        "false-positive rate that does not come from the comparator itself.", "",
        "| # | item | ch | category | machine verdict | your verdict | notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for n, (cat, qid) in enumerate(sample, 1):
        row = next((r for r in rows if r["id"] == qid), {})
        v = row.get("baseline-1", {}).get("verdict", "?")
        lines.append(f"| {n} | `{qid}` | {row.get('ch','?')} | {cat} | {v} |  |  |")

    lines += ["", "---", ""]
    for n, (cat, qid) in enumerate(sample, 1):
        q = qs.get(qid)
        if not q:
            continue
        row = next((r for r in rows if r["id"] == qid), {})
        ev = evidence(qid)
        lines += [
            f"## {n}. `{qid}` — chapter {row.get('ch','?')} — {cat}", "",
            f"**Machine verdict:** baseline `{row.get('baseline-1',{}).get('verdict','?')}`, "
            f"trim `{row.get('trim-1',{}).get('verdict','?')}`  ",
            f"**Required parts detected:** {', '.join(row.get('required_parts', [])) or '—'}  ",
            f"**Coverage:** baseline {row.get('baseline-1',{}).get('coverage','—')}, "
            f"trim {row.get('trim-1',{}).get('coverage','—')}", "",
            "### Question", "", q["stem"].strip(), "",
            "### The key's answer", "", q.get("solution", "").strip()[:6000], "",
        ]
        for lab, sol in ev.items():
            lines += [f"### Blind solver ({lab}) — figures", ""]
            for a in (sol.get("answers") or [])[:24]:
                lines.append(f"- `{a.get('label')}` = **{a.get('value')}**")
            lines.append("")
        hard = row.get("baseline-1", {}).get("hard") or []
        if hard:
            lines += ["### What the comparator flagged", ""]
            for i in hard:
                lines.append(f"- `{i.get('kind')}` {i.get('label') or i.get('solver') or ''}")
            lines.append("")
        lines += ["**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  "
                  "☐ machine wrong (missed a real error)", "", "**Notes:**", "", "---", ""]

    path = os.path.join(OUT, "reports", "hand_check_sample.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"goldens written      : {written} -> {GOLD}/")
    print(f"  true defects       : {sum(1 for v in ADJUDICATED.values() if v[1] == 'KEY_WRONG')}")
    print(f"  comparator-at-fault: {sum(1 for v in ADJUDICATED.values() if v[1] in ('NEITHER','KEY_SILENT','EXTRACTION_BUG'))}")
    print(f"hand-check sample    : {len(sample)} items -> {path}")
    print(f"  machine_passed {len(pick_pass)} / flips {len(pick_flip)} / key_silent {len(pick_silent)}")


if __name__ == "__main__":
    main()
