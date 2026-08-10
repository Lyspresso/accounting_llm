"""Cascade Peak Logistics Inc. discount bond (LO 16-2) - independent derivation.

Facts: $250,000 face, 6% stated (annual), issued 1/1/Y1, matures 12/31/Y4,
semiannual interest 6/30 and 12/31, market yield 8% annual. Effective interest.

Rounding convention: all money as decimal.Decimal. Present values computed at
full Decimal precision (28 sig digits) then the issue price is rounded to the
nearest dollar with ROUND_HALF_UP. The amortization schedule and all journal
entries are stated in whole dollars, with each period's interest expense =
carrying value x 4% rounded ROUND_HALF_UP to the nearest dollar; the FINAL
period's amortization is plugged as the residual so the carrying value closes
EXACTLY to face ($250,000) and the discount closes exactly to zero.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP

getcontext().prec = 40
C = D("0.01")


def d0(x):
    return x.quantize(D("1"), rounding=ROUND_HALF_UP)


face = D("250000")
stated_annual = D("0.06")
market_annual = D("0.08")
periods_per_year = 2
years = 4
n = years * periods_per_year          # 8
i = market_annual / periods_per_year  # 0.04
cash_int = face * stated_annual / periods_per_year  # 7500

# ---- (a) issue price: PV of principal + PV of annuity of interest, full precision
one_plus = D(1) + i
disc_factor = one_plus ** n                 # (1.04)^8
pv_principal_exact = face / disc_factor
annuity_factor = (D(1) - (D(1) / disc_factor)) / i
pv_interest_exact = cash_int * annuity_factor
issue_exact = pv_principal_exact + pv_interest_exact
issue = d0(issue_exact)
discount = face - issue

answers = []
jes = []

answers.append({"label": "a: Semiannual periods (n)", "value": int(n)})
answers.append({"label": "a: Semiannual market (effective) rate per period",
                "value": float(i)})
answers.append({"label": "a: Semiannual cash interest payment (250,000 x 6% x 6/12)",
                "value": int(cash_int)})
answers.append({"label": "a: PV of principal ($250,000 x PV1, 4%, 8 = 0.730690)",
                "value": int(d0(pv_principal_exact))})
answers.append({"label": "a: PV of interest annuity ($7,500 x PVOA, 4%, 8 = 6.732745)",
                "value": int(d0(pv_interest_exact))})
answers.append({"label": "a: Issue price (proceeds), rounded", "value": int(issue)})
answers.append({"label": "a: Discount on bonds payable at issuance", "value": int(discount)})
answers.append({"label": "a: Face value of bonds", "value": int(face)})

jes.append({"part": "a", "description": "Jan 1, Year 1 - issuance of bonds at a discount",
            "lines": [
                {"account": "Cash", "debit": int(issue), "credit": 0},
                {"account": "Discount on Bonds Payable", "debit": int(discount), "credit": 0},
                {"account": "Bonds Payable", "debit": 0, "credit": int(face)},
            ]})

# ---- (b) full effective-interest schedule (whole dollars, residual plug in period 8)
carry = issue
rows = []
total_int_exp = D(0)
total_cash = D(0)
total_amort = D(0)
for p in range(1, n + 1):
    if p < n:
        int_exp = d0(carry * i)
        amort = int_exp - cash_int
    else:
        # final period: plug residual so carrying value closes exactly to face
        amort = face - carry
        int_exp = cash_int + amort
    begin = carry
    carry = carry + amort
    disc_bal = face - carry
    rows.append({"period": p, "begin_carry": begin, "cash_int": cash_int,
                 "int_exp": int_exp, "amort": amort, "disc_bal": disc_bal,
                 "end_carry": carry})
    total_int_exp += int_exp
    total_cash += cash_int
    total_amort += amort

assert carry == face, carry
assert total_amort == discount, (total_amort, discount)

period_dates = ["6/30/Y1", "12/31/Y1", "6/30/Y2", "12/31/Y2",
                "6/30/Y3", "12/31/Y3", "6/30/Y4", "12/31/Y4"]

for r in rows:
    dt = period_dates[r["period"] - 1]
    pre = "b: Period %d (%s)" % (r["period"], dt)
    answers.append({"label": pre + " beginning carrying value", "value": int(r["begin_carry"])})
    answers.append({"label": pre + " cash interest paid", "value": int(r["cash_int"])})
    answers.append({"label": pre + " interest expense (4% x beginning CV)", "value": int(r["int_exp"])})
    answers.append({"label": pre + " discount amortization", "value": int(r["amort"])})
    answers.append({"label": pre + " unamortized discount balance (end)", "value": int(r["disc_bal"])})
    answers.append({"label": pre + " ending carrying value", "value": int(r["end_carry"])})

answers.append({"label": "b: Total cash interest paid over 8 periods", "value": int(total_cash)})
answers.append({"label": "b: Total interest expense over 8 periods", "value": int(total_int_exp)})
answers.append({"label": "b: Total discount amortized over 8 periods", "value": int(total_amort)})
answers.append({"label": "b: Final-period residual amortization plug", "value": int(rows[-1]["amort"])})
answers.append({"label": "b: Ending carrying value at maturity (closes to face)", "value": int(rows[-1]["end_carry"])})

# ---- (c) Year 1 interest JEs
for idx, lbl in ((0, "June 30, Year 1"), (1, "December 31, Year 1")):
    r = rows[idx]
    jes.append({"part": "c",
                "description": "%s - semiannual interest payment and discount amortization (period %d)" % (lbl, r["period"]),
                "lines": [
                    {"account": "Interest Expense", "debit": int(r["int_exp"]), "credit": 0},
                    {"account": "Discount on Bonds Payable", "debit": 0, "credit": int(r["amort"])},
                    {"account": "Cash", "debit": 0, "credit": int(r["cash_int"])},
                ]})

# ---- (d) presentation at 12/31/Y1
y1_int_exp = rows[0]["int_exp"] + rows[1]["int_exp"]
y1_cash = rows[0]["cash_int"] + rows[1]["cash_int"]
y1_amort = rows[0]["amort"] + rows[1]["amort"]
cv_1231y1 = rows[1]["end_carry"]
disc_1231y1 = rows[1]["disc_bal"]

answers.append({"label": "c: June 30 Year 1 interest expense", "value": int(rows[0]["int_exp"])})
answers.append({"label": "c: June 30 Year 1 discount amortization", "value": int(rows[0]["amort"])})
answers.append({"label": "c: June 30 Year 1 cash paid", "value": int(rows[0]["cash_int"])})
answers.append({"label": "c: Dec 31 Year 1 interest expense", "value": int(rows[1]["int_exp"])})
answers.append({"label": "c: Dec 31 Year 1 discount amortization", "value": int(rows[1]["amort"])})
answers.append({"label": "c: Dec 31 Year 1 cash paid", "value": int(rows[1]["cash_int"])})

answers.append({"label": "d: Bonds payable (face) at 12/31/Y1", "value": int(face)})
answers.append({"label": "d: Less unamortized discount at 12/31/Y1", "value": int(disc_1231y1)})
answers.append({"label": "d: Bonds payable, net (carrying value) at 12/31/Y1", "value": int(cv_1231y1)})
answers.append({"label": "d: Year 1 total interest expense", "value": int(y1_int_exp)})
answers.append({"label": "d: Year 1 total cash interest paid", "value": int(y1_cash)})
answers.append({"label": "d: Year 1 total discount amortization", "value": int(y1_amort)})

# ---- (e) maturity 12/31/Y4
r8 = rows[-1]
jes.append({"part": "e",
            "description": "December 31, Year 4 - final semiannual interest and residual discount amortization (period 8)",
            "lines": [
                {"account": "Interest Expense", "debit": int(r8["int_exp"]), "credit": 0},
                {"account": "Discount on Bonds Payable", "debit": 0, "credit": int(r8["amort"])},
                {"account": "Cash", "debit": 0, "credit": int(r8["cash_int"])},
            ]})
jes.append({"part": "e",
            "description": "December 31, Year 4 - repayment of principal at maturity",
            "lines": [
                {"account": "Bonds Payable", "debit": int(face), "credit": 0},
                {"account": "Cash", "debit": 0, "credit": int(face)},
            ]})

answers.append({"label": "e: Final period interest expense (12/31/Y4)", "value": int(r8["int_exp"])})
answers.append({"label": "e: Final period discount amortization (residual plug)", "value": int(r8["amort"])})
answers.append({"label": "e: Final period cash interest paid", "value": int(r8["cash_int"])})
answers.append({"label": "e: Unamortized discount after final amortization", "value": int(r8["disc_bal"])})
answers.append({"label": "e: Principal repaid at maturity", "value": int(face)})
answers.append({"label": "e: Total cash paid on 12/31/Y4 (interest + principal)",
                "value": int(r8["cash_int"] + face)})
answers.append({"label": "e: Gain or loss on retirement at maturity", "value": 0})

# Dr = Cr check on every entry
for je in jes:
    dr = sum(D(str(l["debit"])) for l in je["lines"])
    cr = sum(D(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je["description"], dr, cr)

unplugged_final = d0(rows[-1]["begin_carry"] * i) - cash_int
notes = (
    "Discount bond: market 8 percent exceeds stated 6 percent, so proceeds are below face. "
    f"PVs run at full Decimal precision; issue price rounded ROUND_HALF_UP to ${issue} "
    f"(discount ${discount}). Schedule and JEs in whole dollars; each period's interest expense "
    "= 4 percent x beginning carrying value, rounded ROUND_HALF_UP; the period-8 amortization is "
    f"plugged as the residual (${int(rows[-1]['amort'])} instead of the formula-only "
    f"${int(unplugged_final)}) so carrying value closes EXACTLY to $250,000 face and unamortized "
    f"discount closes exactly to $0. Total interest expense ${int(total_int_exp)} = total cash "
    f"interest ${int(total_cash)} + total discount amortized ${int(total_amort)}. No prior Interest "
    "Payable, so 12/31/Y4 records the final interest entry plus a separate principal repayment; "
    "no gain or loss arises at maturity because carrying value equals face.")

import json
print(json.dumps({
    "id": "agent_143#01",
    "rounding_convention": ("decimal.Decimal throughout, ROUND_HALF_UP; PVs at full precision, "
                            "issue price and every schedule/JE amount stated in whole dollars; "
                            "final-period amortization plugged as residual so the schedule closes "
                            "exactly to $250,000 face and $0 unamortized discount"),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
