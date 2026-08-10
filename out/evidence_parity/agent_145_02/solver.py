"""Solver for agent_145#02 — Cascade Brewing Co. straight-line discount amortization.

Rounding convention: all money is decimal.Decimal, quantized to $0.01 using
ROUND_HALF_UP each period. Straight-line amortization per period is computed as
initial discount / number of periods, rounded HALF_UP per period; the final
period absorbs any residual rounding plug so the discount is fully amortized and
carrying value equals face at maturity. No floats. Every figure derived from the
scenario inputs; nothing hard-coded beyond the stated facts.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---- Given facts ----
FACE = Decimal("100000")
COUPON = Decimal("0.08")
PROCEEDS = Decimal("95026")
YEARS = 3

# ---- Derived ----
discount0 = q(FACE - PROCEEDS)
cash_int = q(FACE * COUPON)
amort_std = q(discount0 / Decimal(YEARS))

rows = []
carry = PROCEEDS
unamort = discount0
for yr in range(1, YEARS + 1):
    beg_carry = q(carry)
    beg_unamort = q(unamort)
    amort = amort_std if yr < YEARS else beg_unamort  # final period plug
    exp = q(cash_int + amort)
    unamort = q(beg_unamort - amort)
    carry = q(beg_carry + amort)
    rows.append({"year": yr, "beg_carry": beg_carry, "cash": cash_int,
                 "amort": amort, "exp": exp, "end_unamort": unamort,
                 "end_carry": carry})

answers = [
    {"label": "a: Issuance JE — Cash debited (proceeds)", "value": n(PROCEEDS)},
    {"label": "a: Issuance JE — Discount on Bonds Payable debited", "value": n(discount0)},
    {"label": "a: Issuance JE — Bonds Payable credited (face)", "value": n(FACE)},
    {"label": "b: Annual cash interest payment (8% x $100,000)", "value": n(cash_int)},
    {"label": "b: Straight-line discount amortization per year ($4,974 / 3)", "value": n(amort_std)},
    {"label": "b: Annual interest expense (cash interest + amortization)", "value": n(rows[0]["exp"])},
]
for r in rows:
    y = r["year"]
    answers += [
        {"label": f"b: Year {y} — beginning carrying value", "value": n(r["beg_carry"])},
        {"label": f"b: Year {y} — cash interest paid", "value": n(r["cash"])},
        {"label": f"b: Year {y} — discount amortization", "value": n(r["amort"])},
        {"label": f"b: Year {y} — interest expense", "value": n(r["exp"])},
        {"label": f"b: Year {y} — unamortized discount at year-end", "value": n(r["end_unamort"])},
        {"label": f"b: Year {y} — ending carrying value", "value": n(r["end_carry"])},
    ]
answers += [
    {"label": "b: Total cash interest paid over 3 years", "value": n(sum((r["cash"] for r in rows), Decimal(0)))},
    {"label": "b: Total discount amortized over 3 years", "value": n(sum((r["amort"] for r in rows), Decimal(0)))},
    {"label": "b: Total interest expense over 3 years", "value": n(sum((r["exp"] for r in rows), Decimal(0)))},
    {"label": "c: Dec 31 Year 1 — interest expense debited", "value": n(rows[0]["exp"])},
    {"label": "c: Dec 31 Year 1 — discount amortization credited", "value": n(rows[0]["amort"])},
    {"label": "c: Dec 31 Year 1 — cash paid", "value": n(rows[0]["cash"])},
    {"label": "c: Dec 31 Year 2 — interest expense debited", "value": n(rows[1]["exp"])},
    {"label": "c: Dec 31 Year 2 — discount amortization credited", "value": n(rows[1]["amort"])},
    {"label": "c: Dec 31 Year 2 — cash paid", "value": n(rows[1]["cash"])},
    {"label": "d: Dec 31 Year 3 — final interest expense debited", "value": n(rows[2]["exp"])},
    {"label": "d: Dec 31 Year 3 — final discount amortization credited", "value": n(rows[2]["amort"])},
    {"label": "d: Dec 31 Year 3 — cash paid for interest", "value": n(rows[2]["cash"])},
    {"label": "d: Dec 31 Year 3 — unamortized discount after final amortization", "value": n(rows[2]["end_unamort"])},
    {"label": "d: Dec 31 Year 3 — carrying value at maturity (equals face)", "value": n(rows[2]["end_carry"])},
    {"label": "d: Maturity settlement — Bonds Payable debited / Cash credited", "value": n(FACE)},
    {"label": "e: Straight-line acceptable under ASC 835-30 only when results are not materially different from the effective interest method (effective interest is the required/preferred method; straight-line is permitted as a practical expedient when the difference is immaterial). Here $1,658 per year vs. effective-interest amounts differ immaterially, so straight-line is acceptable.",
     "value": "Permitted only if not materially different from effective interest"},
    {"label": "e: Reporting of unamortized discount — presented on the balance sheet as a direct deduction (contra-liability) from the face amount of Bonds Payable, not as an asset; the net carrying value is reported in long-term liabilities until the final year, when it becomes a current liability. Amortization is reported as part of interest expense on the income statement.",
     "value": "Direct deduction from the face of Bonds Payable (contra-liability); net carrying value shown"},
    {"label": "e: Year-end unamortized discount balances reported (Y1, Y2, Y3)",
     "value": f"{n(rows[0]['end_unamort'])}, {n(rows[1]['end_unamort'])}, {n(rows[2]['end_unamort'])}"},
]

def je(part, lines):
    d = sum((Decimal(str(l[1])) for l in lines), Decimal(0))
    c = sum((Decimal(str(l[2])) for l in lines), Decimal(0))
    assert q(d) == q(c), (part, d, c)
    return {"part": part, "lines": [{"account": a, "debit": n(dr), "credit": n(cr)} for a, dr, cr in lines]}

jes = [
    je("a", [("Cash", PROCEEDS, Decimal(0)),
             ("Discount on Bonds Payable", discount0, Decimal(0)),
             ("Bonds Payable", Decimal(0), FACE)]),
    je("c", [("Interest Expense", rows[0]["exp"], Decimal(0)),
             ("Discount on Bonds Payable", Decimal(0), rows[0]["amort"]),
             ("Cash", Decimal(0), rows[0]["cash"])]),
    je("c", [("Interest Expense", rows[1]["exp"], Decimal(0)),
             ("Discount on Bonds Payable", Decimal(0), rows[1]["amort"]),
             ("Cash", Decimal(0), rows[1]["cash"])]),
    je("d", [("Interest Expense", rows[2]["exp"], Decimal(0)),
             ("Discount on Bonds Payable", Decimal(0), rows[2]["amort"]),
             ("Cash", Decimal(0), rows[2]["cash"])]),
    je("d", [("Bonds Payable", FACE, Decimal(0)),
             ("Cash", Decimal(0), FACE)]),
]

out = {
    "id": "agent_145#02",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to $0.01 each period; straight-line amortization = initial discount / 3 periods with the final period absorbing any rounding residual so the discount is fully amortized and carrying value equals face at maturity.",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "JE dates: part a = Jan 1 Year 1 issuance; part c JEs = Dec 31 Year 1 then Dec 31 Year 2; part d JEs = Dec 31 Year 3 final interest, then Dec 31 Year 3 maturity settlement of principal (the Year 3 interest and principal payments could also be shown as one combined $108,000 cash disbursement). Straight-line yields constant interest expense of $9,658 per year, unlike effective interest where expense rises with the carrying value; total 3-year expense ($28,974) is the same under both methods. Every amount derived from face $100,000, 8% coupon, $95,026 proceeds, 3 annual periods.",
}
print(json.dumps(out, indent=1))
