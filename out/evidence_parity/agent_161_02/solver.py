"""Lakeshore Packaging Group - ASC 740 deferred tax classification/presentation.

Rounding convention: all money uses decimal.Decimal, quantized to the cent with
ROUND_HALF_UP applied once per period (period-end amounts), never floats.

Everything is derived from the stated future taxable/deductible amounts and the
enacted 25% rate; nothing is hard-coded except the scenario inputs.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

def money(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

RATE = Decimal("0.25")

# (name, future taxable amount, future deductible amount)
TEMP_DIFFS = [
    ("Excess tax depreciation (MACRS > SL)", Decimal("240000"), Decimal("0")),
    ("Installment gross profit (accrual vs cash)", Decimal("80000"), Decimal("0")),
    ("Warranty accrual", Decimal("0"), Decimal("120000")),
    ("Unearned (deferred) revenue", Decimal("0"), Decimal("48000")),
]

# Derive deferred tax effects from future amounts x enacted rate
dtl_items = [(n, q(tax * RATE)) for (n, tax, ded) in TEMP_DIFFS if tax > 0]
dta_items = [(n, q(ded * RATE)) for (n, tax, ded) in TEMP_DIFFS if ded > 0]

gross_dtl = q(sum((v for _, v in dtl_items), Decimal("0")))
gross_dta = q(sum((v for _, v in dta_items), Decimal("0")))

# ---- part a ----
va_a = Decimal("15000")
dta_net_of_va_a = q(gross_dta - va_a)
net_a = q(dta_net_of_va_a - gross_dtl)          # negative => net liability
net_a_abs = q(abs(net_a))
class_a = "noncurrent net deferred tax liability" if net_a < 0 else "noncurrent net deferred tax asset"

# ---- part b ----
va_b = Decimal("36000")
dta_net_of_va_b = q(gross_dta - va_b)
net_b = q(dta_net_of_va_b - gross_dtl)
net_b_abs = q(abs(net_b))
class_b = "noncurrent net deferred tax liability" if net_b < 0 else "noncurrent net deferred tax asset"

# ---- part c: valuation allowance-only adjusting entry ----
va_begin = Decimal("10000")
va_required = va_a
va_adjust = q(va_required - va_begin)   # positive => increase allowance (debit expense)
if va_adjust > 0:
    je_c = [
        {"account": "Income Tax Expense (deferred)", "debit": money(va_adjust), "credit": 0},
        {"account": "Valuation Allowance for Deferred Tax Asset", "debit": 0, "credit": money(va_adjust)},
    ]
else:
    je_c = [
        {"account": "Valuation Allowance for Deferred Tax Asset", "debit": money(abs(va_adjust)), "credit": 0},
        {"account": "Income Tax Expense (deferred)", "debit": 0, "credit": money(abs(va_adjust))},
    ]
assert q(sum(Decimal(str(l["debit"])) for l in je_c)) == q(sum(Decimal(str(l["credit"])) for l in je_c))

answers = [
    {"label": "a: Total gross deferred tax assets (DTA)", "value": money(gross_dta)},
    {"label": "a: Total deferred tax liabilities (DTL)", "value": money(gross_dtl)},
    {"label": "a: Valuation allowance", "value": money(va_a)},
    {"label": "a: Gross DTA net of valuation allowance", "value": money(dta_net_of_va_a)},
    {"label": "a: Single noncurrent amount reported on the classified balance sheet", "value": money(net_a_abs)},
    {"label": "a: Classification of the noncurrent line", "value": class_a},
    {"label": "b: Valuation allowance (revised)", "value": money(va_b)},
    {"label": "b: Gross DTA net of revised valuation allowance", "value": money(dta_net_of_va_b)},
    {"label": "b: Single noncurrent net amount", "value": money(net_b_abs)},
    {"label": "b: Classification of the noncurrent line", "value": class_b},
    {"label": "c: Valuation allowance balance January 1, Year 4", "value": money(va_begin)},
    {"label": "c: Required valuation allowance December 31, Year 4", "value": money(va_required)},
    {"label": "c: Increase in valuation allowance recorded (adjusting entry amount)", "value": money(va_adjust)},
    {"label": "d: ASC 740 offset rule",
     "value": ("For each tax-paying component in each tax jurisdiction, all deferred tax assets "
               "(net of any valuation allowance) and all deferred tax liabilities are offset and "
               "reported as a single net amount; that net deferred tax asset or liability is "
               "classified entirely as noncurrent on the classified balance sheet. DTAs and DTLs of "
               "different components or different jurisdictions may not be offset against each other.")},
    {"label": "e: Note schedule - Gross deferred tax assets", "value": money(gross_dta)},
    {"label": "e: Note schedule - Less: valuation allowance", "value": money(va_a)},
    {"label": "e: Note schedule - Deferred tax assets, net of valuation allowance", "value": money(dta_net_of_va_a)},
    {"label": "e: Note schedule - Gross deferred tax liabilities", "value": money(gross_dtl)},
    {"label": "e: Note schedule - Net noncurrent deferred tax liability", "value": money(net_a_abs)},
]

detail = (
    "Derived DTLs: " + "; ".join(f"{n} ${v:,.0f}" for n, v in dtl_items) + ". "
    "Derived DTAs: " + "; ".join(f"{n} ${v:,.0f}" for n, v in dta_items) + ". "
    f"Part a: DTA {gross_dta:,.0f} - VA {va_a:,.0f} = {dta_net_of_va_a:,.0f}; less DTL {gross_dtl:,.0f} "
    f"= net {net_a:,.0f}, i.e. a ${net_a_abs:,.0f} noncurrent net deferred tax liability. "
    f"Part b: DTA {gross_dta:,.0f} - VA {va_b:,.0f} = {dta_net_of_va_b:,.0f}; less DTL {gross_dtl:,.0f} "
    f"= net {net_b:,.0f}, i.e. a ${net_b_abs:,.0f} noncurrent net deferred tax liability (still a liability, larger). "
    f"Part c: required {va_required:,.0f} - beginning {va_begin:,.0f} = {va_adjust:,.0f} increase, "
    "debit deferred income tax expense and credit the valuation allowance (a contra-DTA)."
)

print(json.dumps({
    "id": "agent_161#02",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent, applied once per period-end amount; no floats",
    "answers": answers,
    "journal_entries": [{"part": "c", "lines": je_c}],
    "insufficient_info": False,
    "notes": detail,
}, indent=1))
