"""Solver for agent_016#00 -- Redwood Metalworks 3-yr $80,000 5% note, 9% market.

Rounding convention: all money computed with decimal.Decimal (28+ digit context),
quantized to the nearest cent using ROUND_HALF_UP at each period (present value,
each period's interest expense, and each period's discount amortization).
The final period's discount amortization is PLUGGED so carrying amount == face.
Nothing is hard-coded: PV factors are derived from the stated market rate/term.
"""
import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 50
C = Decimal("0.01")


def q(x):
    return x.quantize(C, rounding=ROUND_HALF_UP)


def f(x):
    return float(x)


# ---- inputs derived from the scenario text ----
FACE = Decimal("80000")
STATED = Decimal("0.05")
MARKET = Decimal("0.09")
N = 3

cash_int = q(FACE * STATED)

# (a) issue price = PV of annuity of cash interest + PV of face
one = Decimal(1)
pv_factor = one / (one + MARKET) ** N            # PVIF(9%,3)
pvifa = (one - pv_factor) / MARKET               # PVIFA(9%,3)
pv_interest = cash_int * pvifa
pv_principal = FACE * pv_factor
issue_price = q(pv_interest + pv_principal)
discount = q(FACE - issue_price)

# (c) effective-interest amortization schedule
rows = []
cv = issue_price
total_cash = Decimal("0")
total_exp = Decimal("0")
total_amort = Decimal("0")
for yr in range(1, N + 1):
    if yr < N:
        exp = q(cv * MARKET)
        amort = q(exp - cash_int)
    else:
        amort = q(FACE - cv)          # plug so carrying == face at maturity
        exp = q(cash_int + amort)
    cv = q(cv + amort)
    total_cash += cash_int
    total_exp += exp
    total_amort += amort
    rows.append((yr, cash_int, exp, amort, cv))

answers = [
    {"label": "a: Cash proceeds (issue price) of the note, Jan 1 Year 1", "value": f(issue_price)},
    {"label": "a: Discount on note payable at issuance (face - proceeds)", "value": f(discount)},
    {"label": "a: Annual cash interest payment (80,000 x 5%)", "value": f(cash_int)},
    {"label": "c: Carrying amount at Jan 1, Year 1 (schedule opening balance)", "value": f(issue_price)},
]
for yr, ci, exp, am, bal in rows:
    answers += [
        {"label": f"c: Year {yr} - cash interest paid", "value": f(ci)},
        {"label": f"c: Year {yr} - interest expense (9% x beginning carrying amount)", "value": f(exp)},
        {"label": f"c: Year {yr} - discount amortization", "value": f(am)},
        {"label": f"c: Year {yr} - ending carrying amount", "value": f(bal)},
    ]
answers += [
    {"label": "c: Totals - cash interest over 3 years", "value": f(q(total_cash))},
    {"label": "c: Totals - interest expense over 3 years", "value": f(q(total_exp))},
    {"label": "c: Totals - discount amortization over 3 years", "value": f(q(total_amort))},
]

y1 = rows[0]
y3 = rows[2]
jes = [
    {"part": "b", "lines": [
        {"account": "Cash", "debit": f(issue_price), "credit": 0},
        {"account": "Discount on Notes Payable", "debit": f(discount), "credit": 0},
        {"account": "Notes Payable", "debit": 0, "credit": f(FACE)},
    ]},
    {"part": "d", "lines": [
        {"account": "Interest Expense", "debit": f(y1[2]), "credit": 0},
        {"account": "Discount on Notes Payable", "debit": 0, "credit": f(y1[3])},
        {"account": "Cash", "debit": 0, "credit": f(y1[1])},
    ]},
    {"part": "e", "lines": [
        {"account": "Interest Expense", "debit": f(y3[2]), "credit": 0},
        {"account": "Discount on Notes Payable", "debit": 0, "credit": f(y3[3])},
        {"account": "Cash", "debit": 0, "credit": f(y3[1])},
    ]},
    {"part": "e", "lines": [
        {"account": "Notes Payable", "debit": f(FACE), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": f(FACE)},
    ]},
]

for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)
assert rows[-1][4] == FACE

print(json.dumps({
    "id": "agent_016#00",
    "rounding_convention": ("decimal.Decimal throughout; ROUND_HALF_UP to the nearest cent "
                           "each period (PV, interest expense, discount amortization); "
                           "Year 3 amortization plugged so carrying amount equals $80,000 face at maturity"),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("Issue price = 4,000 x PVIFA(9%,3) + 80,000 x PVIF(9%,3), factors derived from the 9% "
              "market rate and 3-year term. Interest expense each year = 9% x beginning carrying amount; "
              "discount amortization = expense - 4,000 cash interest. Year 3 expense/amortization are "
              "plugged (amortization = 80,000 - beginning carrying amount) to absorb rounding so the "
              "carrying amount is exactly 80,000 at maturity. Maturity settlement of principal shown "
              "as a separate entry from the Year 3 interest entry.")
}, indent=2))
