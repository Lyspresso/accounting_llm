#!/usr/bin/env python3
"""Solver for item agent_214#02 — Redwood Circuits LLC (LO 12-7).

Fact pattern (from stem.md), December 31, Year 3, three plant assets HELD FOR USE
with impairment indicators present for all three:

    Asset                   Cost      Accum. depr.   Recoverable cost (undisc.)   Fair value
    A - Precision press   400,000       100,000              350,000                280,000
    B - Curing oven       700,000       200,000              420,000                310,000
    C - Assembly conveyor 900,000       150,000              750,000                600,000

After any write-down, Asset B is used 5 more years, revised residual $10,000,
straight-line. Assets A and C keep their pre-existing policies.

METHOD (ASC 360-10-35, per the course text, Chapter 12 LO 12-7):
  Step 1 - Recoverability test (assets in use):
      carrying amount = cost - accumulated depreciation
      the asset FAILS (is impaired) only if recoverable cost < carrying amount.
      A tie (recoverable cost == carrying amount) PASSES: no impairment loss,
      even if fair value is below carrying amount.
  Step 2 - Impairment test (only for assets that failed step 1):
      impairment loss = carrying amount - fair value
  The written-down fair value becomes the asset's new cost basis and is
  depreciated over the remaining useful life (restoration is prohibited).
  Entry form follows Demo 12-7: debit Loss on Impairment, credit Accumulated
  Depreciation (the asset account keeps its historical cost).

ROUNDING CONVENTION:
  All money is decimal.Decimal; floats are never used. Amounts are quantized to
  the cent with ROUND_HALF_UP, applied per period (each year's straight-line
  depreciation is rounded on its own, then accumulated) rather than once at the
  end. No present-value factors are involved in this item, so no table-vs-formula
  choice arises. Every figure here happens to land on a whole dollar; the
  quantization is still applied deliberately so the convention is explicit.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(value) -> Decimal:
    """Quantize to the cent using ROUND_HALF_UP (the course convention)."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """Render a Decimal as a plain JSON number (int when it is a whole dollar)."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- fact pattern
ASSETS = [
    {
        "key": "A",
        "name": "Precision press",
        "cost": Decimal("400000"),
        "accum_depr": Decimal("100000"),
        "recoverable_cost": Decimal("350000"),
        "fair_value": Decimal("280000"),
    },
    {
        "key": "B",
        "name": "Curing oven",
        "cost": Decimal("700000"),
        "accum_depr": Decimal("200000"),
        "recoverable_cost": Decimal("420000"),
        "fair_value": Decimal("310000"),
    },
    {
        "key": "C",
        "name": "Assembly conveyor",
        "cost": Decimal("900000"),
        "accum_depr": Decimal("150000"),
        "recoverable_cost": Decimal("750000"),
        "fair_value": Decimal("600000"),
    },
]

# Asset B, subsequent measurement after the write-down
B_REMAINING_LIFE_YEARS = 5
B_REVISED_RESIDUAL = Decimal("10000")
B_FIRST_YEAR_AFTER_WRITEDOWN = 4  # Years 4 through 8


# ------------------------------------------------- part a: test each asset
for a in ASSETS:
    a["carrying_amount"] = money(a["cost"] - a["accum_depr"])
    # Step 1: impaired only if recoverable cost is LESS THAN carrying amount.
    a["fails_recoverability"] = a["recoverable_cost"] < a["carrying_amount"]
    if a["fails_recoverability"]:
        # Step 2: loss = carrying amount - fair value (floored at zero).
        loss = a["carrying_amount"] - a["fair_value"]
        a["impairment_loss"] = money(loss if loss > 0 else Decimal("0"))
    else:
        a["impairment_loss"] = money(Decimal("0"))

impaired = [a for a in ASSETS if a["impairment_loss"] > 0]
total_impairment = money(sum((a["impairment_loss"] for a in impaired), Decimal("0")))


# ------------------------------------------------- part c: Asset B schedule
b = next(a for a in ASSETS if a["key"] == "B")
# New cost basis = fair value (only if written down; otherwise carrying amount).
b_new_basis = money(b["fair_value"] if b["impairment_loss"] > 0 else b["carrying_amount"])
b_depreciable_base = money(b_new_basis - B_REVISED_RESIDUAL)

schedule = []
accumulated = Decimal("0.00")
carrying = b_new_basis
for i in range(B_REMAINING_LIFE_YEARS):
    year = B_FIRST_YEAR_AFTER_WRITEDOWN + i
    if i < B_REMAINING_LIFE_YEARS - 1:
        # Round each period on its own (round-per-period convention).
        expense = money(b_depreciable_base / Decimal(B_REMAINING_LIFE_YEARS))
    else:
        # Final period absorbs any rounding drift so the book value lands
        # exactly on the residual value.
        expense = money(b_depreciable_base - accumulated)
    accumulated = money(accumulated + expense)
    carrying = money(b_new_basis - accumulated)
    schedule.append(
        {
            "year": year,
            "beginning_carrying": money(carrying + expense),
            "expense": expense,
            "accumulated_since_writedown": accumulated,
            "ending_carrying": carrying,
        }
    )

assert schedule[-1]["ending_carrying"] == money(B_REVISED_RESIDUAL), "schedule must end at residual"

year4 = schedule[0]


# ------------------------------------------------- assemble reported answers
answers = []

# a. carrying amount and impairment loss for each asset (both are asked for).
for a in ASSETS:
    answers.append(
        {
            "label": f"a: Asset {a['key']} ({a['name']}) carrying amount at Dec 31, Year 3",
            "value": num(a["carrying_amount"]),
        }
    )
for a in ASSETS:
    answers.append(
        {
            "label": f"a: Asset {a['key']} ({a['name']}) impairment loss",
            "value": num(a["impairment_loss"]),
        }
    )

# b. total of the single combined impairment entry.
answers.append(
    {
        "label": "b: total impairment loss recorded in the single Dec 31, Year 3 entry",
        "value": num(total_impairment),
    }
)

# c. Asset B subsequent measurement schedule, Years 4-8.
for row in schedule:
    answers.append(
        {
            "label": f"c: Asset B depreciation expense, Year {row['year']}",
            "value": num(row["expense"]),
        }
    )
for row in schedule:
    answers.append(
        {
            "label": f"c: Asset B carrying amount at end of Year {row['year']}",
            "value": num(row["ending_carrying"]),
        }
    )


# ------------------------------------------------- journal entries
journal_entries = []

# b. One combined entry for all required write-downs.
b_lines = [
    {"account": "Loss on Impairment", "debit": num(total_impairment), "credit": 0}
]
for a in impaired:
    b_lines.append(
        {
            "account": f"Accumulated Depreciation ({a['name']})",
            "debit": 0,
            "credit": num(a["impairment_loss"]),
        }
    )
journal_entries.append({"part": "b", "date": "December 31, Year 3", "lines": b_lines})

# c. Year 4 depreciation entry for Asset B.
journal_entries.append(
    {
        "part": "c",
        "date": "December 31, Year 4",
        "lines": [
            {
                "account": "Depreciation Expense",
                "debit": num(year4["expense"]),
                "credit": 0,
            },
            {
                "account": "Accumulated Depreciation (Curing oven)",
                "debit": 0,
                "credit": num(year4["expense"]),
            },
        ],
    }
)

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"part {je['part']} does not balance: {dr} vs {cr}"


# ------------------------------------------------- narrative / notes
test_lines = []
for a in ASSETS:
    verdict = (
        "FAILS recoverability (recoverable cost < carrying amount) -> impairment test applies"
        if a["fails_recoverability"]
        else "PASSES recoverability (recoverable cost >= carrying amount) -> no impairment loss"
    )
    test_lines.append(
        f"Asset {a['key']}: carrying ${a['carrying_amount']:,} vs recoverable ${a['recoverable_cost']:,} "
        f"and fair value ${a['fair_value']:,} -- {verdict}; loss ${a['impairment_loss']:,}."
    )

notes = (
    "Part a recoverability results: " + " ".join(test_lines) + " "
    "Asset C is the tie case: undiscounted recoverable cost of $750,000 exactly equals its "
    "$750,000 carrying amount, so it is recoverable and no loss is recognized even though fair "
    "value is $600,000. "
    "Part c: Asset B's new cost basis is its $310,000 fair value; ($310,000 - $10,000 residual) / 5 "
    "years = $60,000 straight-line per year for Years 4-8, ending at the $10,000 residual. "
    "Part d (qualitative, no figure to report): the recoverability test is the gate, and it uses "
    "UNDISCOUNTED expected future net cash flows, not fair value. If those undiscounted cash flows "
    "from using and eventually disposing of the asset equal or exceed the carrying amount, the "
    "carrying amount is considered recoverable and step 2 is never reached -- so no loss is recorded "
    "even though the asset's fair value (a discounted / market-exit measure) is below carrying "
    "amount. This keeps write-downs to clearly impaired assets only; Asset C illustrates it."
)

result = {
    "id": "agent_214#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP to the cent applied per period "
        "(each year's straight-line depreciation rounded individually, final year absorbs "
        "drift so book value lands on residual); no present-value factors in this item"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
