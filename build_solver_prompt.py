#!/usr/bin/env python3
"""
The solver prompt BUILDER — single source for every harness's instruction region.

Trim prompts were previously emitted by ad-hoc inline heredocs, one per run.
That is why the LO 11-8 treatment note reached the dual harness and never
reached trim: there was no shared place to put it, so it was added wherever the
last script happened to be written. Every harness now assembles its instruction
region here, and treatment notes are injected from treatment_notes.yaml by
learning objective, so a note lands automatically for the families it governs.

    INSTRUCTION REGION = rules the solver must follow
    QUESTION REGION    = the stem, verbatim

A wiring probe asserts notes appear in the INSTRUCTION region only. A stem that
happens to mention "contribution revenue" must never satisfy the check.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = os.path.join(HERE, "out", "pack_proposals", "treatment_notes.yaml")

INSTRUCTION_OPEN = "--- INSTRUCTIONS (rules you must follow) ---"
INSTRUCTION_CLOSE = "--- END INSTRUCTIONS ---"
QUESTION_OPEN = "--- QUESTION (the whole question is here; do NOT look for it on disk) ---"
QUESTION_CLOSE = "--- END QUESTION ---"


def load_notes():
    """
    Minimal reader for the treatment library. Returns [{id, lo, rule_lines}].
    Deliberately not a full YAML parse - the file is authored by hand and a
    dependency here would be one more thing that can silently drop a note.
    """
    if not os.path.exists(NOTES):
        return []
    out, cur = [], None
    for raw in open(NOTES, encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.startswith("- id:"):
            if cur:
                out.append(cur)
            cur = {"id": line.split(":", 1)[1].strip(), "lo": "", "rule": []}
        elif cur is not None and line.strip().startswith("lo:"):
            cur["lo"] = line.split(":", 1)[1].strip()
        elif cur is not None and line.strip().startswith("rule:"):
            cur["_in_rule"] = True
        elif cur is not None and cur.get("_in_rule"):
            if re.match(r"^\s{2}\w", line) and not line.startswith("    "):
                cur["_in_rule"] = False
            elif line.strip():
                cur["rule"].append(line.strip())
    if cur:
        out.append(cur)
    for n in out:
        n.pop("_in_rule", None)
        n["rule"] = " ".join(n["rule"])
    return out


def notes_for(lo_or_stem):
    """Notes whose LO appears in the item's LO string or stem."""
    hits = []
    for n in load_notes():
        lo = n.get("lo", "").replace("LO", "").strip()
        if lo and re.search(rf"\bLO\s*{re.escape(lo)}\b", lo_or_stem or "", re.I):
            hits.append(n)
    return hits


BASE_RULES = [
    "- decimal.Decimal for money, never floats. ROUND_HALF_UP per period; state it",
    "  in the solver docstring. Derive every figure; hard-code nothing. Dr = Cr.",
    "- BLIND: do not open out/questions.jsonl, core-demo/results/, blind/keys/,",
    "  CORE_DEMO_*, ACCOUNT343_*, verify*/, proof/, ARITH_*. They hold the answer.",
    "  Report peeked:true if you slip.",
    "- EFFICIENCY IS SCORED: write the solver and run it in ONE bash heredoc.",
    "- COVERAGE IS SCORED: report EVERY figure the Required parts ask for, including",
    "  each running balance, schedule row or layer total a part says to show or",
    "  present. Do not report figures no part asked for.",
    "- Schedules: this edition rounds to whole dollars in journal entries while",
    "  running PVs at full precision. Either convention is fine; close the schedule",
    "  exactly to face or zero and say which you used.",
]


ROLE_FRAMING = {
    "primary": "Solve this accounting question COLD.",
    "dual": ("Derive the answers to this accounting question COLD. You are the "
             "SECOND independent derivation; another solver has already worked "
             "it and you cannot see its output. Work bottom-up from the fact "
             "pattern rather than reaching for the shape of an answer."),
    "remake": ("Solve this accounting question COLD. It is a regenerated item "
               "and gets the full gauntlet."),
}


def build(item_id, stem, evidence_dir, role="primary"):
    """
    Full prompt for ANY solver path. Role varies the framing line only.

    The rule set is identical across roles by construction. It was not before:
    the dual harness carried the LO 11-8 treatment note and trim did not,
    because the two scripts were generated separately with hand-written rule
    blocks. Context asymmetry between solvers manufactures construal splits
    that read as disagreements - and it made one solver look worse than the
    other on an item where it had simply not been told the rule.
    """
    applicable = notes_for(stem)
    lines = [
        f"{ROLE_FRAMING.get(role, ROLE_FRAMING['primary'])} Write the result to "
        f"{evidence_dir}/solver_output.json",
        f'Item id: "{item_id}"   Evidence dir: {evidence_dir}',
        "",
        INSTRUCTION_OPEN,
        *BASE_RULES,
    ]
    if applicable:
        lines += ["",
                  "- PACK TREATMENT NOTES (these OVERRIDE your default judgement; this",
                  "  edition's demonstrated treatment differs from another that is",
                  "  defensible in practice):"]
        for n in applicable:
            lines.append(f"  * [{n['lo']}] {n['rule']}")
    lines += [
        INSTRUCTION_CLOSE,
        "",
        QUESTION_OPEN,
        stem,
        QUESTION_CLOSE,
        "",
        "OUTPUT: solver.py prints exactly one JSON object:",
        f'{{"id":"{item_id}","rounding_convention":"...",',
        ' "answers":[{"label":"a: ...","value":6000}],',
        ' "journal_entries":[{"part":"b","lines":[{"account":"...","debit":0,"credit":0}]}],',
        ' "insufficient_info":false,"notes":""}',
    ]
    return "\n".join(lines)


def instruction_region(prompt):
    """The rules region only. Presence checks must never see the stem."""
    if INSTRUCTION_OPEN not in prompt or INSTRUCTION_CLOSE not in prompt:
        return ""
    return prompt.split(INSTRUCTION_OPEN, 1)[1].split(INSTRUCTION_CLOSE, 1)[0]


def question_region(prompt):
    if QUESTION_OPEN not in prompt:
        return ""
    return prompt.split(QUESTION_OPEN, 1)[1].split(QUESTION_CLOSE, 1)[0]


if __name__ == "__main__":
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(HERE, "out", "questions.jsonl"), encoding="utf-8"))}
    q = qs["agent_204#02"]
    p = build("agent_204#02", q["stem"], "/tmp/x")
    ir = instruction_region(p)
    print("=== WIRING PROOF: freshly generated LO 11-8 solver context ===\n")
    print("INSTRUCTION REGION (rules only):")
    for line in ir.strip().splitlines():
        if "11-8" in line or "Contribution Revenue" in line or "NET" in line:
            print("  >>> " + line.strip()[:150])
    print(f"\nnotes detected for this item : {[n['id'] for n in notes_for(q['stem'])]}")
    print(f"rule string in INSTRUCTION    : {'contribution revenue' in ir.lower()}")
    print(f"rule string in QUESTION only  : "
          f"{'contribution revenue' in question_region(p).lower()}")
