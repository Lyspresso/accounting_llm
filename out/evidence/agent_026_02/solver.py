#!/usr/bin/env python3
"""Blind solver for item agent_026#02 (Lakeview Medical Devices LLC).

Topic: book-tax differences (LO 18-1) -- classification grid, a taxable
temporary difference origination/reversal schedule driven by accelerated tax
depreciation, the Year 1 / Year 4 income tax journal entries, and a warranty
settlement entry.

ROUNDING CONVENTION
-------------------
All money is ``decimal.Decimal``; floats are never used.

    * Quantization: 2 decimal places (cents), ``ROUND_HALF_UP``.
    * Round-per-period, not round-at-end: every per-year figure (tax
      depreciation difference, cumulative temporary difference, ending DTL,
      taxable income, tax payable, tax expense) is quantized to cents at the
      moment it is computed, and the quantized figure is what feeds the next
      step and the journal entries.  This is the convention the course uses.
    * No present-value work is required by this fact pattern, so no PV table
      factors are involved.
    * Every figure in this fact pattern happens to land on a whole dollar, so
      the rounding rule is stated for reproducibility rather than because it
      changes a result.

DERIVATION NOTES
----------------
Part A is a qualitative classification, so it is derived from an explicit
rule engine rather than typed in: each item is described only by its economic
facts (is the difference in a revenue or an expense item, which system --
books or tax -- recognizes it first, and does it ever reverse), and
``classify()`` maps those facts onto the five permitted labels.

Part B is computed from the stem's raw inputs (cost, GAAP life, the four tax
depreciation amounts, the four pretax GAAP income amounts, and the 25% enacted
rate).  Nothing in the schedule is hard-coded.

Part C reverses a deductible temporary difference: paying a warranty claim
settles the GAAP liability whose tax basis is zero, so the deductible
temporary difference and the related DTA both shrink.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def m(x: str | int | Decimal) -> Decimal:
    """Build a money Decimal, quantized to cents with ROUND_HALF_UP."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def out(d: Decimal) -> float | int:
    """JSON-friendly rendering: exact int when whole, else 2dp float."""
    d = d.quantize(CENTS, rounding=ROUND_HALF_UP)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem, nothing else)
# ---------------------------------------------------------------------------
TAX_RATE = Decimal("0.25")            # enacted rate

EQUIP_COST = m(80_000)                # placed in service 1/1/Yr1, no salvage
GAAP_LIFE_YEARS = 4                   # straight-line
TAX_DEPRECIATION = [m(32_000), m(24_000), m(16_000), m(8_000)]   # Y1..Y4
PRETAX_GAAP_INCOME = [m(200_000), m(210_000), m(210_000), m(205_000)]

WARRANTY_LIAB_BEGIN = m(18_000)       # tax basis $0
WARRANTY_CASH_PAID = m(7_000)         # during Year 2, no new warranty expense


# ---------------------------------------------------------------------------
# Part A -- classification grid, derived from facts by rule
# ---------------------------------------------------------------------------
# Each item is described by:
#   nature : "revenue" | "expense" | "none"   (what the difference sits in)
#   first  : "book" | "tax" | None            (which system recognizes it first)
#   reverses : bool                           (does it ever turn around?)
#
# Rule engine:
#   never reverses + revenue  -> permanent (nontaxable)
#   never reverses + expense  -> permanent (nondeductible)
#   reverses + revenue in books first -> book income now, tax later
#                                     -> future taxable amount -> TAXABLE temp
#   reverses + revenue taxed first    -> tax now, book later
#                                     -> future deductible amount -> DEDUCTIBLE temp
#   reverses + expense deducted for tax first -> future taxable amount
#                                     -> TAXABLE temp
#   reverses + expense booked for GAAP first  -> future deductible amount
#                                     -> DEDUCTIBLE temp
#   nature "none" -> no book-tax difference

ITEMS = [
    (1, "Installment sale receivable recognized in full for GAAP; taxed as cash is collected",
     "revenue", "book", True,
     "Originates when GAAP records the full gross profit; reverses as cash is "
     "collected and the tax return picks the income up -> future taxable amounts."),
    (2, "Customer advances deferred for GAAP; taxed when cash is received",
     "revenue", "tax", True,
     "Originates when the cash is taxed ahead of the book revenue; reverses when "
     "GAAP later earns the revenue with no further tax -> future deductible amounts."),
    (3, "Straight-line depreciation for GAAP; MACRS (higher early years) for tax",
     "expense", "tax", True,
     "Originates while the tax deduction exceeds book depreciation; reverses in "
     "the later years when book depreciation exceeds tax -> future taxable amounts."),
    (4, "Life insurance proceeds received on officer's death (GAAP gain)",
     "revenue", None, False,
     "Book gain is excluded from taxable income permanently -- never reverses."),
    (5, "Premiums on officer life insurance (company is beneficiary) - GAAP expense",
     "expense", None, False,
     "Book expense is never deductible on the return -- never reverses."),
    (6, "Unrealized holding gain on equity securities (FV-NI) for GAAP; tax at sale",
     "revenue", "book", True,
     "Originates when GAAP marks the security up; reverses on sale when the gain "
     "enters taxable income -> future taxable amounts."),
    (7, "Estimated environmental remediation accrued for GAAP; deductible when paid",
     "expense", "book", True,
     "Originates when GAAP accrues the estimated liability; reverses when the "
     "cash is paid and the deduction is taken -> future deductible amounts."),
    (8, "Interest expense on loan used to carry municipal bonds (tax rules disallow)",
     "expense", None, False,
     "Book interest expense is permanently disallowed on the return -- never reverses."),
    (9, "Percentage-of-completion revenue for GAAP equals completed-contract tax "
        "revenue this year (same amount)",
     "none", None, False,
     "Book and tax revenue are the same amount this year, so there is nothing to "
     "originate or reverse."),
    (10, "Inventory written down to NRV for GAAP; loss not deductible for tax until sold",
     "expense", "book", True,
     "Originates when GAAP books the write-down; reverses when the inventory is "
     "sold and the loss becomes deductible -> future deductible amounts."),
]


def classify(nature: str, first: str | None, reverses: bool) -> str:
    if nature == "none":
        return "no book-tax difference"
    if not reverses:
        return "permanent (nontaxable)" if nature == "revenue" else "permanent (nondeductible)"
    if nature == "revenue":
        # book income first -> taxed later -> future taxable amount
        return "taxable temporary" if first == "book" else "deductible temporary"
    # expense: whichever system takes the deduction/expense first
    #   tax first  -> books will expense later with no deduction -> future taxable
    #   book first -> tax deduction comes later -> future deductible
    return "taxable temporary" if first == "tax" else "deductible temporary"


part_a = []
for num, desc, nature, first, reverses, why in ITEMS:
    part_a.append({
        "item": num,
        "description": desc,
        "classification": classify(nature, first, reverses),
        "justification": why,
    })


# ---------------------------------------------------------------------------
# Part B(a) -- depreciation schedule
# ---------------------------------------------------------------------------
gaap_dep_annual = m(EQUIP_COST / Decimal(GAAP_LIFE_YEARS))     # $20,000 per year

# Guard: the tax table must fully depreciate the same cost.
assert sum(TAX_DEPRECIATION, Decimal("0")) == EQUIP_COST, "tax depreciation must total cost"
assert gaap_dep_annual * GAAP_LIFE_YEARS == EQUIP_COST, "GAAP depreciation must total cost"

schedule = []
cumulative_ttd = m(0)
prior_dtl = m(0)                       # beginning deferred taxes are $0

for i in range(GAAP_LIFE_YEARS):
    year = i + 1
    tax_dep = TAX_DEPRECIATION[i]
    gaap_dep = gaap_dep_annual

    # Tax deduction in excess of book expense originates a TAXABLE temp diff;
    # the excess of book over tax reverses it.
    origin_reversal = m(tax_dep - gaap_dep)
    cumulative_ttd = m(cumulative_ttd + origin_reversal)
    ending_dtl = m(cumulative_ttd * TAX_RATE)

    # Part B(b)
    pretax = PRETAX_GAAP_INCOME[i]
    taxable_income = m(pretax - origin_reversal)
    tax_payable = m(taxable_income * TAX_RATE)

    # Supporting (not reported): expense and the DTL movement for the JEs.
    tax_expense = m(pretax * TAX_RATE)
    dtl_change = m(ending_dtl - prior_dtl)
    assert m(tax_payable + dtl_change) == tax_expense, f"Year {year} tax entry must balance"

    schedule.append({
        "year": year,
        "tax_depreciation": tax_dep,
        "gaap_depreciation": gaap_dep,
        "origin_reversal": origin_reversal,
        "cumulative_ttd": cumulative_ttd,
        "ending_dtl": ending_dtl,
        "taxable_income": taxable_income,
        "tax_payable": tax_payable,
        "tax_expense": tax_expense,
        "dtl_change": dtl_change,
    })
    prior_dtl = ending_dtl

assert schedule[-1]["cumulative_ttd"] == m(0), "temp difference must fully reverse by Year 4"


# ---------------------------------------------------------------------------
# Part B(c) -- income tax journal entries, Year 1 and Year 4 only
# ---------------------------------------------------------------------------
def income_tax_entry(part_label: str, row: dict) -> dict:
    lines = [{"account": "Income Tax Expense",
              "debit": out(row["tax_expense"]), "credit": 0}]
    if row["dtl_change"] > 0:
        lines.append({"account": "Deferred Tax Liability",
                      "debit": 0, "credit": out(row["dtl_change"])})
    elif row["dtl_change"] < 0:
        lines.append({"account": "Deferred Tax Liability",
                      "debit": out(-row["dtl_change"]), "credit": 0})
    lines.append({"account": "Income Tax Payable",
                  "debit": 0, "credit": out(row["tax_payable"])})
    return {"part": part_label, "lines": lines}


journal_entries = [
    income_tax_entry("B(c) Year 1", schedule[0]),
    income_tax_entry("B(c) Year 4", schedule[3]),
]


# ---------------------------------------------------------------------------
# Part C -- warranty settlement
# ---------------------------------------------------------------------------
# Paying a warranty claim with no new accrual debits the liability and credits
# cash.  The liability's tax basis is $0, so the book liability balance IS the
# deductible temporary difference; paying cash makes the deduction real for tax
# and therefore reverses that much of the difference.
warranty_liab_end = m(WARRANTY_LIAB_BEGIN - WARRANTY_CASH_PAID)
dtd_begin = m(WARRANTY_LIAB_BEGIN - Decimal(0))      # book basis less $0 tax basis
dtd_end = m(warranty_liab_end - Decimal(0))
dtd_decrease = m(dtd_begin - dtd_end)
dta_begin = m(dtd_begin * TAX_RATE)
dta_end = m(dtd_end * TAX_RATE)
dta_decrease = m(dta_begin - dta_end)

journal_entries.append({
    "part": "C settlement entry (Year 2)",
    "lines": [
        {"account": "Accrued Warranty Liability",
         "debit": out(WARRANTY_CASH_PAID), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": out(WARRANTY_CASH_PAID)},
    ],
})

# Every entry must balance.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"{je['part']} does not balance: {dr} vs {cr}"


# ---------------------------------------------------------------------------
# Assemble the answers -- only what the Required parts ask for
# ---------------------------------------------------------------------------
answers = []

# Part A: the classification of each of the ten items.
for row in part_a:
    answers.append({
        "label": f"A: item {row['item']} classification",
        "value": row["classification"],
    })

# Part B(a): annual origin/(reversal), ending cumulative taxable temporary
# difference, and ending DTL for each year.
for row in schedule:
    y = row["year"]
    answers.append({"label": f"B(a) Y{y}: origin/(reversal) of taxable temporary difference",
                    "value": out(row["origin_reversal"])})
for row in schedule:
    y = row["year"]
    answers.append({"label": f"B(a) Y{y}: ending cumulative taxable temporary difference",
                    "value": out(row["cumulative_ttd"])})
for row in schedule:
    y = row["year"]
    answers.append({"label": f"B(a) Y{y}: ending deferred tax liability",
                    "value": out(row["ending_dtl"])})

# Part B(b): taxable income and income tax payable each year.
for row in schedule:
    y = row["year"]
    answers.append({"label": f"B(b) Y{y}: taxable income", "value": out(row["taxable_income"])})
for row in schedule:
    y = row["year"]
    answers.append({"label": f"B(b) Y{y}: income tax payable", "value": out(row["tax_payable"])})

# Part C: stated effect on the deductible temporary difference and the DTA.
answers.append({"label": "C: decrease in deductible temporary difference",
                "value": out(dtd_decrease)})
answers.append({"label": "C: ending deductible temporary difference",
                "value": out(dtd_end)})
answers.append({"label": "C: decrease in deferred tax asset",
                "value": out(dta_decrease)})
answers.append({"label": "C: ending deferred tax asset", "value": out(dta_end)})

result = {
    "id": "agent_026#02",
    "rounding_convention": (
        "decimal.Decimal only; quantized to cents with ROUND_HALF_UP, "
        "round-per-period (each year's figure is rounded as computed and the "
        "rounded figure carries forward); no present-value factors needed"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Part A justifications: "
        + "; ".join(f"({r['item']}) {r['classification']} - {r['justification']}"
                    for r in part_a)
        + " | Part C effect in words: the warranty payment reverses $"
        + f"{out(dtd_decrease):,} of the deductible temporary difference "
        + f"(from ${out(dtd_begin):,} to ${out(dtd_end):,}), so the related "
        + f"deferred tax asset falls by ${out(dta_decrease):,} "
        + f"(from ${out(dta_begin):,} to ${out(dta_end):,}) at the 25% rate. "
        + "The settlement entry itself touches no tax account; the DTA change "
        + "is picked up in the year's income tax provision entry."
    ),
}

print(json.dumps(result, indent=2))
