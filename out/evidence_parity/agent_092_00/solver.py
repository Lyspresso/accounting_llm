"""ApexNova Therapeutics Inc. -- ASC 730 R&D cost cycle solver (agent_092#00).

Rounding convention: all money handled with decimal.Decimal; every computed
amount is quantized to cents ("0.01") using ROUND_HALF_UP, applied per period
(each year's depreciation / amortization is rounded independently, then the
final-year carrying amount is trued up so accumulated depreciation exactly
equals depreciable cost). Nothing is hard-coded: all totals, schedules, book
values and gain/loss are derived from the fact-table inputs.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def D(s): return Decimal(str(s))

# ---------------- Inputs (fact table, items 1-10) ----------------
items = [
    # (no, description, amount, treatment)
    (1,  "Materials consumed on current R&D projects (no alternative future use)", D(240000), "RD_EXPENSE"),
    (2,  "Laboratory equipment (significant alternative future uses)",            D(480000), "CAPITALIZE_EQUIP"),
    (3,  "Specialized testing apparatus, single project, no alternative use",     D(96000),  "RD_EXPENSE"),
    (4,  "Salaries and wages of R&D scientists and technicians",                  D(1150000),"RD_EXPENSE"),
    (5,  "Contract research fees paid to outside university lab",                 D(85000),  "RD_EXPENSE"),
    (6,  "Reasonable allocation of indirect facility costs related to R&D",       D(72000),  "RD_EXPENSE"),
    (7,  "Corporate headquarters G&A not clearly related to R&D",                 D(310000), "GA_EXPENSE"),
    (8,  "Troubleshooting/repair of existing commercial production line",         D(41000),  "PRODUCTION_EXPENSE"),
    (9,  "Design and construction of preproduction prototypes",                   D(55000),  "RD_EXPENSE"),
    (10, "Legal fees to register patent on successfully developed process",       D(12000),  "CAPITALIZE_PATENT"),
]

EQUIP_COST   = next(a for n,_,a,_ in items if n == 2)
EQUIP_LIFE   = 6
EQUIP_RESID  = D(0)
PATENT_COST  = next(a for n,_,a,_ in items if n == 10)
PATENT_LIFE  = 10
PATENT_RESID = D(0)
PATENT_MONTHS_Y1 = 6          # placed in service July 1
SALE_PRICE   = D(250000)
YEARS_DEPREC_BEFORE_SALE = 3  # Jan 1, Year 4 sale after 3 full years

# ---------------- Part a: initial recognition classification ----------------
rd_cash_items   = [(n,d,a) for n,d,a,t in items if t == "RD_EXPENSE"]
rd_cash_total   = q(sum((a for _,_,a in rd_cash_items), Decimal(0)))
cap_equip_total = q(sum((a for n,_,a,t in items if t == "CAPITALIZE_EQUIP"), Decimal(0)))
cap_patent_total= q(sum((a for n,_,a,t in items if t == "CAPITALIZE_PATENT"), Decimal(0)))
ga_total        = q(sum((a for n,_,a,t in items if t == "GA_EXPENSE"), Decimal(0)))
prod_total      = q(sum((a for n,_,a,t in items if t == "PRODUCTION_EXPENSE"), Decimal(0)))
cash_paid_total = q(sum((a for _,_,a,_ in items), Decimal(0)))

# ---------------- Part b/c: equipment depreciation schedule ----------------
annual_dep = q((EQUIP_COST - EQUIP_RESID) / D(EQUIP_LIFE))
schedule, bv, accum = [], EQUIP_COST, Decimal(0)
for yr in range(1, EQUIP_LIFE + 1):
    dep = annual_dep if yr < EQUIP_LIFE else q(EQUIP_COST - EQUIP_RESID - accum)  # true-up final year
    accum = q(accum + dep)
    end = q(bv - dep)
    schedule.append({"year": yr, "beginning_book_value": bv, "depreciation_expense_rd": dep,
                     "accumulated_depreciation": accum, "ending_book_value": end})
    bv = end
y1_dep = schedule[0]["depreciation_expense_rd"]

# ---------------- Part b: patent amortization ----------------
patent_annual_amort = q((PATENT_COST - PATENT_RESID) / D(PATENT_LIFE))
y1_amort = q(patent_annual_amort * D(PATENT_MONTHS_Y1) / D(12))
patent_bv_end_y1 = q(PATENT_COST - y1_amort)

# ---------------- Part d: R&D expense disclosed ----------------
rd_disclosed = q(rd_cash_total + y1_dep)
excluded_total = q(ga_total + prod_total + cap_patent_total + y1_amort)

# ---------------- Part e: disposal Jan 1, Year 4 ----------------
accum_at_sale = q(sum((schedule[i]["depreciation_expense_rd"] for i in range(YEARS_DEPREC_BEFORE_SALE)), Decimal(0)))
bv_at_sale    = q(EQUIP_COST - accum_at_sale)
gain          = q(SALE_PRICE - bv_at_sale)

# ---------------- Journal entries ----------------
def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": dr if dr is not None else Decimal(0),
            "credit": cr if cr is not None else Decimal(0)}

je = []
for n, desc, amt, t in items:
    if t == "RD_EXPENSE":
        je.append({"part": "a", "description": "Item %d - %s (expensed as R&D when incurred)" % (n, desc),
                   "lines": [L("Research and Development Expense", dr=q(amt)), L("Cash", cr=q(amt))]})
    elif t == "CAPITALIZE_EQUIP":
        je.append({"part": "a", "description": "Item %d - %s (capitalized: alternative future use)" % (n, desc),
                   "lines": [L("Laboratory Equipment (multi-use)", dr=q(amt)), L("Cash", cr=q(amt))]})
    elif t == "CAPITALIZE_PATENT":
        je.append({"part": "a", "description": "Item %d - %s (capitalized registration cost, not R&D)" % (n, desc),
                   "lines": [L("Patent", dr=q(amt)), L("Cash", cr=q(amt))]})
    elif t == "GA_EXPENSE":
        je.append({"part": "a", "description": "Item %d - %s (not R&D)" % (n, desc),
                   "lines": [L("General and Administrative Expense", dr=q(amt)), L("Cash", cr=q(amt))]})
    else:
        je.append({"part": "a", "description": "Item %d - %s (not R&D; routine production cost)" % (n, desc),
                   "lines": [L("Repairs and Maintenance Expense (Production)", dr=q(amt)), L("Cash", cr=q(amt))]})
je.append({"part": "a", "description": "Summary of part a: total R&D expensed immediately vs capitalized vs non-R&D",
           "lines": [L("Research and Development Expense (items 1,3,4,5,6,9)", dr=rd_cash_total),
                     L("Laboratory Equipment (multi-use, item 2)", dr=cap_equip_total),
                     L("Patent (item 10)", dr=cap_patent_total),
                     L("General and Administrative Expense (item 7)", dr=ga_total),
                     L("Repairs and Maintenance Expense (item 8)", dr=prod_total),
                     L("Cash", cr=cash_paid_total)]})
je.append({"part": "b", "description": "Dec 31, Year 1 - depreciation of multi-use laboratory equipment (charged to R&D)",
           "lines": [L("Research and Development Expense (Depreciation)", dr=y1_dep),
                     L("Accumulated Depreciation - Laboratory Equipment", cr=y1_dep)]})
je.append({"part": "b", "description": "Dec 31, Year 1 - patent amortization (6 months, not R&D)",
           "lines": [L("Amortization Expense - Patent", dr=y1_amort),
                     L("Accumulated Amortization - Patent", cr=y1_amort)]})
je.append({"part": "e", "description": "Jan 1, Year 4 - sale of multi-use laboratory equipment for cash",
           "lines": [L("Cash", dr=SALE_PRICE),
                     L("Accumulated Depreciation - Laboratory Equipment", dr=accum_at_sale),
                     L("Laboratory Equipment (multi-use)", cr=EQUIP_COST),
                     L("Gain on Sale of Equipment", cr=gain)]})
for e in je:
    dr = sum((l["debit"] for l in e["lines"]), Decimal(0))
    cr = sum((l["credit"] for l in e["lines"]), Decimal(0))
    assert q(dr) == q(cr), (e["description"], dr, cr)

# ---------------- Answers ----------------
A = []
for n, desc, amt, t in items:
    lab = {"RD_EXPENSE": "expensed immediately as R&D",
           "CAPITALIZE_EQUIP": "capitalized (equipment, alternative future use)",
           "CAPITALIZE_PATENT": "capitalized (patent registration legal fees)",
           "GA_EXPENSE": "NOT R&D - G&A expense",
           "PRODUCTION_EXPENSE": "NOT R&D - routine production troubleshooting/repair"}[t]
    A.append({"label": "a: Item %d treatment - %s" % (n, lab), "value": q(amt)})
A += [
 {"label": "a: Total Year 1 costs expensed immediately as R&D (items 1,3,4,5,6,9)", "value": rd_cash_total},
 {"label": "a: Total Year 1 costs capitalized - multi-use laboratory equipment (item 2)", "value": cap_equip_total},
 {"label": "a: Total Year 1 costs capitalized - patent registration legal fees (item 10)", "value": cap_patent_total},
 {"label": "a: Total Year 1 costs charged to G&A, not R&D (item 7)", "value": ga_total},
 {"label": "a: Total Year 1 costs charged to production repairs, not R&D (item 8)", "value": prod_total},
 {"label": "a: Total cash paid, Year 1 (items 1-10)", "value": cash_paid_total},
 {"label": "b(1): Dec 31, Year 1 depreciation on multi-use laboratory equipment (R&D expense)", "value": y1_dep},
 {"label": "b(2): Dec 31, Year 1 patent amortization (12,000 / 10 yrs x 6/12)", "value": y1_amort},
 {"label": "b(2): Patent carrying amount, Dec 31, Year 1", "value": patent_bv_end_y1},
]
for r in schedule:
    A.append({"label": "c: Year %d beginning book value" % r["year"], "value": r["beginning_book_value"]})
    A.append({"label": "c: Year %d depreciation expense (classified as R&D expense)" % r["year"], "value": r["depreciation_expense_rd"]})
    A.append({"label": "c: Year %d accumulated depreciation" % r["year"], "value": r["accumulated_depreciation"]})
    A.append({"label": "c: Year %d ending book value" % r["year"], "value": r["ending_book_value"]})
A += [
 {"label": "d: Total Year 1 R&D expense to be disclosed (1,698,000 cash R&D + 80,000 equipment depreciation)", "value": rd_disclosed},
 {"label": "d: Excluded from R&D - corporate HQ G&A (item 7)", "value": ga_total},
 {"label": "d: Excluded from R&D - routine troubleshooting/repair of existing production line (item 8)", "value": prod_total},
 {"label": "d: Excluded from R&D - patent registration legal fees, capitalized as intangible (item 10)", "value": cap_patent_total},
 {"label": "d: Excluded from R&D - Year 1 patent amortization (amortization of intangible, not R&D)", "value": y1_amort},
 {"label": "d: Excluded from R&D - equipment cost itself capitalized (only its 80,000 depreciation is R&D) (item 2)", "value": cap_equip_total},
 {"label": "d: Total Year 1 costs excluded from the R&D disclosure", "value": excluded_total},
 {"label": "e: Accumulated depreciation at Jan 1, Year 4 (3 x 80,000)", "value": accum_at_sale},
 {"label": "e: Book value of laboratory equipment at Jan 1, Year 4", "value": bv_at_sale},
 {"label": "e: Cash proceeds on sale", "value": SALE_PRICE},
 {"label": "e: Gain on sale of laboratory equipment (250,000 - 240,000)", "value": gain},
 {"label": "f: ASC 730 presentation/disclosure of total R&D cost", "value":
  "ASC 730-10-50-1 requires disclosure of the total R&D costs charged to expense in each income "
  "statement period presented. R&D costs are expensed as incurred and reported as an operating "
  "expense; the total (here $%s for Year 1) is disclosed either as a separate line item on the face "
  "of the income statement or in the notes/significant accounting policies, and includes depreciation "
  "of capitalized multi-use assets used in R&D." % format(rd_disclosed, ",")},
]

class E(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o) if o == o.to_integral_value() else float(o)
        return super().default(o)

out = {
 "id": "agent_092#00",
 "rounding_convention": "decimal.Decimal throughout; amounts quantized to cents (0.01) with ROUND_HALF_UP, applied per period (each year's depreciation/amortization rounded independently, final year trued up so accumulated depreciation equals depreciable cost). All results here are exact whole dollars.",
 "answers": A,
 "journal_entries": je,
 "insufficient_info": False,
 "notes": "Item 2 equipment has alternative future uses, so it is capitalized and only its annual straight-line depreciation ($480,000/6 = $80,000) is charged to R&D expense; item 3 apparatus has no alternative future use, so its full $96,000 is expensed immediately as R&D even though purchased April 1 (no depreciation on it). Items 7 (corporate G&A) and 8 (routine troubleshooting/repair of an existing commercial production line) are not R&D under ASC 730-10-55. Item 9 preproduction prototypes ARE R&D. Item 10 patent registration legal fees are capitalized as an intangible (not R&D) and amortized over the shorter 10-year useful life from July 1, Year 1 ($600 in Year 1); patent amortization is not part of R&D expense. Year 1 R&D disclosure = 240,000 + 96,000 + 1,150,000 + 85,000 + 72,000 + 55,000 + 80,000 = 1,778,000. Sale on Jan 1, Year 4: book value 480,000 - 240,000 = 240,000 vs proceeds 250,000, so a 10,000 gain (no Year 4 depreciation because the sale is on the first day of the year)."
}
print(json.dumps(out, cls=E, indent=1))
