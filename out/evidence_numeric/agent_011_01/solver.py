"""Solver for agent_011#01 — Summit Forge Equipment bonds issued at a discount.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal (never float). Present values are computed at full
precision (Decimal context prec=50); every reported dollar figure is rounded to
the nearest whole dollar with ROUND_HALF_UP, applied per period (each period's
interest expense is rounded independently, not carried at full precision).
Journal entries are stated in whole dollars. The final period's discount
amortization is PLUGGED so the schedule closes exactly to the $250,000 face
amount; the final period's interest expense is then cash interest + plugged
amortization. Nothing is hard-coded: every figure is derived from face, stated
rate, market rate, term and payment frequency.
"""

import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 50

CENT = Decimal("1")


def d0(x):
    """Round to nearest whole dollar, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- given facts
FACE = Decimal("250000")
STATED_ANNUAL = Decimal("0.05")
MARKET_ANNUAL = Decimal("0.07")
YEARS = Decimal("5")
PER_YEAR = Decimal("2")

n = int(YEARS * PER_YEAR)                      # 10 semiannual periods
i = MARKET_ANNUAL / PER_YEAR                   # 0.035 market rate per period
c = STATED_ANNUAL / PER_YEAR                   # 0.025 stated rate per period
cash = FACE * c                                # 6,250 cash interest each period

# ------------------------------------------------- (c) issue price at 3.5%/pd
one = Decimal(1)
pv_factor = one / (one + i) ** n               # PV of $1, 10 periods @ 3.5%
pvifa = (one - pv_factor) / i                  # PV of ordinary annuity of $1
pv_interest_exact = cash * pvifa
pv_principal_exact = FACE * pv_factor
price_exact = pv_interest_exact + pv_principal_exact

pv_interest = d0(pv_interest_exact)
pv_principal = d0(pv_principal_exact)
price = d0(price_exact)
discount = FACE - price

# ------------------------------------------------------- (d) full schedule
rows = []
carry = price
for p in range(1, n + 1):
    begin = carry
    if p < n:
        exp = d0(begin * i)
        amort = exp - d0(cash)
    else:
        amort = FACE - begin              # plug so schedule closes to face
        exp = d0(cash) + amort
    carry = begin + amort
    rows.append({
        "period": p,
        "date": ("Jun 30" if p % 2 == 1 else "Dec 31") + f", Year {(p + 1) // 2}",
        "begin": begin,
        "cash": d0(cash),
        "expense": exp,
        "amort": amort,
        "end": carry,
    })

assert rows[-1]["end"] == FACE, "schedule must close to face"
total_cash = sum((r["cash"] for r in rows), Decimal(0))
total_exp = sum((r["expense"] for r in rows), Decimal(0))
total_amort = sum((r["amort"] for r in rows), Decimal(0))
assert total_amort == discount
assert total_cash + total_amort == total_exp

p1, p2 = rows[0], rows[1]
dec31_net = p2["end"]

# ---------------------------------------------------------------- answers
def n0(x):
    return int(Decimal(x))


answers = []
A = lambda label, value: answers.append({"label": label, "value": value})

# a. bond type(s)
A("a: bond type 1 — secured bonds (collateralized/mortgage-type: first lien on "
  "specified manufacturing equipment)", "Secured bonds")
A("a: bond type 2 — callable (redeemable) bonds: issuer may call any time after "
  "3 years at 102", "Callable bonds")
A("a: bond type 3 — term bonds: entire $250,000 face matures on one date, "
  "5 years out (not serial)", "Term bonds")

# b. the eight bond features
A("b: feature 1 — face (par/maturity) value", n0(FACE))
A("b: feature 2 — stated (contract/coupon) rate, annual", "5% annual (2.5% per semiannual period)")
A("b: feature 3 — market (effective/yield) rate at issue, annual",
  "7% annual (3.5% per semiannual period)")
A("b: feature 4 — term to maturity", "5 years = 10 semiannual interest periods")
A("b: feature 5 — interest payment dates/frequency", "Semiannual, each June 30 and December 31")
A("b: feature 6 — cash interest payment per period", n0(d0(cash)))
A("b: feature 7 — security/collateral",
  "Secured — first lien on specified manufacturing equipment")
A("b: feature 8 — call (redemption) provision",
  "Callable by issuer any time after 3 years at 102 (call price $255,000)")

# c. issue price and issuance JE
A("c: PV of the 10 semiannual interest payments of $6,250 at 3.5%", n0(pv_interest))
A("c: PV of the $250,000 face amount at 3.5% for 10 periods", n0(pv_principal))
A("c: issue price (proceeds), nearest dollar", n0(price))
A("c: discount on bonds payable at issuance", n0(discount))

# d. schedule
for r in rows:
    A(f"d: period {r['period']} ({r['date']}) — carrying value, beginning", n0(r["begin"]))
    A(f"d: period {r['period']} ({r['date']}) — cash interest paid", n0(r["cash"]))
    A(f"d: period {r['period']} ({r['date']}) — interest expense (3.5% x beginning carrying value)", n0(r["expense"]))
    A(f"d: period {r['period']} ({r['date']}) — discount amortization", n0(r["amort"]))
    A(f"d: period {r['period']} ({r['date']}) — carrying value, ending", n0(r["end"]))
A("d: total cash interest paid over 10 periods", n0(total_cash))
A("d: total interest expense over 10 periods", n0(total_exp))
A("d: total discount amortized (= discount at issue)", n0(total_amort))

# e. June 30, Year 1
A("e: June 30, Year 1 — interest expense", n0(p1["expense"]))
A("e: June 30, Year 1 — discount amortization", n0(p1["amort"]))
A("e: June 30, Year 1 — cash paid", n0(p1["cash"]))

# f. December 31, Year 1
A("f: December 31, Year 1 — bonds payable, face", n0(FACE))
A("f: December 31, Year 1 — unamortized discount", n0(FACE - dec31_net))
A("f: December 31, Year 1 — bonds payable, net (carrying value)", n0(dec31_net))

# ---------------------------------------------------------------- JEs
jes = [
    {"part": "c", "lines": [
        {"account": "Cash", "debit": n0(price), "credit": 0},
        {"account": "Discount on Bonds Payable", "debit": n0(discount), "credit": 0},
        {"account": "Bonds Payable", "debit": 0, "credit": n0(FACE)},
    ]},
    {"part": "e", "lines": [
        {"account": "Interest Expense", "debit": n0(p1["expense"]), "credit": 0},
        {"account": "Discount on Bonds Payable", "debit": 0, "credit": n0(p1["amort"])},
        {"account": "Cash", "debit": 0, "credit": n0(p1["cash"])},
    ]},
]
for je in jes:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"])

out = {
    "id": "agent_011#01",
    "rounding_convention": (
        "decimal.Decimal throughout (no floats); PV factors at full precision "
        "(prec=50); every dollar figure rounded to the nearest whole dollar with "
        "ROUND_HALF_UP, applied per period (interest expense = 3.5% x that period's "
        "beginning carrying value, rounded each period). Journal entries in whole "
        "dollars. Period 10 amortization is plugged so the schedule closes exactly "
        "to the $250,000 face amount."
    ),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": (
        "Semiannual effective interest: 10 periods, market 3.5%/period, coupon "
        "2.5%/period = $6,250 cash. Issued at a discount because the 5% stated rate "
        "is below the 7% market yield. Part b lists the same eight features as Q1 "
        "(face, stated rate, market rate, term, payment dates, periodic cash "
        "interest, security, call provision) since Q1's own text was not supplied. "
        "The call price of 102 ($255,000) is a feature only; no call occurs in "
        "Year 1, so it does not affect any entry above. Interest is paid on the "
        "Dec 31 year-end date, so no accrual adjusting entry is needed and the "
        "Dec 31, Year 1 net carrying amount reflects two periods of amortization. "
        "Price detail: exact PV = 229,208.48 -> $229,208 at full precision. A text "
        "using 5-decimal table factors (0.70892 / 8.31661) would show $229,209, a $1 "
        "table-rounding difference; the whole schedule shifts by that same $1 if the "
        "table price is used. The rounded PV components (51,979 + 177,230) also sum to "
        "229,209 because each component rounds up; the total is rounded once from the "
        "exact 229,208.48."
    ),
}
print(json.dumps(out, indent=1))
