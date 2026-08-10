"""Glacier Lab Analytics LLC - finance lease with purchase-option reassessment (LO 17-11).

Rounding convention: all math uses decimal.Decimal at 28-digit precision.
Present values / schedule carrying amounts are carried at FULL PRECISION;
every reported figure and every journal-entry amount is rounded to whole
dollars with ROUND_HALF_UP applied once, per period/per figure (no chained
rounding). The post-remeasurement schedule closes EXACTLY to the $30,000
purchase-option face at Dec 31 Year 5 and to zero after the option payment.
Nothing is hard-coded except the fact-pattern inputs; Dr = Cr on every entry.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 28

def q(x):
    return x.quantize(D("1"), rounding=ROUND_HALF_UP)

def i(x):
    return int(q(x))

# ---------------- fact pattern ----------------
PMT      = D("80000")          # annual payment, in advance (Jan 1)
TERM     = 5                   # lease term, years
ECON     = 6                   # economic life, years
PO       = D("30000")          # purchase option at end of Year 5
R0       = D("0.07")           # IBR at commencement
R1       = D("0.05")           # revised IBR at Jan 1 Year 3
YRS_ELAPSED = 2                # Year 1 and Year 2 complete at Jan 1 Year 3

def pv(amount, rate, n):
    return amount / (D(1) + rate) ** n

# ---------------- (a) commencement ----------------
# Annuity due: payments at t = 0..4, PO excluded (not reasonably certain)
pv0 = sum((pv(PMT, R0, n) for n in range(TERM)), D(0))

# ---------------- (b) roll forward to Jan 1 Year 3 ----------------
bal = pv0
roll = []
for yr in range(1, YRS_ELAPSED + 1):
    after_pmt = bal - PMT
    interest = after_pmt * R0
    end = after_pmt + interest
    roll.append((yr, bal, after_pmt, interest, end))
    bal = end
liab_before = bal                      # Jan 1 Y3, before remeasurement & before payment

# cross-check: PV of the 3 remaining payments as an annuity due at 7%
chk = sum((pv(PMT, R0, n) for n in range(TERM - YRS_ELAPSED)), D(0))
assert abs(chk - liab_before) < D("0.0000001"), (chk, liab_before)

amort_orig = pv0 / D(TERM)             # SL over the 5-year lease term
accum_orig = amort_orig * D(YRS_ELAPSED)
rou_before = pv0 - accum_orig

# ---------------- (c) remeasurement at Jan 1 Year 3 ----------------
# Revised payments: 3 remaining rents (t=0,1,2) + PO at end of Year 5 (t=3), at 5%
remaining = TERM - YRS_ELAPSED
liab_remeas = sum((pv(PMT, R1, n) for n in range(remaining)), D(0)) + pv(PO, R1, remaining)
adj = liab_remeas - liab_before
rou_after = rou_before + adj

# ---------------- (d) payment + full schedule through the PO ----------------
sched = []
b = liab_remeas
# Jan 1 Y3 payment
after = b - PMT
sched.append(("Jan 1, Year 3", "payment", PMT, D(0), after))
b = after
for yr in (3, 4, 5):
    interest = b * R1
    b = b + interest
    sched.append((f"Dec 31, Year {yr}", "interest accrual", D(0), interest, b))
    if yr < 5:
        b = b - PMT
        sched.append((f"Jan 1, Year {yr+1}", "payment", PMT, D(0), b))
# exercise the purchase option
b = b - PO
sched.append(("Dec 31, Year 5", "purchase option exercised", PO, D(0), b))
assert abs(b) < D("0.000001"), b
b = D(0)
sched[-1] = (sched[-1][0], sched[-1][1], sched[-1][2], sched[-1][3], b)
int_y3 = sched[1][3]

# ---------------- (e) amortization after remeasurement ----------------
rem_life = ECON - YRS_ELAPSED          # PO now reasonably certain -> remaining economic life
amort_new = rou_after / D(rem_life)

answers = [
 {"label": "a: Initial lease liability / ROU asset - PV of 5 annual payments of $80,000 in advance at 7% (PO excluded, not reasonably certain)", "value": i(pv0)},
 {"label": "a: Jan 1, Year 1 first lease payment (cash)", "value": i(PMT)},

 {"label": "b: Annual ROU amortization Years 1-2 (SL, $350,977 over 5-year lease term)", "value": i(amort_orig)},
 {"label": "b: Accumulated ROU amortization at Jan 1, Year 3 (2 years)", "value": i(accum_orig)},
 {"label": "b: ROU asset carrying amount, Jan 1, Year 3 (before remeasurement)", "value": i(rou_before)},
 {"label": "b: Lease liability, Jan 1, Year 3 before remeasurement and before payment", "value": i(liab_before)},

 {"label": "c: Remeasured lease liability, Jan 1, Year 3 - 3 payments of $80,000 in advance plus $30,000 PO, discounted at 5%", "value": i(liab_remeas)},
 {"label": "c: Remeasurement adjustment (increase to liability and ROU asset)", "value": i(adj)},
 {"label": "c: Lease liability immediately after remeasurement (before Jan 1, Year 3 payment)", "value": i(liab_remeas)},
 {"label": "c: ROU asset carrying amount immediately after remeasurement", "value": i(rou_after)},

 {"label": "d: Jan 1, Year 3 lease payment", "value": i(PMT)},
 {"label": "d: Schedule - liability balance after Jan 1, Year 3 payment", "value": i(sched[0][4])},
 {"label": "d: Schedule - Year 3 interest at 5% (Dec 31, Year 3)", "value": i(sched[1][3])},
 {"label": "d: Schedule - liability balance Dec 31, Year 3", "value": i(sched[1][4])},
 {"label": "d: Schedule - Jan 1, Year 4 payment", "value": i(sched[2][2])},
 {"label": "d: Schedule - liability balance after Jan 1, Year 4 payment", "value": i(sched[2][4])},
 {"label": "d: Schedule - Year 4 interest at 5% (Dec 31, Year 4)", "value": i(sched[3][3])},
 {"label": "d: Schedule - liability balance Dec 31, Year 4", "value": i(sched[3][4])},
 {"label": "d: Schedule - Jan 1, Year 5 payment", "value": i(sched[4][2])},
 {"label": "d: Schedule - liability balance after Jan 1, Year 5 payment", "value": i(sched[4][4])},
 {"label": "d: Schedule - Year 5 interest at 5% (Dec 31, Year 5)", "value": i(sched[5][3])},
 {"label": "d: Schedule - liability balance Dec 31, Year 5 before exercising PO (equals $30,000 option price)", "value": i(sched[5][4])},
 {"label": "d: Schedule - purchase option paid at end of Year 5", "value": i(sched[6][2])},
 {"label": "d: Schedule - liability balance after exercising the purchase option", "value": i(sched[6][4])},
 {"label": "d: Dec 31, Year 3 interest expense (JE amount)", "value": i(int_y3)},

 {"label": "e: Remaining economic life used after remeasurement (years)", "value": rem_life},
 {"label": "e: Annual ROU amortization after remeasurement ($240,613 over 4 remaining years of economic life)", "value": i(amort_new)},
]

jes = [
 {"part": "a", "lines": [
   {"account": "Right-of-Use Asset (Jan 1, Year 1 commencement)", "debit": i(pv0), "credit": 0},
   {"account": "Lease Liability", "debit": 0, "credit": i(pv0)}]},
 {"part": "a", "lines": [
   {"account": "Lease Liability (Jan 1, Year 1 first payment)", "debit": i(PMT), "credit": 0},
   {"account": "Cash", "debit": 0, "credit": i(PMT)}]},
 {"part": "c", "lines": [
   {"account": "Right-of-Use Asset (Jan 1, Year 3 remeasurement for purchase option)", "debit": i(adj), "credit": 0},
   {"account": "Lease Liability", "debit": 0, "credit": i(adj)}]},
 {"part": "d", "lines": [
   {"account": "Lease Liability (Jan 1, Year 3 payment)", "debit": i(PMT), "credit": 0},
   {"account": "Cash", "debit": 0, "credit": i(PMT)}]},
 {"part": "d", "lines": [
   {"account": "Interest Expense (Dec 31, Year 3, 5% on $174,668)", "debit": i(int_y3), "credit": 0},
   {"account": "Lease Liability", "debit": 0, "credit": i(int_y3)}]},
]
for je in jes:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"]), je

out = {
 "id": "agent_151#01",
 "rounding_convention": "decimal.Decimal throughout; PVs and schedule balances carried at full precision, every reported figure and journal-entry amount rounded once to whole dollars with ROUND_HALF_UP; schedule closes exactly to the $30,000 purchase-option face at Dec 31, Year 5 and to $0 after exercise.",
 "answers": answers,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": ("PO excluded at commencement (not reasonably certain), so initial PV = annuity due of 5 x $80,000 at 7% = $350,976.90 and ROU amortizes SL over the 5-year lease term. "
           "Liability rolled to Jan 1, Year 3 pre-payment = $224,641.45 (= PV of the 3 remaining payments as an annuity due at 7%). "
           "Reassessment on Jan 1, Year 3 is measured BEFORE that day's payment, so the revised payment stream is three $80,000 rents at t=0,1,2 plus the $30,000 option at t=3, discounted at the updated 5% rate = $254,667.96; "
           "the $30,026.51 increase is added to the ROU asset (no P&L). Post-remeasurement ROU = $210,586.14 + $30,026.51 = $240,612.65, amortized over the remaining 4 years of the 6-year economic life because exercise is now reasonably certain. "
           "Unrounded schedule: 174,667.96 / int 8,733.40 -> 183,401.36 / pay 80,000 -> 103,401.36 / int 5,170.07 -> 108,571.43 / pay 80,000 -> 28,571.43 / int 1,428.57 -> 30,000.00 / PO 30,000 -> 0.")
}
print(json.dumps(out, indent=1))
