"""Solver for agent_333#02 — Northline Processors Corp., LO 11-6.

Rounding convention: all money is decimal.Decimal; every computed amount is
quantized to the cent using ROUND_HALF_UP, applied once per period / per
computed figure (no float arithmetic anywhere). Partial-period depreciation
uses whole months (7/12 for the old machine through Aug 1; 5/12 for the new
machine from Aug 1 to Dec 31). Building depreciation for 20X7 follows the
stated simplifying assumption: a full year of revised depreciation computed on
post-expenditure book value over the new remaining life.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---------- given data ----------
bldg_cost      = Decimal("2400000")
bldg_ad_jan1   = Decimal("960000")
bldg_life_jan1 = Decimal("12")
bldg_resid     = Decimal("0")

mach_cost      = Decimal("84000")
mach_ad_jan1   = Decimal("60000")
mach_life_jan1 = Decimal("2")
mach_resid     = Decimal("0")

budget_overhaul = Decimal("180000")   # planned major maintenance (event 1)
upgrade_cost    = Decimal("192000")   # Aug 1 electrical modernization
life_extension  = Decimal("4")
proceeds_old    = Decimal("2000")
new_mach_cost   = Decimal("96000")
new_mach_life   = Decimal("8")
new_mach_resid  = Decimal("0")
months_to_disposal = Decimal("7")     # Jan 1 -> Aug 1
months_new_held    = Decimal("5")     # Aug 1 -> Dec 31

# ---------- (a) planned major maintenance ----------
jan_entry_amount = Decimal("0")       # no present obligation -> no accrual

# ---------- (b) reduction of accumulated depreciation ----------
bldg_bv_jan1   = q(bldg_cost - bldg_ad_jan1)
bldg_dep_pre   = q((bldg_bv_jan1 - bldg_resid) / bldg_life_jan1)   # ties to $120,000
bldg_ad_aug1   = q(bldg_ad_jan1 - upgrade_cost)
bldg_bv_aug1   = q(bldg_cost - bldg_ad_aug1)
bldg_life_new  = bldg_life_jan1 + life_extension
bldg_dep_20x7  = q((bldg_bv_aug1 - bldg_resid) / bldg_life_new)
bldg_ad_dec31  = q(bldg_ad_aug1 + bldg_dep_20x7)
bldg_bv_dec31  = q(bldg_cost - bldg_ad_dec31)

# ---------- (c) capitalization alternative ----------
cap_cost_aug1  = q(bldg_cost + upgrade_cost)
cap_bv_aug1    = q(cap_cost_aug1 - bldg_ad_jan1)
cap_dep_20x7   = q((cap_bv_aug1 - bldg_resid) / bldg_life_new)
cap_ad_dec31   = q(bldg_ad_jan1 + cap_dep_20x7)
cap_bv_dec31   = q(cap_cost_aug1 - cap_ad_dec31)
dep_difference = q(cap_dep_20x7 - bldg_dep_20x7)
gross_cost_diff = q(cap_cost_aug1 - bldg_cost)
ad_diff_dec31   = q(cap_ad_dec31 - bldg_ad_dec31)
bv_diff_dec31   = q(cap_bv_dec31 - bldg_bv_dec31)

# ---------- (d) old machine: update, dispose; new machine capitalized ----------
mach_bv_jan1   = q(mach_cost - mach_ad_jan1)
mach_dep_ann   = q((mach_bv_jan1 - mach_resid) / mach_life_jan1)
mach_dep_stub  = q(mach_dep_ann * months_to_disposal / Decimal("12"))
mach_ad_disp   = q(mach_ad_jan1 + mach_dep_stub)
mach_bv_disp   = q(mach_cost - mach_ad_disp)
gain_loss      = q(proceeds_old - mach_bv_disp)      # negative => loss
loss_on_disp   = q(-gain_loss) if gain_loss < 0 else Decimal("0")
gain_on_disp   = gain_loss if gain_loss > 0 else Decimal("0")

# ---------- (e) new machine period-end depreciation + snapshot ----------
new_dep_ann    = q((new_mach_cost - new_mach_resid) / new_mach_life)
new_dep_20x7   = q(new_dep_ann * months_new_held / Decimal("12"))
new_ad_dec31   = new_dep_20x7
new_bv_dec31   = q(new_mach_cost - new_ad_dec31)
new_months_rem = int(new_mach_life * 12 - months_new_held)
new_years_rem  = (Decimal(new_months_rem) / Decimal("12")).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)

answers = [
 {"label":"a: Journal entry required in January (or before overhaul begins) for the $180,000 planned major maintenance budget — none; planned future maintenance is not a present obligation and may not be accrued in advance; the cost is recorded only when incurred. Amount recorded in January ($)","value":n(jan_entry_amount)},
 {"label":"b: Building accumulated depreciation immediately after Aug 1 reduction ($)","value":n(bldg_ad_aug1)},
 {"label":"b: Building book value immediately after Aug 1 expenditure ($)","value":n(bldg_bv_aug1)},
 {"label":"b: New remaining useful life of building (years)","value":n(bldg_life_new)},
 {"label":"b: Revised full-year 20X7 building depreciation ($)","value":n(bldg_dep_20x7)},
 {"label":"c: Building gross cost after Aug 1 under capitalization method ($)","value":n(cap_cost_aug1)},
 {"label":"c: Building book value immediately after Aug 1 under capitalization method ($)","value":n(cap_bv_aug1)},
 {"label":"c: 20X7 building depreciation expense under capitalization method ($)","value":n(cap_dep_20x7)},
 {"label":"c: Difference in 20X7 depreciation expense, capitalization vs reduction of accumulated depreciation ($)","value":n(dep_difference)},
 {"label":"c: Dec 31, 20X7 balance-sheet gross cost — reduction method ($)","value":n(bldg_cost)},
 {"label":"c: Dec 31, 20X7 balance-sheet gross cost — capitalization method ($)","value":n(cap_cost_aug1)},
 {"label":"c: Dec 31, 20X7 accumulated depreciation — reduction method ($)","value":n(bldg_ad_dec31)},
 {"label":"c: Dec 31, 20X7 accumulated depreciation — capitalization method ($)","value":n(cap_ad_dec31)},
 {"label":"c: Dec 31, 20X7 building carrying amount — reduction method ($)","value":n(bldg_bv_dec31)},
 {"label":"c: Dec 31, 20X7 building carrying amount — capitalization method ($)","value":n(cap_bv_dec31)},
 {"label":"c: Difference in Dec 31, 20X7 carrying amount between the two methods ($)","value":n(bv_diff_dec31)},
 {"label":"c: Presentation contrast — gross cost is higher under capitalization by ($)","value":n(gross_cost_diff)},
 {"label":"c: Presentation contrast — accumulated depreciation is higher under capitalization by ($)","value":n(ad_diff_dec31)},
 {"label":"d: Old machine depreciation update through Aug 1 (7/12 of $%s annual) ($)" % n(mach_dep_ann),"value":n(mach_dep_stub)},
 {"label":"d: Old machine accumulated depreciation at Aug 1 disposal date ($)","value":n(mach_ad_disp)},
 {"label":"d: Old machine book value at Aug 1 disposal date ($)","value":n(mach_bv_disp)},
 {"label":"d: Proceeds on sale of old machine ($)","value":n(proceeds_old)},
 {"label":"d: Loss on disposal of old machine ($)","value":n(loss_on_disp)},
 {"label":"d: Cost capitalized for new machine ($)","value":n(new_mach_cost)},
 {"label":"e: New machine annual (full-year) depreciation ($)","value":n(new_dep_ann)},
 {"label":"e: Dec 31, 20X7 period-end depreciation expense on new machine (5/12) ($)","value":n(new_dep_20x7)},
 {"label":"e: New machine snapshot Dec 31, 20X7 — cost ($)","value":n(new_mach_cost)},
 {"label":"e: New machine snapshot Dec 31, 20X7 — accumulated depreciation ($)","value":n(new_ad_dec31)},
 {"label":"e: New machine snapshot Dec 31, 20X7 — carrying amount / book value ($)","value":n(new_bv_dec31)},
 {"label":"e: New machine snapshot Dec 31, 20X7 — remaining useful life (months)","value":new_months_rem},
 {"label":"e: New machine snapshot Dec 31, 20X7 — remaining useful life (years)","value":float(new_years_rem)},
 {"label":"f: Building schedule — Jan 1, 20X7 cost ($)","value":n(bldg_cost)},
 {"label":"f: Building schedule — Jan 1, 20X7 accumulated depreciation ($)","value":n(bldg_ad_jan1)},
 {"label":"f: Building schedule — Jan 1, 20X7 book value ($)","value":n(bldg_bv_jan1)},
 {"label":"f: Building schedule — Aug 1 electrical modernization: reduction of accumulated depreciation ($)","value":n(upgrade_cost)},
 {"label":"f: Building schedule — Aug 1, 20X7 cost after expenditure (unchanged) ($)","value":n(bldg_cost)},
 {"label":"f: Building schedule — Aug 1, 20X7 accumulated depreciation after expenditure ($)","value":n(bldg_ad_aug1)},
 {"label":"f: Building schedule — Aug 1, 20X7 book value after expenditure ($)","value":n(bldg_bv_aug1)},
 {"label":"f: Building schedule — 20X7 depreciation expense recorded Dec 31 ($)","value":n(bldg_dep_20x7)},
 {"label":"f: Building schedule — Dec 31, 20X7 cost ($)","value":n(bldg_cost)},
 {"label":"f: Building schedule — Dec 31, 20X7 accumulated depreciation ($)","value":n(bldg_ad_dec31)},
 {"label":"f: Building schedule — Dec 31, 20X7 book value ($)","value":n(bldg_bv_dec31)},
 {"label":"f: Building schedule — remaining useful life at Dec 31, 20X7 (years)","value":n(bldg_life_new - Decimal('1'))},
]

def E(part, desc, lines):
    tot_d = sum(q(l[1]) for l in lines)
    tot_c = sum(q(l[2]) for l in lines)
    assert tot_d == tot_c, (part, desc, tot_d, tot_c)
    return {"part": part, "description": desc,
            "lines": [{"account": a, "debit": n(d), "credit": n(c)} for a, d, c in lines]}

Z = Decimal("0")
journal_entries = [
 E("a","January 20X7 — planned major maintenance budget: NO journal entry (memo only; future maintenance cannot be accrued in advance)",
   [("No entry required (memorandum only)", Z, Z)]),
 E("b","Aug 1, 20X7 — electrical system modernization, reduction of accumulated depreciation method",
   [("Accumulated Depreciation — Building", upgrade_cost, Z),
    ("Cash", Z, upgrade_cost)]),
 E("b","Dec 31, 20X7 — period-end adjusting entry, building depreciation (revised full year)",
   [("Depreciation Expense — Building", bldg_dep_20x7, Z),
    ("Accumulated Depreciation — Building", Z, bldg_dep_20x7)]),
 E("c","Alternative — Aug 1, 20X7 electrical system modernization under the capitalization method",
   [("Building", upgrade_cost, Z),
    ("Cash", Z, upgrade_cost)]),
 E("c","Alternative — Dec 31, 20X7 period-end adjusting entry under the capitalization method (same expense)",
   [("Depreciation Expense — Building", cap_dep_20x7, Z),
    ("Accumulated Depreciation — Building", Z, cap_dep_20x7)]),
 E("d","Aug 1, 20X7 — update depreciation on old machine through disposal date (7/12)",
   [("Depreciation Expense — Machine", mach_dep_stub, Z),
    ("Accumulated Depreciation — Machine", Z, mach_dep_stub)]),
 E("d","Aug 1, 20X7 — disposal (sale) of old production machine",
   [("Cash", proceeds_old, Z),
    ("Accumulated Depreciation — Machine", mach_ad_disp, Z),
    ("Loss on Disposal of Machine", loss_on_disp, Z),
    ("Machine (old)", Z, mach_cost)]),
 E("d","Aug 1, 20X7 — purchase / capitalization of new production machine",
   [("Machine (new)", new_mach_cost, Z),
    ("Cash", Z, new_mach_cost)]),
 E("e","Dec 31, 20X7 — period-end adjusting entry, depreciation on new machine (5/12)",
   [("Depreciation Expense — Machine", new_dep_20x7, Z),
    ("Accumulated Depreciation — Machine", Z, new_dep_20x7)]),
]

out = {
 "id": "agent_333#02",
 "rounding_convention": "decimal.Decimal throughout (no floats); every amount quantized to the cent with ROUND_HALF_UP, once per period/figure. Partial periods by whole months: old machine 7/12 through Aug 1 disposal, new machine 5/12 from Aug 1; building uses the stated full-year revised-depreciation simplifying assumption.",
 "answers": answers,
 "journal_entries": journal_entries,
 "insufficient_info": False,
 "notes": "(a) No entry: a planned future overhaul is not a present obligation at Jan 1 and future maintenance/overhaul costs may not be accrued in advance; the $180,000 budget is a memo item and cost is recognized only when the work is performed (capitalized if it meets the betterment criteria, otherwise expensed). (b) Life extension with untracked old component cost => reduction of accumulated depreciation: Dr Accum. Dep. $192,000; post-expenditure BV $1,632,000 over 16 years = $102,000 full-year 20X7 depreciation. (c) Capitalization gives identical BV ($1,632,000) and identical $102,000 expense; only presentation differs — gross cost $2,592,000 vs $2,400,000 and accumulated depreciation $1,062,000 vs $870,000 at Dec 31, with the same $1,530,000 carrying amount. (d) Old machine BV at Aug 1 $17,000 vs $2,000 proceeds = $15,000 loss. (e) New machine $96,000/8 = $12,000 per year x 5/12 = $5,000 for 20X7; BV $91,000 with 91 months (7.583 years) of life remaining."
}
print(json.dumps(out, indent=1))
