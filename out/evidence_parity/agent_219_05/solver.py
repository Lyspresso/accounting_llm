"""Solver for agent_219#05 — Meridian Optics Corp. patent full life cycle.

Rounding convention: all money is decimal.Decimal, quantized to cents
(0.01) with ROUND_HALF_UP independently in each period (no float use,
no carry-forward of unrounded residue). Every figure is derived from the
scenario inputs; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- inputs ----
COST = Decimal("96000")
LIFE = Decimal("8")
RESIDUAL = Decimal("0")
IMPAIR_YEAR = 3
UNDISC = Decimal("52000")
FAIR_VALUE = Decimal("48000")
REMAIN_LIFE = Decimal("5")
SALE_PRICE = Decimal("18500")
SALE_MONTHS = Decimal("9")   # Jan 1 -> Oct 1, Year 6
MONTHS_YR = Decimal("12")

answers = []
rows = []

# ---- pre-impairment amortization (Years 1-3) ----
annual_pre = q((COST - RESIDUAL) / LIFE)
cv = COST
for yr in range(1, IMPAIR_YEAR + 1):
    beg = cv
    amt = annual_pre
    cv = q(beg - amt)
    rows.append((yr, beg, amt, cv))

# ---- impairment test at 12/31 Year 3 (after Year 3 amortization) ----
cv_before_imp = cv
impaired = UNDISC < cv_before_imp
imp_loss = q(cv_before_imp - FAIR_VALUE) if impaired else Decimal("0")
cv = q(cv_before_imp - imp_loss)
cv_after_imp = cv

# ---- post-impairment amortization ----
annual_post = q((cv_after_imp - RESIDUAL) / REMAIN_LIFE)
post_rows = []
for yr in range(IMPAIR_YEAR + 1, IMPAIR_YEAR + 1 + 2):   # Years 4 and 5 (schedule ends Year 5)
    beg = cv
    amt = annual_post
    cv = q(beg - amt)
    post_rows.append((yr, beg, amt, cv))
cv_end_y5 = cv

# ---- Year 6 partial amortization to Oct 1 and disposal ----
amort_y6 = q(annual_post * SALE_MONTHS / MONTHS_YR)
cv_at_sale = q(cv_end_y5 - amort_y6)
gain = q(SALE_PRICE - cv_at_sale)

# ---- part a: schedule ----
for yr, beg, amt, end in rows:
    answers.append({"label": f"a: Year {yr} — beginning carrying amount", "value": n(beg)})
    answers.append({"label": f"a: Year {yr} — amortization expense", "value": n(amt)})
    answers.append({"label": f"a: Year {yr} — ending carrying amount", "value": n(end)})

answers.append({"label": "a: 12/31 Year 3 impairment row — carrying amount before impairment", "value": n(cv_before_imp)})
answers.append({"label": "a: 12/31 Year 3 impairment row — undiscounted future net cash inflows (recoverability test)", "value": n(UNDISC)})
answers.append({"label": "a: 12/31 Year 3 impairment row — impairment loss", "value": n(imp_loss)})
answers.append({"label": "a: 12/31 Year 3 impairment row — carrying amount after impairment (new basis = fair value)", "value": n(cv_after_imp)})
answers.append({"label": "a: post-impairment annual amortization (Years 4-8, 5-year remaining life)", "value": n(annual_post)})

for yr, beg, amt, end in post_rows:
    answers.append({"label": f"a: Year {yr} — beginning carrying amount", "value": n(beg)})
    answers.append({"label": f"a: Year {yr} — amortization expense", "value": n(amt)})
    answers.append({"label": f"a: Year {yr} — ending carrying amount", "value": n(end)})

# ---- part c ----
answers.append({"label": "c: carrying amount at Oct 1, Year 6 (after 9 months of Year 6 amortization)", "value": n(cv_at_sale)})
answers.append({"label": "c: gain (positive) or loss (negative) on disposal — loss", "value": n(gain)})

# ---- part b: journal entries ----
def je(part, lines):
    dr = sum(Decimal(str(l[1])) for l in lines)
    cr = sum(Decimal(str(l[2])) for l in lines)
    assert q(dr) == q(cr), (part, dr, cr)
    return {"part": part, "lines": [{"account": a, "debit": n(d), "credit": n(c)} for a, d, c in lines]}

y3_amort = rows[IMPAIR_YEAR - 1][2]
y4_amort = post_rows[0][2]
loss_on_sale = -gain if gain < 0 else Decimal("0")
gain_on_sale = gain if gain > 0 else Decimal("0")

disposal_lines = [("Cash", SALE_PRICE, Decimal("0"))]
if loss_on_sale > 0:
    disposal_lines.append(("Loss on Disposal of Patent", loss_on_sale, Decimal("0")))
disposal_lines.append(("Patent", Decimal("0"), cv_at_sale))
if gain_on_sale > 0:
    disposal_lines.append(("Gain on Disposal of Patent", Decimal("0"), gain_on_sale))

journal_entries = [
    je("b(1) Jan 1, Year 1 — acquisition of patent for cash", [
        ("Patent", COST, Decimal("0")),
        ("Cash", Decimal("0"), COST),
    ]),
    je("b(2) Dec 31, Year 3 — annual amortization", [
        ("Amortization Expense", y3_amort, Decimal("0")),
        ("Patent", Decimal("0"), y3_amort),
    ]),
    je("b(3) Dec 31, Year 3 — impairment loss (write down to fair value)", [
        ("Loss on Impairment of Patent", imp_loss, Decimal("0")),
        ("Patent", Decimal("0"), imp_loss),
    ]),
    je("b(4) Dec 31, Year 4 — annual amortization on new basis", [
        ("Amortization Expense", y4_amort, Decimal("0")),
        ("Patent", Decimal("0"), y4_amort),
    ]),
    je("b(5) Oct 1, Year 6 — amortization for 9 months of Year 6", [
        ("Amortization Expense", amort_y6, Decimal("0")),
        ("Patent", Decimal("0"), amort_y6),
    ]),
    je("b(6) Oct 1, Year 6 — sale of patent for cash", disposal_lines),
]

out = {
    "id": "agent_219#05",
    "rounding_convention": "decimal.Decimal throughout; each period's amount quantized to cents with ROUND_HALF_UP; no floats",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": ("Recoverability test at 12/31/Y3 after Y3 amortization: undiscounted cash flows 52,000 < carrying amount "
              "60,000, so the patent is impaired; loss = 60,000 carrying - 48,000 fair value = 12,000, and 48,000 becomes "
              "the new basis amortized over the 5-year remaining life at 9,600/yr. Year 6 amortization runs 9 months "
              "(Jan 1 to Oct 1) = 7,200, leaving a 21,600 carrying amount; 18,500 cash proceeds produce a 3,100 LOSS on "
              "disposal (reported as -3100 in part c). Patent is credited directly (no accumulated amortization account).")
}
print(json.dumps(out, indent=1))
