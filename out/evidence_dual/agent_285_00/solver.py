"""agent_285#00 - Operating lease full life cycle (LO 17-3), independent derivation.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal (never float). The commencement PV of the annuity-due
lease payments is computed at full Decimal precision (prec=40) and then rounded ONCE
to the nearest dollar with ROUND_HALF_UP. From that whole-dollar opening balance the
lease-liability schedule runs entirely in whole dollars: each period's interest accrual
is 5% of the post-payment carrying amount, rounded to the nearest dollar ROUND_HALF_UP
per period (no carried fractional cents). The FINAL interest accrual is PLUGGED so the
liability closes exactly to face/zero (here the plug happens to equal the rounded value,
so no forced adjustment was needed - reported below). ROU amortization each period is
derived as (single straight-line lease expense - interest on the liability); the final
period's ROU reduction is plugged so the ROU asset closes exactly to zero.
Journal entries are whole dollars and every entry is proved Dr = Cr.
Nothing is hard-coded: every figure below is derived from the stem facts
(pmt=22000, n=4, annuity due, implicit rate 5% known, FV=140000, life=10 yrs).
"""
import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 40
D = Decimal
CENT0 = D("1")


def r0(x: Decimal) -> Decimal:
    return x.quantize(CENT0, rounding=ROUND_HALF_UP)


def f(x: Decimal):
    x = r0(x) if x == r0(x) else x
    i = int(x)
    return i if D(i) == x else float(x)


# ---------------- stem facts ----------------
PMT = D("22000")          # annual payment
N = 4                     # lease term in years
RATE_IMPLICIT = D("0.05") # lessor implicit rate, KNOWN to lessee
RATE_IBR = D("0.06")      # not used (implicit known)
FV = D("140000")          # fair value of equipment at commencement
ECON_LIFE = D("10")       # remaining economic life, years
DUE = True                # payments at beginning of period (annuity due)

rate = RATE_IMPLICIT      # a: discount rate used

# ---------------- b: PV of annuity due ----------------
pv_factor = sum((D(1) + rate) ** (-k) for k in range(0, N))   # 1 + PVA-ord(n-1)
pv_exact = PMT * pv_factor
liab0 = r0(pv_exact)      # lease liability at commencement, before 1st payment
rou0 = liab0              # basic case: no IDC / prepaid / incentives

# ---------------- a: classification tests ----------------
term_pct = (D(N) / ECON_LIFE * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
pv_pct = (liab0 / FV * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
total_payments = PMT * N

# ---------------- c: liability schedule (whole dollars) ----------------
liab_rows = []
bal = liab0
plug_used = False
plug_delta = D(0)
for yr in range(1, N + 1):
    open_bal = bal
    after_pmt = open_bal - PMT                     # Jan 1 payment: all principal
    unplugged_int = r0(after_pmt * rate)
    if yr == N:
        # last year: liability must clear to zero after the final payment
        interest = D(0) - after_pmt
    elif yr == N - 1:
        # last accrual that must leave exactly one payment outstanding
        interest = PMT - after_pmt
    else:
        interest = unplugged_int
    if yr >= N - 1 and interest != unplugged_int:
        plug_used = True
        plug_delta += interest - unplugged_int
    close_bal = after_pmt + interest
    liab_rows.append(
        dict(year=yr, opening=open_bal, payment=PMT, principal=PMT,
             after_payment=after_pmt, interest=interest, closing=close_bal)
    )
    bal = close_bal
assert bal == 0, bal
total_interest = sum(r["interest"] for r in liab_rows)
assert total_payments - liab0 == total_interest, (total_payments - liab0, total_interest)

# ---------------- straight-line single lease cost ----------------
total_lease_cost = total_payments                 # no incentives / IDC / prepaid
annual_expense = total_lease_cost / D(N)
assert annual_expense == r0(annual_expense)

# ---------------- c: ROU asset schedule ----------------
rou_rows = []
rbal = rou0
for r in liab_rows:
    amort = annual_expense - r["interest"]
    if r["year"] == N:
        amort = rbal                              # plug final reduction -> zero
    rou_rows.append(dict(year=r["year"], opening=rbal, expense=annual_expense,
                         interest=r["interest"], amortization=amort,
                         closing=rbal - amort))
    rbal = rbal - amort
assert rbal == 0, rbal
assert sum(x["amortization"] for x in rou_rows) == rou0

# ROU closing == liability closing every period (no IDC/prepaid)
for a, b in zip(rou_rows, liab_rows):
    assert a["closing"] == b["closing"]

# ---------------- e: Dec 31 Y1 balance sheet split ----------------
y1 = liab_rows[0]
liab_y1 = y1["closing"]
current_y1 = liab_rows[1]["principal"]            # principal paid within next 12 mo
noncurrent_y1 = liab_y1 - current_y1
rou_y1 = rou_rows[0]["closing"]

# ---------------- journal entries ----------------
JE = []


def je(part, desc, lines):
    dr = sum(D(str(l[1])) for l in lines if l[1])
    cr = sum(D(str(l[2])) for l in lines if l[2])
    assert dr == cr, (part, desc, dr, cr)
    JE.append(dict(part=part, description=desc,
                   lines=[dict(account=a, debit=f(D(str(d_))), credit=f(D(str(c_))))
                          for a, d_, c_ in lines]))


je("d", "Jan 1, Year 1 - commencement: recognize ROU asset and lease liability",
   [("Right-of-Use Asset - Operating Lease", rou0, 0),
    ("Lease Liability - Operating Lease", 0, liab0)])
je("d", "Jan 1, Year 1 - first annual lease payment (annuity due; all principal)",
   [("Lease Liability - Operating Lease", PMT, 0), ("Cash", 0, PMT)])
je("d", "Dec 31, Year 1 - period-end adjusting entry (single lease expense)",
   [("Lease Expense", annual_expense, 0),
    ("Lease Liability - Operating Lease", 0, liab_rows[0]["interest"]),
    ("Right-of-Use Asset - Operating Lease", 0, rou_rows[0]["amortization"])])
for yr, part in ((2, "f"), (3, "f"), (4, "g")):
    lr = liab_rows[yr - 1]
    rr = rou_rows[yr - 1]
    je(part, f"Jan 1, Year {yr} - annual lease payment", 
       [("Lease Liability - Operating Lease", PMT, 0), ("Cash", 0, PMT)])
    lines = [("Lease Expense", annual_expense, 0)]
    if lr["interest"] != 0:
        lines.append(("Lease Liability - Operating Lease", 0, lr["interest"]))
    lines.append(("Right-of-Use Asset - Operating Lease", 0, rr["amortization"]))
    je(part, f"Dec 31, Year {yr} - period-end adjusting entry (single lease expense)",
       lines)

# ---------------- answers ----------------
A = []


def add(label, value):
    A.append(dict(label=label, value=value))


add("a: Criterion 1 - transfer of ownership by end of term? Equipment reverts to Summit",
    "No - no transfer of ownership")
add("a: Criterion 2 - purchase option reasonably certain to be exercised?",
    "No - no purchase option exists")
add(f"a: Criterion 3 - lease term ({N} yrs) a major part (>=75%) of remaining economic life "
    f"({f(ECON_LIFE)} yrs)? term percentage",
    f"{f(term_pct)}% - No (40% < 75%)")
add(f"a: Criterion 4 - PV of lease payments ${f(liab0)} vs fair value ${f(FV)}; "
    f"substantially all (>=90%)?", f"{f(pv_pct)}% - No (58.51% < 90%)")
add("a: Criterion 5 - specialized asset with no alternative use to lessor?",
    "No - Summit routinely leases this equipment to other customers")
add("a: Classification conclusion for Riverglen", "OPERATING lease (no criterion met)")
add("a: Discount rate used", "5% - lessor's implicit rate, known to the lessee "
    "(the 6% incremental borrowing rate is NOT used)")
add("b: PV annuity-due factor, 4 payments @ 5% (1 + PVA-ordinary 3 yrs)",
    float(pv_factor.quantize(D("0.000001"), rounding=ROUND_HALF_UP)))
add("b: PV of lease payments at full precision (before rounding)",
    float(pv_exact.quantize(D("0.01"), rounding=ROUND_HALF_UP)))
add("b: Lease liability at commencement, Jan 1 Year 1 (before first payment)", f(liab0))
add("b: Right-of-use asset at commencement, Jan 1 Year 1 (before first payment)", f(rou0))
add("c: Total of the four lease payments", f(total_payments))
add("c: Total interest over the lease term (88,000 - 81,911)", f(total_interest))
add("c: Straight-line single annual lease expense (total lease cost / 4 yrs)",
    f(annual_expense))
add("c: Liability schedule - Jan 1 Yr 1 opening balance", f(liab_rows[0]["opening"]))
for r in liab_rows:
    y = r["year"]
    add(f"c: Liability schedule Yr {y} - Jan 1 payment", f(r["payment"]))
    add(f"c: Liability schedule Yr {y} - Jan 1 reduction of liability (principal)",
        f(r["principal"]))
    add(f"c: Liability schedule Yr {y} - balance immediately after Jan 1 payment",
        f(r["after_payment"]))
    add(f"c: Liability schedule Yr {y} - Dec 31 interest accrual @ 5% on post-payment balance",
        f(r["interest"]))
    add(f"c: Liability schedule Yr {y} - Dec 31 closing lease liability", f(r["closing"]))
add("c: Liability schedule - balance after final (Jan 1 Yr 4) payment", f(D(0)))
for r in rou_rows:
    y = r["year"]
    add(f"c: ROU schedule Yr {y} - opening ROU asset", f(r["opening"]))
    add(f"c: ROU schedule Yr {y} - single lease expense", f(r["expense"]))
    add(f"c: ROU schedule Yr {y} - less interest on lease liability", f(r["interest"]))
    add(f"c: ROU schedule Yr {y} - ROU amortization (expense - interest)",
        f(r["amortization"]))
    add(f"c: ROU schedule Yr {y} - Dec 31 closing ROU asset", f(r["closing"]))
add("d: Jan 1 Yr 1 commencement - Dr Right-of-Use Asset / Cr Lease Liability", f(liab0))
add("d: Jan 1 Yr 1 first payment - Dr Lease Liability / Cr Cash", f(PMT))
add("d: Dec 31 Yr 1 adjusting - Dr Lease Expense", f(annual_expense))
add("d: Dec 31 Yr 1 adjusting - Cr Lease Liability (interest accretion)",
    f(liab_rows[0]["interest"]))
add("d: Dec 31 Yr 1 adjusting - Cr Right-of-Use Asset (period reduction)",
    f(rou_rows[0]["amortization"]))
add("e: Year 1 income statement - single Lease Expense in operating expenses "
    "(no separate interest or amortization line)", f(annual_expense))
add("e: Dec 31 Yr 1 balance sheet - Right-of-use asset, operating lease (noncurrent)",
    f(rou_y1))
add("e: Dec 31 Yr 1 balance sheet - Lease liability, current portion "
    "(principal due Jan 1 Yr 2)", f(current_y1))
add("e: Dec 31 Yr 1 balance sheet - Lease liability, noncurrent portion",
    f(noncurrent_y1))
add("e: Dec 31 Yr 1 balance sheet - Total lease liability", f(liab_y1))
for yr in (2, 3):
    lr = liab_rows[yr - 1]
    rr = rou_rows[yr - 1]
    add(f"f: Jan 1 Yr {yr} payment - Dr Lease Liability / Cr Cash", f(PMT))
    add(f"f: Dec 31 Yr {yr} adjusting - Dr Lease Expense", f(lr and annual_expense))
    add(f"f: Dec 31 Yr {yr} adjusting - Cr Lease Liability (interest)", f(lr["interest"]))
    add(f"f: Dec 31 Yr {yr} adjusting - Cr Right-of-Use Asset", f(rr["amortization"]))
    add(f"f: Dec 31 Yr {yr} closing lease liability", f(lr["closing"]))
    add(f"f: Dec 31 Yr {yr} closing right-of-use asset", f(rr["closing"]))
add("g: Jan 1 Yr 4 final payment - Dr Lease Liability / Cr Cash", f(PMT))
add("g: Lease liability balance immediately after the Jan 1 Yr 4 payment",
    f(liab_rows[3]["after_payment"]))
add("g: Year 4 interest on lease liability (liability is zero all year)",
    f(liab_rows[3]["interest"]))
add("g: Dec 31 Yr 4 adjusting - Dr Lease Expense", f(annual_expense))
add("g: Dec 31 Yr 4 adjusting - Cr Right-of-Use Asset (final reduction)",
    f(rou_rows[3]["amortization"]))
add("g: Right-of-use asset balance after lease end", f(rou_rows[3]["closing"]))
add("g: Lease liability balance after lease end", f(liab_rows[3]["closing"]))
add("g: Cumulative lease expense recognized over 4 years (= total cash paid)",
    f(annual_expense * N))

out = dict(
    id="agent_285#00",
    rounding_convention=(
        "decimal.Decimal throughout (prec=40); commencement PV computed at full "
        "precision then rounded once to the nearest dollar ROUND_HALF_UP ($81,911); "
        "schedule thereafter runs in whole dollars with each period's 5% interest "
        "accrual rounded ROUND_HALF_UP per period; final interest accrual PLUGGED so "
        "the liability closes exactly to zero and the final ROU reduction plugged so "
        "the ROU asset closes exactly to zero. Plug adjustment actually required: "
        f"${f(plug_delta)} (rounded values already closed the schedule). "
        "All journal entries whole dollars, Dr = Cr asserted."
    ),
    answers=A,
    journal_entries=JE,
    insufficient_info=False,
    notes=(
        "Operating lease: none of the five finance-lease criteria is met (no ownership "
        "transfer, no purchase option, 4/10 = 40% of economic life, PV 81,911/140,000 = "
        "58.51% of fair value, non-specialized asset routinely leased to others). "
        "Discounted at the 5% implicit rate because it is known to the lessee. "
        "Annuity due: the Jan 1 payment is 100% principal (no interest has accrued yet), "
        "so interest is accrued only at each Dec 31 on the post-payment balance. "
        "Single straight-line lease cost = 88,000/4 = 22,000 per year; the Dec 31 "
        "adjusting entry debits Lease Expense 22,000, credits Lease Liability for the "
        "interest accretion, and credits the ROU asset directly for the plug difference "
        "(chapter convention - no separate accumulated amortization account). Because "
        "there are no initial direct costs, prepaid rent or incentives, the ROU asset "
        "and lease liability carrying amounts are equal at every period end "
        "(62,907 / 42,952 / 22,000 / 0). Year 4 has zero interest because the Jan 1 Yr 4 "
        "payment retires the liability at the start of the year, so the entire 22,000 of "
        "Year 4 expense reduces the ROU asset. Current portion at 12/31/Yr1 = the 22,000 "
        "of principal retired by the Jan 1 Yr 2 payment."
    ),
)
print(json.dumps(out, indent=1))
