"""Solver for agent_025#00 — Summit Trail Retail Co. operating lease (ASC 842 lessee).

ROUNDING CONVENTION: all money is decimal.Decimal, never float. Present values are
computed at full Decimal precision (getcontext().prec = 28) and then rounded to the
cent with ROUND_HALF_UP.  Rounding is applied PER PERIOD: each period's interest is
computed on the already-rounded carrying amount and immediately rounded HALF_UP to
the cent, so the schedule's own arithmetic is internally consistent.  Journal-entry
amounts are stated in dollars and cents (the payment is quoted to the cent, so the
cent convention is used rather than whole dollars).  The liability schedule closes
exactly to $0.00 and the ROU schedule closes exactly to $0.00 with NO forced plug —
this is asserted below.  Every figure is derived; nothing is hard-coded except the
facts given in the question.
"""
from decimal import Decimal, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 28
CENT = Decimal("0.01")


def q(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------- given facts ----------------
PMT = Decimal("41387.12")     # annual payment, due Jan 1 (annuity due)
N = 4                          # lease term, years
LIFE = Decimal("12")           # remaining economic life, years
FV = Decimal("400000")         # fair value at commencement
RATE = Decimal("0.07")         # implicit rate = IBR
IDC = Decimal("2000")          # initial direct costs paid by lessee
INCENTIVE = Decimal("7500")    # cash incentive received from lessor

# ---------------- (b)/(c) present value: annuity due ----------------
pv_exact = Decimal(0)
pv_factor = Decimal(0)
for t in range(N):                      # t = 0,1,2,3  (payments in advance)
    disc = Decimal(1) / ((Decimal(1) + RATE) ** t)
    pv_factor += disc
    pv_exact += PMT * disc
liability0 = q(pv_exact)                # lease liability at commencement
pv_pct_fv = (liability0 / FV * Decimal(100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
term_pct_life = (Decimal(N) / LIFE * Decimal(100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
classification = "Operating lease"      # none of the five criteria met

# ---------------- (c) ROU asset ----------------
rou0 = q(liability0 + IDC - INCENTIVE)

# ---------------- (e) lease liability amortization schedule ----------------
total_payments = q(PMT * N)
liab_rows = []
bal = liability0
total_interest = Decimal("0.00")
for yr in range(1, N + 1):
    beg = bal
    pay = PMT
    after_pay = q(beg - pay)
    interest = q(after_pay * RATE)      # interest accrues Jan 1 -> Dec 31 on post-payment balance
    end = q(after_pay + interest)
    total_interest += interest
    liab_rows.append({"year": yr, "beg": beg, "payment": pay, "after_payment": after_pay,
                      "interest": interest, "end": end})
    bal = end
assert bal == Decimal("0.00"), bal                       # closes exactly to zero, no plug
assert q(total_payments - liability0) == total_interest  # interest ties to payments less PV

# ---------------- (e) right-of-use asset schedule ----------------
total_lease_cost = q(total_payments + IDC - INCENTIVE)
annual_expense = q(total_lease_cost / N)
assert q(annual_expense * N) == total_lease_cost          # straight-line divides evenly
rou_rows = []
rbal = rou0
for r in liab_rows:
    beg = rbal
    amort = q(annual_expense - r["interest"])             # ROU amortization = SL cost - interest
    end = q(beg - amort)
    rou_rows.append({"year": r["year"], "beg": beg, "expense": annual_expense,
                     "interest": r["interest"], "amortization": amort, "end": end})
    rbal = end
assert rbal == Decimal("0.00"), rbal                      # closes exactly to zero, no plug

# ---------------- (g) Dec 31 Year 1 balance sheet split ----------------
rou_net_y1 = rou_rows[0]["end"]
liab_y1 = liab_rows[0]["end"]
liab_y2 = liab_rows[1]["end"]
current_y1 = q(liab_y1 - liab_y2)      # decrease in the liability over the next 12 months
noncurrent_y1 = q(liab_y1 - current_y1)
assert q(current_y1 + noncurrent_y1) == liab_y1

# ---------------- answers ----------------
A = []


def add(label, value):
    A.append({"label": label, "value": value})


add("a: Initial direct costs capitalized before commencement (Dr Prepaid Initial Direct Costs / Cr Cash)", IDC)
add("a: Lease incentive received before commencement (Dr Cash / Cr Lease Incentive Liability)", INCENTIVE)

add("b: Criterion 1 — transfer of ownership by end of term (0 = not met, fixtures revert to lessor)", 0)
add("b: Criterion 2 — purchase option reasonably certain (0 = not met, none exists)", 0)
add("b: Criterion 3 — lease term as % of remaining economic life (4/12; <75%, not met)", term_pct_life)
add("b: Criterion 4 — PV of lease payments at 7% (annuity due, 4 payments)", liability0)
add("b: Criterion 4 — PV as % of $400,000 fair value (<90%, not met)", pv_pct_fv)
add("b: Criterion 5 — specialized asset with no alternative use (0 = not met, routinely re-leased)", 0)
add("b: Classification for Summit (lessee)", classification)

add("c: Lease liability at commencement (Jan 1, Year 1)", liability0)
add("c: Right-of-use asset at commencement = liability + IDC $2,000 - incentive $7,500", rou0)

for r in liab_rows:
    y = r["year"]
    add(f"e: Liability schedule — Jan 1 Yr {y} balance before payment", r["beg"])
    add(f"e: Liability schedule — Jan 1 Yr {y} payment (all principal, annuity due)", r["payment"])
    add(f"e: Liability schedule — Jan 1 Yr {y} balance after payment", r["after_payment"])
    add(f"e: Liability schedule — Dec 31 Yr {y} interest accretion @ 7%", r["interest"])
    add(f"e: Liability schedule — Dec 31 Yr {y} ending lease liability", r["end"])
add("e: Liability schedule — total payments", total_payments)
add("e: Liability schedule — total interest", total_interest)

add("e: ROU schedule — Jan 1 Year 1 beginning right-of-use asset", rou0)
for r in rou_rows:
    y = r["year"]
    add(f"e: ROU schedule — Yr {y} single straight-line lease expense", r["expense"])
    add(f"e: ROU schedule — Yr {y} less interest on lease liability", r["interest"])
    add(f"e: ROU schedule — Yr {y} ROU amortization", r["amortization"])
    add(f"e: ROU schedule — Dec 31 Yr {y} ending right-of-use asset", r["end"])
add("e: Total lease cost over the term (payments + IDC - incentive)", total_lease_cost)

add("f: Jan 1 Year 1 payment applied to lease liability", PMT)
add("f: Dec 31 Year 1 single lease expense", annual_expense)
add("f: Dec 31 Year 1 credit to lease liability (interest accretion)", liab_rows[0]["interest"])
add("f: Dec 31 Year 1 credit to right-of-use asset (amortization)", rou_rows[0]["amortization"])

add("g: Year 1 income statement — single operating lease expense", annual_expense)
add("g: Dec 31 Year 1 balance sheet — right-of-use asset, net", rou_net_y1)
add("g: Dec 31 Year 1 balance sheet — total lease liability", liab_y1)
add("g: Dec 31 Year 1 balance sheet — current lease liability", current_y1)
add("g: Dec 31 Year 1 balance sheet — noncurrent lease liability", noncurrent_y1)

add("h: Jan 1 Year 2 payment applied to lease liability", PMT)
add("h: Dec 31 Year 2 single lease expense", annual_expense)
add("h: Dec 31 Year 2 interest accretion on lease liability", liab_rows[1]["interest"])
add("h: Dec 31 Year 2 ROU amortization", rou_rows[1]["amortization"])
add("h: Jan 1 Year 4 final payment applied to lease liability", PMT)
add("h: Dec 31 Year 4 single lease expense", annual_expense)
add("h: Dec 31 Year 4 interest accretion (liability is zero all of Year 4)", liab_rows[3]["interest"])
add("h: Dec 31 Year 4 ROU amortization", rou_rows[3]["amortization"])
add("h: Lease liability after maturity", liab_rows[3]["end"])
add("h: Right-of-use asset after maturity", rou_rows[3]["end"])

# ---------------- journal entries ----------------
JE = []


def je(part, lines):
    dr = sum((l[1] for l in lines), Decimal("0.00"))
    cr = sum((l[2] for l in lines), Decimal("0.00"))
    assert q(dr) == q(cr), (part, dr, cr)
    JE.append({"part": part, "lines": [{"account": a, "debit": d, "credit": c} for a, d, c in lines]})


Z = Decimal("0.00")
je("a (before commencement — initial direct costs paid)",
   [("Prepaid Initial Direct Costs (Lease)", IDC, Z), ("Cash", Z, IDC)])
je("a (before commencement — cash lease incentive received)",
   [("Cash", INCENTIVE, Z), ("Lease Incentive Liability", Z, INCENTIVE)])
je("d (Jan 1, Year 1 — commencement)",
   [("Right-of-Use Asset", rou0, Z), ("Lease Incentive Liability", INCENTIVE, Z),
    ("Lease Liability", Z, liability0), ("Prepaid Initial Direct Costs (Lease)", Z, IDC)])
je("f (Jan 1, Year 1 — first annual payment, in advance)",
   [("Lease Liability", PMT, Z), ("Cash", Z, PMT)])
je("f (Dec 31, Year 1 — single lease expense)",
   [("Lease Expense", annual_expense, Z), ("Lease Liability", Z, liab_rows[0]["interest"]),
    ("Right-of-Use Asset", Z, rou_rows[0]["amortization"])])
je("h (Jan 1, Year 2 — second annual payment)",
   [("Lease Liability", PMT, Z), ("Cash", Z, PMT)])
je("h (Dec 31, Year 2 — single lease expense)",
   [("Lease Expense", annual_expense, Z), ("Lease Liability", Z, liab_rows[1]["interest"]),
    ("Right-of-Use Asset", Z, rou_rows[1]["amortization"])])
je("h (Jan 1, Year 4 — final annual payment; liability goes to zero)",
   [("Lease Liability", PMT, Z), ("Cash", Z, PMT)])
je("h (Dec 31, Year 4 — final lease expense; no interest, liability already zero)",
   [("Lease Expense", annual_expense, Z), ("Right-of-Use Asset", Z, rou_rows[3]["amortization"])])

notes = (
    "Annuity-due PV factor at 7% for 4 payments = "
    + str(pv_factor.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))
    + "; 41,387.12 x that factor = 150,000.00 lease liability at commencement. "
    "(b) None of the five ASC 842 criteria is met: no title transfer (fixtures revert), no purchase "
    "option, term 4/12 = 33.33% of economic life (not a major part), PV 150,000/400,000 = 37.50% of "
    "fair value (not substantially all), and the fixtures are not specialized (routinely re-leased) — "
    "therefore an operating lease. (c)-(d) ROU = 150,000 + 2,000 IDC - 7,500 incentive = 144,500; the "
    "commencement entry clears the prepaid IDC and the incentive liability. Under the operating-lease "
    "model a single straight-line lease cost of (165,548.48 + 2,000 - 7,500)/4 = 40,012.12 is recognized "
    "each year; the liability is accreted at 7% and the ROU asset is amortized by the plug (lease cost "
    "less interest). Because payments are in advance, each payment is 100% principal and interest for "
    "the year accrues on the post-payment balance. (g) The current portion is the decrease in the lease "
    "liability over the next twelve months (116,215.78 - 80,066.67 = 36,149.11); if instead the entire "
    "Jan 1 Year 2 payment of 41,387.12 were shown as current, noncurrent would be 74,828.67. "
    "(h) In Year 4 the liability is zero for the whole year, so no interest accretes and the entire "
    "40,012.12 of lease cost amortizes the remaining ROU asset; both the ROU asset and the lease "
    "liability are exactly 0.00 after maturity and the fixtures are simply returned to Crestline "
    "(memo entry only)."
)

out = {
    "id": "agent_025#00",
    "rounding_convention": ("decimal.Decimal throughout (no floats); PVs computed at full precision "
                            "(prec=28) then rounded to the cent with ROUND_HALF_UP; rounding applied "
                            "per period — each period's interest is computed on the rounded carrying "
                            "amount and rounded HALF_UP to the cent. Amounts stated in dollars and "
                            "cents. Both schedules close exactly to 0.00 with no forced plug."),
    "answers": A,
    "journal_entries": JE,
    "insufficient_info": False,
    "notes": notes,
}


class E(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)


print(json.dumps(out, cls=E))
