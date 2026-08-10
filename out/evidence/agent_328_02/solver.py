#!/usr/bin/env python3
"""
Blind solver for item agent_328#02.

Fact pattern (Quillridge Components Inc., calendar year-end, LO 11-1 / 11-7):
    Self-constructed production equipment. Costs accumulate in Construction in
    Process (CIP) during Year 1 under full costing. Complete and placed in
    service July 1, Year 1.

        Direct materials            $120,000
        Direct labor                 280,000
        Incremental overhead          35,000
        Applied general overhead      25,000
        Total CIP                   $460,000

    Fair value of a similar unit of equal capacity and quality on July 1:
    $440,000.  Depreciation: straight-line, salvage $40,000, 8-year life.
    On Dec 31 Year 2, after recording Year 2 depreciation, the equipment is
    sold for $355,000 cash.

Authorities applied (textbook, chapter 11):
  * Full costing: materials, labor, incremental overhead AND applied general
    overhead are all capitalized into CIP.
  * Fair-value ceiling on self-constructed assets: "If total construction costs
    exceed the fair value of a similar asset of equal capacity and quality, the
    excess is recognized as a loss in the period incurred."  The maximum
    valuation allowed is fair value.  Cost $460,000 > FV $440,000, so Equipment
    is recorded at $440,000 and a $20,000 "Loss on Construction of Equipment"
    is recognized at settlement (Demo 11-1B pattern).
  * Depreciation begins when the asset is placed in service (July 1, Year 1),
    so Year 1 gets a half year.  Depreciable base is the CAPITALIZED cost
    ($440,000, i.e. fair value), not the $460,000 of construction cost.
  * Disposal (LO 11-7): depreciation is updated through the disposal date
    first, then cost and accumulated depreciation are derecognized and the
    difference between proceeds and carrying amount is a gain or loss.  Cash is
    received, so the account is "Loss on Sale of Equipment".

ROUNDING CONVENTION
    All money is decimal.Decimal.  Rounding is ROUND_HALF_UP to the cent
    (two decimal places), applied PER PERIOD -- each period's depreciation
    charge is rounded as it is computed and the rounded charge is what
    accumulates, rather than rounding only a cumulative total at the end.
    (In this fact pattern every figure is an exact whole dollar, so the
    convention does not change any reported number; it is applied and stated
    for reproducibility.)  Partial-year depreciation uses the exact fraction of
    a year the asset was in service (6/12 for Year 1), not a table factor.
    Output values are emitted as integers when they are whole dollars.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x):
    """Round a Decimal to the cent, ROUND_HALF_UP. Applied per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def emit(d):
    """JSON-friendly number: int when whole dollars, else float-safe string->float."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------------------
# Stem facts
# ---------------------------------------------------------------------------
DIRECT_MATERIALS = Decimal("120000")
DIRECT_LABOR = Decimal("280000")
INCREMENTAL_OH = Decimal("35000")
APPLIED_GENERAL_OH = Decimal("25000")

FAIR_VALUE_AT_COMPLETION = Decimal("440000")
SALVAGE = Decimal("40000")
USEFUL_LIFE_YEARS = Decimal("8")

# In service July 1, Year 1 -> 6 of 12 months in Year 1.
YEAR1_SERVICE_FRACTION = Decimal("6") / Decimal("12")
YEAR2_SERVICE_FRACTION = Decimal("1")

SALE_PROCEEDS = Decimal("355000")

# ---------------------------------------------------------------------------
# (a) Accumulate construction costs in CIP
# ---------------------------------------------------------------------------
total_cip = money(DIRECT_MATERIALS + DIRECT_LABOR + INCREMENTAL_OH + APPLIED_GENERAL_OH)

entry_a = {
    "part": "a",
    "date": "Year 1 (summary, as incurred)",
    "description": "Accumulate self-construction costs in Construction in Process",
    "lines": [
        {"account": "Construction in Process", "debit": emit(total_cip), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": emit(total_cip)},
    ],
}

# ---------------------------------------------------------------------------
# (b) July 1, Year 1 settlement JE with fair-value ceiling
# ---------------------------------------------------------------------------
# Maximum valuation allowed = fair value. Excess of cost over FV = loss.
capitalized_cost = money(min(total_cip, FAIR_VALUE_AT_COMPLETION))
construction_loss = money(max(Decimal("0"), total_cip - FAIR_VALUE_AT_COMPLETION))

lines_b = [{"account": "Equipment", "debit": emit(capitalized_cost), "credit": 0}]
if construction_loss > 0:
    lines_b.append(
        {
            "account": "Loss on Construction of Equipment",
            "debit": emit(construction_loss),
            "credit": 0,
        }
    )
lines_b.append(
    {"account": "Construction in Process", "debit": 0, "credit": emit(total_cip)}
)

entry_b = {
    "part": "b",
    "date": "July 1, Year 1",
    "description": (
        "Transfer Construction in Process to Equipment at the fair-value "
        "ceiling; expense the excess of construction cost over fair value"
    ),
    "lines": lines_b,
}

# ---------------------------------------------------------------------------
# (c) Dec 31, Year 1 period-end depreciation adjusting entry
# ---------------------------------------------------------------------------
depreciable_base = money(capitalized_cost - SALVAGE)
annual_depreciation = money(depreciable_base / USEFUL_LIFE_YEARS)

# Round per period: each period's charge is rounded as computed.
dep_year1 = money(annual_depreciation * YEAR1_SERVICE_FRACTION)
dep_year2 = money(annual_depreciation * YEAR2_SERVICE_FRACTION)

entry_c = {
    "part": "c",
    "date": "December 31, Year 1",
    "description": (
        "Period-end adjusting entry: straight-line depreciation for the "
        "half year the equipment was in service"
    ),
    "lines": [
        {"account": "Depreciation Expense", "debit": emit(dep_year1), "credit": 0},
        {
            "account": "Accumulated Depreciation - Equipment",
            "debit": 0,
            "credit": emit(dep_year1),
        },
    ],
}

# ---------------------------------------------------------------------------
# (d) Subsequent measurement schedule
# ---------------------------------------------------------------------------
accum_dep_y1 = money(dep_year1)
carrying_y1 = money(capitalized_cost - accum_dep_y1)

accum_dep_y2 = money(accum_dep_y1 + dep_year2)
carrying_y2 = money(capitalized_cost - accum_dep_y2)

# ---------------------------------------------------------------------------
# (e) Dec 31, Year 2 depreciation JE and disposal JE
# ---------------------------------------------------------------------------
entry_e1 = {
    "part": "e",
    "date": "December 31, Year 2",
    "description": "Period-end adjusting entry: full-year straight-line depreciation",
    "lines": [
        {"account": "Depreciation Expense", "debit": emit(dep_year2), "credit": 0},
        {
            "account": "Accumulated Depreciation - Equipment",
            "debit": 0,
            "credit": emit(dep_year2),
        },
    ],
}

# Disposal: proceeds vs carrying amount AFTER Year 2 depreciation.
disposal_result = money(SALE_PROCEEDS - carrying_y2)  # negative => loss

lines_e2 = [
    {"account": "Cash", "debit": emit(SALE_PROCEEDS), "credit": 0},
    {
        "account": "Accumulated Depreciation - Equipment",
        "debit": emit(accum_dep_y2),
        "credit": 0,
    },
]
if disposal_result < 0:
    lines_e2.append(
        {
            "account": "Loss on Sale of Equipment",
            "debit": emit(-disposal_result),
            "credit": 0,
        }
    )
lines_e2.append(
    {"account": "Equipment", "debit": 0, "credit": emit(capitalized_cost)}
)
if disposal_result > 0:
    lines_e2.append(
        {
            "account": "Gain on Sale of Equipment",
            "debit": 0,
            "credit": emit(disposal_result),
        }
    )

entry_e2 = {
    "part": "e",
    "date": "December 31, Year 2",
    "description": "Sale of equipment for cash; derecognize cost and accumulated depreciation",
    "lines": lines_e2,
}

journal_entries = [entry_a, entry_b, entry_c, entry_e1, entry_e2]

# ---------------------------------------------------------------------------
# Balance proof (part b explicitly asks for the proof; all entries checked)
# ---------------------------------------------------------------------------
for je in journal_entries:
    dr = sum(Decimal(str(ln["debit"])) for ln in je["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in je["lines"])
    assert dr == cr, f"Entry {je['part']} ({je['date']}) does not balance: {dr} vs {cr}"

# ---------------------------------------------------------------------------
# Reported figures = only what the Required parts ask for as numbers.
# Parts a, b, c, e are journal entries (reported in journal_entries).
# Part d is a schedule -> its six figures are the reported answers.
# ---------------------------------------------------------------------------
answers = [
    {"label": "d: cost at Dec 31, Year 1", "value": emit(capitalized_cost)},
    {"label": "d: accumulated depreciation at Dec 31, Year 1", "value": emit(accum_dep_y1)},
    {"label": "d: carrying amount at Dec 31, Year 1", "value": emit(carrying_y1)},
    {"label": "d: cost at Dec 31, Year 2 (before disposal)", "value": emit(capitalized_cost)},
    {
        "label": "d: accumulated depreciation at Dec 31, Year 2 (before disposal)",
        "value": emit(accum_dep_y2),
    },
    {
        "label": "d: carrying amount at Dec 31, Year 2 (before disposal)",
        "value": emit(carrying_y2),
    },
]

output = {
    "id": "agent_328#02",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per "
        "period (each period's depreciation charge rounded as computed, then "
        "accumulated); partial-year depreciation uses the exact 6/12 service "
        "fraction, not a table factor. All figures here are exact whole dollars."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Fair-value ceiling applied: CIP cost $460,000 exceeds the $440,000 fair "
        "value of a similar unit, so Equipment is capitalized at $440,000 and the "
        "$20,000 excess is recognized as Loss on Construction of Equipment on "
        "July 1, Year 1. Depreciation base is the capitalized $440,000 less "
        "$40,000 salvage over 8 years = $50,000/yr; Year 1 is a half year "
        "because the asset was placed in service July 1. The Dec 31, Year 2 "
        "schedule column is stated after Year 2 depreciation and before the "
        "disposal, matching the stem's sequence. Every entry was asserted to "
        "balance (debits = credits), which is the part-b proof."
    ),
}

print(json.dumps(output, indent=2))
