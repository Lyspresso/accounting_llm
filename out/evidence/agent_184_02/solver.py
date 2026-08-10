#!/usr/bin/env python3
"""Blind solver — Pinnacle Fasteners Corp., LIFO reserve / allowance (LO 9-6).

Item id: agent_184#02

ROUNDING CONVENTION
-------------------
All money is carried as ``decimal.Decimal`` and quantized to whole cents
(``0.01``) with ``ROUND_HALF_UP`` at every point a figure is reported — the
course convention is ROUND_HALF_UP applied per period, never at the end only.
No floats are used anywhere. Every fact-pattern amount in this item is an exact
whole dollar and every operation is addition/subtraction, so no rounding
actually bites; the quantization is applied regardless so the convention is
explicit and the script would behave correctly on cent-level inputs.
There are no present-value factors in this item.

DERIVATION (all from the stem; nothing hard-coded that was not given)
---------------------------------------------------------------------
Given: FIFO used internally, LIFO used externally. The credit balance in
"Allowance to Reduce Inventory to LIFO Basis" at Jan 1, Year 6 is $120,000,
equal to the Dec 31, Year 5 LIFO reserve. Year-end FIFO and LIFO ending
inventories are given for Years 6-8, plus LIFO-basis COGS for Years 6 and 8.

Rules applied (textbook LO 9-6, Demo 9-6):
  1. LIFO reserve at a date  = FIFO ending inventory - LIFO ending inventory.
  2. The allowance is a contra-inventory account whose balance is trued up each
     period end to equal the current LIFO reserve, so
         ending allowance = LIFO reserve at that year-end,
         change in allowance = current reserve - prior reserve.
  3. The true-up runs through Cost of Goods Sold:
         reserve increases -> Dr Cost of Goods Sold, Cr Allowance
         reserve decreases -> Dr Allowance, Cr Cost of Goods Sold
     So the COGS effect for a year equals the change in the reserve
     (positive = COGS increased, negative = COGS decreased).
  4. Balance-sheet presentation under the "in the accounts" approach:
         Inventory (at FIFO) - Allowance = Inventory at LIFO basis (current asset).
  5. COGS bridge: because the books are kept on FIFO and the year-end allowance
     entry is the only COGS adjustment,
         LIFO COGS = FIFO COGS + change in reserve
     hence FIFO COGS = LIFO COGS - change in reserve.
  6. Under the "outside the accounts" approach no formal entry is recorded; the
     LIFO-basis balance sheet still shows the LIFO inventory figure, the reserve
     is disclosed in the notes, and an analyst reconstructs
         FIFO inventory = LIFO inventory + disclosed LIFO reserve.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(value: str) -> Decimal:
    """Build a money Decimal from a string (never a float)."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def r(value: Decimal) -> Decimal:
    """Apply the reporting rounding convention: ROUND_HALF_UP to the cent."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def out(value: Decimal):
    """Render money for JSON: int when whole dollars, else float-free string."""
    v = r(value)
    return int(v) if v == v.to_integral_value() else v


# ----------------------------------------------------------------------------
# Given fact pattern
# ----------------------------------------------------------------------------
BEGINNING_ALLOWANCE_Y6 = m("120000")  # credit balance at Jan 1, Year 6

FIFO_EI = {6: m("520000"), 7: m("545000"), 8: m("490000")}
LIFO_EI = {6: m("385000"), 7: m("400000"), 8: m("415000")}

LIFO_COGS_GIVEN = {6: m("890000"), 8: m("920000")}

YEARS = [6, 7, 8]

# ----------------------------------------------------------------------------
# (a) Subsequent measurement schedule, Years 6-8
# ----------------------------------------------------------------------------
schedule = []
prior_reserve = BEGINNING_ALLOWANCE_Y6  # Dec 31, Year 5 reserve = opening allowance
for yr in YEARS:
    reserve = r(FIFO_EI[yr] - LIFO_EI[yr])       # rule 1
    delta = r(reserve - prior_reserve)           # rule 2
    cogs_effect = delta                          # rule 3
    ending_allowance = reserve                   # rule 2
    schedule.append(
        {
            "year": yr,
            "beginning_allowance": prior_reserve,
            "fifo_ei": FIFO_EI[yr],
            "lifo_ei": LIFO_EI[yr],
            "lifo_reserve": reserve,
            "delta_reserve": delta,
            "cogs_effect": cogs_effect,
            "ending_allowance": ending_allowance,
        }
    )
    prior_reserve = reserve

by_year = {row["year"]: row for row in schedule}

# ----------------------------------------------------------------------------
# (b) Period-end adjusting journal entries, approach (1) "in the accounts"
# ----------------------------------------------------------------------------
ALLOWANCE = "Allowance to Reduce Inventory to LIFO Basis"
COGS = "Cost of Goods Sold"

journal_entries = []
for row in schedule:
    delta = row["delta_reserve"]
    amount = r(abs(delta))
    if delta > 0:
        lines = [
            {"account": COGS, "debit": out(amount), "credit": 0},
            {"account": ALLOWANCE, "debit": 0, "credit": out(amount)},
        ]
    elif delta < 0:
        lines = [
            {"account": ALLOWANCE, "debit": out(amount), "credit": 0},
            {"account": COGS, "debit": 0, "credit": out(amount)},
        ]
    else:
        lines = []
    journal_entries.append(
        {
            "part": "b",
            "date": f"December 31, Year {row['year']}",
            "lines": lines,
        }
    )

# Debits must equal credits in every entry.
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, f"unbalanced entry: {je}"

# ----------------------------------------------------------------------------
# (c) Balance-sheet classification at December 31, Year 8, approach (1)
# ----------------------------------------------------------------------------
y8 = by_year[8]
bs_inventory_fifo = y8["fifo_ei"]
bs_allowance = y8["ending_allowance"]
bs_inventory_net = r(bs_inventory_fifo - bs_allowance)  # rule 4

# ----------------------------------------------------------------------------
# (d) Approach (2) "outside the accounts" for Year 8
# ----------------------------------------------------------------------------
d_formal_je = "No — no formal journal entry is made for the reserve; the books stay on FIFO and the LIFO conversion is made only for external reporting."
d_bs_inventory = y8["lifo_ei"]                      # LIFO-basis balance sheet
d_note_reserve = y8["lifo_reserve"]                 # disclosed in the notes
d_analyst_fifo = r(d_bs_inventory + d_note_reserve)  # rule 6

# ----------------------------------------------------------------------------
# (e) FIFO COGS from LIFO COGS using the change in reserve (rule 5)
# ----------------------------------------------------------------------------
fifo_cogs = {
    yr: r(LIFO_COGS_GIVEN[yr] - by_year[yr]["delta_reserve"]) for yr in (6, 8)
}

# ----------------------------------------------------------------------------
# (f) Which year is the reverse / settlement-type adjustment
# ----------------------------------------------------------------------------
reversal_years = [row["year"] for row in schedule if row["delta_reserve"] < 0]
assert len(reversal_years) == 1, reversal_years
rev_year = reversal_years[0]
rev_amount = r(abs(by_year[rev_year]["delta_reserve"]))
f_effect = (
    f"Year {rev_year}: the allowance is debited ${rev_amount:,.0f} to reverse part of the "
    f"prior LIFO-reserve build-up, with the credit to Cost of Goods Sold. COGS decreases "
    f"by ${rev_amount:,.0f}, so gross profit and pretax income each increase by ${rev_amount:,.0f}."
)

# ----------------------------------------------------------------------------
# Answers — only the figures the Required parts ask for
# ----------------------------------------------------------------------------
answers = []

for row in schedule:
    yr = row["year"]
    answers.extend(
        [
            {"label": f"a: Year {yr} — ending inventory at FIFO", "value": out(row["fifo_ei"])},
            {"label": f"a: Year {yr} — ending inventory at LIFO", "value": out(row["lifo_ei"])},
            {"label": f"a: Year {yr} — LIFO reserve at Dec 31", "value": out(row["lifo_reserve"])},
            {"label": f"a: Year {yr} — change in LIFO reserve", "value": out(row["delta_reserve"])},
            {
                "label": f"a: Year {yr} — COGS effect (positive = increase in COGS)",
                "value": out(row["cogs_effect"]),
            },
            {
                "label": f"a: Year {yr} — ending allowance balance (credit)",
                "value": out(row["ending_allowance"]),
            },
        ]
    )

answers.extend(
    [
        {
            "label": "c: Dec 31, Year 8 balance sheet — Inventory (at FIFO cost)",
            "value": out(bs_inventory_fifo),
        },
        {
            "label": "c: Dec 31, Year 8 balance sheet — less Allowance to Reduce Inventory to LIFO Basis",
            "value": out(bs_allowance),
        },
        {
            "label": "c: Dec 31, Year 8 balance sheet — Inventory at LIFO basis (net current asset)",
            "value": out(bs_inventory_net),
        },
        {"label": "d(i): formal JE made for the reserve under approach (2)?", "value": d_formal_je},
        {
            "label": "d(ii): inventory on the Year 8 LIFO-basis balance sheet",
            "value": out(d_bs_inventory),
        },
        {"label": "d(iii): LIFO reserve disclosed in the Year 8 notes", "value": out(d_note_reserve)},
        {
            "label": "d(iv): FIFO inventory an analyst would reconstruct at Dec 31, Year 8",
            "value": out(d_analyst_fifo),
        },
        {"label": "e: Year 6 FIFO-basis COGS", "value": out(fifo_cogs[6])},
        {"label": "e: Year 8 FIFO-basis COGS", "value": out(fifo_cogs[8])},
        {"label": "f: year with the reverse / settlement-type adjustment", "value": f"Year {rev_year}"},
        {"label": "f: income-statement effect", "value": f_effect},
    ]
)

result = {
    "id": "agent_184#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP quantized to the cent per period "
        "(applied at each year-end figure, not only at the end). No PV factors in this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Allowance is trued up to the year-end LIFO reserve (FIFO EI - LIFO EI) each Dec 31, with the "
        "change run through Cost of Goods Sold. Year 6 +15,000 and Year 7 +10,000 build the reserve "
        "(Dr COGS); Year 8 reverses 70,000 (Dr Allowance, Cr COGS). FIFO COGS = LIFO COGS - change in "
        "reserve. Given Jan 1, Year 6 allowance of 120,000 is the Dec 31, Year 5 reserve and is the "
        "starting point of the Year 6 change."
    ),
}

print(json.dumps(result, indent=2))
