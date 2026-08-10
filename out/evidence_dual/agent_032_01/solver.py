"""Harborline Ceramics LLC -- NOL carryforward: initial recognition (Y1) and
Year-2 utilization with valuation allowance.

Rounding convention: all money handled with decimal.Decimal; every computed
amount is quantized to whole cents with ROUND_HALF_UP once per period
(Year 1 close, Year 2 close). No floats anywhere. Amounts here happen to be
exact whole dollars, so no rounding differences arise; the JE debits and
credits are proved equal for every entry.

Facts (from stem, nothing hard-coded downstream):
  Year 1 tax operating loss        = $(120,000)
  Enacted rate (all years)         = 25%
  No temporary differences other than the NOL carryforward
  Carryforward only, 80% utilization limit
  12/31/Y1: full DTA is more likely than not (MLTN) -> no valuation allowance
  Year 2 actual taxable income (before NOL deduction) = $30,000
  12/31/Y2 (after utilization): MLTN that only 75% of remaining DTA realized
  Valuation allowance beginning balance = $0
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def q(x: Decimal) -> Decimal:
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def money(x: Decimal) -> float:
    d = q(x)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------- given facts ----------------
y1_operating_loss = Decimal("-120000")          # book = tax, no other temp diffs
tax_rate = Decimal("0.25")
util_limit_pct = Decimal("0.80")
y2_taxable_income_pre_nol = Decimal("30000")
mltn_realizable_pct = Decimal("0.75")
va_begin = Decimal("0")

# ---------------- (a) Year 1: initial recognition ----------------
nol_carryforward_y1 = -y1_operating_loss                    # 120,000
dta_y1_gross = q(nol_carryforward_y1 * tax_rate)            # 30,000
va_y1 = q(va_begin)                                         # 0 -- full DTA MLTN
dta_y1_net = q(dta_y1_gross - va_y1)                        # 30,000

je_a = [
    {"account": "Deferred Tax Asset", "debit": money(dta_y1_gross), "credit": 0},
    {"account": "Income Tax Benefit (Benefit Due to Loss Carryforward)",
     "debit": 0, "credit": money(dta_y1_gross)},
]

# ---------------- (b) Year 1 partial income statement ----------------
y1_tax_benefit = dta_y1_gross                               # 30,000 benefit
y1_net_loss = q(y1_operating_loss + y1_tax_benefit)         # (90,000)

# ---------------- (c) Year 2: utilization + payable ----------------
nol_deduction_cap = q(y2_taxable_income_pre_nol * util_limit_pct)   # 24,000
nol_available = q(nol_carryforward_y1)                              # 120,000
nol_used_y2 = min(nol_deduction_cap, nol_available)                 # 24,000
y2_taxable_income_after_nol = q(y2_taxable_income_pre_nol - nol_used_y2)  # 6,000
y2_taxes_payable = q(y2_taxable_income_after_nol * tax_rate)        # 1,500
dta_reduction_y2 = q(nol_used_y2 * tax_rate)                        # 6,000
y2_current_plus_deferred_expense = q(y2_taxes_payable + dta_reduction_y2)  # 7,500

nol_remaining = q(nol_available - nol_used_y2)                      # 96,000
dta_gross_after_util = q(dta_y1_gross - dta_reduction_y2)           # 24,000
# cross-check gross DTA against remaining NOL x rate
assert dta_gross_after_util == q(nol_remaining * tax_rate)
# cross-check total expense against pretax book income x rate (no other diffs)
assert y2_current_plus_deferred_expense == q(y2_taxable_income_pre_nol * tax_rate)

je_c = [
    {"account": "Income Tax Expense", "debit": money(y2_current_plus_deferred_expense), "credit": 0},
    {"account": "Income Taxes Payable", "debit": 0, "credit": money(y2_taxes_payable)},
    {"account": "Deferred Tax Asset", "debit": 0, "credit": money(dta_reduction_y2)},
]

# ---------------- (d) Year 2: valuation allowance ----------------
unrealizable_pct = Decimal("1") - mltn_realizable_pct              # 25%
va_required_end_y2 = q(dta_gross_after_util * unrealizable_pct)    # 6,000
va_adjustment = q(va_required_end_y2 - va_begin)                   # 6,000 increase
dta_net_reported_y2 = q(dta_gross_after_util - va_required_end_y2) # 18,000
assert dta_net_reported_y2 == q(dta_gross_after_util * mltn_realizable_pct)

je_d = [
    {"account": "Income Tax Expense", "debit": money(va_adjustment), "credit": 0},
    {"account": "Allowance to Reduce Deferred Tax Asset to Expected Realizable Value",
     "debit": 0, "credit": money(va_adjustment)},
]

y2_total_income_tax_expense = q(y2_current_plus_deferred_expense + va_adjustment)  # 13,500
y2_net_income = q(y2_taxable_income_pre_nol - y2_total_income_tax_expense)          # 16,500

# ---------------- prove Dr = Cr on every entry ----------------
for part, lines in (("a", je_a), ("c", je_c), ("d", je_d)):
    dr = sum(Decimal(str(l["debit"])) for l in lines)
    cr = sum(Decimal(str(l["credit"])) for l in lines)
    assert dr == cr, (part, dr, cr)

answers = [
    {"label": "a: Year 1 NOL carryforward (tax loss available)", "value": money(nol_carryforward_y1)},
    {"label": "a: Enacted tax rate applied", "value": float(tax_rate)},
    {"label": "a: Gross DTA at 12/31/Y1 (120,000 x 25%)", "value": money(dta_y1_gross)},
    {"label": "a: Valuation allowance at 12/31/Y1 (full DTA is MLTN)", "value": money(va_y1)},
    {"label": "a: Net DTA reported at 12/31/Y1", "value": money(dta_y1_net)},

    {"label": "b: Year 1 operating loss (pretax)", "value": money(y1_operating_loss)},
    {"label": "b: Year 1 income tax benefit", "value": money(y1_tax_benefit)},
    {"label": "b: Year 1 net loss", "value": money(y1_net_loss)},

    {"label": "c: Year 2 taxable income before NOL deduction", "value": money(y2_taxable_income_pre_nol)},
    {"label": "c: 80% utilization limit on Year 2 income (30,000 x 80%)", "value": money(nol_deduction_cap)},
    {"label": "c: NOL carryforward used in Year 2", "value": money(nol_used_y2)},
    {"label": "c: Year 2 taxable income after NOL deduction", "value": money(y2_taxable_income_after_nol)},
    {"label": "c: Year 2 income taxes payable (6,000 x 25%)", "value": money(y2_taxes_payable)},
    {"label": "c: DTA reduction on utilization (24,000 x 25%)", "value": money(dta_reduction_y2)},
    {"label": "c: Year 2 income tax expense recorded in entry (c)", "value": money(y2_current_plus_deferred_expense)},
    {"label": "c: NOL carryforward remaining after Year 2", "value": money(nol_remaining)},
    {"label": "c: Gross DTA balance after utilization (96,000 x 25%)", "value": money(dta_gross_after_util)},

    {"label": "d: Portion of remaining DTA not MLTN of realization (25%)", "value": float(unrealizable_pct)},
    {"label": "d: Valuation allowance required at 12/31/Y2 (24,000 x 25%)", "value": money(va_required_end_y2)},
    {"label": "d: Valuation allowance adjustment recorded (from 0 beginning balance)", "value": money(va_adjustment)},
    {"label": "d: Net DTA reported at 12/31/Y2 (24,000 - 6,000)", "value": money(dta_net_reported_y2)},
    {"label": "d: Total Year 2 income tax expense (7,500 + 6,000)", "value": money(y2_total_income_tax_expense)},
    {"label": "d: Year 2 net income (30,000 - 13,500), informational", "value": money(y2_net_income)},
]

journal_entries = [
    {"part": "a", "lines": je_a},
    {"part": "c", "lines": je_c},
    {"part": "d", "lines": je_d},
]

notes = (
    "Book income = taxable income each year (no temporary differences other than the NOL), "
    "so Year 1 records a full tax benefit of 30,000 and no valuation allowance because the full "
    "DTA is MLTN of realization at 12/31/Y1. Year 2: the 80% limit caps the NOL deduction at "
    "80% x 30,000 = 24,000, leaving 6,000 of taxable income and 1,500 of tax payable; the 24,000 "
    "of NOL consumed writes off 6,000 of DTA, so total expense in entry (c) is 7,500 = 25% of the "
    "30,000 of pretax income. Remaining NOL 96,000 -> gross DTA 24,000; only 75% MLTN, so a 6,000 "
    "valuation allowance (25% x 24,000) is set up against income tax expense, leaving net DTA of "
    "18,000 on the 12/31/Y2 balance sheet and total Year 2 income tax expense of 13,500. "
    "Part (b) is an income-statement presentation, not a journal entry, so no JE is listed for it."
)

print(json.dumps({
    "id": "agent_032#01",
    "rounding_convention": "decimal.Decimal throughout; each period's amounts quantized to cents with ROUND_HALF_UP (all figures resolve to exact whole dollars); Dr = Cr asserted on every entry",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=2))
