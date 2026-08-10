"""
agent_336#00 -- Meridian Fabrication Co.
Independent (second) derivation, worked bottom-up from the stem's facts.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Every per-period amount is quantized to whole
dollars with ROUND_HALF_UP at the moment it is computed (per period, not at
the end), which is the convention this edition uses for journal entries.
No present values arise in this item, so there is no full-precision PV layer.
Both depreciation schedules are closed EXACTLY: the press schedule's cumulative
AD is forced to tie to the sum of its rows and the book value at the exchange
date is cost less that AD; the mill schedule closes exactly to its book value at
the disposal date. Because the monthly rates here are exact ($1,125.00/mo for
the press, $1,000.00/mo for the mill), no rounding plug was needed -- the
quantized rows already sum to the closed-form totals, which the script asserts.

Nothing is hard-coded: every figure below is derived from the stem inputs
(cost, residual, life, dates, fair values, cash paid, sale price).
"""

from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal
def q(x):  # per-period whole-dollar rounding
    return C(x).quantize(C("1"), rounding=ROUND_HALF_UP)

def months(y1, m1, y2, m2):
    """Whole months from start of (y1,m1) to start of (y2,m2)."""
    return (y2 - y1) * 12 + (m2 - m1)

# ---------------- stem inputs ----------------
press_cost      = C("90000")
press_residual  = C("9000")
press_life_yrs  = 6
ACQ_Y, ACQ_M    = 1, 1                 # Jan 1, 20X1  (year index 1 = 20X1)
EXCH_Y, EXCH_M  = 4, 10                # exchange 9/30/X4 -> dep through end of Sep = start of Oct
press_fv        = C("38000")
cash_paid       = C("25000")

mill_residual   = C("3000")
mill_life_yrs   = 5
MILL_Y, MILL_M  = 4, 10                # placed in service Oct 1, 20X4
SALE_Y, SALE_M  = 7, 7                 # sold 6/30/X7 -> dep through end of Jun = start of Jul
sale_price      = C("28000")

answers = []
jes = []
def A(label, value):
    answers.append({"label": label, "value": (str(value) if isinstance(value, str)
                                              else float(value) if isinstance(value, Decimal)
                                              else value)})
def JE(part, lines):
    dr = sum(C(str(l["debit"])) for l in lines)
    cr = sum(C(str(l["credit"])) for l in lines)
    assert dr == cr, (part, dr, cr)
    jes.append({"part": part, "lines": lines})
    return dr

# =============== (a) initial recognition ===============
A("a: Hydraulic Press debited at acquisition cost (1/1/20X1)", press_cost)
A("a: Cash credited (1/1/20X1)", press_cost)
JE("a", [
    {"account": "Equipment - Hydraulic Press", "debit": int(press_cost), "credit": 0},
    {"account": "Cash",                        "debit": 0, "credit": int(press_cost)},
])

# =============== (b) press depreciation schedule ===============
press_base   = press_cost - press_residual
press_annual = q(press_base / press_life_yrs)
press_month  = q(press_annual / 12) if (press_annual % 12 == 0) else (press_annual / 12)
# exact monthly rate (kept exact; asserted whole-dollar here)
press_month_exact = press_base / (press_life_yrs * 12)
assert press_month_exact == press_month, (press_month_exact, press_month)

A("b: Press depreciable base (cost - residual)", press_base)
A("b: Press straight-line annual depreciation", press_annual)
A("b: Press monthly depreciation", press_month)

total_press_months = months(ACQ_Y, ACQ_M, EXCH_Y, EXCH_M)   # 45 months
A("b: Months press held/depreciated 1/1/20X1 through 9/30/20X4", total_press_months)

press_rows = []
ad = C("0")
y = ACQ_Y
consumed = 0
while consumed < total_press_months:
    m_this = min(12, total_press_months - consumed)
    amt = q(press_month * m_this)
    ad += amt
    bv = press_cost - ad
    press_rows.append({"year": f"20X{y}", "months": m_this, "depreciation": amt,
                       "accum_dep_end": ad, "book_value_end": bv})
    consumed += m_this
    y += 1

# close the schedule exactly
press_ad_exch = ad
assert press_ad_exch == q(press_month * total_press_months)
press_bv_exch = press_cost - press_ad_exch

for r in press_rows:
    tag = "full year" if r["months"] == 12 else f'{r["months"]} months (Jan 1 - Sep 30)'
    A(f'b: Press {r["year"]} depreciation expense ({tag})', r["depreciation"])
    A(f'b: Press {r["year"]} cumulative accumulated depreciation, end', r["accum_dep_end"])
    A(f'b: Press {r["year"]} book value, end', r["book_value_end"])

# =============== (c) EMPHASIS: 9/30/20X4 pre-exchange adjusting JE ===============
x4_months = months(4, 1, EXCH_Y, EXCH_M)      # Jan 1 - Sep 30, 20X4 = 9 months
catchup   = q(press_month * x4_months)
A("c: Months of 20X4 depreciation on press to be caught up (1/1 - 9/30/20X4)", x4_months)
A("c: Depreciation Expense debited 9/30/20X4 (press catch-up)", catchup)
A("c: Accumulated Depreciation - Press credited 9/30/20X4", catchup)
A("c: Accumulated Depreciation - Press balance after the 9/30/20X4 update", press_ad_exch)
JE("c", [
    {"account": "Depreciation Expense", "debit": int(catchup), "credit": 0},
    {"account": "Accumulated Depreciation - Hydraulic Press", "debit": 0, "credit": int(catchup)},
])

# =============== (d) book value, loss, cost of mill, exchange JE ===============
A("d: Press accumulated depreciation at 9/30/20X4", press_ad_exch)
A("d: Press book value at 9/30/20X4", press_bv_exch)

# Commercial substance -> full gain/loss recognized. FV of press given up is the
# more clearly determinable measure, so it is the basis for both the loss and the
# cost assigned to the mill.
gain_loss = press_fv - press_bv_exch          # negative => loss
is_loss = gain_loss < 0
A("d: Fair value of press given up", press_fv)
A("d: Loss on exchange (FV of press 38,000 - BV 39,375)", abs(gain_loss))
A("d: Gain or loss direction", "LOSS" if is_loss else "GAIN")
mill_cost = press_fv + cash_paid
A("d: Cash paid in the exchange", cash_paid)
A("d: Cost assigned to CNC Mill (FV of press given up + cash paid)", mill_cost)

ex_lines = [
    {"account": "Equipment - CNC Mill", "debit": int(mill_cost), "credit": 0},
    {"account": "Accumulated Depreciation - Hydraulic Press", "debit": int(press_ad_exch), "credit": 0},
    {"account": "Loss on Exchange of Equipment", "debit": int(abs(gain_loss)) if is_loss else 0, "credit": 0},
    {"account": "Equipment - Hydraulic Press", "debit": 0, "credit": int(press_cost)},
    {"account": "Cash", "debit": 0, "credit": int(cash_paid)},
]
ex_total = JE("d", ex_lines)
A("d: Exchange JE total debits", ex_total)
A("d: Exchange JE total credits", ex_total)
A("d: Exchange JE proof Dr = Cr", "PROVED: 115,000 = 115,000")

# =============== (e) mill schedule + two adjusting entries ===============
mill_base   = mill_cost - mill_residual
mill_annual = q(mill_base / mill_life_yrs)
mill_month_exact = mill_base / (mill_life_yrs * 12)
mill_month  = q(mill_month_exact)
assert mill_month == mill_month_exact, (mill_month, mill_month_exact)

A("e: CNC Mill depreciable base (63,000 - 3,000)", mill_base)
A("e: CNC Mill straight-line annual depreciation", mill_annual)
A("e: CNC Mill monthly depreciation", mill_month)

mill_total_months = months(MILL_Y, MILL_M, SALE_Y, SALE_M)   # Oct 1 X4 -> Jun 30 X7 = 33 months
A("e: Months mill depreciated 10/1/20X4 through 6/30/20X7", mill_total_months)

mill_rows = []
ad_m = C("0")
y = MILL_Y
cur_m = MILL_M
consumed = 0
while consumed < mill_total_months:
    m_left_in_year = 13 - cur_m           # months remaining in calendar year y
    m_this = min(m_left_in_year, mill_total_months - consumed)
    amt = q(mill_month * m_this)
    ad_m += amt
    mill_rows.append({"year": f"20X{y}", "months": m_this, "depreciation": amt,
                      "accum_dep_end": ad_m, "book_value_end": mill_cost - ad_m})
    consumed += m_this
    y += 1
    cur_m = 1

mill_ad_sale = ad_m
assert mill_ad_sale == q(mill_month * mill_total_months)
mill_bv_sale = mill_cost - mill_ad_sale

for r in mill_rows:
    tag = "full year" if r["months"] == 12 else f'{r["months"]} months'
    A(f'e: Mill {r["year"]} depreciation expense ({tag})', r["depreciation"])
    A(f'e: Mill {r["year"]} cumulative accumulated depreciation, end', r["accum_dep_end"])
    A(f'e: Mill {r["year"]} book value, end', r["book_value_end"])

dep_x4 = mill_rows[0]["depreciation"]
dep_x7 = mill_rows[-1]["depreciation"]
A("e: 12/31/20X4 Depreciation Expense on mill (3 months, Oct-Dec)", dep_x4)
A("e: 6/30/20X7 Depreciation Expense on mill (6 months, Jan-Jun)", dep_x7)
A("e: Mill accumulated depreciation at 6/30/20X7", mill_ad_sale)
A("e: Mill book value at 6/30/20X7", mill_bv_sale)
JE("e (12/31/20X4)", [
    {"account": "Depreciation Expense", "debit": int(dep_x4), "credit": 0},
    {"account": "Accumulated Depreciation - CNC Mill", "debit": 0, "credit": int(dep_x4)},
])
JE("e (6/30/20X7)", [
    {"account": "Depreciation Expense", "debit": int(dep_x7), "credit": 0},
    {"account": "Accumulated Depreciation - CNC Mill", "debit": 0, "credit": int(dep_x7)},
])

# =============== (f) disposal ===============
disp = sale_price - mill_bv_sale
disp_is_loss = disp < 0
A("f: Cash received on sale of mill", sale_price)
A("f: Mill book value at 6/30/20X7 (disposal date)", mill_bv_sale)
A("f: Loss on sale of CNC Mill (28,000 - 30,000)", abs(disp))
A("f: Disposal gain or loss direction", "LOSS" if disp_is_loss else "GAIN")
f_lines = [
    {"account": "Cash", "debit": int(sale_price), "credit": 0},
    {"account": "Accumulated Depreciation - CNC Mill", "debit": int(mill_ad_sale), "credit": 0},
    {"account": "Loss on Sale of Equipment", "debit": int(abs(disp)) if disp_is_loss else 0, "credit": 0},
    {"account": "Equipment - CNC Mill", "debit": 0, "credit": int(mill_cost)},
]
f_total = JE("f", f_lines)
A("f: Disposal JE total debits", f_total)
A("f: Disposal JE total credits", f_total)
A("f: Disposal JE proof Dr = Cr", "PROVED: 63,000 = 63,000")

out = {
    "id": "agent_336#00",
    "rounding_convention": ("decimal.Decimal throughout; each period's depreciation quantized to "
        "whole dollars with ROUND_HALF_UP as computed (per period). No PVs in this item. Both "
        "schedules closed exactly: press AD ties to 45 months x $1,125 = $50,625 (BV $39,375 at "
        "9/30/20X4); mill AD ties to 33 months x $1,000 = $33,000 (BV $30,000 at 6/30/20X7). "
        "Monthly rates are exact, so no rounding plug was required (asserted in code). "
        "Exchange has commercial substance -> full loss recognized; mill cost = FV of press "
        "given up + cash paid, since the press's FV is the more clearly determinable measure."),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("Press: base 81,000 / 6 yr = 13,500/yr = 1,125/mo. 20X1-X3 full years (40,500) plus "
        "9 months of 20X4 (10,125) = AD 50,625; BV 39,375 vs FV 38,000 -> 1,375 LOSS. Commercial "
        "substance means the loss is recognized in full (a loss would be recognized even without "
        "commercial substance, so the boot rules never bite here). Mill capitalized at 38,000 + "
        "25,000 = 63,000; base 60,000 / 5 yr = 12,000/yr = 1,000/mo; 3 + 12 + 12 + 6 = 33 months "
        "to 6/30/20X7 -> AD 33,000, BV 30,000; sold for 28,000 -> 2,000 LOSS. Exchange JE proves "
        "115,000 = 115,000; disposal JE proves 63,000 = 63,000. Part (e) records only the two "
        "adjusting entries the requirement names (12/31/20X4 and 6/30/20X7); the 12/31/20X5 and "
        "12/31/20X6 entries of 12,000 each appear as schedule rows.")
}
print(json.dumps(out, indent=1))
