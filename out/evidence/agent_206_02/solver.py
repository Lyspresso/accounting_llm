#!/usr/bin/env python3
"""Blind solver for item agent_206#02 - Riverton Machine Co. (LO 12-1).

FACT PATTERN (taken only from stem.md)
--------------------------------------
Equipment acquired 1/1/Year 1 for $50,000 cash.
Residual value $5,000; useful life 5 years; total estimated output 10,000 units.
Year 1 actual production 1,800 units.
Books use double-declining-balance (DDB).
On 12/31/Year 3, after recording Year 3 DDB depreciation, the equipment is sold
for $12,000 cash.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, applied per period (each year's depreciation expense is rounded
to the cent as it is computed, and the rounded amount is what rolls forward into
accumulated depreciation and the next year's carrying amount).  There is no
round-at-end restatement.  No present-value work is required by this item, so no
PV table factors are involved.  All money is decimal.Decimal; no floats are used
anywhere in the computation.  Every figure here happens to fall on a whole
dollar, but the quantization is applied deliberately regardless.

METHOD NOTES (textbook conventions, ACCOUNT-343 ch. 11-12)
----------------------------------------------------------
* Straight-line and SYD and units-of-production all depreciate the DEPRECIABLE
  COST = cost - residual value.
* DDB applies a constant rate of 2 / useful life to the DECLINING CARRYING
  AMOUNT and does NOT subtract residual value when applying the rate.  Because
  of that, the final year's expense is a forced amount (plug): the amount needed
  to bring the carrying amount down to - but not below - residual value.  The
  floor is enforced in every year, not just the last, so an asset can never be
  depreciated below residual.
* Disposal: derecognize cost and accumulated depreciation; the difference
  between proceeds and carrying amount is the gain or loss
  (account titles "Gain on Sale of Equipment" / "Loss on Sale of Equipment").

Run:  python3 solver.py    -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to cents using the course convention, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Given facts (stem only)
# ---------------------------------------------------------------------------
COST = Decimal("50000")
RESIDUAL = Decimal("5000")
LIFE_YEARS = 5
TOTAL_OUTPUT_UNITS = Decimal("10000")
YEAR1_UNITS = Decimal("1800")
DISPOSAL_YEAR = 3
PROCEEDS = Decimal("12000")

DEPRECIABLE_COST = COST - RESIDUAL


# ---------------------------------------------------------------------------
# Part a - Year 1 depreciation under each of the four LO 12-1 methods
# ---------------------------------------------------------------------------
def straight_line_year1() -> Decimal:
    return money(DEPRECIABLE_COST / Decimal(LIFE_YEARS))


def syd_year1() -> Decimal:
    # sum-of-the-years'-digits denominator = 1 + 2 + ... + n
    syd_denominator = Decimal(sum(range(1, LIFE_YEARS + 1)))
    fraction_year1 = Decimal(LIFE_YEARS) / syd_denominator  # 5/15
    return money(DEPRECIABLE_COST * fraction_year1)


def ddb_rate() -> Decimal:
    # 2 x the straight-line rate; residual is NOT subtracted from the base
    return Decimal(2) / Decimal(LIFE_YEARS)


def ddb_year1() -> Decimal:
    return money(COST * ddb_rate())


def uop_year1() -> Decimal:
    per_unit = DEPRECIABLE_COST / TOTAL_OUTPUT_UNITS
    return money(per_unit * YEAR1_UNITS)


# ---------------------------------------------------------------------------
# Part b - full DDB schedule Years 1-5 with the residual-value floor / plug
# ---------------------------------------------------------------------------
def ddb_schedule():
    rate = ddb_rate()
    rows = []
    carrying = COST
    accumulated = Decimal("0")
    for year in range(1, LIFE_YEARS + 1):
        computed = money(carrying * rate)
        # residual-value floor: never depreciate below residual value
        max_allowed = carrying - RESIDUAL
        if max_allowed < 0:
            max_allowed = Decimal("0")
        if computed > max_allowed:
            expense = money(max_allowed)   # forced amount / plug
            plug = True
        else:
            expense = computed
            plug = False
        accumulated += expense
        ending = carrying - expense
        rows.append(
            {
                "year": year,
                "beginning_carrying_amount": carrying,
                "rate": rate,
                "computed_before_floor": computed,
                "depreciation_expense": expense,
                "accumulated_depreciation": accumulated,
                "ending_carrying_amount": ending,
                "is_plug": plug,
            }
        )
        carrying = ending
    return rows


# ---------------------------------------------------------------------------
# Part c - disposal on 12/31/Year 3 after recording Year 3 DDB depreciation
# ---------------------------------------------------------------------------
def disposal(rows):
    row = rows[DISPOSAL_YEAR - 1]
    accum = row["accumulated_depreciation"]
    carrying = row["ending_carrying_amount"]
    result = money(PROCEEDS - carrying)  # positive = gain, negative = loss
    return accum, carrying, result


def num(d: Decimal):
    """Emit a plain JSON number: int when whole, else float."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


def main() -> None:
    sl1 = straight_line_year1()
    syd1 = syd_year1()
    ddb1 = ddb_year1()
    uop1 = uop_year1()

    rows = ddb_schedule()
    accum_y3, carrying_y3, gain_loss = disposal(rows)

    # internal consistency guards (not reported as answers)
    assert rows[-1]["ending_carrying_amount"] == RESIDUAL, rows[-1]
    assert rows[0]["depreciation_expense"] == ddb1
    assert sum(r["depreciation_expense"] for r in rows) == DEPRECIABLE_COST

    answers = [
        {"label": "a: Year 1 depreciation - straight-line", "value": num(sl1)},
        {"label": "a: Year 1 depreciation - sum-of-the-years'-digits", "value": num(syd1)},
        {"label": "a: Year 1 depreciation - double-declining-balance", "value": num(ddb1)},
        {"label": "a: Year 1 depreciation - units-of-production", "value": num(uop1)},
    ]

    for r in rows:
        y = r["year"]
        answers.append(
            {
                "label": f"b: DDB schedule Year {y} - beginning carrying amount",
                "value": num(r["beginning_carrying_amount"]),
            }
        )
        answers.append(
            {
                "label": (
                    f"b: DDB schedule Year {y} - depreciation expense"
                    + (" (plug to residual floor)" if r["is_plug"] else "")
                ),
                "value": num(r["depreciation_expense"]),
            }
        )
        answers.append(
            {
                "label": f"b: DDB schedule Year {y} - accumulated depreciation",
                "value": num(r["accumulated_depreciation"]),
            }
        )
        answers.append(
            {
                "label": f"b: DDB schedule Year {y} - ending carrying amount",
                "value": num(r["ending_carrying_amount"]),
            }
        )

    answers.append(
        {
            "label": "c: gain on sale of equipment, 12/31/Year 3 (gain)",
            "value": num(abs(gain_loss)),
        }
    )

    journal_entries = [
        {
            "part": "a",
            "description": "Dec 31, Year 1 - period-end adjusting entry, DDB",
            "lines": [
                {"account": "Depreciation Expense", "debit": num(ddb1), "credit": 0},
                {"account": "Accumulated Depreciation", "debit": 0, "credit": num(ddb1)},
            ],
        },
        {
            "part": "c",
            "description": "Jan 1, Year 1 - initial recognition of equipment purchased for cash",
            "lines": [
                {"account": "Equipment", "debit": num(COST), "credit": 0},
                {"account": "Cash", "debit": 0, "credit": num(COST)},
            ],
        },
        {
            "part": "c",
            "description": (
                "Dec 31, Year 3 - disposal settlement after recording Year 3 DDB depreciation"
            ),
            "lines": [
                {"account": "Cash", "debit": num(PROCEEDS), "credit": 0},
                {"account": "Accumulated Depreciation", "debit": num(accum_y3), "credit": 0},
                {"account": "Equipment", "debit": 0, "credit": num(COST)},
                {
                    "account": (
                        "Gain on Sale of Equipment"
                        if gain_loss >= 0
                        else "Loss on Sale of Equipment"
                    ),
                    "debit": 0 if gain_loss >= 0 else num(abs(gain_loss)),
                    "credit": num(abs(gain_loss)) if gain_loss >= 0 else 0,
                },
            ],
        },
    ]

    for je in journal_entries:
        dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
        cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
        assert dr == cr, (je["part"], dr, cr)

    plug_year = next(r["year"] for r in rows if r["is_plug"])
    notes = (
        "d (narrative, no figure): DDB applies its constant rate (2/5 = 40%) to the "
        "declining carrying amount rather than to depreciable cost, so residual value "
        "never enters the rate calculation; the method still lands exactly on residual "
        "because the residual-value floor forces the final year's expense to be a plug - "
        f"in Year {plug_year} the computed "
        f"{rows[plug_year - 1]['computed_before_floor']} is replaced by "
        f"{rows[plug_year - 1]['depreciation_expense']}, the amount needed to bring "
        "carrying amount down to the $5,000 residual and no further. "
        "Part c disposal: proceeds $12,000 less carrying amount at 12/31/Year 3 of "
        f"${carrying_y3} = a GAIN of ${abs(gain_loss)}."
    )

    out = {
        "id": "agent_206#02",
        "rounding_convention": (
            "ROUND_HALF_UP to the cent, applied per period (rounded annual expense "
            "rolls forward into accumulated depreciation and the next year's carrying "
            "amount); decimal.Decimal throughout, no floats; no PV factors needed"
        ),
        "answers": answers,
        "journal_entries": journal_entries,
        "insufficient_info": False,
        "notes": notes,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
