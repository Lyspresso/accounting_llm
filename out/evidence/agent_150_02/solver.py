#!/usr/bin/env python3
"""Solver for item agent_150#02 — Redrock Analytics LLC, ASC 842 lease
identification, classification (Options 1-4), and expense presentation.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no floats appear anywhere in this module.

* Discount factors are computed from the EXACT closed-form formulas
  (1+i)^-n and [1 - (1+i)^-n] / i at 50 significant digits of working
  precision, matching the Excel PV() results the textbook uses in its
  Chapter 17 demonstrations. Factors are NOT pre-rounded to 5-place table
  values before being multiplied by the payment.
* Each reported present value is rounded ONCE, at the end, to the nearest
  cent using ROUND_HALF_UP (the course convention). There are no
  intermediate per-period roundings in this item because nothing is
  amortized here — only single present-value measurements are required.
* Classification thresholds are compared on the UNROUNDED present values;
  rounding to cents cannot flip any of the four conclusions here (the
  nearest test result is 88.28% vs. the 90% threshold).
* For reference, using 5-decimal-place printed table factors instead of the
  exact formula moves each present value by less than $0.25 and changes no
  conclusion.

AUTHORITY (textbook Ch. 17, ASC 842)
------------------------------------
Identified asset / lease existence: ASC 842-10-15-4, -15-9, -15-10. A
supplier's substitution right defeats the "right to direct the use"
criterion when the supplier has the practical ability to substitute AND
benefits economically from doing so.

Five classification criteria (ASC 842-10-25-2): (1) ownership transfer,
(2) purchase option reasonably certain to be exercised, (3) lease term is a
major part of remaining economic life (75% test), (4) PV of lease payments
equals or exceeds substantially all of fair value (90% test), (5) no
alternative use. Meeting ANY ONE makes it a finance lease; meeting NONE
makes it operating.

Discount rate (ASC 842-20-30-3): rate implicit in the lease if readily
determinable, otherwise the lessee's incremental borrowing rate.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 50

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to the nearest cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def as_num(x: Decimal):
    """JSON-friendly number: int when whole cents land on a whole dollar."""
    q = money(x)
    return int(q) if q == q.to_integral_value() else float(q)


def compound(rate: Decimal, n: int) -> Decimal:
    """(1 + rate) ** n by exact repeated multiplication (integer n >= 0)."""
    factor = Decimal(1)
    base = Decimal(1) + rate
    for _ in range(n):
        factor *= base
    return factor


def pv_single(rate: Decimal, n: int) -> Decimal:
    """PV of $1 received n periods hence."""
    return Decimal(1) / compound(rate, n)


def pvifa_ordinary(rate: Decimal, n: int) -> Decimal:
    """PV of an ordinary annuity of $1 for n periods (payments at period end)."""
    return (Decimal(1) - pv_single(rate, n)) / rate


def pvifa_due(rate: Decimal, n: int) -> Decimal:
    """PV of an annuity due of $1 for n periods (payments at period start)."""
    return pvifa_ordinary(rate, n) * (Decimal(1) + rate)


# ---------------------------------------------------------------------------
# Facts given in the stem
# ---------------------------------------------------------------------------
FAIR_VALUE = Decimal("250000")          # FV of the equipment class
ECONOMIC_LIFE = Decimal("10")           # years of remaining economic life
TERM_THRESHOLD = Decimal("0.75")        # "major part" test, per the stem
PV_THRESHOLD = Decimal("0.90")          # "substantially all" test, per the stem

PV_HURDLE = FAIR_VALUE * PV_THRESHOLD               # 90% x 250,000 = 225,000
TERM_HURDLE = ECONOMIC_LIFE * TERM_THRESHOLD        # 75% x 10 = 7.5 years


# ---------------------------------------------------------------------------
# Case A — is there a lease?
# ---------------------------------------------------------------------------
# CloudRail may fulfil from ANY of a large pool of identical servers, does so
# routinely for its own cost savings, and Redrock cannot prevent substitution.
# Both prongs of ASC 842-10-15-10 are satisfied, so the substitution right is
# SUBSTANTIVE -> there is no identified asset and Redrock cannot direct the use
# of one. Redrock buys capacity (an output), not a machine.
case_a_practical_ability = True     # Redrock cannot prevent substitution
case_a_economic_benefit = True      # CloudRail reallocates for its own savings
case_a_substantive_substitution = case_a_practical_ability and case_a_economic_benefit
case_a_is_lease = not case_a_substantive_substitution   # -> False
case_a_conclusion = "Lease" if case_a_is_lease else "No lease - service contract"


# ---------------------------------------------------------------------------
# Case B — classify each of the four options
# ---------------------------------------------------------------------------
def classify(term_years, pv_of_payments, ownership_transfer,
             purchase_option_certain, no_alternative_use):
    """Apply the five ASC 842-10-25-2 criteria; any one met => finance."""
    term_met = Decimal(term_years) >= TERM_HURDLE
    pv_met = pv_of_payments >= PV_HURDLE
    met = (ownership_transfer or purchase_option_certain or term_met
           or pv_met or no_alternative_use)
    return ("Finance" if met else "Operating"), term_met, pv_met


results = {}

# --- Option 1: 6 years, $40,000 ordinary annuity, IBR 6% (implicit unknown) --
o1_rate, o1_n, o1_pmt = Decimal("0.06"), 6, Decimal("40000")
o1_pv = o1_pmt * pvifa_ordinary(o1_rate, o1_n)
results["1"] = classify(6, o1_pv, False, False, False) + (o1_pv,)

# --- Option 2: 8 years, $40,000 ordinary annuity, IBR 6% ---------------------
o2_rate, o2_n, o2_pmt = Decimal("0.06"), 8, Decimal("40000")
o2_pv = o2_pmt * pvifa_ordinary(o2_rate, o2_n)
results["2"] = classify(8, o2_pv, False, False, False) + (o2_pv,)

# --- Option 3: 6 years, $42,000 ordinary annuity + $15,000 purchase option,
#     implicit rate 5.5% KNOWN (so it, not the IBR, is the discount rate).
#     Option price $15,000 vs. expected FV $55,000 and Redrock is reasonably
#     certain to exercise, so the exercise price is a lease payment. ----------
o3_rate, o3_n, o3_pmt = Decimal("0.055"), 6, Decimal("42000")
o3_option_price = Decimal("15000")
o3_pv = (o3_pmt * pvifa_ordinary(o3_rate, o3_n)
         + o3_option_price * pv_single(o3_rate, o3_n))
results["3"] = classify(6, o3_pv, False, True, False) + (o3_pv,)

# --- Option 4: 6 years, $45,000 annuity DUE (beginning of year), IBR 6% ------
o4_rate, o4_n, o4_pmt = Decimal("0.06"), 6, Decimal("45000")
o4_pv = o4_pmt * pvifa_due(o4_rate, o4_n)
results["4"] = classify(6, o4_pv, False, False, False) + (o4_pv,)


# ---------------------------------------------------------------------------
# Case C — Year 1 income statement presentation (qualitative)
# ---------------------------------------------------------------------------
case_c = (
    "Finance lease (Option 2): TWO expenses appear, reported separately - "
    "straight-line amortization expense on the right-of-use asset (an "
    "operating expense) plus interest expense on the lease liability computed "
    "by the effective-interest method (a non-operating/financing item). "
    "Because the liability balance is largest in Year 1, interest is largest "
    "in Year 1, so total Year 1 lease-related expense is front-loaded and "
    "declines over the term. "
    "Operating lease (the short warehouse lease, meeting none of the five "
    "criteria): ONE expense appears - a single straight-line lease expense "
    "(ASC 842-20-25-6), presented entirely within operating expenses with no "
    "separate interest line, and the same amount is recognized every year. "
    "Over the full term both leases expense the same total; only the timing "
    "and the number of income statement line items differ, so Year 1 expense "
    "is higher, and operating income and EBITDA presentation differ, under "
    "the finance lease."
)


# ---------------------------------------------------------------------------
# Output — only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: Case A - does the contract contain a lease?",
     "value": case_a_conclusion},

    {"label": "b: Option 1 - PV of lease payments (6 yrs, $40,000 ordinary annuity @ 6% IBR)",
     "value": as_num(results["1"][3])},
    {"label": "b: Option 1 - classification", "value": results["1"][0]},

    {"label": "b: Option 2 - PV of lease payments (8 yrs, $40,000 ordinary annuity @ 6% IBR)",
     "value": as_num(results["2"][3])},
    {"label": "b: Option 2 - classification", "value": results["2"][0]},

    {"label": "b: Option 3 - PV of lease payments incl. purchase option (6 yrs, $42,000 ordinary annuity + $15,000 option @ 5.5% implicit)",
     "value": as_num(results["3"][3])},
    {"label": "b: Option 3 - classification", "value": results["3"][0]},

    {"label": "b: Option 4 - PV of lease payments (6 yrs, $45,000 annuity due @ 6% IBR)",
     "value": as_num(results["4"][3])},
    {"label": "b: Option 4 - classification", "value": results["4"][0]},

    {"label": "c: Case C - finance vs operating lessee expense presentation, Year 1",
     "value": case_c},
]

notes = (
    "Case A: CloudRail's substitution right is substantive under ASC "
    "842-10-15-10 - it can substitute from a large pool of identical servers "
    "(Redrock cannot prevent it) and it benefits economically by reallocating "
    "for its own cost savings. There is therefore no identified asset and "
    "Redrock cannot direct the use of one; Redrock buys processing capacity, "
    "an output, so the contract is a service contract, not a lease. "
    "Case B thresholds: 75% x 10-year economic life = 7.5 years; 90% x "
    "$250,000 fair value = $225,000. Option 1 meets no criterion (6 yrs = 60% "
    "of life; PV below $225,000) so it is operating. Option 2 meets the term "
    "criterion (8 yrs = 80% of life) and its PV also exceeds $225,000. "
    "Option 3 is finance solely on the purchase-option criterion ($15,000 "
    "exercise price vs. $55,000 expected fair value, reasonably certain to "
    "exercise); its term (60%) and PV (88.3% of fair value) both fail, which "
    "is why the PV is shown. Option 3 discounts at the known 5.5% implicit "
    "rate rather than the IBR, and includes the $15,000 option price as a "
    "lease payment. Option 4 is finance solely on the PV criterion - payments "
    "at the BEGINNING of each year make it an annuity due, and the PV reaches "
    "93.8% of fair value; discounted as an ordinary annuity it would have "
    "failed, so the timing of payment is the deciding fact. No option "
    "transfers ownership and none involves a specialized asset with no "
    "alternative use. No journal entries were required by any part."
)

output = {
    "id": "agent_150#02",
    "rounding_convention": (
        "decimal.Decimal throughout; exact closed-form PV factors at 50-digit "
        "working precision (Excel PV() equivalent, not 5-place table factors); "
        "each present value rounded once at the end to the nearest cent with "
        "ROUND_HALF_UP; classification tests applied to unrounded present values"
    ),
    "answers": answers,
    "journal_entries": [],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
