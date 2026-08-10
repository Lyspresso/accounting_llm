#!/usr/bin/env python3
"""Blind solver for item agent_080#01 — Coastal Glassworks Inc. tempering furnace.

Fact pattern (from stem.md only):
  Cost $240,000 cash, placed in service Jan 1 Year 1.
  Original residual $24,000, original useful life 8 years, straight-line.
  Jan 1 Year 5: TOTAL useful life revised to 12 years; residual revised to $12,000.
  Dec 31 Year 6: sold for $95,000 cash, after recording Year 6 depreciation.

Method
------
Straight-line: annual depreciation = (depreciable base) / (life in years).

A change in useful life and/or residual value is a CHANGE IN ACCOUNTING ESTIMATE,
accounted for PROSPECTIVELY (ASC 250 / IAS 8): prior-period depreciation is NOT
restated. The carrying amount at the date of change becomes the new base:

    revised annual depreciation = (carrying amount at change date - new residual)
                                  / remaining useful life

"Total useful life revised to 12 years" is read as TOTAL life from the original
in-service date, so remaining life at Jan 1 Year 5 = 12 - 4 elapsed years = 8 years.

Disposal: gain/loss = proceeds - carrying amount at the disposal date (after the
current period's depreciation has been recorded).

Rounding convention
-------------------
ROUND_HALF_UP to the cent, applied PER PERIOD (each year's depreciation is rounded
before it is accumulated), using decimal.Decimal exclusively — no floats anywhere.
No PV table factors are involved in this item. Every figure here happens to divide
evenly, so no rounding difference arises, but the convention is applied regardless
and the final year is NOT plugged: the schedule is verified to land exactly on the
revised residual value.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Round to the cent, ROUND_HALF_UP, per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def out(d: Decimal):
    """Emit a Decimal as an int when whole, else as a float-free 2dp number."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- facts
COST = Decimal("240000")
ORIG_RESIDUAL = Decimal("24000")
ORIG_LIFE = 8                      # years, straight-line
CHANGE_AT_START_OF_YEAR = 5        # Jan 1, Year 5
REVISED_TOTAL_LIFE = 12            # years, measured from Jan 1 Year 1
REVISED_RESIDUAL = Decimal("12000")
PROCEEDS = Decimal("95000")
DISPOSAL_END_OF_YEAR = 6           # Dec 31, Year 6, after Year 6 depreciation

ASSET_ACCOUNT = "Equipment — Tempering Furnace"
ACCUM_ACCOUNT = "Accumulated Depreciation — Equipment"

# ------------------------------------------------- b. original SL schedule
orig_annual_dep = money((COST - ORIG_RESIDUAL) / Decimal(ORIG_LIFE))

years_elapsed = CHANGE_AT_START_OF_YEAR - 1          # 4 full years: Y1..Y4
schedule = []                                        # rows: year, dep, accum, carrying
accum = Decimal("0")
for yr in range(1, years_elapsed + 1):
    dep = orig_annual_dep
    accum = money(accum + dep)
    schedule.append({"year": yr, "dep": dep, "accum": accum,
                     "carrying": money(COST - accum)})

# ------------------------- c. carrying amount + revised depreciation at change
carrying_at_change = money(COST - accum)
remaining_life = REVISED_TOTAL_LIFE - years_elapsed   # 12 - 4 = 8 years
revised_annual_dep = money((carrying_at_change - REVISED_RESIDUAL) / Decimal(remaining_life))

# ------------------------------------------- d. schedule Years 5 .. 12
for yr in range(CHANGE_AT_START_OF_YEAR, REVISED_TOTAL_LIFE + 1):
    dep = revised_annual_dep
    accum = money(accum + dep)
    schedule.append({"year": yr, "dep": dep, "accum": accum,
                     "carrying": money(COST - accum)})

carrying_end_of_life = schedule[-1]["carrying"]
assert carrying_end_of_life == REVISED_RESIDUAL, (
    f"schedule must end at revised residual {REVISED_RESIDUAL}, got {carrying_end_of_life}"
)

# ------------------------------------------------------ e. disposal
row_disposal = next(r for r in schedule if r["year"] == DISPOSAL_END_OF_YEAR)
accum_at_disposal = row_disposal["accum"]
carrying_at_disposal = row_disposal["carrying"]
gain_loss = money(PROCEEDS - carrying_at_disposal)    # negative => loss
loss_on_disposal = money(-gain_loss) if gain_loss < 0 else Decimal("0")
gain_on_disposal = gain_loss if gain_loss > 0 else Decimal("0")

# ------------------------------------------------------ journal entries
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": out(debit), "credit": out(credit)}


je_a = {"part": "a", "date": "Year 1, January 1", "lines": [
    line(ASSET_ACCOUNT, debit=COST),
    line("Cash", credit=COST),
]}

je_c = {"part": "c", "date": "Year 5, December 31", "lines": [
    line("Depreciation Expense", debit=revised_annual_dep),
    line(ACCUM_ACCOUNT, credit=revised_annual_dep),
]}

disposal_lines = [
    line("Cash", debit=PROCEEDS),
    line(ACCUM_ACCOUNT, debit=accum_at_disposal),
]
if loss_on_disposal > 0:
    disposal_lines.append(line("Loss on Disposal of Equipment", debit=loss_on_disposal))
disposal_lines.append(line(ASSET_ACCOUNT, credit=COST))
if gain_on_disposal > 0:
    disposal_lines.append(line("Gain on Disposal of Equipment", credit=gain_on_disposal))

je_e = {"part": "e", "date": "Year 6, December 31", "lines": disposal_lines}

journal_entries = [je_a, je_c, je_e]

# balance check — debits must equal credits in every entry
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"entry {je['part']} out of balance: {dr} != {cr}"

# ------------------------------------------------------ answers
answers = [
    {"label": "b: original annual depreciation (Years 1-4)", "value": out(orig_annual_dep)},
]
for r in schedule[:years_elapsed]:
    answers.append({"label": f"b: Year {r['year']} depreciation expense", "value": out(r["dep"])})
    answers.append({"label": f"b: Year {r['year']} accumulated depreciation", "value": out(r["accum"])})
    answers.append({"label": f"b: Year {r['year']} carrying amount, year-end", "value": out(r["carrying"])})

answers.append({"label": "c: carrying amount at January 1, Year 5",
                "value": out(carrying_at_change)})
answers.append({"label": "c: updated (revised) annual depreciation, Years 5-12",
                "value": out(revised_annual_dep)})

for r in schedule[years_elapsed:]:
    answers.append({"label": f"d: Year {r['year']} depreciation expense", "value": out(r["dep"])})
    answers.append({"label": f"d: Year {r['year']} accumulated depreciation", "value": out(r["accum"])})
    answers.append({"label": f"d: Year {r['year']} carrying amount, year-end", "value": out(r["carrying"])})

answers.append({"label": "e: loss on disposal, December 31, Year 6",
                "value": out(loss_on_disposal)})
answers.append({
    "label": "f: classification of the January 1, Year 5 revision",
    "value": "Change in accounting estimate — applied prospectively; prior years are not restated.",
})

result = {
    "id": "agent_080#01",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP to the cent applied per period "
        "(each year's depreciation rounded before accumulation); final year not plugged — "
        "schedule verified to land exactly on the revised $12,000 residual; no PV factors used."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Revised total life of 12 years is read as total life from the January 1, Year 1 "
        "in-service date, leaving 8 remaining years at January 1, Year 5. The revision is a "
        "change in accounting estimate, so it is applied prospectively over the remaining "
        "life against the carrying amount at the date of change."
    ),
}

print(json.dumps(result, indent=2))
