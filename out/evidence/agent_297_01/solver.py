#!/usr/bin/env python3
"""Blind solver for item agent_297#01 -- Cedarwick Packaging LLC, investing activities (LO 22-3).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP per period, applied to every money figure at the moment it is
produced (Decimal quantized to 0.01). No PV/discounting appears in this fact
pattern, so no table-factor-vs-exact-formula choice arises. Every amount in the
stem is a whole dollar and every derivation is pure addition/subtraction of
those amounts, so the quantization is a no-op guard rather than a source of
rounding difference. All money is decimal.Decimal; floats are never used.

METHOD
------
Nothing is hard-coded except the facts stated in the stem. The three unknowns
are solved from subsequent-measurement (rollforward) schedules:

  Equipment (at cost):
      beginning + cash purchases - cost of asset sold = ending
      => cash purchases = ending - beginning + cost of asset sold

  Accumulated depreciation--equipment (contra):
      beginning + depreciation expense - AD removed on sale = ending
      (used as an internal consistency check; the stem gives both endpoints)

  Debt investments (amortized cost) and Long-term notes receivable (nontrade):
      beginning + additions - disposals/collections = ending
      (both given; used as internal consistency checks)

Gain/loss on each disposal = proceeds - carrying amount at disposal. Gains are
NOT investing cash flows; the gross cash proceeds are. The debt investments are
explicitly not held for trading/resale, so their purchase and sale are investing
(not operating) cash flows. The nontrade notes receivable are lending activity,
so the advance and the principal collection are likewise investing cash flows.

Internal checks (rollforward ties, debits == credits on every journal entry,
and the investing section footing back to the sum of its line items) raise
AssertionError rather than silently reporting a wrong figure. Check figures are
deliberately excluded from the reported "answers" list.

Run:  python3 solver.py     -> prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(value) -> Decimal:
    """Money constructor: Decimal, quantized ROUND_HALF_UP to the cent."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


def out(value: Decimal):
    """Render a money Decimal for JSON: int when whole dollars, else float-free str."""
    q = value.quantize(CENT, rounding=ROUND_HALF_UP)
    if q == q.to_integral_value():
        return int(q)
    return str(q)


# ---------------------------------------------------------------------------
# FACTS FROM THE STEM (comparative balances)
# ---------------------------------------------------------------------------
EQUIP_BEG = m(450_000)          # Equipment, Dec 31, 2025
EQUIP_END = m(680_000)          # Equipment, Dec 31, 2026
AD_BEG = m(140_000)             # Accumulated depreciation--equipment, Dec 31, 2025
AD_END = m(175_000)             # Accumulated depreciation--equipment, Dec 31, 2026
INVEST_BEG = m(50_000)          # Debt investments (amortized cost), Dec 31, 2025
INVEST_END = m(67_000)          # Debt investments (amortized cost), Dec 31, 2026
NOTES_BEG = m(130_000)          # Long-term notes receivable (nontrade), Dec 31, 2025
NOTES_END = m(88_000)           # Long-term notes receivable (nontrade), Dec 31, 2026

# FACTS FROM THE STEM (additional information for 2026)
SOLD_EQUIP_COST = m(60_000)     # (1) cost of equipment sold
SOLD_EQUIP_AD = m(38_000)       # (1) accumulated depreciation on equipment sold
SOLD_EQUIP_PROCEEDS = m(25_000)  # (1) cash received on sale
DEPRECIATION_EXPENSE = m(73_000)  # (2) year-end adjusting entry
# (3) all equipment purchases were cash purchases
INVEST_PURCHASED = m(40_000)    # (4) debt investments purchased for cash
INVEST_SOLD_CARRYING = m(23_000)  # (4) carrying amount of investments sold
INVEST_SOLD_PROCEEDS = m(26_000)  # (4) cash received on sale of investments
LOAN_ADVANCED = m(22_000)       # (5) new nontrade loan advanced, cash out
PRINCIPAL_COLLECTED = m(64_000)  # (5) principal collections on notes receivable
# (6) no other investing activities


# ---------------------------------------------------------------------------
# (b) SUBSEQUENT-MEASUREMENT SCHEDULES: EQUIPMENT AND ACCUMULATED DEPRECIATION
# ---------------------------------------------------------------------------
# Equipment at cost rollforward, solved for the single unknown (cash purchases):
#   EQUIP_BEG + purchases - SOLD_EQUIP_COST = EQUIP_END
equipment_purchases = m(EQUIP_END - EQUIP_BEG + SOLD_EQUIP_COST)

# Verify the solved figure closes the schedule.
assert m(EQUIP_BEG + equipment_purchases - SOLD_EQUIP_COST) == EQUIP_END, "Equipment rollforward does not tie"

# Accumulated depreciation rollforward: both endpoints given, so this is a
# consistency check on depreciation expense and the AD removed on disposal.
ad_computed_end = m(AD_BEG + DEPRECIATION_EXPENSE - SOLD_EQUIP_AD)
assert ad_computed_end == AD_END, (
    f"Accumulated depreciation rollforward does not tie: computed {ad_computed_end} vs given {AD_END}"
)

# ---------------------------------------------------------------------------
# (c) SUBSEQUENT-MEASUREMENT SCHEDULES: DEBT INVESTMENTS AND NOTES RECEIVABLE
# ---------------------------------------------------------------------------
invest_computed_end = m(INVEST_BEG + INVEST_PURCHASED - INVEST_SOLD_CARRYING)
assert invest_computed_end == INVEST_END, (
    f"Debt investments rollforward does not tie: computed {invest_computed_end} vs given {INVEST_END}"
)

notes_computed_end = m(NOTES_BEG + LOAN_ADVANCED - PRINCIPAL_COLLECTED)
assert notes_computed_end == NOTES_END, (
    f"Notes receivable rollforward does not tie: computed {notes_computed_end} vs given {NOTES_END}"
)

# ---------------------------------------------------------------------------
# DISPOSAL GAINS / LOSSES (needed to balance the journal entries)
# ---------------------------------------------------------------------------
equip_carrying_at_sale = m(SOLD_EQUIP_COST - SOLD_EQUIP_AD)
equip_gain = m(SOLD_EQUIP_PROCEEDS - equip_carrying_at_sale)
invest_gain = m(INVEST_SOLD_PROCEEDS - INVEST_SOLD_CARRYING)

# ---------------------------------------------------------------------------
# JOURNAL ENTRIES
# ---------------------------------------------------------------------------
ZERO = m(0)


def line(account, debit=ZERO, credit=ZERO):
    return {"account": account, "debit": m(debit), "credit": m(credit)}


journal_entries = []


def add_entry(part, description, lines):
    total_debits = sum((ln["debit"] for ln in lines), ZERO)
    total_credits = sum((ln["credit"] for ln in lines), ZERO)
    assert total_debits == total_credits, (
        f"Entry '{description}' out of balance: debits {total_debits} vs credits {total_credits}"
    )
    journal_entries.append({"part": part, "description": description, "lines": lines})


# (a) period-end adjusting entry for depreciation
add_entry("a", "Dec. 31, 2026 adjusting entry -- depreciation on equipment", [
    line("Depreciation Expense", debit=DEPRECIATION_EXPENSE),
    line("Accumulated Depreciation-Equipment", credit=DEPRECIATION_EXPENSE),
])

# (d) equipment sale JE
sale_lines = [
    line("Cash", debit=SOLD_EQUIP_PROCEEDS),
    line("Accumulated Depreciation-Equipment", debit=SOLD_EQUIP_AD),
    line("Equipment", credit=SOLD_EQUIP_COST),
]
if equip_gain > 0:
    sale_lines.append(line("Gain on Disposal of Equipment", credit=equip_gain))
elif equip_gain < 0:
    sale_lines.insert(2, line("Loss on Disposal of Equipment", debit=-equip_gain))
add_entry("d", "Sale of equipment for cash", sale_lines)

# (d) equipment purchase JE (solved amount from the schedule in part b)
add_entry("d", "Purchase of equipment for cash", [
    line("Equipment", debit=equipment_purchases),
    line("Cash", credit=equipment_purchases),
])

# (e) debt investment purchase JE
add_entry("e", "Purchase of debt investments for cash", [
    line("Debt Investments", debit=INVEST_PURCHASED),
    line("Cash", credit=INVEST_PURCHASED),
])

# (e) debt investment sale JE
invest_sale_lines = [
    line("Cash", debit=INVEST_SOLD_PROCEEDS),
    line("Debt Investments", credit=INVEST_SOLD_CARRYING),
]
if invest_gain > 0:
    invest_sale_lines.append(line("Gain on Sale of Debt Investments", credit=invest_gain))
elif invest_gain < 0:
    invest_sale_lines.insert(1, line("Loss on Sale of Debt Investments", debit=-invest_gain))
add_entry("e", "Sale of debt investments for cash", invest_sale_lines)

# (e) nontrade loan advanced
add_entry("e", "Nontrade loan advanced (cash lent)", [
    line("Notes Receivable", debit=LOAN_ADVANCED),
    line("Cash", credit=LOAN_ADVANCED),
])

# (e) principal collections on notes receivable
add_entry("e", "Principal collections on notes receivable", [
    line("Cash", debit=PRINCIPAL_COLLECTED),
    line("Notes Receivable", credit=PRINCIPAL_COLLECTED),
])

# ---------------------------------------------------------------------------
# (f) CASH FLOWS FROM INVESTING ACTIVITIES
# ---------------------------------------------------------------------------
# Inflows positive, outflows negative. Gains/losses are non-cash reconciling
# items belonging to operating activities, so only gross proceeds appear here.
investing_lines = [
    ("Purchase of equipment", m(-equipment_purchases)),
    ("Proceeds from sale of equipment", SOLD_EQUIP_PROCEEDS),
    ("Purchase of debt investments", m(-INVEST_PURCHASED)),
    ("Proceeds from sale of debt investments", INVEST_SOLD_PROCEEDS),
    ("Loan advanced (nontrade note receivable issued)", m(-LOAN_ADVANCED)),
    ("Principal collected on notes receivable", PRINCIPAL_COLLECTED),
]

net_investing = sum((amt for _, amt in investing_lines), ZERO)
net_investing = m(net_investing)

# Footing check: recompute independently as inflows minus outflows.
inflows = sum((amt for _, amt in investing_lines if amt > 0), ZERO)
outflows = sum((-amt for _, amt in investing_lines if amt < 0), ZERO)
assert m(inflows - outflows) == net_investing, "Investing section does not foot"

# ---------------------------------------------------------------------------
# REPORTED ANSWERS -- only figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "b: cash paid to purchase equipment (solved from equipment schedule)",
     "value": out(equipment_purchases)},
]
for label, amount in investing_lines:
    answers.append({"label": f"f: investing activities -- {label}", "value": out(amount)})
answers.append({
    "label": "f: net cash provided (used) by investing activities",
    "value": out(net_investing),
})

result = {
    "id": "agent_297#01",
    "rounding_convention": (
        "ROUND_HALF_UP per period, quantized to the cent as each money figure is produced; "
        "decimal.Decimal throughout, no floats. No present-value discounting in this item, "
        "so no PV table factor vs exact formula choice applies."
    ),
    "answers": answers,
    "journal_entries": [
        {
            "part": e["part"],
            "description": e["description"],
            "lines": [
                {"account": ln["account"], "debit": out(ln["debit"]), "credit": out(ln["credit"])}
                for ln in e["lines"]
            ],
        }
        for e in journal_entries
    ],
    "insufficient_info": False,
    "notes": (
        "Equipment purchases solved from the cost rollforward: 680,000 - 450,000 + 60,000 = 290,000 "
        "(all purchases were cash per fact 3). AD, debt investment, and notes receivable rollforwards "
        "all tie to the given ending balances. Gains on the equipment sale (3,000) and the debt "
        "investment sale (3,000) are operating-section reconciling items, not investing cash flows, so "
        "only gross proceeds are reported in (f). Debt investments are amortized cost and explicitly "
        "not held for trading/resale, and the notes receivable are nontrade lending, so all four of "
        "those flows are investing rather than operating."
    ),
}

print(json.dumps(result, indent=2))
