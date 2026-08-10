#!/usr/bin/env python3
"""Blind solver for item agent_251#00 — Riverbend Precision Instruments Inc.

Topic: convertible bonds issued at par; Year 1 interest schedule and JEs; basic
EPS; diluted EPS under the if-converted method; income-statement presentation;
Jan 1 Year 2 conversion (settlement) JE; and a July 1 issuance alternate fact
requiring partial-year weighting of both the interest add-back and the
incremental shares.

--------------------------------------------------------------------------
ROUNDING CONVENTION
--------------------------------------------------------------------------
All money is decimal.Decimal — no binary floats anywhere in this file.

* Money (bond carrying amounts, interest expense, cash paid, journal-entry
  amounts): rounded to the cent with ROUND_HALF_UP, applied PER PERIOD, not
  once at the end. Each semiannual interest amount is computed and rounded on
  its own line of the schedule; the schedule is never derived by rounding an
  annual total.
* Per-share amounts (basic EPS, diluted EPS): rounded to the cent with
  ROUND_HALF_UP at the moment of presentation. The numerator and denominator
  that feed an EPS figure are exact (unrounded) values; only the resulting
  ratio is rounded. This is the ordinary "round once, at the reported figure"
  treatment for EPS.
* Share counts are exact integers (no rounding needed — 1,500 bonds x 30
  shares divides evenly, and the partial-year weight is exactly 6/12).
* No present-value table factors are used. The bonds are issued AT PAR, so the
  effective rate equals the stated rate, carrying amount stays at face for
  every period, and interest expense equals cash interest paid. There is no
  discount/premium amortization and therefore no table-factor-vs-exact-formula
  choice to make.

--------------------------------------------------------------------------
DERIVATION NOTES
--------------------------------------------------------------------------
Issued at par  ->  interest expense = cash paid = face x stated rate x 6/12
                   each semiannual period; carrying amount is constant at face.

If-converted method: assume conversion at the LATER of the start of the period
or the issuance date. Numerator = net income + after-tax interest that was
actually charged against income on the convertible debt during the period.
Denominator = weighted-average common shares + incremental conversion shares
weighted for the portion of the period the bonds were outstanding.

The bonds are dilutive when diluted EPS < basic EPS.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Round a monetary amount to the cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def per_share(numerator: Decimal, denominator: Decimal) -> Decimal:
    """Round a per-share amount to the cent, ROUND_HALF_UP."""
    return (numerator / denominator).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly: emit an int when the value is whole, else a float-free str-safe float."""
    d = d.normalize()
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------------------
# Given facts (straight from the stem — nothing here is a computed answer)
# ---------------------------------------------------------------------------
BONDS = Decimal(1500)                     # number of convertible bonds
FACE_PER_BOND = Decimal(1000)             # $ face per bond
STATED_RATE = Decimal("0.06")             # 6% stated annual
PERIODS_PER_YEAR = Decimal(2)             # semiannual interest, Jun 30 / Dec 31
SHARES_PER_BOND = Decimal(30)             # conversion ratio
PAR_PER_SHARE = Decimal("1.00")           # $1 par common
WA_SHARES = Decimal(250000)               # weighted-average common shares
NET_INCOME_Y1 = Decimal(750000)           # Year 1 NI, full-year bond facts
TAX_RATE = Decimal("0.25")                # enacted rate
NET_INCOME_Y1_ALT = Decimal("783750")     # Year 1 NI, July 1 issuance alternate

TOTAL_FACE = BONDS * FACE_PER_BOND                       # 1,500,000
CONVERSION_SHARES = BONDS * SHARES_PER_BOND              # 45,000

# ---------------------------------------------------------------------------
# (a) January 1, Year 1 issuance at par
# ---------------------------------------------------------------------------
je_a = {
    "part": "a",
    "description": "Jan 1, Year 1 - issuance of 1,500 convertible bonds at par",
    "lines": [
        {"account": "Cash", "debit": num(money(TOTAL_FACE)), "credit": 0},
        {"account": "Bonds Payable", "debit": 0, "credit": num(money(TOTAL_FACE))},
    ],
}

# ---------------------------------------------------------------------------
# (b) Year 1 subsequent measurement interest schedule (issued at par)
# ---------------------------------------------------------------------------
semi_rate = STATED_RATE / PERIODS_PER_YEAR               # 3% per period
carrying = money(TOTAL_FACE)
schedule = []
for period_label in ("June 30, Year 1", "December 31, Year 1"):
    # Issued at par: effective rate == stated rate, so expense == cash paid.
    interest_expense = money(carrying * semi_rate)
    cash_paid = money(TOTAL_FACE * semi_rate)
    amortization = interest_expense - cash_paid           # zero at par
    carrying = money(carrying + amortization)
    schedule.append(
        {
            "date": period_label,
            "face": num(money(TOTAL_FACE)),
            "semiannual_rate": "3%",
            "interest_expense": num(interest_expense),
            "cash_paid": num(cash_paid),
            "premium_discount_amortization": num(amortization),
            "carrying_amount_end": num(carrying),
        }
    )

je_b_jun = {
    "part": "b",
    "description": "June 30, Year 1 - semiannual cash interest payment",
    "lines": [
        {
            "account": "Interest Expense",
            "debit": schedule[0]["interest_expense"],
            "credit": 0,
        },
        {"account": "Cash", "debit": 0, "credit": schedule[0]["cash_paid"]},
    ],
}
je_b_dec = {
    "part": "b",
    "description": "December 31, Year 1 - semiannual cash interest payment",
    "lines": [
        {
            "account": "Interest Expense",
            "debit": schedule[1]["interest_expense"],
            "credit": 0,
        },
        {"account": "Cash", "debit": 0, "credit": schedule[1]["cash_paid"]},
    ],
}

# ---------------------------------------------------------------------------
# (c) Basic EPS, Year 1 (full-year facts)
# ---------------------------------------------------------------------------
basic_eps = per_share(NET_INCOME_Y1, WA_SHARES)

# ---------------------------------------------------------------------------
# (d) Diluted EPS - if-converted method, full-year facts
# ---------------------------------------------------------------------------
annual_interest = money(TOTAL_FACE * STATED_RATE)                    # 90,000
tax_effect = money(annual_interest * TAX_RATE)                       # 22,500
after_tax_interest_addback = money(annual_interest - tax_effect)     # 67,500

diluted_numerator = money(NET_INCOME_Y1 + after_tax_interest_addback)
diluted_denominator = WA_SHARES + CONVERSION_SHARES
diluted_eps = per_share(diluted_numerator, diluted_denominator)

# Dilution test: compare the exact if-converted ratio to basic EPS.
dilutive = (diluted_numerator / diluted_denominator) < (NET_INCOME_Y1 / WA_SHARES)
dilution_status = "dilutive" if dilutive else "antidilutive"

# EPS actually reported = diluted only if the instrument is dilutive.
reported_diluted_eps = diluted_eps if dilutive else basic_eps

# ---------------------------------------------------------------------------
# (f) January 1, Year 2 conversion (settlement) JE - book value method
# ---------------------------------------------------------------------------
common_stock_par = money(CONVERSION_SHARES * PAR_PER_SHARE)          # 45,000
carrying_at_conversion = money(TOTAL_FACE)                           # par, no disc/prem
apic = money(carrying_at_conversion - common_stock_par)              # 1,455,000

je_f = {
    "part": "f",
    "description": (
        "Jan 1, Year 2 - conversion of all 1,500 bonds into 45,000 common shares "
        "(book value method; carrying amount = par, no unamortized discount/premium)"
    ),
    "lines": [
        {"account": "Bonds Payable", "debit": num(carrying_at_conversion), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(common_stock_par)},
        {
            "account": "Paid-in Capital in Excess of Par - Common Stock",
            "debit": 0,
            "credit": num(apic),
        },
    ],
}

# ---------------------------------------------------------------------------
# (g) July 1, Year 1 issuance alternate - partial-year weighting
# ---------------------------------------------------------------------------
MONTHS_OUTSTANDING = Decimal(6)
MONTHS_IN_YEAR = Decimal(12)
weight = MONTHS_OUTSTANDING / MONTHS_IN_YEAR                          # 6/12

basic_eps_alt = per_share(NET_INCOME_Y1_ALT, WA_SHARES)

# Only one semiannual period of interest was charged against income.
alt_interest_pretax = money(TOTAL_FACE * semi_rate)                   # 45,000
alt_tax_effect = money(alt_interest_pretax * TAX_RATE)                # 11,250
alt_addback = money(alt_interest_pretax - alt_tax_effect)             # 33,750

alt_numerator = money(NET_INCOME_Y1_ALT + alt_addback)
alt_incremental_shares = CONVERSION_SHARES * weight                   # 22,500
alt_denominator = WA_SHARES + alt_incremental_shares
diluted_eps_alt = per_share(alt_numerator, alt_denominator)

alt_dilutive = (alt_numerator / alt_denominator) < (NET_INCOME_Y1_ALT / WA_SHARES)
alt_status = "dilutive" if alt_dilutive else "antidilutive"

# ---------------------------------------------------------------------------
# Internal consistency checks (not reported as answers)
# ---------------------------------------------------------------------------
for je in (je_a, je_b_jun, je_b_dec, je_f):
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"JE {je['part']} out of balance: {dr} vs {cr}"

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
answers = [
    # (b) subsequent measurement interest schedule figures
    {
        "label": "b: Year 1 interest schedule - face used each period",
        "value": num(money(TOTAL_FACE)),
    },
    {
        "label": "b: June 30, Year 1 interest expense",
        "value": schedule[0]["interest_expense"],
    },
    {"label": "b: June 30, Year 1 cash paid", "value": schedule[0]["cash_paid"]},
    {
        "label": "b: carrying amount after June 30, Year 1",
        "value": schedule[0]["carrying_amount_end"],
    },
    {
        "label": "b: December 31, Year 1 interest expense",
        "value": schedule[1]["interest_expense"],
    },
    {"label": "b: December 31, Year 1 cash paid", "value": schedule[1]["cash_paid"]},
    {
        "label": "b: carrying amount at December 31, Year 1",
        "value": schedule[1]["carrying_amount_end"],
    },
    # (c) basic EPS
    {"label": "c: basic EPS, Year 1", "value": num(basic_eps)},
    # (d) if-converted reconciliation
    {
        "label": "d: after-tax interest add-back to numerator (if-converted)",
        "value": num(after_tax_interest_addback),
    },
    {"label": "d: diluted EPS numerator", "value": num(diluted_numerator)},
    {
        "label": "d: incremental shares from assumed conversion",
        "value": num(CONVERSION_SHARES),
    },
    {"label": "d: diluted EPS denominator", "value": num(diluted_denominator)},
    {"label": "d: diluted EPS, Year 1", "value": num(diluted_eps)},
    {"label": "d: bonds dilutive or antidilutive", "value": dilution_status},
    # (e) presentation
    {
        "label": "e: basic EPS reported on face of Year 1 income statement",
        "value": num(basic_eps),
    },
    {
        "label": "e: diluted EPS reported on face of Year 1 income statement",
        "value": num(reported_diluted_eps),
    },
    # (g) July 1 issuance alternate
    {
        "label": "g: basic EPS, Year 1 (July 1 issuance)",
        "value": num(basic_eps_alt),
    },
    {
        "label": "g: after-tax interest add-back (six months, July 1 issuance)",
        "value": num(alt_addback),
    },
    {"label": "g: diluted EPS numerator (July 1 issuance)", "value": num(alt_numerator)},
    {
        "label": "g: incremental shares weighted 6/12 (July 1 issuance)",
        "value": num(alt_incremental_shares),
    },
    {
        "label": "g: diluted EPS denominator (July 1 issuance)",
        "value": num(alt_denominator),
    },
    {
        "label": "g: diluted EPS, Year 1 (July 1 issuance)",
        "value": num(diluted_eps_alt),
    },
    {"label": "g: bonds dilutive or antidilutive (July 1 issuance)", "value": alt_status},
]

notes = (
    "Bonds issued at par, so effective rate = stated rate: interest expense equals "
    "cash paid ($45,000 each semiannual period) and the carrying amount stays at "
    "$1,500,000 all of Year 1 with no amortization. "
    "(e) Because the convertible bonds are dilutive, Riverbend presents a dual "
    "presentation on the face of the Year 1 income statement: basic EPS $3.00 and "
    "diluted EPS $2.77 (both for income from continuing operations and net income, "
    "which are the same here since there are no discontinued operations). "
    "(g) Under the July 1 alternate, only six months of interest was charged against "
    "income, so only the six-month after-tax interest ($33,750) is added back, and "
    "the 45,000 conversion shares are weighted 6/12 = 22,500; diluted EPS $3.00 is "
    "below basic EPS $3.14, so the bonds remain dilutive. "
    "Part (b)'s schedule and part (d)/(g)'s reconciliation lines are reported above "
    "because those parts explicitly require the schedules themselves."
)

result = {
    "id": "agent_251#00",
    "rounding_convention": (
        "decimal.Decimal throughout; money rounded to the cent with ROUND_HALF_UP "
        "per period (each semiannual line rounded on its own, never from an annual "
        "total); EPS rounded to the cent with ROUND_HALF_UP from exact unrounded "
        "numerator/denominator; no PV table factors needed because the bonds are "
        "issued at par (effective rate = stated rate, no amortization)"
    ),
    "answers": answers,
    "journal_entries": [je_a, je_b_jun, je_b_dec, je_f],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
