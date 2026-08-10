#!/usr/bin/env python3
"""Solver for item agent_029#01 -- Meridian Fabricators Inc. (LO 18-4).

Fact pattern (from stem.md only):
  Pretax GAAP income: Y1 320,000 / Y2 280,000 / Y3 350,000.
  Enacted rate 25% for all years; beginning deferred balances zero at 1/1/Y1.
  1. Prepaid insurance 48,000 paid & recorded 12/31/Y1 -- deducted for tax in
     Y1 (when paid), expensed for GAAP in Y2.  Originating TAXABLE temporary
     difference in Y1 (book asset 48,000 vs tax basis 0) -> deferred tax
     LIABILITY at 12/31/Y1, fully reversing in Y2.
  2. Warranty accrual 36,000 recorded 12/31/Y1 (GAAP expense Y1); deducted for
     tax when settled, 12,000 in each of Y2, Y3, Y4.  Originating DEDUCTIBLE
     temporary difference in Y1 (book liability 36,000 vs tax basis 0) ->
     deferred tax ASSET, reversing 12,000/yr.
  3. Municipal bond interest 4,000 per year, Y1-Y3: PERMANENT difference,
     nontaxable, never creates a deferred tax balance.

ROUNDING CONVENTION
  All money is decimal.Decimal, quantized to whole cents (0.01) with
  ROUND_HALF_UP, applied per period (each year's taxable income, tax payable,
  deferred balance, and deferred-tax adjustment is rounded on its own before
  being carried forward) -- never round-at-end, never floats.
  Percentages in the rate reconciliation are quantized to 0.01 percentage
  points with ROUND_HALF_UP.  Every figure here happens to be exact at the
  cent level; the quantization is defensive, not corrective.

METHOD
  Taxable income = pretax GAAP income
                   - nontaxable permanent items
                   - originating/reversing temporary adjustments (book-to-tax).
  Ending deferred balances are computed from the ENDING cumulative temporary
  difference (balance-sheet approach) x enacted rate, not from the year's
  activity.  The deferred entry each year is the change in those balances.
  Income tax expense is the plug; it is independently cross-checked against
  (pretax income - permanent differences) x rate.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
PCT = Decimal("0.01")


def m(x):
    """Money: quantize to whole cents, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def pct(x):
    """Percentage points: quantize to 0.01, ROUND_HALF_UP."""
    return Decimal(x).quantize(PCT, rounding=ROUND_HALF_UP)


def num(d):
    """Decimal -> plain JSON number (int when integral)."""
    d = d.normalize()
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------- facts
YEARS = [1, 2, 3]
RATE = Decimal("0.25")

PRETAX = {1: m("320000"), 2: m("280000"), 3: m("350000")}
MUNI = {1: m("4000"), 2: m("4000"), 3: m("4000")}  # permanent, nontaxable

# Prepaid insurance: 48,000 deducted for tax in Y1, expensed for GAAP in Y2.
PREPAID = m("48000")
# book-to-tax adjustment to arrive at taxable income
prepaid_adj = {1: -PREPAID, 2: +PREPAID, 3: m("0")}
# ending cumulative TAXABLE temporary difference (book basis - tax basis of the
# prepaid asset): 48,000 at end Y1, 0 thereafter
prepaid_cum_taxable = {1: PREPAID, 2: m("0"), 3: m("0")}

# Warranty: 36,000 accrued Y1; 12,000 settled (deducted) in each of Y2, Y3, Y4.
WARRANTY_ACCRUAL = m("36000")
WARRANTY_PAID = {1: m("0"), 2: m("12000"), 3: m("12000")}
warranty_adj = {y: (WARRANTY_ACCRUAL if y == 1 else m("0")) - WARRANTY_PAID[y]
                for y in YEARS}
# ending cumulative DEDUCTIBLE temporary difference (warranty liability balance)
warranty_cum_deductible = {}
_bal = m("0")
for y in YEARS:
    _bal = m(_bal + (WARRANTY_ACCRUAL if y == 1 else m("0")) - WARRANTY_PAID[y])
    warranty_cum_deductible[y] = _bal

# ------------------------------------------------ (a) taxable income / payable
taxable = {}
payable = {}
for y in YEARS:
    ti = m(PRETAX[y] - MUNI[y] + prepaid_adj[y] + warranty_adj[y])
    taxable[y] = ti
    payable[y] = m(ti * RATE)

# ------------------------------------------------------ (b) deferred balances
dtl_end = {y: m(prepaid_cum_taxable[y] * RATE) for y in YEARS}
dta_end = {y: m(warranty_cum_deductible[y] * RATE) for y in YEARS}

# ------------------------------------------------------------ (c) JE amounts
entries = []
prev_dtl = m("0")
prev_dta = m("0")
for y in YEARS:
    d_dtl = m(dtl_end[y] - prev_dtl)   # + => credit DTL, - => debit DTL
    d_dta = m(dta_end[y] - prev_dta)   # + => debit DTA,  - => credit DTA
    expense = m(payable[y] + d_dtl - d_dta)

    # independent cross-check: expense = (pretax - permanent) * rate
    assert expense == m((PRETAX[y] - MUNI[y]) * RATE), (y, expense)

    lines = [{"account": "Income Tax Expense",
              "debit": num(expense), "credit": 0}]
    if d_dta > 0:
        lines.append({"account": "Deferred Tax Asset",
                      "debit": num(d_dta), "credit": 0})
    if d_dtl < 0:
        lines.append({"account": "Deferred Tax Liability",
                      "debit": num(-d_dtl), "credit": 0})
    if d_dta < 0:
        lines.append({"account": "Deferred Tax Asset",
                      "debit": 0, "credit": num(-d_dta)})
    if d_dtl > 0:
        lines.append({"account": "Deferred Tax Liability",
                      "debit": 0, "credit": num(d_dtl)})
    lines.append({"account": "Income Tax Payable",
                  "debit": 0, "credit": num(payable[y])})

    tot_dr = sum(Decimal(str(l["debit"])) for l in lines)
    tot_cr = sum(Decimal(str(l["credit"])) for l in lines)
    assert m(tot_dr) == m(tot_cr), (y, tot_dr, tot_cr)

    entries.append({"part": "c",
                    "description": "December 31, Year %d income tax entry" % y,
                    "lines": lines})
    prev_dtl, prev_dta = dtl_end[y], dta_end[y]

# --------------------------------------------- (d) Year 1 rate reconciliation
y1 = 1
stat_amt = m(PRETAX[y1] * RATE)
stat_pct = pct(RATE * 100)
muni_amt = m(-MUNI[y1] * RATE)
muni_pct = pct(muni_amt / PRETAX[y1] * 100)
eff_amt = m(stat_amt + muni_amt)
eff_pct = pct(eff_amt / PRETAX[y1] * 100)
assert eff_amt == m((PRETAX[y1] - MUNI[y1]) * RATE)

# --------------------------------------------------------------- assemble
answers = []
for y in YEARS:
    answers.append({"label": "a: taxable income Year %d" % y,
                    "value": num(taxable[y])})
for y in YEARS:
    answers.append({"label": "a: income tax payable Year %d" % y,
                    "value": num(payable[y])})
for y in YEARS:
    answers.append({"label": "b: deferred tax liability ending balance Year %d" % y,
                    "value": num(dtl_end[y])})
for y in YEARS:
    answers.append({"label": "b: deferred tax asset ending balance Year %d" % y,
                    "value": num(dta_end[y])})
answers += [
    {"label": "d: Year 1 tax at statutory rate (dollars)", "value": num(stat_amt)},
    {"label": "d: Year 1 statutory rate (percent)", "value": num(stat_pct)},
    {"label": "d: Year 1 tax-exempt municipal interest effect (dollars)",
     "value": num(muni_amt)},
    {"label": "d: Year 1 tax-exempt municipal interest effect (percent)",
     "value": num(muni_pct)},
    {"label": "d: Year 1 income tax expense / effective tax (dollars)",
     "value": num(eff_amt)},
    {"label": "d: Year 1 effective tax rate (percent)", "value": num(eff_pct)},
]

out = {
    "id": "agent_029#01",
    "rounding_convention": ("decimal.Decimal throughout; money quantized to "
                            "0.01 with ROUND_HALF_UP per period (per year), "
                            "not at end; percentages quantized to 0.01 "
                            "percentage points with ROUND_HALF_UP; no floats"),
    "answers": answers,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": ("Municipal interest is a permanent difference (no deferred tax). "
              "Prepaid insurance creates a taxable temporary difference / DTL "
              "at 12/31/Y1 that fully reverses in Y2. Warranty accrual creates "
              "a deductible temporary difference / DTA reversing 12,000 per "
              "year in Y2-Y4, so 3,000 of DTA remains at 12/31/Y3 for the Y4 "
              "settlement. Deferred balances are stated gross (DTL and DTA "
              "shown separately) as the Required part asks for each."),
}

print(json.dumps(out, indent=2))
