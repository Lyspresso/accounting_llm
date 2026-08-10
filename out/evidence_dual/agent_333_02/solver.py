"""Independent (second) cold derivation of agent_333#02 — Northline Processors Corp., 20X7.

LO 11-6: subsequent measurement / betterments.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Every amount is quantized to whole dollars with
ROUND_HALF_UP, applied period-by-period (each period's depreciation is rounded
as it is computed, never carried as an unrounded residual). No floats anywhere.
Schedules close exactly: the building schedule's Dec 31 book value is proved to
equal cost less accumulated depreciation, and the new machine's snapshot proves
cost - accum. dep. = book value. Nothing is hard-coded: every figure below is
computed from the stem's facts (the stem's stated $120,000 pre-change building
depreciation and $12,000 machine depreciation are recomputed and cross-checked,
not assumed).
"""

from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal
CENT0 = C("1")


def d(x):
    """Quantize to whole dollars, ROUND_HALF_UP."""
    return C(x).quantize(CENT0, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- stem facts
# Building at Jan 1, 20X7
bld_cost_0 = C("2400000")
bld_ad_0 = C("960000")
bld_life_0 = C("12")          # remaining useful life, years
bld_residual = C("0")
bld_stated_annual_dep = C("120000")   # given; recomputed below as a check

# Production machine (separate asset) at Jan 1, 20X7
mach_cost = C("84000")
mach_ad_0 = C("60000")
mach_life_0 = C("2")
mach_residual = C("0")
mach_stated_annual_dep = C("12000")   # given; recomputed below as a check

# Events in 20X7
maint_budget = C("180000")            # planned August overhaul, budgeted in January
elec_cost = C("192000")               # Aug 1 electrical modernization, cash
life_extension_yrs = C("4")
months_in_year = C("12")
disposal_month = C("8")               # August 1
months_old_mach_held = disposal_month - C("1")     # Jan 1 -> Aug 1 = 7 months
months_new_mach_held = months_in_year - months_old_mach_held   # Aug 1 -> Dec 31 = 5
old_mach_proceeds = C("2000")
new_mach_cost = C("96000")
new_mach_life = C("8")
new_mach_residual = C("0")

answers = []
jes = []


def A(label, value):
    answers.append({"label": label, "value": value})


def JE(part, lines, memo=None):
    dr = sum((C(l["debit"]) for l in lines), C("0"))
    cr = sum((C(l["credit"]) for l in lines), C("0"))
    assert dr == cr, (part, dr, cr)
    e = {"part": part, "lines": lines}
    if memo:
        e["memo"] = memo
    jes.append(e)


def L(acct, debit=C("0"), credit=C("0")):
    return {"account": acct, "debit": float(d(debit)), "credit": float(d(credit))}


# ------------------------------------------------- cross-checks on the givens
bld_bv_0 = d(bld_cost_0 - bld_ad_0)
bld_annual_dep_pre = d((bld_bv_0 - bld_residual) / bld_life_0)
assert bld_annual_dep_pre == bld_stated_annual_dep, bld_annual_dep_pre

mach_bv_0 = d(mach_cost - mach_ad_0)
mach_annual_dep = d((mach_bv_0 - mach_residual) / mach_life_0)
assert mach_annual_dep == mach_stated_annual_dep, mach_annual_dep

A("check: building Jan 1, 20X7 book value = cost - accum. dep.", float(bld_bv_0))
A("check: building pre-change annual depreciation = BV / remaining life (straight line)",
  float(bld_annual_dep_pre))
A("check: machine Jan 1, 20X7 book value = cost - accum. dep.", float(mach_bv_0))
A("check: old machine annual depreciation = BV / remaining life", float(mach_annual_dep))

# ---------------------------------------------------------------------- (a)
# A planned major maintenance overhaul is a FUTURE event. At January there is no
# past transaction or event creating a present obligation (the entity could sell
# the building or forgo the overhaul), so no liability and no expense may be
# recognized. Accruing/providing in advance for planned major maintenance is
# prohibited; the cost is recognized only when incurred (then expensed as a
# repair, or capitalized if it is a betterment). Budgeting is not an accountable
# event. Dollar amount of any January entry:
jan_entry_amount = C("0")
A("a: journal entry required in January for the planned major maintenance budget? "
  "(0 = no entry / no amount recognized)", float(d(jan_entry_amount)))
A("a: liability accrued in January for the planned $180,000 overhaul", float(d(C("0"))))
A("a: expense recognized in January for the planned $180,000 overhaul", float(d(C("0"))))
A("a: the budgeted overhaul amount that remains merely a budget figure (no JE)",
  float(d(maint_budget)))
JE("a", [L("No entry required (memorandum only: $180,000 budget is not an accountable event)",
           C("0"), C("0"))],
   memo="No JE. No past event -> no present obligation; accruing planned major "
        "maintenance in advance is not permitted. Recognize only when incurred.")

# ---------------------------------------------------------------------- (b)
# Reduction of accumulated depreciation method: the life-extending betterment is
# debited to Accumulated Depreciation (old component cost is not separately
# tracked, and life extension - not improved output quality - is the primary
# result), so the asset's gross cost is unchanged.
JE("b", [L("Accumulated Depreciation - Building", debit=elec_cost),
         L("Cash", credit=elec_cost)],
   memo="Aug 1 electrical modernization, $192,000, charged against accumulated "
        "depreciation (life extension; reduction-of-accumulated-depreciation method).")

bld_ad_after_elec = d(bld_ad_0 - elec_cost)
bld_bv_after_elec = d(bld_cost_0 - bld_ad_after_elec)
assert bld_bv_after_elec == d(bld_bv_0 + elec_cost)
bld_life_new = bld_life_0 + life_extension_yrs
bld_annual_dep_rev = d((bld_bv_after_elec - bld_residual) / bld_life_new)

A("b: debit to Accumulated Depreciation - Building on Aug 1", float(d(elec_cost)))
A("b: credit to Cash on Aug 1", float(d(elec_cost)))
A("b: building gross cost after the Aug 1 entry (unchanged)", float(d(bld_cost_0)))
A("b: building accumulated depreciation immediately after the Aug 1 entry "
  "(960,000 - 192,000)", float(bld_ad_after_elec))
A("b: building book value immediately after the Aug 1 expenditure", float(bld_bv_after_elec))
A("b: revised remaining useful life of the building (12 + 4)", float(bld_life_new))
A("b: revised FULL-YEAR 20X7 building depreciation (post-expenditure BV / 16 yrs)",
  float(bld_annual_dep_rev))
A("b: increase/(decrease) in annual building depreciation vs pre-change $120,000",
  float(d(bld_annual_dep_rev - bld_annual_dep_pre)))
JE("b-dec31", [L("Depreciation Expense - Building", debit=bld_annual_dep_rev),
               L("Accumulated Depreciation - Building", credit=bld_annual_dep_rev)],
   memo="Dec 31, 20X7 period-end adjusting entry - revised building depreciation.")

bld_ad_dec31_red = d(bld_ad_after_elec + bld_annual_dep_rev)
bld_bv_dec31 = d(bld_cost_0 - bld_ad_dec31_red)
A("b: building accumulated depreciation at Dec 31, 20X7 (reduction method)",
  float(bld_ad_dec31_red))
A("b: building book value at Dec 31, 20X7", float(bld_bv_dec31))

# ---------------------------------------------------------------------- (c)
# Capitalization alternative: debit the asset account instead.
JE("c", [L("Building", debit=elec_cost),
         L("Cash", credit=elec_cost)],
   memo="Alternative presentation - Aug 1 modernization capitalized to the asset account.")

bld_cost_cap = d(bld_cost_0 + elec_cost)
bld_ad_cap_after = d(bld_ad_0)                    # unchanged by the expenditure
bld_bv_cap_after = d(bld_cost_cap - bld_ad_cap_after)
bld_annual_dep_cap = d((bld_bv_cap_after - bld_residual) / bld_life_new)
assert bld_bv_cap_after == bld_bv_after_elec
assert bld_annual_dep_cap == bld_annual_dep_rev

A("c: building gross cost after Aug 1 under capitalization (2,400,000 + 192,000)",
  float(bld_cost_cap))
A("c: building accumulated depreciation after Aug 1 under capitalization (unchanged)",
  float(bld_ad_cap_after))
A("c: building book value after Aug 1 under capitalization (identical to (b))",
  float(bld_bv_cap_after))
A("c: 20X7 depreciation expense under capitalization (same BV, same 16-year life)",
  float(bld_annual_dep_cap))
A("c: difference in 20X7 depreciation expense between the two methods",
  float(d(bld_annual_dep_cap - bld_annual_dep_rev)))
JE("c-dec31", [L("Depreciation Expense - Building", debit=bld_annual_dep_cap),
               L("Accumulated Depreciation - Building", credit=bld_annual_dep_cap)],
   memo="Dec 31 under the capitalization alternative - identical amount.")

bld_ad_dec31_cap = d(bld_ad_cap_after + bld_annual_dep_cap)
bld_bv_dec31_cap = d(bld_cost_cap - bld_ad_dec31_cap)
assert bld_bv_dec31_cap == bld_bv_dec31
A("c: Dec 31 balance sheet - gross cost, reduction method", float(d(bld_cost_0)))
A("c: Dec 31 balance sheet - accumulated depreciation, reduction method",
  float(bld_ad_dec31_red))
A("c: Dec 31 balance sheet - gross cost, capitalization method", float(bld_cost_cap))
A("c: Dec 31 balance sheet - accumulated depreciation, capitalization method",
  float(bld_ad_dec31_cap))
A("c: Dec 31 net book value under BOTH methods (identical)", float(bld_bv_dec31))
A("c: gross-cost presentation difference (capitalization - reduction)",
  float(d(bld_cost_cap - bld_cost_0)))
A("c: accumulated-depreciation presentation difference (capitalization - reduction)",
  float(d(bld_ad_dec31_cap - bld_ad_dec31_red)))

# ---------------------------------------------------------------------- (d)
mach_dep_to_disposal = d(mach_annual_dep * months_old_mach_held / months_in_year)
mach_ad_at_disposal = d(mach_ad_0 + mach_dep_to_disposal)
mach_bv_at_disposal = d(mach_cost - mach_ad_at_disposal)
gain_loss = d(old_mach_proceeds - mach_bv_at_disposal)   # negative => loss
loss_on_disposal = d(-gain_loss) if gain_loss < 0 else C("0")
gain_on_disposal = gain_loss if gain_loss > 0 else C("0")

A("d: months of depreciation on the old machine in 20X7 (Jan 1 -> Aug 1)",
  float(months_old_mach_held))
A("d: depreciation update on the old machine through Aug 1 (7/12 x 12,000)",
  float(mach_dep_to_disposal))
A("d: old machine accumulated depreciation at Aug 1 (after the update)",
  float(mach_ad_at_disposal))
A("d: old machine book value at the disposal date", float(mach_bv_at_disposal))
A("d: cash proceeds on sale of the old machine", float(d(old_mach_proceeds)))
A("d: loss on disposal of the old machine (BV 17,000 - proceeds 2,000)",
  float(loss_on_disposal))
A("d: gain on disposal of the old machine", float(gain_on_disposal))
A("d: cost capitalized for the new machine", float(d(new_mach_cost)))
A("d: total cash paid Aug 1 (modernization + new machine)",
  float(d(elec_cost + new_mach_cost)))
A("d: net cash outflow Aug 1 (modernization + new machine - proceeds)",
  float(d(elec_cost + new_mach_cost - old_mach_proceeds)))

JE("d-1", [L("Depreciation Expense - Machinery", debit=mach_dep_to_disposal),
           L("Accumulated Depreciation - Machinery", credit=mach_dep_to_disposal)],
   memo="Aug 1 - update depreciation on the old machine through the disposal date "
        "(7/12 x $12,000).")

disposal_lines = [L("Cash", debit=old_mach_proceeds),
                  L("Accumulated Depreciation - Machinery", debit=mach_ad_at_disposal)]
if loss_on_disposal > 0:
    disposal_lines.append(L("Loss on Disposal of Machinery", debit=loss_on_disposal))
disposal_lines.append(L("Machinery (old)", credit=mach_cost))
if gain_on_disposal > 0:
    disposal_lines.append(L("Gain on Disposal of Machinery", credit=gain_on_disposal))
JE("d-2", disposal_lines, memo="Aug 1 - sell the old machine for $2,000 cash; remove "
                              "cost and accumulated depreciation; recognize the loss.")

JE("d-3", [L("Machinery (new)", debit=new_mach_cost),
           L("Cash", credit=new_mach_cost)],
   memo="Aug 1 - purchase the replacement machine for $96,000 cash.")

# ---------------------------------------------------------------------- (e)
new_mach_annual_dep = d((new_mach_cost - new_mach_residual) / new_mach_life)
new_mach_dep_20x7 = d(new_mach_annual_dep * months_new_mach_held / months_in_year)
new_mach_ad_dec31 = d(new_mach_dep_20x7)
new_mach_bv_dec31 = d(new_mach_cost - new_mach_ad_dec31)
new_mach_months_total = d(new_mach_life * months_in_year)
new_mach_months_remaining = d(new_mach_months_total - months_new_mach_held)

A("e: new machine full-year (annual) depreciation (96,000 / 8)", float(new_mach_annual_dep))
A("e: months the new machine was held in 20X7 (Aug 1 -> Dec 31)",
  float(months_new_mach_held))
A("e: new machine 20X7 depreciation expense (5/12 x 12,000)", float(new_mach_dep_20x7))
A("e: new machine cost at Dec 31, 20X7", float(d(new_mach_cost)))
A("e: new machine accumulated depreciation at Dec 31, 20X7", float(new_mach_ad_dec31))
A("e: new machine book value (carrying amount) at Dec 31, 20X7", float(new_mach_bv_dec31))
A("e: new machine remaining useful life at Dec 31, 20X7, in months",
  float(new_mach_months_remaining))
A("e: new machine remaining useful life at Dec 31, 20X7, in years (91/12)",
  float((new_mach_months_remaining / months_in_year).quantize(C("0.001"),
                                                             rounding=ROUND_HALF_UP)))
A("e: new machine residual value", float(d(new_mach_residual)))
A("e: new machine monthly depreciation (12,000 / 12)",
  float(d(new_mach_annual_dep / months_in_year)))
JE("e", [L("Depreciation Expense - Machinery", debit=new_mach_dep_20x7),
         L("Accumulated Depreciation - Machinery", credit=new_mach_dep_20x7)],
   memo="Dec 31, 20X7 period-end adjusting entry - depreciation on the new machine.")
assert new_mach_bv_dec31 == d(new_mach_cost - new_mach_ad_dec31)

# ---------------------------------------------------------------------- (f)
# Building subsequent measurement schedule, reduction-of-accum.-dep. method.
rows = []
rows.append(("Jan 1, 20X7 - opening balances", d(bld_cost_0), d(bld_ad_0), bld_bv_0,
             bld_life_0, bld_annual_dep_pre))
rows.append(("Aug 1, 20X7 - modernization charged to accum. dep. ($192,000)",
             d(bld_cost_0), bld_ad_after_elec, bld_bv_after_elec, bld_life_new,
             bld_annual_dep_rev))
rows.append(("Dec 31, 20X7 - period-end depreciation ($102,000)", d(bld_cost_0),
             bld_ad_dec31_red, bld_bv_dec31, d(bld_life_new - C("1")),
             bld_annual_dep_rev))
for label, cost, ad, bv, life, dep in rows:
    assert bv == d(cost - ad), label
    A("f: [%s] cost" % label, float(cost))
    A("f: [%s] accumulated depreciation" % label, float(ad))
    A("f: [%s] book value" % label, float(bv))
    A("f: [%s] remaining useful life (years)" % label, float(life))
    A("f: [%s] annual depreciation going forward" % label, float(dep))

# close the schedule exactly
assert d(bld_ad_0 - elec_cost + bld_annual_dep_rev) == bld_ad_dec31_red
assert d(bld_bv_0 + elec_cost - bld_annual_dep_rev) == bld_bv_dec31
A("f: proof - opening BV + betterment - 20X7 depreciation = Dec 31 BV",
  float(d(bld_bv_0 + elec_cost - bld_annual_dep_rev)))
A("f: remaining depreciable amount at Dec 31, 20X7 over 15 remaining years",
  float(bld_bv_dec31))

# ------------------------------------------------------------- 20X7 totals
total_dep_20x7 = d(bld_annual_dep_rev + mach_dep_to_disposal + new_mach_dep_20x7)
A("total 20X7 depreciation expense (building 102,000 + old machine 7,000 + "
  "new machine 5,000)", float(total_dep_20x7))
A("total 20X7 loss on disposal", float(loss_on_disposal))
A("total 20X7 charge to income (depreciation + loss on disposal)",
  float(d(total_dep_20x7 + loss_on_disposal)))
A("total 20X7 PPE-related cash outflow, net of proceeds",
  float(d(elec_cost + new_mach_cost - old_mach_proceeds)))

notes = (
    "(a) No JE in January. A planned major overhaul is a future event: there is no past "
    "transaction creating a present obligation, so no liability and no expense may be "
    "recognized, and accruing/providing in advance for planned major maintenance is not "
    "permitted. The $180,000 is a budget only; the cost is recognized when incurred "
    "(expensed as repairs/maintenance, or capitalized if it qualifies as a betterment). "
    "(b) Because the modernization extends the building's life (rather than improving "
    "output quality) and the old electrical component's cost is not separately tracked, "
    "the $192,000 is debited to Accumulated Depreciation - Building; gross cost stays at "
    "$2,400,000, accum. dep. falls to $768,000, and BV rises to $1,632,000. Revised "
    "full-year depreciation = $1,632,000 / 16 yrs = $102,000 (per the stem's simplifying "
    "assumption, a full year is taken in 20X7 rather than pro-rating the pre- and "
    "post-change periods). (c) Capitalizing instead debits Building $192,000, giving gross "
    "cost $2,592,000 with accum. dep. still $960,000 - the same $1,632,000 BV and the same "
    "16-year life, hence identical $102,000 depreciation and identical Dec 31 net book value "
    "of $1,530,000. Only the gross presentation differs: capitalization shows a $192,000 "
    "larger cost AND a $192,000 larger accumulated depreciation than the reduction method. "
    "(d) Old machine: 7/12 x $12,000 = $7,000 catch-up depreciation, accum. dep. $67,000, "
    "BV $17,000; sold for $2,000, so a $15,000 loss on disposal. New machine capitalized at "
    "$96,000. (e) New machine depreciation for 20X7 = 5/12 x ($96,000 / 8) = $5,000 (held "
    "Aug 1 - Dec 31); no full-year simplifying assumption was extended to the machine, "
    "which was only acquired on Aug 1. Dec 31 snapshot: cost $96,000, accum. dep. $5,000, "
    "BV $91,000, 91 months (7 yr 7 mo) of life left, residual $0. (f) Schedule closes "
    "exactly: $1,440,000 + $192,000 - $102,000 = $1,530,000 = $2,400,000 - $870,000. "
    "Whole-dollar ROUND_HALF_UP throughout; every amount divided evenly, so no rounding "
    "residual arose."
)

out = {
    "id": "agent_333#02",
    "rounding_convention": (
        "decimal.Decimal only (no floats); every amount quantized to whole dollars with "
        "ROUND_HALF_UP, applied period-by-period as each period's depreciation is computed; "
        "schedules closed exactly (Dec 31 BV proved = cost - accum. dep.; all divisions here "
        "are exact so no rounding residual arose); Dr = Cr asserted on every entry."
    ),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}
print(json.dumps(out, indent=1))
