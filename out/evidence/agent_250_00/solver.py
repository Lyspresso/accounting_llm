#!/usr/bin/env python3
"""Solver for item agent_250#00 -- Pinecrest Logistics Corp. (LO 20-5).

Topic: weighted-average common shares outstanding with a mid-year treasury
buyback and a mid-year cash issuance, retroactively restated for an October 1
2-for-1 stock split; basic EPS with a cumulative-preferred numerator reduction;
plus the related journal entries.

ROUNDING CONVENTION
-------------------
* All monetary amounts use ``decimal.Decimal`` exclusively -- no floats anywhere.
* ROUND_HALF_UP is applied per period / per computed figure (never a single
  round-at-the-end sweep), matching the ACCOUNT-343 course convention.
* Money is carried and reported at 2 decimal places (cents).
* Share counts are whole shares, quantized to 0 decimal places with
  ROUND_HALF_UP. Each row of the weighted-average schedule is rounded to whole
  shares *as that row is computed* (round-per-period), then the rounded rows are
  summed to give the denominator. Here every row divides evenly, so the
  per-period convention and a round-at-end convention agree.
* Per-share amounts (EPS) are rounded to 2 decimal places with ROUND_HALF_UP.
* Time weighting uses exact month fractions n/12 as Decimal ratios (the course's
  table method: Dates | Shares Outstanding | Restatement | Fraction of Year).
  No PV table factors are involved in this item.

METHOD NOTES
------------
* Cumulative preferred: the annual preferred dividend claim is subtracted from
  net income in the basic EPS numerator whether or not it was declared, because
  undeclared cumulative dividends go into arrears (CH 20 handout, BEPS
  numerator).
* Stock split: the restatement factor of 2.0 is applied to every period
  *before* October 1 so the additional split shares are treated as outstanding
  from the beginning of the period. A split under the memorandum method
  produces no journal entry.

Run:  python3 solver.py   ->  prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")
SHARE = Decimal("1")


def money(x: Decimal) -> Decimal:
    """Round a monetary amount to cents, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def shares(x: Decimal) -> Decimal:
    """Round a share count to whole shares, ROUND_HALF_UP (applied per period)."""
    return Decimal(x).quantize(SHARE, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly number: int when integral, else float of the exact Decimal."""
    d = Decimal(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Fact pattern (transcribed from the stem -- nothing below is a hard-coded answer)
# ---------------------------------------------------------------------------
COMMON_SHARES_JAN1 = Decimal("100000")
COMMON_PAR = Decimal("2")

PREF_SHARES = Decimal("5000")
PREF_PAR = Decimal("20")
PREF_RATE = Decimal("0.08")          # 8%, cumulative
PREF_DIVIDENDS_DECLARED = False       # none declared in Year 1

TREASURY_SHARES = Decimal("4000")     # March 31, cost method
TREASURY_PRICE = Decimal("15")

ISSUED_SHARES = Decimal("20000")      # July 1, cash issuance
ISSUE_PRICE = Decimal("12")

SPLIT_FACTOR = Decimal("2")           # October 1, 2-for-1 split, memorandum only

NET_INCOME = Decimal("436000")

MONTHS_IN_YEAR = Decimal("12")

# ---------------------------------------------------------------------------
# (a) March 31 -- treasury stock repurchase (cost method)
# ---------------------------------------------------------------------------
treasury_cost = money(TREASURY_SHARES * TREASURY_PRICE)

je_a = {
    "part": "a",
    "description": "March 31 - repurchase 4,000 common shares for the treasury at $15 cash (cost method)",
    "lines": [
        {"account": "Treasury Stock", "debit": num(treasury_cost), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(treasury_cost)},
    ],
}

# ---------------------------------------------------------------------------
# (b) July 1 -- initial recognition of the cash common stock issuance
# ---------------------------------------------------------------------------
cash_received = money(ISSUED_SHARES * ISSUE_PRICE)
common_stock_at_par = money(ISSUED_SHARES * COMMON_PAR)
apic_common = money(cash_received - common_stock_at_par)

je_b = {
    "part": "b",
    "description": "July 1 - issue 20,000 shares of $2 par common stock for $12 cash per share",
    "lines": [
        {"account": "Cash", "debit": num(cash_received), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(common_stock_at_par)},
        {
            "account": "Paid-in Capital in Excess of Par - Common Stock",
            "debit": 0,
            "credit": num(apic_common),
        },
    ],
}

# ---------------------------------------------------------------------------
# (c) October 1 -- 2-for-1 stock split treatment
# ---------------------------------------------------------------------------
split_treatment = (
    "Memorandum entry only - no journal entry. A 2-for-1 stock split under the "
    "memorandum method doubles the shares outstanding and halves the par value "
    "per share ($2 par to $1 par); total contributed capital, retained earnings, "
    "and total stockholders' equity are unchanged, so no formal equity transfer "
    "is recorded. Memo: 100,000 -> 200,000 issued equivalent; 116,000 -> 232,000 "
    "shares outstanding; par $2.00 -> $1.00."
)
par_after_split = money(COMMON_PAR / SPLIT_FACTOR)

# ---------------------------------------------------------------------------
# (d) Weighted-average common shares outstanding schedule
#     Restatement factor 2.0 applied to every period BEFORE the Oct 1 split.
# ---------------------------------------------------------------------------
outstanding_jan1 = COMMON_SHARES_JAN1                              # 100,000
outstanding_after_buyback = outstanding_jan1 - TREASURY_SHARES     # 96,000
outstanding_after_issue = outstanding_after_buyback + ISSUED_SHARES  # 116,000
outstanding_after_split = outstanding_after_issue * SPLIT_FACTOR   # 232,000

wa_rows = [
    ("Jan 1 - Mar 31", outstanding_jan1, SPLIT_FACTOR, Decimal("3")),
    ("Mar 31 - Jul 1", outstanding_after_buyback, SPLIT_FACTOR, Decimal("3")),
    ("Jul 1 - Oct 1", outstanding_after_issue, SPLIT_FACTOR, Decimal("3")),
    ("Oct 1 - Dec 31", outstanding_after_split, Decimal("1"), Decimal("3")),
]

wa_schedule = []
weighted_average_shares = Decimal("0")
for label, out_shares, restatement, months in wa_rows:
    fraction = months / MONTHS_IN_YEAR
    row_weighted = shares(out_shares * restatement * fraction)  # round per period
    weighted_average_shares += row_weighted
    wa_schedule.append(
        {
            "dates": label,
            "shares_outstanding": num(out_shares),
            "restatement": num(restatement),
            "fraction_of_year": f"{int(months)}/12",
            "weighted_average_shares": num(row_weighted),
        }
    )

weighted_average_shares = shares(weighted_average_shares)

# ---------------------------------------------------------------------------
# (e) Basic EPS computation schedule
# ---------------------------------------------------------------------------
preferred_dividend_claim = money(PREF_SHARES * PREF_PAR * PREF_RATE)
# Cumulative preferred: subtract the current-year claim even though undeclared
# (it goes into arrears), per the CH 20 BEPS numerator rule.
beps_numerator = money(NET_INCOME - preferred_dividend_claim)
basic_eps = (beps_numerator / weighted_average_shares).quantize(
    CENTS, rounding=ROUND_HALF_UP
)

# ---------------------------------------------------------------------------
# (f) December 31 -- closing entry transferring net income to retained earnings
# ---------------------------------------------------------------------------
je_f = {
    "part": "f",
    "description": "December 31 - close Income Summary to Retained Earnings",
    "lines": [
        {"account": "Income Summary", "debit": num(money(NET_INCOME)), "credit": 0},
        {"account": "Retained Earnings", "debit": 0, "credit": num(money(NET_INCOME))},
    ],
}

# ---------------------------------------------------------------------------
# Balance check: every entry must have Dr = Cr
# ---------------------------------------------------------------------------
journal_entries = [je_a, je_b, je_f]
for entry in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert dr == cr, f"Part {entry['part']} does not balance: Dr {dr} vs Cr {cr}"

# ---------------------------------------------------------------------------
# Output -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    # (c) split treatment
    {"label": "c: October 1 2-for-1 stock split accounting treatment", "value": split_treatment},
    {"label": "c: par value per common share after the split", "value": num(par_after_split)},
    # (d) weighted-average schedule
    {
        "label": "d: weighted-average common shares outstanding schedule (restatement 2.0 pre-split)",
        "value": wa_schedule,
    },
    {
        "label": "d: weighted-average common shares outstanding, Year 1",
        "value": num(weighted_average_shares),
    },
    # (e) basic EPS schedule
    {
        "label": "e: preferred dividend claim (cumulative, undeclared - in arrears)",
        "value": num(preferred_dividend_claim),
    },
    {
        "label": "e: basic EPS numerator - net income available to common stockholders",
        "value": num(beps_numerator),
    },
    {"label": "e: basic EPS denominator - weighted-average common shares", "value": num(weighted_average_shares)},
    {"label": "e: basic earnings per share", "value": num(basic_eps)},
    # (g) income statement presentation
    {"label": "g: net income presented on the Year 1 income statement", "value": num(money(NET_INCOME))},
    {"label": "g: basic earnings per share presented on the Year 1 income statement", "value": num(basic_eps)},
]

result = {
    "id": "agent_250#00",
    "rounding_convention": (
        "decimal.Decimal only, never floats. ROUND_HALF_UP applied per period: "
        "money to 2 dp (cents), share counts to whole shares rounded row-by-row in "
        "the weighted-average schedule then summed, EPS to 2 dp. Time weighting "
        "uses exact n/12 Decimal month fractions; no PV table factors apply to "
        "this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Part c requires a memorandum note, not a journal entry, so no entry is "
        "included for it. Preferred dividend of $8,000 (5,000 x $20 x 8%) is "
        "deducted in the basic EPS numerator despite being undeclared because the "
        "preferred is cumulative and the dividend goes into arrears. The Oct 1 "
        "restatement factor of 2.0 is applied to all pre-split periods, so the "
        "Jul 1 - Oct 1 period (116,000 x 2 = 232,000) and the Oct 1 - Dec 31 "
        "period carry the same share count."
    ),
}

print(json.dumps(result, indent=2))
