#!/usr/bin/env python3
"""
Split every CORE DEMO pack into (a) a stem-only version a solver can be handed
without ever seeing the answer, and (b) the answer key held back for comparison.

The whole blind re-solve is worthless if a single answer leaks into a stem, so
this errs hard toward over-stripping and then asserts the result is clean.

Usage:
    python3 blind_strip.py            # write blind/stems + blind/keys
    python3 blind_strip.py --check    # re-verify existing output only
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT = os.path.join(HERE, "blind")
STEMS = os.path.join(OUT, "stems")
KEYS = os.path.join(OUT, "keys")

# A line that begins an answer region. Authors wrote several variants of this
# marker - "**Answer key:**", "**Answer key (Part A):**", "**Answer key B:**" -
# so match the keyword and allow any qualifier before the closing stars.
ANSWER_START = re.compile(
    r"^\s*\*\*(Answer key|Answer|Key insight|Solution|Check)\b[^*]*\*\*", re.I
)
# An answer region ends where the next question part begins. Items in several
# packs interleave Required/Answer/Required/Answer, so an answer must NOT be cut
# all the way to the end of the item or the later question parts vanish with it.
#
# This must be STRICT. Answer keys contain prose headings that begin with the
# same words - "**Required each reporting period (ASC 360-10-50-1):**" is a
# disclosure heading inside an answer, and "**Required allowance** credit =
# **$1,080**" is a literal answer value. Treating either as a question boundary
# ends the strip early and leaks the answer into the stem. A real part marker is
# the keyword plus at most a short qualifier, always closed with a colon.
#
# Sub-question labels vary more than they look. All of these start a new
# question and must CLOSE the preceding answer region, or that sub-question's
# stem and options get swallowed into the answer and vanish from the stem:
#     **Required:**   **Required (Part B):**   **Required C:**
#     **Question 2:**  **Question 4B:**  **Question 4.2:**
#     **Q4B.**   **Q5.2**
# The "Required/Question" branch still demands a colon, because answer prose
# writes headings like "**Required each reporting period (ASC 360-10-50-1):**"
# and values like "**Required allowance** credit = **$1,080**", neither of
# which may be treated as a boundary.
ANSWER_END = re.compile(
    r"^\s*\*\*(?:"
    # "Required" stays STRICT - answer prose imitates it, so it must carry a
    # short qualifier and a colon to count as a boundary.
    r"Required(?:\s*\((?:Part\s+)?[A-Za-z0-9 ]{1,12}\))?\s*[A-Za-z0-9.]{0,5}\s*:\s*\*\*"
    # Question labels are permissive - observed: "Question 2:", "Question 4B:",
    # "Question 4.2", "Question 4-2:", "Question 2 of 2:", "Q4B.", "Q5.2".
    # Nothing in an answer body opens with these, so breadth is safe here.
    r"|Question\b[-\w. ]{0,14}\s*[.:]?\s*\*\*"
    r"|Q\s*\d[-\w.]{0,6}\s*[.:]?\s*\*\*"
    r"|(?:Scenario|LO|Concept)\s*:\s*\*\*"
    r")",
    re.I,
)
# Where a later question part supplies its own facts, they sit at the tail of the
# preceding answer region, introduced by a rule or a bold Part header. That tail
# is question content and has to be handed back to the stem.
SETUP_HEAD = re.compile(r"^\s*(-{3,}\s*$|\*\*(Part|Situation|Case)\b)", re.I)
# Item boundary.
ITEM_START = re.compile(r"^###\s+(.*)$")
# Sections that are bookkeeping, not question content.
DROP_SECTION = re.compile(r"^###\s*Self-?check", re.I)
# The trailing machine-readable block each author emitted.
JSON_FENCE = re.compile(r"^\s*(```|JSON:\s*$|\{\s*$)")

# Belt-and-braces: any of these surviving in a stem means the strip failed.
# Anchored to line start on purpose - a question part may legitimately say
# "e. **Key insight:** State in one sentence why ..." as the thing being asked.
LEAK_PATTERNS = [
    re.compile(r"^\s*\*\*(Answer key|Answer|Key insight|Solution|Check)\b", re.I | re.M),
]


def split_items(lines):
    """Yield (heading_or_None, [lines]) for the preamble then each ### section."""
    chunks, cur, head = [], [], None
    for ln in lines:
        if ITEM_START.match(ln):
            chunks.append((head, cur))
            head, cur = ln, [ln]
        else:
            cur.append(ln)
    chunks.append((head, cur))
    return chunks


def strip_pack(text):
    """Return (stem_markdown, [{'heading','answer'} ...])."""
    lines = text.splitlines()

    # Drop the trailing JSON block the authors appended.
    cut = len(lines)
    for i in range(len(lines) - 1, max(0, len(lines) - 60), -1):
        if JSON_FENCE.match(lines[i]):
            cut = i
    lines = lines[:cut]

    stem_out, held = [], []

    for head, chunk in split_items(lines):
        if head is not None and DROP_SECTION.match(head):
            continue  # author self-check checklist: not question content

        kept, answer, in_answer, pending = [], [], False, []
        for ln in chunk:
            if in_answer:
                if ANSWER_END.match(ln):
                    # Hand back any trailing setup block this next part needs.
                    heads = [j for j, x in enumerate(pending) if SETUP_HEAD.match(x)]
                    if heads:
                        answer.extend(pending[: heads[-1]])
                        kept.extend(pending[heads[-1]:])
                    else:
                        answer.extend(pending)
                    pending, in_answer = [], False
                else:
                    pending.append(ln)
                    continue
            elif ANSWER_START.match(ln):
                in_answer = True
            (answer if in_answer else kept).append(ln)
        answer.extend(pending)

        stem_out.extend(kept)
        if head is not None:
            held.append({"heading": head.strip(), "answer": "\n".join(answer).strip()})

    stem = "\n".join(stem_out).rstrip() + "\n"
    # Collapse the run of blank lines / stray rules left where answers were cut.
    stem = re.sub(r"\n{3,}", "\n\n", stem)
    stem = re.sub(r"\n(-{3,}\n)+(?=-{3,}\n)", "\n", stem)
    return stem, held


def audit(stem, path):
    """Raise if anything answer-shaped survived."""
    problems = []
    for pat in LEAK_PATTERNS:
        for m in pat.finditer(stem):
            line = stem[: m.start()].count("\n") + 1
            problems.append(f"{path}:{line}: leaked {pat.pattern!r}")
    # A stem with no question left means the split ate too much.
    if "**Required:**" not in stem and "**Question:**" not in stem:
        problems.append(f"{path}: no Required/Question survived - over-stripped")
    return problems


def main():
    check_only = "--check" in sys.argv
    if not check_only:
        os.makedirs(STEMS, exist_ok=True)
        os.makedirs(KEYS, exist_ok=True)

    packs = sorted(f for f in os.listdir(RESULTS) if re.fullmatch(r"agent_\d+\.md", f))
    problems, n_items, index = [], 0, []

    for fn in packs:
        src = os.path.join(RESULTS, fn)
        with open(src, encoding="utf-8") as fh:
            text = fh.read()

        stem, held = strip_pack(text)
        problems.extend(audit(stem, fn))
        n_items += len(held)

        # An item that yielded no held-back answer means the parser never found
        # this item's answer - so it is either still sitting in the stem or the
        # item genuinely has no key. Either way a human needs to look.
        for item in held:
            if not item["answer"].strip():
                problems.append(f"{fn}: no answer captured for {item['heading'][:70]!r}")

        stem_path = os.path.join(STEMS, fn)
        key_path = os.path.join(KEYS, fn.replace(".md", ".json"))
        if not check_only:
            with open(stem_path, "w", encoding="utf-8") as fh:
                fh.write(stem)
            with open(key_path, "w", encoding="utf-8") as fh:
                json.dump({"pack": fn, "items": held}, fh, indent=1)

        index.append({
            "pack": fn,
            "stem": stem_path,
            "key": key_path,
            "n_items": len(held),
            "stem_chars": len(stem),
            "src_chars": len(text),
        })

    if not check_only:
        with open(os.path.join(OUT, "INDEX.json"), "w", encoding="utf-8") as fh:
            json.dump({"packs": index, "n_packs": len(index), "n_items": n_items}, fh, indent=1)

    print(f"packs      : {len(packs)}")
    print(f"items held : {n_items}")
    shrink = 1 - sum(i["stem_chars"] for i in index) / max(1, sum(i["src_chars"] for i in index))
    print(f"stripped   : {shrink:.1%} of pack text removed")
    if problems:
        print(f"\nLEAKS/ERRORS ({len(problems)}):")
        for p in problems[:40]:
            print("  " + p)
        sys.exit(1)
    print("audit      : clean - no answer text survived in any stem")


if __name__ == "__main__":
    main()
