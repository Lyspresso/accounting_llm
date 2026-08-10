"""Copper Ridge Utilities -- 4-yr 6% bonds, $400,000 face, 8% yield, issued $373,503.

Rounding convention: all money is decimal.Decimal. Each period's effective-interest
expense is rounded to the nearest whole dollar with ROUND_HALF_UP; discount
amortization = rounded expense - cash interest. In the FINAL period of each bond
layer the amortization is plugged (expense = cash interest + remaining unamortized
discount) so carrying value closes exactly on face. Nothing is hard-coded: every
figure is derived from face, coupon rate, yield, issue price, retirement fraction
and call price.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("1")
def r(x):  # whole dollars, ROUND_HALF_UP
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

FACE   = Decimal("400000")
COUPON = Decimal("0.06")
YIELD  = Decimal("0.08")
PRICE  = Decimal("373503")
N      = 4
FRAC   = Decimal("0.50")          # retired at end of Year 2
CALL   = Decimal("103") / Decimal("100")
RETIRE_AFTER = 2                  # periods elapsed before retirement

DISCOUNT = FACE - PRICE
CASH_INT = r(FACE * COUPON)

# ---- (b) full effective-interest schedule, Years 1-4 -------------------------
sched = []
cv = PRICE
for yr in range(1, N + 1):
    beg = cv
    if yr == N:
        amort = FACE - beg
        exp = CASH_INT + amort
    else:
        exp = r(beg * YIELD)
        amort = exp - CASH_INT
    cv = beg + amort
    sched.append({"year": yr, "beg": beg, "exp": exp, "cash": CASH_INT,
                  "amort": amort, "end": cv, "unamort": FACE - cv})

tot_exp   = sum(x["exp"] for x in sched)
tot_cash  = sum(x["cash"] for x in sched)
tot_amort = sum(x["amort"] for x in sched)

# ---- (c) Dec 31 Year 2 interest, then 50% extinguishment ---------------------
y2 = sched[RETIRE_AFTER - 1]
cv_after_y2   = y2["end"]
unamort_after = FACE - cv_after_y2

face_ret    = r(FACE * FRAC)
cv_ret      = r(cv_after_y2 * FRAC)
disc_ret    = face_ret - cv_ret                 # unamortized discount removed
reacq_price = r(face_ret * CALL)
gain_loss   = cv_ret - reacq_price              # negative => loss
loss        = -gain_loss

# ---- (d) remaining half, Years 3-4 ------------------------------------------
face_rem = FACE - face_ret
cash_rem = r(face_rem * COUPON)
half = []
cvh = cv_ret
for yr in range(RETIRE_AFTER + 1, N + 1):
    beg = cvh
    if yr == N:
        am = face_rem - beg
        ex = cash_rem + am
    else:
        ex = r(beg * YIELD)
        am = ex - cash_rem
    cvh = beg + am
    half.append({"year": yr, "beg": beg, "exp": ex, "cash": cash_rem,
                 "amort": am, "end": cvh})

def f(x):
    return float(Decimal(x).quantize(C, rounding=ROUND_HALF_UP))

A = []
def add(lbl, v):
    A.append({"label": lbl, "value": f(v)})

# a
add("a: Cash debited on issuance (Jan 1, Year 1)", PRICE)
add("a: Discount on Bonds Payable debited on issuance", DISCOUNT)
add("a: Bonds Payable credited on issuance", FACE)

# b
for s in sched:
    y = s["year"]
    add(f"b: Year {y} beginning carrying value", s["beg"])
    add(f"b: Year {y} interest expense (8% x beginning carrying value)", s["exp"])
    add(f"b: Year {y} cash interest paid (6% x face)", s["cash"])
    add(f"b: Year {y} discount amortization", s["amort"])
    add(f"b: Year {y} ending carrying value", s["end"])
    add(f"b: Year {y} unamortized discount at year-end", s["unamort"])
add("b: Total interest expense, Years 1-4", tot_exp)
add("b: Total cash interest paid, Years 1-4", tot_cash)
add("b: Total discount amortized, Years 1-4", tot_amort)

# c
add("c: Dec 31 Year 2 interest expense", y2["exp"])
add("c: Dec 31 Year 2 discount amortization", y2["amort"])
add("c: Dec 31 Year 2 cash interest paid", y2["cash"])
add("c: Carrying value of all bonds after Dec 31 Year 2 entry", cv_after_y2)
add("c: Unamortized discount on all bonds after Dec 31 Year 2 entry", unamort_after)
add("c: Face amount retired (50%)", face_ret)
add("c: Carrying value of the 50% retired", cv_ret)
add("c: Unamortized discount removed on the 50% retired", disc_ret)
add("c: Reacquisition price paid (50% face x 103)", reacq_price)
add("c: Loss on extinguishment (reacquisition price - carrying value)", loss)

# d
add("d: Face of bonds remaining after retirement", face_rem)
add("d: Carrying value of remaining half at Jan 1, Year 3", cv_ret)
add("d: Annual cash interest on remaining half (6% x $200,000)", cash_rem)
for s in half:
    y = s["year"]
    add(f"d: Year {y} beginning carrying value (remaining half)", s["beg"])
    add(f"d: Year {y} interest expense (remaining half)", s["exp"])
    add(f"d: Year {y} cash interest paid (remaining half)", s["cash"])
    add(f"d: Year {y} discount amortization (remaining half)", s["amort"])
    add(f"d: Year {y} ending carrying value (remaining half)", s["end"])
add("d: Maturity payment Dec 31, Year 4 (remaining half at par)", face_rem)

def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": f(dr) if dr is not None else 0,
            "credit": f(cr) if cr is not None else 0}

JE = [
 {"part": "a", "lines": [
    L("Cash", dr=PRICE),
    L("Discount on Bonds Payable", dr=DISCOUNT),
    L("Bonds Payable", cr=FACE)]},
 {"part": "c", "lines": [
    L("Interest Expense", dr=y2["exp"]),
    L("Discount on Bonds Payable", cr=y2["amort"]),
    L("Cash", cr=y2["cash"])]},
 {"part": "c", "lines": [
    L("Bonds Payable", dr=face_ret),
    L("Loss on Extinguishment of Debt", dr=loss),
    L("Discount on Bonds Payable", cr=disc_ret),
    L("Cash", cr=reacq_price)]},
]
for s in half:
    JE.append({"part": "d", "lines": [
        L("Interest Expense", dr=s["exp"]),
        L("Discount on Bonds Payable", cr=s["amort"]),
        L("Cash", cr=s["cash"])]})
JE.append({"part": "d", "lines": [
    L("Bonds Payable", dr=face_rem),
    L("Cash", cr=face_rem)]})

for e in JE:
    d = sum(Decimal(str(x["debit"])) for x in e["lines"])
    c = sum(Decimal(str(x["credit"])) for x in e["lines"])
    assert d == c, (e["part"], d, c)
assert sched[-1]["end"] == FACE and half[-1]["end"] == face_rem

print(json.dumps({
 "id": "agent_279#01",
 "rounding_convention": ("decimal.Decimal throughout; interest expense rounded to "
   "the nearest whole dollar each period with ROUND_HALF_UP; amortization = rounded "
   "expense - cash interest; final period of each layer plugged so carrying value "
   "equals face exactly"),
 "answers": A,
 "journal_entries": JE,
 "insufficient_info": False,
 "notes": ("Discount = 400,000 - 373,503 = 26,497. Retirement occurs after the Dec 31 "
   "Year 2 entry, so the 50% layer carries at 50% x 385,734 = 192,867 versus 206,000 "
   "paid, a 13,133 loss. The remaining half is re-amortized on its own 192,867 base at "
   "8% (Year 4 plugged to 200,000), so its Year 3-4 expense is not exactly half of the "
   "original schedule rows.")
}, indent=1))
