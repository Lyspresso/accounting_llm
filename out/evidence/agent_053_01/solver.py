#!/usr/bin/env python3
"""Solver for item agent_053#01 — Northfork Merchandising LLC, LIFO reserve twin (LO 9-6).

FACT PATTERN (from stem.md)
--------------------------
Northfork Merchandising LLC keeps internal records at AVERAGE COST and converts to
LIFO at year-end for EXTERNAL reporting. Year 1 is the first year of operations, so
the opening LIFO reserve / allowance balance is 0. The conversion is recognized
*in the accounts* (i.e., a real allowance account is carried, not a note-only
disclosure).

    Date            Ending inv. @ average cost     Ending inv. @ LIFO
    Dec 31, Yr 1              90,000                      55,000
    Dec 31, Yr 2             105,000                      62,000
    Dec 31, Yr 3              98,000                      70,000

MODEL
-----
LIFO reserve (required allowance balance) at each year-end
    = inventory at the internal method (average cost) - inventory at LIFO.

The allowance ("Allowance to Reduce Inventory to LIFO Basis") is a contra-asset
adjusted at each period end to the required balance. The adjusting amount is the
CHANGE in the reserve, and the offsetting side is Cost of Goods Sold:

    reserve increases -> Dr Cost of Goods Sold / Cr Allowance
    reserve decreases -> Dr Allowance          / Cr Cost of Goods Sold

Balance-sheet presentation (gross internal method, allowance, net LIFO):
    Inventory at average cost               XXX
    Less: Allowance to reduce inv. to LIFO (XXX)
    Inventory at LIFO (net)                 XXX

Cumulative effect on COGS across Years 1-3 = sum of the signed changes in the
reserve (debits positive, credits negative); a positive total is a net DEBIT to
COGS (COGS increased). Because the reserve began at zero in Year 1, this must
equal the Year 3 ending reserve balance — that identity is asserted below as an
internal consistency check (it is not reported as an answer).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to the cent (Decimal quantize to 0.01) per period; every figure in
this fact pattern is a whole dollar, so no rounding is actually triggered — the
quantization is applied deliberately at each period end (round-per-period, not
round-at-end) rather than carrying unrounded residue forward. All money uses
decimal.Decimal; floats are never used. No present-value factors are involved in
this item.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(x):
    """Quantize to cents with ROUND_HALF_UP (applied per period)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def out(d):
    """Render a Decimal for JSON: int when whole, else float-free string-safe number."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- fact pattern
YEARS = [1, 2, 3]
AVG_COST = {
    1: money("90000"),
    2: money("105000"),
    3: money("98000"),
}
LIFO = {
    1: money("55000"),
    2: money("62000"),
    3: money("70000"),
}

ALLOWANCE = "Allowance to Reduce Inventory to LIFO Basis"
COGS = "Cost of Goods Sold"

# ------------------------------------------------- (a) reserve and change/year
reserve = {}
for y in YEARS:
    reserve[y] = money(AVG_COST[y] - LIFO[y])

delta = {}
prior = money("0")  # Year 1 is the first year of operations -> opening reserve 0
for y in YEARS:
    delta[y] = money(reserve[y] - prior)
    prior = reserve[y]

# ------------------------------------------------------- (b),(c) journal entries
journal_entries = []
for y in YEARS:
    amt = delta[y]
    part = "b" if y == 1 else "c"
    if amt > 0:
        lines = [
            {"account": COGS, "debit": out(amt), "credit": 0},
            {"account": ALLOWANCE, "debit": 0, "credit": out(amt)},
        ]
    elif amt < 0:
        amt_abs = money(-amt)
        lines = [
            {"account": ALLOWANCE, "debit": out(amt_abs), "credit": 0},
            {"account": COGS, "debit": 0, "credit": out(amt_abs)},
        ]
    else:
        lines = []
    if lines:
        journal_entries.append(
            {
                "part": part,
                "date": "December 31, Year %d" % y,
                "lines": lines,
            }
        )

# ---------------------------------------------- (d) Dec 31 Year 3 balance sheet
bs_gross = AVG_COST[3]
bs_allowance = reserve[3]
bs_net = money(bs_gross - bs_allowance)

# --------------------------- (e) cumulative effect on COGS from reserve entries
cumulative_cogs = money(sum((delta[y] for y in YEARS), Decimal("0")))
cumulative_direction = (
    "net debit (increase) to Cost of Goods Sold"
    if cumulative_cogs > 0
    else "net credit (decrease) to Cost of Goods Sold"
)

# --------------------------------------------------------- internal assertions
# Debits must equal credits in every entry.
for je in journal_entries:
    dr = sum((Decimal(str(l["debit"])) for l in je["lines"]), Decimal("0"))
    cr = sum((Decimal(str(l["credit"])) for l in je["lines"]), Decimal("0"))
    assert dr == cr, "unbalanced entry: %s" % je
# Net presentation must reproduce reported LIFO inventory.
assert bs_net == LIFO[3], "balance sheet net does not tie to LIFO inventory"
# Reserve began at zero, so cumulative COGS effect == ending reserve balance.
assert cumulative_cogs == reserve[3], "cumulative COGS effect does not tie to reserve"

answers = [
    {"label": "a: LIFO reserve at December 31, Year 1", "value": out(reserve[1])},
    {"label": "a: LIFO reserve at December 31, Year 2", "value": out(reserve[2])},
    {"label": "a: LIFO reserve at December 31, Year 3", "value": out(reserve[3])},
    {
        "label": "a: change in LIFO reserve, Year 1 (increase)",
        "value": out(delta[1]),
    },
    {
        "label": "a: change in LIFO reserve, Year 2 (increase)",
        "value": out(delta[2]),
    },
    {
        "label": "a: change in LIFO reserve, Year 3 (decrease)",
        "value": out(delta[3]),
    },
    {
        "label": "d: Inventory at average cost (gross), December 31, Year 3",
        "value": out(bs_gross),
    },
    {
        "label": "d: Less allowance to reduce inventory to LIFO basis, December 31, Year 3",
        "value": out(bs_allowance),
    },
    {
        "label": "d: Inventory at LIFO (net), December 31, Year 3",
        "value": out(bs_net),
    },
    {
        "label": "e: cumulative effect on Cost of Goods Sold, Years 1-3 (net debit / increase)",
        "value": out(cumulative_cogs),
    },
]

result = {
    "id": "agent_053#01",
    "rounding_convention": (
        "ROUND_HALF_UP to the cent, applied per period (round-per-period, not "
        "round-at-end); decimal.Decimal throughout, no floats. All amounts are "
        "whole dollars so no rounding is triggered. No PV factors involved."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Internal method is average cost, so the reserve is average cost less LIFO. "
        "Year 1 is the first year of operations, so the opening allowance is zero and "
        "the Year 1 entry creates the allowance. Year 3's reserve falls, so the Year 3 "
        "entry debits the allowance and credits COGS. Sign convention: the Year 3 "
        "change is reported as -15000 (a decrease in the reserve). Textbook account "
        "title is 'Allowance to Reduce FIFO Inventory to LIFO Basis' (Demo 9-6); it is "
        "given here as 'Allowance to Reduce Inventory to LIFO Basis' because the "
        "internal method is average cost, not FIFO."
    ),
}

print(json.dumps(result, indent=2))
