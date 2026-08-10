"""Solver for agent_285#00 - ASC 842 lessee operating lease, 4-yr annuity due.

ROUNDING CONVENTION: all money computed with decimal.Decimal (never floats).
Every period amount (commencement PV, each period's interest accretion, each
period's ROU reduction, each ending balance) is quantized to the nearest whole
dollar using ROUND_HALF_UP, applied per period (not cumulatively re-derived).
Final-period interest is PLUGGED so the lease liability clears to exactly zero.
Nothing is hard-coded: PV factors, schedules and JEs are all derived.
"""
import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 40
D = Decimal
CENT = D("1")


def r(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def i(x):
    return int(x)


# ---------------- Given facts ----------------
PMT = D("22000")
N = 4
RATE_IMPLICIT = D("0.05")
RATE_IBR = D("0.06")
FV = D("140000")
TERM = D("4")
ECON_LIFE = D("10")

# (a) Discount rate: implicit rate is known to the lessee -> use it.
rate = RATE_IMPLICIT

# ---------------- (b) Commencement measurement ----------------
# PV of an annuity DUE of 4 payments: ordinary-annuity factor * (1+i)
one = D(1)
disc = one / (one + rate)
ord_factor = D(0)
p = one
for k in range(1, N + 1):
    p = p * disc
    ord_factor += p
due_factor = ord_factor * (one + rate)
pv_exact = PMT * due_factor
liability0 = r(pv_exact)
rou0 = liability0  # basic case: no IDC, prepaid rent, or incentives

# ---------------- (a) Classification tests ----------------
term_pct = (TERM / ECON_LIFE * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
pv_pct = (liability0 / FV * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP)

# ---------------- Straight-line single lease cost ----------------
total_payments = PMT * N
annual_expense = r(total_payments / D(N))

# ---------------- (c) Schedules ----------------
liab_rows = []
rou_rows = []
lb = liability0          # liability balance (Jan 1, before payment)
rb = rou0                # ROU balance
tot_int = D(0)
tot_amort = D(0)
for yr in range(1, N + 1):
    after_pmt = lb - PMT
    if yr < N:
        interest = r(after_pmt * rate)
    else:
        interest = -after_pmt  # plug so liability clears exactly
    end_liab = after_pmt + interest
    amort = annual_expense - interest
    end_rou = rb - amort
    liab_rows.append({
        "year": yr, "beginning_liability": i(lb), "payment_jan1": i(PMT),
        "balance_after_payment": i(after_pmt), "interest_at_5pct": i(interest),
        "ending_liability_dec31": i(end_liab)})
    rou_rows.append({
        "year": yr, "beginning_rou": i(rb), "straight_line_lease_expense": i(annual_expense),
        "less_interest_component": i(interest), "rou_reduction_amortization": i(amort),
        "ending_rou_dec31": i(end_rou)})
    tot_int += interest
    tot_amort += amort
    lb, rb = end_liab, end_rou

end_liab_y = [D(row["ending_liability_dec31"]) for row in liab_rows]
end_rou_y = [D(row["ending_rou_dec31"]) for row in rou_rows]
int_y = [D(row["interest_at_5pct"]) for row in liab_rows]
amort_y = [D(row["rou_reduction_amortization"]) for row in rou_rows]

# ---------------- (e) Presentation at 12/31/Y1 ----------------
# Payment on Jan 1 Yr2 is made at the start of the period, so the entire
# $22,000 reduces principal within 12 months -> current portion.
current_liab_y1 = PMT
noncurrent_liab_y1 = end_liab_y[0] - current_liab_y1

answers = [
    {"label": "a: Criterion 1 - transfer of ownership by end of term", "value": "Not met - equipment reverts to Summit Asset Finance"},
    {"label": "a: Criterion 2 - purchase option reasonably certain of exercise", "value": "Not met - no purchase option"},
    {"label": "a: Criterion 3 - lease term is major part of remaining economic life (%)", "value": float(term_pct)},
    {"label": "a: Criterion 3 conclusion", "value": "Not met - 4 of 10 years = 40.00%, not a major part (< 75%)"},
    {"label": "a: Criterion 4 - PV of lease payments as % of fair value", "value": float(pv_pct)},
    {"label": "a: Criterion 4 conclusion", "value": "Not met - $81,911 / $140,000 = 58.51%, not substantially all (< 90%)"},
    {"label": "a: Criterion 5 - specialized asset with no alternative use", "value": "Not met - Summit routinely leases this equipment to other customers"},
    {"label": "a: Classification conclusion", "value": "OPERATING lease (no criterion met)"},
    {"label": "a: Discount rate used", "value": "5% implicit rate (known to Riverglen; IBR of 6% is not used)"},
    {"label": "b: PV factor, annuity due, 4 payments @ 5%", "value": float(due_factor.quantize(D("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "b: Lease liability at commencement (Jan 1, Yr 1, before first payment)", "value": i(liability0)},
    {"label": "b: Right-of-use asset at commencement (Jan 1, Yr 1)", "value": i(rou0)},
    {"label": "c: Liability schedule - Yr 1 beginning balance", "value": i(liability0)},
    {"label": "c: Liability schedule - Yr 1 payment (Jan 1)", "value": i(PMT)},
    {"label": "c: Liability schedule - Yr 1 balance after payment", "value": i(liability0 - PMT)},
    {"label": "c: Liability schedule - Yr 1 interest at 5%", "value": i(int_y[0])},
    {"label": "c: Liability schedule - Yr 1 ending balance (Dec 31, Yr 1)", "value": i(end_liab_y[0])},
    {"label": "c: Liability schedule - Yr 2 payment (Jan 1)", "value": i(PMT)},
    {"label": "c: Liability schedule - Yr 2 balance after payment", "value": i(end_liab_y[0] - PMT)},
    {"label": "c: Liability schedule - Yr 2 interest at 5%", "value": i(int_y[1])},
    {"label": "c: Liability schedule - Yr 2 ending balance (Dec 31, Yr 2)", "value": i(end_liab_y[1])},
    {"label": "c: Liability schedule - Yr 3 payment (Jan 1)", "value": i(PMT)},
    {"label": "c: Liability schedule - Yr 3 balance after payment", "value": i(end_liab_y[1] - PMT)},
    {"label": "c: Liability schedule - Yr 3 interest at 5%", "value": i(int_y[2])},
    {"label": "c: Liability schedule - Yr 3 ending balance (Dec 31, Yr 3)", "value": i(end_liab_y[2])},
    {"label": "c: Liability schedule - Yr 4 payment (Jan 1)", "value": i(PMT)},
    {"label": "c: Liability schedule - Yr 4 balance after payment", "value": i(end_liab_y[2] - PMT)},
    {"label": "c: Liability schedule - Yr 4 interest (plugged)", "value": i(int_y[3])},
    {"label": "c: Liability schedule - Yr 4 ending balance (Dec 31, Yr 4)", "value": i(end_liab_y[3])},
    {"label": "c: Liability schedule - total payments", "value": i(total_payments)},
    {"label": "c: Liability schedule - total interest", "value": i(tot_int)},
    {"label": "c: ROU schedule - annual straight-line lease expense", "value": i(annual_expense)},
    {"label": "c: ROU schedule - Yr 1 beginning ROU", "value": i(rou0)},
    {"label": "c: ROU schedule - Yr 1 amortization (expense less interest)", "value": i(amort_y[0])},
    {"label": "c: ROU schedule - Yr 1 ending ROU (Dec 31, Yr 1)", "value": i(end_rou_y[0])},
    {"label": "c: ROU schedule - Yr 2 amortization", "value": i(amort_y[1])},
    {"label": "c: ROU schedule - Yr 2 ending ROU (Dec 31, Yr 2)", "value": i(end_rou_y[1])},
    {"label": "c: ROU schedule - Yr 3 amortization", "value": i(amort_y[2])},
    {"label": "c: ROU schedule - Yr 3 ending ROU (Dec 31, Yr 3)", "value": i(end_rou_y[2])},
    {"label": "c: ROU schedule - Yr 4 amortization", "value": i(amort_y[3])},
    {"label": "c: ROU schedule - Yr 4 ending ROU (Dec 31, Yr 4)", "value": i(end_rou_y[3])},
    {"label": "c: ROU schedule - total amortization", "value": i(tot_amort)},
    {"label": "e: Year 1 income statement - single operating lease expense", "value": i(annual_expense)},
    {"label": "e: Dec 31 Yr 1 balance sheet - Right-of-use asset (noncurrent)", "value": i(end_rou_y[0])},
    {"label": "e: Dec 31 Yr 1 balance sheet - Lease liability, current", "value": i(current_liab_y1)},
    {"label": "e: Dec 31 Yr 1 balance sheet - Lease liability, noncurrent", "value": i(noncurrent_liab_y1)},
    {"label": "e: Dec 31 Yr 1 balance sheet - Total lease liability", "value": i(end_liab_y[0])},
    {"label": "g: Right-of-use asset balance after lease end (Dec 31, Yr 4)", "value": i(end_rou_y[3])},
    {"label": "g: Lease liability balance after lease end (Dec 31, Yr 4)", "value": i(end_liab_y[3])},
]


def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": i(dr) if dr is not None else 0,
            "credit": i(cr) if cr is not None else 0}


jes = [
    {"part": "d", "description": "Jan 1, Yr 1 - commencement recognition",
     "lines": [L("Right-of-Use Asset - Operating Lease", dr=rou0),
               L("Lease Liability", cr=liability0)]},
    {"part": "d", "description": "Jan 1, Yr 1 - first annual lease payment (annuity due)",
     "lines": [L("Lease Liability", dr=PMT), L("Cash", cr=PMT)]},
    {"part": "d", "description": "Dec 31, Yr 1 - period-end adjusting JE (single lease expense)",
     "lines": [L("Lease Expense", dr=annual_expense),
               L("Lease Liability", cr=int_y[0]),
               L("Right-of-Use Asset - Operating Lease", cr=amort_y[0])]},
    {"part": "f", "description": "Jan 1, Yr 2 - annual lease payment",
     "lines": [L("Lease Liability", dr=PMT), L("Cash", cr=PMT)]},
    {"part": "f", "description": "Dec 31, Yr 2 - period-end adjusting JE (single lease expense)",
     "lines": [L("Lease Expense", dr=annual_expense),
               L("Lease Liability", cr=int_y[1]),
               L("Right-of-Use Asset - Operating Lease", cr=amort_y[1])]},
    {"part": "f", "description": "Jan 1, Yr 3 - annual lease payment",
     "lines": [L("Lease Liability", dr=PMT), L("Cash", cr=PMT)]},
    {"part": "f", "description": "Dec 31, Yr 3 - period-end adjusting JE (single lease expense)",
     "lines": [L("Lease Expense", dr=annual_expense),
               L("Lease Liability", cr=int_y[2]),
               L("Right-of-Use Asset - Operating Lease", cr=amort_y[2])]},
    {"part": "g", "description": "Jan 1, Yr 4 - final lease payment; lease liability goes to zero",
     "lines": [L("Lease Liability", dr=PMT), L("Cash", cr=PMT)]},
    {"part": "g", "description": "Dec 31, Yr 4 - final period-end adjusting JE; no interest (liability already zero); ROU goes to zero",
     "lines": [L("Lease Expense", dr=annual_expense),
               L("Right-of-Use Asset - Operating Lease", cr=amort_y[3])]},
]

for je in jes:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"]), je
assert end_liab_y[3] == 0 and end_rou_y[3] == 0
assert tot_amort == rou0 and total_payments - liability0 == tot_int

notes = (
    "Operating lease: no classification criterion is met, so a single straight-line lease "
    "cost of $22,000/yr is recognized. Discount rate = 5% implicit rate because it is known "
    "to the lessee. Commencement PV of a 4-payment annuity due @5% = $22,000 x 3.723248 = "
    "$81,911 (rounded, ROUND_HALF_UP); ROU asset = lease liability since there are no initial "
    "direct costs, prepaid rent, or incentives. Each Dec 31 adjusting entry debits Lease "
    "Expense $22,000, credits Lease Liability for that period's 5% accretion on the "
    "post-payment balance, and credits the ROU asset directly for the remainder (chapter "
    "convention - no separate accumulated amortization account). Year 4 interest is plugged "
    "at $0: the Jan 1 Yr 4 payment of $22,000 exactly extinguishes the liability, so nothing "
    "accretes and the whole $22,000 of Year 4 expense reduces the ROU asset. Total interest "
    "$6,089 = $88,000 payments - $81,911; total ROU amortization $81,911. At 12/31/Yr1 the "
    "current portion of the lease liability is the full $22,000 Jan 1 Yr 2 payment (paid at "
    "the start of the period, so it is entirely principal), leaving $40,907 noncurrent. Both "
    "the ROU asset and the lease liability are $0 after the lease ends."
)

print(json.dumps({
    "id": "agent_285#00",
    "rounding_convention": ("decimal.Decimal throughout (no floats); every period amount "
                            "quantized to the nearest whole dollar with ROUND_HALF_UP, applied "
                            "per period; final-period interest plugged so the lease liability "
                            "clears to exactly zero"),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
