#!/usr/bin/env python3
"""Blind solver for item agent_092#00 -- ApexNova Therapeutics Inc., full R&D cost cycle
(ASC 730 initial recognition, Year-1 R&D depreciation, 6-year depreciation schedule,
disposal of multi-use equipment, R&D disclosure total).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; floats are never used for money.
Rounding: ROUND_HALF_UP to the cent (two decimal places), applied PER PERIOD --
i.e. each year's straight-line depreciation charge and each period's patent
amortization charge is rounded on its own before being accumulated, rather than
rounding only a cumulative total at the end.  Any residual rounding difference
would be absorbed in the final period of the asset's life so that accumulated
depreciation exactly equals depreciable cost; with the facts in this stem every
periodic charge divides evenly, so no plug is actually needed.
No present-value work is required by this item, so no PV table factors are used.

ACCOUNTING POLICY APPLIED (ASC 730-10; textbook Ch. 13, LO 13-7, Exhibit 13-4)
-----------------------------------------------------------------------------
* Materials/equipment/facilities acquired for R&D with NO alternative future use
  -> expensed immediately as R&D expense (items 1 and 3).
* Materials/equipment/facilities with SIGNIFICANT ALTERNATIVE FUTURE USES
  -> capitalized; the periodic depreciation is classified as R&D expense (item 2).
* Salaries/wages of personnel engaged in R&D -> R&D expense (item 4).
* R&D services performed by another entity -> R&D expense (item 5).
* Reasonable allocation of indirect costs clearly related to R&D -> R&D expense (item 6).
* G&A not clearly related to R&D -> NOT R&D; ordinary operating expense (item 7).
* Troubleshooting breakdowns during COMMERCIAL PRODUCTION -> NOT R&D; ordinary
  operating (repairs/maintenance) expense (item 8).
* Design/construction/testing of PREPRODUCTION PROTOTYPES -> R&D expense (item 9).
* Legal fees to an outside counsel to register a successfully developed patent
  -> capitalized as a finite-life intangible (Patent); NOT R&D.  Amortized
  straight-line over the SHORTER of remaining legal life (20 yr) and estimated
  useful life (10 yr) = 10 years, from the July 1 in-service date, so Year 1 gets
  6/12 of a full year.  Patent amortization is NOT part of R&D expense.

Run:  python3 solver.py      (prints one JSON object on stdout)
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Round to the cent, ROUND_HALF_UP (the convention used per period)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly: integral cents -> int, otherwise float of the exact string."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Fact pattern (Year 1), transcribed from the stem
# ---------------------------------------------------------------------------
# (item no., description, amount, treatment)
#   treatment: "RD_EXPENSE"  -> immediately expensed and included in R&D disclosure
#              "RD_ASSET"    -> capitalized equipment; depreciation classified as R&D
#              "NON_RD"      -> expensed but excluded from R&D disclosure
#              "INTANGIBLE"  -> capitalized intangible; amortization NOT R&D
FACTS = [
    (1, "Materials purchased and consumed solely on current R&D projects (no alternative future use)",
     Decimal("240000"), "RD_EXPENSE", "Research and Development Expense"),
    (2, "Laboratory equipment with significant alternative future uses (Jan 1, Year 1)",
     Decimal("480000"), "RD_ASSET", "Laboratory Equipment"),
    (3, "Specialized testing apparatus for a single R&D project only (no alternative future use)",
     Decimal("96000"), "RD_EXPENSE", "Research and Development Expense"),
    (4, "Salaries and wages of scientists and technicians engaged in R&D",
     Decimal("1150000"), "RD_EXPENSE", "Research and Development Expense"),
    (5, "Fees paid to an outside university lab for contract research services",
     Decimal("85000"), "RD_EXPENSE", "Research and Development Expense"),
    (6, "Reasonable allocation of indirect facility costs clearly related to R&D",
     Decimal("72000"), "RD_EXPENSE", "Research and Development Expense"),
    (7, "Corporate headquarters G&A not clearly related to R&D",
     Decimal("310000"), "NON_RD", "General and Administrative Expense"),
    (8, "Troubleshooting/repair of breakdowns on an existing commercial production line",
     Decimal("41000"), "NON_RD", "Repairs and Maintenance Expense"),
    (9, "Design and construction of preproduction prototypes",
     Decimal("55000"), "RD_EXPENSE", "Research and Development Expense"),
    (10, "Legal fees to outside counsel to register a patent on a successfully developed process",
     Decimal("12000"), "INTANGIBLE", "Patent"),
]

# Item 2 -- multi-use laboratory equipment
EQUIP_COST = Decimal("480000")
EQUIP_RESIDUAL = Decimal("0")
EQUIP_LIFE_YEARS = 6
EQUIP_IN_SERVICE_MONTHS_YEAR1 = 12          # placed in service January 1, Year 1
SALE_PROCEEDS = Decimal("250000")           # January 1, Year 4
YEARS_DEPRECIATED_BEFORE_SALE = 3           # three full years (Years 1-3)

# Item 10 -- patent
PATENT_COST = Decimal("12000")
PATENT_LEGAL_LIFE = 20
PATENT_USEFUL_LIFE = 10
PATENT_MONTHS_YEAR1 = 6                     # July 1 -> December 31

# ---------------------------------------------------------------------------
# (c) straight-line depreciation schedule, Years 1-6
# ---------------------------------------------------------------------------
depreciable_base = EQUIP_COST - EQUIP_RESIDUAL
annual_dep_full = money(depreciable_base / EQUIP_LIFE_YEARS)

schedule = []
book_value = EQUIP_COST
accumulated = Decimal("0")
for year in range(1, EQUIP_LIFE_YEARS + 1):
    months = EQUIP_IN_SERVICE_MONTHS_YEAR1 if year == 1 else 12
    charge = money(annual_dep_full * Decimal(months) / Decimal(12))
    if year == EQUIP_LIFE_YEARS:
        # final-period plug so accumulated depreciation ties to depreciable base
        charge = money(depreciable_base - accumulated)
    beginning = book_value
    accumulated += charge
    book_value = money(EQUIP_COST - accumulated)
    schedule.append({
        "year": year,
        "beginning_book_value": beginning,
        "depreciation_expense_rd": charge,
        "accumulated_depreciation": accumulated,
        "ending_book_value": book_value,
    })

year1_depreciation = schedule[0]["depreciation_expense_rd"]

# ---------------------------------------------------------------------------
# (b)(2) patent amortization, Year 1
# ---------------------------------------------------------------------------
amort_life = min(PATENT_LEGAL_LIFE, PATENT_USEFUL_LIFE)
patent_annual_amort = money(PATENT_COST / amort_life)
patent_year1_amort = money(patent_annual_amort * Decimal(PATENT_MONTHS_YEAR1) / Decimal(12))

# ---------------------------------------------------------------------------
# (d) total R&D expense disclosed for Year 1
# ---------------------------------------------------------------------------
rd_cash_costs = sum((amt for _, _, amt, t, _ in FACTS if t == "RD_EXPENSE"), Decimal("0"))
total_rd_expense = money(rd_cash_costs + year1_depreciation)

excluded_from_rd = [
    {"item": n, "description": desc, "amount": num(amt)}
    for n, desc, amt, t, _ in FACTS if t in ("NON_RD", "INTANGIBLE")
]

# ---------------------------------------------------------------------------
# (e) January 1, Year 4 disposal of the laboratory equipment
# ---------------------------------------------------------------------------
accum_at_sale = sum((r["depreciation_expense_rd"] for r in schedule
                     if r["year"] <= YEARS_DEPRECIATED_BEFORE_SALE), Decimal("0"))
accum_at_sale = money(accum_at_sale)
book_value_at_sale = money(EQUIP_COST - accum_at_sale)
gain_loss = money(SALE_PROCEEDS - book_value_at_sale)   # positive = gain

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = []

# (a) Year 1 initial recognition, grouped by accounting treatment.
rd_items = [n for n, _, _, t, _ in FACTS if t == "RD_EXPENSE"]
journal_entries.append({
    "part": "a",
    "description": ("Year 1 - costs immediately expensed as R&D (items "
                    + ", ".join(str(n) for n in rd_items) + ")"),
    "lines": [line("Research and Development Expense", debit=rd_cash_costs),
              line("Cash", credit=rd_cash_costs)],
})
journal_entries.append({
    "part": "a",
    "description": "Year 1 - item 2: capitalize laboratory equipment with alternative future uses",
    "lines": [line("Laboratory Equipment", debit=EQUIP_COST),
              line("Cash", credit=EQUIP_COST)],
})
_ga = next(amt for n, _, amt, _, _ in FACTS if n == 7)
journal_entries.append({
    "part": "a",
    "description": "Year 1 - item 7: corporate G&A not clearly related to R&D (non-R&D)",
    "lines": [line("General and Administrative Expense", debit=_ga),
              line("Cash", credit=_ga)],
})
_repairs = next(amt for n, _, amt, _, _ in FACTS if n == 8)
journal_entries.append({
    "part": "a",
    "description": "Year 1 - item 8: troubleshooting/repairs on commercial production line (non-R&D)",
    "lines": [line("Repairs and Maintenance Expense", debit=_repairs),
              line("Cash", credit=_repairs)],
})
journal_entries.append({
    "part": "a",
    "description": "Year 1 - item 10 (July 1): capitalize legal fees to register the patent",
    "lines": [line("Patent", debit=PATENT_COST),
              line("Cash", credit=PATENT_COST)],
})

# (b) December 31, Year 1 adjusting entries
journal_entries.append({
    "part": "b",
    "description": "Dec 31, Year 1 - depreciation on multi-use laboratory equipment (classified as R&D)",
    "lines": [line("Research and Development Expense", debit=year1_depreciation),
              line("Accumulated Depreciation - Laboratory Equipment", credit=year1_depreciation)],
})
journal_entries.append({
    "part": "b",
    "description": "Dec 31, Year 1 - patent amortization, 6 months over a 10-year life (not R&D)",
    "lines": [line("Amortization Expense - Patent", debit=patent_year1_amort),
              line("Patent", credit=patent_year1_amort)],
})

# (e) January 1, Year 4 disposal
disposal_lines = [
    line("Cash", debit=SALE_PROCEEDS),
    line("Accumulated Depreciation - Laboratory Equipment", debit=accum_at_sale),
    line("Laboratory Equipment", credit=EQUIP_COST),
]
if gain_loss > 0:
    disposal_lines.append(line("Gain on Sale of Equipment", credit=gain_loss))
elif gain_loss < 0:
    disposal_lines.insert(2, line("Loss on Sale of Equipment", debit=-gain_loss))
journal_entries.append({
    "part": "e",
    "description": "Jan 1, Year 4 - sale of laboratory equipment for cash after 3 full years of depreciation",
    "lines": disposal_lines,
})

# balance check: debits must equal credits in every entry
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, f"unbalanced entry: {je['description']} ({d} != {c})"

# ---------------------------------------------------------------------------
# Answers -- only figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = []
for row in schedule:
    y = row["year"]
    answers.append({"label": f"c: Year {y} beginning book value",
                    "value": num(row["beginning_book_value"])})
    answers.append({"label": f"c: Year {y} depreciation expense (classified as R&D)",
                    "value": num(row["depreciation_expense_rd"])})
    answers.append({"label": f"c: Year {y} ending book value",
                    "value": num(row["ending_book_value"])})
answers.append({"label": "d: total research and development expense disclosed for Year 1",
                "value": num(total_rd_expense)})

notes = (
    "Year 1 R&D expense = 240,000 materials + 96,000 single-use apparatus (no alternative "
    "future use, expensed in full, not depreciated) + 1,150,000 R&D salaries + 85,000 contract "
    "research + 72,000 R&D-related indirect costs + 55,000 preproduction prototypes + 80,000 "
    "depreciation on the multi-use lab equipment = 1,778,000. "
    "Excluded from R&D: " + "; ".join(
        f"item {e['item']} ${e['amount']:,}" for e in excluded_from_rd
    ) + " (corporate G&A not clearly related to R&D; troubleshooting during commercial "
    "production; patent registration legal fees, which are capitalized, and the related "
    "600 of Year 1 patent amortization). "
    "(f) Presentation/disclosure under ASC 730-10-50-1: R&D costs are charged to expense as "
    "incurred and the TOTAL R&D cost charged to expense (1,778,000) is disclosed for each "
    "period an income statement is presented - shown either as a separate operating expense "
    "line in the income statement or in the notes to the financial statements; capitalized "
    "multi-use assets appear in PP&E with their depreciation included in that R&D total."
)

out = {
    "id": "agent_092#00",
    "rounding_convention": ("ROUND_HALF_UP to the cent, applied per period (each year's "
                            "depreciation and each period's amortization rounded separately); "
                            "no PV factors required"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
