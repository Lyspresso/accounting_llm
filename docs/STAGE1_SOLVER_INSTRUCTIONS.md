# Stage 1 — Deterministic verification: blind solver

You derive the answer to one accounting question **independently**. You are not
grading anything and there is no answer key anywhere you are allowed to look.
The pipeline — not you — compares your result to the key afterwards.

## Blindness (the invariant this whole stage rests on)

Read **only** your assigned `stem.md`. These are off-limits, and opening one
invalidates this item and everything downstream of it:

- `out/questions.jsonl` (contains `solution`)
- `staged-work/core-demo/results/`, `blind/keys/`, `blind/solved/`
- `CORE_DEMO_QUESTIONS_AND_ANSWERS.md`, `ACCOUNT343_QUESTION_BANK_TAGGED.md`
- any `verify50/`, `verify100/`, `proof/`, `fix_pass/`, `VERIFY*`, `ARITH_*` file

Wrong-key canaries run in this stream to test that the wall holds. If you open
one by accident, return `peeked: true` — an honest true costs one item, a false
one silently contaminates the run.

The textbook IS allowed and encouraged:
`<the local course-files directory — set `paths.textbook` in config.yaml>`

## Pack treatment notes — apply these, they override your default judgement

These record where this edition's demonstrated treatment differs from another
treatment that is defensible in practice. A solver that picks the other one
produces internally consistent work that is wrong for this course, and the
divergence propagates through every downstream figure.

- **LO 11-8, donated assets with incidental costs.** Record the asset at its
  **full fair value**, credit **Cash** for costs actually paid (legal, title,
  transfer), and credit **Contribution Revenue NET of those costs** (fair value
  − costs paid). Do **not** capitalize the costs into the asset, and do **not**
  include them in the depreciable base. Demo 11-8: `Building 400,000 / Land
  100,000 / Cash 5,000 / Contribution Revenue ($500,000 − $5,000) 495,000`;
  Review 11-8 depreciates 375,000, so the 5,000 is absent from the base.

- **Rounding in schedules.** Inside an amortization / effective-interest / ROU
  or lease-liability rollforward, this edition rounds to whole dollars in the
  journal entries while running PVs at full precision, and says so
  ("Amounts adjusted to whole numbers to simplify recording ... If we prepare
  this schedule in Excel with unlimited decimals, the numbers slightly vary").
  Either convention is acceptable; state which you used and close the schedule
  exactly to face or to zero.

The full library, with authority citations, is
`out/pack_proposals/treatment_notes.yaml`.

## What to produce

Write `solver.py` **into your own evidence directory** (the one holding your
`stem.md`), run it, and save its stdout to `solver_output.json` in that same
directory. Both files are the evidence bundle; they must be re-runnable by
someone else with no other context.

Rules for the solver:

1. **`decimal.Decimal` for money. Never floats.** Floats silently produce
   `0.1 + 0.2 != 0.3` errors in exactly the cent-level places that matter here.
2. **State the rounding convention explicitly** in a module docstring and apply
   it deliberately — round-per-period vs round-at-end, PV table factor vs exact
   formula. This course uses ROUND_HALF_UP per period.
3. Derive from the fact pattern in the stem. Hard-coding a number you did not
   compute defeats the entire stage.
4. The script must run standalone: `python3 solver.py` prints one JSON object.

`solver_output.json` shape:

```json
{
  "id": "<your item id>",
  "rounding_convention": "ROUND_HALF_UP per period, PV via table factors",
  "answers": [{"label": "a: write-down under item approach", "value": 6000}],
  "journal_entries": [
    {"part": "b", "lines": [{"account": "Cost of Goods Sold", "debit": 6000, "credit": 0}]}
  ],
  "insufficient_info": false,
  "notes": ""
}
```

- `answers` — only the figures the Required parts ask for. Not intermediates,
  not check figures. Plain numbers, no `$` or commas.
- `journal_entries` — every entry a part asked you to prepare. Debits must equal
  credits; if yours do not, fix the derivation rather than the numbers.
- `insufficient_info` — true if the stem genuinely underdetermines the answer.
  Say what is missing in `notes`. Never invent a fact to close a gap.

Accuracy over speed. Recompute anything you are unsure of.
