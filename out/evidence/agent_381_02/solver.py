#!/usr/bin/env python3
"""Blind solver — agent_381#02.

Lakeshore Fiber Optics Ltd., calendar Year 1. Simple capital structure
(no convertibles, options, warrants, or NCI). Derives:

  a. April 1 common stock issuance JE (10,000 sh, $1 par, $20 cash)
  b. July 1 treasury stock purchase JE (5,000 sh @ $22, cost method)
  c. October 1 100% (large) stock dividend JE, capitalized at PAR, plus
     shares outstanding immediately before and immediately after
  d. December 10 noncumulative preferred cash dividend declaration + payment
  e. Weighted-average common shares schedule, applying the retroactive
     restatement factor for the 100% stock dividend to ALL periods before
     October 1
  f. Basic EPS schedule

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal. No floats anywhere.
* Rounding is ROUND_HALF_UP, applied per period / per line item (this
  course's convention), never by truncation and never at the very end only.
* Share counts: each period's weighted-average contribution is rounded to
  whole shares with ROUND_HALF_UP before summing (matches the textbook's
  per-row weighted-average table in Ch. 20 LO 20-5, e.g. the 16,917 row).
  Here every period divides evenly, so rounding is a no-op — it is applied
  anyway so the method, not luck, produces the figure.
* Money amounts are carried to cents (2dp).
* Basic EPS is rounded to 2 decimal places (cents per share) with
  ROUND_HALF_UP, computed as a single division of exact income available to
  common by exact weighted-average shares (round-at-end for the per-share
  figure only; its two inputs are already exact whole numbers).
* No present-value factors are involved in this item.

AUTHORITY APPLIED
-----------------
* ASC 505-20-25-2 / 505-20-30-6: a stock dividend large enough to materially
  reduce market price is a stock split in substance -> record at par; fair
  value is NOT used. Market price of $24 on Oct 1 is therefore ignored.
* ASC 260-10-45-10: shares issued and reacquired during the period are
  weighted for the portion of the period outstanding.
* ASC 260-10-55-12: stock dividends/splits are restated retroactively for all
  periods presented, because they generate no new capital -- unlike the
  April 1 cash issuance, which is weighted only from its issuance date.
* Noncumulative preferred: subtract the dividend in the numerator only in the
  year it is DECLARED. It was declared (and paid) on December 10, so the full
  $30,000 is subtracted.

Run: python3 solver.py   ->  prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")
SHARE = Decimal("1")


def money(x: Decimal) -> Decimal:
    """Round a money amount to cents, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def shares(x: Decimal) -> Decimal:
    """Round a share count to whole shares, ROUND_HALF_UP."""
    return Decimal(x).quantize(SHARE, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """Emit a JSON-friendly number: int when integral, else float of the
    already-rounded Decimal (rounding is done in Decimal, never in float)."""
    x = Decimal(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Given fact pattern (transcribed from the stem; nothing else is assumed)
# ---------------------------------------------------------------------------
COMMON_PAR = Decimal("1")
COMMON_BEGIN = Decimal("50000")

PFD_SHARES = Decimal("5000")
PFD_PAR = Decimal("100")
PFD_RATE = Decimal("0.06")

APR_SHARES_ISSUED = Decimal("10000")
APR_PRICE = Decimal("20")

JUL_TS_SHARES = Decimal("5000")
JUL_TS_COST = Decimal("22")

OCT_DIVIDEND_PCT = Decimal("1.00")          # 100% large stock dividend
OCT_MARKET_PRICE = Decimal("24")            # context only; NOT used (par capitalization)

DEC_PFD_DIVIDEND_DECLARED = Decimal("30000")

NET_INCOME = Decimal("360000")

MONTHS_IN_YEAR = Decimal("12")

# ---------------------------------------------------------------------------
# (a) April 1 — issue 10,000 common shares, $1 par, for $20 cash
# ---------------------------------------------------------------------------
apr_cash = money(APR_SHARES_ISSUED * APR_PRICE)
apr_common_stock = money(APR_SHARES_ISSUED * COMMON_PAR)
apr_apic = money(apr_cash - apr_common_stock)

entry_a = {
    "part": "a",
    "date": "April 1",
    "description": "Issue 10,000 shares of $1 par common stock for $20 cash per share",
    "lines": [
        {"account": "Cash", "debit": num(apr_cash), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(apr_common_stock)},
        {"account": "Paid-In Capital in Excess of Par-Common Stock",
         "debit": 0, "credit": num(apr_apic)},
    ],
}

# ---------------------------------------------------------------------------
# (b) July 1 — buy 5,000 common shares for treasury at $22 (cost method)
# ---------------------------------------------------------------------------
jul_cost = money(JUL_TS_SHARES * JUL_TS_COST)

entry_b = {
    "part": "b",
    "date": "July 1",
    "description": "Purchase 5,000 common shares for the treasury at $22 cash per share (cost method)",
    "lines": [
        {"account": "Treasury Stock", "debit": num(jul_cost), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(jul_cost)},
    ],
}

# ---------------------------------------------------------------------------
# Share counts through the year (OUTSTANDING = issued less treasury)
# ---------------------------------------------------------------------------
sh_jan = COMMON_BEGIN                                   # 50,000
sh_apr = sh_jan + APR_SHARES_ISSUED                     # 60,000
sh_jul = sh_apr - JUL_TS_SHARES                         # 55,000  (treasury shares are not outstanding)

# ---------------------------------------------------------------------------
# (c) October 1 — 100% large stock dividend, capitalized at par
# ---------------------------------------------------------------------------
shares_before_dividend = sh_jul
dividend_shares_issued = shares(shares_before_dividend * OCT_DIVIDEND_PCT)
shares_after_dividend = shares_before_dividend + dividend_shares_issued

# Large stock dividend (stock split effected in the form of a dividend):
# capitalize PAR of the shares issued. Fair value ($24) is deliberately unused.
oct_capitalized = money(dividend_shares_issued * COMMON_PAR)
assert OCT_MARKET_PRICE not in (oct_capitalized,), "market price must not drive the entry"

entry_c = {
    "part": "c",
    "date": "October 1",
    "description": (
        "Distribute 100% large common stock dividend (stock split effected in the form of a "
        "dividend): capitalize par of the {:,} shares issued. Declaration and distribution occur "
        "on the same date, so the entry is shown combined; equivalently, credit Common Stock "
        "Dividends Distributable on declaration and reclassify it to Common Stock on "
        "distribution.".format(int(dividend_shares_issued))
    ),
    "lines": [
        {"account": "Retained Earnings", "debit": num(oct_capitalized), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(oct_capitalized)},
    ],
}

# ---------------------------------------------------------------------------
# (d) December 10 — declare and immediately pay preferred cash dividend
# ---------------------------------------------------------------------------
pfd_stated_annual = money(PFD_SHARES * PFD_PAR * PFD_RATE)   # 5,000 x $100 x 6% = $30,000
# Cross-check the stem's stated $30,000 against the stated rate; they agree.
assert pfd_stated_annual == DEC_PFD_DIVIDEND_DECLARED, (
    "stated preferred rate does not reproduce the declared amount"
)
pfd_dividend = pfd_stated_annual

entry_d = {
    "part": "d",
    "date": "December 10",
    "description": (
        "Declare and immediately pay the full stated annual dividend on 5,000 shares of 6%, $100 "
        "par noncumulative preferred stock (declaration and payment combined; no common cash "
        "dividend declared)"
    ),
    "lines": [
        {"account": "Retained Earnings (Preferred Dividends)",
         "debit": num(pfd_dividend), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(pfd_dividend)},
    ],
}

# ---------------------------------------------------------------------------
# (e) Weighted-average common shares, with retroactive restatement
# ---------------------------------------------------------------------------
# ASC 260-10-55-12: the 100% stock dividend is treated as if it occurred at the
# beginning of the year, so every period BEFORE October 1 is multiplied by the
# retroactive restatement factor. Factor = 1 + 100% = 2.00.
RESTATEMENT_FACTOR = Decimal("1") + OCT_DIVIDEND_PCT   # 2.00

wa_periods = [
    # (label, actual shares outstanding, restatement factor, months)
    ("Jan 1 - Mar 31", sh_jan, RESTATEMENT_FACTOR, Decimal("3")),
    ("Apr 1 - Jun 30", sh_apr, RESTATEMENT_FACTOR, Decimal("3")),
    ("Jul 1 - Sep 30", sh_jul, RESTATEMENT_FACTOR, Decimal("3")),
    ("Oct 1 - Dec 31", shares_after_dividend, Decimal("1"), Decimal("3")),
]

wa_schedule = []
weighted_average_shares = Decimal("0")
months_check = Decimal("0")
for label, actual, factor, months in wa_periods:
    equivalent = shares(actual * factor)
    fraction = months / MONTHS_IN_YEAR
    contribution = shares(equivalent * fraction)   # ROUND_HALF_UP per period
    weighted_average_shares += contribution
    months_check += months
    wa_schedule.append({
        "period": label,
        "actual_shares_outstanding": num(actual),
        "retroactive_restatement": num(factor),
        "equivalent_shares_outstanding": num(equivalent),
        "months_outstanding": num(months),
        "fraction_of_year": "{}/12".format(int(months)),
        "weighted_average_shares": num(contribution),
    })

assert months_check == MONTHS_IN_YEAR, "weighted-average periods must span 12 months"
# The Oct 1 restated count must tie to the actual post-dividend count.
assert shares(sh_jul * RESTATEMENT_FACTOR) == shares_after_dividend

# ---------------------------------------------------------------------------
# (f) Basic EPS
# ---------------------------------------------------------------------------
# Noncumulative preferred: subtract only because it was DECLARED this year.
income_available_to_common = money(NET_INCOME - pfd_dividend)
basic_eps = (income_available_to_common / weighted_average_shares).quantize(
    CENTS, rounding=ROUND_HALF_UP
)

# ---------------------------------------------------------------------------
# Integrity: every entry must balance
# ---------------------------------------------------------------------------
journal_entries = [entry_a, entry_b, entry_c, entry_d]
for e in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert dr == cr, "part {} does not balance: {} != {}".format(e["part"], dr, cr)

# ---------------------------------------------------------------------------
# Output — only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "c: common shares outstanding immediately BEFORE the 100% stock dividend",
     "value": num(shares_before_dividend)},
    {"label": "c: common shares outstanding immediately AFTER the 100% stock dividend",
     "value": num(shares_after_dividend)},
    {"label": "e: weighted-average common shares outstanding for Year 1",
     "value": num(weighted_average_shares)},
    {"label": "f: net income available to common stockholders",
     "value": num(income_available_to_common)},
    {"label": "f: basic earnings per share",
     "value": num(basic_eps)},
]

notes = (
    "e schedule (actual shares x retroactive restatement factor {factor} for all periods before "
    "Oct 1 x fraction of year): {rows}; total {wa} weighted-average shares. "
    "f explanation: the noncumulative preferred dividend is subtracted because basic EPS measures "
    "income available to COMMON stockholders, and the ${pfd} was actually declared in Year 1 (for "
    "noncumulative preferred only declared dividends are deducted -- had none been declared, "
    "nothing would be subtracted). The Oct 1 stock dividend differs from the April 1 cash "
    "issuance because it raised no new capital and merely re-denominated existing ownership, so it "
    "is restated retroactively to the start of the year (and to all prior periods presented), "
    "while the April issuance brought in ${cash} of new capital and is therefore weighted only "
    "from April 1 forward. Market price of $24 on Oct 1 is disclosed for context and is not used: "
    "a large stock dividend is a stock split in substance and is capitalized at par."
).format(
    factor=num(RESTATEMENT_FACTOR),
    rows="; ".join(
        "{} {} x {} = {} x {} = {}".format(
            r["period"], r["actual_shares_outstanding"], r["retroactive_restatement"],
            r["equivalent_shares_outstanding"], r["fraction_of_year"],
            r["weighted_average_shares"])
        for r in wa_schedule
    ),
    wa=num(weighted_average_shares),
    pfd=num(pfd_dividend),
    cash=num(apr_cash),
)

result = {
    "id": "agent_381#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats. ROUND_HALF_UP applied per period/per line: share "
        "contributions rounded to whole shares each period before summing; money to cents; basic "
        "EPS rounded to 2 decimals. No PV factors in this item. Large stock dividend capitalized "
        "at par (fair value ignored per ASC 505-20)."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
