#!/usr/bin/env python3
"""
Blind solver -- item agent_160#01
Silverpine Logistics Inc. (LO 18-4): multi-year DTL/DTA schedules, period-end
income tax journal entries, and a Year 1 rate reconciliation.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, applied per period (never round-at-end-only):
  * All money is decimal.Decimal, never float. Every per-year tax figure
    (income tax payable, each deferred balance, each journal-entry line) is
    quantized to $0.01 with ROUND_HALF_UP at the moment it is computed, and the
    rounded figure is what carries into the next period's roll-forward.
  * Percentages in the rate reconciliation are quantized to 0.01 percentage
    points with ROUND_HALF_UP. The exact (unrounded) percentages are also
    reported in `notes` so the reconciliation footing can be checked.
  * No present-value factors are involved in this item, so the table-factor vs
    exact-formula question does not arise.
In this particular fact pattern every amount happens to land on a whole cent,
so rounding never actually bites; the convention is applied regardless.

METHOD
------
Taxable income = pretax GAAP income
                 - permanent nontaxable items (municipal bond interest)
                 +/- temporary book-to-tax adjustments for the period.
A temporary adjustment is negative when the tax return gets a deduction the
books do not yet have (prepaid insurance, Year 1) and positive when the books
take an expense the tax return does not yet get (warranty accrual, Year 1);
each reverses with the opposite sign in the period the other system catches up.

Deferred balances are computed from the cumulative temporary difference
remaining at each year end (the "future taxable / future deductible amounts"),
times the enacted rate expected to be in effect on reversal:
  DTL = cumulative taxable temporary difference    x rate
  DTA = cumulative deductible temporary difference x rate
Income tax expense in each journal entry is the plug; it is independently
cross-checked against (pretax GAAP income - permanent differences) x rate.

Run:  python3 solver.py     -> prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
PCT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP, per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def pct(x: Decimal) -> Decimal:
    """Quantize a percentage to 0.01 percentage points, ROUND_HALF_UP."""
    return Decimal(x).quantize(PCT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly plain number: int when integral, else float of the cents value."""
    d = Decimal(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------------------
# Fact pattern (from the stem only)
# ---------------------------------------------------------------------------
YEARS = [1, 2, 3]

PRETAX = {
    1: Decimal("400000"),
    2: Decimal("450000"),
    3: Decimal("380000"),
}

RATE = Decimal("0.21")  # enacted 21% for all years

# Permanent difference: nontaxable municipal bond interest, included in pretax
# GAAP income each of Years 1-3, never in taxable income.
MUNI_INTEREST = {1: Decimal("3000"), 2: Decimal("3000"), 3: Decimal("3000")}

# --- Difference 1: prepaid insurance -----------------------------------------
# $60,000 paid and recorded 12/31/Y1. Deductible for tax when paid (Year 1);
# GAAP expense in Year 2. Asset book basis > tax basis => taxable temporary
# difference => DTL.
PREPAID = Decimal("60000")
# Amount the tax return deducts, by year:
prepaid_tax_deduction = {1: PREPAID, 2: Decimal("0"), 3: Decimal("0")}
# Amount the books expense, by year:
prepaid_book_expense = {1: Decimal("0"), 2: PREPAID, 3: Decimal("0")}

# --- Difference 2: warranty accrual ------------------------------------------
# $48,000 accrued 12/31/Y1 (book expense in Year 1); settled/paid $16,000 in
# each of Years 2, 3, and 4 (tax deduction when paid). Liability book basis >
# tax basis => deductible temporary difference => DTA.
WARRANTY_ACCRUAL = Decimal("48000")
WARRANTY_SETTLEMENT = Decimal("16000")
warranty_book_expense = {1: WARRANTY_ACCRUAL, 2: Decimal("0"), 3: Decimal("0")}
warranty_tax_deduction = {
    1: Decimal("0"),
    2: WARRANTY_SETTLEMENT,
    3: WARRANTY_SETTLEMENT,
    4: WARRANTY_SETTLEMENT,  # Year 4 settlement drives the Y3 ending DTA
}

# ---------------------------------------------------------------------------
# (a) Taxable income and income tax payable, Years 1-3
# ---------------------------------------------------------------------------
taxable_income = {}
tax_payable = {}
recon_detail = {}

for y in YEARS:
    # book-to-tax adjustment for each temporary difference:
    #   (what tax recognizes) - (what books recognize), signed as an income effect.
    # An expense/deduction reduces income, so a tax deduction the books lack is
    # a NEGATIVE adjustment, and a book expense the tax return lacks is POSITIVE.
    adj_prepaid = prepaid_book_expense[y] - prepaid_tax_deduction[y]
    adj_warranty = warranty_book_expense[y] - warranty_tax_deduction[y]

    ti = PRETAX[y] - MUNI_INTEREST[y] + adj_prepaid + adj_warranty
    taxable_income[y] = money(ti)
    tax_payable[y] = money(taxable_income[y] * RATE)

    recon_detail[y] = {
        "pretax_gaap": money(PRETAX[y]),
        "less_muni": money(-MUNI_INTEREST[y]),
        "prepaid_adj": money(adj_prepaid),
        "warranty_adj": money(adj_warranty),
    }

# ---------------------------------------------------------------------------
# (b) Ending-balance schedules and three-year roll-forwards
# ---------------------------------------------------------------------------
# Cumulative temporary difference remaining at each year end = amounts still to
# reverse in future periods.

# DTL (prepaid insurance): future TAXABLE amounts = book expense still to come
# for which the tax deduction has already been taken.
future_taxable = {}
for y in YEARS:
    remaining = sum(
        (prepaid_book_expense[k] for k in prepaid_book_expense if k > y),
        Decimal("0"),
    )
    future_taxable[y] = money(remaining)

# DTA (warranty): future DEDUCTIBLE amounts = settlements still to be paid, for
# which the book expense has already been recorded.
future_deductible = {}
for y in YEARS:
    remaining = sum(
        (warranty_tax_deduction[k] for k in warranty_tax_deduction if k > y),
        Decimal("0"),
    )
    future_deductible[y] = money(remaining)

dtl_end = {y: money(future_taxable[y] * RATE) for y in YEARS}
dta_end = {y: money(future_deductible[y] * RATE) for y in YEARS}

# Roll-forwards, beginning balances zero on January 1, Year 1.
dtl_roll = {}
dta_roll = {}
prev_dtl = Decimal("0.00")
prev_dta = Decimal("0.00")
for y in YEARS:
    dtl_roll[y] = {
        "beginning": prev_dtl,
        "change": money(dtl_end[y] - prev_dtl),
        "ending": dtl_end[y],
    }
    dta_roll[y] = {
        "beginning": prev_dta,
        "change": money(dta_end[y] - prev_dta),
        "ending": dta_end[y],
    }
    prev_dtl = dtl_end[y]
    prev_dta = dta_end[y]

# ---------------------------------------------------------------------------
# (c) December 31 income tax journal entries, Years 1-3
# ---------------------------------------------------------------------------
journal_entries = []
for y in YEARS:
    dtl_change = dtl_roll[y]["change"]  # + => DTL increases (credit DTL)
    dta_change = dta_roll[y]["change"]  # + => DTA increases (debit DTA)

    # Income tax expense is the plug:
    #   expense = current payable + increase in DTL - increase in DTA
    expense = money(tax_payable[y] + dtl_change - dta_change)

    lines = []
    if expense >= 0:
        lines.append({"account": "Income Tax Expense",
                      "debit": num(expense), "credit": 0})
    else:
        lines.append({"account": "Income Tax Expense",
                      "debit": 0, "credit": num(-expense)})

    # Deferred tax asset: debit when it increases, credit when it reverses.
    if dta_change > 0:
        lines.append({"account": "Deferred Tax Asset",
                      "debit": num(dta_change), "credit": 0})
    elif dta_change < 0:
        lines.append({"account": "Deferred Tax Asset",
                      "debit": 0, "credit": num(-dta_change)})

    # Deferred tax liability: credit when it increases, debit when it reverses.
    if dtl_change < 0:
        lines.append({"account": "Deferred Tax Liability",
                      "debit": num(-dtl_change), "credit": 0})
    elif dtl_change > 0:
        lines.append({"account": "Deferred Tax Liability",
                      "debit": 0, "credit": num(dtl_change)})

    lines.append({"account": "Income Taxes Payable",
                  "debit": 0, "credit": num(tax_payable[y])})

    # Debits must equal credits.
    tot_dr = sum(Decimal(str(l["debit"])) for l in lines)
    tot_cr = sum(Decimal(str(l["credit"])) for l in lines)
    assert tot_dr == tot_cr, f"Year {y} entry out of balance: {tot_dr} vs {tot_cr}"

    # Independent cross-check: total tax expense should equal
    # (pretax GAAP income - permanent differences) x rate.
    expected = money((PRETAX[y] - MUNI_INTEREST[y]) * RATE)
    assert expense == expected, f"Year {y} expense {expense} != check {expected}"

    journal_entries.append({"part": "c", "lines": lines,
                            "_year": y, "_expense": expense})

expense_by_year = {je["_year"]: je["_expense"] for je in journal_entries}
for je in journal_entries:
    del je["_year"]
    del je["_expense"]

# ---------------------------------------------------------------------------
# (d) Year 1 rate reconciliation (dollars and percentages)
# ---------------------------------------------------------------------------
Y1 = 1
statutory_dollars = money(PRETAX[Y1] * RATE)
statutory_pct_exact = RATE * Decimal("100")

muni_effect_dollars = money(-MUNI_INTEREST[Y1] * RATE)
muni_pct_exact = (muni_effect_dollars / PRETAX[Y1]) * Decimal("100")

total_expense_dollars = expense_by_year[Y1]
effective_pct_exact = (total_expense_dollars / PRETAX[Y1]) * Decimal("100")

# Reconciliation must foot in dollars.
assert money(statutory_dollars + muni_effect_dollars) == total_expense_dollars

# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------
answers = []

# (a)
for y in YEARS:
    answers.append({"label": f"a: Year {y} taxable income",
                    "value": num(taxable_income[y])})
    answers.append({"label": f"a: Year {y} income tax payable",
                    "value": num(tax_payable[y])})

# (b) ending-balance schedules
for y in YEARS:
    answers.append({"label": f"b: Deferred tax liability ending balance, December 31 Year {y}",
                    "value": num(dtl_end[y])})
for y in YEARS:
    answers.append({"label": f"b: Deferred tax asset ending balance, December 31 Year {y}",
                    "value": num(dta_end[y])})

# (b) three-year roll-forwards
for y in YEARS:
    answers.append({"label": f"b: DTL roll-forward Year {y} - beginning balance",
                    "value": num(dtl_roll[y]["beginning"])})
    answers.append({"label": f"b: DTL roll-forward Year {y} - change (increase/(decrease))",
                    "value": num(dtl_roll[y]["change"])})
    answers.append({"label": f"b: DTL roll-forward Year {y} - ending balance",
                    "value": num(dtl_roll[y]["ending"])})
for y in YEARS:
    answers.append({"label": f"b: DTA roll-forward Year {y} - beginning balance",
                    "value": num(dta_roll[y]["beginning"])})
    answers.append({"label": f"b: DTA roll-forward Year {y} - change (increase/(decrease))",
                    "value": num(dta_roll[y]["change"])})
    answers.append({"label": f"b: DTA roll-forward Year {y} - ending balance",
                    "value": num(dta_roll[y]["ending"])})

# (d)
answers.append({"label": "d: Year 1 tax at statutory rate (dollars)",
                "value": num(statutory_dollars)})
answers.append({"label": "d: Year 1 statutory tax rate (percent)",
                "value": num(pct(statutory_pct_exact))})
answers.append({"label": "d: Year 1 tax-exempt municipal bond interest effect (dollars)",
                "value": num(muni_effect_dollars)})
answers.append({"label": "d: Year 1 tax-exempt municipal bond interest effect (percent)",
                "value": num(pct(muni_pct_exact))})
answers.append({"label": "d: Year 1 total income tax expense (dollars)",
                "value": num(total_expense_dollars)})
answers.append({"label": "d: Year 1 effective tax rate (percent)",
                "value": num(pct(effective_pct_exact))})

notes = (
    "Year 1 book-to-tax: 400,000 pretax - 3,000 muni interest (permanent) "
    "- 60,000 prepaid insurance deducted for tax when paid + 48,000 warranty "
    "accrued for books but not yet paid = 385,000 taxable. The prepaid "
    "insurance is a taxable temporary difference (asset book basis 60,000 > "
    "tax basis 0) so it creates the DTL and fully reverses in Year 2; the "
    "warranty is a deductible temporary difference that reverses 16,000 per "
    "year in Years 2-4, so a 3,360 DTA still remains at December 31 Year 3 "
    "for the Year 4 settlement. Exact unrounded rate-reconciliation "
    f"percentages: statutory {statutory_pct_exact}%, municipal interest "
    f"{muni_pct_exact}%, effective {effective_pct_exact}%."
)

output = {
    "id": "agent_160#01",
    "rounding_convention": (
        "ROUND_HALF_UP per period, to $0.01 on every per-year figure "
        "(Decimal throughout, no floats); percentages ROUND_HALF_UP to 0.01 "
        "percentage points; no PV factors involved"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
