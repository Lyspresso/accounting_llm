#!/usr/bin/env python3
"""
Blind solver -- item agent_382#00
Harborline Robotics Corp.: convertible bonds issued at par, period-end interest
accrual AJ, interest schedule, basic/diluted EPS under the if-converted method
(full-year and October 1 partial-year), and the January 1, 20X6 interest payment
and conversion settlement entries.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no float is ever constructed.

* Money: computed period by period and quantized to cents (0.01) with
  ROUND_HALF_UP at the point each period's amount is determined
  (round-per-period, not round-at-end). Every amount in this fact pattern is a
  whole dollar, so the quantization is exact and never actually shifts a value.
* Interest accrual: simple stated-rate interest on face, prorated by whole
  months outstanding over 12 (3/12 for the October 1 alternate fact). The bonds
  were issued AT PAR, so there is no discount/premium and no effective-interest
  amortization; interest expense equals cash interest and the carrying amount
  stays at face.
* Tax effect on the if-converted add-back: interest x (1 - 25%), quantized to
  cents with ROUND_HALF_UP after the multiplication.
* EPS: computed as an exact Decimal quotient of (already-rounded) numerator over
  denominator, then quantized to 2 decimal places with ROUND_HALF_UP. This
  matters in part g, where basic EPS lands exactly on 2.935 and ROUND_HALF_UP
  carries it to 2.94.
* Denominator share weighting: incremental shares from assumed conversion are
  prorated by months outstanding over 12 and quantized to whole shares with
  ROUND_HALF_UP (3/12 x 30,000 = 7,500 exactly here).
* Dilution test: a security is dilutive only if it REDUCES EPS below basic. The
  test is applied by comparing the recomputed diluted EPS against basic EPS; if
  the security were antidilutive its effects would be excluded and diluted EPS
  would be reported equal to basic EPS.

Run: python3 solver.py   (prints one JSON object on stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 50

CENTS = Decimal("0.01")
SHARE = Decimal("1")


def money(value):
    """Quantize to cents, ROUND_HALF_UP (applied per period, as computed)."""
    return Decimal(value).quantize(CENTS, rounding=ROUND_HALF_UP)


def shares(value):
    """Quantize a weighted share count to whole shares, ROUND_HALF_UP."""
    return Decimal(value).quantize(SHARE, rounding=ROUND_HALF_UP)


def eps(numerator, denominator):
    """EPS to 2 decimals, ROUND_HALF_UP, from an exact Decimal quotient."""
    return (Decimal(numerator) / Decimal(denominator)).quantize(
        CENTS, rounding=ROUND_HALF_UP
    )


def num(dec):
    """JSON-friendly number: int when integral, else float-free string->number."""
    dec = dec.normalize()
    if dec == dec.to_integral_value():
        return int(dec)
    return json.loads(str(dec))


# ---------------------------------------------------------------------------
# Fact pattern (transcribed from the stem; nothing below is hard-coded output)
# ---------------------------------------------------------------------------
BOND_COUNT = Decimal("1200")
FACE_PER_BOND = Decimal("1000")
STATED_RATE = Decimal("0.07")
SHARES_PER_BOND = Decimal("25")
PAR_PER_SHARE = Decimal("2")
TAX_RATE = Decimal("0.25")

WA_SHARES = Decimal("350000")
NET_INCOME_FULL_YEAR = Decimal("980000")
NET_INCOME_OCT1 = Decimal("1027250")

MONTHS_FULL_YEAR = Decimal("12")
MONTHS_OCT1 = Decimal("3")  # Oct 1 -> Dec 31

TOTAL_FACE = money(BOND_COUNT * FACE_PER_BOND)
CONVERSION_SHARES = shares(BOND_COUNT * SHARES_PER_BOND)


def accrued_interest(months):
    """Stated-rate interest on face for `months` months, rounded per period."""
    return money(TOTAL_FACE * STATED_RATE * (months / Decimal("12")))


def after_tax(amount):
    return money(amount * (Decimal("1") - TAX_RATE))


# ---------------------------------------------------------------------------
# (a) January 1, 20X5 issuance at par
# ---------------------------------------------------------------------------
je_a = {
    "part": "a",
    "description": "January 1, 20X5 - issue 1,200 convertible bonds at par",
    "lines": [
        {"account": "Cash", "debit": num(TOTAL_FACE), "credit": 0},
        {"account": "Bonds Payable", "debit": 0, "credit": num(TOTAL_FACE)},
    ],
}

# ---------------------------------------------------------------------------
# (b) December 31, 20X5 period-end adjusting entry - full year of interest
# ---------------------------------------------------------------------------
interest_full_year = accrued_interest(MONTHS_FULL_YEAR)

je_b = {
    "part": "b",
    "description": "December 31, 20X5 AJ - accrue 12 months interest "
                   "($1,200,000 x 7% x 12/12); paid January 1, 20X6",
    "lines": [
        {"account": "Interest Expense", "debit": num(interest_full_year), "credit": 0},
        {"account": "Interest Payable", "debit": 0, "credit": num(interest_full_year)},
    ],
}

# ---------------------------------------------------------------------------
# (c) 20X5 subsequent-measurement interest schedule
#     Issued at par -> no discount/premium -> carrying amount stays at face.
#     Interest is paid every January 1 for the preceding year, so the first cash
#     payment (for 20X5) occurs January 1, 20X6 -> cash paid DURING 20X5 = 0.
# ---------------------------------------------------------------------------
cash_paid_20x5 = money("0")
interest_payable_end_20x5 = money(interest_full_year - cash_paid_20x5)
carrying_amount_end_20x5 = TOTAL_FACE  # at par, nothing to amortize

# ---------------------------------------------------------------------------
# (d) Basic EPS - full-year facts
#     No preferred stock, so income available to common = net income.
# ---------------------------------------------------------------------------
basic_numerator = NET_INCOME_FULL_YEAR
basic_denominator = WA_SHARES
basic_eps = eps(basic_numerator, basic_denominator)

# ---------------------------------------------------------------------------
# (e) Diluted EPS - if-converted, full year
# ---------------------------------------------------------------------------
addback_full_year = after_tax(interest_full_year)
diluted_numerator = money(basic_numerator + addback_full_year)
diluted_denominator = shares(basic_denominator + CONVERSION_SHARES)
diluted_eps = eps(diluted_numerator, diluted_denominator)
is_dilutive = diluted_eps < basic_eps
dilution_label = "dilutive" if is_dilutive else "antidilutive"

# If antidilutive the effects would be excluded and diluted EPS = basic EPS.
reported_diluted_eps = diluted_eps if is_dilutive else basic_eps

# ---------------------------------------------------------------------------
# (f) Face-of-income-statement presentation
#     Complex capital structure -> present basic AND diluted with equal
#     prominence.
# ---------------------------------------------------------------------------
presented = (
    "Complex capital structure: present both basic EPS of ${b} and diluted EPS "
    "of ${d} on the face of the 20X5 income statement, with equal prominence."
).format(b=basic_eps, d=reported_diluted_eps)

# ---------------------------------------------------------------------------
# (g) October 1, 20X5 issuance alternate facts
# ---------------------------------------------------------------------------
interest_oct1 = accrued_interest(MONTHS_OCT1)
addback_oct1 = after_tax(interest_oct1)
incremental_shares_oct1 = shares(CONVERSION_SHARES * (MONTHS_OCT1 / Decimal("12")))

basic_numerator_g = NET_INCOME_OCT1
basic_denominator_g = WA_SHARES
basic_eps_g = eps(basic_numerator_g, basic_denominator_g)

diluted_numerator_g = money(basic_numerator_g + addback_oct1)
diluted_denominator_g = shares(basic_denominator_g + incremental_shares_oct1)
diluted_eps_g = eps(diluted_numerator_g, diluted_denominator_g)
is_dilutive_g = diluted_eps_g < basic_eps_g
dilution_label_g = "dilutive" if is_dilutive_g else "antidilutive"
reported_diluted_eps_g = diluted_eps_g if is_dilutive_g else basic_eps_g

je_g = {
    "part": "g",
    "description": "December 31, 20X5 AJ (October 1 issuance alternate facts) - "
                   "accrue 3 months interest ($1,200,000 x 7% x 3/12)",
    "lines": [
        {"account": "Interest Expense", "debit": num(interest_oct1), "credit": 0},
        {"account": "Interest Payable", "debit": 0, "credit": num(interest_oct1)},
    ],
}

# ---------------------------------------------------------------------------
# (h) January 1, 20X6 - (i) pay accrued interest, (ii) convert all bonds
#     Book-value method: carrying amount of the debt moves into equity, no gain
#     or loss (ASC 470-20-40-4). Accrued interest was settled in cash first, so
#     nothing is left to roll into the conversion entry.
# ---------------------------------------------------------------------------
je_h1 = {
    "part": "h",
    "description": "January 1, 20X6 (i) - pay 20X5 accrued interest",
    "lines": [
        {"account": "Interest Payable", "debit": num(interest_full_year), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(interest_full_year)},
    ],
}

common_stock_credit = money(CONVERSION_SHARES * PAR_PER_SHARE)
apic_credit = money(TOTAL_FACE - common_stock_credit)

je_h2 = {
    "part": "h",
    "description": "January 1, 20X6 (ii) - all bondholders convert; book-value "
                   "method, no gain or loss recognized",
    "lines": [
        {"account": "Bonds Payable", "debit": num(TOTAL_FACE), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(common_stock_credit)},
        {
            "account": "Paid-In Capital in Excess of Par-Common Stock",
            "debit": 0,
            "credit": num(apic_credit),
        },
    ],
}

journal_entries = [je_a, je_b, je_g, je_h1, je_h2]

# Balance proof: debits must equal credits in every entry.
for entry in journal_entries:
    dr = sum(Decimal(str(line["debit"])) for line in entry["lines"])
    cr = sum(Decimal(str(line["credit"])) for line in entry["lines"])
    assert dr == cr, "Entry {} out of balance: {} vs {}".format(entry["part"], dr, cr)

# ---------------------------------------------------------------------------
# Answers - only the figures the Required parts ask for.
# ---------------------------------------------------------------------------
answers = [
    # c - subsequent measurement interest schedule for 20X5
    {"label": "c: face amount", "value": num(TOTAL_FACE)},
    {"label": "c: stated rate (%)", "value": num(STATED_RATE * Decimal("100"))},
    {"label": "c: interest expense 20X5", "value": num(interest_full_year)},
    {"label": "c: cash interest paid during 20X5", "value": num(cash_paid_20x5)},
    {"label": "c: interest payable, December 31, 20X5",
     "value": num(interest_payable_end_20x5)},
    {"label": "c: carrying amount, December 31, 20X5",
     "value": num(carrying_amount_end_20x5)},

    # d - basic EPS, full-year facts
    {"label": "d: basic EPS 20X5", "value": num(basic_eps)},

    # e - diluted EPS reconciliation, if-converted, full year
    {"label": "e: add back interest net of tax", "value": num(addback_full_year)},
    {"label": "e: add new common shares", "value": num(CONVERSION_SHARES)},
    {"label": "e: diluted EPS numerator", "value": num(diluted_numerator)},
    {"label": "e: diluted EPS denominator", "value": num(diluted_denominator)},
    {"label": "e: diluted EPS 20X5", "value": num(diluted_eps)},
    {"label": "e: bonds dilutive or antidilutive", "value": dilution_label},

    # f - presentation
    {"label": "f: EPS reported on face of income statement", "value": presented},

    # g - October 1 issuance alternate facts
    {"label": "g: basic EPS 20X5 (Oct 1 issuance)", "value": num(basic_eps_g)},
    {"label": "g: add back prorated interest net of tax", "value": num(addback_oct1)},
    {"label": "g: add new prorated common shares",
     "value": num(incremental_shares_oct1)},
    {"label": "g: diluted EPS numerator (Oct 1 issuance)",
     "value": num(diluted_numerator_g)},
    {"label": "g: diluted EPS denominator (Oct 1 issuance)",
     "value": num(diluted_denominator_g)},
    {"label": "g: diluted EPS 20X5 (Oct 1 issuance)", "value": num(diluted_eps_g)},
    {"label": "g: bonds dilutive or antidilutive (Oct 1 issuance)",
     "value": dilution_label_g},
]

notes = (
    "Bonds issued at par, so no discount/premium and no effective-interest "
    "amortization; interest expense = cash interest = $84,000 and carrying "
    "amount stays at $1,200,000. Because interest is paid every January 1 for "
    "the preceding year, cash interest paid DURING 20X5 is $0 and the full "
    "$84,000 sits in Interest Payable at December 31, 20X5. If-converted "
    "add-back is after-tax interest at 25%. Part g weights both the add-back "
    "and the 30,000 conversion shares by 3/12. Part g basic EPS is exactly "
    "$2.935 before rounding; ROUND_HALF_UP carries it to $2.94. Conversion in "
    "part h uses the book-value method after the accrued interest is paid in "
    "cash, so no gain or loss and no accrued interest rolls into equity."
)

output = {
    "id": "agent_382#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats. Money quantized to cents with "
        "ROUND_HALF_UP per period as computed (round-per-period). Interest = "
        "face x stated rate x months/12 (simple, at par, no amortization). "
        "After-tax add-back = interest x (1 - 25%), rounded to cents. EPS = "
        "exact Decimal quotient of rounded numerator over denominator, then "
        "quantized to 2 decimals with ROUND_HALF_UP. Weighted incremental "
        "shares prorated by months/12 and rounded to whole shares ROUND_HALF_UP."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
