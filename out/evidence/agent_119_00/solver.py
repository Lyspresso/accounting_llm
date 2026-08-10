#!/usr/bin/env python3
"""Blind solver for item agent_119#00 - Northlake Precision Inc. (LO 20-5).

Topic: share issuance / treasury buyback / cumulative preferred dividend /
large stock dividend journal entries, weighted-average common shares with
retroactive restatement, basic EPS, and income-statement presentation.

ROUNDING CONVENTION
-------------------
    ROUND_HALF_UP, applied once, at the end of each reported figure.

  * All money is decimal.Decimal. No floats anywhere in this module.
  * Share counts and dollar amounts in this fact pattern are exact integers:
    every journal-entry amount, the weighted-average share schedule, and
    income available to common stockholders come out whole with no rounding
    applied at all. Dollar figures are quantized to 0.01 for presentation.
  * The only genuinely inexact figure is basic EPS
    (366,000 / 167,400 = 2.186379...). It is computed from the UNROUNDED
    numerator and UNROUNDED denominator and quantized ONCE to the nearest
    cent with ROUND_HALF_UP, as part (c) directs ("round EPS to the nearest
    cent"). There is no round-per-period step here because EPS is a single
    annual computation; the weighted-average denominator is accumulated at
    full precision before the division.
  * No present-value factors are involved in this item.

DERIVATION NOTES (all figures below are computed, none are hard-coded)
----------------------------------------------------------------------
  * Preferred is cumulative, 8,000 sh x $25 par x 6% = full annual claim,
    declared AND paid Sept 30, so it is subtracted from net income in the
    basic-EPS numerator (ch. 20 handout: subtract preferred dividends that
    are either declared, or undeclared and going into arrears).
  * Treasury shares are not outstanding. They neither count in the EPS
    denominator from July 1 nor participate in the Nov 1 stock dividend, so
    the stock dividend is 20% of the 144,000 shares outstanding on Nov 1.
  * Large stock dividend (>20-25% threshold, and the stem directs it): debit
    Retained Earnings at PAR, not at the $18 market price. The $18 market
    price is therefore a distractor and is deliberately unused.
  * Retroactive restatement: the 1.20 stock-dividend factor is applied to
    every period BEFORE Nov 1, per the ch. 20 handout worked example.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 34

CENT = Decimal("0.01")


def money(d: Decimal) -> Decimal:
    """Quantize a dollar amount to the cent, ROUND_HALF_UP."""
    return d.quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """Render a Decimal as a JSON number: int when integral, else float-free str->float."""
    d = d.normalize()
    if d == d.to_integral_value():
        return int(d)
    # json needs a number; Decimal is exact here and only ever has 2 dp.
    return float(d)


# ---------------------------------------------------------------------------
# Given fact pattern (stem only)
# ---------------------------------------------------------------------------
COMMON_SHARES_JAN1 = Decimal("120000")
COMMON_PAR = Decimal("2")

PREF_SHARES = Decimal("8000")
PREF_RATE = Decimal("0.06")
PREF_PAR = Decimal("25")

NET_INCOME = Decimal("378000")

APR1_SHARES_ISSUED = Decimal("30000")
APR1_PRICE = Decimal("14")

JUL1_TREASURY_SHARES = Decimal("6000")
JUL1_COST = Decimal("16")

NOV1_STOCK_DIV_PCT = Decimal("0.20")
NOV1_MARKET_PRICE = Decimal("18")  # distractor: large stock dividend -> par

MONTHS_IN_YEAR = Decimal("12")


# ---------------------------------------------------------------------------
# (a) Initial recognition journal entries
# ---------------------------------------------------------------------------

# April 1 - issuance of 30,000 common shares at $14
apr1_cash = APR1_SHARES_ISSUED * APR1_PRICE
apr1_common_stock = APR1_SHARES_ISSUED * COMMON_PAR
apr1_apic = apr1_cash - apr1_common_stock

# July 1 - treasury buyback, cost method
jul1_treasury = JUL1_TREASURY_SHARES * JUL1_COST

# September 30 - full annual cumulative preferred claim, declared and paid
pref_annual_dividend = PREF_SHARES * PREF_PAR * PREF_RATE

# November 1 - 20% LARGE stock dividend on shares OUTSTANDING, recorded at par
shares_out_after_apr1 = COMMON_SHARES_JAN1 + APR1_SHARES_ISSUED
shares_out_after_jul1 = shares_out_after_apr1 - JUL1_TREASURY_SHARES
nov1_dividend_shares = shares_out_after_jul1 * NOV1_STOCK_DIV_PCT
nov1_stock_dividend_amount = nov1_dividend_shares * COMMON_PAR
shares_out_after_nov1 = shares_out_after_jul1 + nov1_dividend_shares

journal_entries = [
    {
        "part": "a",
        "date": "2025-04-01",
        "description": "Issued 30,000 common shares for cash at $14",
        "lines": [
            {"account": "Cash", "debit": money(apr1_cash), "credit": money(Decimal(0))},
            {"account": "Common Stock", "debit": money(Decimal(0)),
             "credit": money(apr1_common_stock)},
            {"account": "Paid-in Capital in Excess of Par - Common",
             "debit": money(Decimal(0)), "credit": money(apr1_apic)},
        ],
    },
    {
        "part": "a",
        "date": "2025-07-01",
        "description": "Purchased 6,000 treasury shares at $16 (cost method)",
        "lines": [
            {"account": "Treasury Stock", "debit": money(jul1_treasury),
             "credit": money(Decimal(0))},
            {"account": "Cash", "debit": money(Decimal(0)),
             "credit": money(jul1_treasury)},
        ],
    },
    {
        "part": "a",
        "date": "2025-09-30",
        "description": "Declared and paid full annual cumulative preferred dividend "
                       "(8,000 sh x $25 par x 6%)",
        "lines": [
            {"account": "Retained Earnings (Cash Dividends - Preferred)",
             "debit": money(pref_annual_dividend), "credit": money(Decimal(0))},
            {"account": "Cash", "debit": money(Decimal(0)),
             "credit": money(pref_annual_dividend)},
        ],
    },
    {
        "part": "a",
        "date": "2025-11-01",
        "description": "Declared and distributed 20% large common stock dividend "
                       "(144,000 sh outstanding x 20% = 28,800 sh) recorded at $2 par",
        "lines": [
            {"account": "Retained Earnings (Stock Dividends)",
             "debit": money(nov1_stock_dividend_amount), "credit": money(Decimal(0))},
            {"account": "Common Stock", "debit": money(Decimal(0)),
             "credit": money(nov1_stock_dividend_amount)},
        ],
    },
]

# Dr = Cr proof for every entry
for je in journal_entries:
    dr = sum((ln["debit"] for ln in je["lines"]), Decimal(0))
    cr = sum((ln["credit"] for ln in je["lines"]), Decimal(0))
    assert dr == cr, f"Entry {je['date']} out of balance: {dr} != {cr}"


# ---------------------------------------------------------------------------
# (b) Weighted-average common shares schedule, with retroactive restatement
# ---------------------------------------------------------------------------
restate = Decimal("1") + NOV1_STOCK_DIV_PCT  # 1.20, applied to all pre-Nov-1 periods

schedule = [
    ("Jan 1 - Apr 1", COMMON_SHARES_JAN1, restate, Decimal("3")),
    ("Apr 1 - Jul 1", shares_out_after_apr1, restate, Decimal("3")),
    ("Jul 1 - Nov 1", shares_out_after_jul1, restate, Decimal("4")),
    ("Nov 1 - Dec 31", shares_out_after_nov1, Decimal("1"), Decimal("2")),
]

schedule_rows = []
weighted_average_shares = Decimal(0)
for label, shares, factor, months in schedule:
    weighted = shares * factor * months / MONTHS_IN_YEAR
    weighted_average_shares += weighted
    schedule_rows.append({
        "dates": label,
        "shares_outstanding": num(shares),
        "restatement": num(factor),
        "fraction_of_year": f"{int(months)}/12",
        "weighted_average_shares": num(weighted),
    })

# Cross-check: restating the un-restated weighted average must give the same total.
_unrestated = (COMMON_SHARES_JAN1 * Decimal("3")
               + shares_out_after_apr1 * Decimal("3")
               + shares_out_after_jul1 * Decimal("6")) / MONTHS_IN_YEAR
assert _unrestated * restate == weighted_average_shares, "WAS cross-check failed"


# ---------------------------------------------------------------------------
# (c) Income available to common stockholders and basic EPS
# ---------------------------------------------------------------------------
income_available_to_common = NET_INCOME - pref_annual_dividend

basic_eps_exact = income_available_to_common / weighted_average_shares
basic_eps = basic_eps_exact.quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
answers = [
    {"label": "b: weighted-average common shares outstanding for 2025",
     "value": num(weighted_average_shares)},
    {"label": "c: income available to common stockholders",
     "value": num(money(income_available_to_common))},
    {"label": "c: basic earnings per share",
     "value": num(basic_eps)},
    {"label": "d: basic EPS as presented on the 2025 income statement "
              "(single line, 'Earnings per common share')",
     "value": num(basic_eps)},
]

notes = (
    "PART b SCHEDULE: "
    + "; ".join(
        f"{r['dates']}: {r['shares_outstanding']:,} x {r['restatement']} x "
        f"{r['fraction_of_year']} = {r['weighted_average_shares']:,}"
        for r in schedule_rows
    )
    + f"; total = {int(weighted_average_shares):,} shares. "
    "PART d PRESENTATION: a simple capital structure presents ONE EPS figure on "
    "the face of the income statement, immediately below net income: "
    f"'Earnings per common share .......... ${basic_eps}'. Because there are no "
    "discontinued operations, no per-share subtotals are required, and diluted "
    "EPS is not presented. "
    "PART e EXPLANATION: the April 1 cash issuance brought new assets into the "
    "company, so those shares are weighted only from April 1 forward - the "
    "company had that capital for 9 months, not 12. The November 1 stock "
    "dividend brought in nothing: it merely re-sliced the same pie, so every "
    "shareholder's proportionate interest and the company's resources are "
    "unchanged. Weighting the new shares from November 1 would depress EPS "
    "without any economic cause and would destroy comparability with prior "
    "years, so the 1.20 factor is applied retroactively to every period before "
    "the dividend, as if those shares had always been outstanding. "
    "STOCK-DIVIDEND BASE: the 28,800 dividend shares are 20% of the 144,000 "
    "shares OUTSTANDING on Nov 1; treasury shares do not receive dividends. "
    "The $18 Nov 1 market price is a distractor - a LARGE stock dividend is "
    "recorded at par ($2), not at fair value. "
    "Preferred is cumulative and the full annual claim was declared and paid, "
    "so exactly one year of preferred dividends is subtracted in the numerator; "
    "no arrearages exist."
)

out = {
    "id": "agent_119#00",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats. ROUND_HALF_UP applied once at "
        "the end. Journal-entry amounts and the weighted-average share schedule "
        "are exact integers (no rounding occurs). Basic EPS is computed from the "
        "unrounded numerator and unrounded weighted-average denominator and "
        "quantized once to the nearest cent with ROUND_HALF_UP. No PV factors "
        "in this item."
    ),
    "answers": answers,
    "journal_entries": [
        {
            "part": je["part"],
            "date": je["date"],
            "description": je["description"],
            "lines": [
                {"account": ln["account"],
                 "debit": num(ln["debit"]),
                 "credit": num(ln["credit"])}
                for ln in je["lines"]
            ],
        }
        for je in journal_entries
    ],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
