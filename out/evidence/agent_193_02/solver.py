#!/usr/bin/env python3
"""Solver for item agent_193#02 — LO 10-6, accounting changes in inventory method.

FACT PATTERN (from stem.md only)
--------------------------------
Part A — Pinecrest Retail Group. Reported on FIFO in Year 1 and Year 2.
Changes to LIFO on January 1, Year 3. Reconstructing prior LIFO layers is
impracticable. Ignore taxes.
    Net income:        Y1 (FIFO) 200,000 | Y2 (FIFO) 240,000 | Y3 (LIFO) 210,000
    Ending inventory:  Y1 (FIFO) 150,000 | Y2 (FIFO) 180,000 | Y3 (LIFO) 165,000

Part B — Oakridge Parts Co. Changes from average cost to FIFO on
January 1, Year 3. Ignore taxes.
    Inventory at Dec 31:   Year 2            Year 1
        Average cost       180,000           140,000
        FIFO               150,000           120,000

REASONING
---------
Part A (a, b).  A change TO LIFO is the standard exception to retrospective
application: when earlier LIFO layers cannot be reconstructed, the change is
applied PROSPECTIVELY.  There is no cumulative-effect computation, so there is
NO January 1, Year 3 journal entry.  The carrying amount of inventory under the
OLD method at the beginning of the year of change — the December 31, Year 2
FIFO balance — simply becomes the opening LIFO cost basis, i.e. the LIFO BASE
LAYER.  Years 1 and 2 are NOT restated; they continue to be labeled FIFO in the
comparative schedule, and only Year 3 is labeled LIFO.  Disclosure of the effect
of the change replaces restatement.

    base_layer = FIFO ending inventory, December 31, Year 2

Part B (c, d, e).  Average cost -> FIFO is applied RETROSPECTIVELY.  The
cumulative effect at the date of change is the difference between the two
measurements of the December 31, Year 2 (= January 1, Year 3) inventory.  FIFO
is LOWER here, so inventory is written DOWN and retained earnings is charged:

    cumulative_effect_Y3_open = avg_cost(Dec 31 Y2) - FIFO(Dec 31 Y2)      (asset decrease)
    Entry 1/1/Y3:   Dr Retained Earnings  X   /   Cr Inventory  X

(d)  On Year 3 comparative balance sheets the December 31, Year 2 inventory is
presented on the NEW (FIFO) basis: the FIFO figure, not the average-cost figure.
When Years 2 and 3 are shown comparatively, Year 2 is the earliest period
presented, so the portion of the cumulative effect attributable to periods
BEFORE Year 2 is charged against the OPENING retained earnings of Year 2.  That
pre-Year-2 portion is the December 31, Year 1 measurement difference:

    prior_period_effect = avg_cost(Dec 31 Y1) - FIFO(Dec 31 Y1)            (RE decrease)

(e)  Accounting-equation settlement.  Assets fall by the full cumulative effect;
equity falls by the same amount, split between the opening-retained-earnings
charge for pre-Year-2 periods and the restatement of Year 2 income:

    year2_income_effect = cumulative_effect_Y3_open - prior_period_effect
    (cross-check: FIFO COGS(Y2) - avg COGS(Y2)
        = [FIFO_BI_Y2 + P - FIFO_EI_Y2] - [avg_BI_Y2 + P - avg_EI_Y2]
        = (FIFO_BI_Y2 - avg_BI_Y2) + (avg_EI_Y2 - FIFO_EI_Y2)
        -- purchases P cancel, so the result is independent of purchases.)

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, applied per computed amount, to the cent (Decimal exponent
0.01); all source amounts are exact whole dollars and every operation is
addition/subtraction, so no rounding is actually invoked — the quantizer is
applied deliberately at each output so the convention is explicit and
reproducible. No present-value factors are involved in this item.
All money is decimal.Decimal; floats are never used.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to cents using the course convention, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-safe number: int when the cents are zero, else float-free string-parsed Decimal."""
    q = money(x)
    return int(q) if q == q.to_integral_value() else float(q)


# ---------------------------------------------------------------------------
# Given facts — transcribed from the stem, nothing else.
# ---------------------------------------------------------------------------

# Part A — Pinecrest Retail Group
A_NET_INCOME = {
    "Year 1": Decimal("200000"),
    "Year 2": Decimal("240000"),
    "Year 3": Decimal("210000"),
}
A_ENDING_INV = {
    "Year 1": Decimal("150000"),
    "Year 2": Decimal("180000"),
    "Year 3": Decimal("165000"),
}
# Method actually used to produce each reported figure (per the stem's column heads)
A_METHOD_AS_REPORTED = {"Year 1": "FIFO", "Year 2": "FIFO", "Year 3": "LIFO"}

# Part B — Oakridge Parts Co.
B_AVG = {"Year 1": Decimal("140000"), "Year 2": Decimal("180000")}
B_FIFO = {"Year 1": Decimal("120000"), "Year 2": Decimal("150000")}


# ---------------------------------------------------------------------------
# Part A — prospective change to LIFO
# ---------------------------------------------------------------------------

# (a) No cumulative effect is computed under prospective application, so there
#     is no entry. Represent that as a zero-dollar adjustment, derived rather
#     than asserted: prospective application charges nothing to any account.
a_entry_amount = money(Decimal("0"))

# (b) Prospective => prior years are not restated. The schedule is the reported
#     figures with their original method labels; only Year 3 is LIFO.
a_schedule = []
for yr in ("Year 1", "Year 2", "Year 3"):
    a_schedule.append(
        {
            "year": yr,
            "method_after_change": A_METHOD_AS_REPORTED[yr],
            "net_income": money(A_NET_INCOME[yr]),
            "ending_inventory": money(A_ENDING_INV[yr]),
            "restated": False,
        }
    )

# LIFO base layer = carrying amount of inventory under the OLD method at the
# beginning of the year of change = FIFO ending inventory at December 31, Year 2.
lifo_base_layer = money(A_ENDING_INV["Year 2"])


# ---------------------------------------------------------------------------
# Part B — retrospective change from average cost to FIFO
# ---------------------------------------------------------------------------

# Cumulative effect at the date of change (Jan 1, Year 3 == Dec 31, Year 2).
# Positive number = inventory (asset) must be reduced, RE charged.
cumulative_effect = money(B_AVG["Year 2"] - B_FIFO["Year 2"])

# Portion attributable to periods prior to Year 2 (= the Dec 31, Year 1 gap).
prior_period_effect = money(B_AVG["Year 1"] - B_FIFO["Year 1"])

# Portion attributable to Year 2 itself.
year2_income_effect = money(cumulative_effect - prior_period_effect)

# Cross-check the Year 2 income effect independently via cost of goods sold.
# Purchases cancel, so they need not be known.
cogs_check = money(
    (B_FIFO["Year 1"] - B_AVG["Year 1"]) + (B_AVG["Year 2"] - B_FIFO["Year 2"])
)
assert cogs_check == year2_income_effect, (cogs_check, year2_income_effect)

# (c) Retrospective entry, January 1, Year 3.
c_lines = []
if cumulative_effect > 0:
    c_lines = [
        {
            "account": "Retained Earnings",
            "debit": num(cumulative_effect),
            "credit": 0,
        },
        {
            "account": "Inventory",
            "debit": 0,
            "credit": num(cumulative_effect),
        },
    ]
elif cumulative_effect < 0:
    c_lines = [
        {"account": "Inventory", "debit": num(-cumulative_effect), "credit": 0},
        {"account": "Retained Earnings", "debit": 0, "credit": num(-cumulative_effect)},
    ]

# Debits must equal credits.
_dr = sum(Decimal(str(l["debit"])) for l in c_lines)
_cr = sum(Decimal(str(l["credit"])) for l in c_lines)
assert _dr == _cr, (_dr, _cr)

# (d) December 31, Year 2 inventory on Year 3 comparative balance sheets:
#     presented on the NEW method (FIFO).
d_inventory_reported_dec31_y2 = money(B_FIFO["Year 2"])
#     Adjustment to BEGINNING retained earnings of Year 2 for pre-Year-2 periods
#     when Years 2 and 3 are the periods presented (a decrease).
d_beginning_re_y2_adjustment = prior_period_effect

# (e) Accounting-equation settlement of the cumulative effect.
e_asset_change = money(-cumulative_effect)   # Inventory
e_equity_change = money(-cumulative_effect)  # Retained Earnings
assert e_asset_change == e_equity_change, "A = L + E must stay in balance"


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

answers = [
    {
        "label": "a: Part A — January 1, Year 3 journal entry for the FIFO-to-LIFO change (dollar amount; none required)",
        "value": num(a_entry_amount),
    },
    {
        "label": "b: Part A schedule — Year 1 net income (method after change: FIFO, not restated)",
        "value": num(a_schedule[0]["net_income"]),
    },
    {
        "label": "b: Part A schedule — Year 1 ending inventory (FIFO)",
        "value": num(a_schedule[0]["ending_inventory"]),
    },
    {
        "label": "b: Part A schedule — Year 2 net income (method after change: FIFO, not restated)",
        "value": num(a_schedule[1]["net_income"]),
    },
    {
        "label": "b: Part A schedule — Year 2 ending inventory (FIFO)",
        "value": num(a_schedule[1]["ending_inventory"]),
    },
    {
        "label": "b: Part A schedule — Year 3 net income (method after change: LIFO)",
        "value": num(a_schedule[2]["net_income"]),
    },
    {
        "label": "b: Part A schedule — Year 3 ending inventory (LIFO)",
        "value": num(a_schedule[2]["ending_inventory"]),
    },
    {
        "label": "b: Part A — LIFO base-layer amount at January 1, Year 3",
        "value": num(lifo_base_layer),
    },
    {
        "label": "c: Part B — cumulative effect recorded January 1, Year 3 (Dr Retained Earnings / Cr Inventory)",
        "value": num(cumulative_effect),
    },
    {
        "label": "d: Part B — inventory reported at December 31, Year 2 on Year 3 comparative balance sheets (FIFO basis)",
        "value": num(d_inventory_reported_dec31_y2),
    },
    {
        "label": "d: Part B — decrease in beginning retained earnings of Year 2 for periods prior to Year 2",
        "value": num(d_beginning_re_y2_adjustment),
    },
    {
        "label": "e: Part B settlement — change in assets (Inventory)",
        "value": num(e_asset_change),
    },
    {
        "label": "e: Part B settlement — change in equity (Retained Earnings)",
        "value": num(e_equity_change),
    },
]

journal_entries = [
    {
        "part": "a",
        "date": "January 1, Year 3",
        "lines": [],
        "memo": (
            "No entry. A change to LIFO when earlier layers cannot be reconstructed is "
            "applied prospectively: no cumulative effect is computed, prior years are not "
            "restated, and the December 31, Year 2 FIFO carrying amount of $"
            + f"{lifo_base_layer:,.0f}"
            + " simply becomes the opening LIFO cost basis (base layer). The change is "
            "handled through disclosure instead of a journal entry."
        ),
    },
    {
        "part": "c",
        "date": "January 1, Year 3",
        "lines": c_lines,
        "memo": (
            "Retrospective application of the change from average cost to FIFO. FIFO "
            "measures December 31, Year 2 inventory lower than average cost, so inventory "
            "is written down and the cumulative effect is charged to retained earnings "
            "(taxes ignored)."
        ),
    },
]

notes = (
    "Part A (a): no journal entry — a change TO LIFO with impracticable prior layers is "
    "applied prospectively. (b) Years 1 and 2 stay on FIFO and are not restated; only "
    "Year 3 is LIFO. The LIFO base layer is the December 31, Year 2 FIFO balance carried "
    "forward as the opening LIFO cost basis. "
    "Part B (e): the $"
    + f"{cumulative_effect:,.0f}"
    + " equity reduction is composed of $"
    + f"{prior_period_effect:,.0f}"
    + " charged to the beginning retained earnings of Year 2 (pre-Year-2 periods) and $"
    + f"{year2_income_effect:,.0f}"
    + " of additional Year 2 cost of goods sold that reduces restated Year 2 net income; "
    "assets and equity both fall by the full cumulative effect, so the accounting equation "
    "stays in balance. Sign convention: negative values in part e denote decreases."
)

out = {
    "id": "agent_193#02",
    "rounding_convention": (
        "ROUND_HALF_UP to the cent, applied per computed amount (round-at-each-output); "
        "all inputs are exact whole dollars and only addition/subtraction is used, so no "
        "rounding is materially invoked. No present-value factors in this item. "
        "decimal.Decimal throughout; no floats."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
