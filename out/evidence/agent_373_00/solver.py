#!/usr/bin/env python3
"""Blind solver for item agent_373#00 — SummitRidge Packaging Corp. stock dividends / split.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, applied per computed amount, to the cent (2 dp) for all money and
to the whole share for share counts. Every figure in this fact pattern happens to
land exactly on a whole dollar / whole share, so the quantizer is a guard rather
than a rounding decision. No present-value factors are involved. All money is
carried in decimal.Decimal; floats are never used.

Par value per share after the Scenario C split is quantized to 2 dp
($3.00 / 2 = $1.50) using the same ROUND_HALF_UP rule.

DERIVATION NOTES (all from the stem, nothing hard-coded downstream)
-------------------------------------------------------------------
Given Dec 15, Year 1 balances: 60,000 shares of $3 par common ($180,000),
PIC in excess of par $540,000, Retained Earnings $750,000, total equity
$1,470,000. Market price $22/share.

Scenario A (12% = SMALL stock dividend, < 20-25%): measured at FAIR VALUE on the
declaration date. Retained Earnings is charged for total fair value; Common Stock
Dividends Distributable (CSDD) is credited at PAR; the excess goes to PIC in
excess of par.

Scenario B (50% = LARGE stock dividend / split effected as a dividend, > 20-25%):
measured at PAR. Retained Earnings is charged for par only; CSDD credited at par;
no PIC effect.

CSDD is NOT a liability — it is an equity account, presented in the paid-in
capital section of stockholders' equity (an addition to contributed capital).
No December 31 adjusting entry is required for a declared-but-undistributed stock
dividend; the declaration entry already recorded the full effect.

Scenario C (true 2-for-1 split by reducing par): memorandum only, NO journal
entry. Shares double, par per share halves, total Common Stock dollar amount and
total stockholders' equity are unchanged.

Convention: the declaration debit is presented as "Retained Earnings". A course
that uses a temporary "Stock Dividends" account would substitute that title; the
amount and the closing effect on Retained Earnings are identical.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")
ONE = Decimal("1")


def money(x: Decimal) -> Decimal:
    """Quantize to the cent, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def shares(x: Decimal) -> Decimal:
    """Quantize to a whole share, ROUND_HALF_UP (stem: no fractional shares)."""
    return Decimal(x).quantize(ONE, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly: int when integral, else float of the exact 2dp Decimal."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ----------------------------------------------------------------------------
# Given facts (Dec 15, Year 1, before any dividend or split action)
# ----------------------------------------------------------------------------
PAR_PER_SHARE = Decimal("3")
SHARES_OUT_0 = Decimal("60000")
COMMON_STOCK_0 = Decimal("180000")
PIC_EXCESS_0 = Decimal("540000")
RETAINED_EARNINGS_0 = Decimal("750000")
TOTAL_EQUITY_0 = Decimal("1470000")
MARKET_PRICE = Decimal("22")

SMALL_DIV_PCT = Decimal("0.12")   # Scenario A
LARGE_DIV_PCT = Decimal("0.50")   # Scenario B
SPLIT_RATIO = Decimal("2")        # Scenario C, 2-for-1

# Internal consistency of the given trial balance (guard, not an answer).
assert COMMON_STOCK_0 == money(SHARES_OUT_0 * PAR_PER_SHARE)
assert TOTAL_EQUITY_0 == money(COMMON_STOCK_0 + PIC_EXCESS_0 + RETAINED_EARNINGS_0)

# ----------------------------------------------------------------------------
# Scenario A — 12% SMALL stock dividend, measured at fair value
# ----------------------------------------------------------------------------
a_shares = shares(SHARES_OUT_0 * SMALL_DIV_PCT)                 # 7,200
a_fair_value = money(a_shares * MARKET_PRICE)                   # RE charge
a_par_amount = money(a_shares * PAR_PER_SHARE)                  # CSDD credit
a_pic_excess = money(a_fair_value - a_par_amount)               # PIC credit

entry_a = {
    "part": "a",
    "date": "Year 1, December 15 (declaration — Scenario A)",
    "lines": [
        {"account": "Retained Earnings (Stock Dividends)",
         "debit": num(a_fair_value), "credit": 0},
        {"account": "Common Stock Dividends Distributable",
         "debit": 0, "credit": num(a_par_amount)},
        {"account": "Paid-in Capital in Excess of Par—Common Stock",
         "debit": 0, "credit": num(a_pic_excess)},
    ],
}

# Part b — no December 31 adjusting entry.
entry_b = {
    "part": "b",
    "date": "Year 1, December 31 (period-end — Scenario A)",
    "lines": [],
    "memo": ("No adjusting journal entry is required. Common Stock Dividends "
             "Distributable is an EQUITY account, reported in the paid-in "
             "capital section of stockholders' equity as an addition to "
             "contributed capital — it is not a liability."),
}

# Part c — equity / share schedule at three dates
# (1) immediately before declaration
c1 = {
    "point": "1. Immediately before declaration (Dec 15, Year 1)",
    "common_stock": money(COMMON_STOCK_0),
    "common_stock_dividends_distributable": money(Decimal("0")),
    "paid_in_capital_in_excess_of_par": money(PIC_EXCESS_0),
    "retained_earnings": money(RETAINED_EARNINGS_0),
    "shares_outstanding": shares(SHARES_OUT_0),
    "par_per_share": money(PAR_PER_SHARE),
}
c1["total_stockholders_equity"] = money(
    c1["common_stock"] + c1["common_stock_dividends_distributable"]
    + c1["paid_in_capital_in_excess_of_par"] + c1["retained_earnings"])

# (2) December 31, Year 1 — after declaration, before distribution
c2 = {
    "point": "2. December 31, Year 1 (after declaration, before distribution)",
    "common_stock": money(COMMON_STOCK_0),                       # unchanged
    "common_stock_dividends_distributable": money(a_par_amount),
    "paid_in_capital_in_excess_of_par": money(PIC_EXCESS_0 + a_pic_excess),
    "retained_earnings": money(RETAINED_EARNINGS_0 - a_fair_value),
    "shares_outstanding": shares(SHARES_OUT_0),                  # not yet issued
    "par_per_share": money(PAR_PER_SHARE),
}
c2["total_stockholders_equity"] = money(
    c2["common_stock"] + c2["common_stock_dividends_distributable"]
    + c2["paid_in_capital_in_excess_of_par"] + c2["retained_earnings"])

# (3) after distribution on January 12, Year 2
c3 = {
    "point": "3. After distribution (January 12, Year 2)",
    "common_stock": money(COMMON_STOCK_0 + a_par_amount),
    "common_stock_dividends_distributable": money(Decimal("0")),
    "paid_in_capital_in_excess_of_par": money(PIC_EXCESS_0 + a_pic_excess),
    "retained_earnings": money(RETAINED_EARNINGS_0 - a_fair_value),
    "shares_outstanding": shares(SHARES_OUT_0 + a_shares),
    "par_per_share": money(PAR_PER_SHARE),
}
c3["total_stockholders_equity"] = money(
    c3["common_stock"] + c3["common_stock_dividends_distributable"]
    + c3["paid_in_capital_in_excess_of_par"] + c3["retained_earnings"])

# A stock dividend never changes total equity — guard, not an answer.
for blk in (c1, c2, c3):
    assert blk["total_stockholders_equity"] == money(TOTAL_EQUITY_0)
assert c3["common_stock"] == money(c3["shares_outstanding"] * PAR_PER_SHARE)

# Part d — January 12, Year 2 distribution (settlement)
entry_d = {
    "part": "d",
    "date": "Year 2, January 12 (distribution — Scenario A)",
    "lines": [
        {"account": "Common Stock Dividends Distributable",
         "debit": num(a_par_amount), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(a_par_amount)},
    ],
}

# ----------------------------------------------------------------------------
# Scenario B — 50% LARGE stock dividend, measured at PAR
# ----------------------------------------------------------------------------
b_shares = shares(SHARES_OUT_0 * LARGE_DIV_PCT)                 # 30,000
b_par_amount = money(b_shares * PAR_PER_SHARE)                  # RE charge = par

entry_e1 = {
    "part": "e",
    "date": "Year 1, December 15 (declaration — Scenario B, at par)",
    "lines": [
        {"account": "Retained Earnings (Stock Dividends)",
         "debit": num(b_par_amount), "credit": 0},
        {"account": "Common Stock Dividends Distributable",
         "debit": 0, "credit": num(b_par_amount)},
    ],
}
entry_e2 = {
    "part": "e",
    "date": "Year 2, January 12 (distribution — Scenario B)",
    "lines": [
        {"account": "Common Stock Dividends Distributable",
         "debit": num(b_par_amount), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(b_par_amount)},
    ],
}

b_shares_end = shares(SHARES_OUT_0 + b_shares)
b_common_stock_end = money(COMMON_STOCK_0 + b_par_amount)
b_pic_end = money(PIC_EXCESS_0)                                 # untouched
b_re_end = money(RETAINED_EARNINGS_0 - b_par_amount)
b_total_equity_end = money(b_common_stock_end + b_pic_end + b_re_end)

assert b_common_stock_end == money(b_shares_end * PAR_PER_SHARE)
assert b_total_equity_end == money(TOTAL_EQUITY_0)

# ----------------------------------------------------------------------------
# Scenario C — true 2-for-1 split by reducing par: memorandum only
# ----------------------------------------------------------------------------
c_shares_end = shares(SHARES_OUT_0 * SPLIT_RATIO)
c_par_end = money(PAR_PER_SHARE / SPLIT_RATIO)
c_common_stock_end = money(c_shares_end * c_par_end)

assert c_common_stock_end == money(COMMON_STOCK_0)              # unchanged

entry_f = {
    "part": "f",
    "date": "Year 1, December 15 (2-for-1 true split — Scenario C)",
    "lines": [],
    "memo": ("No journal entry. A true stock split effected by reducing par "
             "value is recorded by memorandum only: no account balance changes, "
             "so there is nothing to debit or credit."),
}

# ----------------------------------------------------------------------------
# Debits = credits check on every prepared entry
# ----------------------------------------------------------------------------
journal_entries = [entry_a, entry_b, entry_d, entry_e1, entry_e2, entry_f]
for je in journal_entries:
    dr = sum(Decimal(str(ln["debit"])) for ln in je["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in je["lines"])
    assert dr == cr, f"part {je['part']}: Dr {dr} != Cr {cr}"

# ----------------------------------------------------------------------------
# Answers — only figures the Required parts ask for
# ----------------------------------------------------------------------------
answers = [
    # a — declaration at fair value
    {"label": "a: Scenario A declaration — Dr Retained Earnings (Stock Dividends)",
     "value": num(a_fair_value)},
    {"label": "a: Scenario A declaration — Cr Common Stock Dividends Distributable (at par)",
     "value": num(a_par_amount)},
    {"label": "a: Scenario A declaration — Cr Paid-in Capital in Excess of Par—CS",
     "value": num(a_pic_excess)},

    # b — period-end
    {"label": "b: Number of December 31, Year 1 adjusting journal entries required",
     "value": 0},
    {"label": "b: Classification/presentation of Common Stock Dividends Distributable "
              "at December 31, Year 1",
     "value": "Stockholders' equity — paid-in capital section, an addition to "
              "contributed capital (NOT a liability); reported at par, "
              f"{num(a_par_amount)}"},

    # c — schedule, three points
    {"label": "c(1) before declaration: Common Stock", "value": num(c1["common_stock"])},
    {"label": "c(1) before declaration: Common Stock Dividends Distributable",
     "value": num(c1["common_stock_dividends_distributable"])},
    {"label": "c(1) before declaration: Paid-in Capital in Excess of Par—CS",
     "value": num(c1["paid_in_capital_in_excess_of_par"])},
    {"label": "c(1) before declaration: Retained Earnings", "value": num(c1["retained_earnings"])},
    {"label": "c(1) before declaration: Total stockholders' equity",
     "value": num(c1["total_stockholders_equity"])},
    {"label": "c(1) before declaration: Shares outstanding", "value": int(c1["shares_outstanding"])},
    {"label": "c(1) before declaration: Par per share", "value": num(c1["par_per_share"])},

    {"label": "c(2) December 31, Year 1: Common Stock", "value": num(c2["common_stock"])},
    {"label": "c(2) December 31, Year 1: Common Stock Dividends Distributable",
     "value": num(c2["common_stock_dividends_distributable"])},
    {"label": "c(2) December 31, Year 1: Paid-in Capital in Excess of Par—CS",
     "value": num(c2["paid_in_capital_in_excess_of_par"])},
    {"label": "c(2) December 31, Year 1: Retained Earnings", "value": num(c2["retained_earnings"])},
    {"label": "c(2) December 31, Year 1: Total stockholders' equity",
     "value": num(c2["total_stockholders_equity"])},
    {"label": "c(2) December 31, Year 1: Shares outstanding", "value": int(c2["shares_outstanding"])},
    {"label": "c(2) December 31, Year 1: Par per share", "value": num(c2["par_per_share"])},

    {"label": "c(3) after distribution Jan 12, Year 2: Common Stock", "value": num(c3["common_stock"])},
    {"label": "c(3) after distribution Jan 12, Year 2: Common Stock Dividends Distributable",
     "value": num(c3["common_stock_dividends_distributable"])},
    {"label": "c(3) after distribution Jan 12, Year 2: Paid-in Capital in Excess of Par—CS",
     "value": num(c3["paid_in_capital_in_excess_of_par"])},
    {"label": "c(3) after distribution Jan 12, Year 2: Retained Earnings",
     "value": num(c3["retained_earnings"])},
    {"label": "c(3) after distribution Jan 12, Year 2: Total stockholders' equity",
     "value": num(c3["total_stockholders_equity"])},
    {"label": "c(3) after distribution Jan 12, Year 2: Shares outstanding",
     "value": int(c3["shares_outstanding"])},
    {"label": "c(3) after distribution Jan 12, Year 2: Par per share", "value": num(c3["par_per_share"])},

    # d — settlement
    {"label": "d: Scenario A distribution Jan 12, Year 2 — Dr Common Stock Dividends "
              "Distributable / Cr Common Stock", "value": num(a_par_amount)},

    # e — Scenario B
    {"label": "e: Scenario B declaration — Dr Retained Earnings / Cr CSDD (at par)",
     "value": num(b_par_amount)},
    {"label": "e: Scenario B distribution — Dr CSDD / Cr Common Stock",
     "value": num(b_par_amount)},
    {"label": "e: Scenario B after distribution — Common Stock", "value": num(b_common_stock_end)},
    {"label": "e: Scenario B after distribution — Paid-in Capital in Excess of Par—CS",
     "value": num(b_pic_end)},
    {"label": "e: Scenario B after distribution — Retained Earnings", "value": num(b_re_end)},
    {"label": "e: Scenario B after distribution — Shares outstanding", "value": int(b_shares_end)},
    {"label": "e: Scenario B after distribution — Total stockholders' equity",
     "value": num(b_total_equity_end)},

    # f — Scenario C
    {"label": "f: Scenario C — journal entry required?",
     "value": "None — memorandum entry only for a true stock split"},
    {"label": "f: Scenario C after 2-for-1 split — Shares outstanding", "value": int(c_shares_end)},
    {"label": "f: Scenario C after 2-for-1 split — Par per share", "value": num(c_par_end)},
    {"label": "f: Scenario C after 2-for-1 split — Total Common Stock dollar amount",
     "value": num(c_common_stock_end)},
]

result = {
    "id": "agent_373#00",
    "rounding_convention": (
        "ROUND_HALF_UP per computed amount, to the cent for money and to the "
        "whole share for share counts; decimal.Decimal throughout, no floats. "
        "No PV factors involved. Small stock dividend (12%) measured at "
        "declaration-date fair value; large stock dividend (50%) measured at par."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Scenario A is a small stock dividend (12% < 20-25% threshold), so it is "
        "recorded at fair value: 7,200 shares x $22 = $158,400 charged to Retained "
        "Earnings, split between CSDD at par ($21,600) and PIC in excess of par "
        "($136,800). No Dec 31 adjusting entry is needed; CSDD sits in the paid-in "
        "capital section of stockholders' equity, not in liabilities. Scenario B is "
        "a large stock dividend (50%), recorded at par only: 30,000 shares x $3 = "
        "$90,000, with no PIC effect. Scenario C is a true split -- memorandum only, "
        "no journal entry. Total stockholders' equity stays $1,470,000 in every "
        "scenario at every date. If the course uses a temporary 'Stock Dividends' "
        "account instead of debiting Retained Earnings directly, substitute that "
        "title; the amounts and the ultimate effect on Retained Earnings are the same."
    ),
}

print(json.dumps(result, indent=2, ensure_ascii=False))
