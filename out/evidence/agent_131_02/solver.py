#!/usr/bin/env python3
"""Blind solver -- agent_131#02.

Q3 (CORE alternate angle): HarborPoint Retail Group, 2025.
Internal-use software (ASC 350-40) + cloud computing hosting arrangement
accounted for as a service contract (ASC 350-40-15-4A / 25-18 / 45-1..45-3).

ROUNDING CONVENTION
-------------------
All money is ``decimal.Decimal``; no binary floats are used anywhere.
Amortization is computed period by period and each period's amount is rounded
to the cent with ``ROUND_HALF_UP`` before it is posted (round-per-period, not
round-at-end).  The final period of each schedule is then set equal to the
remaining unamortized carrying amount so the asset closes to exactly zero at
the end of its amortization period (no rounding drift is carried into the
terminal balance).  Every figure in this fact pattern divides evenly, so the
plug never actually differs from the straight-line period amount here; the
mechanism is present so the script stays correct if the inputs change.
No present-value work is required by this item, so no PV table factors are
used.

Partial-year rule taken from the stem: HarborPoint records FULL-MONTH
amortization beginning in the month the internal-use software is ready for
its intended use (July 2025) -> 6 of 12 months in 2025.

Run: ``python3 solver.py``  -> prints one JSON object on stdout.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when the value is a whole dollar amount."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Facts from the stem (nothing below is an answer copied from anywhere)
# ---------------------------------------------------------------------------

# Part A -- internal-use software
PRELIMINARY_STAGE = Decimal("18000")        # needs assessment, vendor eval, tech selection
APPLICATION_DEVELOPMENT = Decimal("240000")  # coding, configuration, testing, installation
TRAINING = Decimal("12000")                  # during and after development
IUS_LIFE_YEARS = 4
IUS_RESIDUAL = Decimal("0")
IUS_READY_MONTH = 7                          # ready for intended use July 1, 2025
IUS_FIRST_YEAR = 2025
MONTHS_IN_YEAR = 12

# Part B -- cloud computing arrangement (hosting)
CLOUD_IMPLEMENTATION = Decimal("80000")      # paid Jan 1, 2025, development-stage costs
CLOUD_SUBSCRIPTION_ANNUAL = Decimal("96000")  # paid each December 31
CLOUD_TERM_YEARS = 4
CLOUD_START_YEAR = 2025
# Stem: no contractual right to take possession without significant penalty,
# and not feasible to run it on its own hardware -> ASC 350-40-15-4A criteria
# (a) and (b) both fail.
RIGHT_TO_TAKE_POSSESSION = False
FEASIBLE_TO_RUN_OWN_HARDWARE = False


# ---------------------------------------------------------------------------
# Part a -- internal-use software: capitalize only the application dev stage
# ---------------------------------------------------------------------------
# ASC 350-40-25-1: preliminary project stage costs expensed as incurred.
# ASC 350-40-25-2: application development stage costs capitalized.
# Training costs are expensed as incurred even if incurred during the
# application development stage.
ius_capitalized = money(APPLICATION_DEVELOPMENT)
ius_expensed_preliminary = money(PRELIMINARY_STAGE)
ius_expensed_training = money(TRAINING)


# ---------------------------------------------------------------------------
# Part b -- internal-use software amortization schedule
# ---------------------------------------------------------------------------
ius_amortizable_base = ius_capitalized - IUS_RESIDUAL
ius_full_year = money(ius_amortizable_base / Decimal(IUS_LIFE_YEARS))

# Months amortized in each calendar year, given a July 1, 2025 in-service date
# and full-month amortization starting in July.
total_months = IUS_LIFE_YEARS * MONTHS_IN_YEAR          # 48
months_2025 = MONTHS_IN_YEAR - (IUS_READY_MONTH - 1)     # 6 (Jul-Dec 2025)

ius_schedule = []
carrying = ius_capitalized
months_remaining = total_months
year = IUS_FIRST_YEAR
while months_remaining > 0:
    months_this_year = months_2025 if year == IUS_FIRST_YEAR else MONTHS_IN_YEAR
    months_this_year = min(months_this_year, months_remaining)
    beginning = carrying
    if months_this_year == months_remaining:
        # terminal period: plug to the remaining carrying amount net of residual
        amort = money(beginning - IUS_RESIDUAL)
    else:
        amort = money(
            ius_amortizable_base
            * Decimal(months_this_year)
            / Decimal(total_months)
        )
    carrying = money(beginning - amort)
    ius_schedule.append(
        {
            "year": year,
            "months": months_this_year,
            "beginning_carrying_amount": num(beginning),
            "amortization": num(amort),
            "ending_carrying_amount": num(carrying),
        }
    )
    months_remaining -= months_this_year
    year += 1

by_year = {row["year"]: row for row in ius_schedule}
ius_amort_2025 = Decimal(str(by_year[2025]["amortization"]))
ius_cv_2025 = Decimal(str(by_year[2025]["ending_carrying_amount"]))

# The Required asks for the schedule 2025-2028 ("full years after 2025").
ius_schedule_2025_2028 = [r for r in ius_schedule if 2025 <= r["year"] <= 2028]


# ---------------------------------------------------------------------------
# Part c -- service contract vs software purchase
# ---------------------------------------------------------------------------
is_software_purchase = RIGHT_TO_TAKE_POSSESSION and FEASIBLE_TO_RUN_OWN_HARDWARE
cloud_classification = "Software purchase (intangible asset)" if is_software_purchase \
    else "Service contract"
cloud_classification_reason = (
    "ASC 350-40-15-4A requires BOTH (a) a contractual right to take possession of "
    "the software at any time during the hosting period without significant penalty "
    "and (b) feasibility of running the software on the customer's own hardware or "
    "having an unrelated party host it. HarborPoint fails both: it has no right to "
    "take possession without significant penalty and cannot practically run the ERP "
    "module on its own hardware. Failing either criterion makes the arrangement a "
    "service contract, so no software intangible is recognized for the right to use "
    "the ERP module. Only the development-stage implementation/setup costs are "
    "capitalized (ASC 350-40-25-18) and amortized straight-line over the hosting "
    "term; the annual subscription fee is expensed."
)


# ---------------------------------------------------------------------------
# Parts d and e -- cloud implementation asset schedule
# ---------------------------------------------------------------------------
cloud_base = CLOUD_IMPLEMENTATION
cloud_schedule = []
cloud_carrying = cloud_base
for i in range(CLOUD_TERM_YEARS):
    yr = CLOUD_START_YEAR + i
    beginning = cloud_carrying
    if i == CLOUD_TERM_YEARS - 1:
        amort = money(beginning)  # terminal-year plug -> closes to zero
    else:
        amort = money(cloud_base / Decimal(CLOUD_TERM_YEARS))
    cloud_carrying = money(beginning - amort)
    cloud_schedule.append(
        {
            "year": yr,
            "beginning_book_value": num(beginning),
            "amortization": num(amort),
            "ending_book_value": num(cloud_carrying),
        }
    )

cloud_amort_2025 = Decimal(str(cloud_schedule[0]["amortization"]))
cloud_subscription_2025 = money(CLOUD_SUBSCRIPTION_ANNUAL)


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def je(part, description, lines):
    out = {"part": part, "description": description, "lines": []}
    for account, dr, cr in lines:
        out["lines"].append(
            {"account": account, "debit": num(dr), "credit": num(cr)}
        )
    return out


journal_entries = [
    je(
        "a(i)",
        "2025 - Preliminary project stage costs on internal-use software "
        "(expensed as incurred, ASC 350-40-25-1)",
        [
            ("Research and Development Expense (Preliminary Project Stage)",
             ius_expensed_preliminary, Decimal("0")),
            ("Cash", Decimal("0"), ius_expensed_preliminary),
        ],
    ),
    je(
        "a(ii)",
        "2025 - Application development stage costs on internal-use software "
        "(capitalized, ASC 350-40-25-2)",
        [
            ("Software Intangible Asset (Internal-Use Software)",
             ius_capitalized, Decimal("0")),
            ("Cash", Decimal("0"), ius_capitalized),
        ],
    ),
    je(
        "a(iii)",
        "2025 - Employee training costs (expensed as incurred even when "
        "incurred during the application development stage)",
        [
            ("Training Expense", ius_expensed_training, Decimal("0")),
            ("Cash", Decimal("0"), ius_expensed_training),
        ],
    ),
    je(
        "b",
        "December 31, 2025 - Amortize internal-use software, 6 months "
        "(July-December) of a 4-year straight-line life",
        [
            ("Software Amortization Expense", ius_amort_2025, Decimal("0")),
            ("Accumulated Amortization - Software Intangible Asset "
             "(Software Intangible Asset)", Decimal("0"), ius_amort_2025),
        ],
    ),
    je(
        "d(i)",
        "January 1, 2025 - Capitalize development-stage implementation/setup "
        "costs of the cloud hosting arrangement (ASC 350-40-25-18)",
        [
            ("Capitalized Cloud Computing Implementation Costs",
             CLOUD_IMPLEMENTATION, Decimal("0")),
            ("Cash", Decimal("0"), CLOUD_IMPLEMENTATION),
        ],
    ),
    je(
        "d(ii)",
        "December 31, 2025 - Pay annual cloud subscription (hosting) fee, "
        "expensed as incurred",
        [
            ("Cloud Subscription (Hosting) Expense",
             cloud_subscription_2025, Decimal("0")),
            ("Cash", Decimal("0"), cloud_subscription_2025),
        ],
    ),
    je(
        "d(iii)",
        "December 31, 2025 - Adjusting entry to amortize capitalized cloud "
        "implementation costs straight-line over the 4-year hosting term",
        [
            ("Cloud Subscription (Hosting) Expense - Amortization of "
             "Implementation Costs", cloud_amort_2025, Decimal("0")),
            ("Capitalized Cloud Computing Implementation Costs",
             Decimal("0"), cloud_amort_2025),
        ],
    ),
]

# Debits must equal credits in every entry.
for entry in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert dr == cr, f"JE {entry['part']} out of balance: {dr} vs {cr}"


# ---------------------------------------------------------------------------
# Part f -- classification / presentation of the cloud implementation costs
# ---------------------------------------------------------------------------
presentation_bs = (
    "Balance sheet (ASC 350-40-45-2): present the capitalized implementation "
    "costs in the SAME line item in which a prepayment of the hosting fees "
    "would be presented - i.e., as a prepaid expense / other asset, split "
    "current vs. noncurrent by the portion to be amortized within the next "
    "year (at 12/31/25: $20,000 current, $40,000 noncurrent). They are NOT "
    "reported as software or as an intangible asset, because the arrangement "
    "is a service contract."
)
presentation_is = (
    "Income statement (ASC 350-40-45-1): present amortization of the "
    "capitalized implementation costs in the SAME line item as the expense "
    "for the hosting/subscription fees - i.e., inside operating expenses with "
    "the subscription cost ($20,000 of amortization alongside the $96,000 "
    "subscription fee, $116,000 total for 2025). It is NOT presented with "
    "depreciation and amortization of long-lived assets."
)
presentation_cf = (
    "Statement of cash flows (ASC 350-40-45-3): classify the cash paid for "
    "the capitalized implementation costs in the SAME manner as the cash "
    "flows for the hosting fees - operating activities (an operating outflow "
    "of $80,000 on 1/1/25), not investing. The $96,000 subscription payment "
    "is likewise operating."
)


# ---------------------------------------------------------------------------
# Output -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {
        "label": "a: internal-use software amount initially capitalized",
        "value": num(ius_capitalized),
    },
    {
        "label": "b: 2025 amortization expense on internal-use software",
        "value": num(ius_amort_2025),
    },
    {
        "label": "b: December 31, 2025 carrying amount of internal-use software",
        "value": num(ius_cv_2025),
    },
    {
        "label": "b: internal-use software amortization schedule 2025-2028 "
                 "(year, beginning carrying amount, amortization, ending carrying amount)",
        "value": [
            [r["year"], r["beginning_carrying_amount"], r["amortization"],
             r["ending_carrying_amount"]]
            for r in ius_schedule_2025_2028
        ],
    },
    {
        "label": "c: classification of the cloud hosting arrangement",
        "value": cloud_classification,
    },
    {
        "label": "e: cloud implementation asset subsequent measurement schedule "
                 "(year, beginning BV, amortization, ending BV)",
        "value": [
            [r["year"], r["beginning_book_value"], r["amortization"],
             r["ending_book_value"]]
            for r in cloud_schedule
        ],
    },
    {
        "label": "f(i): balance sheet presentation of capitalized cloud "
                 "implementation costs",
        "value": presentation_bs,
    },
    {
        "label": "f(ii): income statement presentation of amortization of cloud "
                 "implementation costs",
        "value": presentation_is,
    },
    {
        "label": "f(iii): statement of cash flows classification of cloud "
                 "implementation cash flows",
        "value": presentation_cf,
    },
]

result = {
    "id": "agent_131#02",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats. ROUND_HALF_UP to the cent "
        "per period (round-per-period, not round-at-end); the terminal period "
        "of each amortization schedule is plugged to the remaining carrying "
        "amount so the asset closes to exactly zero. No PV factors needed. "
        "Internal-use software uses full-month amortization beginning July "
        "2025 (6/12 of a full year in 2025) per the stem."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Part a: only the $240,000 application development stage cost is "
        "capitalized (ASC 350-40-25-2); the $18,000 preliminary project stage "
        "cost and the $12,000 training cost are expensed as incurred, training "
        "even though some of it was incurred during the development stage. "
        "Part b: $240,000 / 4 years = $60,000 per full year; 2025 gets 6 months "
        "(July-December) = $30,000, leaving a 12/31/25 carrying amount of "
        "$210,000. The 2025-2028 schedule therefore runs 30,000 / 60,000 / "
        "60,000 / 60,000 with a 12/31/28 carrying amount of $30,000; the final "
        "$30,000 is amortized January-June 2029, when the 4-year life ends. "
        "Part c: " + cloud_classification_reason + " "
        "Parts d-e: the $80,000 implementation cost is capitalized and "
        "amortized $20,000 per year over the 4-year hosting term; the $96,000 "
        "subscription fee is expensed when incurred each December 31. "
        "Part f: presentation follows ASC 350-40-45-1 through 45-3 - the "
        "capitalized implementation costs and their amortization and cash "
        "flows all follow the hosting fee, not the intangible-asset lines."
    ),
}

print(json.dumps(result, indent=2))
