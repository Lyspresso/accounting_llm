# accounting_llm

A blind verification pipeline for an AI-generated accounting question bank.

The bank is 1,828 items written by 400 authoring agents for an Intermediate
Accounting II course. The problem this repo solves is that **nobody knows which
of those items are right**, and a study app built on a wrong answer key teaches
the wrong thing. The pipeline re-derives each question's answer from the question
text alone, with the answer key held back, and only then compares.

---

## The corpus is here, and that is deliberate

The 1,828 questions are **AI-authored** — written by 400 CORE DEMO authoring
agents, one pack per agent, each keyed to a learning objective. Every record
carries `provenance.generated_by: "core-demo authoring agent"` and an empty
`citations` list. They are not reproduced from a textbook.

That matters for what this repo is *for*. The claim being tested is that
**AI-generated study material is unreliable until something verifies it**, and
that claim is unfalsifiable without the corpus and the evidence in the open. So
both ship:

| Path | What it is |
|---|---|
| `out/questions.jsonl` | 1,828 normalized items — stem, worked solution, parsed answer key, content hash, lineage |
| `corpus/source-packs/` | the 400 original authoring packs, unmodified, with their metadata sidecars |
| `out/evidence*/` | 191 blind-solver runs across 6 harnesses — the stem each solver saw, the solver it wrote, its output, its scoring, its provenance stamp |
| `out/ledger.jsonl` | 3,165 rows, full history, superseded rows retained on purpose |
| `goldens/` | 28 adjudicated reference items that calibrate the false-positive floor |

Because the corpus is in the tree, **a fresh clone runs**. No configuration is
needed to reproduce the fixtures or the gate.

What stays out is machine-local or regenerable: `config.yaml` (absolute paths),
and `out/reports/`.

**The textbook itself is a different question.** Chapter files, PDFs and
courseware exports are not here and should not be added — those *are* the
publisher's. A handful of short citations of a demonstration problem appear in
comments where they justify a specific comparator rule; that is ordinary
technical citation, not reproduction.

---

## Where the work stands

Two calibration floors gate any production run. Both are measured, not asserted.

| Floor | Requirement | Measured | Verdict |
|---|---|---|---|
| #1 detection — seeded defects must FAIL | ≥ 85% | 40/40 = 100%, CI [91.2%, 100%] | **PASS** |
| #2 false positive — known-clean items must PASS | upper CI ≤ 10% | 4/26 = 15.4%, CI [6.1%, 33.5%] | **FAIL** |

**Launch gate: RED.** No production tranche has run.

Floor #2 has two independent blockers, and only one of them is engineering:

1. **Sample size.** At 26 goldens a *flawless* run still bounds at 12.9%. The
   floor is arithmetically unreachable at this n no matter how good the
   comparator is. It needs **≥ 35 clean goldens**.
2. **Four comparator gaps**, each with a named mechanism — see
   `docs/fp-taxonomy.md`. All four are *loosenings*, so floor #1 must be
   **re-measured after each one**; a comparator that accepts more also detects
   less.

Of every finding that kept floor #2 red, **zero are true false positives**. The
breakdown is 2 `GOLDEN_WRONG`, 10 `MATCHER_ARTIFACT`, 1 `HASH_MIXING`.

## What the pipeline actually found in the bank

Across all items examined so far, **almost every "defect" investigated turned
out to be an instrument defect, not a bank defect.** That is the headline result
and it is why the calibration floors exist at all.

Genuine key defects found: **three.**

- `agent_130#00` — T-account credit total off by 15,000 *(repaired)*
- `agent_130#00` — key omits the entry its own `Required (b)` demands for the
  restricted-cash change *(repair **proposed, not applied** — the bank is never
  edited without the owner's per-item approval)*
- `agent_283#02` — $1 present-value rounding

## Design invariants

These are the rules the code enforces, each written after the failure that
proved it was needed:

- **Blindness.** Solvers see the stem and nothing else. Wrong-key canaries run in
  the same stream to test that the wall holds.
- **Solver-context symmetry.** Every harness builds its instruction region from
  one builder. Two solvers given different rules manufacture disagreements that
  read as findings — that happened, and it cost an item's worth of false
  conclusions before it was caught.
- **Write-time provenance.** Stamps are captured at generation and are immutable.
  A stamp applied retroactively certifies a stale cache as current.
- **One ledger writer.** `ledger_io.append_rows` is merge-only. Two writers using
  `open(..., "w")` each destroyed history before this existed.
- **Two terminal states only** — `verified` and `needs_human`. `machine_passed`
  is progress, not a verdict. Counting it as terminal once reported 671 verified
  items when the true count was zero.
- **Repair is not remake.** A container defect re-normalizes at zero remake cost.
- **Units are declared.** rows → distinct content hashes → lineages. A count
  without its unit is how one lineage gets counted twice.

## Layout

```
*.py                     pipeline source
  canon.py               the single canonicalization library
  compare_stage1_v3.py   the comparator
  ledger_io.py           the only ledger write path
  provenance.py          write-time capture + admissibility audit
  sentinel.py            ledger monotonicity + duplicate policy
  fp_taxonomy.py         five-way false-positive classification
  cluster_b.py           Class B (MCQ) family clustering
  preflight.py           the two calibration floors
test_*.py                fixtures — see below
run_fixtures.sh          runs all of them
corpus/source-packs/     the 400 original authoring packs
out/questions.jsonl      the normalized 1,828-item bank
out/evidence*/           191 blind-solver runs
out/ledger.jsonl         full verification history
goldens/                 28 adjudicated reference items
pack/                    chart of accounts + alias table
docs/                    solver instructions + the open-gaps report
```

## Fixtures

`sh run_fixtures.sh` — eight suites, all currently GREEN. Every one exists
because something broke:

| Fixture | Guards against |
|---|---|
| `test_matcher.py` | label mis-pairing that made a correct derivation look impossible |
| `test_canon.py` | each canonicalization ruling, made permanent |
| `test_wiring.py` | a treatment note reaching one harness and not another |
| `test_chart.py` | hand-written per-ruling patterns leaking orphans |
| `test_provenance.py` | provenance laundering |
| `test_writepath.py` | any writer that truncates the ledger |
| `test_sentinel.py` | the sentinel itself, by fault injection |

Reproduce the gate with `python3 preflight.py`; it prints both floors from the
committed evidence.

A fixture is only trusted here once it has been shown to **fail** against the bug
it claims to catch. Green proves nothing on its own.

## Join protocol — start here if you are picking this up

1. Read "The corpus is here, and that is deliberate" above — it tells you what
   ships and what does not.
2. `sh run_fixtures.sh`. If anything is RED, fix that before touching anything
   else — a red fixture means the instruments are lying.
3. `python3 preflight.py`. This prints both floors and the gate. Do not start a
   production run on a RED gate.
4. `python3 sentinel.py`. Confirms no ledger history was lost.
5. Read `docs/fp-taxonomy.md` for the four open comparator gaps. That is the
   work queue.

**No setup needed.** The corpus, the evidence bundles and the account pack are
all in the tree, so a fresh clone reproduces both floors and every fixture with
no configuration. `config.template.yaml` exists only if you want to point the
pipeline at a *different* corpus.

## Status

Pre-production. The gate is RED by design until both floors clear with
statistical bounds — this pipeline is built to refuse to run, not to produce a
number.

---

> **New here — human or AI? Open [00-START-HERE.md](00-START-HERE.md) and follow it exactly.**

## Repository map (reviewer + knowledge layer)

- `00-START-HERE.md` — the front door: who you are → what you do.
- Top-level `.py` files, `run_fixtures.sh`, `deliver.sh` — the pipeline
  itself (executor-owned). `corpus/`, `goldens/`, `pack/` — the bank,
  the goldens, the subject pack.
- `skill/` — the portable spec: current prompts + `releases/vX.Y.Z/`
  (append-only archive). `skill/PACKAGE-CHANGELOG.md` — version history.
- `docs/01…08` — the knowledge layer IN READ ORDER: glossary, settled
  DECISIONS, RETIRED dead-ends, items casebook, open questions, scored
  predictions, the RULEBOOK (every rule + its incident), releasing.
- `deliverables/` — reviewer's snapshot of executor exports (never
  hand-edit; `deliver.sh` regenerates).
- `reviewer/` — REVIEW-STATE.md (continuity) + hand-check verdicts.
- `comms/` — the mailbox: `orders/`, `reports/`, `operator/`. Protocol:
  `01-COMMUNICATION.md`.

**Source-material rule**: the AI-authored corpus is published here
deliberately (rationale above and in `.gitignore`). Textbook chapter
files (Hanlon 4e text) are NEVER committed — `.gitignore` blocks the
common names; do not work around it.
