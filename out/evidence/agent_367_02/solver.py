#!/usr/bin/env python3
"""Solver for item agent_367#02 — QuarryBend Foods Co., year ended Dec 31, Year 3.

Topic: disposal (settlement) entry for a discontinued component; intraperiod tax
allocation with a permanent difference (nondeductible fines) and an originating
taxable temporary difference; period-end income tax adjusting entry; income
statement through net income.  (ACCOUNT-343, LO 18-9.)

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal.  Floats are never used anywhere in this module.
Rounding is ROUND_HALF_UP applied per computed amount (i.e., per period /
per line item), quantized to cents ($0.01), which is the convention this course
uses.  Every input in this fact pattern is a whole dollar amount and the only
multiplications are by an exact 25% enacted rate, so each product is already
exact to the cent; the quantization is applied deliberately at each step
anyway so the discipline is visible and re-runnable, not so it changes a value.
No present-value factors are involved in this item.

DERIVATION (all figures computed below from the stem, none hard-coded)
---------------------------------------------------------------------
a. Disposal entry 10/1/Yr 3: cash proceeds received, carrying amount of the
   component's net assets removed, plug = pretax loss on disposal.
b. Pretax income from continuing operations = revenues - COGS - operating
   expenses.  The disposal loss is excluded (it is discontinued operations)
   and the $3,000 of fines stay IN book operating expenses (a permanent
   difference affects taxable income, not book income).
c. Taxable income = pretax book income from continuing operations
   + nondeductible fines (permanent difference added back)
   - originating future taxable amount (temporary difference; book > taxable)
   - disposal loss (fully deductible in Year 3).
   Income taxes payable = taxable income x enacted rate.
d. Deferred tax liability originating = future taxable amount x enacted rate.
   Intraperiod split: tax on continuing operations is computed on continuing
   pretax income adjusted only for the PERMANENT difference (temporary
   differences shift tax between current and deferred, never the total);
   tax on discontinued operations is the rate applied to the disposal loss,
   which is a benefit.  Cross-check: continuing tax + discontinued tax
   (a negative benefit) must equal total tax expense = payable + DTL change.
e. Period-end entry: debit continuing-operations income tax expense, credit the
   discontinued-operations tax benefit, credit income tax payable and the
   deferred tax liability.  Dr = Cr is asserted before output.
f. Income statement through net income using intraperiod allocation: income
   from continuing operations is shown net of ITS OWN tax; the discontinued
   loss is shown net of its own tax benefit (per Demo 18-9).
g. Narrative (see notes / part-g answer).
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def q(amount: Decimal) -> Decimal:
    """Quantize to cents using ROUND_HALF_UP (applied per computed amount)."""
    return Decimal(amount).quantize(CENTS, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem, nothing else)
# ---------------------------------------------------------------------------
REVENUES = Decimal("900000")
COGS = Decimal("400000")
OPERATING_EXPENSES = Decimal("150000")          # includes the fines below
NONDEDUCTIBLE_FINES = Decimal("3000")           # permanent difference
FUTURE_TAXABLE_AMOUNT = Decimal("36000")        # originating temporary diff
CASH_PROCEEDS = Decimal("156000")               # Oct 1, Year 3 sale
NET_ASSETS_CARRYING = Decimal("180000")         # removed at disposal
TAX_RATE = Decimal("0.25")                      # enacted, all years

# ---------------------------------------------------------------------------
# a. Disposal journal entry, October 1, Year 3 (ignore tax in this entry)
# ---------------------------------------------------------------------------
loss_on_disposal = q(NET_ASSETS_CARRYING - CASH_PROCEEDS)   # 180,000 - 156,000

entry_a = {
    "part": "a",
    "date": "Year 3, October 1",
    "description": "Sale of discontinued component (tax ignored in this entry)",
    "lines": [
        {"account": "Cash", "debit": q(CASH_PROCEEDS), "credit": Decimal("0")},
        {
            "account": "Loss on Disposal of Discontinued Component",
            "debit": loss_on_disposal,
            "credit": Decimal("0"),
        },
        {
            "account": "Net Assets of Discontinued Component",
            "debit": Decimal("0"),
            "credit": q(NET_ASSETS_CARRYING),
        },
    ],
}

# ---------------------------------------------------------------------------
# b. Pretax income from continuing operations
# ---------------------------------------------------------------------------
gross_profit = q(REVENUES - COGS)
pretax_continuing = q(gross_profit - OPERATING_EXPENSES)

# ---------------------------------------------------------------------------
# c. Taxable income and income taxes payable
# ---------------------------------------------------------------------------
taxable_income = q(
    pretax_continuing
    + NONDEDUCTIBLE_FINES        # permanent difference: add back, never deducted
    - FUTURE_TAXABLE_AMOUNT      # originating taxable temporary difference
    - loss_on_disposal           # disposal loss fully deductible in Year 3
)
income_taxes_payable = q(taxable_income * TAX_RATE)

# ---------------------------------------------------------------------------
# d. Deferred tax liability and the intraperiod split
# ---------------------------------------------------------------------------
deferred_tax_liability = q(FUTURE_TAXABLE_AMOUNT * TAX_RATE)

# Continuing operations bears tax on its book income adjusted only for the
# permanent difference.  The temporary difference moves tax between current and
# deferred; it does not change how much tax continuing operations reports.
tax_expense_continuing = q((pretax_continuing + NONDEDUCTIBLE_FINES) * TAX_RATE)

# Discontinued operations: the deductible disposal loss produces a benefit.
tax_benefit_discontinued = q(loss_on_disposal * TAX_RATE)

# Cross-check (not reported): total expense = current + deferred, and the two
# intraperiod pieces must reconcile to it.
total_tax_expense = q(income_taxes_payable + deferred_tax_liability)
assert q(tax_expense_continuing - tax_benefit_discontinued) == total_tax_expense, (
    tax_expense_continuing,
    tax_benefit_discontinued,
    total_tax_expense,
)

# ---------------------------------------------------------------------------
# e. December 31, Year 3 period-end adjusting entry for income taxes
# ---------------------------------------------------------------------------
entry_e = {
    "part": "e",
    "date": "Year 3, December 31",
    "description": "Record income taxes with intraperiod allocation",
    "lines": [
        {
            "account": "Income Tax Expense (Continuing Operations)",
            "debit": tax_expense_continuing,
            "credit": Decimal("0"),
        },
        {
            "account": "Income Tax Benefit (Discontinued Operations)",
            "debit": Decimal("0"),
            "credit": tax_benefit_discontinued,
        },
        {
            "account": "Deferred Tax Liability",
            "debit": Decimal("0"),
            "credit": deferred_tax_liability,
        },
        {
            "account": "Income Tax Payable",
            "debit": Decimal("0"),
            "credit": income_taxes_payable,
        },
    ],
}

# ---------------------------------------------------------------------------
# f. Income statement through net income (intraperiod tax allocation)
# ---------------------------------------------------------------------------
income_from_continuing = q(pretax_continuing - tax_expense_continuing)
disc_ops_net_of_tax = q(-(loss_on_disposal - tax_benefit_discontinued))  # negative
net_income = q(income_from_continuing + disc_ops_net_of_tax)

# ---------------------------------------------------------------------------
# Proofs: every entry must balance before anything is printed.
# ---------------------------------------------------------------------------
for entry in (entry_a, entry_e):
    debits = sum((line["debit"] for line in entry["lines"]), Decimal("0"))
    credits = sum((line["credit"] for line in entry["lines"]), Decimal("0"))
    assert q(debits) == q(credits), (entry["part"], debits, credits)


def plain(value: Decimal):
    """Emit a JSON number: int when the amount is whole dollars."""
    value = q(value)
    return int(value) if value == value.to_integral_value() else float(value)


def render_entry(entry: dict) -> dict:
    return {
        "part": entry["part"],
        "date": entry["date"],
        "description": entry["description"],
        "lines": [
            {
                "account": line["account"],
                "debit": plain(line["debit"]),
                "credit": plain(line["credit"]),
            }
            for line in entry["lines"]
        ],
    }


answers = [
    {"label": "b: pretax income from continuing operations", "value": plain(pretax_continuing)},
    {"label": "c: taxable income", "value": plain(taxable_income)},
    {"label": "c: income taxes payable", "value": plain(income_taxes_payable)},
    {"label": "d: deferred tax liability originating in Year 3", "value": plain(deferred_tax_liability)},
    {"label": "d: intraperiod tax expense allocated to continuing operations", "value": plain(tax_expense_continuing)},
    {"label": "d: intraperiod tax benefit allocated to discontinued operations", "value": plain(tax_benefit_discontinued)},
    {"label": "f: income from continuing operations", "value": plain(income_from_continuing)},
    {"label": "f: loss from discontinued operations, net of tax", "value": plain(disc_ops_net_of_tax)},
    {"label": "f: net income", "value": plain(net_income)},
]

part_g = (
    "g: The tax effect of the disposal loss is not reported in the continuing-operations "
    "income tax expense line. Under intraperiod tax allocation the $24,000 pretax loss on "
    "disposal is presented in the discontinued operations section net of its own $6,000 tax "
    "benefit, i.e., a single $18,000 net-of-tax loss below income from continuing operations. "
    "Continuing operations therefore reports tax computed on its own pretax income adjusted "
    "for the nondeductible fines, and the deferred tax liability from the originating "
    "temporary difference does not change the total tax expense, only its current/deferred split."
)

output = {
    "id": "agent_367#02",
    "rounding_convention": (
        "decimal.Decimal only, never floats; ROUND_HALF_UP quantized to cents "
        "applied per computed amount (per period / per line item); no PV factors "
        "in this item; all inputs are whole dollars at a 25% enacted rate so every "
        "result is exact to the cent"
    ),
    "answers": answers,
    "journal_entries": [render_entry(entry_a), render_entry(entry_e)],
    "insufficient_info": False,
    "notes": part_g,
}

print(json.dumps(output, indent=2))
