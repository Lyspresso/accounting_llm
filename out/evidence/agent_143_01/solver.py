#!/usr/bin/env python3
"""Blind solver -- agent_143#01.

Cascade Peak Logistics Inc. discount bond:
  Face $250,000, stated 6% paid semiannually (June 30 / Dec 31),
  issued January 1, Year 1, maturing December 31, Year 4 (4 years = 8 periods),
  priced to yield a market rate of 8%. Effective-interest method.

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal. No floats anywhere.
* Issue price: present value computed from the EXACT annuity/lump-sum formulas
  at 28 significant digits (i = 4% per semiannual period, n = 8), then rounded
  ONCE to the nearest dollar with ROUND_HALF_UP. (Cross-checked against
  5-decimal PV table factors PVA(4%,8)=6.73274 and PV(4%,8)=0.73069, which give
  the identical $233,168 issue price -- see "table_cross_check" note.)
* Amortization schedule: ROUND_HALF_UP to the nearest dollar PER PERIOD.
  Interest expense each period = beginning carrying amount x 4%, rounded to the
  nearest dollar at that period before the discount amortization is derived.
  Cash interest is exact ($7,500) and needs no rounding.
* Final period (period 8) uses a PLUG, as the stem directs: discount
  amortization = remaining unamortized discount, so carrying amount closes to
  face exactly; interest expense = cash interest + plug amortization.
* No rounding is carried forward as a fraction; each period's carrying amount is
  a whole dollar, so the schedule is internally consistent and self-checking
  (sum of amortization must equal the original discount).

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 28

CENT = Decimal("1")  # this problem rounds to the nearest dollar


def d(x):
    return Decimal(str(x))


def r(x):
    """Round to nearest dollar, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x):
    """Serialize a Decimal for JSON: exact int when whole, else float of the
    Decimal's own string (money here is always whole dollars)."""
    if x == x.to_integral_value():
        return int(x)
    return float(str(x))


# ---------------------------------------------------------------- fact pattern
FACE = d(250000)
STATED_ANNUAL = d("0.06")
MARKET_ANNUAL = d("0.08")
PERIODS_PER_YEAR = 2
YEARS = 4

N = YEARS * PERIODS_PER_YEAR                     # 8 semiannual periods
i = MARKET_ANNUAL / PERIODS_PER_YEAR             # 0.04 market rate per period
c = STATED_ANNUAL / PERIODS_PER_YEAR             # 0.03 stated rate per period
CASH_INTEREST = FACE * c                         # $7,500 exact each period


# ------------------------------------------------------- a. issue price + JE
one_plus_i_pow_n = (Decimal(1) + i) ** N          # exact Decimal exponentiation
pv_factor = Decimal(1) / one_plus_i_pow_n         # PV of $1, 4%, 8 periods
pv_annuity_factor = (Decimal(1) - pv_factor) / i  # PV of ordinary annuity

pv_principal_exact = FACE * pv_factor
pv_interest_exact = CASH_INTEREST * pv_annuity_factor
issue_price = r(pv_principal_exact + pv_interest_exact)

# Cross-check with 5-decimal textbook table factors (not reported as an answer).
tbl_price = r(CASH_INTEREST * d("6.73274") + FACE * d("0.73069"))
table_cross_check = (tbl_price == issue_price)

discount = FACE - issue_price


# --------------------------------------- b. full effective-interest schedule
schedule = []
carrying = issue_price
unamortized = discount

for period in range(1, N + 1):
    beginning = carrying
    if period < N:
        interest_expense = r(beginning * i)
        amortization = interest_expense - CASH_INTEREST
    else:
        # final period: plug the residual so carrying amount closes to face
        amortization = unamortized
        interest_expense = CASH_INTEREST + amortization
    unamortized -= amortization
    carrying = beginning + amortization
    schedule.append(
        {
            "period": period,
            "beginning_carrying_amount": beginning,
            "cash_interest": CASH_INTEREST,
            "interest_expense": interest_expense,
            "discount_amortization": amortization,
            "unamortized_discount": unamortized,
            "ending_carrying_amount": carrying,
        }
    )

# self-checks (must hold or the derivation is wrong)
assert carrying == FACE, f"carrying amount did not close to face: {carrying}"
assert unamortized == 0, f"unamortized discount did not close to zero: {unamortized}"
assert sum(p["discount_amortization"] for p in schedule) == discount


# --------------------------- c/d. Year 1 interest JE figures and presentation
p1, p2 = schedule[0], schedule[1]
year1_interest_expense = p1["interest_expense"] + p2["interest_expense"]
bonds_payable_net_y1 = p2["ending_carrying_amount"]


# ------------------------------------------------ e. maturity (period 8) data
p8 = schedule[7]


# ------------------------------------------------------------- journal entries
def line(account, debit=None, credit=None):
    return {
        "account": account,
        "debit": num(debit) if debit is not None else 0,
        "credit": num(credit) if credit is not None else 0,
    }


journal_entries = [
    {
        "part": "a",
        "date": "January 1, Year 1",
        "description": "Issuance of $250,000 face, 6% bonds at a discount to yield 8%",
        "lines": [
            line("Cash", debit=issue_price),
            line("Discount on Bonds Payable", debit=discount),
            line("Bonds Payable", credit=FACE),
        ],
    },
    {
        "part": "c",
        "date": "June 30, Year 1",
        "description": "Semiannual interest payment and discount amortization (period 1)",
        "lines": [
            line("Interest Expense", debit=p1["interest_expense"]),
            line("Discount on Bonds Payable", credit=p1["discount_amortization"]),
            line("Cash", credit=p1["cash_interest"]),
        ],
    },
    {
        "part": "c",
        "date": "December 31, Year 1",
        "description": "Semiannual interest payment and discount amortization (period 2)",
        "lines": [
            line("Interest Expense", debit=p2["interest_expense"]),
            line("Discount on Bonds Payable", credit=p2["discount_amortization"]),
            line("Cash", credit=p2["cash_interest"]),
        ],
    },
    {
        "part": "e",
        "date": "December 31, Year 4",
        "description": "Final semiannual interest and residual discount amortization (period 8, plug)",
        "lines": [
            line("Interest Expense", debit=p8["interest_expense"]),
            line("Discount on Bonds Payable", credit=p8["discount_amortization"]),
            line("Cash", credit=p8["cash_interest"]),
        ],
    },
    {
        "part": "e",
        "date": "December 31, Year 4",
        "description": "Repayment of principal at maturity",
        "lines": [
            line("Bonds Payable", debit=FACE),
            line("Cash", credit=FACE),
        ],
    },
]

for je in journal_entries:
    td = sum(Decimal(str(l["debit"])) for l in je["lines"])
    tc = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert td == tc, f"entry out of balance ({je['part']} {je['date']}): {td} vs {tc}"


# --------------------------------------------------------------------- answers
answers = [
    {"label": "a: issue price of the bonds (January 1, Year 1)", "value": num(issue_price)},
]

for p in schedule:
    answers.append(
        {
            "label": f"b: period {p['period']} interest expense",
            "value": num(p["interest_expense"]),
        }
    )
    answers.append(
        {
            "label": f"b: period {p['period']} discount amortization",
            "value": num(p["discount_amortization"]),
        }
    )
    answers.append(
        {
            "label": f"b: period {p['period']} ending carrying amount (bonds payable, net)",
            "value": num(p["ending_carrying_amount"]),
        }
    )

answers.append(
    {"label": "d: bonds payable, net at December 31, Year 1", "value": num(bonds_payable_net_y1)}
)
answers.append(
    {"label": "d: Year 1 interest expense", "value": num(year1_interest_expense)}
)

notes = (
    "Semiannual: 8 periods, market 4%/period, cash interest $7,500/period. "
    "Issue price from exact PV formulas = "
    f"{issue_price}; 5-decimal table factors (6.73274 / 0.73069) agree: "
    f"{'yes' if table_cross_check else 'NO'}. "
    "Discount of "
    f"{num(discount)} fully amortized; period 8 amortization is the residual plug "
    f"({num(p8['discount_amortization'])}), so interest expense in period 8 is "
    f"{num(p8['interest_expense'])}. Cash interest of $7,500 per period is stated-rate "
    "based and is not rounded. No prior Interest Payable at maturity, per the stem."
)

out = {
    "id": "agent_143#01",
    "rounding_convention": (
        "ROUND_HALF_UP to the nearest dollar per period (interest expense = "
        "beginning carrying amount x 4%, rounded each period before deriving "
        "amortization); issue price from exact PV formulas rounded once to the "
        "nearest dollar (5-decimal PV table factors give the same figure); "
        "final period discount amortization plugged so carrying amount closes "
        "to face"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
