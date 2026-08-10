#!/usr/bin/env python3
"""Blind solver for item agent_219#05 -- Meridian Optics Corp. patent life cycle.

Fact pattern (from stem.md only):
  - Patent acquired 1/1/Y1 for $96,000 cash. Useful life 8 years, residual $0,
    straight-line. Company credits Patent directly (no accumulated amortization
    contra account). Fiscal year ends December 31.
  - 12/31/Y3, after Y3 amortization: impairment indicator present.
    Undiscounted future net cash inflows $52,000; fair value $48,000.
    Remaining useful life after impairment = 5 years.
  - 10/1/Y6: patent sold for $18,500 cash; no Y6 amortization recorded yet.

Method (ASC 350-30-35-14 / ASC 360-10-35, per ACCOUNT-343 Ch. 13 LO 13-3):
  1. Straight-line amortization = (cost - residual) / useful life.
  2. Impairment is a TWO-STEP test triggered by an indicator:
       Step 1 (recoverability): compare undiscounted future net cash inflows to
       the carrying amount AFTER recording that year's amortization. If
       undiscounted cash flows >= carrying amount, no impairment; stop.
       Step 2 (measurement): impairment loss = carrying amount - fair value.
     The written-down fair value becomes the new accounting basis, amortized
     straight-line over the new remaining useful life (residual still $0).
  3. On disposal, amortize to the disposal date first (months elapsed / 12),
     then derecognize the carrying amount. Gain/(loss) = proceeds - carrying
     amount at disposal date.

ROUNDING CONVENTION
  All money is decimal.Decimal. Rounding is ROUND_HALF_UP to the cent,
  applied PER PERIOD (each year's amortization charge, and the partial-year
  charge to the disposal date, is rounded as it is computed and the rounded
  figure is what reduces the carrying amount) -- never round only at the end.
  No present-value factors are used in this item (fair value is given
  directly), so no PV table-vs-formula question arises.
  Every figure in this fact pattern divides exactly, so rounding is a no-op
  here; it is applied anyway so the script is correct for perturbed inputs.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP. Applied per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """Emit an int when the value is a whole number of dollars, else a float-free
    string-safe Decimal converted via float only at the JSON boundary."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- given facts
COST = Decimal("96000")
RESIDUAL = Decimal("0")
LIFE_YEARS = Decimal("8")
UNDISCOUNTED_CF_Y3 = Decimal("52000")
FAIR_VALUE_Y3 = Decimal("48000")
REMAINING_LIFE_AFTER_IMPAIRMENT = Decimal("5")
PROCEEDS = Decimal("18500")
MONTHS_IN_Y6_BEFORE_SALE = Decimal("9")  # Jan 1 -> Oct 1 = 9 months

# ------------------------------------------------- (a) subsequent measurement
annual_amort_original = money((COST - RESIDUAL) / LIFE_YEARS)

schedule = []
carrying = COST

# Years 1-3 at the original rate.
for yr in (1, 2, 3):
    charge = annual_amort_original
    carrying = money(carrying - charge)
    schedule.append(
        {"year": yr, "amortization": charge, "carrying_end": carrying,
         "impairment": Decimal("0")}
    )

carrying_before_impairment = carrying  # 12/31/Y3 after Y3 amortization

# Step 1: recoverability test.
impaired = UNDISCOUNTED_CF_Y3 < carrying_before_impairment
if impaired:
    # Step 2: measurement.
    impairment_loss = money(carrying_before_impairment - FAIR_VALUE_Y3)
    carrying = money(FAIR_VALUE_Y3)
else:
    impairment_loss = Decimal("0")

schedule[-1]["impairment"] = impairment_loss
schedule[-1]["carrying_end"] = carrying

# New basis amortized over the new remaining life.
annual_amort_post = money((carrying - RESIDUAL) / REMAINING_LIFE_AFTER_IMPAIRMENT)

for yr in (4, 5):
    charge = annual_amort_post
    carrying = money(carrying - charge)
    schedule.append(
        {"year": yr, "amortization": charge, "carrying_end": carrying,
         "impairment": Decimal("0")}
    )

carrying_end_y5 = carrying

# ------------------------------------------------- (b)/(c) disposal 10/1/Y6
amort_to_disposal = money(annual_amort_post * MONTHS_IN_Y6_BEFORE_SALE / Decimal("12"))
carrying_at_disposal = money(carrying_end_y5 - amort_to_disposal)
gain_loss = money(PROCEEDS - carrying_at_disposal)  # negative => loss

# ---------------------------------------------------------------- output
answers = []
for row in schedule:
    y = row["year"]
    answers.append({"label": f"a: Year {y} amortization expense",
                    "value": num(row["amortization"])})
    if row["impairment"] != 0:
        answers.append({"label": f"a: Year {y} impairment loss",
                        "value": num(row["impairment"])})
        answers.append({"label": f"a: Year {y} carrying amount, 12/31 after impairment",
                        "value": num(row["carrying_end"])})
    else:
        answers.append({"label": f"a: Year {y} carrying amount, 12/31",
                        "value": num(row["carrying_end"])})

answers.append({"label": "c: loss on disposal of patent, 10/1/Year 6",
                "value": num(abs(gain_loss))})

journal_entries = [
    {
        "part": "b(1)",
        "date": "January 1, Year 1",
        "description": "Acquisition of process patent for cash",
        "lines": [
            {"account": "Patent", "debit": num(COST), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": num(COST)},
        ],
    },
    {
        "part": "b(2)",
        "date": "December 31, Year 3",
        "description": "Year 3 straight-line amortization ($96,000 / 8)",
        "lines": [
            {"account": "Amortization Expense",
             "debit": num(annual_amort_original), "credit": 0},
            {"account": "Patent", "debit": 0,
             "credit": num(annual_amort_original)},
        ],
    },
    {
        "part": "b(3)",
        "date": "December 31, Year 3",
        "description": "Impairment write-down to fair value "
                       "(carrying $60,000 - fair value $48,000)",
        "lines": [
            {"account": "Impairment Loss", "debit": num(impairment_loss),
             "credit": 0},
            {"account": "Patent", "debit": 0, "credit": num(impairment_loss)},
        ],
    },
    {
        "part": "b(4)",
        "date": "December 31, Year 4",
        "description": "Year 4 amortization on new basis ($48,000 / 5)",
        "lines": [
            {"account": "Amortization Expense",
             "debit": num(annual_amort_post), "credit": 0},
            {"account": "Patent", "debit": 0, "credit": num(annual_amort_post)},
        ],
    },
    {
        "part": "b(5)",
        "date": "October 1, Year 6",
        "description": "Amortization for 9 months of Year 6 to date of disposal "
                       "($9,600 x 9/12)",
        "lines": [
            {"account": "Amortization Expense",
             "debit": num(amort_to_disposal), "credit": 0},
            {"account": "Patent", "debit": 0, "credit": num(amort_to_disposal)},
        ],
    },
    {
        "part": "b(6)",
        "date": "October 1, Year 6",
        "description": "Sale of patent for cash; derecognize carrying amount",
        "lines": (
            [{"account": "Cash", "debit": num(PROCEEDS), "credit": 0}]
            + ([{"account": "Loss on Sale of Patent",
                 "debit": num(abs(gain_loss)), "credit": 0}]
               if gain_loss < 0 else [])
            + [{"account": "Patent", "debit": 0,
                "credit": num(carrying_at_disposal)}]
            + ([{"account": "Gain on Sale of Patent", "debit": 0,
                 "credit": num(gain_loss)}] if gain_loss > 0 else [])
        ),
    },
]

# Self-check: every entry must balance.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"unbalanced entry {je['part']}: {dr} != {cr}"

out = {
    "id": "agent_219#05",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per "
        "period (each annual and partial-year amortization charge rounded as "
        "computed, then applied to carrying amount), not round-at-end. "
        "No PV factors needed - fair value is given."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Recoverability test at 12/31/Y3: undiscounted cash inflows $52,000 < "
        "carrying amount $60,000, so the asset is not recoverable and the "
        "impairment test applies; loss = carrying $60,000 - fair value "
        "$48,000. Fair value becomes the new basis, amortized over the new "
        "5-year remaining life. Patent is credited directly per the stem, so "
        "no accumulated amortization account is used."
    ),
}

print(json.dumps(out, indent=2))
