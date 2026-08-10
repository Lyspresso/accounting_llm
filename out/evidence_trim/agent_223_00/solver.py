"""Northline Photonix Corp. — R&D initial recognition, subsequent measurement, disposal (LO 13-7).

Rounding convention: all money is decimal.Decimal, quantized to the cent with
ROUND_HALF_UP independently in each period (per-period rounding, no float math).
Every figure is derived from the fact pattern; nothing is hard-coded as a result.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------- fact pattern ----------
materials      = Decimal("185000")   # 1  no alt use -> R&D expense
equip_cost     = Decimal("600000")   # 2  alt future uses -> capitalize
equip_residual = Decimal("30000")
equip_life     = 5
chamber        = Decimal("72000")    # 3  single project, no alt use -> R&D expense
salaries       = Decimal("980000")   # 4  R&D expense
contract_rd    = Decimal("125000")   # 5  R&D expense
indirect       = Decimal("48000")    # 6  R&D expense
lic_cost       = Decimal("40000")    # 7  multi-project intangible -> capitalize
lic_residual   = Decimal("0")
lic_life       = 4
prototypes     = Decimal("44000")    # 8  R&D expense
qc_production  = Decimal("35000")    # 9  NOT R&D (commercial production)
ga             = Decimal("200000")   # 10 NOT R&D (corporate G&A)
sale_price     = Decimal("240000")   # Jan 1, Yr 4
years_held     = 3

# ---------- (a) initial recognition ----------
rd_expensed_now = materials + chamber + salaries + contract_rd + indirect + prototypes
capitalized     = equip_cost + lic_cost
non_rd_expense  = qc_production + ga
total_cash      = rd_expensed_now + capitalized + non_rd_expense

# ---------- (b)-(c) equipment straight-line schedule ----------
dep_annual = q((equip_cost - equip_residual) / Decimal(equip_life))
equip_sched, bv = [], equip_cost
for yr in range(1, equip_life + 1):
    d = dep_annual if yr < equip_life else q(bv - equip_residual)  # true-up final year
    equip_sched.append({"year": yr, "beginning_bv": n(bv), "depreciation_rd": n(d),
                        "ending_bv": n(bv - d)})
    bv = bv - d

# ---------- (b)-(d) license straight-line amortization schedule ----------
amort_annual = q((lic_cost - lic_residual) / Decimal(lic_life))
lic_sched, cv = [], lic_cost
for yr in range(1, lic_life + 1):
    a = amort_annual if yr < lic_life else q(cv - lic_residual)
    lic_sched.append({"year": yr, "beginning_cv": n(cv), "amortization_rd": n(a),
                      "ending_cv": n(cv - a)})
    cv = cv - a

# ---------- (e) Year 1 disclosed R&D ----------
dep_y1   = q(Decimal(str(equip_sched[0]["depreciation_rd"])))
amort_y1 = q(Decimal(str(lic_sched[0]["amortization_rd"])))
rd_disclosed_y1 = rd_expensed_now + dep_y1 + amort_y1

# ---------- (f) disposal Jan 1, Year 4 ----------
accum_dep_3 = q(sum((Decimal(str(r["depreciation_rd"])) for r in equip_sched[:years_held]), Decimal("0")))
bv_at_sale  = q(equip_cost - accum_dep_3)
gain_loss   = q(sale_price - bv_at_sale)          # negative => loss
loss        = q(-gain_loss) if gain_loss < 0 else Decimal("0")
gain        = gain_loss if gain_loss > 0 else Decimal("0")

def L(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account": acct, "debit": n(dr), "credit": n(cr)}

jes = [
 {"part": "a", "lines": [
   L("Research and Development Expense (items 1,3,4,5,6,8: materials $%s, single-use testing chamber $%s, R&D salaries $%s, contract R&D $%s, allocated R&D facility costs $%s, preproduction prototypes $%s)"
     % (materials, chamber, salaries, contract_rd, indirect, prototypes), dr=rd_expensed_now),
   L("Cash", cr=rd_expensed_now)]},
 {"part": "a", "lines": [
   L("Laboratory Equipment (item 2 — significant alternative future uses)", dr=equip_cost),
   L("Technical Database/Know-How License (item 7 — multi-project intangible)", dr=lic_cost),
   L("Cash", cr=capitalized)]},
 {"part": "a", "lines": [
   L("Quality Control / Cost of Production Expense (item 9 — commercial production)", dr=qc_production),
   L("General and Administrative Expense (item 10 — corporate G&A)", dr=ga),
   L("Cash", cr=non_rd_expense)]},
 {"part": "b", "lines": [
   L("Research and Development Expense (depreciation — multi-use laboratory equipment)", dr=dep_y1),
   L("Accumulated Depreciation — Laboratory Equipment", cr=dep_y1)]},
 {"part": "b", "lines": [
   L("Research and Development Expense (amortization — multi-project technical license)", dr=amort_y1),
   L("Accumulated Amortization — Technical License", cr=amort_y1)]},
 {"part": "f", "lines": [
   L("Cash", dr=sale_price),
   L("Accumulated Depreciation — Laboratory Equipment", dr=accum_dep_3),
   L("Loss on Disposal of Equipment", dr=loss),
   L("Laboratory Equipment", cr=equip_cost)] + ([L("Gain on Disposal of Equipment", cr=gain)] if gain > 0 else [])},
]
for je in jes:
    assert q(sum(Decimal(str(l["debit"])) for l in je["lines"])) == q(sum(Decimal(str(l["credit"])) for l in je["lines"]))

ans = [
 {"label": "a: Total Year 1 costs expensed immediately as R&D (items 1,3,4,5,6,8)", "value": n(rd_expensed_now)},
 {"label": "a: Laboratory equipment capitalized (item 2)", "value": n(equip_cost)},
 {"label": "a: Technical license capitalized (item 7)", "value": n(lic_cost)},
 {"label": "a: Total capitalized in Year 1", "value": n(capitalized)},
 {"label": "a: Non-R&D expense recognized (item 9 QC $%s + item 10 G&A $%s)" % (qc_production, ga), "value": n(non_rd_expense)},
 {"label": "a: Total cash paid, items 1-10", "value": n(total_cash)},
 {"label": "b(1): Dec 31, Yr 1 depreciation of multi-use lab equipment (charged to R&D)", "value": n(dep_y1)},
 {"label": "b(2): Dec 31, Yr 1 amortization of multi-project technical license (charged to R&D)", "value": n(amort_y1)},
 {"label": "c: Annual straight-line depreciation, laboratory equipment ($600,000 - $30,000) / 5", "value": n(dep_annual)},
]
for r in equip_sched:
    ans += [{"label": "c: Equipment Year %d beginning book value" % r["year"], "value": r["beginning_bv"]},
            {"label": "c: Equipment Year %d depreciation (R&D expense)" % r["year"], "value": r["depreciation_rd"]},
            {"label": "c: Equipment Year %d ending book value" % r["year"], "value": r["ending_bv"]}]
ans.append({"label": "d: Annual straight-line amortization, technical license $40,000 / 4", "value": n(amort_annual)})
for r in lic_sched:
    ans += [{"label": "d: License Year %d beginning carrying value" % r["year"], "value": r["beginning_cv"]},
            {"label": "d: License Year %d amortization (R&D expense)" % r["year"], "value": r["amortization_rd"]},
            {"label": "d: License Year %d ending carrying value" % r["year"], "value": r["ending_cv"]}]
ans += [
 {"label": "e: Total Year 1 R&D expense disclosed (direct R&D $%s + equipment depreciation $%s + license amortization $%s)" % (rd_expensed_now, dep_y1, amort_y1), "value": n(rd_disclosed_y1)},
 {"label": "e: Item 9 quality control during commercial production — EXCLUDED from R&D", "value": n(qc_production)},
 {"label": "e: Item 10 corporate G&A not clearly related to R&D — EXCLUDED from R&D", "value": n(ga)},
 {"label": "e: Item 2 equipment purchase price — EXCLUDED from Year 1 R&D (capitalized; only depreciation is R&D)", "value": n(equip_cost)},
 {"label": "e: Item 7 license purchase price — EXCLUDED from Year 1 R&D (capitalized; only amortization is R&D)", "value": n(lic_cost)},
 {"label": "f: Accumulated depreciation at Jan 1, Year 4 (3 x $%s)" % dep_annual, "value": n(accum_dep_3)},
 {"label": "f: Book value of laboratory equipment at Jan 1, Year 4", "value": n(bv_at_sale)},
 {"label": "f: Loss on disposal (proceeds $%s - book value $%s)" % (sale_price, bv_at_sale), "value": n(loss)},
]

notes = (
 "a. Items 1,3,4,5,6,8 have no alternative future use (or are R&D services/labor/overhead/preproduction "
 "prototypes of an asset still under development) and are expensed as R&D when incurred = $%s. Items 2 and 7 "
 "have significant alternative future uses across multiple projects, so they are capitalized ($%s and $%s) and "
 "charged to R&D through depreciation/amortization. Item 9 (quality control during commercial production) and "
 "item 10 (corporate G&A not clearly related to R&D) are ordinary operating expenses, not R&D. "
 "e. Year 1 disclosed R&D = $%s. Excluded: QC on commercial production $%s; corporate G&A $%s; the capitalized "
 "cost of the lab equipment $%s and of the technical license $%s (only the $%s depreciation and $%s amortization "
 "enter R&D in Year 1). "
 "f. Jan 1 Yr 4: cost $%s less accumulated depreciation $%s = book value $%s; proceeds $%s produce a loss of $%s. "
 "g. The equipment is not fully expensed in Year 1 because it has significant alternative future uses — it is a "
 "productive asset that will serve future R&D projects and production support, so it meets the definition of an "
 "asset and is capitalized. Its service potential is nevertheless consumed by R&D activity, so each period's "
 "depreciation is the portion of the asset's cost used up in R&D and is classified as R&D expense in that period. "
 "Equipment devoted to a single project with no alternative use (item 3) has no future service potential beyond "
 "that project and is expensed immediately."
) % (rd_expensed_now, equip_cost, lic_cost, rd_disclosed_y1, qc_production, ga, equip_cost, lic_cost,
     dep_y1, amort_y1, equip_cost, accum_dep_3, bv_at_sale, sale_price, loss)

print(json.dumps({
 "id": "agent_223#00",
 "rounding_convention": "decimal.Decimal throughout; amounts quantized to $0.01 using ROUND_HALF_UP independently each period; final-period depreciation/amortization trued up to residual value.",
 "answers": ans,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": notes}, indent=1))
