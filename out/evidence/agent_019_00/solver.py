#!/usr/bin/env python3
"""
Solver for item agent_019#00 — Northline Logistics Corp. / Cascade Equipment
Partners, 4-year conveyor lease (ASC 842, lessee, finance lease).

FACT PATTERN (from stem.md only):
  Commencement            Jan 1, Year 1
  Term                    4 years, noncancellable
  Payment                 $32,500 annually, due at the BEGINNING of each year
                          (Jan 1 of Years 1-4)  -> annuity DUE
  Discount rate           5% lessor implicit rate, KNOWN by lessee, so it is
                          used (the 6% IBR is not)
  Fair value              $125,000
  Economic life           4 years
  Residual / GRV          $0 / none
  Ownership transfer      No
  Purchase / renewal      None
  Specialized asset       No (standard equipment, re-leased by lessor)
  Incentives / IDC        None
  Fiscal year end         December 31

ROUNDING CONVENTION
  - All money is decimal.Decimal. No floats are used in any computation.
    Floats are produced only at JSON-serialization time, and each conversion
    is asserted to round-trip back to the exact Decimal cent value.
  - Rounding mode is ROUND_HALF_UP throughout, to the cent (0.01),
    applied PER PERIOD (round-as-you-go), which is this course's convention:
    each year's interest is rounded to the cent before it is added to the
    liability, and the next year's interest is computed on that rounded
    balance. Interest is never accumulated at full precision and rounded once
    at the end.
  - The present value of the lease payments is computed with the EXACT
    annuity-due formula at 28-significant-digit precision and rounded to the
    cent exactly once:
        PV = PMT * ((1 - (1+i)^-n) / i) * (1+i)
    The course handout (CH 17) specifies the Excel PV() function with type=1
    for this test, i.e. the closed-form formula, not a 5-decimal printed table
    factor. (Cross-check: the exact result also makes the liability schedule
    self-clear to exactly 0.00 with no plug, and divides evenly by 4 for
    straight-line amortization; a 5-decimal table factor does neither.)
  - Amortization of the ROU asset is straight-line over the LEASE TERM
    (4 years), because ownership does not transfer and no purchase option is
    reasonably certain. The final year absorbs any rounding residue so the
    ROU asset ends at exactly 0.00.
  - Per the CH 17 handout, amortization is credited directly to ROU Asset
    (the course does not use a contra "Accumulated Amortization" account).

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

CENT = Decimal("0.01")


def c(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- fact pattern
PMT = Decimal("32500")
N = 4                                   # payments / lease term in years
RATE = Decimal("0.05")                  # implicit rate, known -> use it
IBR = Decimal("0.06")                   # not used
FAIR_VALUE = Decimal("125000")
ECONOMIC_LIFE = Decimal("4")
LEASE_TERM = Decimal("4")
GRV = Decimal("0")
INCENTIVES = Decimal("0")
INITIAL_DIRECT_COSTS = Decimal("0")
TRANSFERS_OWNERSHIP = False
PURCHASE_OPTION_REASONABLY_CERTAIN = False
SPECIALIZED_NO_ALTERNATIVE_USE = False

MAJOR_PART_BRIGHT_LINE = Decimal("0.75")
SUBSTANTIALLY_ALL_BRIGHT_LINE = Decimal("0.90")


# ------------------------------------------------- (c) PV of the lease payments
def pv_annuity_due(pmt: Decimal, rate: Decimal, n: int) -> Decimal:
    """Exact closed-form PV of an n-payment annuity due (Excel PV, type=1)."""
    one = Decimal(1)
    growth = (one + rate) ** n                      # (1+i)^n
    ordinary_factor = (one - one / growth) / rate   # PVOA factor
    due_factor = ordinary_factor * (one + rate)     # x (1+i) for beginning-of-period
    return pmt * due_factor


pv_exact = pv_annuity_due(PMT, RATE, N)
lease_liability_0 = c(pv_exact)                     # liability at commencement

# ROU asset = liability - incentives + initial direct costs
rou_asset_0 = c(lease_liability_0 - INCENTIVES + INITIAL_DIRECT_COSTS)


# ------------------------------------- (a) lease identification / (b) the 5 tests
contains_lease = True
control_criteria = [
    "Identified asset: conveyor serial CLX-4419 is explicitly specified and the "
    "lessor has no substantive substitution right.",
    "Control over the period of use: Northline obtains substantially all of the "
    "economic benefits from use AND directs the use of the asset during the term.",
]

term_pct = (LEASE_TERM / ECONOMIC_LIFE) * Decimal("100")           # 100.00%
pv_pct = (lease_liability_0 / FAIR_VALUE) * Decimal("100")         # ~96.80%
term_pct_r = term_pct.quantize(CENT, rounding=ROUND_HALF_UP)
pv_pct_r = pv_pct.quantize(CENT, rounding=ROUND_HALF_UP)

test1 = TRANSFERS_OWNERSHIP
test2 = PURCHASE_OPTION_REASONABLY_CERTAIN
test3 = (LEASE_TERM / ECONOMIC_LIFE) >= MAJOR_PART_BRIGHT_LINE
test4 = (lease_liability_0 / FAIR_VALUE) >= SUBSTANTIALLY_ALL_BRIGHT_LINE
test5 = SPECIALIZED_NO_ALTERNATIVE_USE

classification = "Finance" if any([test1, test2, test3, test4, test5]) else "Operating"

classification_tests = [
    {"test": "1. Transfer of ownership by end of term", "met": test1,
     "basis": "Asset reverts to Cascade; no transfer."},
    {"test": "2. Purchase option reasonably certain of exercise", "met": test2,
     "basis": "No purchase or renewal option exists."},
    {"test": "3. Lease term is a major part of remaining economic life (>= 75%)",
     "met": test3,
     "basis": f"{LEASE_TERM} / {ECONOMIC_LIFE} = {term_pct_r}% >= 75%."},
    {"test": "4. PV of lease payments >= substantially all of fair value (>= 90%)",
     "met": test4,
     "basis": f"{lease_liability_0} / {FAIR_VALUE} = {pv_pct_r}% >= 90%."},
    {"test": "5. Specialized asset with no alternative use to lessor", "met": test5,
     "basis": "Standard equipment the lessor re-leases to others."},
]


# ---------------------------------------------- (d) the lease liability schedule
# Columns per CH 17 handout:
#   Date | Lease Payment | Interest on Liability | Lease Liability Change | Lease Liability
# Row conventions:
#   - Jan 1 Yr 1 payment carries NO interest (annuity due: paid at commencement).
#   - Each later Jan 1 payment carries the interest accrued over the prior year,
#     computed on the post-payment balance of that prior year, rounded per period.
schedule = []
balance = lease_liability_0
schedule.append({
    "date": "Jan 1, Year 1 (commencement)",
    "lease_payment": None,
    "interest_on_liability": None,
    "lease_liability_change": None,
    "lease_liability": balance,
})

dec31_balances = {}   # year -> carrying amount of lease liability at Dec 31
interest_by_year = {}  # year -> interest expense accrued during that year

for year in range(1, N + 1):
    # Jan 1 payment of `year`. Interest column = interest accrued during the
    # PRIOR year (zero for Year 1).
    interest = Decimal("0.00") if year == 1 else interest_by_year[year - 1]
    change = c(PMT - interest)            # net reduction of the liability
    balance = c(balance + interest - PMT)
    schedule.append({
        "date": f"Jan 1, Year {year}",
        "lease_payment": PMT,
        "interest_on_liability": interest,
        "lease_liability_change": change,
        "lease_liability": balance,
    })

    # Dec 31 accrual of `year` on the post-payment balance.
    if year < N:
        accrued = c(balance * RATE)
        interest_by_year[year] = accrued
        dec31_balances[year] = c(balance + accrued)
    else:
        # Year 4: liability is 0 immediately after the final Jan 1 payment,
        # so no interest accrues during Year 4.
        interest_by_year[year] = Decimal("0.00")
        dec31_balances[year] = balance

total_payments = c(PMT * N)
total_interest = c(sum(interest_by_year.values()))
total_reduction = c(total_payments - total_interest)

# Internal consistency guards (not reported):
assert schedule[-1]["lease_liability"] == Decimal("0.00"), schedule[-1]
assert total_reduction == lease_liability_0, (total_reduction, lease_liability_0)


# ------------------------------------------------- ROU asset amortization table
annual_amort = c(rou_asset_0 / Decimal(N))
amort_by_year = {}
rou_balance = rou_asset_0
rou_carrying = {}
for year in range(1, N + 1):
    amt = annual_amort if year < N else rou_balance   # last year absorbs residue
    amort_by_year[year] = amt
    rou_balance = c(rou_balance - amt)
    rou_carrying[year] = rou_balance

assert rou_carrying[N] == Decimal("0.00"), rou_carrying


# --------------------------------------------- (f) current vs noncurrent split
# The only payment in the next 12 months after Dec 31, Year 1 is the Jan 1,
# Year 2 payment. Because it falls the day after the balance sheet date, no
# further interest accretes before it; the whole $32,500 reduces principal.
# Current portion = principal reduction expected within one year.
dec31_y1_total = dec31_balances[1]
current_liability_y1 = c(PMT)
noncurrent_liability_y1 = c(dec31_y1_total - current_liability_y1)
net_rou_y1 = rou_carrying[1]


# --------------------------------------------------------- journal entries
def line(account, debit=None, credit=None):
    return {
        "account": account,
        "debit": debit if debit is not None else Decimal("0.00"),
        "credit": credit if credit is not None else Decimal("0.00"),
    }


journal_entries = []

# (e) Year 1
journal_entries.append({
    "part": "e",
    "date": "Year 1 - Jan 1 (commencement)",
    "description": "Recognize ROU asset and lease liability",
    "lines": [
        line("Right-of-Use Asset", debit=rou_asset_0),
        line("Lease Liability", credit=lease_liability_0),
    ],
})
journal_entries.append({
    "part": "e",
    "date": "Year 1 - Jan 1 (first payment)",
    "description": "First annual lease payment (annuity due; no interest yet)",
    "lines": [
        line("Lease Liability", debit=PMT),
        line("Cash", credit=PMT),
    ],
})
journal_entries.append({
    "part": "e",
    "date": "Year 1 - Dec 31 (adjusting)",
    "description": "Accrue interest on lease liability",
    "lines": [
        line("Interest Expense", debit=interest_by_year[1]),
        line("Lease Liability", credit=interest_by_year[1]),
    ],
})
journal_entries.append({
    "part": "e",
    "date": "Year 1 - Dec 31 (adjusting)",
    "description": "Straight-line amortization of ROU asset over the 4-year lease term",
    "lines": [
        line("Amortization Expense", debit=amort_by_year[1]),
        line("Right-of-Use Asset", credit=amort_by_year[1]),
    ],
})

# (g) Years 2 and 3
for year in (2, 3):
    journal_entries.append({
        "part": "g",
        "date": f"Year {year} - Jan 1",
        "description": "Annual lease payment",
        "lines": [
            line("Lease Liability", debit=PMT),
            line("Cash", credit=PMT),
        ],
    })
    journal_entries.append({
        "part": "g",
        "date": f"Year {year} - Dec 31 (adjusting)",
        "description": "Accrue interest on lease liability",
        "lines": [
            line("Interest Expense", debit=interest_by_year[year]),
            line("Lease Liability", credit=interest_by_year[year]),
        ],
    })
    journal_entries.append({
        "part": "g",
        "date": f"Year {year} - Dec 31 (adjusting)",
        "description": "Straight-line amortization of ROU asset",
        "lines": [
            line("Amortization Expense", debit=amort_by_year[year]),
            line("Right-of-Use Asset", credit=amort_by_year[year]),
        ],
    })

# (h) Year 4 settlement
journal_entries.append({
    "part": "h",
    "date": "Year 4 - Jan 1 (final payment)",
    "description": "Final lease payment; lease liability is extinguished (balance 0.00)",
    "lines": [
        line("Lease Liability", debit=PMT),
        line("Cash", credit=PMT),
    ],
})
journal_entries.append({
    "part": "h",
    "date": "Year 4 - Dec 31 (adjusting)",
    "description": ("Final amortization of ROU asset; no interest accrues in Year 4 "
                    "because the liability was zero all year. ROU asset balance 0.00 "
                    "and asset reverts to Cascade; no further entry required."),
    "lines": [
        line("Amortization Expense", debit=amort_by_year[4]),
        line("Right-of-Use Asset", credit=amort_by_year[4]),
    ],
})

for je in journal_entries:
    d = sum(l["debit"] for l in je["lines"])
    cr = sum(l["credit"] for l in je["lines"])
    assert d == cr, (je["date"], d, cr)


# ------------------------------------------------------------------- answers
answers = [
    {"label": "a: does the contract contain a lease?", "value": "Yes"},
    {"label": "b: lease term as % of remaining economic life (75% bright line)",
     "value": term_pct_r},
    {"label": "b: PV of lease payments as % of fair value (90% bright line)",
     "value": pv_pct_r},
    {"label": "b: number of the five classification criteria met",
     "value": Decimal(sum(1 for t in [test1, test2, test3, test4, test5] if t))},
    {"label": "b: lease classification", "value": classification},

    {"label": "c: lease liability at commencement", "value": lease_liability_0},
    {"label": "c: right-of-use asset at commencement", "value": rou_asset_0},

    {"label": "d: liability balance at Jan 1, Year 1 after first payment",
     "value": schedule[1]["lease_liability"]},
    {"label": "d: Year 1 interest on liability", "value": interest_by_year[1]},
    {"label": "d: Jan 1, Year 2 payment", "value": PMT},
    {"label": "d: Jan 1, Year 2 lease liability change (principal reduction)",
     "value": schedule[2]["lease_liability_change"]},
    {"label": "d: liability balance after Jan 1, Year 2 payment",
     "value": schedule[2]["lease_liability"]},
    {"label": "d: Year 2 interest on liability", "value": interest_by_year[2]},
    {"label": "d: Jan 1, Year 3 payment", "value": PMT},
    {"label": "d: Jan 1, Year 3 lease liability change (principal reduction)",
     "value": schedule[3]["lease_liability_change"]},
    {"label": "d: liability balance after Jan 1, Year 3 payment",
     "value": schedule[3]["lease_liability"]},
    {"label": "d: Year 3 interest on liability", "value": interest_by_year[3]},
    {"label": "d: Jan 1, Year 4 payment", "value": PMT},
    {"label": "d: Jan 1, Year 4 lease liability change (principal reduction)",
     "value": schedule[4]["lease_liability_change"]},
    {"label": "d: liability balance after Jan 1, Year 4 payment",
     "value": schedule[4]["lease_liability"]},
    {"label": "d: total lease payments", "value": total_payments},
    {"label": "d: total interest expense over the lease", "value": total_interest},
    {"label": "d: total lease liability reduction", "value": total_reduction},

    {"label": "f: Dec 31, Year 1 total lease liability", "value": dec31_y1_total},
    {"label": "f: Dec 31, Year 1 current lease liability", "value": current_liability_y1},
    {"label": "f: Dec 31, Year 1 noncurrent lease liability",
     "value": noncurrent_liability_y1},
    {"label": "f: Dec 31, Year 1 net right-of-use asset", "value": net_rou_y1},

    {"label": "h: ending right-of-use asset at Dec 31, Year 4", "value": rou_carrying[4]},
    {"label": "h: ending lease liability at Dec 31, Year 4", "value": dec31_balances[4]},
]


# ------------------------------------------------------------- serialization
def to_json_number(d: Decimal):
    """Decimal -> float for JSON, asserting an exact round trip."""
    f = float(d)
    assert Decimal(repr(f)) == d.normalize() or Decimal(repr(f)) == d, (d, f)
    return f


def conv(obj):
    if isinstance(obj, Decimal):
        return to_json_number(obj)
    if isinstance(obj, dict):
        return {k: conv(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [conv(v) for v in obj]
    return obj


out = {
    "id": "agent_019#00",
    "rounding_convention": (
        "decimal.Decimal only (no floats in computation); ROUND_HALF_UP to the "
        "cent applied PER PERIOD (each year's interest rounded before it accretes "
        "to the liability, next year's interest computed on the rounded balance). "
        "PV of the annuity due computed with the exact closed-form formula "
        "PMT*((1-(1+i)^-n)/i)*(1+i) at 28-digit precision, rounded to the cent once "
        "(course handout specifies Excel PV with type=1, not a printed table factor). "
        "ROU asset amortized straight-line over the 4-year lease term, final year "
        "absorbing any residue."
    ),
    "answers": conv(answers),
    "journal_entries": conv(journal_entries),
    "insufficient_info": False,
    "notes": (
        "(a) Yes - a lease exists: an identified asset (conveyor CLX-4419, no "
        "substantive substitution right) plus control over the period of use "
        "(Northline obtains substantially all economic benefits AND directs the "
        "use). (b) Finance lease: criteria 3 and 4 are met (term = 100% of "
        "economic life >= 75%; PV = 96.80% of fair value >= 90%); criteria 1, 2 "
        "and 5 are not. The 5% implicit rate is used because it is known; the 6% "
        "IBR is ignored. (h) No interest accrues in Year 4 because the Jan 1 "
        "Year 4 payment extinguishes the liability; both the ROU asset and the "
        "lease liability end at exactly 0.00 with no rounding plug. Per the CH 17 "
        "handout, ROU amortization is credited directly to Right-of-Use Asset "
        "rather than to a contra accumulated-amortization account."
    ),
    "schedule_part_d": conv(schedule),
}

print(json.dumps(out, indent=2))
