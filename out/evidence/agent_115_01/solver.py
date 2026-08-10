#!/usr/bin/env python3
"""
Blind solver for item agent_115#01 — SummitRidge Logistics Inc., liability-classified
Stock Appreciation Rights (SARs), four-year service period with a negative-expense year.

FACT PATTERN (taken only from stem.md)
--------------------------------------
  * 8,000 SARs granted January 1, Year 1.
  * Each SAR pays cash for the excess of market price at exercise over the
    grant-date market price of $15.
  * Vest after four years; requisite service period = 4 years
    (first exercise expected December 31, Year 4).
  * The EMPLOYEE may require cash settlement  ->  LIABILITY classification.
  * Year-end fair values per SAR: Y1 $2.00, Y2 $5.00, Y3 $3.00, Y4 $6.00.
  * December 31, Year 4: employee exercises all SARs; stock price $21.
    Cash paid = ($21 - $15) x 8,000 = $48,000.

METHOD (ASC 718 liability-classified SARs; matches the course text's
Appendix 20A "Example Two — Stock Appreciation Rights: Recorded as Liability")
-----------------------------------------------------------------------------
For each year end:
    aggregate compensation      = year-end fair value per SAR x number of SARs
    % of service period accrued = elapsed years / requisite service period
    cumulative SARs liability   = aggregate compensation x % accrued
    annual expense              = cumulative liability - prior cumulative liability

A liability award is remeasured to fair value every period, so the annual
expense is a plug that can be NEGATIVE when fair value falls (Year 3 here).
At settlement the liability equals the cash owed, so the settlement entry is
simply a debit to the liability and a credit to Cash — no gain or loss.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to the cent (2 decimal places), applied PER PERIOD: each year's
cumulative liability is rounded to cents first, and that rounded balance is the
basis for the following year's expense plug. No round-at-end restatement is
performed. No present-value discounting applies to this item, so no PV table
factors are used. All inputs here are exact to the cent, so the rounding step
is a no-op in practice; it is applied deliberately anyway so the schedule is
reproducible under a different set of fair values.

Run:  python3 solver.py     (prints one JSON object on stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(value):
    """Round a Decimal to the cent using ROUND_HALF_UP (per-period rounding)."""
    return value.quantize(CENTS, rounding=ROUND_HALF_UP)


def out(value):
    """Render a Decimal for JSON: integer when whole, else a 2-dp number."""
    value = money(value)
    if value == value.to_integral_value():
        return int(value)
    return float(value)


# ---------------------------------------------------------------- given facts
N_SARS = Decimal("8000")
GRANT_DATE_MARKET_PRICE = Decimal("15")
SERVICE_PERIOD_YEARS = Decimal("4")

# (year, year-end fair value per SAR)
FAIR_VALUES = [
    (1, Decimal("2.00")),
    (2, Decimal("5.00")),
    (3, Decimal("3.00")),
    (4, Decimal("6.00")),
]

EXERCISE_STOCK_PRICE = Decimal("21")  # December 31, Year 4


# ------------------------------------------- part a: measurement schedule
schedule = []
prior_liability = Decimal("0")

for year, fv_per_sar in FAIR_VALUES:
    aggregate_compensation = money(fv_per_sar * N_SARS)
    pct_accrued = Decimal(year) / SERVICE_PERIOD_YEARS  # 25%, 50%, 75%, 100%
    cumulative_liability = money(aggregate_compensation * pct_accrued)
    annual_expense = money(cumulative_liability - prior_liability)

    schedule.append(
        {
            "year": year,
            "fair_value_per_sar": fv_per_sar,
            "aggregate_compensation": aggregate_compensation,
            "pct_accrued": pct_accrued,
            "cumulative_liability": cumulative_liability,
            "annual_expense": annual_expense,
        }
    )
    prior_liability = cumulative_liability

# ----------------------------------------------------- settlement at exercise
# Cash paid derived from the stem's own facts, not copied from its arithmetic.
intrinsic_per_sar = EXERCISE_STOCK_PRICE - GRANT_DATE_MARKET_PRICE
cash_paid = money(intrinsic_per_sar * N_SARS)

liability_before_settlement = schedule[-1]["cumulative_liability"]
settlement_difference = money(liability_before_settlement - cash_paid)

# ------------------------------------------------------------- part d: proof
total_expense = money(sum((row["annual_expense"] for row in schedule), Decimal("0")))
proof_holds = total_expense == cash_paid

# --------------------------------------------------------- required answers
answers = []
for row in schedule:
    y = row["year"]
    answers.append(
        {
            "label": "a: Year {} aggregate compensation (year-end FV x 8,000 SARs)".format(y),
            "value": out(row["aggregate_compensation"]),
        }
    )
    answers.append(
        {
            "label": "a: Year {} percent of service period accrued".format(y),
            "value": out(row["pct_accrued"] * Decimal("100")),
        }
    )
    answers.append(
        {
            "label": "a: Year {} cumulative SARs liability".format(y),
            "value": out(row["cumulative_liability"]),
        }
    )
    answers.append(
        {
            "label": "a: Year {} annual compensation expense".format(y),
            "value": out(row["annual_expense"]),
        }
    )

answers.append(
    {
        "label": "d: total compensation expense over the service period",
        "value": out(total_expense),
    }
)
answers.append({"label": "d: cash paid at settlement", "value": out(cash_paid)})

# --------------------------------------------------------- journal entries
journal_entries = []

for row in schedule:
    y = row["year"]
    expense = row["annual_expense"]
    if expense >= 0:
        lines = [
            {"account": "Compensation Expense", "debit": out(expense), "credit": 0},
            {"account": "SARs Liability", "debit": 0, "credit": out(expense)},
        ]
    else:
        # Negative expense: reverse previously recognized compensation.
        reversal = money(-expense)
        lines = [
            {"account": "SARs Liability", "debit": out(reversal), "credit": 0},
            {"account": "Compensation Expense", "debit": 0, "credit": out(reversal)},
        ]
    journal_entries.append(
        {
            "part": "b",
            "date": "December 31, Year {}".format(y),
            "description": "To record compensation expense (SARs remeasurement)",
            "lines": lines,
        }
    )

journal_entries.append(
    {
        "part": "c",
        "date": "December 31, Year 4",
        "description": "To record exercise/settlement of the SARs plan in cash",
        "lines": [
            {"account": "SARs Liability", "debit": out(cash_paid), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": out(cash_paid)},
        ],
    }
)

# -------------------------------------------------------------- self-checks
for entry in journal_entries:
    debits = sum(Decimal(str(line["debit"])) for line in entry["lines"])
    credits = sum(Decimal(str(line["credit"])) for line in entry["lines"])
    assert debits == credits, "Entry out of balance: {}".format(entry)
    assert debits > 0, "Empty entry: {}".format(entry)

assert settlement_difference == Decimal("0"), (
    "Liability before settlement does not equal cash paid; a gain/loss line "
    "would be required."
)
assert proof_holds, "Total expense does not equal cash paid."

notes = (
    "Liability-classified SARs are remeasured to fair value each period, so the "
    "annual expense is the change in the cumulative accrued liability and is "
    "negative in Year 3 (-2,000) when fair value fell from $5.00 to $3.00. At "
    "December 31, Year 4 the year-end fair value of $6.00 equals the intrinsic "
    "value ($21 - $15), so the fully accrued liability of 48,000 exactly equals "
    "the 48,000 cash paid and the settlement entry records no gain or loss. "
    "Part d is satisfied: 4,000 + 16,000 - 2,000 + 30,000 = 48,000 = cash paid."
)

result = {
    "id": "agent_115#01",
    "rounding_convention": (
        "ROUND_HALF_UP to the cent, applied per period: each year's cumulative "
        "SARs liability is rounded first and the rounded balance drives the next "
        "year's expense plug. No PV discounting applies to this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
