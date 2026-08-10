#!/usr/bin/env python3
"""Blind solver — Q3 CORE alternate angle, Northpine Logistics Group (LO 18-4).

Fact pattern (from stem.md only):
  Enacted rate 21%, calendar year, no valuation allowance.
  1/1  DTL 5,040 credit, entirely from prepaid rent 24,000 (tax-deducted last
       year, GAAP-expensed this year).  DTA 0.
  Pretax GAAP income 360,000 (already includes every item below).
    1. Warranty expense accrued 35,000, not deductible until paid (none paid).
    2. Tax depreciation exceeds book depreciation by 40,000.
    3. Municipal bond interest 5,000 — nontaxable permanent.
    4. Officer life insurance premiums 8,000 — nondeductible permanent.
    5. Prepaid rent 24,000 reverses fully (book expense now, tax deduction taken
       last year) — settlement of the beginning taxable temporary difference.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal — no binary floats anywhere.
Money is quantized to cents (0.01) with ROUND_HALF_UP, applied per computed
figure (round-per-period, not round-at-end): every tax effect (base x 21%) is
rounded to cents at the moment it is computed, and the rounded amounts are the
ones that roll forward into the journal entry and the balance sheet.  With this
fact pattern every product is exact to the cent, so the convention is not
load-bearing, but it is applied deliberately.
Rate-reconciliation percentages are quantized to 0.01 percentage point with
ROUND_HALF_UP; the effective-rate line is computed from total tax expense over
pretax income directly (not by summing the rounded component percentages), and
the components are shown as-rounded.
No present-value factors are involved in this item.

Sign conventions in the output: taxable-income adjustments are signed relative
to pretax GAAP income (positive = increases taxable income).  Rate-reconciliation
dollars are signed relative to the statutory-amount line.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")
PCT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP (applied per figure as computed)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def pct(x: Decimal) -> Decimal:
    """Quantize a percentage to 0.01 percentage point, ROUND_HALF_UP."""
    return Decimal(x).quantize(PCT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly: int when the cents are zero, else float of the exact cents."""
    d = Decimal(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------- given facts
RATE = Decimal("0.21")

PRETAX_GAAP = Decimal("360000")

BEG_DTL = Decimal("5040")          # given
BEG_DTA = Decimal("0")             # given

PREPAID_RENT_REVERSAL = Decimal("24000")   # beginning taxable TD settling
WARRANTY_ACCRUAL = Decimal("35000")        # new deductible TD originating
EXCESS_TAX_DEPR = Decimal("40000")         # new taxable TD originating
MUNI_INTEREST = Decimal("5000")            # nontaxable permanent
OFFICER_LIFE_INS = Decimal("8000")         # nondeductible permanent

# Internal consistency check on the given beginning balance (not reported).
assert money(PREPAID_RENT_REVERSAL * RATE) == money(BEG_DTL)

# ------------------------------------------------- (a) taxable income & payable
# Start at pretax GAAP income and adjust.
#   + warranty accrued but not yet deductible          (deductible TD originates)
#   - excess tax depreciation over book                (taxable TD originates)
#   - municipal bond interest (in book income, never taxed)
#   + officer life insurance premiums (in book expense, never deductible)
#   + prepaid rent expensed for book this year, already deducted for tax last
#     year (settlement of the beginning taxable TD)
adj_warranty = WARRANTY_ACCRUAL
adj_depreciation = -EXCESS_TAX_DEPR
adj_muni = -MUNI_INTEREST
adj_life_ins = OFFICER_LIFE_INS
adj_prepaid_reversal = PREPAID_RENT_REVERSAL

taxable_income = money(
    PRETAX_GAAP
    + adj_warranty
    + adj_depreciation
    + adj_muni
    + adj_life_ins
    + adj_prepaid_reversal
)
tax_payable = money(taxable_income * RATE)

# ------------------------------------------ (b) ending DTL / DTA + rollforward
# DTL roll-forward
dtl_settlement = money(PREPAID_RENT_REVERSAL * RATE)   # prepaid rent TD reverses
dtl_origination = money(EXCESS_TAX_DEPR * RATE)        # excess tax depreciation
end_dtl = money(BEG_DTL - dtl_settlement + dtl_origination)

# DTA
dta_origination = money(WARRANTY_ACCRUAL * RATE)       # warranty TD originates
end_dta = money(BEG_DTA + dta_origination)

delta_dtl = money(end_dtl - BEG_DTL)   # credit if positive
delta_dta = money(end_dta - BEG_DTA)   # debit if positive

# ---------------------------------------------------- (c) period-end adjusting JE
current_expense = tax_payable
deferred_expense = money(delta_dtl - delta_dta)   # negative = deferred benefit
total_tax_expense = money(current_expense + deferred_expense)

je_lines = [
    {"account": "Income Tax Expense", "debit": num(total_tax_expense), "credit": 0},
    {"account": "Deferred Tax Asset", "debit": num(delta_dta), "credit": 0},
    {"account": "Income Tax Payable", "debit": 0, "credit": num(tax_payable)},
    {"account": "Deferred Tax Liability", "debit": 0, "credit": num(delta_dtl)},
]
debits = sum(Decimal(str(l["debit"])) for l in je_lines)
credits = sum(Decimal(str(l["credit"])) for l in je_lines)
assert money(debits) == money(credits), (debits, credits)

# ----------------------------------------------------- (d) rate reconciliation
statutory_amount = money(PRETAX_GAAP * RATE)
recon_life_ins = money(OFFICER_LIFE_INS * RATE)     # increases expense
recon_muni = money(-MUNI_INTEREST * RATE)           # decreases expense
recon_total = money(statutory_amount + recon_life_ins + recon_muni)
assert recon_total == total_tax_expense, (recon_total, total_tax_expense)

statutory_pct = pct(RATE * Decimal("100"))
life_ins_pct = pct(recon_life_ins / PRETAX_GAAP * Decimal("100"))
muni_pct = pct(recon_muni / PRETAX_GAAP * Decimal("100"))
effective_pct = pct(total_tax_expense / PRETAX_GAAP * Decimal("100"))

# ------------------------------------------------ (e) balance sheet presentation
# Same component/jurisdiction -> DTA and DTL are offset and reported as a single
# noncurrent net amount (ASC 740: all deferred taxes are noncurrent).
net_position = money(end_dta - end_dtl)   # negative -> net liability
net_is_liability = net_position < 0
net_amount = money(abs(net_position))

answers = [
    {"label": "a: taxable income", "value": num(taxable_income)},
    {"label": "a: income tax payable (current tax)", "value": num(tax_payable)},
    {"label": "b: ending Deferred Tax Liability balance", "value": num(end_dtl)},
    {"label": "b: ending Deferred Tax Asset balance", "value": num(end_dta)},
    {"label": "b: DTL roll-forward - beginning balance", "value": num(BEG_DTL)},
    {"label": "b: DTL roll-forward - settlement of prepaid rent difference",
     "value": num(-dtl_settlement)},
    {"label": "b: DTL roll-forward - origination from excess tax depreciation",
     "value": num(dtl_origination)},
    {"label": "b: DTL roll-forward - ending balance", "value": num(end_dtl)},
    {"label": "d: rate reconciliation - tax at 21% statutory rate ($)",
     "value": num(statutory_amount)},
    {"label": "d: rate reconciliation - tax at 21% statutory rate (%)",
     "value": num(statutory_pct)},
    {"label": "d: rate reconciliation - nondeductible officer life insurance ($)",
     "value": num(recon_life_ins)},
    {"label": "d: rate reconciliation - nondeductible officer life insurance (%)",
     "value": num(life_ins_pct)},
    {"label": "d: rate reconciliation - nontaxable municipal bond interest ($)",
     "value": num(recon_muni)},
    {"label": "d: rate reconciliation - nontaxable municipal bond interest (%)",
     "value": num(muni_pct)},
    {"label": "d: rate reconciliation - total income tax expense ($)",
     "value": num(total_tax_expense)},
    {"label": "d: effective tax rate (%)", "value": num(effective_pct)},
    {"label": "e: balance sheet - net noncurrent deferred tax liability",
     "value": num(net_amount)},
]

notes = (
    "Taxable income = 360,000 + 35,000 warranty accrual - 40,000 excess tax "
    "depreciation - 5,000 muni interest + 8,000 officer life insurance + 24,000 "
    "prepaid rent reversal = 382,000. Ending DTL 8,400 = 5,040 beginning - 5,040 "
    "settlement of the prepaid-rent difference + 8,400 origination on excess tax "
    "depreciation; ending DTA 7,350 = 35,000 warranty x 21%. Deferred portion of "
    "the December 31 entry is a net benefit of 3,990 (DTL up 3,360, DTA up 7,350), "
    "so total tax expense is 80,220 - 3,990 = 76,230. Part (e): DTA 7,350 and DTL "
    "8,400 are the same component and jurisdiction, so they are offset and shown "
    "as one noncurrent net deferred tax liability of 1,050 (all deferred taxes are "
    "noncurrent under ASC 740). Effective rate 76,230/360,000 = 21.18%."
)

out = {
    "id": "agent_291#02",
    "rounding_convention": (
        "decimal.Decimal only; money quantized to cents with ROUND_HALF_UP applied "
        "per computed figure (round-per-period, tax effects rounded as computed and "
        "carried forward); rate-reconciliation percentages quantized to 0.01 "
        "percentage point with ROUND_HALF_UP, effective rate computed from total tax "
        "expense / pretax income rather than by summing rounded components; no PV "
        "factors in this item"
    ),
    "answers": answers,
    "journal_entries": [
        {
            "part": "c",
            "description": (
                "December 31 period-end adjusting entry to record current and "
                "deferred income taxes"
            ),
            "lines": je_lines,
        }
    ],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
