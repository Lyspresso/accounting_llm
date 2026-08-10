# accounting_llm

A blind verification pipeline for an AI-generated accounting question bank.

The bank is 1,828 items written by 400 authoring agents for an Intermediate
Accounting II course. The problem this repo solves is that **nobody knows which
of those items are right**, and a study app built on a wrong answer key teaches
the wrong thing. The pipeline re-derives each question's answer from the question
text alone, with the answer key held back, and only then compares.

---

## ⚠️ THIS REPOSITORY IS PUBLIC — READ BEFORE YOUR FIRST COMMIT

**Never commit textbook-derived source material.** The question bank is derived
from a commercial textbook and its courseware. It is licensed to one person for
personal use. Publishing it — even inside a data file, a test fixture, an
evidence bundle, or a report — is copyright infringement, and a public git
history cannot be un-published by deleting the file later.

Specifically, **never commit**:

| Never commit | Why |
|---|---|
| `questions.jsonl` / any corpus dump | every stem **and** every worked answer key, verbatim |
| `out/evidence*/**` | each bundle carries a verbatim `stem.md` |
| generated harness scripts (`out/*.js`) | full question stems embedded in prompt strings |
| batch/queue files (`*_batch.json`, `parity50.json`) | same, embedded in prompts |
| any report that quotes key text | reproduces solutions in prose |
| chapter text, PDFs, Canvas downloads | verbatim textbook |

The `.gitignore` blocks these **by pattern**, so new files of the same shape land
on the safe side by default. Do not add exceptions to it without reading the file
you are excepting.

**What is safe to commit:** the pipeline source, the fixtures, the shell runners,
and reports that carry only counts, hashes, item ids, and mechanism descriptions.

If you ever need to share the corpus with a collaborator, share it out-of-band.
Do not solve it by making a public repo "temporarily" private — the history is
already distributed by then.

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
docs/                    reports that carry no key text
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

A fixture is only trusted here once it has been shown to **fail** against the bug
it claims to catch. Green proves nothing on its own.

## Join protocol — start here if you are picking this up

1. Read this file's public-repo warning. It is the one mistake that cannot be
   undone.
2. `sh run_fixtures.sh`. If anything is RED, fix that before touching anything
   else — a red fixture means the instruments are lying.
3. `python3 preflight.py`. This prints both floors and the gate. Do not start a
   production run on a RED gate.
4. `python3 sentinel.py`. Confirms no ledger history was lost.
5. Read `docs/fp-taxonomy.md` for the four open comparator gaps. That is the
   work queue.

**Corpus setup.** The corpus is not in this repo and never will be. Point
`config.template.yaml` at your local copy and save it as `config.yaml`, which is
gitignored.

## Status

Pre-production. The gate is RED by design until both floors clear with
statistical bounds — this pipeline is built to refuse to run, not to produce a
number.
