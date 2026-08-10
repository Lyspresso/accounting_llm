#!/usr/bin/env python3
"""Blind solver for item agent_305#01.

FACT PATTERN (from stem.md only)
--------------------------------
Oct 1, Year 1: Steelhaven Components LLC (Dec 31 year-end) sells inventory with a
fair value of $28,000 and receives a three-year, NONINTEREST-BEARING note with
face $37,268, due Sept 30, Year 4. Market rate for similar risk = 10%. No cash
interest during the term. Ignore cost of goods sold.

Check embedded in the stem: 28,000 * 1.10^3 = 28,000 * 1.331 = 37,268, so the
$28,000 fair value IS the present value of the note at the 10% market rate and
the implicit rate equals the market rate. Nothing needs to be imputed.

METHOD
------
ASC 835-30 / effective-interest method, gross presentation as used in the course
text (Chapter 8, Demo 8-5C "Noncurrent Note Receivable [Stated Rate = 0%; Market
Rate = 10%]"):

  * Note Receivable is carried at FACE, with "Discount on Note Receivable" as a
    contra-asset. Initial discount = face - present value.
  * Sales Revenue is credited at the fair value (= PV) of the consideration.
  * With a 0% stated rate there is no cash interest, so each period's interest
    revenue EQUALS that period's discount amortization:
        interest = opening carrying amount x market rate
        closing carrying amount = opening + interest
  * The amortization schedule runs on NOTE years (Oct 1 -> Sept 30), which do
    not line up with the Dec 31 reporting date. Per Demo 8-5C part b, each
    note-year's interest is ALLOCATED straight-line across the reporting periods
    it spans: 3 months (Oct 1 - Dec 31) and 9 months (Jan 1 - Sept 30).
  * A reporting period's adjusting entry is the sum of every allocated slice
    falling in that period.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. No floats anywhere.

1. Currency unit: whole dollars (the stem and the course text both work in whole
   dollars for this problem type).
2. ROUND_HALF_UP, applied PER PERIOD, not once at the end. Each note-year's
   effective interest is computed on that year's OPENING carrying amount and
   rounded to the dollar before it rolls into the closing carrying amount.
3. Final-period plug: the last note-year's interest is set to
   (face - opening carrying amount) so the schedule closes exactly on the face
   amount and total interest equals the initial discount to the penny. (Here the
   plug happens to equal the unrounded computation exactly, so no forcing occurs
   -- the solver asserts this.)
4. Time allocation: the 3-month stub slice is computed as
   note_year_interest * 3/12 and rounded ROUND_HALF_UP; the 9-month slice is
   taken as the REMAINDER (note_year_interest - stub) so each note-year's
   allocation ties exactly to its schedule interest. This matches the text's
   treatment (Demo 8-5C part b splits 601 into 301 / 300).
   Here every split is exact, so rounding is not actually invoked.
5. PV: not needed as a table lookup -- the stem supplies the PV ($28,000) and its
   own arithmetic check. The solver re-verifies 28,000 * 1.10^3 = 37,268 with
   exact Decimal arithmetic rather than trusting the stem.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("1")  # whole-dollar rounding unit


def d(x):
    return Decimal(str(x))


def money(x):
    """ROUND_HALF_UP to the currency unit (whole dollars)."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x):
    """Decimal -> JSON-safe number (int when integral)."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem, nothing else)
# ---------------------------------------------------------------------------
FAIR_VALUE = d("28000")      # fair value of inventory sold = PV of the note
FACE = d("37268")            # face amount due Sept 30, Year 4
MARKET_RATE = d("0.10")      # market rate for similar risk
TERM_YEARS = 3               # Oct 1 Yr 1 -> Sept 30 Yr 4
STUB_MONTHS = d("3")         # Oct 1 -> Dec 31 (falls in the earlier calendar yr)
MONTHS_PER_YEAR = d("12")

# --- verify the stem's own PV arithmetic exactly (no floats) ----------------
compound = (Decimal("1") + MARKET_RATE) ** TERM_YEARS      # exactly 1.331
implied_face = money(FAIR_VALUE * compound)
assert compound == d("1.331"), compound
assert implied_face == FACE, (implied_face, FACE)

# ---------------------------------------------------------------------------
# (a) Initial recognition, Oct 1 Year 1
# ---------------------------------------------------------------------------
initial_discount = FACE - FAIR_VALUE            # 37,268 - 28,000

je_a = {
    "part": "a",
    "date": "October 1, Year 1",
    "description": "Record receipt of noninterest-bearing note in exchange for inventory sold",
    "lines": [
        {"account": "Note Receivable", "debit": num(FACE), "credit": 0},
        {"account": "Discount on Note Receivable", "debit": 0, "credit": num(initial_discount)},
        {"account": "Sales Revenue", "debit": 0, "credit": num(FAIR_VALUE)},
    ],
}

# ---------------------------------------------------------------------------
# (b) Note-year effective-interest amortization schedule
#     Periods end Sept 30 of Years 2, 3, 4.
# ---------------------------------------------------------------------------
note_year_labels = [
    "Note year 1 (Oct 1, Yr 1 - Sept 30, Yr 2)",
    "Note year 2 (Oct 1, Yr 2 - Sept 30, Yr 3)",
    "Note year 3 (Oct 1, Yr 3 - Sept 30, Yr 4)",
]
period_end_labels = ["September 30, Year 2", "September 30, Year 3", "September 30, Year 4"]

schedule = []
carrying = FAIR_VALUE
for i in range(TERM_YEARS):
    opening = carrying
    if i == TERM_YEARS - 1:
        # Final period plugs to face so the schedule closes exactly.
        interest = FACE - opening
        unrounded_check = money(opening * MARKET_RATE)
        assert interest == unrounded_check, (interest, unrounded_check)
    else:
        interest = money(opening * MARKET_RATE)
    closing = opening + interest
    schedule.append(
        {
            "note_year": note_year_labels[i],
            "period_end": period_end_labels[i],
            "opening_carrying_amount": num(opening),
            "cash_interest": 0,                       # 0% stated rate
            "interest_revenue": num(interest),        # = discount amortization
            "discount_amortization": num(interest),
            "closing_carrying_amount": num(closing),
        }
    )
    carrying = closing

assert carrying == FACE, carrying
total_interest = sum((d(r["interest_revenue"]) for r in schedule), Decimal("0"))
assert total_interest == initial_discount, (total_interest, initial_discount)

# ---------------------------------------------------------------------------
# (c) Allocation of each note-year's interest to calendar reporting periods
#     3 months ending Dec 31  /  9 months ending Sept 30
# ---------------------------------------------------------------------------
allocation_rows = []
# reporting-period buckets, in chronological order
bucket_labels = [
    "December 31, Year 1",
    "December 31, Year 2",
    "December 31, Year 3",
    "September 30, Year 4",
]
buckets = {lbl: Decimal("0") for lbl in bucket_labels}

for i, row in enumerate(schedule):
    ny_interest = d(row["interest_revenue"])
    stub = money(ny_interest * STUB_MONTHS / MONTHS_PER_YEAR)   # 3 months
    remainder = ny_interest - stub                              # 9 months (plug)
    assert stub + remainder == ny_interest

    # 3-month slice lands in the Dec 31 of calendar year (i + 1)
    stub_bucket = "December 31, Year {}".format(i + 1)
    # 9-month slice lands in the reporting period ending the following Sept 30,
    # i.e. Dec 31 of calendar year (i + 2) for note years 1 and 2; for the final
    # note year it lands in the short period ending Sept 30, Year 4 (maturity).
    if i == TERM_YEARS - 1:
        rem_bucket = "September 30, Year 4"
    else:
        rem_bucket = "December 31, Year {}".format(i + 2)

    buckets[stub_bucket] += stub
    buckets[rem_bucket] += remainder

    allocation_rows.append(
        {
            "note_year": row["note_year"],
            "note_year_interest": num(ny_interest),
            "months_3_period": stub_bucket,
            "months_3_amount": num(stub),
            "months_9_period": rem_bucket,
            "months_9_amount": num(remainder),
        }
    )

assert sum(buckets.values(), Decimal("0")) == initial_discount

# ---------------------------------------------------------------------------
# (d) Period-end interest JEs: Dec 31 Years 1-3 and Sept 30 Year 4
# ---------------------------------------------------------------------------
interest_jes = []
for lbl in bucket_labels:
    amt = buckets[lbl]
    interest_jes.append(
        {
            "part": "d",
            "date": lbl,
            "description": "Record amortization of discount / accrue interest revenue",
            "lines": [
                {"account": "Discount on Note Receivable", "debit": num(amt), "credit": 0},
                {"account": "Interest Revenue", "debit": 0, "credit": num(amt)},
            ],
        }
    )

# ---------------------------------------------------------------------------
# (e) Maturity JE, Sept 30 Year 4 (after the final interest entry) + proof
# ---------------------------------------------------------------------------
je_e = {
    "part": "e",
    "date": "September 30, Year 4",
    "description": "Record collection of the note's face value at maturity",
    "lines": [
        {"account": "Cash", "debit": num(FACE), "credit": 0},
        {"account": "Note Receivable", "debit": 0, "credit": num(FACE)},
    ],
}

cash_collected = FACE
assert FAIR_VALUE + total_interest == cash_collected

# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------
journal_entries = [je_a] + interest_jes + [je_e]

for je in journal_entries:
    dr = sum((d(l["debit"]) for l in je["lines"]), Decimal("0"))
    cr = sum((d(l["credit"]) for l in je["lines"]), Decimal("0"))
    assert dr == cr, (je["date"], dr, cr)

answers = [
    # a
    {"label": "a: initial discount on note receivable (Oct 1, Year 1)",
     "value": num(initial_discount)},
    # b - note-year effective-interest schedule
    {"label": "b: interest revenue / discount amortization, note year ended Sept 30 Year 2",
     "value": schedule[0]["interest_revenue"]},
    {"label": "b: carrying amount of note, Sept 30 Year 2",
     "value": schedule[0]["closing_carrying_amount"]},
    {"label": "b: interest revenue / discount amortization, note year ended Sept 30 Year 3",
     "value": schedule[1]["interest_revenue"]},
    {"label": "b: carrying amount of note, Sept 30 Year 3",
     "value": schedule[1]["closing_carrying_amount"]},
    {"label": "b: interest revenue / discount amortization, note year ended Sept 30 Year 4",
     "value": schedule[2]["interest_revenue"]},
    {"label": "b: carrying amount of note, Sept 30 Year 4",
     "value": schedule[2]["closing_carrying_amount"]},
    # c - allocation to calendar reporting periods
    {"label": "c: note year 1 interest allocated to 3 months ended Dec 31 Year 1",
     "value": allocation_rows[0]["months_3_amount"]},
    {"label": "c: note year 1 interest allocated to 9 months ended Sept 30 Year 2",
     "value": allocation_rows[0]["months_9_amount"]},
    {"label": "c: note year 2 interest allocated to 3 months ended Dec 31 Year 2",
     "value": allocation_rows[1]["months_3_amount"]},
    {"label": "c: note year 2 interest allocated to 9 months ended Sept 30 Year 3",
     "value": allocation_rows[1]["months_9_amount"]},
    {"label": "c: note year 3 interest allocated to 3 months ended Dec 31 Year 3",
     "value": allocation_rows[2]["months_3_amount"]},
    {"label": "c: note year 3 interest allocated to 9 months ended Sept 30 Year 4",
     "value": allocation_rows[2]["months_9_amount"]},
    {"label": "c: total interest revenue recognized, reporting period ended Dec 31 Year 1",
     "value": num(buckets["December 31, Year 1"])},
    {"label": "c: total interest revenue recognized, reporting period ended Dec 31 Year 2",
     "value": num(buckets["December 31, Year 2"])},
    {"label": "c: total interest revenue recognized, reporting period ended Dec 31 Year 3",
     "value": num(buckets["December 31, Year 3"])},
    {"label": "c: total interest revenue recognized, period ended Sept 30 Year 4",
     "value": num(buckets["September 30, Year 4"])},
    # e - proof
    {"label": "e: total interest revenue over the term of the note",
     "value": num(total_interest)},
    {"label": "e: cash collected at maturity (sales revenue 28000 + total interest 9268)",
     "value": num(cash_collected)},
]

out = {
    "id": "agent_305#01",
    "rounding_convention": (
        "decimal.Decimal only, no floats. Whole-dollar currency unit, ROUND_HALF_UP "
        "applied per period (not once at the end): each note-year's effective interest "
        "= opening carrying amount x 10%, rounded, then rolled forward. Final note-year "
        "interest plugged to face - opening carrying amount so the schedule closes on "
        "37268 (plug equals the unrounded figure here, asserted). 3/9 month allocation: "
        "3-month stub = note-year interest x 3/12 ROUND_HALF_UP, 9-month slice taken as "
        "the remainder so each note year ties. PV not table-looked-up: the stem supplies "
        "PV = 28000 and 28000 x 1.10^3 = 37268 is re-verified in exact Decimal arithmetic."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Zero-interest note, so interest revenue equals discount amortization each period "
        "and cash interest is 0 throughout. Gross presentation per ACC 343 Ch.8 Demo 8-5C: "
        "Note Receivable at face 37268 with contra Discount on Note Receivable 9268, Sales "
        "Revenue at fair value 28000. Amortization runs on note years (Oct 1 - Sept 30); "
        "each note year's interest is split 3/12 to the calendar year of issuance and 9/12 "
        "to the following reporting period, so the Dec 31 Year 2 and Year 3 adjusting "
        "entries each combine two slices. Every split is exact at these amounts, so no "
        "rounding is actually invoked. COGS ignored per the stem."
    ),
}

print(json.dumps(out, indent=2))
