"""Harborline Ceramics LLC - NOL carryforward (Y1 recognition, Y2 utilization + VA).

Rounding convention: all money is decimal.Decimal; every computed amount is
quantized to whole dollars using ROUND_HALF_UP per period (each period's tax
figures are rounded independently before being carried forward). Nothing is
hard-coded: every figure below is derived from the four scenario inputs
(loss, rate, 80% limit, Y2 taxable income, 75% realizable fraction).
"""
import json
from decimal import Decimal, ROUND_HALF_UP

D = Decimal
CENT = D("1")          # whole dollars


def r(x):
    return (D(x)).quantize(CENT, rounding=ROUND_HALF_UP)


# ---- scenario inputs -------------------------------------------------------
op_loss_y1 = r("-120000")          # Y1 tax operating loss (pretax = taxable)
rate = D("0.25")                   # enacted, all years
limit_pct = D("0.80")              # 80% utilization limit
ti_y2_before_nol = r("30000")      # Y2 taxable income before NOL deduction
realizable_pct = D("0.75")         # MLTN fraction realizable at 12/31/Y2
va_begin = r("0")

# ---- (a) DTA at 12/31/Y1 ---------------------------------------------------
nol_cf_y1 = -op_loss_y1                      # 120,000 carryforward
dta_y1 = r(nol_cf_y1 * rate)                 # 30,000
va_y1 = va_begin                             # MLTN full realization -> no VA
net_dta_y1 = r(dta_y1 - va_y1)

# ---- (b) Year 1 partial income statement -----------------------------------
tax_benefit_y1 = dta_y1                      # deferred benefit only
net_loss_y1 = r(op_loss_y1 + tax_benefit_y1)

# ---- (c) Year 2 utilization -------------------------------------------------
max_nol_deduct = r(ti_y2_before_nol * limit_pct)          # 80% cap
nol_used_y2 = min(nol_cf_y1, max_nol_deduct)              # 24,000
ti_y2_after_nol = r(ti_y2_before_nol - nol_used_y2)       # 6,000
tax_payable_y2 = r(ti_y2_after_nol * rate)                # 1,500
dta_used_y2 = r(nol_used_y2 * rate)                       # 6,000 deferred exp
tax_expense_y2_before_va = r(tax_payable_y2 + dta_used_y2)

# ---- (d) Year-2 valuation allowance ----------------------------------------
nol_cf_end_y2 = r(nol_cf_y1 - nol_used_y2)                # 96,000
dta_end_y2_gross = r(nol_cf_end_y2 * rate)                # 24,000
assert dta_end_y2_gross == r(dta_y1 - dta_used_y2)        # roll-forward ties
va_required_y2 = r(dta_end_y2_gross * (D(1) - realizable_pct))
va_adjustment = r(va_required_y2 - va_begin)
net_dta_y2 = r(dta_end_y2_gross - va_required_y2)
total_tax_expense_y2 = r(tax_expense_y2_before_va + va_adjustment)


def f(x):
    return int(x)


def je(part, lines):
    dr = sum(D(str(l[1])) for l in lines)
    cr = sum(D(str(l[2])) for l in lines)
    assert dr == cr, (part, dr, cr)
    return {"part": part,
            "lines": [{"account": a, "debit": f(d), "credit": f(c)}
                      for a, d, c in lines]}


Z = D("0")
entries = [
    je("a", [("Deferred Tax Asset - NOL carryforward", dta_y1, Z),
             ("Income Tax Benefit (deferred)", Z, dta_y1)]),
    je("c", [("Income Tax Expense", tax_expense_y2_before_va, Z),
             ("Deferred Tax Asset - NOL carryforward", Z, dta_used_y2),
             ("Income Tax Payable", Z, tax_payable_y2)]),
    je("d", [("Income Tax Expense (valuation allowance)", va_adjustment, Z),
             ("Valuation Allowance - Deferred Tax Asset", Z, va_adjustment)]),
]

answers = [
    {"label": "a: NOL carryforward at 12/31/Y1", "value": f(nol_cf_y1)},
    {"label": "a: DTA at 12/31/Y1 (120,000 x 25%)", "value": f(dta_y1)},
    {"label": "a: Valuation allowance at 12/31/Y1 (MLTN full realization)",
     "value": f(va_y1)},
    {"label": "a: Net DTA reported at 12/31/Y1", "value": f(net_dta_y1)},
    {"label": "b: Year 1 operating loss (pretax)", "value": f(op_loss_y1)},
    {"label": "b: Year 1 income tax benefit", "value": f(tax_benefit_y1)},
    {"label": "b: Year 1 net loss", "value": f(net_loss_y1)},
    {"label": "c: Year 2 taxable income before NOL deduction",
     "value": f(ti_y2_before_nol)},
    {"label": "c: Maximum NOL deduction (80% x 30,000)",
     "value": f(max_nol_deduct)},
    {"label": "c: NOL carryforward utilized in Year 2", "value": f(nol_used_y2)},
    {"label": "c: Year 2 taxable income after NOL deduction",
     "value": f(ti_y2_after_nol)},
    {"label": "c: Income tax payable Year 2 (6,000 x 25%)",
     "value": f(tax_payable_y2)},
    {"label": "c: DTA reduction (deferred tax expense) Year 2",
     "value": f(dta_used_y2)},
    {"label": "c: Total income tax expense Year 2 before VA",
     "value": f(tax_expense_y2_before_va)},
    {"label": "d: NOL carryforward remaining at 12/31/Y2",
     "value": f(nol_cf_end_y2)},
    {"label": "d: Gross DTA at 12/31/Y2 after utilization",
     "value": f(dta_end_y2_gross)},
    {"label": "d: Valuation allowance required at 12/31/Y2 (25% of 24,000)",
     "value": f(va_required_y2)},
    {"label": "d: Valuation allowance JE amount (from $0 beginning balance)",
     "value": f(va_adjustment)},
    {"label": "d: Net DTA reported at 12/31/Y2", "value": f(net_dta_y2)},
    {"label": "d: Total income tax expense Year 2 including VA charge",
     "value": f(total_tax_expense_y2)},
]

out = {
    "id": "agent_032#01",
    "rounding_convention": ("decimal.Decimal throughout; ROUND_HALF_UP to whole "
                            "dollars applied per period (no cents arise; all "
                            "amounts are exact multiples of $1). Journal entries "
                            "are stated in whole dollars and the DTA roll-forward "
                            "closes exactly: 30,000 - 6,000 utilized = 24,000 "
                            "gross, less 6,000 VA = 18,000 net."),
    "answers": answers,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": ("Year 1: loss 120,000 x 25% = 30,000 DTA, no VA because full "
              "realization is MLTN; deferred benefit 30,000 drives net loss to "
              "90,000. Year 2: the 80% limit caps the NOL deduction at 24,000 "
              "(80% of 30,000), leaving 6,000 taxable -> 1,500 currently "
              "payable; the 24,000 of NOL used releases 6,000 of DTA as deferred "
              "tax expense, so tax expense before VA is 7,500 (= 30,000 book/tax "
              "income x 25% since there are no other differences). Remaining NOL "
              "96,000 x 25% = 24,000 gross DTA; only 75% MLTN realizable, so a "
              "6,000 valuation allowance is recorded against income tax expense "
              "(VA began at 0), leaving a net DTA of 18,000 and total Year 2 tax "
              "expense of 13,500.")
}
print(json.dumps(out, indent=1))
