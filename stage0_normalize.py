#!/usr/bin/env python3
"""
Stage 0 - Normalize (budget mode, PIPELINE_VERSION 1.2)

100% of questions, pure Python, zero LLM spend. Per the budget prompt this stage
is never sampled and never cut: it is nearly free, and the leak/degeneracy and
format-drift defenses live here. Its job is to hand Stage 1 a clean corpus and to
pause bad packs BEFORE any model looks at them.

Outputs (under OUTPUT_DIR):
    questions.jsonl        one schema object per question
    ledger.jsonl           content-hash-keyed state
    pack_profiles.json     per-pack format statistics
    reports/stage0.md      human summary

Run:  python3 stage0_normalize.py
"""

from paths import resolve
import hashlib
import json
import ledger_io
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = resolve("questions")


def _packs_dir(base):
    """
    The directory that actually holds agent_NNN.md.

    This was `os.path.join(CORE, "results")`, which appended a subdirectory to a
    path that already pointed AT the packs - so it resolved to `.../results/
    results` and stage 0 could not find a corpus at all. It went unnoticed
    because stage 0 is a one-time normalisation step and is not in the fixture
    suite. Checked layouts, in order, then the base itself.
    """
    for sub in ("", "source-packs", "results"):
        cand = os.path.join(base, sub) if sub else base
        if os.path.isdir(cand) and any(
                re.fullmatch(r"agent_\d+\.md", f) for f in os.listdir(cand)):
            return cand
    return base


QUESTIONS = _packs_dir(CORE)
OUT = os.path.join(HERE, "out")
PACK = resolve("pack")

# blind_strip.py may sit beside this file (repo layout) or beside the corpus
# (original working-tree layout). Both are added rather than guessed at.
for _p in (HERE, CORE, os.path.dirname(QUESTIONS)):
    if _p and _p not in sys.path:
        sys.path.insert(0, _p)
# Reuse the audited splitter: its answer-region rules were hardened against four
# real leak bugs in this exact corpus, so Stage 0 must not re-derive them.
from blind_strip import strip_pack, ITEM_START  # noqa: E402

PIPELINE_VERSION = "1.2"

LO_RE = re.compile(r"^\*\*LO:\*\*\s*(.+?)\s*$", re.M)
CONCEPT_RE = re.compile(r"^\*\*Concept:\*\*\s*(.+?)\s*$", re.M)
OPTION_RE = re.compile(r"^\s*[-*]?\s*([A-E])\)\s+(.*?)\s*$", re.M)
MC_ANSWER_RE = re.compile(r"\*\*Answer\s*:?\*\*\s*\**\s*([A-E])\b", re.I)
JE_HEADER_RE = re.compile(r"^\|\s*Account\s*\|\s*Debit\s*\|\s*Credit\s*\|", re.I | re.M)
TABLE_ROW_RE = re.compile(r"^\|(.+)\|\s*$", re.M)
MONEY_RE = re.compile(r"-?\$?\s*\d[\d,]*(?:\.\d+)?")
ASC_RE = re.compile(r"\bASC\s*\d{3}(?:-\d+)*", re.I)
DATE_RE = re.compile(
    r"(?:January|February|March|April|May|June|July|August|September|October|"
    r"November|December)\s+\d{1,2}(?:,\s*(?:Year\s*\d|\d{4}))?|Year\s*\d|\d{1,2}/\d{1,2}/\d{2,4}",
    re.I,
)
WORD_RE = re.compile(r"[a-z0-9]+")
# An acceptable-form notation names two permissible accounts, e.g.
# "Cash (or Salaries Payable)". It can never resolve against a chart.
NOTATION_RE = re.compile(r"\(\s*or\b|\bor\s*\)", re.I)


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def money(tok):
    try:
        return float(tok.replace("$", "").replace(",", "").strip())
    except ValueError:
        return None


def load_aliases():
    """canonical account name -> set of accepted variants (lowercased)."""
    known = set()
    p = os.path.join(PACK, "chart_of_accounts.txt")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                known.add(line.lower())
    p = os.path.join(PACK, "account_aliases.csv")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            for cell in line.strip().split(","):
                cell = cell.strip().strip('"')
                if cell and not cell.lower().startswith("canonical"):
                    known.add(cell.lower())
    return known


def je_header(raw):
    """
    (account_col, debit_col, credit_col) if this row is a journal-entry header.

    Header-driven rather than a fixed "| Account | Debit | Credit |" match: the
    corpus also writes "| Date | Account | Debit | Credit |", "| | Debit |
    Credit |" and variants carrying a Balance column. A fixed match skipped 151
    tables across 78 items - and on one of them the parser then lifted an
    "Optional two-part form" side table as the ENTIRE answer key, discarding the
    real 20-line key and failing a solver that agreed with it exactly.
    """
    m = TABLE_ROW_RE.match(raw)
    if not m:
        return None
    cells = [c.strip().lower() for c in m.group(1).split("|")]
    dr_i = next((i for i, c in enumerate(cells) if re.search(r"\bdebit\b", c)), None)
    cr_i = next((i for i, c in enumerate(cells) if re.search(r"\bcredit\b", c)), None)
    if dr_i is None or cr_i is None or dr_i == cr_i:
        return None
    named = [i for i, c in enumerate(cells)
             if re.search(r"account|description|component|item|particular", c)]
    if named:
        acct_i = named[0]
    else:
        # the last non-date column before the debit column, else the first
        cand = [i for i in range(dr_i) if not re.search(r"\bdate\b", cells[i])]
        acct_i = cand[-1] if cand else 0
    return (acct_i, dr_i, cr_i)


def parse_je_lines(answer_text):
    """
    Parse answer tables into (date, account, dr|cr, amount) lines.
    Returns (lines, n_tables). A journal_entry item that yields no lines is
    SCHEMA_FAIL per the spec.
    """
    lines, n_tables, cur_date = [], 0, None
    in_je = False
    for raw in answer_text.splitlines():
        d = DATE_RE.search(raw)
        if d and not raw.strip().startswith("|"):
            cur_date = d.group(0)
        hdr = je_header(raw)
        if hdr:
            in_je, n_tables = True, n_tables + 1
            acct_i, dr_i, cr_i = hdr
            continue
        if in_je:
            m = TABLE_ROW_RE.match(raw)
            if not m:
                in_je = False
                continue
            cells = [c.strip() for c in m.group(1).split("|")]
            if not cells or set("".join(cells)) <= set("-: "):
                continue
            if max(dr_i, cr_i) >= len(cells):
                continue
            # Credit lines are indented with HTML entities in the source
            # markdown, so the parsed account name carried "&nbsp;&nbsp;" as
            # part of the string: 175 lines across 42 distinct spellings, every
            # one of them an UNKNOWN_ACCOUNT that is really just Cash.
            acct = cells[acct_i] if acct_i < len(cells) else ""
            acct = re.sub(r"&nbsp;|&#160;|&emsp;|&ensp;|&thinsp;", " ", acct)
            acct = re.sub(r"&amp;", "&", acct)
            acct = re.sub(r"&[a-z]+;|&#\d+;", " ", acct)
            acct = re.sub(r"[*_`]", "", acct)
            acct = re.sub(r"\s+", " ", acct).strip()
            if not acct or acct.startswith("*"):
                continue
            dr = money(cells[dr_i]) if cells[dr_i] else None
            cr = money(cells[cr_i]) if cells[cr_i] else None
            if dr:
                lines.append({"date": cur_date, "account": acct, "side": "dr", "amount": dr})
            if cr:
                lines.append({"date": cur_date, "account": acct, "side": "cr", "amount": cr})
    return lines, n_tables


def ngrams(text, n=8):
    w = WORD_RE.findall(text.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def classify_type(stem, answer, options):
    if options and MC_ANSWER_RE.search(answer):
        return "mcq"
    if JE_HEADER_RE.search(answer):
        return "journal_entry"
    if MONEY_RE.search(answer):
        return "numeric"
    return "short_answer"


def difficulty_of(qtype, stem, answer):
    """Provisional tier; Stage 4 LO mapping may revise it."""
    if qtype == "mcq":
        return "understand"
    parts = len(re.findall(r"^\s*[a-h]\.\s", stem, re.M))
    if parts >= 4 or "schedule" in stem.lower():
        return "analyze"
    return "apply"


def main():
    aliases = load_aliases()
    packs = sorted(f for f in os.listdir(QUESTIONS) if re.fullmatch(r"agent_\d+\.md", f))

    questions, ledger = [], []
    per_pack = defaultdict(lambda: {
        "items": 0, "parsed": 0, "stem_len": [], "sol_len": [], "overlap": [],
        "no_key": 0, "schema_fail": 0, "types": Counter(), "unknown_accounts": 0,
    })
    reasons = Counter()

    for fn in packs:
        pack_id = fn[:-3]
        raw_path = os.path.join(QUESTIONS, fn)
        text = open(raw_path, encoding="utf-8").read()
        stem_md, held = strip_pack(text)

        # Re-split the stem side by item so each question keeps its own text.
        stem_chunks, cur, head = {}, [], None
        for ln in stem_md.splitlines():
            if ITEM_START.match(ln):
                if head:
                    stem_chunks[head.strip()] = "\n".join(cur)
                head, cur = ln, [ln]
            elif head:
                cur.append(ln)
        if head:
            stem_chunks[head.strip()] = "\n".join(cur)

        for idx, item in enumerate(held):
            heading = item["heading"]
            answer = item["answer"]
            stem = stem_chunks.get(heading, "")
            prof = per_pack[pack_id]
            prof["items"] += 1

            flags, tier = [], None
            options = [(m.group(1), m.group(2)) for m in OPTION_RE.finditer(stem)]
            qtype = classify_type(stem, answer, options)
            prof["types"][qtype] += 1

            # --- deterministic quarantine checks -------------------------------
            if not answer.strip():
                flags.append("NO_KEY")
                tier = "failed"
                prof["no_key"] += 1
            if not stem.strip():
                flags.append("SCHEMA_FAIL")
                tier = "failed"
                prof["schema_fail"] += 1

            if options:
                seen = Counter(re.sub(r"\W+", " ", o[1]).strip().lower() for o in options)
                if any(v > 1 for v in seen.values()):
                    flags.append("DUP_OPTIONS")
                    tier = "failed"
                letters = MC_ANSWER_RE.findall(answer)
                # One heading may legitimately hold several numbered MC
                # sub-questions, so MULTI_KEY only fires when there are more
                # keyed letters than there are question stems in the item.
                # Count option groups (each sub-question restarts at "A)") as
                # well as the label, because labels vary - "**Question 4B:**"
                # is not matched by a digits-only pattern.
                n_labels = len(re.findall(r"\*\*Question[^*]{0,14}\*\*", stem, re.I))
                n_groups = sum(1 for l, _ in options if l.upper() == "A")
                n_subs = max(1, n_labels, n_groups)
                if len(letters) > n_subs:
                    flags.append("MULTI_KEY")
                    tier = "failed"

            je_lines, n_tables = ([], 0)
            if qtype in ("journal_entry", "ledger"):
                je_lines, n_tables = parse_je_lines(answer)
                if not je_lines:
                    flags.append("SCHEMA_FAIL")
                    tier = "failed"
                    prof["schema_fail"] += 1
                for l in je_lines:
                    # An acceptable-form notation names two permissible accounts
                    # ("Cash (or Salaries Payable)"). It can never resolve
                    # against a chart, so counting it as UNKNOWN_ACCOUNT
                    # inflated that number with strings no chart entry could
                    # ever satisfy. Classified, not flagged.
                    if NOTATION_RE.search(l["account"]):
                        l["notation"] = True
                        prof["notations"] = prof.get("notations", 0) + 1
                        continue
                    if l["account"].lower() not in aliases:
                        prof["unknown_accounts"] += 1
                        if "UNKNOWN_ACCOUNT" not in flags:
                            flags.append("UNKNOWN_ACCOUNT")  # a flag, never a fail

            # --- leak / degeneracy (free layer) --------------------------------
            sg, ag = ngrams(stem), ngrams(answer)
            overlap = len(sg & ag) / max(1, min(len(sg), len(ag))) if sg and ag else 0.0
            prof["overlap"].append(overlap)

            if qtype == "mcq" and options:
                letters = MC_ANSWER_RE.findall(answer)
                if letters:
                    correct = dict((l, t) for l, t in options).get(letters[0].upper(), "")
                    core = re.sub(r"\W+", " ", correct).strip().lower()
                    # Compare against the FACT PATTERN only. The stem also holds
                    # the option list itself, so testing against the whole stem
                    # matches the correct option against its own text and calls
                    # every well-formed MCQ degenerate.
                    body = "\n".join(l for l in stem.splitlines() if not OPTION_RE.match(l))
                    if len(core) > 25 and core in re.sub(r"\W+", " ", body).lower():
                        flags.append("DEGENERATE_TRIVIAL")
                        tier = "failed"

            if not flags or tier != "failed":
                prof["parsed"] += 1
            prof["stem_len"].append(len(stem))
            prof["sol_len"].append(len(answer))

            los = LO_RE.findall(stem) or LO_RE.findall(answer)
            concepts = CONCEPT_RE.findall(stem)
            asc = ASC_RE.findall(stem) + ASC_RE.findall(answer)

            # The hash must cover the WHOLE key, not just the structured JE
            # lines. A repair to a schedule/T-account table changes the answer a
            # student reads while leaving je_lines untouched - under a
            # lines-only hash that edit is invisible to the ledger, which
            # breaks the "any change produces a new content hash" invariant and
            # would let a silent key edit pass as the same item.
            key_repr = json.dumps(je_lines, sort_keys=True) if je_lines else ""
            chash = sha(stem + json.dumps(options) + key_repr + answer)
            qid = f"{pack_id}#{idx:02d}"

            q = {
                "id": qid,
                "lineage_id": qid,
                "parent_hash": None,
                "pack_id": pack_id,
                "provenance": {
                    "generated_by": "core-demo authoring agent",
                    "session": "2026-08-07 CORE DEMO",
                    "raw_source": raw_path,
                },
                "type": qtype,
                "heading": heading,
                "stem": stem,
                "options": [f"{l}) {t}" for l, t in options],
                "answer_key": je_lines if je_lines else None,
                "solution": answer,
                "citations": [],
                "concepts": [c.strip() for c in (los + concepts)],
                "standard_context": ", ".join(sorted(set(a.upper() for a in asc))),
                "authority": None,
                "difficulty": difficulty_of(qtype, stem, answer),
                "content_hash": chash,
                "remake_count": 0,
                "status": "failed" if tier == "failed" else "unverified",
                "flags": flags,
                "stem_solution_overlap": round(overlap, 4),
                "n_je_tables": n_tables,
                "n_je_lines": len(je_lines),
            }
            questions.append(q)
            for f in flags:
                reasons[f] += 1
            # make_row is the single row constructor: it validates `status`
            # against ledger_io.STATUSES, so a typo becomes an error here
            # instead of a silent new state that every consumer then has to
            # guess at. Verified before adoption that this file's vocabulary
            # ({unverified, failed}) is a subset of STATUSES.
            ledger.append(ledger_io.make_row(
                content_hash=chash, id=qid, status=q["status"], stage=None,
                pack_id=pack_id, lineage_id=qid, remake_count=0, reasons=flags,
                pipeline_version=PIPELINE_VERSION))

    # --- per-pack format profiling / FORMAT_DRIFT ---------------------------
    profiles, drift = {}, []
    ov_means = []
    for pid, p in per_pack.items():
        m = statistics.mean(p["overlap"]) if p["overlap"] else 0.0
        ov_means.append(m)
        profiles[pid] = {
            "items": p["items"],
            "parse_rate": round(p["parsed"] / max(1, p["items"]), 4),
            "mean_stem_len": round(statistics.mean(p["stem_len"]), 1) if p["stem_len"] else 0,
            "mean_solution_len": round(statistics.mean(p["sol_len"]), 1) if p["sol_len"] else 0,
            "mean_stem_solution_overlap": round(m, 4),
            "no_key": p["no_key"], "schema_fail": p["schema_fail"],
            "unknown_account_lines": p["unknown_accounts"],
            "types": dict(p["types"]),
        }

    gmean = statistics.mean(ov_means) if ov_means else 0
    gsd = statistics.pstdev(ov_means) if len(ov_means) > 1 else 0
    all_parse = [p["parse_rate"] for p in profiles.values()]
    pmean = statistics.mean(all_parse) if all_parse else 1
    psd = statistics.pstdev(all_parse) if len(all_parse) > 1 else 0

    # Leak overlap is ONE-SIDED (high only) and needs an ABSOLUTE band as well as
    # a sigma test. A 3-sigma rule on a mean of 0.003 fired on seven packs whose
    # worst absolute overlap was 0.064 - five times below the 0.35 leak floor -
    # and all seven were cleared on review. Low overlap is not a defect, so the
    # two-sided form was wrong in principle too. Parse/field stats stay
    # two-sided: both an unusually low AND an unusually high parse rate are
    # worth a look.
    LEAK_ABS_BAND = 0.15        # below this, a sigma outlier is noise
    for pid, pr in profiles.items():
        why = []
        ov = pr["mean_stem_solution_overlap"]
        if gsd and ov > gmean + 3 * gsd and ov >= LEAK_ABS_BAND:
            why.append(f"stem/solution overlap {ov:.3f} vs corpus {gmean:.3f}+3sd "
                       f"AND above the {LEAK_ABS_BAND} absolute band")
        if psd and abs(pr["parse_rate"] - pmean) > 3 * psd:
            why.append(f"parse rate {pr['parse_rate']:.2f} vs corpus {pmean:.2f}+-3sd")
        if pr["schema_fail"] or pr["no_key"]:
            why.append(f"{pr['schema_fail']} schema_fail / {pr['no_key']} no_key")
        if why:
            pr["FORMAT_DRIFT"] = why
            drift.append(pid)

    # ANSWER_LEAK at the item level, corpus-relative
    item_ov = [q["stem_solution_overlap"] for q in questions]
    imean = statistics.mean(item_ov) if item_ov else 0
    isd = statistics.pstdev(item_ov) if len(item_ov) > 1 else 0
    leak_cut = max(0.35, imean + 4 * isd)
    for q in questions:
        if q["stem_solution_overlap"] >= leak_cut:
            q["flags"].append("ANSWER_LEAK")
            q["status"] = "failed"
            reasons["ANSWER_LEAK"] += 1

    os.makedirs(os.path.join(OUT, "reports"), exist_ok=True)
    with open(os.path.join(OUT, "questions.jsonl"), "w", encoding="utf-8") as fh:
        for q in questions:
            fh.write(json.dumps(q) + "\n")
    # Single write path. Two writers previously opened this file with "w" and
    # each destroyed history; ledger_io is now the only way in.
    from ledger_io import append_rows
    append_rows(ledger)

    with open(os.path.join(OUT, "pack_profiles.json"), "w", encoding="utf-8") as fh:
        json.dump({"corpus": {"mean_overlap": round(gmean, 4), "sd": round(gsd, 4),
                              "leak_cutoff": round(leak_cut, 4)},
                   "packs": profiles, "format_drift": drift}, fh, indent=1)

    classA = sum(1 for q in questions if q["type"] in ("journal_entry", "ledger", "numeric"))
    lines = [
        "# Stage 0 — Normalize (budget mode, pipeline 1.2)", "",
        f"- packs: **{len(packs)}**",
        f"- questions: **{len(questions)}**",
        f"- Class A (machine-verifiable): **{classA}**  ({classA/max(1,len(questions)):.1%})",
        f"- Class B (judgment): **{len(questions)-classA}**",
        f"- journal-entry lines parsed: **{sum(q['n_je_lines'] for q in questions)}**",
        f"- quarantined to `failed`: **{sum(1 for q in questions if q['status']=='failed')}**",
        f"- packs paused FORMAT_DRIFT: **{len(drift)}** {drift if drift else ''}",
        "", "## Reason codes", "",
        "| code | items |", "|---|---:|",
    ]
    for k, v in reasons.most_common():
        lines.append(f"| `{k}` | {v} |")
    lines += ["", "## Type mix", "", "| type | items |", "|---|---:|"]
    for k, v in Counter(q["type"] for q in questions).most_common():
        lines.append(f"| {k} | {v} |")
    lines += ["", f"Leak cutoff (corpus mean {imean:.4f} + 4sd, floor 0.35): "
                  f"**{leak_cut:.4f}**", "",
              "LLM spend so far: **zero**. Stage 0 is pure Python."]
    with open(os.path.join(OUT, "reports", "stage0.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\n".join(lines[:14]))
    print(f"\nwrote {OUT}/questions.jsonl, ledger.jsonl, pack_profiles.json, reports/stage0.md")


if __name__ == "__main__":
    main()
