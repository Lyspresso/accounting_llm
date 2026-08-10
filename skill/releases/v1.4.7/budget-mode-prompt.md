# BUDGET MODE — Question-Bank Verification Orchestrator

PIPELINE_VERSION: 1.4.4
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

## 1.4.1 ADDENDUM

The Maxxer 1.4.1 addendum applies **in full**: state-store law (single
write API, full-vector sentinel with precondition-synthesizing fault
injection, the declared unit ladder), write-time provenance and
comparison-symmetry, the role-invariant builder with instruction-region
identity across every solver path, generated pack governance (one
banned-patterns generator, chart-invariants fixture, full-store sweeps,
seeds yielding to measured dominance), and the reporting rules (fixtures
age with semantics; stacked defects re-diagnose; informational numbers
re-derive before projections; findings re-attribute when their
comparisons are contaminated). Budget bends none of it.

## 1.4.2 ADDENDUM

The Maxxer 1.4.2 addendum applies in full: the case-history artifacts
(DECISIONS, RETIRED, casebook) bind Budget mode identically.

## 1.4.4 ADDENDUM

The Maxxer 1.4.4 addendum (communication law: 01-COMMUNICATION.md and
the comms/ mailbox) applies in full.

### Terminal write gate (v1.4.5, behavior change)

`verified` and `needs_human` are PIPELINE terminals: they assert Stage-3
adversary has run for flagged items AND that the label sits under a CERTIFIED
floor. Neither holds while the LAUNCH gate is RED, so the single ledger write
path REFUSES terminal rows under RED. The only exception is an explicit,
committed override file in `comms/operator/OVERRIDE-terminal*.md` — an exception
must be an artifact with an author and a diff, never a flag passed once.

An unreadable or missing gate file counts as RED. A gate that cannot be read is
not a green light.

### The gate's number is CHARGEABLE, not finding-bearing

Floor #2 consumes the taxonomy's CHARGEABLE metric (TRUE_FP | PENDING). A
MATCHER_ARTIFACT is an instrument defect and a GOLDEN_WRONG means the finding
was a TRUE positive; charging either to the false-positive floor measures
something the law does not define. Report the raw count too — a forecast that
hides its gross number is not auditable.

### Loosenings are serialized and each one owes a detection re-measure

Every comparator loosening is implemented ALONE and floor #1 is re-measured
immediately after it. A comparator that accepts more also detects less, and a
batch of four loosenings shipped together cannot tell you which one cost what.

### Monotonicity is asserted on status TOTALS, not status|scope cells

Merge-only semantics make rows immortal, so a status TOTAL can only rise. Scope
(`current` / `superseded`) is a DERIVED view: an authorised key repair moves a
lineage's rows from current to superseded and drops a status|scope cell without
destroying anything. Halting on the finer cell makes every lawful repair look
like data loss, which trains everyone to reach for `--invalidate` — and that is
how a real loss gets waved through.

### Current state is a resolution, not a lookup

For each lineage: the highest STAGE reached wins (stage-0 re-normalisation never
overrides a verdict), and among rows at that stage the LAST one wins (so a
verdict can be revised and the revision is visible). "Latest row wins" hides
verdicts behind re-normalisation rows; "terminal outranks everything" makes a
terminal state unrevertable.

### Evidence registry (v1.4.6)

A directory not listed in `provenance.EVIDENCE_PREFERENCE` is INVISIBLE to every
tool. Fourteen goldens were once minted into an unlisted directory and all
fourteen resolved "no admissible evidence" — silently, with no error, just a
smaller number that looked plausible. Every `out/evidence_*` directory is either
registered or explicitly excluded with a reason, and a standing probe asserts it.

### Measurement paths must be machine-independent

Batch manifests record absolute paths. Any consumer of one re-roots through
`provenance.local()`. A floor that reads raw manifest paths measures nothing on
any machine but the one that wrote them — and it fails to ZERO PROBES, which is
a broken measurement, not a failing one. The two must never look alike, so the
suite asserts probes-run > 0.

### The launch condition is a conjunction

Terminal writes require the gate GREEN **and** floor #2 certified at human tier
(D6, DECISION-002 letter A). GREEN alone is a measurement; certification is the
permission. Keying the guard on RED alone meant the gate turning GREEN silently
unlocked terminal labelling while zero human-tier goldens existed.

### Single-homing admits no fallback

A constant imported "with a fallback that must track the source" is a second
source. Fixtures carry their dependencies into the sandbox instead.

### Aggregation across alias-equivalent families (v1.4.7)

One pooled solver line may match a SET of key lines when, on the same side: the
sums agree exactly, every absorbed account shares a COMMON family token with the
pooled one (and with each other), the absorbed accounts are DISTINCT, and none of
them is the pooled account itself.

Each clause is a defect that occurred, not a precaution:

- **common token, not pairwise** — pairwise linkage absorbed "Loss from Storm"
  into an inventory balance because both mentioned "storm". A scenario word is
  not an account identity.
- **distinct accounts, never the pooled one** — same-account absorption
  collapsed several distinct Cash movements into one line. Summing one account's
  postings is per-entry netting, which `net_per_account` already does.
- **family resolution is PREFIX-aware** — exact-after-normalisation lookup is
  why an alias ruling could not clear anything: a pooled account carries extra
  qualifiers and never keys into the map. An alias key that is a prefix of the
  account identifies its family.

### Predict at the mechanism level or not at all

A symptom-level prediction ("the offender clears") cannot be scored, and it hides
the mechanisms that decide the outcome. Name the mechanism; if you cannot, say
you do not know.
