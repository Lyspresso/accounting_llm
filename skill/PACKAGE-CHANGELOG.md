# Question-Bank Verification — v1.2 Package

A two-mode, loop-based pipeline that verifies an AI-generated question bank
against its textbook and syllabus. Every question ends `verified` with a
reproducible evidence bundle or `needs_human` with a complete dossier.
Coverage and checker quality are measured, never asserted. Built for
accounting first; the SUBJECT PACK section swaps to port it to any class.

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
