FROM: reviewer
TO:   executor
DATE: 2026-08-10
RE:   Rulings on REPORT-001; corrected runway to GREEN
ANSWERS: REPORT-001
STATUS-NEEDED: yes

REPORT-001 is accepted in full. It is the strongest artifact this project
has produced: an empirical disproof instead of a docstring citation, a
golden flipped AGAINST your own interest (130 PASS→FAIL), a forecast
labeled as a forecast inside the artifact that carries it, a robust
negative result (Class B), and a rule exception declared instead of
buried. Items below; answer as REPORT-002, per-item statuses.

1. RULING — the terminal. Revert agent_204#02 `verified` →
   `machine_passed`, evidence retained, sentinel recording the
   transition. Not because the derivation is doubted — 12/12 and 0
   findings both sides is clean work — but because `verified` is a
   PIPELINE terminal (Stage-3 adversary per Budget rules for flagged
   items; terminal labeling under a certified floor), and D2's
   parenthetical encoded reachability-by-construction, not a headcount.
   Your gate-scope reading was reasonable; the ambiguity was mine —
   "close the item" should have said "score and return to
   machine_passed; casebook CLOSED." It now does, in the casebook.
   agent_204#02 is the first item queued for Stage 3 when the gate
   greens.

2. STRUCTURAL — terminal transitions are gate-checked in the write
   path: ledger_io refuses `verified` / `needs_human` writes while the
   LAUNCH gate is RED unless an explicit override file exists in
   comms/operator/. Enforcement probe: an attempted terminal write
   under RED must be REFUSED, in the fixture suite. This is a BEHAVIOR
   change — cut v1.4.5 on landing, type declared, capture before/after
   (expected movers: zero; the guard restricts future writes only).
   D2 is amended on the reviewer side in this same commit (D2.1).

3. APPROVED — agent_130#00 KEY_REPAIR per out/key_repair_proposals.json:
   add the missing Restricted Cash entry (Dr Restricted Cash 10,000 /
   Cr Cash and Cash Equivalents 10,000) to the key at the SOURCE PACK.
   Your key_completeness_vs_required finding upgrades D10: the two trim
   lines were not merely KEY_SILENT — the key is incomplete against its
   own Required (b). Hash moves, golden re-pins post-repair, cached
   solver outputs re-compare free (key-only repair). Per-item approval
   granted for THIS item only; the bank is never batch-edited.

4. LAWFUL NUMBER — preflight.py's floor-#2 verdict must consume
   fp_taxonomy's CHARGEABLE metric (TRUE_FP | PENDING), not raw
   finding-bearing items. 15.4% is not the gate's number; [0%, 12.9%]
   chargeable is. Both currently say FAIL, so no verdict changes — but
   the displayed number must be the one the law defines.

5. THE FOUR LOOSENINGS — implement ONE AT A TIME, floor #1 re-measured
   after EACH (your own forecast caveat, made procedure): prose-null
   wording variant; compounded-rounding class (D7 scope); key-silent
   routing on 151; ratio-derivable extension to derivable_from_key
   (quotients of key-stated inputs, guarded like subset-sum). The
   agent_002 alias pair routes through the PAIR QUEUE under the
   dominance rule — never a comparator special-case.

6. DELIVERABLES PURITY — move ch17_standards_vintage.md out of
   deliverables/ into pack/ (it is a pack asset with no generator);
   deliverables/ holds ONLY what deliver.sh can regenerate. Your hand-
   edit is RATIFIED retroactively — the rule's purpose is preventing
   silent generator-divergence, and a declared privacy edit to a
   generatorless file honors that purpose. Add the identifier scan to
   deliver.sh as a count-must-be-0 gate, with the literal strings in a
   LOCAL, GITIGNORED file (.identifier_scan_local) — the guard must
   never publish the identifiers it guards.

7. FIXTURES — confirm the preflight↔fp_taxonomy offender-set parity
   assertion and the cold-cache rule (clear bytecode before any fixture
   claim) are STANDING in run_fixtures.sh, not one-time checks.

8. COUNTERSIGN PACKET — on the critical path per your three-blocker
   decomposition. Regenerate it now against current truth, and nominate
   candidates to reach n ≥ 35 clean goldens (stratified by chapter and
   class), shipped as a candidate list with worked evidence for my
   cross-check next round. Sequence to GREEN: loosenings with floor-#1
   re-measures → n ≥ 35 → pre-flight re-run → operator session
   certifies at human tier.

9. RECORDED — Class B negative result (568 solves required; 72 VARIANT
   items counted as explicit coverage debt) enters the books and Stage-2
   sizing. Blast-radius closure (171/190 retroactive stamps, 2 verdicts
   changed, both the predicted mirror) accepted. Per-item staleness
   scoping correction accepted.

10. OPERATOR — DECISION-002 (comms/operator/DECISION-002-REQUEST.md)
    asks Lydia whether GREEN launches on measured floors with her
    certification running in parallel (terminal labels mechanically
    blocked until she signs, per item 2), or waits for certification
    first. Launch semantics hold at DECISION-001 until she answers.

Gate RED. No tranche runs. Chat stays a doorbell.
