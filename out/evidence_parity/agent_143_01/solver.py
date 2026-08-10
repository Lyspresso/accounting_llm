"""Solver for agent_143#01 - Cascade Peak Logistics discount bond.

Rounding convention: all money uses decimal.Decimal (never float).
Every per-period figure is rounded to the nearest whole dollar using
ROUND_HALF_UP at the moment it is computed (issue price, each period's
interest expense); cash interest is exact; amortization is the derived
difference; the final period plugs the residual discount amortization so
carrying value closes exactly to face.
"""
import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 50
CENT = Decimal("1")


def d(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


face = Decimal("250000")
stated_annual = Decimal("0.06")
market_annual = Decimal("0.08")
periods_per_year = 2
years = 4
n = periods_per_year * years

i = market_annual / periods_per_year          # 0.04 effective per period
c = stated_annual / periods_per_year          # 0.03 stated per period
cash_interest = face * c                      # exact, whole dollars

# --- a. issue price -------------------------------------------------------
pv_factor = (Decimal(1) + i) ** (-n)
annuity_factor = (Decimal(1) - pv_factor) / i
issue_price = d(cash_interest * annuity_factor + face * pv_factor)
discount = face - issue_price

# --- b. effective-interest schedule --------------------------------------
rows = []
bv = issue_price
unamort = discount
for p in range(1, n + 1):
    beg = bv
    if p < n:
        exp = d(beg * i)
        amort = exp - cash_interest
    else:
        amort = unamort              # plug residual in final period
        exp = cash_interest + amort
    end = beg + amort
    unamort -= amort
    rows.append({"p": p, "beg": beg, "cash": cash_interest,
                 "exp": exp, "amort": amort, "end": end})
    bv = end

assert rows[-1]["end"] == face, rows[-1]["end"]

# --- d. Year 1 figures ----------------------------------------------------
y1_expense = rows[0]["exp"] + rows[1]["exp"]
bv_dec31_y1 = rows[1]["end"]
unamort_dec31_y1 = face - bv_dec31_y1

I = lambda x: int(x)

answers = [
    {"label": "a: PV annuity factor, 8 periods @ 4% (support)",
     "value": float(annuity_factor.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "a: PV of $1 factor, 8 periods @ 4% (support)",
     "value": float(pv_factor.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "a: semiannual cash interest payment (250,000 x 3%)", "value": I(cash_interest)},
    {"label": "a: issue price (proceeds) of the bonds", "value": I(issue_price)},
    {"label": "a: discount on bonds payable at issuance", "value": I(discount)},
]

for r in rows:
    p = r["p"]
    answers += [
        {"label": f"b: period {p} - beginning carrying value", "value": I(r["beg"])},
        {"label": f"b: period {p} - cash interest paid", "value": I(r["cash"])},
        {"label": f"b: period {p} - interest expense (4% of carrying value)", "value": I(r["exp"])},
        {"label": f"b: period {p} - discount amortization", "value": I(r["amort"])},
        {"label": f"b: period {p} - ending carrying value", "value": I(r["end"])},
    ]

answers += [
    {"label": "c: June 30, Year 1 - interest expense", "value": I(rows[0]["exp"])},
    {"label": "c: June 30, Year 1 - discount amortization", "value": I(rows[0]["amort"])},
    {"label": "c: June 30, Year 1 - cash paid", "value": I(rows[0]["cash"])},
    {"label": "c: December 31, Year 1 - interest expense", "value": I(rows[1]["exp"])},
    {"label": "c: December 31, Year 1 - discount amortization", "value": I(rows[1]["amort"])},
    {"label": "c: December 31, Year 1 - cash paid", "value": I(rows[1]["cash"])},
    {"label": "d: bonds payable, face amount at December 31, Year 1", "value": I(face)},
    {"label": "d: less unamortized discount at December 31, Year 1", "value": I(unamort_dec31_y1)},
    {"label": "d: bonds payable, net at December 31, Year 1", "value": I(bv_dec31_y1)},
    {"label": "d: Year 1 total interest expense", "value": I(y1_expense)},
    {"label": "e: December 31, Year 4 - final interest expense", "value": I(rows[-1]["exp"])},
    {"label": "e: December 31, Year 4 - final discount amortization (residual plug)", "value": I(rows[-1]["amort"])},
    {"label": "e: December 31, Year 4 - final cash interest paid", "value": I(rows[-1]["cash"])},
    {"label": "e: December 31, Year 4 - principal repaid at maturity", "value": I(face)},
]


def je(part, lines):
    dr = sum(l[1] for l in lines)
    cr = sum(l[2] for l in lines)
    assert dr == cr, (part, dr, cr)
    return {"part": part, "lines": [
        {"account": a, "debit": I(x), "credit": I(y)} for a, x, y in lines]}


Z = Decimal(0)
jes = [
    je("a", [("Cash", issue_price, Z),
             ("Discount on Bonds Payable", discount, Z),
             ("Bonds Payable", Z, face)]),
    je("c", [("Interest Expense (June 30, Year 1)", rows[0]["exp"], Z),
             ("Discount on Bonds Payable", Z, rows[0]["amort"]),
             ("Cash", Z, rows[0]["cash"])]),
    je("c", [("Interest Expense (December 31, Year 1)", rows[1]["exp"], Z),
             ("Discount on Bonds Payable", Z, rows[1]["amort"]),
             ("Cash", Z, rows[1]["cash"])]),
    je("e", [("Interest Expense (December 31, Year 4)", rows[-1]["exp"], Z),
             ("Discount on Bonds Payable", Z, rows[-1]["amort"]),
             ("Cash", Z, rows[-1]["cash"])]),
    je("e", [("Bonds Payable", face, Z),
             ("Cash", Z, face)]),
]

out = {
    "id": "agent_143#01",
    "rounding_convention": ("Decimal money only; ROUND_HALF_UP to the nearest whole dollar "
                            "on the issue price and on each period's interest expense; "
                            "amortization = expense - cash interest; final period plugs the "
                            "residual discount so carrying value equals $250,000 face."),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("Priced at 4% per semiannual period for 8 periods: PV of $7,500 annuity plus PV of "
              "$250,000 face. Discount, so carrying value and interest expense rise each period. "
              "Maturity split into the final interest entry and the principal repayment; no prior "
              "Interest Payable accrual exists because interest is paid on the December 31 year-end."),
}
print(json.dumps(out, indent=1))
