#!/usr/bin/env python3
"""Blind solver for item agent_022#01 - Northwind Packaging / Lakeside Capital Leasing.

Full basic finance lease (lessee, ASC 842), 4-year term, annuity-due payments.

ROUNDING CONVENTION
-------------------
* All money is `decimal.Decimal`. No floats are used anywhere in the derivation;
  floats appear only at the final JSON serialization step.
* Working precision is 40 significant digits (`getcontext().prec = 40`).
* Money is rounded to the CENT with ROUND_HALF_UP, applied PER PERIOD (each
  year's interest accrual is rounded to the cent before it is added to the
  liability, and the rounded figure is the carrying basis for the next period).
* Present value is computed from the EXACT annuity-due formula
      PVAD(r, n) = sum_{k=0}^{n-1} (1 + r)^(-k)
  not from a 5-decimal PV table factor. This matches the course handout, which
  measures the liability with Excel's =PV(rate, nper, pmt, [fv], [type]) using
  type = 1 for payments due at the beginning of the period.
* AMORTIZATION-TABLE PLUG: the stated annual payment ($85,946.46) is itself the
  cent-rounded annuity-due payment for a $320,000 present value, so it cannot
  amortize the liability to exactly zero under per-period cent rounding. Total
  interest over the lease is therefore fixed as
      (total cash payments) - (initial lease liability),
  and the FINAL interest period absorbs the accumulated rounding difference
  (the standard last-period plug used in amortization schedules). This is what
  makes the schedule's Interest column foot to the total and the final payment
  extinguish the liability exactly, as Required part (f) demands.
* Straight-line ROU amortization is computed once (cost / lease term) and used
  for every period; it divides evenly here, so no per-period plug is needed.

Run: python3 solver.py   ->   prints one JSON object on stdout.
"""

import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 40

CENT = Decimal("0.01")
ZERO = Decimal("0.00")


def c(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# 1. Facts taken from the stem (nothing else is assumed)
# ---------------------------------------------------------------------------
FAIR_VALUE = Decimal("320000")          # fact 3
PAYMENT = Decimal("85946.46")           # fact 2, due each January 1 (annuity due)
N_PAYMENTS = 4                          # fact 2
LEASE_TERM_YEARS = 4                    # fact 1
ECONOMIC_LIFE_YEARS = 4                 # fact 3
RESIDUAL_ESTIMATE = Decimal("0")        # fact 3, no guarantee
IMPLICIT_RATE = Decimal("0.05")         # fact 4, known to lessee
IBR = Decimal("0.055")                  # fact 4
OWNERSHIP_TRANSFERS = False             # fact 1: equipment reverts to lessor
PURCHASE_OPTION = False                 # fact 3
SPECIALIZED = False                     # fact 1: nonspecialized
INITIAL_DIRECT_COSTS = Decimal("0")     # fact 5: no ROU adjustments
LEASE_INCENTIVES = Decimal("0")         # fact 5

MAJOR_PART_THRESHOLD = Decimal("0.75")      # course handout: 75% = "major part"
SUBSTANTIALLY_ALL_THRESHOLD = Decimal("0.90")  # course handout: 90%

# ---------------------------------------------------------------------------
# 2. (a) Discount rate and classification
# ---------------------------------------------------------------------------
# ASC 842: use the rate implicit in the lease when the lessee knows it;
# fall back to the IBR only when it is not readily determinable.
DISCOUNT_RATE = IMPLICIT_RATE if IMPLICIT_RATE is not None else IBR
rate_basis = "rate implicit in the lease (known to lessee); IBR of 5.5% not used"

# Exact annuity-due present value factor: payments at the START of each period.
pvad_factor = sum(
    (Decimal(1) + DISCOUNT_RATE) ** Decimal(-k) for k in range(N_PAYMENTS)
)

pv_of_payments_exact = PAYMENT * pvad_factor

term_ratio = Decimal(LEASE_TERM_YEARS) / Decimal(ECONOMIC_LIFE_YEARS)
pv_ratio = pv_of_payments_exact / FAIR_VALUE

test_ownership = OWNERSHIP_TRANSFERS
test_purchase = PURCHASE_OPTION
test_term = term_ratio >= MAJOR_PART_THRESHOLD
test_pv = pv_ratio >= SUBSTANTIALLY_ALL_THRESHOLD
test_specialized = SPECIALIZED

is_finance = any([test_ownership, test_purchase, test_term, test_pv, test_specialized])
classification = "Finance lease" if is_finance else "Operating lease"

tests_met = [
    name
    for name, met in [
        ("ownership transfer", test_ownership),
        ("purchase option", test_purchase),
        ("lease term / major part of economic life", test_term),
        ("PV of lease payments / substantially all of fair value", test_pv),
        ("specialized asset with no alternative use", test_specialized),
    ]
    if met
]
assert tests_met, "no classification test met"

# ---------------------------------------------------------------------------
# 3. (b) Commencement measurement
# ---------------------------------------------------------------------------
# The stem's payment is quoted to the cent. Check whether it IS the cent-rounded
# annuity-due payment that amortizes the $320,000 fair value at 5%; if so the
# designed present value is the fair value itself and the sub-cent gap in
# `pv_of_payments_exact` is purely an artifact of quoting the payment to a cent.
implied_payment_exact = FAIR_VALUE / pvad_factor
payment_is_designed_from_fv = c(implied_payment_exact) == PAYMENT

pv_rounded = c(pv_of_payments_exact)
pv_gap = (FAIR_VALUE - pv_of_payments_exact).copy_abs()
# Quoting the payment to the nearest cent can move the present value by at most
# half a cent times the annuity-due factor. A gap inside that band proves the
# difference is an artifact of quoting the payment, not a real economic gap.
pv_gap_tolerance = (CENT / Decimal(2)) * pvad_factor

if payment_is_designed_from_fv and pv_gap <= pv_gap_tolerance:
    lease_liability_0 = c(FAIR_VALUE)
    measurement_note = (
        "PV of the four annuity-due payments at 5%% computes to $%s; the stated "
        "payment is exactly the cent-rounded annuity-due payment for a $%s "
        "present value, and the $%s gap is inside the $%s band that quoting the "
        "payment to a cent can create, so the liability is measured at $%s "
        "(= fair value, consistent with the 4-year full-payout structure)."
        % (pv_rounded, c(FAIR_VALUE), c(pv_gap), c(pv_gap_tolerance), c(FAIR_VALUE))
    )
else:
    lease_liability_0 = pv_rounded
    measurement_note = (
        "Liability measured at the exact PV of the lease payments, $%s." % pv_rounded
    )

# ROU asset = liability + initial direct costs - lease incentives (both zero here)
rou_asset_0 = c(lease_liability_0 + INITIAL_DIRECT_COSTS - LEASE_INCENTIVES)

# ---------------------------------------------------------------------------
# 4. (c) Lease liability schedule
# ---------------------------------------------------------------------------
total_payments = c(PAYMENT * N_PAYMENTS)
total_interest = c(total_payments - lease_liability_0)

# Interest accrues at each Dec 31 for the 3 years the liability is outstanding
# (after the Jan 1 Year 4 payment the liability is gone, so Year 4 has none).
n_interest_periods = N_PAYMENTS - 1

schedule = []
schedule.append(
    {
        "date": "1/1/Year 1 (commencement)",
        "lease_payment": None,
        "interest_on_liability": None,
        "lease_liability_change": None,
        "lease_liability": lease_liability_0,
    }
)

balance = lease_liability_0
interest_by_year = []          # interest accrued during Year 1, 2, 3
balance_at_dec31 = []          # liability balance at each Dec 31

# First payment, at commencement: no interest has accrued yet.
balance = c(balance - PAYMENT)
schedule.append(
    {
        "date": "1/1/Year 1",
        "lease_payment": PAYMENT,
        "interest_on_liability": ZERO,
        "lease_liability_change": PAYMENT,
        "lease_liability": balance,
    }
)

plug_basis_balance = None
plug_mechanical = None
plug_amount = None

for k in range(1, n_interest_periods + 1):
    mechanical = c(balance * DISCOUNT_RATE)            # per-period ROUND_HALF_UP
    if k < n_interest_periods:
        interest = mechanical
    else:
        # Final interest period absorbs accumulated cent rounding so the
        # Interest column foots to total_interest and the last payment clears
        # the liability exactly.
        interest = c(total_interest - sum(interest_by_year))
        plug_basis_balance = balance
        plug_mechanical = mechanical
        plug_amount = c(interest - mechanical).copy_abs()
    interest_by_year.append(interest)

    dec31 = c(balance + interest)
    balance_at_dec31.append(dec31)

    reduction = c(PAYMENT - interest)
    balance = c(dec31 - PAYMENT)
    schedule.append(
        {
            "date": "1/1/Year %d" % (k + 1),
            "lease_payment": PAYMENT,
            "interest_on_liability": interest,
            "lease_liability_change": reduction,
            "lease_liability": balance,
        }
    )

assert balance == ZERO, "schedule must amortize to zero, got %s" % balance
assert c(sum(interest_by_year)) == total_interest
assert c(sum(r["lease_liability_change"] for r in schedule[1:])) == lease_liability_0

# ---------------------------------------------------------------------------
# 5. ROU asset amortization
# ---------------------------------------------------------------------------
# No transfer of ownership and no purchase option -> amortize straight-line over
# the LEASE TERM (which equals economic life here anyway), to the $0 residual.
amort_years = LEASE_TERM_YEARS
annual_amortization = c((rou_asset_0 - RESIDUAL_ESTIMATE) / Decimal(amort_years))

rou_by_year_end = []
rou = rou_asset_0
for y in range(1, amort_years + 1):
    if y < amort_years:
        rou = c(rou - annual_amortization)
    else:
        rou = ZERO  # final period absorbs any rounding (none needed here)
    rou_by_year_end.append(rou)

assert rou_by_year_end[-1] == ZERO
rou_end_y1 = rou_by_year_end[0]
rou_end_y4 = rou_by_year_end[-1]

# ---------------------------------------------------------------------------
# 6. (e) Dec 31, Year 1 balance-sheet split
# ---------------------------------------------------------------------------
liab_dec31_y1 = balance_at_dec31[0]
# Current = the portion of the liability that will be extinguished within 12
# months. The 1/1/Year 2 payment is made with no further interest accrual
# between 12/31/Year 1 and 1/1/Year 2, so the whole payment reduces principal.
current_portion_y1 = c(PAYMENT)
noncurrent_portion_y1 = c(liab_dec31_y1 - current_portion_y1)
assert c(current_portion_y1 + noncurrent_portion_y1) == liab_dec31_y1

# ---------------------------------------------------------------------------
# 7. (d) and (f) journal entries
# ---------------------------------------------------------------------------
interest_y1 = interest_by_year[0]
final_payment = PAYMENT
liab_before_final_payment = balance_at_dec31[-1]
assert liab_before_final_payment == final_payment, (
    "final payment must exactly clear the liability: %s vs %s"
    % (liab_before_final_payment, final_payment)
)

journal_entries = [
    {
        "part": "d",
        "date": "Jan 1, Year 1",
        "description": "Commencement - recognize ROU asset and lease liability",
        "lines": [
            {"account": "Right-of-Use Asset", "debit": rou_asset_0, "credit": ZERO},
            {"account": "Lease Liability", "debit": ZERO, "credit": lease_liability_0},
        ],
    },
    {
        "part": "d",
        "date": "Jan 1, Year 1",
        "description": "First annual lease payment (annuity due - all principal)",
        "lines": [
            {"account": "Lease Liability", "debit": PAYMENT, "credit": ZERO},
            {"account": "Cash", "debit": ZERO, "credit": PAYMENT},
        ],
    },
    {
        "part": "d",
        "date": "Dec 31, Year 1",
        "description": "Accrue interest on lease liability",
        "lines": [
            {"account": "Interest Expense", "debit": interest_y1, "credit": ZERO},
            {"account": "Lease Liability", "debit": ZERO, "credit": interest_y1},
        ],
    },
    {
        "part": "d",
        "date": "Dec 31, Year 1",
        "description": "Straight-line amortization of ROU asset",
        "lines": [
            {"account": "Amortization Expense", "debit": annual_amortization, "credit": ZERO},
            {"account": "Right-of-Use Asset", "debit": ZERO, "credit": annual_amortization},
        ],
    },
    {
        "part": "f",
        "date": "Jan 1, Year 4",
        "description": "Final annual lease payment - extinguishes lease liability",
        "lines": [
            {"account": "Lease Liability", "debit": final_payment, "credit": ZERO},
            {"account": "Cash", "debit": ZERO, "credit": final_payment},
        ],
    },
    {
        "part": "f",
        "date": "Dec 31, Year 4",
        "description": "Final straight-line amortization of ROU asset",
        "lines": [
            {"account": "Amortization Expense", "debit": annual_amortization, "credit": ZERO},
            {"account": "Right-of-Use Asset", "debit": ZERO, "credit": annual_amortization},
        ],
    },
]

for je in journal_entries:
    d = c(sum(l["debit"] for l in je["lines"]))
    cr = c(sum(l["credit"] for l in je["lines"]))
    assert d == cr, "entry out of balance (%s %s): %s vs %s" % (je["part"], je["date"], d, cr)

# ---------------------------------------------------------------------------
# 8. Assemble the Required-part answers
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: lease classification", "value": classification},
    {"label": "a: discount rate applied (annual %)", "value": DISCOUNT_RATE * Decimal(100)},
    {"label": "b: right-of-use asset at commencement (1/1/Year 1)", "value": rou_asset_0},
    {"label": "b: lease liability at commencement (1/1/Year 1)", "value": lease_liability_0},
]

# (c) full schedule, row by row
answers.append({"label": "c: schedule - lease liability 1/1/Year 1 before payment",
                "value": lease_liability_0})
row_labels = ["1/1/Year 1", "1/1/Year 2", "1/1/Year 3", "1/1/Year 4"]
for row, lbl in zip(schedule[1:], row_labels):
    answers.append({"label": "c: schedule %s - lease payment" % lbl,
                    "value": row["lease_payment"]})
    answers.append({"label": "c: schedule %s - interest on liability" % lbl,
                    "value": row["interest_on_liability"]})
    answers.append({"label": "c: schedule %s - lease liability change" % lbl,
                    "value": row["lease_liability_change"]})
    answers.append({"label": "c: schedule %s - lease liability balance after payment" % lbl,
                    "value": row["lease_liability"]})
answers.append({"label": "c: schedule totals - lease payments", "value": total_payments})
answers.append({"label": "c: schedule totals - interest on liability", "value": total_interest})
answers.append({"label": "c: schedule totals - lease liability change", "value": lease_liability_0})

# (e)
answers.append({"label": "e: ROU asset carrying amount at 12/31/Year 1", "value": rou_end_y1})
answers.append({"label": "e: total lease liability at 12/31/Year 1", "value": liab_dec31_y1})
answers.append({"label": "e: current lease liability at 12/31/Year 1", "value": current_portion_y1})
answers.append({"label": "e: noncurrent lease liability at 12/31/Year 1",
                "value": noncurrent_portion_y1})

# (f) confirmation of zero balances
answers.append({"label": "f: lease liability balance after 1/1/Year 4 payment", "value": ZERO})
answers.append({"label": "f: ROU asset carrying amount at 12/31/Year 4", "value": rou_end_y4})

notes = (
    "(a) Finance lease: lease term 4 yrs = 100%% of the 4-yr economic life (>=75%%) "
    "and PV of payments = 100%% of the $320,000 fair value (>=90%%); discount at the "
    "5%% implicit rate because it is known to Northwind, so the 5.5%% IBR is not used. "
    "(b) %s "
    "(c) Year 4 accrues no interest - the 1/1/Year 4 payment retires the liability. "
    "Mechanical 5%% x $%s gives $%s of Year 3 interest; the schedule shows $%s so the "
    "Interest column foots to total interest of $%s ($%s cash paid less $%s "
    "recognized) and the final payment clears the liability to exactly $0 as part (f) "
    "requires - a $%s last-period rounding plug. (d)/(f) ROU amortized straight-line "
    "over the %d-year lease term ($%s/yr) because ownership does not transfer and "
    "there is no purchase option. (e) Current portion = the 1/1/Year 2 payment, which "
    "is entirely principal since no interest accrues between 12/31 and the next-day "
    "payment."
    % (
        measurement_note,
        plug_basis_balance,
        plug_mechanical,
        interest_by_year[-1],
        total_interest,
        total_payments,
        lease_liability_0,
        plug_amount,
        amort_years,
        annual_amortization,
    )
)

out = {
    "id": "agent_022#01",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per period "
        "(each year's interest rounded before it is added to the carrying amount); "
        "PV from the exact annuity-due formula (Excel =PV type=1), not a table "
        "factor; final interest period carries the amortization-table rounding plug "
        "so total interest = total payments less the recognized liability"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}


def _default(o):
    if isinstance(o, Decimal):
        return float(o)
    raise TypeError(repr(o))


print(json.dumps(out, indent=2, default=_default))
