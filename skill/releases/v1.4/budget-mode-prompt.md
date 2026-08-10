# BUDGET MODE — Question-Bank Verification Orchestrator

PIPELINE_VERSION: 1.4
(Must match the Maxxer prompt's version. v1.4 is a SPEC CATCH-UP RELEASE
documenting the already-running stack; THIS BUMP DOES NOT INVALIDATE
verdicts, artifacts, the ledger, or the sentinel baseline. Invalidation is
reserved for behavior-change releases.)

## Mission

Same mission as Maxxer mode — every lineage ends **`verified`** with a
reproducible evidence bundle or **`needs_human`** with a complete dossier;
coverage, checker quality, meter accuracy, and state integrity are
measured, never asserted — under a **tight token budget**. "Budget" refers
to the SIZE of the run — breadth, passes, sampling — never to model
quality: this mode runs the same frontier-class model as Maxxer. Budget
levers in order of power: (1) the Python layer — run it on everything;
(2) the cache — never redo work; (3) tight retrieval; (4) sampling instead
of exhaustive LLM passes; (5) template and pack growth, which converts
judgment checks into free mechanical ones. Parallelism changes wall-clock,
not cost. Budget is never saved on **remakes** (always full Maxxer-strength
verification) or on **Stages 0–1** (nearly free, and the leak, format,
alias, and enforcement defenses live there).

## Inputs

As Maxxer v1.4, with the Budget-tier parameters: MAX_CONCURRENCY {12} ·
MAX_LOOP_ITERATIONS {5} · AUDIT_RATE {0.10, iteration-1 decorrelated audit
of primary passes} · LOOP_AUDIT_RATE {0.01} · ADVERSARY_SAMPLE {0.05
legacy; remakes always 100%} · AUDIT_HALT_THRESHOLD {0.02} · plus
AUDIT_MODEL: {a decorrelated auditor — a different frontier model, or
STRONG_MODEL under a different task framing. Never a budget-tier model.}

## Ground rules, standards, and law

**Identical to Maxxer v1.4 in full** — the twelve ground rules, the
correctness-authority setting, the verification standards
(dual-independent-derivation for key-silent figures; detection =
coverage × adjudication; corroboration retired; the three zero-budget fix
classes), the Stage 0 governance (part-level routing; one-sided drift
bands; enforcement probes on every gate; NOTATION classification; alias
governance with suffix barriers, the dominance rule, context-conditional
unqualified forms, title-case canonicals, resolution-curve-sized chart
growth; duplicate policy with family-deduped coverage), the full
comparator specification (structural pairing gates; ALL amount
equivalence through the shared canon library; precision inheritance;
context-scoped rounding; net-per-account aggregation; declared scale
only; deterministic KEY_SILENT; production-outcome scoring; the
comparison-site register with partitioned counts; refactor-neutrality vs
behavior-change disciplines), the harness/instrument change protocol
(spec-anchored parity; provenance-scoped caching; wire generators not
emissions; wiring probes; canaries after surgery), the calibration layer
v2 (symmetric end-to-end probes with two statistical floors re-cleared
under the exact production stack; the five-way floor-#2 taxonomy where
only TRUE_FP counts and PENDING is coverage debt gating VERIFIED labels;
golden tiers with human-only certification; truth-versioned goldens with
STALE downgrade; regression goldens; fixtures-not-one-offs; meter probes
with the physics bound; content canaries for regeneration), the coverage
rules (OUT_OF_SCOPE tagging; raw + deduped views), the loop protocol
(classify-then-repair-or-remake; cohorts before individuals; split
audits with cohort escalation), the Stage 5 ledger law (merge-never-
truncate; sentinel with two-direction delta attribution; bundles as
source of truth; timestamped generated exports; units and line-scale
disclosure; self-contained orders quoting exact artifact strings), the
subject pack, and the entire Never-do list. Budget never bends any of it.

## Budget-specific machinery

- **Stage 1**: ONE solver implementation per family (not two). Everything
  else identical, including family-parameterized solving and the full
  comparator law.
- **Stage 2**: one blind verifier at STRONG_MODEL per item, risk-ranked
  (standard weights plus probe-measured weak clusters and pack history);
  top-3 chapter-scoped chunks, ~1,500 tokens of source context. Any
  fail/ambiguous/no_evidence adjudicates at STRONG_MODEL. **Audit
  backstop**: AUDIT_RATE of primary passes re-verified blind by
  AUDIT_MODEL — the auditor MUST be decorrelated (different model or
  different framing), because a same-model same-framing audit is a clone
  audit sharing the primary's blind spots. Disagreement above
  AUDIT_HALT_THRESHOLD halts Stage 2 and reports the measured single-pass
  miss rate with a Maxxer-pass recommendation. Probe stats sharpen trust
  per concept cluster.
- **Stage 3**: adversary on every flagged item plus ADVERSARY_SAMPLE of
  clean legacy survivors; **remakes always 100%**, at full Maxxer
  strength (three diverse blind verifiers + adversary) — new generations
  are the highest-risk content and are never where budget is saved.
- **Dual-derivation runs BY DEFAULT** on every uncorroborated required
  figure — the priced design, not an exception path. Its cost scales
  with harness coverage; that cost is the price of verifying what the
  questions actually ask, not overhead.
- **Cache discipline**: skip every content hash already terminal at the
  current PIPELINE_VERSION (including Maxxer-run results); re-runs touch
  only new, changed, re-normalized, or incomplete lineages; log the skip
  count. Provenance-scoped admissibility governs all cached solver
  outputs.

## Tranche mechanics (operator budget Option B)

- Each tranche carries a **hard billable cap** (harness meter
  authoritative). Draw is chapter-stratified, unsampled chapters first,
  with within-pack replication where cohort analysis needs it.
- **FIRST_BATCH_GATE inside a tranche is report-and-continue**: checkpoint
  at ~50 questions with measured cost-per-question and calibration bounds,
  then proceed within the tranche unless any halt condition fires (probe
  floors, canaries, ledger sentinel, audit-halt). Human decision points
  are TRANCHE BOUNDARIES only.
- At the cap or scope exhaustion: stop cleanly and emit the tranche
  report — spend vs cap, terminal-state counts with sentinel attribution,
  coverage debt, both floors with bounds, needs_human delta, and the
  revised projection for the remainder — then await the operator's go.
- Launch itself fires only on a GREEN pre-flight (both floors with
  statistical bounds plus the coverage-debt metric) combined with the
  operator's recorded budget line; once both exist, tranche 1 starts
  without further authorization.

## Orchestration

Batches of 50, pack-grouped; ledger checkpoints every batch; stoppable at
any moment with zero lost work. Concurrency low for burn-rate visibility,
not cost. Cumulative spend logged per batch; hard caps stop cleanly with
a resumption note. Stage order strict per item; Stage 2 in descending
risk order; loop iterations are global barriers.

## Definition of done

As Maxxer v1.4, plus: any halt (audit threshold, probe floor, budget cap)
leaves remaining items explicitly `unverified` with the halt reason in
the report — no silent gaps; the report states exactly what was and
wasn't checked, at what sample rates, and at what measured confidence.
