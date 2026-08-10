"""Northline Processors Corp. — LO 11-6 alternate angle.

Rounding convention: decimal.Decimal throughout (no floats); every amount is
quantized to whole dollars with ROUND_HALF_UP once per period / per computed
figure.  Journal entries are stated in whole dollars; underlying straight-line
rates are carried at full Decimal precision and rounded only at the point of
recognition.  The building schedule closes exactly to the Dec 31 book value
and the machine snapshot closes exactly to cost less accumulated depreciation.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

D = Decimal
CENT = D("1")


def r(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def n(x):
    x = r(x)
    return int(x)


# ---------------------------------------------------------------- given facts
bldg_cost = D("2400000")
bldg_ad_jan1 = D("960000")
bldg_life_rem_jan1 = D("12")
bldg_residual = D("0")

mach_cost = D("84000")
mach_ad_jan1 = D("60000")
mach_life_rem_jan1 = D("2")
mach_residual = D("0")

budget_overhaul = D("180000")          # planned major maintenance budget
upgrade_cost = D("192000")             # Aug 1 electrical modernization
life_extension_yrs = D("4")
proceeds_old = D("2000")
new_mach_cost = D("96000")
new_mach_life = D("8")
new_mach_residual = D("0")

months_to_aug1 = D("7")                # Jan 1 -> Aug 1
months_aug1_to_dec31 = D("5")
MONTHS = D("12")

# --------------------------------------------------- derive & tie to the givens
bldg_bv_jan1 = bldg_cost - bldg_ad_jan1
bldg_dep_prechange = r((bldg_bv_jan1 - bldg_residual) / bldg_life_rem_jan1)
assert bldg_bv_jan1 == D("1440000") and bldg_dep_prechange == D("120000")

mach_bv_jan1 = mach_cost - mach_ad_jan1
mach_dep_annual = r((mach_bv_jan1 - mach_residual) / mach_life_rem_jan1)
assert mach_bv_jan1 == D("24000") and mach_dep_annual == D("12000")

# ------------------------------------------------------------------- part (a)
jan_entry_amount = D("0")   # planned major maintenance may NOT be accrued in advance

# ------------------------------------------------------------------- part (b)
# Reduction-of-accumulated-depreciation method: debit Accum. Dep., not the asset.
bldg_ad_after_upgrade = bldg_ad_jan1 - upgrade_cost
bldg_bv_after_upgrade = bldg_cost - bldg_ad_after_upgrade
bldg_life_revised = bldg_life_rem_jan1 + life_extension_yrs
bldg_dep_20x7 = r((bldg_bv_after_upgrade - bldg_residual) / bldg_life_revised)

# ------------------------------------------------------------------- part (c)
# Capitalization method: debit the asset. Same post-expenditure BV and life.
cap_cost_dec31 = bldg_cost + upgrade_cost
cap_bv_after_upgrade = cap_cost_dec31 - bldg_ad_jan1
cap_dep_20x7 = r((cap_bv_after_upgrade - bldg_residual) / bldg_life_revised)
assert cap_bv_after_upgrade == bldg_bv_after_upgrade and cap_dep_20x7 == bldg_dep_20x7
cap_ad_dec31 = bldg_ad_jan1 + cap_dep_20x7
cap_bv_dec31 = cap_cost_dec31 - cap_ad_dec31

red_cost_dec31 = bldg_cost
red_ad_dec31 = bldg_ad_after_upgrade + bldg_dep_20x7
red_bv_dec31 = red_cost_dec31 - red_ad_dec31
assert red_bv_dec31 == cap_bv_dec31

# ------------------------------------------------------------------- part (d)
dep_old_to_aug1 = r(mach_dep_annual * months_to_aug1 / MONTHS)
mach_ad_at_disposal = mach_ad_jan1 + dep_old_to_aug1
mach_bv_at_disposal = mach_cost - mach_ad_at_disposal
gain_loss = proceeds_old - mach_bv_at_disposal            # negative => loss
loss_on_disposal = -gain_loss

# ------------------------------------------------------------------- part (e)
new_dep_annual = r((new_mach_cost - new_mach_residual) / new_mach_life)
new_dep_20x7 = r(new_dep_annual * months_aug1_to_dec31 / MONTHS)
new_ad_dec31 = new_dep_20x7
new_bv_dec31 = new_mach_cost - new_ad_dec31

# ------------------------------------------------------------------- part (f)
sched_open_cost, sched_open_ad, sched_open_bv = bldg_cost, bldg_ad_jan1, bldg_bv_jan1
sched_aug_ad, sched_aug_bv = bldg_ad_after_upgrade, bldg_bv_after_upgrade
sched_close_ad, sched_close_bv = red_ad_dec31, red_bv_dec31
assert sched_close_bv == sched_aug_bv - bldg_dep_20x7          # schedule closes exactly

answers = [
    {"label": "a: journal entry amount required in January for the planned major maintenance budget",
     "value": n(jan_entry_amount)},

    {"label": "b: Aug 1 debit to Accumulated Depreciation-Building (reduction method)",
     "value": n(upgrade_cost)},
    {"label": "b: Aug 1 credit to Cash", "value": n(upgrade_cost)},
    {"label": "b: building accumulated depreciation immediately after the Aug 1 expenditure",
     "value": n(bldg_ad_after_upgrade)},
    {"label": "b: building book value immediately after the Aug 1 expenditure",
     "value": n(bldg_bv_after_upgrade)},
    {"label": "b: revised remaining useful life (years)", "value": n(bldg_life_revised)},
    {"label": "b: revised full-year 20X7 building depreciation expense", "value": n(bldg_dep_20x7)},

    {"label": "c: Aug 1 debit to Building under the capitalization method", "value": n(upgrade_cost)},
    {"label": "c: 20X7 building depreciation expense under the capitalization method",
     "value": n(cap_dep_20x7)},
    {"label": "c: Dec 31 building gross cost - capitalization method", "value": n(cap_cost_dec31)},
    {"label": "c: Dec 31 building accumulated depreciation - capitalization method",
     "value": n(cap_ad_dec31)},
    {"label": "c: Dec 31 building net book value - capitalization method", "value": n(cap_bv_dec31)},
    {"label": "c: Dec 31 building gross cost - reduction of accumulated depreciation method",
     "value": n(red_cost_dec31)},
    {"label": "c: Dec 31 building accumulated depreciation - reduction method",
     "value": n(red_ad_dec31)},
    {"label": "c: Dec 31 building net book value - reduction method", "value": n(red_bv_dec31)},

    {"label": "d: depreciation on the old machine Jan 1 through Aug 1 (7/12 of $12,000)",
     "value": n(dep_old_to_aug1)},
    {"label": "d: old machine accumulated depreciation at Aug 1 disposal date",
     "value": n(mach_ad_at_disposal)},
    {"label": "d: old machine book value at Aug 1 disposal date", "value": n(mach_bv_at_disposal)},
    {"label": "d: cash proceeds on sale of the old machine", "value": n(proceeds_old)},
    {"label": "d: loss on disposal of the old machine", "value": n(loss_on_disposal)},
    {"label": "d: cost capitalized for the new machine", "value": n(new_mach_cost)},

    {"label": "e: new machine full-year straight-line depreciation", "value": n(new_dep_annual)},
    {"label": "e: Dec 31 20X7 depreciation expense on the new machine (5/12)", "value": n(new_dep_20x7)},
    {"label": "e: new machine snapshot Dec 31 20X7 - cost", "value": n(new_mach_cost)},
    {"label": "e: new machine snapshot Dec 31 20X7 - accumulated depreciation", "value": n(new_ad_dec31)},
    {"label": "e: new machine snapshot Dec 31 20X7 - book value", "value": n(new_bv_dec31)},

    {"label": "f: Jan 1 20X7 building cost", "value": n(sched_open_cost)},
    {"label": "f: Jan 1 20X7 building accumulated depreciation", "value": n(sched_open_ad)},
    {"label": "f: Jan 1 20X7 building book value", "value": n(sched_open_bv)},
    {"label": "f: Aug 1 reduction of accumulated depreciation for the modernization",
     "value": n(upgrade_cost)},
    {"label": "f: Aug 1 building accumulated depreciation after the modernization",
     "value": n(sched_aug_ad)},
    {"label": "f: Aug 1 building book value after the modernization", "value": n(sched_aug_bv)},
    {"label": "f: Dec 31 20X7 building depreciation expense", "value": n(bldg_dep_20x7)},
    {"label": "f: Dec 31 20X7 building accumulated depreciation", "value": n(sched_close_ad)},
    {"label": "f: Dec 31 20X7 building book value", "value": n(sched_close_bv)},
]


def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": n(dr) if dr is not None else 0,
            "credit": n(cr) if cr is not None else 0}


journal_entries = [
    {"part": "b", "lines": [
        L("Accumulated Depreciation-Building (Aug 1, electrical modernization)", dr=upgrade_cost),
        L("Cash", cr=upgrade_cost)]},
    {"part": "b", "lines": [
        L("Depreciation Expense-Building (Dec 31 period-end adjusting entry)", dr=bldg_dep_20x7),
        L("Accumulated Depreciation-Building", cr=bldg_dep_20x7)]},
    {"part": "c", "lines": [
        L("Building (Aug 1, electrical modernization capitalized)", dr=upgrade_cost),
        L("Cash", cr=upgrade_cost)]},
    {"part": "c", "lines": [
        L("Depreciation Expense-Building (Dec 31, capitalization alternative)", dr=cap_dep_20x7),
        L("Accumulated Depreciation-Building", cr=cap_dep_20x7)]},
    {"part": "d", "lines": [
        L("Depreciation Expense-Machinery (old machine, Jan 1-Aug 1)", dr=dep_old_to_aug1),
        L("Accumulated Depreciation-Machinery", cr=dep_old_to_aug1)]},
    {"part": "d", "lines": [
        L("Cash", dr=proceeds_old),
        L("Accumulated Depreciation-Machinery (old machine)", dr=mach_ad_at_disposal),
        L("Loss on Disposal of Machinery", dr=loss_on_disposal),
        L("Machinery (old machine)", cr=mach_cost)]},
    {"part": "d", "lines": [
        L("Machinery (new machine)", dr=new_mach_cost),
        L("Cash", cr=new_mach_cost)]},
    {"part": "e", "lines": [
        L("Depreciation Expense-Machinery (Dec 31, new machine, 5/12)", dr=new_dep_20x7),
        L("Accumulated Depreciation-Machinery", cr=new_dep_20x7)]},
]

for je in journal_entries:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"]), je

notes = (
    "(a) No entry. A planned major maintenance overhaul is a future event, not a present "
    "obligation at the balance-sheet date; the accrue-in-advance method is prohibited, so the "
    "$180,000 budget is memorandum only and costs are recognized when the overhaul work is done. "
    "(b) Life extension with untracked old component costs and improved quality NOT the primary "
    "result => reduction of accumulated depreciation: Dr Accum. Dep. $192,000 / Cr Cash $192,000. "
    "AD falls to $768,000, BV rises to $1,632,000, revised life 12+4=16 yrs, and under the stated "
    "simplifying assumption full-year 20X7 depreciation = $1,632,000/16 = $102,000. "
    "(c) Capitalization debits Building instead, giving the same post-expenditure BV ($1,632,000) "
    "and the same $102,000 expense. Balance-sheet contrast only: capitalization shows gross cost "
    "$2,592,000 less AD $1,062,000; the reduction method shows gross cost $2,400,000 less AD "
    "$870,000. Both net to $1,530,000. "
    "(d) Old machine depreciation is updated to the disposal date (7/12 x $12,000 = $7,000), AD "
    "$67,000, BV $17,000, sold for $2,000 => $15,000 loss. "
    "(e) New machine $96,000/8 = $12,000 per year x 5/12 (Aug 1-Dec 31) = $5,000; snapshot cost "
    "$96,000, AD $5,000, BV $91,000 (remaining life 7 yrs 7 mos). "
    "Total 20X7 machinery depreciation expense is $7,000 + $5,000 = $12,000. "
    "All amounts are exact whole dollars; no rounding difference arose, and the building schedule "
    "and machine snapshot both close exactly."
)

print(json.dumps({
    "id": "agent_333#02",
    "rounding_convention": "decimal.Decimal only (no floats); ROUND_HALF_UP to whole dollars once per period/figure; straight-line rates carried at full precision, rounded at recognition; schedules close exactly to book value",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
