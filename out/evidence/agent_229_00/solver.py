#!/usr/bin/env python3
"""Blind solver — Cedarline Outdoor Gear, two-year assurance-type warranty (LO 15-5).

Fact pattern (from stem.md only):
  - Calendar-year company; camping equipment sold with a TWO-YEAR ASSURANCE-type
    warranty (not sold separately) -> loss contingency, expense/liability model
    (ASC 460-10 / ASC 450-20), NOT a separate performance obligation.
  - Estimated warranty cost = 1.5% of that year's product sales, each year.
  - Sales are cash sales; actual claims are paid in cash and charged against the
    accrued Warranty Liability (liability first).
  - Ignore cost of goods sold. No service-type (extended) warranties sold.

    Year | Product sales (cash) | Actual warranty claims paid
       1 |          2,400,000   |      12,000
       2 |          2,800,000   |      48,000
       3 |          3,000,000   |      55,000

Method:
  Accrual_t   = 0.015 * Sales_t                (expense recognized in year of sale,
                                                matching the estimated cost of the
                                                two-year warranty obligation)
  Ending_t    = Beginning_t + Accrual_t - Claims_t
  Beginning_1 = 0 (no warranty liability carried into Year 1)

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats anywhere. Each period's warranty
accrual is computed independently and quantized to the cent with ROUND_HALF_UP
(round-per-period, not round-at-end); the rollforward then chains the already
rounded per-period figures. No present-value discounting is involved in this
item (the warranty obligation is short-term and the stem gives no discount
rate), so no PV table factors are used. Every amount here happens to land on a
whole dollar, so the convention is not outcome-determinative, but it is applied
deliberately.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to the cent, ROUND_HALF_UP, applied per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly plain number: int when whole, else float of the cent value."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- fact pattern
WARRANTY_RATE = Decimal("0.015")  # 1.5% of that year's sales, all three years

SALES = {
    1: Decimal("2400000"),
    2: Decimal("2800000"),
    3: Decimal("3000000"),
}
CLAIMS_PAID = {
    1: Decimal("12000"),
    2: Decimal("48000"),
    3: Decimal("55000"),
}

# ------------------------------------------------- (d) liability rollforward
schedule = []
beginning = money(Decimal("0"))  # no warranty liability entering Year 1
for yr in (1, 2, 3):
    accrual = money(SALES[yr] * WARRANTY_RATE)
    claims = money(CLAIMS_PAID[yr])
    ending = money(beginning + accrual - claims)
    schedule.append(
        {
            "year": yr,
            "beginning": beginning,
            "accrual": accrual,
            "claims": claims,
            "ending": ending,
        }
    )
    beginning = ending

row = {r["year"]: r for r in schedule}

# ------------------------------------------------------------- answers (d only)
# Only the figures a Required part asks for. Parts a, b, c, e, f ask for journal
# entries (reported below); part g is narrative; part d asks for the schedule.
answers = []
for r in schedule:
    y = r["year"]
    answers.append({"label": f"d: Year {y} warranty liability beginning balance",
                    "value": num(r["beginning"])})
    answers.append({"label": f"d: Year {y} warranty accrual (1.5% of sales)",
                    "value": num(r["accrual"])})
    answers.append({"label": f"d: Year {y} actual claims paid (charged to liability)",
                    "value": num(r["claims"])})
    answers.append({"label": f"d: Year {y} warranty liability ending balance",
                    "value": num(r["ending"])})

# ----------------------------------------------------------- journal entries
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = [
    # a. Year 1 product sales (cash sales; assurance warranty is NOT a separate
    #    performance obligation, so the full transaction price is revenue now).
    {
        "part": "a",
        "lines": [
            line("Cash", debit=SALES[1]),
            line("Sales Revenue", credit=SALES[1]),
        ],
    },
    # b. December 31, Year 1 adjusting entry — accrue estimated warranty cost.
    {
        "part": "b",
        "lines": [
            line("Warranty Expense", debit=row[1]["accrual"]),
            line("Warranty Liability", credit=row[1]["accrual"]),
        ],
    },
    # c. Year 1 settlement of actual claims — charged against the liability.
    {
        "part": "c",
        "lines": [
            line("Warranty Liability", debit=row[1]["claims"]),
            line("Cash", credit=row[1]["claims"]),
        ],
    },
    # e. December 31, Year 2 adjusting entry — Year 2 accrual.
    {
        "part": "e",
        "lines": [
            line("Warranty Expense", debit=row[2]["accrual"]),
            line("Warranty Liability", credit=row[2]["accrual"]),
        ],
    },
    # f. Year 3 payment of Year 3 claims, using the liability first. The Year 3
    #    beginning liability (18,000) plus the Year 3 accrual (45,000) = 63,000
    #    exceeds the 55,000 paid, so the entire payment is absorbed by the
    #    liability; no excess is expensed directly.
    {
        "part": "f",
        "lines": [
            line("Warranty Liability", debit=row[3]["claims"]),
            line("Cash", credit=row[3]["claims"]),
        ],
    },
]

# ------------------------------------------------------------------ integrity
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"part {je['part']} does not balance: {dr} vs {cr}"

# Rollforward must articulate year to year.
assert schedule[0]["beginning"] == Decimal("0.00")
for i in range(1, 3):
    assert schedule[i]["beginning"] == schedule[i - 1]["ending"]
for r in schedule:
    assert r["ending"] == r["beginning"] + r["accrual"] - r["claims"]

# ---------------------------------------------------------------------- notes
notes = (
    "Part g (narrative, no figure): An assurance-type warranty is not a separate "
    "performance obligation because it only guarantees the product performs as "
    "promised rather than transferring an additional distinct service, so no part "
    "of the transaction price is deferred; instead the future repair cost is a "
    "probable and reasonably estimable obligation arising from the past sale, so "
    "it is accrued as a loss contingency (Warranty Expense / Warranty Liability) "
    "in the period of sale under the matching principle. Part f: the Year 3 "
    "beginning liability plus the Year 3 accrual covers the 55,000 paid, so the "
    "whole payment is charged to the liability with no direct expense."
)

output = {
    "id": "agent_229#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP quantized to the cent "
        "per period (round-per-period, not round-at-end); no PV discounting "
        "applies to this item"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
