#!/usr/bin/env python3
"""
Blind solver — item agent_161#02
Lakeshore Packaging Group: ASC 740 deferred tax classification, net presentation,
and the period-end valuation-allowance-only adjusting entry.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, quantized to whole cents (0.01) at every step where a monetary
amount is produced, i.e. round-per-computation rather than round-at-end. All
money is decimal.Decimal; no float ever touches a dollar amount. Tax effects are
computed as (future taxable/deductible amount) x (enacted rate 25%), each
quantized on its own before being summed, which is the round-per-period
convention this course uses. In this fact pattern every product lands on an exact
whole dollar, so the convention is not load-bearing here, but it is applied
deliberately anyway. No present-value factors are involved in this item.

DERIVATION (all figures computed, none hard-coded)
--------------------------------------------------
The stem gives four temporary differences with their future taxable/deductible
amounts and an enacted rate of 25%. The solver recomputes each deferred tax
effect from amount x rate rather than trusting the stem's stated effect column,
then asserts the two agree.

  Taxable temporary differences  -> deferred tax LIABILITIES
    Excess tax depreciation   240,000 x 25% =  60,000
    Installment gross profit   80,000 x 25% =  20,000
  Deductible temporary differences -> deferred tax ASSETS
    Warranty accrual          120,000 x 25% =  30,000
    Unearned revenue           48,000 x 25% =  12,000

Presentation (ASC 740-10-45-6): for a single tax-paying component in a single
jurisdiction, ALL deferred tax assets, ALL deferred tax liabilities, and the
related valuation allowance are offset and presented as ONE noncurrent amount.

  net = (gross DTA - valuation allowance) - gross DTL
  net > 0 -> noncurrent deferred tax ASSET, net
  net < 0 -> noncurrent deferred tax LIABILITY, net (reported at abs(net))

Part c: the valuation allowance is a contra-asset account carried at its required
ending balance. Only the CHANGE is journalized. Required ending 15,000 less
beginning 10,000 = 5,000 increase, so the allowance is credited 5,000 and Income
Tax Expense is debited 5,000. (An allowance decrease would reverse the entry.)
The gross DTA and DTL accounts are stated to be already adjusted, so they do not
appear in this entry.

Run: python3 solver.py   -> prints one JSON object to stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to whole cents, ROUND_HALF_UP. Every money value passes through here."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def out(d: Decimal):
    """Emit a Decimal as a plain JSON number: int when whole, else 2dp float-free str->float."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Given facts from the stem (inputs only -- no answers hard-coded)
# ---------------------------------------------------------------------------
ENACTED_RATE = Decimal("0.25")

# (label, future amount, kind) where kind is "taxable" -> DTL, "deductible" -> DTA
TEMP_DIFFS = [
    ("Excess tax depreciation (MACRS > SL)", Decimal("240000"), "taxable",    Decimal("60000")),
    ("Installment gross profit",             Decimal("80000"),  "taxable",    Decimal("20000")),
    ("Warranty accrual",                     Decimal("120000"), "deductible", Decimal("30000")),
    ("Unearned (deferred) revenue",          Decimal("48000"),  "deductible", Decimal("12000")),
]

VA_PART_A = money("15000")     # required allowance at 12/31 Yr 4 (part a)
VA_PART_B = money("36000")     # alternative allowance (part b)
VA_BEGINNING = money("10000")  # balance at 1/1 Yr 4 (part c)


# ---------------------------------------------------------------------------
# Step 1 -- recompute each deferred tax effect from amount x rate
# ---------------------------------------------------------------------------
gross_dta = money(0)
gross_dtl = money(0)

for label, amount, kind, stated_effect in TEMP_DIFFS:
    effect = money(amount * ENACTED_RATE)
    # Cross-check against the effect column the stem supplied.
    assert effect == money(stated_effect), (
        f"{label}: computed {effect} != stem's stated {stated_effect}"
    )
    if kind == "taxable":
        gross_dtl = money(gross_dtl + effect)
    else:
        gross_dta = money(gross_dta + effect)


# ---------------------------------------------------------------------------
# Step 2 -- offset into a single noncurrent amount (ASC 740-10-45-6)
# ---------------------------------------------------------------------------
def net_presentation(dta: Decimal, dtl: Decimal, va: Decimal):
    """Return (reported_amount, classification_string, dta_net_of_va)."""
    dta_net = money(dta - va)
    net = money(dta_net - dtl)           # positive => net asset, negative => net liability
    if net > 0:
        return net, "noncurrent deferred tax asset, net", dta_net
    elif net < 0:
        return money(-net), "noncurrent deferred tax liability, net", dta_net
    else:
        return money(0), "no net deferred tax amount reported (offset to zero)", dta_net


a_amount, a_class, a_dta_net = net_presentation(gross_dta, gross_dtl, VA_PART_A)
b_amount, b_class, b_dta_net = net_presentation(gross_dta, gross_dtl, VA_PART_B)


# ---------------------------------------------------------------------------
# Step 3 -- part c: valuation-allowance-only adjusting entry
# ---------------------------------------------------------------------------
va_change = money(VA_PART_A - VA_BEGINNING)   # + => increase allowance, - => decrease

if va_change > 0:
    c_lines = [
        {"account": "Income Tax Expense",
         "debit": out(va_change), "credit": 0},
        {"account": "Valuation Allowance for Deferred Tax Asset",
         "debit": 0, "credit": out(va_change)},
    ]
elif va_change < 0:
    dec = money(-va_change)
    c_lines = [
        {"account": "Valuation Allowance for Deferred Tax Asset",
         "debit": out(dec), "credit": 0},
        {"account": "Income Tax Expense",
         "debit": 0, "credit": out(dec)},
    ]
else:
    c_lines = []

# Debits must equal credits.
tot_dr = sum(Decimal(str(l["debit"])) for l in c_lines)
tot_cr = sum(Decimal(str(l["credit"])) for l in c_lines)
assert money(tot_dr) == money(tot_cr), "part c entry does not balance"


# ---------------------------------------------------------------------------
# Step 4 -- assemble output (only figures the Required parts ask for)
# ---------------------------------------------------------------------------
answers = [
    # a. gross DTA, total DTL, valuation allowance, single noncurrent amount + classification
    {"label": "a: total gross deferred tax assets (DTA)", "value": out(gross_dta)},
    {"label": "a: total deferred tax liabilities (DTL)", "value": out(gross_dtl)},
    {"label": "a: valuation allowance", "value": out(VA_PART_A)},
    {"label": "a: single noncurrent amount reported on the classified balance sheet",
     "value": out(a_amount)},
    {"label": "a: classification of the single noncurrent amount", "value": a_class},

    # b. recomputed net amount and classification with a $36,000 allowance
    {"label": "b: single noncurrent amount reported (valuation allowance $36,000)",
     "value": out(b_amount)},
    {"label": "b: classification of the single noncurrent amount", "value": b_class},

    # e. disclosure-sketch schedule using part a amounts
    {"label": "e: gross deferred tax assets", "value": out(gross_dta)},
    {"label": "e: less valuation allowance", "value": out(VA_PART_A)},
    {"label": "e: deferred tax assets, net of valuation allowance", "value": out(a_dta_net)},
    {"label": "e: gross deferred tax liabilities", "value": out(gross_dtl)},
    {"label": "e: net deferred tax liability (noncurrent)", "value": out(a_amount)},
]

journal_entries = [
    {
        "part": "c",
        "description": ("December 31, Year 4 - to adjust the deferred tax asset valuation "
                        "allowance from the $10,000 beginning balance to the $15,000 "
                        "required ending balance"),
        "lines": c_lines,
    }
]

notes = (
    "d (narrative, no figures): ASC 740-10-45-6 - for a particular tax-paying component "
    "within a particular tax jurisdiction, all deferred tax assets and deferred tax "
    "liabilities, together with any related valuation allowance, are offset and presented "
    "as a single NONCURRENT amount on the classified balance sheet; deferred taxes of "
    "different tax-paying components or different jurisdictions may not be offset. "
    "Lakeshore has one component in one jurisdiction, so all four temporary differences "
    "and the allowance collapse into one noncurrent line. "
    "Part c journalizes only the $5,000 change in the allowance ($15,000 required less "
    "$10,000 beginning); the gross DTA and DTL accounts are already at the stated balances."
)

result = {
    "id": "agent_161#02",
    "rounding_convention": ("ROUND_HALF_UP quantized to cents per computed amount "
                            "(round-per-period); Decimal throughout, no floats; "
                            "no PV factors in this item"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
