#!/usr/bin/env python3
"""Blind solver for item agent_360#00 (Ironwood Consumer Products).

Topic: LO 15-5 — loss contingencies (litigation) with a recognized (Type 1)
subsequent event, plus a two-year assurance-type warranty accrued as a
period-end adjusting entry.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Every monetary result is quantized to the cent
with ROUND_HALF_UP, applied per computed amount (i.e. per period / per line),
never at the end of a chain of unrounded values. No floats are used anywhere.
No present-value discounting is involved in this item: the litigation
settlement is payable within a few months of the balance sheet date and the
warranty accrual is a percentage-of-sales estimate, so all amounts are
undiscounted. (Warranty percentages of sales happen to land on exact dollars
here, but the same ROUND_HALF_UP-to-the-cent rule is applied regardless.)

DERIVATION NOTES (all inputs below are read off the stem's fact pattern only)
----------------------------------------------------------------------------
Litigation (ASC 450-20 / loss contingencies):
  * Loss is probable and the amount is reasonably estimable, so it is accrued
    at 12/31/Yr1. When a range exists and one amount within the range is a
    better estimate than any other, that better estimate is accrued -> the
    $120,000 better estimate (not the $90,000 low end, and not the $350,000
    amount sought in the complaint).
  * The 2/18/Yr2 settlement occurs after the balance sheet date but before the
    3/10/Yr2 issuance date, and it resolves an uncertainty about a condition
    that already existed at 12/31/Yr1 (the October Yr1 accident). It is
    therefore a RECOGNIZED (Type 1) subsequent event: the Yr1 balance sheet
    liability is remeasured to the $145,000 settlement amount by an additional
    adjusting entry dated 12/31/Yr1 for the incremental $25,000.
  * The 5/1/Yr2 cash payment extinguishes the recorded liability; because the
    liability was already remeasured to $145,000, no additional loss arises.

Warranty (assurance-type, not sold separately -> expense/accrual model, no
revenue deferral):
  * Accrual each 12/31 = warranty rate x that year's product sales.
  * Claims paid in cash during the year reduce the liability (they are not
    expensed again).
  * Ending liability = beginning + accrual - claims, carried forward.
  * Product sales are cash sales; COGS is ignored per the stem.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(value) -> Decimal:
    """Quantize to the cent using ROUND_HALF_UP (applied per amount)."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def out(amount: Decimal):
    """Render a Decimal for JSON: int when whole, else float-free string-safe."""
    amount = money(amount)
    if amount == amount.to_integral_value():
        return int(amount)
    return str(amount)


# ---------------------------------------------------------------------------
# Stem facts
# ---------------------------------------------------------------------------
AMOUNT_SOUGHT = money("350000")          # complaint amount - not the accrual
RANGE_LOW = money("90000")
RANGE_HIGH = money("280000")
BETTER_ESTIMATE = money("120000")        # counsel's better estimate in range
SETTLEMENT = money("145000")             # agreed 2/18/Yr2, paid 5/1/Yr2

WARRANTY_RATE = Decimal("0.020")         # 2.0% of that year's product sales
SALES = {1: money("3200000"), 2: money("3600000"), 3: money("4000000")}
CLAIMS = {1: money("18000"), 2: money("52000"), 3: money("61000")}

# ---------------------------------------------------------------------------
# (a) 12/31/Yr1 adjusting entry - accrue the better estimate
# ---------------------------------------------------------------------------
assert RANGE_LOW <= BETTER_ESTIMATE <= RANGE_HIGH, "better estimate must lie in range"
accrual_a = BETTER_ESTIMATE

# ---------------------------------------------------------------------------
# (b) Recognized subsequent event - remeasure 12/31/Yr1 liability to settlement
# ---------------------------------------------------------------------------
incremental_b = money(SETTLEMENT - accrual_a)
liability_after_b = money(accrual_a + incremental_b)
assert liability_after_b == SETTLEMENT

# ---------------------------------------------------------------------------
# (c) 5/1/Yr2 settlement payment
# ---------------------------------------------------------------------------
cash_paid_c = SETTLEMENT

# ---------------------------------------------------------------------------
# (d)-(f) Warranty accruals, claims, and the liability roll-forward
# ---------------------------------------------------------------------------
schedule = []
beginning = money("0")
for year in (1, 2, 3):
    accrual = money(SALES[year] * WARRANTY_RATE)
    claims = CLAIMS[year]
    ending = money(beginning + accrual - claims)
    schedule.append(
        {
            "year": year,
            "beginning": beginning,
            "accrual": accrual,
            "claims": claims,
            "ending": ending,
        }
    )
    beginning = ending

yr1 = schedule[0]
yr2 = schedule[1]
yr3 = schedule[2]

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=None, credit=None):
    return {
        "account": account,
        "debit": out(debit) if debit is not None else 0,
        "credit": out(credit) if credit is not None else 0,
    }


journal_entries = [
    {
        "part": "a",
        "date": "December 31, Year 1",
        "description": "Accrue probable and estimable litigation loss at counsel's better estimate within the range (ignoring the February settlement).",
        "lines": [
            line("Loss from Litigation", debit=accrual_a),
            line("Litigation Liability", credit=accrual_a),
        ],
    },
    {
        "part": "b",
        "date": "December 31, Year 1",
        "description": "Recognized (Type 1) subsequent event: remeasure the Year 1 litigation liability from the $120,000 better estimate up to the $145,000 February 18, Year 2 settlement amount.",
        "lines": [
            line("Loss from Litigation", debit=incremental_b),
            line("Litigation Liability", credit=incremental_b),
        ],
    },
    {
        "part": "c",
        "date": "May 1, Year 2",
        "description": "Pay the litigation settlement in cash; liability already carried at the settlement amount, so no additional loss.",
        "lines": [
            line("Litigation Liability", debit=cash_paid_c),
            line("Cash", credit=cash_paid_c),
        ],
    },
    {
        "part": "d",
        "date": "Year 1",
        "description": "Record Year 1 cash product sales (COGS ignored per the stem).",
        "lines": [
            line("Cash", debit=SALES[1]),
            line("Sales Revenue", credit=SALES[1]),
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 1",
        "description": "Period-end adjusting entry: accrue estimated warranty cost at 2.0% of Year 1 product sales.",
        "lines": [
            line("Warranty Expense", debit=yr1["accrual"]),
            line("Warranty Liability", credit=yr1["accrual"]),
        ],
    },
    {
        "part": "d",
        "date": "Year 1",
        "description": "Settle actual Year 1 warranty claims in cash against the accrued liability.",
        "lines": [
            line("Warranty Liability", debit=yr1["claims"]),
            line("Cash", credit=yr1["claims"]),
        ],
    },
    {
        "part": "f",
        "date": "December 31, Year 2",
        "description": "Period-end adjusting entry: accrue estimated warranty cost at 2.0% of Year 2 product sales.",
        "lines": [
            line("Warranty Expense", debit=yr2["accrual"]),
            line("Warranty Liability", credit=yr2["accrual"]),
        ],
    },
]

# Debits must equal credits in every entry.
for entry in journal_entries:
    debits = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    credits = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert debits == credits, f"entry {entry['part']} out of balance: {debits} vs {credits}"

# ---------------------------------------------------------------------------
# Answers (only figures the Required parts ask for)
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: Dec 31, Year 1 litigation loss accrued (better estimate)", "value": out(accrual_a)},
    {"label": "b: Dec 31, Year 1 incremental litigation loss from recognized subsequent event", "value": out(incremental_b)},
    {"label": "b: Dec 31, Year 1 litigation liability after remeasurement", "value": out(liability_after_b)},
    {"label": "c: May 1, Year 2 cash paid to settle litigation", "value": out(cash_paid_c)},
    {"label": "d: Year 1 product sales recorded", "value": out(SALES[1])},
    {"label": "d: Dec 31, Year 1 warranty accrual (2.0% of Year 1 sales)", "value": out(yr1["accrual"])},
    {"label": "d: Year 1 warranty claims paid", "value": out(yr1["claims"])},
    {"label": "e: Year 1 warranty liability - beginning", "value": out(yr1["beginning"])},
    {"label": "e: Year 1 warranty liability - accrual", "value": out(yr1["accrual"])},
    {"label": "e: Year 1 warranty liability - claims", "value": out(yr1["claims"])},
    {"label": "e: Year 1 warranty liability - ending", "value": out(yr1["ending"])},
    {"label": "e: Year 2 warranty liability - beginning", "value": out(yr2["beginning"])},
    {"label": "e: Year 2 warranty liability - accrual", "value": out(yr2["accrual"])},
    {"label": "e: Year 2 warranty liability - claims", "value": out(yr2["claims"])},
    {"label": "e: Year 2 warranty liability - ending", "value": out(yr2["ending"])},
    {"label": "e: Year 3 warranty liability - beginning", "value": out(yr3["beginning"])},
    {"label": "e: Year 3 warranty liability - accrual", "value": out(yr3["accrual"])},
    {"label": "e: Year 3 warranty liability - claims", "value": out(yr3["claims"])},
    {"label": "e: Year 3 warranty liability - ending", "value": out(yr3["ending"])},
    {"label": "f: Dec 31, Year 2 warranty accrual (2.0% of Year 2 sales)", "value": out(yr2["accrual"])},
    {
        "label": "g: reporting if the litigation loss were only reasonably possible",
        "value": "No liability or loss would be accrued at December 31, Year 1; the contingency would instead be disclosed in the notes, describing the nature of the lawsuit and the estimated $120,000 possible loss (or range).",
    },
]

result = {
    "id": "agent_360#00",
    "rounding_convention": "decimal.Decimal only, no floats; ROUND_HALF_UP to the cent applied per computed amount (per period / per line), not at the end of a chain; no discounting (all amounts undiscounted)",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Litigation: probable + estimable with a better estimate inside the range, so ASC 450-20 accrues the $120,000 "
        "better estimate rather than the $90,000 low end or the $350,000 amount sought. The February 18, Year 2 settlement "
        "is a recognized (Type 1) subsequent event because the causing condition (the October Year 1 accident) existed at "
        "the balance sheet date and the agreement predates the March 10, Year 2 issuance date, so Year 1 is remeasured to "
        "$145,000 via an additional $25,000 adjusting entry dated December 31, Year 1. "
        "Warranty is assurance-type and not sold separately, so the expense/accrual model applies (no revenue deferral); "
        "the two-year coverage affects only how long the single liability account is drawn down, not the accrual amount, "
        "which is 2.0% of each year's own sales. Claims paid reduce the liability and are not re-expensed."
    ),
}

print(json.dumps(result, indent=2))
