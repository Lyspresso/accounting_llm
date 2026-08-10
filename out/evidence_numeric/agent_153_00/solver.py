"""Solver for agent_153#00 -- Ironvale finance lease (annuity due, 4 yrs, 6%).

ROUNDING CONVENTION: all money is decimal.Decimal; every period's interest,
amortization and balance is quantized to the cent with ROUND_HALF_UP
(per-period rounding, not end-of-schedule rounding).  Present values are run at
full precision (28 sig digits) and only the reported figures are quantized.
The final period's interest is PLUGGED so the liability schedule closes EXACTLY
to zero at the last payment (the un-rounded 6% accrual differs by $0.01).
Nothing is hard-coded: the PV, every schedule row and every JE is derived from
the stated facts (payment, n=4, annuity due, rate, fair value, life).
"""
import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 40
C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---------------- facts ----------------
PMT   = Decimal("40838.42")
N     = 4
FV    = Decimal("150000")
IMPL  = Decimal("0.06")
IBR   = Decimal("0.065")
LIFE  = Decimal("4")
TERM  = Decimal("4")

def factor_annuity_due(r, n):
    f = Decimal(1)
    for k in range(1, n):
        f += (Decimal(1) + r) ** (-k)
    return f

# ---------------- (b) measurement ----------------
fac6   = factor_annuity_due(IMPL, N)
pv6    = q(PMT * fac6)
liab0  = pv6
rou0   = liab0                       # basic case: no IDC / prepaid / incentives

# ---------------- (a) classification ----------------
pct_life = (TERM / LIFE) * Decimal(100)
pct_fv   = (pv6 / FV) * Decimal(100)

# ---------------- (c) schedule ----------------
rows = []            # (event, payment, interest, reduction, balance)
bal = liab0
rows.append(("1/1/Yr1 commencement", None, None, None, bal))
# payment at commencement: all principal (no time elapsed)
bal = bal - PMT
rows.append(("1/1/Yr1 payment", PMT, Decimal("0.00"), PMT, bal))
for yr in range(1, N):               # accrual 12/31 of Yr1..Yr3, payment 1/1 of Yr2..Yr4
    if yr < N - 1:
        interest = q(bal * IMPL)
    else:
        bal3 = bal
        interest = q(PMT - bal)      # PLUG so final payment zeroes the liability
    bal = bal + interest
    rows.append((f"12/31/Yr{yr} interest accrual", None, interest, None, bal))
    bal = bal - PMT
    rows.append((f"1/1/Yr{yr+1} payment", PMT, Decimal("0.00"), PMT, bal))
assert bal == Decimal("0.00"), bal

tot_pmt  = PMT * N
tot_int  = sum(r[2] for r in rows if r[2] is not None)
tot_prin = sum(r[3] for r in rows if r[3] is not None)
assert tot_prin == tot_pmt and tot_pmt == liab0 + tot_int

int_y = {}                            # interest recognized in each fiscal year
for ev, p, i, red, b in rows:
    if ev.startswith("12/31"):
        int_y[int(ev.split("Yr")[1][0])] = i
int_y[4] = Decimal("0.00")            # liability is zero all of Yr4

amort = q(rou0 / Decimal(N))          # straight line over 4-yr lease term

# ---------------- (e) Year 1 statements ----------------
liab_1231_y1 = [r[4] for r in rows if r[0].startswith("12/31/Yr1")][0]
cur_y1  = PMT                          # 1/1/Yr2 payment is 100% principal
noncur_y1 = liab_1231_y1 - cur_y1
rou_net_y1 = rou0 - amort
tot_exp_y1 = int_y[1] + amort

# ---------------- (g) if only the 6.5% IBR were known ----------------
fac65 = factor_annuity_due(IBR, N)
pv65  = q(PMT * fac65)
diff  = liab0 - pv65
int65_total = q(PMT * N - pv65)
pct_fv65 = (pv65 / FV) * Decimal(100)

def f(x): return float(Decimal(x).quantize(C, rounding=ROUND_HALF_UP))

A = []
def add(lbl, val): A.append({"label": lbl, "value": val})

# (a)
add("a: lessee classification", "Finance lease")
add("a: criterion met #1 - lease term as % of remaining economic life (4 yr / 4 yr) = major part (>=75%)", f(pct_life))
add("a: criterion met #2 - PV of lease payments as % of fair value ($150,000.00 / $150,000.00) = substantially all (>=90%)", f(pct_fv))
add("a: criteria NOT met - no transfer of ownership, no purchase option, asset is nonspecialized (alternative use exists)", "not met")

# (b)
add("b: discount rate used - lessor's implicit rate (known to lessee)", "6% (6.5% IBR not used)")
add("b: PV factor, annuity due, n=4, i=6%", float(fac6.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)))
add("b: lease liability at commencement 1/1/Yr1", f(liab0))
add("b: ROU asset at commencement 1/1/Yr1", f(rou0))

# (c) full schedule roll-forward
for ev, p, i, red, b in rows:
    if p is not None:
        add(f"c: {ev} - cash payment", f(p))
        add(f"c: {ev} - interest on liability", f(i))
        add(f"c: {ev} - reduction of lease liability", f(red))
    elif i is not None:
        add(f"c: {ev} - interest expense (6% x prior balance)", f(i))
    add(f"c: {ev} - lease liability balance", f(b))
add("c: schedule total - cash payments", f(tot_pmt))
add("c: schedule total - interest expense", f(tot_int))
add("c: schedule total - reduction of lease liability from payments (= total payments; interest is accrued into the liability each 12/31)", f(tot_prin))

# (e)
add("e: balance sheet 12/31/Yr1 - ROU asset, net ($150,000.00 cost less $37,500.00 amortization)", f(rou_net_y1))
add("e: balance sheet 12/31/Yr1 - total lease liability", f(liab_1231_y1))
add("e: balance sheet 12/31/Yr1 - current lease liability", f(cur_y1))
add("e: balance sheet 12/31/Yr1 - noncurrent lease liability", f(noncur_y1))
add("e: income statement Yr1 - interest expense", f(int_y[1]))
add("e: income statement Yr1 - amortization expense on ROU asset", f(amort))
add("e: income statement Yr1 - total lease-related expense", f(tot_exp_y1))

# (f) supporting figures
add("f: Yr2 interest expense", f(int_y[2]))
add("f: Yr3 interest expense (plugged $0.01 to close schedule to zero)", f(int_y[3]))
add("f: Yr4 interest expense (liability is $0 after the 1/1/Yr4 payment)", f(int_y[4]))
add("f: annual ROU amortization, Yr2 / Yr3 / Yr4", f(amort))
add("f: ROU asset carrying amount after the 12/31/Yr4 entry (asset returned, zero residual)", 0.0)
add("f: lease liability balance after the 1/1/Yr4 payment", 0.0)

# (g)
add("g: PV factor, annuity due, n=4, i=6.5%", float(fac65.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)))
add("g: lease liability = ROU asset at commencement if 6.5% IBR were used", f(pv65))
add("g: decrease vs. the 6% measurement", f(diff))
add("g: PV as % of fair value at 6.5% (still 'substantially all', still a finance lease)", float(pct_fv65.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)))
add("g: total interest expense over the term at 6.5%", f(int65_total))
add("g: annual straight-line ROU amortization at 6.5%", f(q(pv65 / Decimal(N))))

# ---------------- journal entries ----------------
def je(part, lines):
    ls = [{"account": a, "debit": f(d), "credit": f(c)} for a, d, c in lines]
    assert sum(Decimal(str(l["debit"])) for l in ls) == sum(Decimal(str(l["credit"])) for l in ls), part
    return {"part": part, "lines": ls}

Z = Decimal("0")
JE = []
JE.append(je("b/d (1/1/Yr1 - commencement, recognize ROU asset and lease liability)",
             [("Right-of-Use Asset", rou0, Z), ("Lease Liability", Z, liab0)]))
JE.append(je("d (1/1/Yr1 - first annuity-due lease payment, all principal)",
             [("Lease Liability", PMT, Z), ("Cash", Z, PMT)]))
JE.append(je("d (12/31/Yr1 - accrue interest on lease liability)",
             [("Interest Expense", int_y[1], Z), ("Lease Liability", Z, int_y[1])]))
JE.append(je("d (12/31/Yr1 - amortize ROU asset straight-line, credited directly)",
             [("Amortization Expense", amort, Z), ("Right-of-Use Asset", Z, amort)]))
for yr in (2, 3, 4):
    JE.append(je(f"f (1/1/Yr{yr} - lease payment)",
                 [("Lease Liability", PMT, Z), ("Cash", Z, PMT)]))
    if int_y[yr] > 0:
        JE.append(je(f"f (12/31/Yr{yr} - accrue interest on lease liability)",
                     [("Interest Expense", int_y[yr], Z), ("Lease Liability", Z, int_y[yr])]))
    JE.append(je(f"f (12/31/Yr{yr} - amortize ROU asset straight-line, credited directly)",
                 [("Amortization Expense", amort, Z), ("Right-of-Use Asset", Z, amort)]))

notes = (
    "Finance lease: lease term (4 yrs) = 100% of the 4-yr economic life (major part) AND PV of the lease "
    f"payments (${liab0:,.2f}) = {pct_fv:.0f}% of the ${FV:,.0f} fair value (substantially all). Discount rate = the "
    "6% implicit rate because it is known to the lessee. Annuity due: the 1/1/Yr1 payment is 100% principal "
    "(no interest has accrued), and no interest accrues between each 12/31 accrual and the following 1/1 "
    "payment, so every payment is 100% principal against the then-accrued balance. Interest is computed at "
    "6% on the post-payment balance and rounded to the cent (ROUND_HALF_UP) each period; the 12/31/Yr3 "
    f"accrual is plugged to ${int_y[3]:,.2f} (un-rounded ${bal3*IMPL:,.3f}) so the liability closes EXACTLY to "
    "$0.00 at the 1/1/Yr4 payment. No interest arises in Yr4 (the liability is zero after 1/1/Yr4). Current "
    f"portion at 12/31/Yr1 = the full ${cur_y1:,.2f} due 1/1/Yr2, none of which is interest. (g) With only the "
    f"6.5% IBR, the liability and ROU asset would be measured at ${pv65:,.2f} (a ${diff:,.2f} decrease); "
    f"classification is unchanged ({pct_fv65:.2f}% of fair value is still substantially all, and the lease term "
    f"still equals the economic life); total interest over the term rises to ${int65_total:,.2f} and annual ROU "
    f"amortization falls to ${q(pv65/Decimal(N)):,.2f}. A higher discount rate always gives a smaller "
    "liability/ROU asset, more total interest expense, and less amortization expense."
)

print(json.dumps({
    "id": "agent_153#00",
    "rounding_convention": ("decimal.Decimal throughout; ROUND_HALF_UP to the cent per period (interest, "
                            "amortization, balances); PV factors carried at full precision; final-period "
                            "interest plugged so the schedule closes exactly to $0.00"),
    "answers": A,
    "journal_entries": JE,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
