#!/usr/bin/env python3
"""
Solver for item agent_277#00 - Cedar & Flint Ironworks Inc.
Bonds issued at a PREMIUM; effective-interest amortization; period-end accrual.

FACT PATTERN (from stem.md, nothing hard-coded beyond these givens)
-------------------------------------------------------------------
  Face                       $250,000
  Stated (coupon) rate       6% per year, paid semiannually -> 3% per period
  Market (yield) rate        4% per year, compounded semiannually -> 2% per period
  Issue date                 April 1, Year 1
  Maturity                   April 1, Year 4  -> 3 years -> n = 6 semiannual periods
  Interest dates             April 1 and October 1
  Reporting year-end         December 31 (calendar-year reporter)

ROUNDING CONVENTION
-------------------
  * All money is decimal.Decimal. No floats anywhere.
  * Present values are computed from the EXACT effective-interest formula
    ((1 + i)^-n and its annuity sum) at 50-digit working precision, then
    rounded ONCE to the nearest whole dollar with ROUND_HALF_UP.
  * Schedule amounts are rounded PER PERIOD (round-per-period, not
    round-at-end) to the nearest whole dollar with ROUND_HALF_UP, exactly as
    the stem directs ("rounds present values and schedule amounts to the
    nearest dollar").  Each period's carrying amount is carried forward as the
    already-rounded dollar figure, so the next period's interest is computed on
    the rounded balance.
  * FINAL PERIOD PLUG: per the stem, the last row's premium amortization is the
    residual unamortized premium (forces carrying amount to face = $250,000),
    and the last row's interest expense is cash interest less that plug.
  * PERIOD-END ACCRUAL (part d): 3 of the 6 months of the Oct 1 -> Apr 1 period
    have elapsed at Dec 31.  Per the stem's own instruction, the accrual is the
    next full schedule row prorated 3/6:
        Interest expense = (carrying amount after Oct 1 x 2%) x 3/6
        Interest payable = face x 6% x 3/12
        Premium amortization = Interest payable - Interest expense
    Each of those is rounded to the nearest dollar, ROUND_HALF_UP.  (Rounding
    the full-period expense first and then halving gives the identical dollar
    figure here, so the convention choice is not load-bearing.)

  Why the exact formula rather than 5-decimal PV table factors: 5-decimal
  factors give an issue price of $264,003, which makes the final schedule row
  internally inconsistent (the residual plug forces interest expense to $5,050
  while 2% of the opening balance is $5,049).  The exact formula gives
  $264,004, for which the residual plug and 2%-of-carrying-amount agree to the
  dollar in every one of the six periods.  Reported figures use $264,004.

USAGE:  python3 solver.py       (prints one JSON object to stdout)
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 50

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d(x):
    """Money -> Decimal, always from a string so no float ever enters."""
    return Decimal(str(x))


def r0(x):
    """Round to nearest whole dollar, ROUND_HALF_UP."""
    return x.quantize(DOLLAR, rounding=ROUND_HALF_UP)


def num(x):
    """Decimal -> JSON number (int when whole)."""
    x = x.quantize(CENT, rounding=ROUND_HALF_UP)
    return int(x) if x == x.to_integral_value() else float(x)


# ----------------------------------------------------------------------------
# Givens
# ----------------------------------------------------------------------------
FACE = d("250000")
STATED_ANNUAL = d("0.06")
MARKET_ANNUAL = d("0.04")
PERIODS_PER_YEAR = d("2")
YEARS = d("3")

i = MARKET_ANNUAL / PERIODS_PER_YEAR            # 0.02 effective per period
c = STATED_ANNUAL / PERIODS_PER_YEAR            # 0.03 coupon per period
n = int(YEARS * PERIODS_PER_YEAR)               # 6 periods
CASH_INTEREST = FACE * c                        # 7,500 per period (exact)


# ----------------------------------------------------------------------------
# (a) Issue price
# ----------------------------------------------------------------------------
one = Decimal(1)
pv_of_1 = one / ((one + i) ** n)                 # PV of $1, 2%, 6 periods
pv_annuity_of_1 = (one - pv_of_1) / i            # PV of ordinary annuity of $1

pv_principal = FACE * pv_of_1
pv_interest = CASH_INTEREST * pv_annuity_of_1
ISSUE_PRICE = r0(pv_principal + pv_interest)

PREMIUM_AT_ISSUE = ISSUE_PRICE - FACE            # premium (issued above par)


# ----------------------------------------------------------------------------
# (b) Effective-interest amortization schedule, 6 semiannual periods
# ----------------------------------------------------------------------------
schedule = []
carrying = ISSUE_PRICE
unamortized = PREMIUM_AT_ISSUE
cash_int_r = r0(CASH_INTEREST)

for p in range(1, n + 1):
    opening = carrying
    if p < n:
        exp = r0(opening * i)
        amort = cash_int_r - exp
    else:
        # final period: plug the residual unamortized premium
        amort = unamortized
        exp = cash_int_r - amort
    carrying = opening - amort
    unamortized = unamortized - amort
    schedule.append(
        {
            "period": p,
            "opening_carrying_amount": opening,
            "cash_interest": cash_int_r,
            "interest_expense": exp,
            "premium_amortization": amort,
            "unamortized_premium": unamortized,
            "ending_carrying_amount": carrying,
        }
    )

assert carrying == FACE, "schedule must retire to face"
assert unamortized == 0, "premium must be fully amortized"
assert sum(row["premium_amortization"] for row in schedule) == PREMIUM_AT_ISSUE

# Period labels: P1 = Apr 1 Y1 -> Oct 1 Y1, P2 = Oct 1 Y1 -> Apr 1 Y2, ...
PERIOD_ENDS = [
    "Oct 1, Year 1",
    "Apr 1, Year 2",
    "Oct 1, Year 2",
    "Apr 1, Year 3",
    "Oct 1, Year 3",
    "Apr 1, Year 4",
]

p1 = schedule[0]     # Apr 1 Y1 -> Oct 1 Y1  (part c)
p2 = schedule[1]     # Oct 1 Y1 -> Apr 1 Y2  (part d prorates 3/6 of this row)
p6 = schedule[5]     # final period          (part f)


# ----------------------------------------------------------------------------
# (d) December 31, Year 1 adjusting accrual  (3 of 6 months elapsed)
# ----------------------------------------------------------------------------
carrying_after_oct1 = p1["ending_carrying_amount"]
FRACTION = Decimal(3) / Decimal(6)

accrual_expense = r0(carrying_after_oct1 * i * FRACTION)
accrual_payable = r0(FACE * STATED_ANNUAL * (Decimal(3) / Decimal(12)))
accrual_amort = accrual_payable - accrual_expense

# cross-check against "prorate the next full schedule row" wording
assert accrual_expense == r0(p2["interest_expense"] * FRACTION)


# ----------------------------------------------------------------------------
# (e) December 31, Year 1 presentation
# ----------------------------------------------------------------------------
premium_unamort_dec31 = PREMIUM_AT_ISSUE - p1["premium_amortization"] - accrual_amort
bonds_net_dec31 = FACE + premium_unamort_dec31
interest_payable_dec31 = accrual_payable
year1_interest_expense = p1["interest_expense"] + accrual_expense

assert bonds_net_dec31 == carrying_after_oct1 - accrual_amort


# ----------------------------------------------------------------------------
# Answers (only what the Required parts ask for)
# ----------------------------------------------------------------------------
answers = [
    {"label": "a: issue price of the bonds (April 1, Year 1)", "value": num(ISSUE_PRICE)},
    {"label": "a: premium on bonds payable at issuance", "value": num(PREMIUM_AT_ISSUE)},
]

for row in schedule:
    p = row["period"]
    end = PERIOD_ENDS[p - 1]
    answers += [
        {"label": f"b: period {p} (to {end}) cash interest paid",
         "value": num(row["cash_interest"])},
        {"label": f"b: period {p} (to {end}) interest expense",
         "value": num(row["interest_expense"])},
        {"label": f"b: period {p} (to {end}) premium amortization",
         "value": num(row["premium_amortization"])},
        {"label": f"b: period {p} (to {end}) carrying amount at end of period",
         "value": num(row["ending_carrying_amount"])},
    ]

answers += [
    {"label": "d: Dec 31, Year 1 accrued interest expense (3 months)",
     "value": num(accrual_expense)},
    {"label": "d: Dec 31, Year 1 interest payable accrued (3 months)",
     "value": num(accrual_payable)},
    {"label": "d: Dec 31, Year 1 premium amortization (3 months)",
     "value": num(accrual_amort)},
    {"label": "e: Dec 31, Year 1 bonds payable (face)", "value": num(FACE)},
    {"label": "e: Dec 31, Year 1 unamortized premium on bonds payable",
     "value": num(premium_unamort_dec31)},
    {"label": "e: Dec 31, Year 1 bonds payable, net (carrying amount)",
     "value": num(bonds_net_dec31)},
    {"label": "e: Dec 31, Year 1 interest payable (current liability)",
     "value": num(interest_payable_dec31)},
    {"label": "e: Year 1 interest expense (income statement)",
     "value": num(year1_interest_expense)},
]


# ----------------------------------------------------------------------------
# Journal entries
# ----------------------------------------------------------------------------
def line(account, debit=Decimal(0), credit=Decimal(0)):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = [
    {
        "part": "a",
        "date": "April 1, Year 1",
        "description": "Issue $250,000 of 6% bonds at a premium to yield 4%",
        "lines": [
            line("Cash", debit=ISSUE_PRICE),
            line("Bonds Payable", credit=FACE),
            line("Premium on Bonds Payable", credit=PREMIUM_AT_ISSUE),
        ],
    },
    {
        "part": "c",
        "date": "October 1, Year 1",
        "description": "Semiannual interest payment and premium amortization (period 1)",
        "lines": [
            line("Interest Expense", debit=p1["interest_expense"]),
            line("Premium on Bonds Payable", debit=p1["premium_amortization"]),
            line("Cash", credit=p1["cash_interest"]),
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 1",
        "description": "Period-end adjusting accrual for Oct 1 - Dec 31 (3/6 of period 2)",
        "lines": [
            line("Interest Expense", debit=accrual_expense),
            line("Premium on Bonds Payable", debit=accrual_amort),
            line("Interest Payable", credit=accrual_payable),
        ],
    },
    {
        "part": "f1",
        "date": "April 1, Year 4",
        "description": "Final semiannual interest payment and premium amortization (period 6)",
        "lines": [
            line("Interest Expense", debit=p6["interest_expense"]),
            line("Premium on Bonds Payable", debit=p6["premium_amortization"]),
            line("Cash", credit=p6["cash_interest"]),
        ],
    },
    {
        "part": "f2",
        "date": "April 1, Year 4",
        "description": "Derecognize the bonds at maturity (premium fully amortized)",
        "lines": [
            line("Bonds Payable", debit=FACE),
            line("Cash", credit=FACE),
        ],
    },
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"unbalanced entry in part {je['part']}: {dr} vs {cr}"


out = {
    "id": "agent_277#00",
    "rounding_convention": (
        "decimal.Decimal only, ROUND_HALF_UP to the nearest whole dollar. "
        "Issue price from the exact effective-interest PV formula at 50-digit "
        "precision (i=2%, n=6), rounded once. Schedule rounded PER PERIOD with "
        "the rounded carrying amount carried forward; final period's premium "
        "amortization is the residual plug to face. Dec 31 accrual = next "
        "schedule row prorated 3/6 (expense), face x 6% x 3/12 (payable), "
        "amortization = payable - expense."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Premium issue: 6% coupon vs 4% yield, 6 semiannual periods at i=2%. "
        "Issue price $264,004 (premium $14,004). Using 5-decimal PV table "
        "factors instead would give $264,003 and leave the final schedule row "
        "internally inconsistent by $1, so the exact formula is used. "
        "Part f assumes no Interest Payable balance immediately before the "
        "final interest entry, per the stem."
    ),
}

print(json.dumps(out, indent=2))
