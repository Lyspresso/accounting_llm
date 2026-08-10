"""Solver for agent_274#02 (LO 16-2: premium bonds, period-end accrual, between-interest-date issuance).

Rounding convention: all money is decimal.Decimal. Present values are computed at
28-digit precision and every reported money figure is rounded to the NEAREST DOLLAR
using ROUND_HALF_UP, applied PER PERIOD (each period's interest expense is rounded
independently off that period's rounded carrying amount; amortization = cash - expense).
The FINAL period plugs the residual premium (amortization = carrying amount - face),
so the schedule closes exactly at face. Nothing is hard-coded; every figure is derived.
"""
import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28
D = Decimal


def dollar(x):
    return x.quantize(D("1"), rounding=ROUND_HALF_UP)


def i(x):
    return int(x)


# ---------- Part A: Quarry Bend Alloys LLC ----------
face_A = D("180000")
stated_annual = D("0.08")
market_annual = D("0.06")
periods_per_year = D("2")
n = 4  # 2 years x semiannual

r = market_annual / periods_per_year          # 3% effective per period
c = stated_annual / periods_per_year          # 4% stated per period
cash_int = face_A * c                         # cash interest per period

one = D("1")
pv_factor = one / ((one + r) ** n)
annuity_factor = (one - pv_factor) / r
issue_price = dollar(cash_int * annuity_factor + face_A * pv_factor)
premium_initial = issue_price - face_A

# amortization schedule
rows = []
cv = issue_price
for p in range(1, n + 1):
    beg = cv
    if p < n:
        exp = dollar(beg * r)
        amort = dollar(cash_int) - exp
    else:
        amort = beg - face_A          # final period plugs residual premium
        exp = dollar(cash_int) - amort
    end = beg - amort
    rows.append({"period": p, "beg": beg, "cash": dollar(cash_int),
                 "exp": exp, "amort": amort, "end": end})
    cv = end

p1, p2, p3, p4 = rows

# (d) Aug 31, Year 1 accrual = 2/6 of the NEXT full semiannual row (period 2)
frac = D("2") / D("6")
acc_exp = dollar(p2["exp"] * frac)
acc_payable = dollar(p2["cash"] * frac)
acc_amort = acc_payable - acc_exp

# (e) Dec 31, Year 1 position
cv_dec31_y1 = p2["end"]
unamort_prem_dec31_y1 = cv_dec31_y1 - face_A
year1_int_exp = p1["exp"] + p2["exp"]

# ---------- Part B: Pinnacle Loom Textiles Corp. ----------
face_B = D("240000")
rate_B = D("0.07")
months_accrued = D("3")   # Jan 1 dated -> Apr 1 issued
accrued_int_B = dollar(face_B * rate_B * months_accrued / D("12"))
cash_at_issue_B = face_B + accrued_int_B
cash_int_B_semi = dollar(face_B * rate_B / periods_per_year)
exp_B_jun30 = cash_int_B_semi - accrued_int_B   # 3 months held (Apr 1 - Jun 30)

answers = [
    {"label": "a: Issue price (PV of $7,200 annuity + $180,000 at 3% for 4 periods)", "value": i(issue_price)},
    {"label": "a: Premium on bonds payable at issuance", "value": i(premium_initial)},
    {"label": "a: Cash interest per semiannual period (180,000 x 4%)", "value": i(dollar(cash_int))},

    {"label": "b: Period 1 (Jun 30, Yr 1) beginning carrying amount", "value": i(p1["beg"])},
    {"label": "b: Period 1 cash interest paid", "value": i(p1["cash"])},
    {"label": "b: Period 1 interest expense (3% x beginning CV)", "value": i(p1["exp"])},
    {"label": "b: Period 1 premium amortization", "value": i(p1["amort"])},
    {"label": "b: Period 1 ending carrying amount", "value": i(p1["end"])},
    {"label": "b: Period 2 (Dec 31, Yr 1) beginning carrying amount", "value": i(p2["beg"])},
    {"label": "b: Period 2 cash interest paid", "value": i(p2["cash"])},
    {"label": "b: Period 2 interest expense", "value": i(p2["exp"])},
    {"label": "b: Period 2 premium amortization", "value": i(p2["amort"])},
    {"label": "b: Period 2 ending carrying amount", "value": i(p2["end"])},
    {"label": "b: Period 3 (Jun 30, Yr 2) beginning carrying amount", "value": i(p3["beg"])},
    {"label": "b: Period 3 cash interest paid", "value": i(p3["cash"])},
    {"label": "b: Period 3 interest expense", "value": i(p3["exp"])},
    {"label": "b: Period 3 premium amortization", "value": i(p3["amort"])},
    {"label": "b: Period 3 ending carrying amount", "value": i(p3["end"])},
    {"label": "b: Period 4 (Dec 31, Yr 2) beginning carrying amount", "value": i(p4["beg"])},
    {"label": "b: Period 4 cash interest paid", "value": i(p4["cash"])},
    {"label": "b: Period 4 interest expense (plug: cash - residual premium)", "value": i(p4["exp"])},
    {"label": "b: Period 4 premium amortization (residual premium plug)", "value": i(p4["amort"])},
    {"label": "b: Period 4 ending carrying amount (= face)", "value": i(p4["end"])},

    {"label": "c: Jun 30, Yr 1 interest expense", "value": i(p1["exp"])},
    {"label": "c: Jun 30, Yr 1 premium amortization", "value": i(p1["amort"])},
    {"label": "c: Jun 30, Yr 1 cash paid", "value": i(p1["cash"])},

    {"label": "d: Aug 31, Yr 1 accrued interest expense (2/6 of period 2 expense)", "value": i(acc_exp)},
    {"label": "d: Aug 31, Yr 1 interest payable accrued (2/6 x 7,200)", "value": i(acc_payable)},
    {"label": "d: Aug 31, Yr 1 premium amortization (2/6 of period 2 amortization)", "value": i(acc_amort)},

    {"label": "e: Bonds payable, net (carrying amount) at Dec 31, Yr 1", "value": i(cv_dec31_y1)},
    {"label": "e: Unamortized premium at Dec 31, Yr 1", "value": i(unamort_prem_dec31_y1)},
    {"label": "e: Year 1 total interest expense (both semiannual periods)", "value": i(year1_int_exp)},

    {"label": "f: Principal repaid at maturity Dec 31, Yr 2", "value": i(face_A)},

    {"label": "g: Accrued interest collected at Apr 1 issuance (240,000 x 7% x 3/12)", "value": i(accrued_int_B)},
    {"label": "g: Total cash received Apr 1, Yr 1", "value": i(cash_at_issue_B)},
    {"label": "g: Jun 30, Yr 1 cash interest paid (240,000 x 3.5%)", "value": i(cash_int_B_semi)},
    {"label": "g: Jun 30, Yr 1 interest expense recognized (3 months held)", "value": i(exp_B_jun30)},

    {"label": "h: Classification at Dec 31, Yr 1", "value":
        "Current liability. The bonds mature Dec 31, Year 2 - within one year of the Dec 31, Year 1 "
        "balance sheet date - so the obligation is presented as current. It is shown at its net "
        "carrying amount of $%s: face $%s of bonds payable plus the unamortized premium of $%s, "
        "with the premium reported as a direct addition to (valuation account of) bonds payable, "
        "not as a separate asset." % (i(cv_dec31_y1), i(face_A), i(unamort_prem_dec31_y1))},
]

journal_entries = [
    {"part": "a", "lines": [
        {"account": "Cash", "debit": i(issue_price), "credit": 0},
        {"account": "Bonds Payable", "debit": 0, "credit": i(face_A)},
        {"account": "Premium on Bonds Payable", "debit": 0, "credit": i(premium_initial)},
    ]},
    {"part": "c", "lines": [
        {"account": "Interest Expense", "debit": i(p1["exp"]), "credit": 0},
        {"account": "Premium on Bonds Payable", "debit": i(p1["amort"]), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": i(p1["cash"])},
    ]},
    {"part": "d", "lines": [
        {"account": "Interest Expense", "debit": i(acc_exp), "credit": 0},
        {"account": "Premium on Bonds Payable", "debit": i(acc_amort), "credit": 0},
        {"account": "Interest Payable", "debit": 0, "credit": i(acc_payable)},
    ]},
    {"part": "f", "lines": [
        {"account": "Bonds Payable", "debit": i(face_A), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": i(face_A)},
    ]},
    {"part": "g", "lines": [
        {"account": "Cash", "debit": i(cash_at_issue_B), "credit": 0},
        {"account": "Bonds Payable", "debit": 0, "credit": i(face_B)},
        {"account": "Interest Payable", "debit": 0, "credit": i(accrued_int_B)},
    ]},
    {"part": "g", "lines": [
        {"account": "Interest Payable", "debit": i(accrued_int_B), "credit": 0},
        {"account": "Interest Expense", "debit": i(exp_B_jun30), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": i(cash_int_B_semi)},
    ]},
]

for je in journal_entries:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"]), je["part"]
assert p4["end"] == face_A
assert sum(rw["amort"] for rw in rows) == premium_initial
assert acc_exp + acc_amort == acc_payable

out = {
    "id": "agent_274#02",
    "rounding_convention": ("decimal.Decimal throughout; PV factors at 28-digit precision; every money "
                            "figure rounded to the nearest whole dollar with ROUND_HALF_UP, applied per "
                            "period (interest expense = 3% x that period's rounded carrying amount); the "
                            "final period plugs the residual premium so the schedule closes at face"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": ("Part A: semiannual market rate 3%, stated 4%, 4 periods; issued at a premium because market "
              "< stated. Aug 31, Year 1 interim accrual prorates the period-2 schedule row by 2/6 (July-August), "
              "so interest payable 2,400, expense 1,851, premium amortized 549; the remaining 4/6 is picked up in "
              "the Dec 31 payment entry (Dec 31 is an interest date, so full-period totals for Year 1 are "
              "unaffected). Part B: bonds dated Jan 1 but issued Apr 1 at par, so the buyer pays 3 months of "
              "accrued interest (4,200) credited to Interest Payable; the June 30 payment of 8,400 clears that "
              "4,200 and charges only 4,200 of expense for the 3 months the bonds were outstanding."),
}
print(json.dumps(out, indent=1))
