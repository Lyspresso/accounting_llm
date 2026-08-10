#!/usr/bin/env python3
"""
Blind solver -- item agent_223#00
Northline Photonix Corp.: R&D initial recognition, subsequent measurement
schedules (multi-use equipment + multi-project intangible), Year-1 R&D
disclosure total, and Jan 1 Year 4 disposal.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats are used anywhere.
Every monetary result is quantized to the cent with ROUND_HALF_UP, applied
once per period (per-year depreciation / amortization is rounded as it is
computed, and the rounded per-period amounts are what accumulate) rather
than rounding only at the end.  In this fact pattern every straight-line
amount divides evenly, so the convention is not outcome-determinative; it is
stated and applied so the schedules would still tie if the inputs changed.
No present-value factors are involved in this item.

AUTHORITY / METHOD (ASC 730-10; textbook Ch. 13 LO 13-7, Exhibit 13-4)
----------------------------------------------------------------------
R&D costs are expensed as incurred, EXCEPT that materials, equipment,
facilities, and intangibles acquired for R&D that have ALTERNATIVE FUTURE
USES are capitalized; their subsequent depreciation/amortization is then
classified as R&D expense.  Costs with no alternative future use are
expensed immediately in full.  Excluded from R&D: G&A not clearly related
to R&D, and routine quality control during commercial production.

Straight-line depreciation = (cost - residual) / useful life.
Both capitalized assets were acquired January 1 of Year 1, so Year 1 takes a
full year of depreciation / amortization (no partial-period proration).

Run:  python3 solver.py     ->  prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to the cent using ROUND_HALF_UP (applied per period)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """Emit a plain JSON number: int when the cents are zero."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Fact pattern (items 1-10 from the stem), with the ASC 730 classification
# ---------------------------------------------------------------------------
# (item#, description, amount, treatment)
#   "rd_expense"  -> expense immediately, included in Year-1 R&D disclosure
#   "capitalize_equipment" / "capitalize_intangible" -> asset; dep/amort is R&D
#   "non_rd"      -> expense immediately, NOT part of R&D disclosure
FACTS = [
    (1,  "Materials consumed on current R&D projects (no alternative future use)",
     Decimal("185000"), "rd_expense"),
    (2,  "Laboratory equipment, significant alternative future uses (Jan 1, Yr 1)",
     Decimal("600000"), "capitalize_equipment"),
    (3,  "Specialized testing chamber, single R&D project, no alternative future use",
     Decimal("72000"), "rd_expense"),
    (4,  "Salaries and wages of R&D scientists and technicians",
     Decimal("980000"), "rd_expense"),
    (5,  "Contract R&D services performed by outside university lab",
     Decimal("125000"), "rd_expense"),
    (6,  "Reasonable allocation of indirect facility costs clearly related to R&D",
     Decimal("48000"), "rd_expense"),
    (7,  "Finite-life technical database/know-how license, multiple R&D projects (Jan 1, Yr 1)",
     Decimal("40000"), "capitalize_intangible"),
    (8,  "Design and construction of preproduction prototypes",
     Decimal("44000"), "rd_expense"),
    (9,  "Quality control / troubleshooting during commercial production",
     Decimal("35000"), "non_rd"),
    (10, "Corporate HQ G&A not clearly related to R&D",
     Decimal("200000"), "non_rd"),
]

# Capitalized-asset terms, straight from the stem
EQUIP_COST = Decimal("600000")
EQUIP_RESIDUAL = Decimal("30000")
EQUIP_LIFE = 5                       # years, straight-line, in service Jan 1 Yr 1

LICENSE_COST = Decimal("40000")
LICENSE_RESIDUAL = Decimal("0")
LICENSE_LIFE = 4                     # years, straight-line, acquired Jan 1 Yr 1

DISPOSAL_PROCEEDS = Decimal("240000")   # Jan 1, Year 4, cash
YEARS_DEPRECIATED_AT_DISPOSAL = 3       # Years 1-3 already recorded


# ---------------------------------------------------------------------------
# Part a -- Year 1 initial recognition, grouped by treatment
# ---------------------------------------------------------------------------
rd_expensed_items = [f for f in FACTS if f[3] == "rd_expense"]
rd_expensed_total = money(sum((f[2] for f in rd_expensed_items), Decimal("0")))

capitalized_total = money(EQUIP_COST + LICENSE_COST)

non_rd_items = [f for f in FACTS if f[3] == "non_rd"]
qc_amount = money(next(f[2] for f in FACTS if f[0] == 9))
ga_amount = money(next(f[2] for f in FACTS if f[0] == 10))
non_rd_total = money(sum((f[2] for f in non_rd_items), Decimal("0")))


# ---------------------------------------------------------------------------
# Parts c / d -- straight-line schedules (round each period, then accumulate)
# ---------------------------------------------------------------------------
def straight_line_schedule(cost: Decimal, residual: Decimal, life: int):
    """Return list of dicts: year, beginning carrying value, charge, ending CV.

    The per-period charge is rounded HALF_UP to the cent; the final period
    absorbs any residual rounding drift so the schedule ends exactly at the
    residual value (self-balancing, not a plug of the answer)."""
    per_period = money((cost - residual) / Decimal(life))
    rows = []
    begin = money(cost)
    for yr in range(1, life + 1):
        charge = per_period
        if yr == life:                       # force the schedule to close exactly
            charge = money(begin - residual)
        end = money(begin - charge)
        rows.append({"year": yr, "beginning": begin, "charge": charge, "ending": end})
        begin = end
    return rows


equip_sched = straight_line_schedule(EQUIP_COST, EQUIP_RESIDUAL, EQUIP_LIFE)
license_sched = straight_line_schedule(LICENSE_COST, LICENSE_RESIDUAL, LICENSE_LIFE)

equip_annual_dep = equip_sched[0]["charge"]        # Year-1 depreciation (part b)
license_annual_amort = license_sched[0]["charge"]  # Year-1 amortization (part b)


# ---------------------------------------------------------------------------
# Part e -- Year 1 R&D expense to be DISCLOSED
# ---------------------------------------------------------------------------
year1_rd_disclosed = money(
    rd_expensed_total + equip_annual_dep + license_annual_amort
)


# ---------------------------------------------------------------------------
# Part f -- Jan 1, Year 4 disposal of the multi-use laboratory equipment
# ---------------------------------------------------------------------------
accum_dep_at_disposal = money(
    sum((equip_sched[i]["charge"] for i in range(YEARS_DEPRECIATED_AT_DISPOSAL)),
        Decimal("0"))
)
book_value_at_disposal = money(EQUIP_COST - accum_dep_at_disposal)
gain_loss = money(DISPOSAL_PROCEEDS - book_value_at_disposal)   # negative = loss
loss_on_disposal = money(-gain_loss) if gain_loss < 0 else Decimal("0.00")
gain_on_disposal = gain_loss if gain_loss > 0 else Decimal("0.00")


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = []

# a(1) -- R&D costs expensed as incurred (items 1, 3, 4, 5, 6, 8)
journal_entries.append({
    "part": "a",
    "description": ("Year 1 initial recognition - costs expensed as R&D when incurred "
                    "(items 1, 3, 4, 5, 6, 8): no alternative future use / services / "
                    "salaries / indirect R&D costs / prototypes"),
    "lines": [
        line("Research and Development Expense", debit=rd_expensed_total),
        line("Cash", credit=rd_expensed_total),
    ],
})

# a(2) -- capitalized items with alternative future uses (items 2, 7)
journal_entries.append({
    "part": "a",
    "description": ("Year 1 initial recognition - capitalized because of significant "
                    "alternative future uses (items 2 and 7)"),
    "lines": [
        line("Laboratory Equipment", debit=EQUIP_COST),
        line("Technical License (finite-life intangible asset)", debit=LICENSE_COST),
        line("Cash", credit=capitalized_total),
    ],
})

# a(3) -- non-R&D expenses (items 9, 10)
journal_entries.append({
    "part": "a",
    "description": "Year 1 initial recognition - non-R&D operating costs (items 9 and 10)",
    "lines": [
        line("Quality Control Expense (commercial production)", debit=qc_amount),
        line("General and Administrative Expense", debit=ga_amount),
        line("Cash", credit=non_rd_total),
    ],
})

# b(1) -- Dec 31 Year 1 depreciation of multi-use lab equipment
journal_entries.append({
    "part": "b",
    "description": ("December 31, Year 1 adjusting entry - depreciation of the multi-use "
                    "laboratory equipment, classified as R&D expense"),
    "lines": [
        line("Research and Development Expense (Depreciation)", debit=equip_annual_dep),
        line("Accumulated Depreciation - Laboratory Equipment", credit=equip_annual_dep),
    ],
})

# b(2) -- Dec 31 Year 1 amortization of multi-project technical license
journal_entries.append({
    "part": "b",
    "description": ("December 31, Year 1 adjusting entry - amortization of the "
                    "multi-project technical license, classified as R&D expense"),
    "lines": [
        line("Research and Development Expense (Amortization)", debit=license_annual_amort),
        line("Accumulated Amortization - Technical License", credit=license_annual_amort),
    ],
})

# f -- Jan 1 Year 4 disposal
disposal_lines = [
    line("Cash", debit=DISPOSAL_PROCEEDS),
    line("Accumulated Depreciation - Laboratory Equipment", debit=accum_dep_at_disposal),
]
if loss_on_disposal > 0:
    disposal_lines.append(line("Loss on Disposal of Equipment", debit=loss_on_disposal))
disposal_lines.append(line("Laboratory Equipment", credit=EQUIP_COST))
if gain_on_disposal > 0:
    disposal_lines.append(line("Gain on Disposal of Equipment", credit=gain_on_disposal))

journal_entries.append({
    "part": "f",
    "description": ("January 1, Year 4 sale of the multi-use laboratory equipment for cash, "
                    "after Years 1-3 depreciation has been recorded"),
    "lines": disposal_lines,
})

# Debits must equal credits in every entry -- verify, do not plug.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), f"Unbalanced entry in part {je['part']}: {dr} vs {cr}"

# Schedules must close to residual / zero.
assert equip_sched[-1]["ending"] == money(EQUIP_RESIDUAL)
assert license_sched[-1]["ending"] == money(LICENSE_RESIDUAL)


# ---------------------------------------------------------------------------
# Answers -- ONLY the figures the Required parts ask for (c, d, e)
# Parts a, b, f are journal entries; part g is narrative (see notes).
# ---------------------------------------------------------------------------
answers = []

# c -- depreciation schedule for the multi-use laboratory equipment, Years 1-5
for row in equip_sched:
    y = row["year"]
    answers.append({"label": f"c: lab equipment Year {y} beginning book value",
                    "value": num(row["beginning"])})
    answers.append({"label": f"c: lab equipment Year {y} depreciation (R&D expense)",
                    "value": num(row["charge"])})
    answers.append({"label": f"c: lab equipment Year {y} ending book value",
                    "value": num(row["ending"])})

# d -- amortization schedule for the multi-project technical license, Years 1-4
for row in license_sched:
    y = row["year"]
    answers.append({"label": f"d: technical license Year {y} beginning carrying value",
                    "value": num(row["beginning"])})
    answers.append({"label": f"d: technical license Year {y} amortization (R&D expense)",
                    "value": num(row["charge"])})
    answers.append({"label": f"d: technical license Year {y} ending carrying value",
                    "value": num(row["ending"])})

# e -- total Year 1 R&D expense disclosed
answers.append({"label": "e: total Year 1 research and development expense disclosed",
                "value": num(year1_rd_disclosed)})

notes = (
    "c: part c asks for the COMPLETE straight-line schedule over the equipment's 5-year "
    "life, so Years 4-5 are shown as scheduled (the asset is actually sold Jan 1 of Year 4 "
    "per part f, so no Year 4-5 depreciation is in fact recorded). | "
    "e (items EXCLUDED from Year 1 R&D expense): quality control and troubleshooting "
    "during commercial production of existing products $35,000 (routine ongoing "
    "production activity, not R&D); corporate headquarters G&A not clearly related to "
    "R&D $200,000; and the CAPITALIZED COST of the two alternative-future-use assets - "
    "the $600,000 laboratory equipment and the $40,000 technical license - of which only "
    "the current-year depreciation ($114,000) and amortization ($10,000) enter R&D "
    "expense. | g: the equipment has significant alternative future uses beyond the "
    "current projects, so ASC 730-10-25-2(a) requires it to be recognized as an asset "
    "rather than expensed on purchase; the R&D charge is the consumption of that asset, "
    "so each year's depreciation is classified as R&D expense while the asset is used in "
    "R&D. Expensing the full $600,000 in Year 1 would charge future periods' benefit to "
    "Year 1. Items with NO alternative future use (the $72,000 single-project testing "
    "chamber, the $185,000 of materials) are expensed in full when acquired."
)

output = {
    "id": "agent_223#00",
    "rounding_convention": ("decimal.Decimal throughout, no floats; ROUND_HALF_UP to the "
                            "cent applied per period (each year's straight-line charge is "
                            "rounded as computed and the rounded charges accumulate), not "
                            "only at the end; no PV factors are used in this item; both "
                            "capitalized assets were placed in service January 1 of Year 1 "
                            "so Year 1 takes a full year of depreciation/amortization"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
