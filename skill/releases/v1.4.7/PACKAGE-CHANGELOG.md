# Question-Bank Verification — v1.2 Package

A two-mode, loop-based pipeline that verifies an AI-generated question bank
against its textbook and syllabus. Every question ends `verified` with a
reproducible evidence bundle or `needs_human` with a complete dossier.
Coverage and checker quality are measured, never asserted. Built for
accounting first; the SUBJECT PACK section swaps to port it to any class.




## v1.4.7 — BEHAVIOR CHANGE (2026-08-10)

Type: **behavior change** (comparator). Loosening 5 of 5, implemented ALONE
under the serialization protocol.

- **Aggregation across alias-equivalent families**: one pooled solver line may
  match a SET of key lines — same side, exact sum, common family token, distinct
  sibling accounts, never the pooled account itself.
- **Family resolution is prefix-aware**, so an account carrying extra qualifiers
  still keys into its alias family.
- Guard fixture `test_aggregation.py` ships with it (8 cases, 6 of them refusals).

**MOVERS — enumerated:**

| item | before | after | why |
|---|---|---|---|
| `agent_002#03` | 6 hard | **0** | pooled 150,000 ↔ 90,000 + 60,000 per security, both sides |
| everything else (115 items) | — | **unchanged** | verified against a 116-item baseline signature |

**STOP-AND-REPORT, recorded because it happened.** The FIRST implementation
produced two additional movers — `agent_223#00` (19→7) and `agent_322#00` (4→3).
Both were over-matches caused by the implementation exceeding the approved
scope, not by the approved rule: pairwise instead of common-token linkage, and
no same-account exclusion. Tightened to the scope as ordered; both regressions
are now permanent fixture cases.

**Floors after:** #1 detection 40/40, CI [91.2%, 100%] — **held, unchanged by
the loosening**. #2 chargeable 0/40, CI [0%, 8.8%] — **finding-bearing items now
ZERO** (was 1). Gate **GREEN**; launch still blocked pending certification.

## v1.4.6 — BEHAVIOR CHANGE (2026-08-10)

Type: **behavior change**. Owed from REPORT-003, which shipped these without a
release; cut on ORDER-004 item 5. The standard survives by being enforced on the
good nights.

- **parity_dirs / measurement path.** `detection_floor()` re-roots evidence
  paths through `provenance.local()`. Suite asserts probes-run > 0.
- **make_row** adopted in stage 0; stage-0 rows now carry an explicit
  `"stage": null`.
- **sentinel hard-import** of `PIPELINE_VERSION`/`TERMINAL`; fixture carries
  `ledger_io.py`, `paths.py`, `io_json.py` into its sandbox.
- **EVIDENCE_PREFERENCE** registers `evidence_numeric`, `evidence_restem`;
  completeness probe added (`test_registry.py`).
- **Terminal gate is now a conjunction**: GREEN **and** certified.
- **D15.1 aliases applied**: `Accounts Receivable, Net` → `Accounts Receivable`;
  `Common Stock, No Par` → `Common Stock`; `Retained Earnings—Dividends` →
  `Retained Earnings`.

**MOVERS — enumerated, each measured not assumed:**

| change | mover | before → after |
|---|---|---|
| parity_dirs | floor #1 **off the origin machine** | 0/40 (unmeasurable) → 40/40. **On the origin machine: no change** (40/40 both ways) |
| make_row `stage: null` | ledger sha, once | `f034c594…` → new. Inert: `questions.jsonl` byte-identical, 3,167 rows held, decomposition unchanged |
| sentinel hard-import | none | constants were already identical; the fallback was a latent second source |
| EVIDENCE_PREFERENCE | clean goldens | 26 → 41 (14 numeric + restem became resolvable) |
| terminal conjunction | **zero rows** | restricts future writes only; verified a terminal write is REFUSED under today's GREEN gate |
| D15.1 aliases | **UNKNOWN_ACCOUNT: ZERO delta** | 843 items / 3,690 lines, unchanged — the three forms occur **0 times in corpus keys** (they are solver-side names), so aliasing them cannot move a count over key accounts |

**Gate at this release:** floor #1 40/40 CI [91.2%, 100%] PASS; floor #2
chargeable 0/40 CI [0%, 8.8%] PASS; **FIRST_BATCH_GATE GREEN**; launch BLOCKED
pending certification (zero human-tier goldens).

## v1.4.5 — BEHAVIOR CHANGE (2026-08-10)

Type: **behavior change**. Invalidation capture below.

- Terminal write gate: `ledger_io` REFUSES `verified`/`needs_human` while the
  LAUNCH gate is RED, unless `comms/operator/OVERRIDE-terminal*.md` exists.
  Unreadable/missing gate = RED. Enforcement probe standing in the fixture suite
  (5 cases incl. override and GREEN paths).
- Floor #2 consumes the CHARGEABLE metric (TRUE_FP | PENDING); raw
  finding-bearing count still reported alongside.
- Four comparator loosenings, applied ONE AT A TIME, floor #1 re-measured after
  each: prose-null wording, compounded-rounding (schedule-scoped, bound derived
  as 0.5 x ROUND_CHAIN_MAX), key-silent routing to Stage 2, ratio-derivable
  quotients in `derivable_from_key`.
- Sentinel: monotonicity moved to status TOTALS; current-state resolution is
  max-stage-then-latest; scope migrations reported, not halted.
- Shared resolvers: `provenance.evidence_dir()` (one admissible-bundle rule) and
  `canon.key_addresses_label()` (one key-silence rule).

**Before/after capture (movers audit):**

| metric | before | after |
|---|---|---|
| floor #1 detection | 40/40, CI [91.2%, 100%] | 40/40, CI [91.2%, 100%] — held after EACH loosening |
| floor #2 finding-bearing items | 4 of 26 | 1 of 27 |
| floor #2 CHARGEABLE | 0 | 0 |
| chargeable CI upper | 12.9% | 12.5% |
| terminal states | 1 | 0 (ORDER-002 item 1 revert) |
| ledger rows | 3,165 | 3,167 (nothing deleted) |
| gate | RED | RED |

**Expected movers from the write gate itself: ZERO.** It restricts FUTURE
writes only; no existing row was rewritten by it.

**Movers attributable to the RESOLUTION RULE specifically (ORDER-003 item 7):**
exactly one — `agent_204#02`, `verified` → `machine_passed`. The rule changed
which row *speaks* for a lineage (highest stage, then latest at that stage); it
rewrote nothing. Every other lineage resolves to the same row under both the old
and new rules, so the decomposition is unchanged apart from that single item.
Verified by re-running `sentinel.py` across the full ledger: 8 status|scope
cells, 1,951 distinct items, partition remainder 0, all status totals
non-decreasing.

**Also inert (verified, not assumed):** `make_row` adoption in stage 0 adds an
explicit `"stage": null` to stage-0 rows that previously omitted the key. That
moves the ledger's sha once and changes no meaning — `questions.jsonl` is
byte-identical, row count holds at 3,167, and the decomposition is unchanged,
because the sentinel already treats an absent `stage` and `stage: null` as one
cell.

## What's in the box

| File | What it is |
|---|---|
| `maxxer-mode-prompt.md` | v1.2 orchestrator prompt — full-strength mode: dual solvers, three diverse blind verifiers, adversary on 100%, wide fan-out. |
| `budget-mode-prompt.md` | v1.2 orchestrator prompt — constrained mode: full Python layer, single frontier verifier risk-ranked, decorrelated audits, remakes at Maxxer strength. Budget = run size, never model tier. |
| `config.template.yaml` | Every parameter for both modes with defaults. Fill the paths, save as `config.yaml`, keep defaults to start. |
| `START_CHECKLIST.md` | The 13 things to gather or decide before the first run. |
| `pack/chart_of_accounts.txt` | SEED chart-of-accounts whitelist — extend from your textbook's own examples. |
| `pack/account_aliases.csv` | SEED alias table (canonical name ↔ textbook variants) — grows from `UNKNOWN_ACCOUNT` flags. |
| `pack/entry_templates.yaml` | SEED canonical entry templates — grows automatically from adjudicated escalations. |
| `tests/loop_protocol_sim.py` | Proves loop structure: termination, conservation, retry budgets, skip-list integrity, work bound, no-livelock. 304/304 scenarios pass. |
| `tests/checker_quality_sim.py` | Proves calibration defenses: probes halt garbage checkers with measured numbers; independent ensembles cube detection (10% → 0.1% escapes); targeted audits catch ~3x more escapes at equal spend. |

## Quick start

1. Work through `START_CHECKLIST.md` items 1–10 (materials, edition note, models, spend cap).
2. Fill the paths in `config.template.yaml`, save as `config.yaml`.
3. Paste `budget-mode-prompt.md` into your runner (Claude Code or any agent with
   Python and file access), point it at the config and this folder.
4. Pilot: ~100 questions end-to-end. Hand-check 50 random questions yourself —
   they become `goldens/` and seed the probe stream. Eyeball `taxonomy.json` once.
5. Full run. Watch the convergence log and `calibration.md`.

## The guarantee, honestly stated

- Machine-verifiable content (most of this corpus): independently re-derived by
  saved, re-runnable Python — as close to absolute as verification gets.
- Judgment content: quoted-citation grounding, diverse blind ensembles,
  adversarial attack, and human adjudication of escalations.
- Checker quality: measured live by unlabeled probes and goldens; blindness
  tested by wrong-key canaries; violations halt loudly, never degrade silently.
- Residual error: bounded by your own random hand-audit (200 clean ⇒ <~1.5% at
  95% confidence), not assumed to be zero.

## Changelog

- **v1.4.4 (spec catch-up — no invalidation)** — communication becomes
  law: the 01-COMMUNICATION.md mailbox protocol (comms/ orders/reports/
  operator, append-only, per-item statuses, evidence-in-same-commit,
  BLOCKED-names-the-path) governs all inter-agent traffic.

- **v1.4.3 (navigation release — no invalidation)** — repo reorganized
  for zero-inference navigation: 00-START-HERE with role/where-is/hard-
  rules tables, numbered docs/ read order (01–08), RULEBOOK renamed from
  the fold-queue, generated-folder do-not-edit marker, textbook-source
  gitignore. Prompt content unchanged except file references.

- **v1.4.2 (spec catch-up — no invalidation)** — the case-history layer
  becomes law: DECISIONS/RETIRED/casebook are maintained artifacts;
  settled rulings reopen only by citation with new evidence; retired
  numbers and approaches are never silently re-tried.

- **v1.4.1 (spec catch-up #2 — no invalidation)** — folds the post-1.4
  campaign law: single-write-API state stores with full-vector sentinels
  and precondition-synthesizing fault injection; the declared unit ladder
  (rows/hashes/lineages); write-time provenance and comparison-symmetry;
  the role-invariant solver builder; generated pack governance (banned-
  pattern generator, chart invariants, full-store sweeps, dominance);
  and the reporting epistemics (fixtures age with semantics, stacked
  defects, informational-number rot, proactive re-attribution).

- **v1.4 (spec catch-up — no invalidation)** — the campaign's accumulated
  law folded into both prompts: dual-independent-derivation standard;
  detection = coverage x adjudication with corroboration retired; the shared
  canon library and full comparator specification (precision inheritance,
  context-scoped rounding, net-per-account, declared scale, structured label
  grammar, comparison-site register); provenance-scoped caching and the
  repair classes (keys and stems included); builder wiring with wiring
  probes; calibration v2 (symmetric end-to-end probes, two statistical
  floors, five-way floor taxonomy, golden tiers and truth-versioning,
  regression goldens, meter probes with the physics bound); ledger law
  (merge-never-truncate, sentinel with two-direction attribution, bundles
  as source of truth, timestamped generated exports); pack governance
  (suffix barriers, dominance rule, NOTATION class, resolution curves,
  duplicates); pre-registration, enforcement probes, and the full process
  discipline. Rationale and incident provenance: docs/07-RULEBOOK.md.

- **v1.0** — two-mode pipeline: normalize, blind Python solvers, grounded
  verification, adversary, coverage audit, hash-keyed ledger.
- **v1.1** — convergence loop (four-tier triage, investigate-before-remake,
  remakes at full strength, two terminal states, retry budgets); journal-entry
  template layer + alias table; authority setting (textbook_then_gaap);
  syllabus-scoped coverage; loop protocol proven by simulation.
- **v1.2** — calibration layer (seeded probes, goldens, wrong-key canaries,
  per-concept detection tracking, ensemble correlation monitoring, framing
  bake-off); leak & degeneracy detection; pack provenance, format profiling,
  and cohort escalation with auto pack-diffs; repair-vs-remake rule; split
  uniform/targeted audit; defenses proven by simulation. Model policy: both
  modes run frontier-class models (Opus); Budget economizes on breadth —
  passes, sampling, caching — never on model quality, and audits must be
  decorrelated (different model or framing).
- **v1.3** — first live-run discoveries folded in: part-level class routing
  (judgment parts inside computable questions route to Stage 2); comparator
  specification (structural, symmetric within solver scope, canonicalize
  before diff, versioned, free re-compare from cached solver outputs);
  statistical floor clearance (95% lower bound over ≥30 falsifiable probes);
  family-parameterized solvers; corpus-driven pack bootstrap (alias harvest);
  mismatch classification before remake spend; artifact-vs-verdict cache
  split; first-batch gate before full fan-out.
