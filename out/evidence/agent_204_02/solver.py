#!/usr/bin/env python3
"""Blind solver for item agent_204#02 -- contributed equipment, partial-year
straight-line depreciation schedule, and scrap disposal.

Run:  python3 solver.py            -> prints one JSON object on stdout

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats are used anywhere.
Rounding is ROUND_HALF_UP to the cent, applied PER PERIOD (each year's
depreciation expense is rounded as it is computed, and the accumulated
depreciation / net book value columns are built by accumulating those
already-rounded per-period amounts).  No present-value work is required by
this fact pattern, so no PV table factors are involved.  Every figure in this
particular problem happens to fall on a whole dollar, so the rounding step is
a no-op here, but it is applied deliberately rather than assumed away.

ACCOUNTING BASIS (ASC 958-605; textbook LO 11-8, Demo 11-8)
-----------------------------------------------------------
An unconditional, nonreciprocal transfer of a fixed asset is recognized by the
RECIPIENT at the asset's fair value in the period received, with the credit to
Contribution Revenue measured NET OF ANY COSTS PAID by the recipient.  The
$3,000 legal title-transfer cost is therefore NOT capitalized into the
equipment account; it reduces Contribution Revenue and is paid in cash.
(Demo 11-8 pattern: Building 400,000 / Land 100,000 / Cash 5,000 /
Contribution Revenue 495,000 -- the asset stays at fair value.)

Depreciation therefore runs on the fair value of $180,000, not $183,000.
Year 1 is a partial year: the asset was held from April 1 through December 31,
i.e. 9 of 12 months, and depreciation is taken for the fraction of the year
held.  Years 2 and 3 are full years.

Disposal by scrapping on December 31, Year 3 is recorded AFTER Year 3
depreciation, so the carrying amount removed is the Year 3 year-end NBV.
Proceeds below carrying amount produce a loss on disposal.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(value: Decimal) -> Decimal:
    """Round a Decimal to the cent using ROUND_HALF_UP (course convention)."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Facts taken from the stem
# ---------------------------------------------------------------------------
FAIR_VALUE = Decimal("180000")          # reliable FV of the donated equipment
TITLE_TRANSFER_CASH = Decimal("3000")   # cash paid by Cedar Ridge for title
USEFUL_LIFE_YEARS = Decimal("6")
RESIDUAL_VALUE = Decimal("12000")
MONTHS_HELD_YEAR_1 = Decimal("9")       # April 1 -> December 31 = 9 months
MONTHS_IN_YEAR = Decimal("12")
SCRAP_PROCEEDS = Decimal("9500")        # cash from salvage dealer, 12/31 Yr 3

# ---------------------------------------------------------------------------
# (a) April 1, Year 1 contribution
# ---------------------------------------------------------------------------
equipment_cost = money(FAIR_VALUE)                       # asset at fair value
contribution_revenue = money(FAIR_VALUE - TITLE_TRANSFER_CASH)  # net of costs

entry_a = {
    "part": "a",
    "description": "April 1, Year 1 -- record unconditional contribution of "
                   "equipment received (asset at fair value; contribution "
                   "revenue net of transfer costs paid).",
    "lines": [
        {"account": "Equipment", "debit": equipment_cost, "credit": Decimal("0")},
        {"account": "Cash", "debit": Decimal("0"), "credit": money(TITLE_TRANSFER_CASH)},
        {"account": "Contribution Revenue", "debit": Decimal("0"), "credit": contribution_revenue},
    ],
}

# ---------------------------------------------------------------------------
# (b) Subsequent measurement schedule, Years 1-3
# ---------------------------------------------------------------------------
depreciable_base = equipment_cost - RESIDUAL_VALUE
full_year_depreciation = money(depreciable_base / USEFUL_LIFE_YEARS)

year_1_depreciation = money(
    (depreciable_base / USEFUL_LIFE_YEARS) * (MONTHS_HELD_YEAR_1 / MONTHS_IN_YEAR)
)

annual_expense = {
    1: year_1_depreciation,
    2: full_year_depreciation,
    3: full_year_depreciation,
}

schedule = []
accumulated = Decimal("0.00")
for year in (1, 2, 3):
    expense = annual_expense[year]
    accumulated = money(accumulated + expense)   # accumulate rounded amounts
    nbv = money(equipment_cost - accumulated)
    schedule.append(
        {"year": year, "depreciation_expense": expense,
         "accumulated_depreciation": accumulated, "net_book_value": nbv}
    )

year_3_nbv = schedule[2]["net_book_value"]
accum_at_disposal = schedule[2]["accumulated_depreciation"]

# ---------------------------------------------------------------------------
# (c) December 31, Year 1 and December 31, Year 2 depreciation adjusting JEs
# ---------------------------------------------------------------------------
def depreciation_entry(part: str, year: int) -> dict:
    amount = annual_expense[year]
    label = "partial year, 9 of 12 months held" if year == 1 else "full year"
    return {
        "part": part,
        "description": f"December 31, Year {year} -- adjusting entry to record "
                       f"straight-line depreciation ({label}).",
        "lines": [
            {"account": "Depreciation Expense", "debit": amount, "credit": Decimal("0")},
            {"account": "Accumulated Depreciation -- Equipment",
             "debit": Decimal("0"), "credit": amount},
        ],
    }


entry_c1 = depreciation_entry("c", 1)
entry_c2 = depreciation_entry("c", 2)

# ---------------------------------------------------------------------------
# (d) December 31, Year 3 depreciation JE and the scrap disposal JE
# ---------------------------------------------------------------------------
entry_d1 = depreciation_entry("d", 3)

loss_on_disposal = money(year_3_nbv - SCRAP_PROCEEDS)
gain_on_disposal = money(SCRAP_PROCEEDS - year_3_nbv)

disposal_lines = [
    {"account": "Cash", "debit": money(SCRAP_PROCEEDS), "credit": Decimal("0")},
    {"account": "Accumulated Depreciation -- Equipment",
     "debit": accum_at_disposal, "credit": Decimal("0")},
]
if loss_on_disposal > 0:
    disposal_lines.append(
        {"account": "Loss on Disposal of Equipment",
         "debit": loss_on_disposal, "credit": Decimal("0")}
    )
elif gain_on_disposal > 0:
    disposal_lines.append(
        {"account": "Gain on Disposal of Equipment",
         "debit": Decimal("0"), "credit": gain_on_disposal}
    )
disposal_lines.append(
    {"account": "Equipment", "debit": Decimal("0"), "credit": equipment_cost}
)

entry_d2 = {
    "part": "d",
    "description": "December 31, Year 3 -- scrap the equipment; remove cost and "
                   "accumulated depreciation, record cash from the salvage "
                   "dealer and the resulting loss.",
    "lines": disposal_lines,
}

journal_entries = [entry_a, entry_c1, entry_c2, entry_d1, entry_d2]

# Self-check: every entry must balance.
for entry in journal_entries:
    debits = sum((line["debit"] for line in entry["lines"]), Decimal("0"))
    credits = sum((line["credit"] for line in entry["lines"]), Decimal("0"))
    assert debits == credits, (entry["part"], entry["description"], debits, credits)

# ---------------------------------------------------------------------------
# Answers -- only the figures the Required parts ask for.
# Parts a, c and d ask for journal entries (reported in journal_entries).
# Part b asks for the schedule figures, reported here.
# ---------------------------------------------------------------------------
answers = []
for row in schedule:
    y = row["year"]
    answers.append({"label": f"b: Year {y} depreciation expense",
                    "value": row["depreciation_expense"]})
    answers.append({"label": f"b: Year {y} year-end accumulated depreciation",
                    "value": row["accumulated_depreciation"]})
    answers.append({"label": f"b: Year {y} year-end net book value",
                    "value": row["net_book_value"]})


def jsonable(obj):
    """Convert Decimals to exact JSON numbers (int when whole)."""
    if isinstance(obj, Decimal):
        if obj == obj.to_integral_value():
            return int(obj)
        return float(obj)
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [jsonable(v) for v in obj]
    return obj


result = {
    "id": "agent_204#02",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per "
        "period (each year's depreciation rounded as computed, accumulated "
        "depreciation built from the rounded per-period amounts); no PV "
        "factors needed"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Per ASC 958-605 and textbook LO 11-8 / Demo 11-8, the recipient records "
        "the contributed asset at fair value ($180,000) and credits Contribution "
        "Revenue net of costs paid ($180,000 - $3,000 = $177,000); the $3,000 "
        "title-transfer cash is NOT capitalized. Depreciable base = $180,000 - "
        "$12,000 residual = $168,000 over 6 years = $28,000 per full year; Year 1 "
        "is 9/12 of a year (April 1 - December 31). The December 31, Year 3 scrap "
        "is recorded after Year 3 depreciation, so NBV removed is the Year 3 "
        "year-end NBV and the shortfall versus the $9,500 proceeds is a loss."
    ),
}

if __name__ == "__main__":
    print(json.dumps(jsonable(result), indent=2))
