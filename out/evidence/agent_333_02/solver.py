#!/usr/bin/env python3
"""Blind solver for item agent_333#02 -- Northline Processors Corp. (LO 11-6 / 11-7).

Fact pattern (from stem.md only):
  Building at 1/1/20X7: cost 2,400,000; accum. dep. 960,000; BV 1,440,000;
    remaining life 12 yrs; residual 0; pre-change annual dep. 120,000.
  Production machine at 1/1/20X7: cost 84,000; accum. dep. 60,000; BV 24,000;
    remaining life 2 yrs; residual 0; annual dep. 12,000.
  Jan 20X7: $180,000 budgeted for a planned major maintenance overhaul.
  Aug 1 20X7: electrical modernization, $192,000 cash, extends building life by
    4 years, old component cost not tracked, life extension (not improved
    quality) is the result -> reduction of accumulated depreciation method.
    Simplifying assumption: FULL-YEAR revised 20X7 building depreciation is
    computed on the post-expenditure book value over the new remaining life
    (12 + 4 = 16 years).
  Aug 1 20X7: old machine depreciated through disposal date (7/12 of a year),
    sold for $2,000 cash; new machine bought for $96,000 cash, residual 0,
    8-year life.
  Dec 31 20X7: period-end depreciation on the building and the new machine.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Rounding is ROUND_HALF_UP to the cent
(quantize to 0.01), applied PER PERIOD -- i.e. each period's depreciation
charge is rounded as it is computed and the rounded charge is what is posted
and carried into accumulated depreciation; carrying amounts are never derived
from an unrounded running total. Partial-period depreciation uses the
months-of-service fraction of the rounded annual charge (7/12 for the old
machine Jan 1 -> Aug 1; 5/12 for the new machine Aug 1 -> Dec 31), rounded once
to the cent. The building follows the stem's explicit simplifying assumption
and takes a full-year revised charge in 20X7 (no partial-period proration).
No present-value factors are involved in this item.

Authoritative basis relied on (US GAAP, matching the course text, Ch. 11):
  ASC 360-10-25-5 -- accrue-in-advance for planned major maintenance is
  PROHIBITED in annual and interim periods; no obligation exists before the
  activity is initiated. -> part (a) requires no journal entry.

Run: python3 solver.py   (prints one JSON object to stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x):
    """Round a Decimal to the cent, ROUND_HALF_UP (the per-period convention)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    """JSON-friendly number: int when the cents are zero, else float-free string->float."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem, nothing else)
# ---------------------------------------------------------------------------
BLD_COST_0 = Decimal("2400000")
BLD_AD_0 = Decimal("960000")
BLD_LIFE_0 = Decimal("12")          # remaining years at 1/1/20X7
BLD_RESIDUAL = Decimal("0")

MCH_COST_0 = Decimal("84000")
MCH_AD_0 = Decimal("60000")
MCH_LIFE_0 = Decimal("2")
MCH_RESIDUAL = Decimal("0")

MAINT_BUDGET = Decimal("180000")    # planned overhaul budget -- never recorded
UPGRADE_COST = Decimal("192000")    # Aug 1 electrical modernization, cash
LIFE_EXTENSION = Decimal("4")       # additional years

OLD_MCH_PROCEEDS = Decimal("2000")
OLD_MCH_MONTHS_20X7 = Decimal("7")  # Jan 1 -> Aug 1

NEW_MCH_COST = Decimal("96000")
NEW_MCH_LIFE = Decimal("8")
NEW_MCH_RESIDUAL = Decimal("0")
NEW_MCH_MONTHS_20X7 = Decimal("5")  # Aug 1 -> Dec 31

MONTHS = Decimal("12")

# ---------------------------------------------------------------------------
# (a) Planned major maintenance budget -- no entry
# ---------------------------------------------------------------------------
part_a_entries_required = 0  # ASC 360-10-25-5: accrue-in-advance prohibited
part_a_amount_recorded = money(0)

# ---------------------------------------------------------------------------
# Building: carrying amounts and revised depreciation
# ---------------------------------------------------------------------------
bld_bv_0 = money(BLD_COST_0 - BLD_AD_0)                      # 1,440,000
bld_annual_dep_pre = money((bld_bv_0 - BLD_RESIDUAL) / BLD_LIFE_0)  # ties to 120,000

# Aug 1 -- reduction of accumulated depreciation method:
#   Dr Accumulated Depreciation  192,000 / Cr Cash 192,000
bld_ad_after_upgrade = money(BLD_AD_0 - UPGRADE_COST)        # 768,000
bld_cost_after_upgrade = money(BLD_COST_0)                   # cost unchanged
bld_bv_after_upgrade = money(bld_cost_after_upgrade - bld_ad_after_upgrade)  # 1,632,000

bld_new_life = BLD_LIFE_0 + LIFE_EXTENSION                   # 16 years
bld_revised_annual_dep = money(
    (bld_bv_after_upgrade - BLD_RESIDUAL) / bld_new_life
)                                                            # full-year 20X7 charge

bld_ad_1231 = money(bld_ad_after_upgrade + bld_revised_annual_dep)
bld_bv_1231 = money(bld_cost_after_upgrade - bld_ad_1231)

# (c) Capitalization alternative -- same post-expenditure BV and life
cap_cost_after_upgrade = money(BLD_COST_0 + UPGRADE_COST)    # 2,592,000
cap_ad_after_upgrade = money(BLD_AD_0)                       # 960,000 (unchanged)
cap_bv_after_upgrade = money(cap_cost_after_upgrade - cap_ad_after_upgrade)
cap_revised_annual_dep = money((cap_bv_after_upgrade - BLD_RESIDUAL) / bld_new_life)
cap_ad_1231 = money(cap_ad_after_upgrade + cap_revised_annual_dep)
cap_bv_1231 = money(cap_cost_after_upgrade - cap_ad_1231)

assert bld_bv_after_upgrade == cap_bv_after_upgrade
assert bld_revised_annual_dep == cap_revised_annual_dep
assert bld_bv_1231 == cap_bv_1231

# ---------------------------------------------------------------------------
# (d) Old machine: update depreciation through Aug 1, then dispose
# ---------------------------------------------------------------------------
mch_bv_0 = money(MCH_COST_0 - MCH_AD_0)                      # 24,000
mch_annual_dep = money((mch_bv_0 - MCH_RESIDUAL) / MCH_LIFE_0)      # ties to 12,000
old_mch_dep_to_disposal = money(mch_annual_dep * OLD_MCH_MONTHS_20X7 / MONTHS)
old_mch_ad_at_disposal = money(MCH_AD_0 + old_mch_dep_to_disposal)
old_mch_bv_at_disposal = money(MCH_COST_0 - old_mch_ad_at_disposal)
old_mch_gain_loss = money(OLD_MCH_PROCEEDS - old_mch_bv_at_disposal)  # negative = loss
old_mch_loss = money(-old_mch_gain_loss) if old_mch_gain_loss < 0 else money(0)
old_mch_gain = money(old_mch_gain_loss) if old_mch_gain_loss > 0 else money(0)

# ---------------------------------------------------------------------------
# (e) New machine: Dec 31 partial-year depreciation and snapshot
# ---------------------------------------------------------------------------
new_mch_annual_dep = money((NEW_MCH_COST - NEW_MCH_RESIDUAL) / NEW_MCH_LIFE)
new_mch_dep_20X7 = money(new_mch_annual_dep * NEW_MCH_MONTHS_20X7 / MONTHS)
new_mch_ad_1231 = money(new_mch_dep_20X7)
new_mch_bv_1231 = money(NEW_MCH_COST - new_mch_ad_1231)

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = [
    {
        "part": "b",
        "date": "20X7-08-01",
        "description": "Electrical modernization -- reduction of accumulated "
                       "depreciation method (life extended 4 years)",
        "lines": [
            line("Accumulated Depreciation - Building", debit=UPGRADE_COST),
            line("Cash", credit=UPGRADE_COST),
        ],
    },
    {
        "part": "b",
        "date": "20X7-12-31",
        "description": "Period-end adjusting entry -- revised full-year 20X7 "
                       "building depreciation (post-expenditure BV / 16 years)",
        "lines": [
            line("Depreciation Expense - Building", debit=bld_revised_annual_dep),
            line("Accumulated Depreciation - Building", credit=bld_revised_annual_dep),
        ],
    },
    {
        "part": "c",
        "date": "20X7-08-01",
        "description": "ALTERNATIVE presentation -- electrical modernization "
                       "under the capitalization method",
        "lines": [
            line("Building", debit=UPGRADE_COST),
            line("Cash", credit=UPGRADE_COST),
        ],
    },
    {
        "part": "c",
        "date": "20X7-12-31",
        "description": "ALTERNATIVE presentation -- period-end depreciation under "
                       "the capitalization method (identical amount)",
        "lines": [
            line("Depreciation Expense - Building", debit=cap_revised_annual_dep),
            line("Accumulated Depreciation - Building", credit=cap_revised_annual_dep),
        ],
    },
    {
        "part": "d",
        "date": "20X7-08-01",
        "description": "Update depreciation on old production machine through "
                       "disposal date (7/12 x 12,000)",
        "lines": [
            line("Depreciation Expense - Machine", debit=old_mch_dep_to_disposal),
            line("Accumulated Depreciation - Machine", credit=old_mch_dep_to_disposal),
        ],
    },
    {
        "part": "d",
        "date": "20X7-08-01",
        "description": "Sale of old production machine for cash",
        "lines": (
            [
                line("Cash", debit=OLD_MCH_PROCEEDS),
                line("Accumulated Depreciation - Machine", debit=old_mch_ad_at_disposal),
            ]
            + ([line("Loss on Disposal of Machine", debit=old_mch_loss)]
               if old_mch_loss > 0 else [])
            + [line("Machine", credit=MCH_COST_0)]
            + ([line("Gain on Disposal of Machine", credit=old_mch_gain)]
               if old_mch_gain > 0 else [])
        ),
    },
    {
        "part": "d",
        "date": "20X7-08-01",
        "description": "Purchase of new production machine for cash",
        "lines": [
            line("Machine", debit=NEW_MCH_COST),
            line("Cash", credit=NEW_MCH_COST),
        ],
    },
    {
        "part": "e",
        "date": "20X7-12-31",
        "description": "Period-end adjusting entry -- depreciation on new machine "
                       "(5/12 x 12,000)",
        "lines": [
            line("Depreciation Expense - Machine", debit=new_mch_dep_20X7),
            line("Accumulated Depreciation - Machine", credit=new_mch_dep_20X7),
        ],
    },
]

# Debits must equal credits in every entry.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), (je["part"], je["description"], dr, cr)

# ---------------------------------------------------------------------------
# Answers -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: journal entries required in January for the planned major "
              "maintenance budget (count; accrue-in-advance prohibited)",
     "value": part_a_entries_required},
    {"label": "a: amount recorded in January for the $180,000 planned overhaul",
     "value": num(part_a_amount_recorded)},

    {"label": "b: building book value immediately after the Aug 1 expenditure "
              "(reduction of accum. dep. method)",
     "value": num(bld_bv_after_upgrade)},
    {"label": "b: revised full-year 20X7 building depreciation expense",
     "value": num(bld_revised_annual_dep)},

    {"label": "c: 20X7 building depreciation expense under the capitalization "
              "method (same as reduction method)",
     "value": num(cap_revised_annual_dep)},
    {"label": "c: building gross cost at Dec 31, 20X7 under capitalization",
     "value": num(cap_cost_after_upgrade)},
    {"label": "c: building accumulated depreciation at Dec 31, 20X7 under "
              "capitalization",
     "value": num(cap_ad_1231)},
    {"label": "c: building carrying amount at Dec 31, 20X7 under capitalization",
     "value": num(cap_bv_1231)},

    {"label": "e: new machine cost at Dec 31, 20X7",
     "value": num(NEW_MCH_COST)},
    {"label": "e: new machine accumulated depreciation at Dec 31, 20X7",
     "value": num(new_mch_ad_1231)},
    {"label": "e: new machine carrying amount at Dec 31, 20X7",
     "value": num(new_mch_bv_1231)},

    {"label": "f: building cost at Jan 1, 20X7", "value": num(BLD_COST_0)},
    {"label": "f: building accumulated depreciation at Jan 1, 20X7",
     "value": num(BLD_AD_0)},
    {"label": "f: building carrying amount at Jan 1, 20X7", "value": num(bld_bv_0)},
    {"label": "f: reduction of accumulated depreciation, Aug 1, 20X7",
     "value": num(UPGRADE_COST)},
    {"label": "f: building accumulated depreciation after Aug 1, 20X7",
     "value": num(bld_ad_after_upgrade)},
    {"label": "f: building carrying amount after Aug 1, 20X7",
     "value": num(bld_bv_after_upgrade)},
    {"label": "f: 20X7 building depreciation expense recorded Dec 31",
     "value": num(bld_revised_annual_dep)},
    {"label": "f: building cost at Dec 31, 20X7 (unchanged under reduction method)",
     "value": num(bld_cost_after_upgrade)},
    {"label": "f: building accumulated depreciation at Dec 31, 20X7",
     "value": num(bld_ad_1231)},
    {"label": "f: building carrying amount at Dec 31, 20X7",
     "value": num(bld_bv_1231)},
]

notes = (
    "(a) No entry. ASC 360-10-25-5 prohibits the accrue-in-advance method for "
    "planned major maintenance; before the overhaul is initiated Northline has "
    "no present obligation, so the $180,000 budget is a management plan only "
    "and is recorded when (and as) the work is performed. "
    "(b) Life extension without improved quality -> reduction of accumulated "
    "depreciation: Dr Accum. Dep. 192,000 / Cr Cash 192,000; post-expenditure "
    "BV 1,440,000 + 192,000 = 1,632,000 over 16 years = 102,000 full-year 20X7 "
    "charge per the stem's simplifying assumption. "
    "(c) Capitalization gives the same 1,632,000 BV over 16 years, so 20X7 "
    "expense is identical at 102,000. Balance-sheet contrast: capitalization "
    "grosses up the asset (cost 2,592,000, accum. dep. 1,062,000) while the "
    "reduction method leaves cost at 2,400,000 and shrinks accum. dep. "
    "(768,000 at Aug 1, 870,000 at Dec 31); both report a 1,530,000 carrying "
    "amount, so only the gross presentation differs. "
    "(d) Old machine: 7/12 x 12,000 = 7,000 catch-up depreciation, accum. dep. "
    "67,000, carrying amount 17,000, sold for 2,000 -> 15,000 loss on disposal. "
    "(e) New machine: 96,000 / 8 = 12,000 per year x 5/12 = 5,000 for 20X7; "
    "Dec 31 snapshot cost 96,000, accum. dep. 5,000, carrying amount 91,000, "
    "7 years 7 months of the 8-year life remaining. "
    "(f) Building schedule 20X7 (reduction method): Jan 1 cost 2,400,000, "
    "accum. dep. 960,000, BV 1,440,000; Aug 1 accum. dep. reduced 192,000 -> "
    "768,000, BV 1,632,000; Dec 31 depreciation 102,000 -> accum. dep. 870,000, "
    "BV 1,530,000, cost unchanged at 2,400,000."
)

output = {
    "id": "agent_333#02",
    "rounding_convention": "ROUND_HALF_UP to the cent, applied per period; "
                           "partial-period depreciation = months/12 of the "
                           "rounded annual charge (old machine 7/12, new machine "
                           "5/12); building takes the stem's full-year revised "
                           "charge; no PV factors involved",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
