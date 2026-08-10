# REVIEW-STATE — live continuity document
Updated: 2026-08-10 · Supersedes docs/archive/HANDOFF-2026-08-08.md
This is the reviewer's pick-up-here file. Read it with deliverables/STATUS.md
(the executor's generated state) and docs/07-RULEBOOK.md (the law). Case history: docs/02-02-DECISIONS.md, docs/03-03-RETIRED.md, docs/04-04-items-casebook.md, docs/06-06-PREDICTIONS.md, docs/05-05-OPEN-QUESTIONS.md.

## Gates and authorization

- LAUNCH GATE: **GREEN** — floor #1 40/40 [91.2,100]; floor #2 0
  chargeable /40, CI [0, 8.8%] vs 10% ceiling; re-measured independently
  on the reviewer's machine. LAUNCH = GREEN **AND** certified (letter A);
  certification is the sole remaining condition. Ledger sha b210c246
  (stage-null mover, declared + proved inert).
- FAMILY GATE (LO 11-8): LIFTED — wiring probe green, 13/13 contexts,
  rule not stem-satisfiable, instruction regions identical across roles.
- BUDGET (operator-recorded, standing): **Option B** — tranche 1 hard cap
  10,000,000 billable tokens (harness meter authoritative), ≈182 questions
  at the measured 39,652/q trim rate with dual-by-default @38%.
  **Launch trigger is a CONJUNCTION (operator letter A): pre-flight GREEN
  AND countersign session complete. GREEN alone does not launch.** FIRST_BATCH_GATE inside the tranche is
  report-and-continue; human decisions at tranche boundaries only.

## The in-flight order block

ORDER-006 (comms/orders/) — fifth loosening (D24) serialized; D15.2 recorded.
Worksheet READY at deliverables/countersign_worksheet.md; fixtures 10/10;
ledger 3,184 rows / 1,828 lineages / 0 terminal; v1.4.6 cut.
Superseded history below retained for context:

1. Write-time provenance: stamps captured at generation, immutable;
   stamp()'s retroactive mode removed; historical outputs re-stamped by
   RECONSTRUCTION (labeled); admissibility audit re-run corpus-wide —
   expected: parity50 trim cache for LO 11-8 goes PACK_NOTES_STALE.
2. Provenance fixture (seventh in run_fixtures.sh): a synthetic
   old-pack-version output must be flagged inadmissible.
3. agent_204#02: fresh symmetric TRIM derivation (pack-notes change ⇒
   re-solve), score its 13 figures fresh-vs-fresh, close the item.
4. Blast radius: enumerate retroactively-stamped outputs; report how many
   admissibility verdicts change under reconstructed stamps.
5. Cost re-derivation ACCEPTED (trim 39,652/q vs baseline 50,091);
   0.799 ratio and +44% retired — discarded, not refreshed.
6. Then: five-way fp taxonomy → Class B family/duplicate clustering →
   PRE-FLIGHT LAST, countersign packet regenerated first.

## Remaining runway to production

agent_204 closure → five-way taxonomy (TRUE_FP only counts against the
ceiling; PENDING = coverage debt gating VERIFIED labels; MATCHER_ARTIFACT;
HASH_MIXING; GOLDEN_WRONG) → Class B clustering (596 MCQs, never yet
analyzed) → pre-flight under the exact production stack → tranche 1
auto-fires on GREEN → tranches to the caps → Stage 2/3 on Class B →
operator countersign session (~90 min, certifies floor #2, blocks nothing).

## Prediction ledger (metric + threshold register together; scored)

- P1 convergence under dual-derivation: HELD (gap 13 → 2 items).
- P2 130/283 free re-compare both-pass: **FAILED 0/2** — informative;
  exposed the un-unified JE comparison path.
- P3 JE-unification movers = operating-lease year-end only: HELD
  (exactly one mover, in-class, probes 40/40 unmoved).
- Genuinely-lost after ledger truncations = 0: HELD (100/100 recoverable).

## Current numbers (see deliverables/STATUS.md for the generated version)

Corpus 1,828 lineages = 1,819 active + 9 DUPLICATE_OF. Funnel: 1,719
unverified / 86 machine_passed / 14 failed / 9 retired. Terminal count 0
BY DESIGN (gate RED; verified is unreachable until the taxonomy exists and
the gate is green). Unresolved account lines 3,690 across 842 items.
Goldens 28 (20 ai_cross_checked / 8 adjudicated / 0 human — certification
requires the human tier). Six fixtures green (matcher, canon, wiring,
chart invariants, write-path, sentinel fault-injection); provenance
fixture pending as the seventh.

## Open items owned by the operator (Lydia)

- Countersign session against the REGENERATED packet (after pre-flight
  prep) — certifies the false-positive ceiling at human tier.
- Go/no-go at each tranche boundary.
- Nothing else blocks on her.

## Protocol (how the three roles work)

Executor reports with artifacts (deliver.sh regenerates and stamps
exports; verbal-only state does not exist). Reviewer verifies arithmetic
independently, issues SELF-CONTAINED order blocks quoting exact artifact
strings, keeps the rulebook (docs/07-RULEBOOK.md) current, and scores every registered
prediction. Operator protocol: if a document the reviewer needs has not
arrived, the reviewer replies with exactly one sentence — "I cannot
continue until you give me the documents" — and nothing else. Numbers
that move name their movers; decompositions partition exactly or carry an
explicit remainder; corrected instruments derive their old readings.
