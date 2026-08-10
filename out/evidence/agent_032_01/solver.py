#!/usr/bin/env python3
"""Blind solver — agent_032#01 — Harborline Ceramics LLC, NOL carryforward (LO 18-7).

FACT PATTERN (from stem.md only)
    Year 1 tax operating loss ............................. $(120,000)
    Enacted tax rate, all years ...........................       25%
    Temporary differences other than the NOL ..............      none
    Carryforward only (no carryback), 80% utilization limit
    12/31/Y1: realization of FULL DTA is more likely than not (no VA)
    Year 2 actual taxable income ..........................   $30,000
    12/31/Y2 (after utilization): MLTN only 75% of remaining DTA
        will be realized; VA beginning balance $0

ROUNDING CONVENTION
    All money is decimal.Decimal. Every monetary result is quantized to
    cents (0.01) with ROUND_HALF_UP, applied per period / per computed
    figure (round-per-period, not round-only-at-the-end), matching the
    course convention. No present-value discounting appears in this item,
    so no PV table factor vs. exact formula choice arises. The fact pattern
    is composed of whole dollars and quarter/whole percentages, so every
    figure lands exactly on a whole dollar; the quantization is defensive,
    not corrective.

METHOD
    (a) The entire Year 1 loss is carried forward and measured at the
        enacted rate:  DTA(12/31/Y1) = loss x rate.  Because full
        realization is MLTN at 12/31/Y1, NO valuation allowance is
        recorded in Year 1.  The credit goes to Income Tax Expense
        (reported on the Year 1 income statement as an income tax
        benefit).
    (b) Year 1 partial income statement: operating loss before income
        taxes, the deferred income tax benefit, and the resulting net loss.
    (c) Year 2 utilization is capped by the 80% limitation:
            NOL used     = min(NOL available, 80% x taxable income)
            DTA reduction = NOL used x rate
            Taxable income NOT sheltered = taxable income - NOL used
            Income Tax Payable = unsheltered taxable income x rate
            Income Tax Expense = DTA reduction + Income Tax Payable (plug)
    (d) Remaining DTA after utilization x (1 - 75% realizable) = the
        required ending Valuation Allowance balance.  Beginning VA is $0,
        so the adjusting credit equals that ending balance.  Net DTA
        reported = remaining DTA - valuation allowance.

Run:  python3 solver.py     -> prints one JSON object on stdout
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP (applied per period / per figure)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly: emit int when the cents are zero, else float-free str->float."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- given facts
YEAR1_OPERATING_LOSS = Decimal("120000")   # magnitude of the Year 1 tax loss
TAX_RATE = Decimal("0.25")                 # enacted for all years
UTILIZATION_LIMIT = Decimal("0.80")        # 80% of taxable income
YEAR2_TAXABLE_INCOME = Decimal("30000")    # actual, before NOL deduction
PCT_REALIZABLE_Y2 = Decimal("0.75")        # MLTN only 75% of remaining DTA
VA_BEGINNING_BALANCE = Decimal("0")

# ------------------------------------------------------- (a) DTA at 12/31/Y1
# Whole loss carried forward (carryforward only, indefinite), measured at the
# enacted rate. Full realization is MLTN => no valuation allowance in Year 1.
nol_carryforward_y1_end = money(YEAR1_OPERATING_LOSS)
dta_y1_end = money(nol_carryforward_y1_end * TAX_RATE)

je_a = {
    "part": "a",
    "description": "December 31, Year 1 - to record the deferred tax asset "
                   "and income tax benefit from the NOL carryforward "
                   "(no valuation allowance; full realization is MLTN)",
    "lines": [
        {"account": "Deferred Tax Asset",
         "debit": num(dta_y1_end), "credit": 0},
        {"account": "Income Tax Expense",
         "debit": 0, "credit": num(dta_y1_end)},
    ],
}

# ----------------------------------------- (b) Year 1 partial income statement
y1_operating_loss_reported = money(-YEAR1_OPERATING_LOSS)   # shown negative
y1_income_tax_benefit = money(dta_y1_end)                   # all deferred
y1_net_loss = money(y1_operating_loss_reported + y1_income_tax_benefit)

# ------------------------------------------------- (c) Year 2 income tax entry
# 80% limitation: the carryforward may shelter at most 80% of taxable income,
# and can never exceed the carryforward actually available.
limit_based_cap = money(YEAR2_TAXABLE_INCOME * UTILIZATION_LIMIT)
nol_utilized_y2 = money(min(nol_carryforward_y1_end, limit_based_cap))

dta_reduction_y2 = money(nol_utilized_y2 * TAX_RATE)
taxable_income_not_sheltered = money(YEAR2_TAXABLE_INCOME - nol_utilized_y2)
income_tax_payable_y2 = money(taxable_income_not_sheltered * TAX_RATE)
income_tax_expense_y2 = money(dta_reduction_y2 + income_tax_payable_y2)

je_c = {
    "part": "c",
    "description": "December 31, Year 2 - to record income tax expense "
                   "(NOL utilization limited to 80% of taxable income, "
                   "plus current tax on the unsheltered 20%)",
    "lines": [
        {"account": "Income Tax Expense",
         "debit": num(income_tax_expense_y2), "credit": 0},
        {"account": "Deferred Tax Asset",
         "debit": 0, "credit": num(dta_reduction_y2)},
        {"account": "Income Tax Payable",
         "debit": 0, "credit": num(income_tax_payable_y2)},
    ],
}

# ------------------------------------------- (d) Year 2 valuation allowance JE
nol_carryforward_y2_end = money(nol_carryforward_y1_end - nol_utilized_y2)
dta_y2_end_before_va = money(dta_y1_end - dta_reduction_y2)

va_required_ending_balance = money(
    dta_y2_end_before_va * (Decimal("1") - PCT_REALIZABLE_Y2)
)
va_adjustment_y2 = money(va_required_ending_balance - VA_BEGINNING_BALANCE)
net_dta_reported_y2 = money(dta_y2_end_before_va - va_required_ending_balance)

je_d = {
    "part": "d",
    "description": "December 31, Year 2 - to establish the valuation allowance "
                   "for the 25% of the remaining deferred tax asset that is "
                   "not more likely than not to be realized",
    "lines": [
        {"account": "Income Tax Expense",
         "debit": num(va_adjustment_y2), "credit": 0},
        {"account": "Valuation Allowance for Deferred Tax Asset",
         "debit": 0, "credit": num(va_adjustment_y2)},
    ],
}

# ------------------------------------------------------------- sanity: Dr = Cr
journal_entries = [je_a, je_c, je_d]
for je in journal_entries:
    dr = sum(Decimal(str(ln["debit"])) for ln in je["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in je["lines"])
    assert dr == cr, f"part {je['part']} out of balance: Dr {dr} vs Cr {cr}"

# Internal cross-check (not reported): DTA roll-forward must tie to the
# remaining carryforward measured at the enacted rate.
assert dta_y2_end_before_va == money(nol_carryforward_y2_end * TAX_RATE)

# ----------------------------------------------------------------- the answer
result = {
    "id": "agent_032#01",
    "rounding_convention": (
        "decimal.Decimal throughout; every monetary figure quantized to cents "
        "with ROUND_HALF_UP applied per period (round-per-period, not "
        "round-at-end). No present-value discounting in this item, so no PV "
        "table-factor vs. exact-formula election applies."
    ),
    "answers": [
        {"label": "a: Deferred tax asset at 12/31/Year 1",
         "value": num(dta_y1_end)},
        {"label": "b: Year 1 operating loss before income taxes",
         "value": num(y1_operating_loss_reported)},
        {"label": "b: Year 1 income tax benefit (deferred)",
         "value": num(y1_income_tax_benefit)},
        {"label": "b: Year 1 net loss",
         "value": num(y1_net_loss)},
        {"label": "d: Net deferred tax asset reported at 12/31/Year 2",
         "value": num(net_dta_reported_y2)},
    ],
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Part (a): entire $120,000 loss carried forward (carryforward only) x "
        "25% = $30,000 DTA; no valuation allowance at 12/31/Y1 because full "
        "realization is MLTN. Part (c): the 80% limitation caps the Year 2 NOL "
        "deduction at 80% x $30,000 = $24,000, so the DTA falls by $24,000 x "
        "25% = $6,000 and the remaining 20% of taxable income ($6,000) is taxed "
        "at 25% for $1,500 payable; income tax expense is the $7,500 plug. "
        "Part (d): remaining carryforward $96,000 x 25% = $24,000 DTA, of which "
        "25% is not MLTN realizable, so a $6,000 valuation allowance is "
        "established (beginning balance $0) and the net DTA reported is "
        "$18,000. The Year 1 credit is to Income Tax Expense, which is "
        "presented on the Year 1 income statement as an income tax benefit."
    ),
}

print(json.dumps(result, indent=2))
