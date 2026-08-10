"""Q1 agent_285#00 -- Riverglen Industrial Supply Co. operating lease, full life cycle.

Rounding convention: all money is decimal.Decimal. Present values are computed at
FULL Decimal precision, then each period-end figure is rounded to whole dollars with
ROUND_HALF_UP (per period, not cumulatively). The lease-liability schedule is closed
EXACTLY to zero by plugging the final accrual period's interest (here the plug equals
the independently rounded figure, so no forced adjustment was needed); the ROU-asset
schedule is closed exactly to zero by plugging the final period's ROU reduction.
Every figure is derived; nothing is hard-coded. Dr = Cr in every entry.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

D = Decimal
CENT = D("1")


def r(x):
    """Whole dollars, ROUND_HALF_UP."""
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def i2(x):
    return int(r(x))


# ---------------- facts ----------------
PMT = D("22000")          # annual payment, beginning of year (annuity due)
N = 4                     # number of payments / lease term in years
IMPLICIT = D("0.05")      # lessor's implicit rate, KNOWN to lessee
IBR = D("0.06")           # lessee incremental borrowing rate (not used)
FV = D("140000")          # fair value of equipment at commencement
ECON_LIFE = D("10")       # remaining economic life, years
TERM = D(N)

# ASC 842 lessee uses the rate implicit in the lease when it is readily determinable.
RATE = IMPLICIT

# ---------------- b. commencement measurement ----------------
pv_exact = sum((PMT / (D(1) + RATE) ** k for k in range(0, N)), D(0))
LIAB0 = r(pv_exact)       # lease liability at commencement (before first payment)
ROU0 = LIAB0              # no IDC, no prepaid rent, no incentives

# ---------------- a. classification tests ----------------
pct_life = (TERM / ECON_LIFE * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
pct_fv = (LIAB0 / FV * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
crit = [
    ("transfer of ownership", False, "Equipment reverts to Summit at end of term."),
    ("purchase option reasonably certain of exercise", False, "No purchase option."),
    ("lease term is a major part of remaining economic life", False,
     f"{TERM} / {ECON_LIFE} yrs = {pct_life}% < 75%."),
    ("PV of lease payments is substantially all of fair value", False,
     f"{LIAB0} / {FV} = {pct_fv}% < 90%."),
    ("specialized asset with no alternative use to lessor", False,
     "Summit routinely leases this equipment to other customers."),
]
classification = "operating"

# ---------------- c. lease liability schedule (annuity due) ----------------
# Rows: (date, payment, interest, reduction/(increase) of liability, ending balance)
liab_rows = []
bal = LIAB0
liab_rows.append({"date": "1/1/Yr1 (commencement)", "payment": 0, "interest": 0,
                  "reduction": 0, "balance": i2(bal)})
interest_by_year = {}
for yr in range(1, N + 1):
    # beginning-of-year payment
    bal = bal - PMT
    liab_rows.append({"date": f"1/1/Yr{yr} payment", "payment": i2(PMT), "interest": 0,
                      "reduction": i2(PMT), "balance": i2(bal)})
    # year-end accrual of interest on the outstanding balance
    if yr < N:
        computed = r(bal * RATE)
        if yr == N - 1:
            # final accrual period: PLUG so the liability equals the last payment and
            # therefore clears exactly to zero on 1/1 of the final year.
            plug = PMT - bal
            interest = plug
        else:
            interest = computed
    else:
        interest = D(0)   # nothing outstanding during the final year
    bal = bal + interest
    interest_by_year[yr] = interest
    liab_rows.append({"date": f"12/31/Yr{yr} accrual", "payment": 0,
                      "interest": i2(interest), "reduction": -i2(interest),
                      "balance": i2(bal)})
assert bal == 0, bal
TOT_PMTS = PMT * N
TOT_INT = sum(interest_by_year.values(), D(0))
assert TOT_INT == TOT_PMTS - LIAB0

# ---------------- straight-line single lease cost ----------------
SL_EXPENSE = r(TOT_PMTS / D(N))

# ---------------- c. right-of-use asset schedule ----------------
rou_rows = []
rou = ROU0
rou_rows.append({"year": "1/1/Yr1 (commencement)", "lease_expense": 0,
                 "interest_on_liability": 0, "rou_reduction": 0, "rou_balance": i2(rou)})
rou_red_by_year = {}
for yr in range(1, N + 1):
    interest = interest_by_year[yr]
    red = SL_EXPENSE - interest
    if yr == N:
        red = rou      # plug the final period so the ROU asset closes exactly to zero
    rou = rou - red
    rou_red_by_year[yr] = red
    rou_rows.append({"year": f"Yr{yr}", "lease_expense": i2(SL_EXPENSE),
                     "interest_on_liability": i2(interest), "rou_reduction": i2(red),
                     "rou_balance": i2(rou)})
assert rou == 0, rou

# year-end balances for presentation
liab_ye = {}
rou_ye = {}
b = LIAB0
for yr in range(1, N + 1):
    b = b - PMT + interest_by_year[yr]
    liab_ye[yr] = b
x = ROU0
for yr in range(1, N + 1):
    x = x - rou_red_by_year[yr]
    rou_ye[yr] = x

# ---------------- e. balance sheet split at 12/31/Yr1 ----------------
CURRENT_1 = liab_ye[1] - liab_ye[2]        # reduction of the liability over next 12 months
NONCURRENT_1 = liab_ye[2]
assert CURRENT_1 + NONCURRENT_1 == liab_ye[1]

# ---------------- journal entries ----------------
JE = []


def je(part, date, desc, lines):
    dr = sum(D(l[1]) for l in lines)
    cr = sum(D(l[2]) for l in lines)
    assert dr == cr, (part, date, dr, cr)
    JE.append({"part": part, "date": date, "description": desc,
               "lines": [{"account": a, "debit": int(d), "credit": int(c)} for a, d, c in lines]})


je("d", "Jan 1, Yr 1", "Commencement - recognize ROU asset and lease liability",
   [("Right-of-Use Asset - Operating Lease", i2(ROU0), 0),
    ("Lease Liability", 0, i2(LIAB0))])
je("d", "Jan 1, Yr 1", "First annual lease payment (annuity due; no interest yet accrued)",
   [("Lease Liability", i2(PMT), 0),
    ("Cash", 0, i2(PMT))])
je("d", "Dec 31, Yr 1", "Period-end adjusting entry - single operating lease expense",
   [("Lease Expense", i2(SL_EXPENSE), 0),
    ("Lease Liability", 0, i2(interest_by_year[1])),
    ("Right-of-Use Asset - Operating Lease", 0, i2(rou_red_by_year[1]))])
for yr in (2, 3):
    je("f", f"Jan 1, Yr {yr}", "Annual lease payment",
       [("Lease Liability", i2(PMT), 0), ("Cash", 0, i2(PMT))])
    je("f", f"Dec 31, Yr {yr}", "Period-end adjusting entry - single operating lease expense",
       [("Lease Expense", i2(SL_EXPENSE), 0),
        ("Lease Liability", 0, i2(interest_by_year[yr])),
        ("Right-of-Use Asset - Operating Lease", 0, i2(rou_red_by_year[yr]))])
je("g", "Jan 1, Yr 4", "Final annual lease payment - lease liability settled in full",
   [("Lease Liability", i2(PMT), 0), ("Cash", 0, i2(PMT))])
je("g", "Dec 31, Yr 4", "Period-end adjusting entry - no interest (liability already zero); ROU written off",
   [("Lease Expense", i2(SL_EXPENSE), 0),
    ("Right-of-Use Asset - Operating Lease", 0, i2(rou_red_by_year[4]))])

# ---------------- answers ----------------
A = []


def add(label, value):
    A.append({"label": label, "value": value})


# a
for name, met, why in crit:
    add(f"a: Criterion - {name}", f"Not met. {why}")
add("a: Classification for Riverglen", "Operating lease - none of the five finance-lease criteria is met")
add("a: Discount rate used", "5% - the rate implicit in the lease, which is known to Riverglen (the 6% IBR is not used)")
add("a: Lease term as % of remaining economic life", float(pct_life))
add("a: PV of lease payments as % of fair value", float(pct_fv))
# b
add("b: Lease liability at commencement (PV of 4 payments of $22,000, annuity due, 5%)", i2(LIAB0))
add("b: Right-of-use asset at commencement (before first payment)", i2(ROU0))
# c
for row in liab_rows:
    add(f"c: Lease liability schedule - {row['date']} - payment", row["payment"])
    add(f"c: Lease liability schedule - {row['date']} - interest expense (5%)", row["interest"])
    add(f"c: Lease liability schedule - {row['date']} - reduction of liability", row["reduction"])
    add(f"c: Lease liability schedule - {row['date']} - lease liability balance", row["balance"])
add("c: Lease liability schedule - total payments", i2(TOT_PMTS))
add("c: Lease liability schedule - total interest", i2(TOT_INT))
add("c: Lease liability schedule - total reduction of liability", i2(LIAB0))
for row in rou_rows:
    add(f"c: ROU asset schedule - {row['year']} - straight-line lease expense", row["lease_expense"])
    add(f"c: ROU asset schedule - {row['year']} - interest on lease liability", row["interest_on_liability"])
    add(f"c: ROU asset schedule - {row['year']} - reduction (amortization) of ROU asset", row["rou_reduction"])
    add(f"c: ROU asset schedule - {row['year']} - ROU asset balance", row["rou_balance"])
add("c: ROU asset schedule - total lease expense", i2(TOT_PMTS))
add("c: ROU asset schedule - total interest component", i2(TOT_INT))
add("c: ROU asset schedule - total ROU reduction", i2(ROU0))
# e
add("e: Year 1 income statement - single operating lease expense (operating expense)", i2(SL_EXPENSE))
add("e: BS 12/31/Yr1 - Right-of-use asset (noncurrent)", i2(rou_ye[1]))
add("e: BS 12/31/Yr1 - Lease liability, current portion", i2(CURRENT_1))
add("e: BS 12/31/Yr1 - Lease liability, noncurrent portion", i2(NONCURRENT_1))
add("e: BS 12/31/Yr1 - Total lease liability", i2(liab_ye[1]))
# g
add("g: Lease liability balance after the Jan 1, Yr 4 final payment", i2(D(0)))
add("g: Lease liability balance at 12/31/Yr4 (lease end)", i2(liab_ye[4]))
add("g: Right-of-use asset balance at 12/31/Yr4 (lease end)", i2(rou_ye[4]))

out = {
    "id": "agent_285#00",
    "rounding_convention": ("decimal.Decimal throughout; PV of the annuity due computed at full precision "
                            "then rounded to the nearest whole dollar (ROUND_HALF_UP) at commencement, and every "
                            "schedule/JE amount stated in whole dollars rounded ROUND_HALF_UP per period. "
                            "Final accrual period's interest is plugged so the lease liability clears exactly to $0 "
                            "(the plug equals the rounded 5% figure, $1,048, so no forced adjustment arose); the "
                            "final-year ROU reduction is plugged so the ROU asset closes exactly to $0."),
    "answers": A,
    "journal_entries": JE,
    "insufficient_info": False,
    "notes": ("Operating lease (ASC 842 lessee): none of the five finance criteria met - no transfer, no purchase "
              "option, 4/10 = 40% of economic life, PV $81,911 / FV $140,000 = 58.51%, and the forklifts are not "
              "specialized (Summit routinely leases them to others). Discount rate = 5% implicit rate because it is "
              "known to Riverglen. Payments are an annuity due, so the Jan 1 Yr1 payment reduces the liability with "
              "no interest, and the liability accretes 5% on the outstanding balance during each year. Single lease "
              "cost is straight-line: $88,000 / 4 = $22,000 per year; the period-end adjusting entry debits Lease "
              "Expense $22,000, credits Lease Liability for the year's interest accretion, and credits the ROU asset "
              "directly for the plug (chapter convention - no separate accumulated amortization). Because there are "
              "no IDC/prepaid rent/incentives, the ROU asset equals the lease liability at every year end. Current "
              "portion at 12/31/Yr1 is the net reduction of the liability during Yr2 ($62,907 - $42,952 = $19,955); "
              "the $22,000 payment due 1/1/Yr2 less the $2,045 of Yr2 accretion gives the same amount. During Year 4 "
              "the liability is zero all year, so no interest accrues and the entire $22,000 of lease expense is "
              "charged against the ROU asset, leaving both accounts at $0.")
}
print(json.dumps(out, indent=1))
