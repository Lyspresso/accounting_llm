"""Harborline Ceramics LLC - NOL carryforward, VA in Year 2 (LO 18-7).

Rounding convention: all money computed with decimal.Decimal, quantized to the
cent using ROUND_HALF_UP once per period/derived figure (no float arithmetic
anywhere). Every figure is derived from the scenario inputs; nothing hard-coded
beyond the stated facts.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- Given facts -----------------------------------------------------------
y1_operating_loss = Decimal("-120000")          # pretax = taxable loss
rate              = Decimal("0.25")             # enacted, all years
util_limit        = Decimal("0.80")             # 80% of taxable income
y2_taxable_income = Decimal("30000")            # before NOL deduction
mltn_realizable   = Decimal("0.75")             # 12/31/Y2 conclusion
va_begin          = Decimal("0")

# ---- (a) Year 1 ------------------------------------------------------------
nol_cf_y1  = q(-y1_operating_loss)              # 120,000 carryforward
dta_y1     = q(nol_cf_y1 * rate)                # 30,000
tax_benefit_y1 = dta_y1                         # no VA (full realization MLTN)

# ---- (b) Year 1 partial income statement ----------------------------------
net_loss_y1 = q(y1_operating_loss + tax_benefit_y1)

# ---- (c) Year 2 utilization -----------------------------------------------
nol_limit_y2   = q(y2_taxable_income * util_limit)      # 24,000 cap
nol_used_y2    = min(nol_cf_y1, nol_limit_y2)           # 24,000
ti_after_nol   = q(y2_taxable_income - nol_used_y2)     # 6,000
tax_payable_y2 = q(ti_after_nol * rate)                 # 1,500
dta_reduction  = q(nol_used_y2 * rate)                  # 6,000
tax_expense_y2_current = q(tax_payable_y2 + dta_reduction)  # 7,500

# ---- (d) Year 2 valuation allowance ---------------------------------------
nol_remaining  = q(nol_cf_y1 - nol_used_y2)             # 96,000
dta_gross_y2   = q(nol_remaining * rate)                # 24,000
va_end         = q(dta_gross_y2 * (Decimal("1") - mltn_realizable))  # 6,000
va_expense     = q(va_end - va_begin)                   # 6,000
net_dta_y2     = q(dta_gross_y2 - va_end)               # 18,000

answers = [
 {"label": "a: NOL carryforward at 12/31/Y1", "value": n(nol_cf_y1)},
 {"label": "a: Deferred tax asset at 12/31/Y1 (120,000 x 25%)", "value": n(dta_y1)},
 {"label": "a: Valuation allowance at 12/31/Y1 (full realization MLTN)", "value": n(va_begin)},
 {"label": "b: Operating loss before income taxes, Year 1", "value": n(y1_operating_loss)},
 {"label": "b: Income tax benefit, Year 1", "value": n(tax_benefit_y1)},
 {"label": "b: Net loss, Year 1", "value": n(net_loss_y1)},
 {"label": "c: Year 2 taxable income before NOL deduction", "value": n(y2_taxable_income)},
 {"label": "c: NOL deduction allowed in Year 2 (80% x 30,000)", "value": n(nol_used_y2)},
 {"label": "c: Taxable income after NOL deduction", "value": n(ti_after_nol)},
 {"label": "c: Income tax payable, Year 2 (6,000 x 25%)", "value": n(tax_payable_y2)},
 {"label": "c: DTA reduction from NOL utilization (24,000 x 25%)", "value": n(dta_reduction)},
 {"label": "c: Total income tax expense recorded in Year 2 entry (c)", "value": n(tax_expense_y2_current)},
 {"label": "d: NOL carryforward remaining at 12/31/Y2", "value": n(nol_remaining)},
 {"label": "d: Gross DTA at 12/31/Y2 before valuation allowance", "value": n(dta_gross_y2)},
 {"label": "d: Valuation allowance required at 12/31/Y2 (25% of 24,000)", "value": n(va_end)},
 {"label": "d: Increase in valuation allowance recorded (additional tax expense)", "value": n(va_expense)},
 {"label": "d: Net DTA reported at 12/31/Y2", "value": n(net_dta_y2)},
]

def je(part, lines):
    d = sum(Decimal(str(l[1])) for l in lines)
    c = sum(Decimal(str(l[2])) for l in lines)
    assert q(d) == q(c), (part, d, c)
    return {"part": part,
            "lines": [{"account": a, "debit": n(dr), "credit": n(cr)} for a, dr, cr in lines]}

journal_entries = [
 je("a", [("Deferred Tax Asset - NOL Carryforward", dta_y1, Decimal("0")),
          ("Income Tax Benefit (Deferred)", Decimal("0"), tax_benefit_y1)]),
 je("c", [("Income Tax Expense", tax_expense_y2_current, Decimal("0")),
          ("Deferred Tax Asset - NOL Carryforward", Decimal("0"), dta_reduction),
          ("Income Tax Payable", Decimal("0"), tax_payable_y2)]),
 je("d", [("Income Tax Expense (Valuation Allowance)", va_expense, Decimal("0")),
          ("Valuation Allowance - Deferred Tax Asset", Decimal("0"), va_expense)]),
]

print(json.dumps({
 "id": "agent_032#01",
 "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied once per period/derived figure; no floats",
 "answers": answers,
 "journal_entries": journal_entries,
 "insufficient_info": False,
 "notes": "Year 1: full $120,000 loss carried forward, DTA = 120,000 x 25% = 30,000, no valuation allowance since full realization is MLTN. Year 2: NOL deduction capped at 80% of the $30,000 taxable income = 24,000, leaving 6,000 taxable (payable 1,500) and reducing the DTA by 6,000, so total tax expense in entry (c) is 7,500. Remaining NOL 96,000 -> gross DTA 24,000; only 75% MLTN realizable, so a 6,000 valuation allowance is set up (expense), leaving a net DTA of 18,000 reported at 12/31/Y2.",
}, indent=1))
