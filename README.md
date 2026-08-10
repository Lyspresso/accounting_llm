# The Question-Verifier Project — what we're doing here

*Current as of 2026-08-10. Owner: Lydia. Executor: a Claude Code agent on
her machine. Reviewer: Claude (this chat). One page of orientation; the
detailed law lives in `v1.4-fold-queue.md`, the live state in `STATUS.md`.*

---

## The goal

Lydia has **1,828 AI-generated study questions** built from her
intermediate accounting course (Hanlon 4e). AI-generated means every
question — and every answer key — is untrusted until proven. The project's
spec, set on day one: **every question verified correct, the textbook's
coverage mapped, and the whole method packaged as a reusable skill** that
can verify any question bank against any textbook.

The end state for each question is one of exactly two labels:

- **`verified`** — with a reproducible evidence bundle: the blind solver
  code, the grounded quotes, the adversarial attack that failed.
- **`needs_human`** — with a complete dossier of why the machine couldn't
  decide.

Nothing exits any other way. A pipeline that can only say "correct"
manufactures correctness.

## How it works (the short version)

1. **Stage 0 — Normalize.** Parse everything into structured form
   (13,970 journal-entry lines), quarantine malformed items, catch
   answer leaks, govern the chart of accounts.
2. **Stage 1 — Deterministic verification.** Blind Python solvers (keys
   withheld) recompute every machine-checkable figure; a specified
   comparator decides equivalence. 1,232 questions are in this class.
3. **Stage 2 — Grounded verification.** For judgment questions (596
   MCQs), blind verifiers must cite verbatim textbook passages. A pass
   without a quote is no evidence at all.
4. **Stage 3 — Adversarial pass.** A dedicated attacker tries to break
   every survivor. Surviving attacks is part of "verified."
5. **A convergence loop** with strict retry budgets turns flags into one
   of the two terminal states. Repairs (key fixes, stem clarifications,
   treatment notes) are free; only confirmed content defects spend
   remake budget.

Two run modes share all of this law: **Maxxer** (maximum redundancy) and
**Budget** (same frontier models, smaller run size — sampling and caching,
never weaker checks).

## The idea that turned out to matter most

**Instrument quality is measured, never assumed.** Every checker, meter,
matcher, and state store carries its own tests: mutation probes with
statistical floors, wrong-key canaries that verify solvers stay blind,
known-usage meter fixtures with a physics bound, a ledger sentinel with
fault-injection, wiring probes proving pack knowledge actually reaches
solver prompts. Seven standing fixtures run green before anything ships.

This paid for itself many times over. The campaign's scary numbers — a
67% "pass rate," a 27% "false-positive rate," a 2.4× cost "correction" —
were, on investigation, **all instrument artifacts**: a comparator that
couldn't read LaTeX, a matcher pairing figures against unrelated zeros, a
meter double-counting retries. The question bank itself keeps measuring
**roughly 93–95% clean**. Across two days of maximum scrutiny, the
genuine content defects found number four — a mis-totaled T-account, a
$1 rounding error, one ambiguous sentence, one solver working without a
rule it was never given — and each produced a repair, not a remake.

The system also now **catches itself**: the last three significant
defects (a context asymmetry between solvers, an over-confident finding,
a provenance stamp recording the wrong moment in time) were found and
reported by the executor before review got there — including retracting
its own headline conclusion, unprompted.

## The working structure

Three roles, deliberately separated:

- **Executor** (Claude Code agent): runs the pipeline, writes reports,
  ships artifacts.
- **Reviewer** (this chat): audits every report against its own
  arithmetic, issues self-contained order blocks, keeps the living
  rulebook (`v1.4-fold-queue.md`) and folds it into the versioned
  prompts.
- **Operator** (Lydia): owns the budget, countersigns the goldens that
  certify the false-positive floor, and makes the calls no machine
  should — everything else is designed to need her only at tranche
  boundaries.

Standing rules of engagement: artifacts over verbal claims, exports
regenerated and timestamped at every send, predictions registered with
metric and threshold before the result exists, and every number that
moves names its mover.

## Where it stands right now

| | |
|---|---|
| Corpus | 1,828 lineages = 1,819 active + 9 retired duplicates |
| Funnel | 1,719 unverified · 86 machine_passed · 14 failed · 9 DUPLICATE_OF |
| Terminal (`verified`/`needs_human`) | **0 — by design**: the launch gate is RED, so nothing may claim completion yet |
| Launch gate | **RED** — the false-positive floor must re-clear under the finished stack |
| Family gate (LO 11-8) | LIFTED — treatment note proven in all solver contexts |
| Measured cost | trim harness **39,652 billable/question** (cheaper than baseline's 50,091) |
| Budget decision | **Option B recorded**: tranche 1 = 10M token hard cap ≈ **182 questions**, fires automatically the moment the gate turns GREEN |

## What remains

1. Close `agent_204` under the write-time provenance fix (the last open
   instrument item).
2. Build the five-way false-positive taxonomy (so the floor counts only
   true contradictions, with coverage debt reported separately).
3. Family/duplicate clustering over the 596 Class B questions.
4. **Pre-flight**: both statistical floors re-measured under the exact
   production stack. GREEN launches tranche 1 automatically; RED says
   precisely why.
5. Production tranches to the caps, human go/no-go between tranches.
6. Lydia's countersign session (~90 minutes against worked evidence,
   packet regenerated first) — certifies the false-positive ceiling;
   blocks nothing else.

## The one-line ethos

Certainty is an output of evidence, never a substitute for it — and that
applies to the instruments doing the measuring just as much as to the
questions being measured.

---

## Repository map

- `README.md` — this overview.
- `skill/` — the portable question-verifier skill, v1.4: both mode
  prompts, config template, subject pack, and simulation tests
  (`skill/tests/` must stay green).
- `docs/RELEASING.md` — the continuous-release standard: publish every
  change as a new patch version, keep every old release verbatim under
  `skill/releases/`, compare any two on demand.
- `docs/v1.4-fold-queue.md` — the living rulebook: every rule with the
  incident that taught it. Single source; the skill README points here.
- `deliverables/` — the executor's current generated artifacts
  (STATUS.md is the live state; regenerate via deliver.sh, never edit).
- `reviewer/REVIEW-STATE.md` — the reviewer's pick-up-here file: gates,
  in-flight orders, prediction ledger, runway.
- `reviewer/hand_check_verdicts_v1.json` — the 20-item cross-check
  packet (ai_cross_checked tier; operator countersign pending).
- `docs/archive/` — historical snapshots, superseded but preserved.

Working protocol for agents joining via this repo: pull fresh, read
reviewer/REVIEW-STATE.md + deliverables/STATUS.md, work, commit your
artifacts, push before ending the session. The remote is the memory.
