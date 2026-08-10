#!/usr/bin/env python3
"""
Solver for item agent_151#01 -- Q2 "Glacier Lab Analytics LLC" (LO 17-11):
finance-lease purchase-option reassessment, remeasurement, and subsequent
interest / schedule path.

--------------------------------------------------------------------------
ROUNDING CONVENTION
--------------------------------------------------------------------------
* All money is decimal.Decimal. No floats are used anywhere in the
  derivation; floats appear only in the final JSON serialization of values
  that are already exact to the cent.
* Discount factors are computed from the EXACT closed-form formula
  1 / (1 + i)**n at 28 significant digits of Decimal precision -- NOT from
  5-decimal printed table factors. (Table factors would shift the initial PV
  by $0.10 and leave a $0.04 plug at the end of the remeasured schedule; the
  exact-formula path retires the liability to exactly the $30,000 purchase
  option, which is the internal consistency check this fact pattern is built
  around.)
* Every MONEY amount -- present values, periodic interest, carrying amounts,
  amortization -- is rounded to the cent with ROUND_HALF_UP, PER PERIOD, as
  it is recorded. Interest for a period is computed on the already-rounded
  opening balance of that period and is itself rounded before it is added,
  so the amortization schedule is self-consistent line by line rather than
  rounded once at the end.
* No end-of-schedule plug is applied. The final balance falls out of the
  arithmetic.

--------------------------------------------------------------------------
FACT PATTERN (from the stem only)
--------------------------------------------------------------------------
Commencement Jan 1, Year 1. Economic life 6 years; lease term 5 years.
Payment $80,000 annually IN ADVANCE (Jan 1 of Years 1-5). Purchase option
of $30,000 exercisable at the END of Year 5 (Dec 31, Y5) -- NOT reasonably
certain at commencement, so it is excluded from the initial measurement.
Lessee IBR at commencement 7%. Finance lease.

Jan 1, Year 3, BEFORE the Year 3 payment: exercise becomes reasonably
certain. Classification stays finance. Original 7% did not reflect the PO,
so the discount rate is updated to the current IBR of 5%. Remaining cash
flows at that date: the Jan 1 Y3, Jan 1 Y4 and Jan 1 Y5 payments of $80,000
(an annuity due of 3) plus the $30,000 option price 3 periods out
(Dec 31, Y5).

Because exercise is reasonably certain, the ROU asset is amortized after
remeasurement over the REMAINING ECONOMIC LIFE: 6 - 2 = 4 years.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28

CENT = Decimal("0.01")
ZERO = Decimal("0")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def pv_single(rate: Decimal, n: int) -> Decimal:
    """Exact PV factor of 1 due n periods hence."""
    return Decimal(1) / ((Decimal(1) + rate) ** n)


def pv_annuity_due(rate: Decimal, n: int) -> Decimal:
    """Exact PV factor of an n-payment annuity DUE (first payment at t=0)."""
    return sum((pv_single(rate, t) for t in range(n)), Decimal(0))


# ---------------------------------------------------------------- inputs ---
PMT = Decimal("80000")
OPTION = Decimal("30000")
TERM = 5                       # lease term, years
ECON_LIFE = 6                  # economic life, years
R0 = Decimal("0.07")           # IBR at commencement
R1 = Decimal("0.05")           # current IBR at reassessment
ELAPSED = 2                    # full years elapsed before Jan 1, Y3

# ------------------------------------------------ (a) initial measurement ---
# PO not reasonably certain at commencement -> excluded. 5 payments in advance.
initial_pv = money(PMT * pv_annuity_due(R0, TERM))

je_commencement = [
    {"account": "Right-of-Use Asset", "debit": initial_pv, "credit": ZERO},
    {"account": "Lease Liability", "debit": ZERO, "credit": initial_pv},
]
je_first_payment = [
    {"account": "Lease Liability", "debit": PMT, "credit": ZERO},
    {"account": "Cash", "debit": ZERO, "credit": PMT},
]

# ------------------------------- (b) roll forward at 7% to Jan 1, Year 3 ---
# Annuity due: pay first, then accrue interest on the reduced balance.
bal = initial_pv
pre_schedule = []
for year in range(1, ELAPSED + 1):
    opening = bal
    after_pmt = opening - PMT                      # payment on Jan 1 of `year`
    interest = money(after_pmt * R0)               # accrued Dec 31 of `year`
    bal = after_pmt + interest
    pre_schedule.append(
        {
            "year": year,
            "opening_jan1": opening,
            "payment_jan1": PMT,
            "balance_after_payment": after_pmt,
            "interest_dec31": interest,
            "closing_dec31": bal,
        }
    )

liab_before_remeasurement = bal                    # Jan 1, Y3 pre-payment

# ROU asset: straight line over the 5-year lease term (PO not yet certain).
rou_amort_original = money(initial_pv / Decimal(TERM))
rou_ca_before = initial_pv - rou_amort_original * ELAPSED

# --------------------------------------- (c) remeasurement at 5%, Jan 1 Y3 ---
remaining_payments = TERM - ELAPSED                # Jan 1 of Y3, Y4, Y5 -> 3
periods_to_option = remaining_payments             # Dec 31, Y5 is 3 periods out

pv_remaining_pmts = money(PMT * pv_annuity_due(R1, remaining_payments))
pv_option = money(OPTION * pv_single(R1, periods_to_option))
liab_remeasured = pv_remaining_pmts + pv_option

remeasurement_adj = liab_remeasured - liab_before_remeasurement
je_remeasurement = [
    {"account": "Right-of-Use Asset", "debit": remeasurement_adj, "credit": ZERO},
    {"account": "Lease Liability", "debit": ZERO, "credit": remeasurement_adj},
]
rou_ca_after = rou_ca_before + remeasurement_adj

# ------------------------- (d) Jan 1 Y3 payment + post-remeasurement schedule ---
je_y3_payment = [
    {"account": "Lease Liability", "debit": PMT, "credit": ZERO},
    {"account": "Cash", "debit": ZERO, "credit": PMT},
]

bal = liab_remeasured
post_schedule = []
# Years 3, 4, 5: payment each Jan 1, interest each Dec 31.
for year in range(ELAPSED + 1, TERM + 1):
    opening = bal
    after_pmt = opening - PMT
    interest = money(after_pmt * R1)
    bal = after_pmt + interest
    post_schedule.append(
        {
            "date_payment": "Jan 1, Year %d" % year,
            "opening_before_payment": opening,
            "payment": PMT,
            "balance_after_payment": after_pmt,
            "interest_dec31": interest,
            "closing_dec31": bal,
        }
    )
# Dec 31, Year 5: exercise the purchase option, retiring the liability.
balance_before_option = bal
post_schedule.append(
    {
        "date_payment": "Dec 31, Year 5 (exercise purchase option)",
        "opening_before_payment": balance_before_option,
        "payment": OPTION,
        "balance_after_payment": balance_before_option - OPTION,
        "interest_dec31": ZERO,
        "closing_dec31": balance_before_option - OPTION,
    }
)

interest_y3 = post_schedule[0]["interest_dec31"]
je_interest_y3 = [
    {"account": "Interest Expense", "debit": interest_y3, "credit": ZERO},
    {"account": "Lease Liability", "debit": ZERO, "credit": interest_y3},
]

# ------------------------------ (e) ROU amortization after remeasurement ---
remaining_econ_life = ECON_LIFE - ELAPSED          # 4 years
rou_amort_after = money(rou_ca_after / Decimal(remaining_econ_life))

# ------------------------------------------------------- integrity checks ---
assert post_schedule[-1]["closing_dec31"] == ZERO, (
    "liability did not retire to zero at the purchase option: %s"
    % post_schedule[-1]["closing_dec31"]
)
for entry in (je_commencement, je_first_payment, je_remeasurement,
              je_y3_payment, je_interest_y3):
    dr = sum((ln["debit"] for ln in entry), Decimal(0))
    cr = sum((ln["credit"] for ln in entry), Decimal(0))
    assert dr == cr, "entry out of balance: %s vs %s" % (dr, cr)

# --------------------------------------------------------------- output ---
answers = [
    {"label": "a: initial lease liability = ROU asset (PV of 5 payments in advance at 7%, PO excluded)",
     "value": initial_pv},
    {"label": "a: first lease payment applied to liability, Jan 1 Year 1",
     "value": PMT},
    {"label": "b: lease liability Jan 1 Year 3 before remeasurement and before payment",
     "value": liab_before_remeasurement},
    {"label": "b: ROU asset carrying amount Jan 1 Year 3 (2 years SL over 5-year term)",
     "value": rou_ca_before},
    {"label": "c: remeasured lease liability at 5% (Jan 1 Year 3, before payment)",
     "value": liab_remeasured},
    {"label": "c: remeasurement adjustment (increase to liability and ROU asset)",
     "value": remeasurement_adj},
    {"label": "c: post-remeasurement lease liability (before Jan 1 Year 3 payment)",
     "value": liab_remeasured},
    {"label": "c: post-remeasurement ROU asset carrying amount",
     "value": rou_ca_after},
    {"label": "d: lease liability after the Jan 1 Year 3 payment",
     "value": post_schedule[0]["balance_after_payment"]},
    {"label": "d: schedule - interest Dec 31 Year 3",
     "value": post_schedule[0]["interest_dec31"]},
    {"label": "d: schedule - liability Dec 31 Year 3",
     "value": post_schedule[0]["closing_dec31"]},
    {"label": "d: schedule - liability after Jan 1 Year 4 payment",
     "value": post_schedule[1]["balance_after_payment"]},
    {"label": "d: schedule - interest Dec 31 Year 4",
     "value": post_schedule[1]["interest_dec31"]},
    {"label": "d: schedule - liability Dec 31 Year 4",
     "value": post_schedule[1]["closing_dec31"]},
    {"label": "d: schedule - liability after Jan 1 Year 5 payment",
     "value": post_schedule[2]["balance_after_payment"]},
    {"label": "d: schedule - interest Dec 31 Year 5",
     "value": post_schedule[2]["interest_dec31"]},
    {"label": "d: schedule - liability Dec 31 Year 5 before exercising the option",
     "value": post_schedule[2]["closing_dec31"]},
    {"label": "d: schedule - liability after paying the $30,000 purchase option",
     "value": post_schedule[3]["closing_dec31"]},
    {"label": "e: annual ROU amortization after remeasurement (4 years of remaining economic life)",
     "value": rou_amort_after},
]

journal_entries = [
    {"part": "a", "date": "Jan 1, Year 1",
     "description": "Recognize finance lease ROU asset and lease liability at commencement",
     "lines": je_commencement},
    {"part": "a", "date": "Jan 1, Year 1",
     "description": "First annual payment, made in advance",
     "lines": je_first_payment},
    {"part": "c", "date": "Jan 1, Year 3",
     "description": "Remeasure lease liability at the updated 5% rate for the reasonably certain purchase option",
     "lines": je_remeasurement},
    {"part": "d", "date": "Jan 1, Year 3",
     "description": "Third annual payment, made in advance after remeasurement",
     "lines": je_y3_payment},
    {"part": "d", "date": "Dec 31, Year 3",
     "description": "Accrue interest on the remeasured lease liability at 5%",
     "lines": je_interest_y3},
]


def plain(obj):
    """Serialize Decimals as JSON numbers; every one is already cent-exact."""
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, dict):
        return {k: plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [plain(v) for v in obj]
    return obj


result = {
    "id": "agent_151#01",
    "rounding_convention": (
        "ROUND_HALF_UP to the cent, applied per period as amounts are recorded; "
        "discount factors from the exact formula 1/(1+i)^n at 28-digit Decimal "
        "precision rather than 5-decimal table factors; no end-of-schedule plug"
    ),
    "answers": plain(answers),
    "journal_entries": plain(journal_entries),
    "insufficient_info": False,
    "notes": (
        "Purchase option is excluded at commencement (not reasonably certain), so "
        "initial PV is the 5-payment annuity due at 7%. At Jan 1 Year 3 the option "
        "becomes reasonably certain and the rate is updated to 5%, so the remeasured "
        "liability is the 3-payment annuity due of $80,000 at 5% plus the $30,000 "
        "option discounted 3 periods to Dec 31 Year 5; the whole adjustment goes to "
        "the ROU asset. Because exercise is reasonably certain, post-remeasurement "
        "amortization runs over the remaining economic life (6 - 2 = 4 years) rather "
        "than the lease term. The schedule retires the liability to exactly $30,000 "
        "at Dec 31 Year 5 with no plug."
    ),
}

print(json.dumps(result, indent=2))
