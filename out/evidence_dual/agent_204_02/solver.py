"""
Independent (second) derivation of agent_204#02 — LO 11-8.

Rounding convention: decimal.Decimal throughout (never float). Every money
figure is quantized to whole dollars with ROUND_HALF_UP, applied per period
(each year's depreciation is rounded on its own, then accumulated), matching
this edition's "whole dollars in journal entries" rule. The schedule is not
forced to a plug: because the asset is scrapped after Year 3 of a 6-year life,
the schedule does NOT run to residual value, so it is closed by tying
year-end accumulated depreciation to the sum of the rounded annual amounts and
year-end NBV to (full fair value - accumulated depreciation) exactly; the
final NBV is then relieved in full by the disposal entry (Dr/Cr equal, no
rounding residue).

Treatment (per LO 11-8, overriding any instinct to capitalize):
  - Donated (contributed) asset recorded at FULL fair value: $180,000.
  - Incidental cost paid in cash ($3,000 title transfer) is NOT capitalized;
    Cash is credited for it and Contribution Revenue is recorded NET:
    180,000 - 3,000 = 177,000.
  - Depreciable base therefore excludes the $3,000: (180,000 - 12,000).
"""
from decimal import Decimal, ROUND_HALF_UP
import json

D = Decimal
CENT = D("1")


def r(x):
    """Whole-dollar ROUND_HALF_UP."""
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def n(x):
    """JSON-friendly number (whole dollars -> int)."""
    x = r(x)
    return int(x)


# ---------------- stem facts (only these are hard inputs) ----------------
FAIR_VALUE = D("180000")
INCIDENTAL_CASH = D("3000")          # legal title transfer paid by Cedar Ridge
RESIDUAL = D("12000")
LIFE_YEARS = D("6")
MONTHS_IN_YEAR = D("12")
ACQ_MONTH = D("4")                   # April 1, Year 1
SCRAP_PROCEEDS = D("9500")
SCRAP_YEAR = 3

# ---------------- (a) contribution ----------------
asset_recorded = FAIR_VALUE                       # full FV, not FV + costs
contribution_revenue = FAIR_VALUE - INCIDENTAL_CASH   # revenue NET of cost paid

# ---------------- (b) subsequent measurement schedule ----------------
depreciable_base = FAIR_VALUE - RESIDUAL
full_year_dep = r(depreciable_base / LIFE_YEARS)
# months held in Year 1: April 1 -> Dec 31 inclusive of April
months_held_y1 = MONTHS_IN_YEAR - ACQ_MONTH + D("1")
dep_y1 = r(depreciable_base / LIFE_YEARS * (months_held_y1 / MONTHS_IN_YEAR))

schedule = []
accum = D("0")
for yr in (1, 2, 3):
    dep = dep_y1 if yr == 1 else full_year_dep
    accum = accum + dep
    nbv = asset_recorded - accum
    schedule.append({
        "year": yr,
        "months": int(months_held_y1) if yr == 1 else int(MONTHS_IN_YEAR),
        "dep": dep,
        "accum": accum,
        "nbv": nbv,
    })

accum_at_disposal = schedule[SCRAP_YEAR - 1]["accum"]
nbv_at_disposal = schedule[SCRAP_YEAR - 1]["nbv"]
assert nbv_at_disposal == asset_recorded - accum_at_disposal

# ---------------- (d) scrap disposal ----------------
gain_loss = SCRAP_PROCEEDS - nbv_at_disposal      # negative => loss
loss_on_disposal = -gain_loss

# ---------------- answers ----------------
answers = [
    {"label": "a: Equipment (asset) debited at full fair value", "value": n(asset_recorded)},
    {"label": "a: Cash credited for incidental title-transfer cost paid", "value": n(INCIDENTAL_CASH)},
    {"label": "a: Contribution Revenue credited, NET of the cash cost (180,000 - 3,000)", "value": n(contribution_revenue)},

    {"label": "b: depreciable base (180,000 FV - 12,000 residual; 3,000 excluded)", "value": n(depreciable_base)},
    {"label": "b: full-year straight-line depreciation (168,000 / 6)", "value": n(full_year_dep)},
    {"label": "b: months held in Year 1 (Apr 1 - Dec 31)", "value": int(months_held_y1)},
    {"label": "b: Year 1 depreciation expense (28,000 x 9/12)", "value": n(schedule[0]["dep"])},
    {"label": "b: Year 1 year-end accumulated depreciation", "value": n(schedule[0]["accum"])},
    {"label": "b: Year 1 year-end NBV", "value": n(schedule[0]["nbv"])},
    {"label": "b: Year 2 depreciation expense (full year)", "value": n(schedule[1]["dep"])},
    {"label": "b: Year 2 year-end accumulated depreciation", "value": n(schedule[1]["accum"])},
    {"label": "b: Year 2 year-end NBV", "value": n(schedule[1]["nbv"])},
    {"label": "b: Year 3 depreciation expense (full year)", "value": n(schedule[2]["dep"])},
    {"label": "b: Year 3 year-end accumulated depreciation", "value": n(schedule[2]["accum"])},
    {"label": "b: Year 3 year-end NBV (before disposal)", "value": n(schedule[2]["nbv"])},

    {"label": "c: Dec 31 Year 1 depreciation adjusting entry amount", "value": n(schedule[0]["dep"])},
    {"label": "c: Dec 31 Year 2 depreciation adjusting entry amount", "value": n(schedule[1]["dep"])},

    {"label": "d: Dec 31 Year 3 depreciation adjusting entry amount", "value": n(schedule[2]["dep"])},
    {"label": "d: cash received from salvage dealer", "value": n(SCRAP_PROCEEDS)},
    {"label": "d: accumulated depreciation removed on disposal", "value": n(accum_at_disposal)},
    {"label": "d: equipment cost (FV basis) removed on disposal", "value": n(asset_recorded)},
    {"label": "d: NBV at disposal date", "value": n(nbv_at_disposal)},
    {"label": "d: loss on disposal / scrapping (9,500 - 103,000)", "value": n(loss_on_disposal)},
]

# ---------------- journal entries ----------------
def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": n(dr) if dr is not None else 0,
            "credit": n(cr) if cr is not None else 0}

journal_entries = [
    {"part": "a", "date": "Year 1, April 1", "description": "Unconditional contribution of packaging equipment received at fair value; title-transfer cost paid in cash; contribution revenue recorded net of that cost",
     "lines": [
        L("Equipment", dr=asset_recorded),
        L("Cash", cr=INCIDENTAL_CASH),
        L("Contribution Revenue (Revenue from Contributed Equipment)", cr=contribution_revenue),
     ]},
    {"part": "c", "date": "Year 1, December 31", "description": "Partial-year depreciation, 9 of 12 months",
     "lines": [
        L("Depreciation Expense", dr=schedule[0]["dep"]),
        L("Accumulated Depreciation - Equipment", cr=schedule[0]["dep"]),
     ]},
    {"part": "c", "date": "Year 2, December 31", "description": "Full-year depreciation",
     "lines": [
        L("Depreciation Expense", dr=schedule[1]["dep"]),
        L("Accumulated Depreciation - Equipment", cr=schedule[1]["dep"]),
     ]},
    {"part": "d", "date": "Year 3, December 31 (1 of 2)", "description": "Full-year depreciation recorded before disposal",
     "lines": [
        L("Depreciation Expense", dr=schedule[2]["dep"]),
        L("Accumulated Depreciation - Equipment", cr=schedule[2]["dep"]),
     ]},
    {"part": "d", "date": "Year 3, December 31 (2 of 2)", "description": "Equipment scrapped; cash received from salvage dealer; carrying amount relieved and loss recognized",
     "lines": [
        L("Cash", dr=SCRAP_PROCEEDS),
        L("Accumulated Depreciation - Equipment", dr=accum_at_disposal),
        L("Loss on Disposal of Equipment", dr=loss_on_disposal),
        L("Equipment", cr=asset_recorded),
     ]},
]

for je in journal_entries:
    dsum = sum(D(l["debit"]) for l in je["lines"])
    csum = sum(D(l["credit"]) for l in je["lines"])
    assert dsum == csum, (je["part"], je["date"], dsum, csum)

notes = (
    "LO 11-8 donated asset: Equipment debited at the FULL reliable fair value 180,000; the 3,000 "
    "title-transfer cash paid is NOT capitalized, so Cash is credited 3,000 and Contribution Revenue "
    "is 177,000 (net). Depreciable base = 180,000 - 12,000 = 168,000; full-year SL = 28,000. Year 1 "
    "holds 9 months (Apr 1 - Dec 31) => 21,000. Schedule: Y1 21,000 / accum 21,000 / NBV 159,000; "
    "Y2 28,000 / accum 49,000 / NBV 131,000; Y3 28,000 / accum 77,000 / NBV 103,000. Disposal at "
    "12/31/Y3 after Y3 depreciation: Dr Cash 9,500, Dr Accum. Dep. 77,000, Dr Loss 93,500, Cr Equipment "
    "180,000. Because the asset is scrapped in year 3 of a 6-year life the schedule does not reach "
    "residual value, so it is closed by tying accum. dep. to the sum of rounded annual charges and NBV "
    "to 180,000 - accum. dep.; the disposal entry then relieves the 103,000 NBV in full. All amounts are "
    "exact whole dollars, so ROUND_HALF_UP produced no rounding difference anywhere."
)

out = {
    "id": "agent_204#02",
    "rounding_convention": ("decimal.Decimal only; whole-dollar ROUND_HALF_UP applied per period "
                           "(each year's depreciation rounded, then accumulated); schedule closed by "
                           "tying accum. dep. to the sum of rounded annual charges and NBV to FV less "
                           "accum. dep. (asset scrapped before end of life, so it does not close to "
                           "residual); no rounding difference arose"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}
print(json.dumps(out, indent=1))
