#!/usr/bin/env python3
"""Blind solver for item agent_187#02 - Harborcrest Supply Co. (LO 9-9).

Topic: LIFO reserve / FIFO-to-LIFO period-end conversion entry, restated
subsequent-measurement ratio schedule (LIFO as reported vs FIFO as if), and a
FIFO peer comparison.

=====================================================================
ROUNDING CONVENTION (applied deliberately, decimal.ROUND_HALF_UP only)
=====================================================================
* All money is decimal.Decimal. No floats are used anywhere in the
  computation; floats appear only at JSON serialization time.
* Dollar amounts: quantized to the cent (0.01) with ROUND_HALF_UP. Every
  dollar figure in this fact pattern happens to be an exact whole dollar,
  so no cent-level rounding actually bites.
* Ratios (inventory turnover): ROUND_HALF_UP to 2 decimal places, stated in
  "times".
* Average days in inventory: 365-day year. Computed as
  365 / (turnover ALREADY ROUNDED to 2 dp), then ROUND_HALF_UP to 1 decimal
  place. This is round-per-step (chained), matching the intermediate-
  accounting textbook presentation where the displayed turnover ratio is the
  divisor, and matching the course's "ROUND_HALF_UP per period" rule (round
  at each reported step rather than only at the end). The alternative
  round-at-end figures (365 / unrounded turnover) are computed as well and
  reported in "notes" for transparency; they differ by 0.1 day in two places.
* Percentages (gross profit %): ROUND_HALF_UP to 1 decimal place, expressed
  in percent (32.1 means 32.1%).
* Part (e) is a written interpretation, not a figure, so it produces no
  entry in "answers" (only figures the Required parts ask for are reported).

Run: python3 solver.py   ->  prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
TWO_DP = Decimal("0.01")
ONE_DP = Decimal("0.1")
DAYS_IN_YEAR = Decimal("365")


def money(x: Decimal) -> Decimal:
    """Quantize a dollar amount to the cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def ratio2(x: Decimal) -> Decimal:
    """Quantize a ratio to 2 decimal places, ROUND_HALF_UP."""
    return x.quantize(TWO_DP, rounding=ROUND_HALF_UP)


def one_dp(x: Decimal) -> Decimal:
    """Quantize to 1 decimal place, ROUND_HALF_UP."""
    return x.quantize(ONE_DP, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem, nothing else)
# ---------------------------------------------------------------------------
# Harborcrest Supply Co.: internal perpetual records on FIFO, converted to
# LIFO for external reporting at year-end. Acquisition costs are RISING.
LIFO_INV_Y2 = Decimal("480000")        # Inventory (LIFO, as reported) 12/31/Y2
LIFO_INV_Y3 = Decimal("510000")        # Inventory (LIFO, as reported) 12/31/Y3
LIFO_RESERVE_Y2 = Decimal("72000")     # FIFO inventory - LIFO inventory, Y2
LIFO_RESERVE_Y3 = Decimal("95000")     # FIFO inventory - LIFO inventory, Y3

NET_SALES_Y3 = Decimal("4200000")
LIFO_COGS_Y3 = Decimal("2850000")      # COGS (LIFO, as reported), Year 3

# Peer: Maplebridge Retailers Inc. (FIFO), Year 3
PEER_BEG_INV = Decimal("560000")
PEER_END_INV = Decimal("590000")
PEER_COGS = Decimal("2750000")


# ---------------------------------------------------------------------------
# (a) Increase in the LIFO reserve for Year 3 + the conversion adjusting entry
# ---------------------------------------------------------------------------
# The reserve is the cumulative excess of FIFO inventory over LIFO inventory.
# Its change for the year is the amount by which LIFO COGS must exceed FIFO
# COGS, i.e. the size of the period-end conversion entry.
reserve_increase = money(LIFO_RESERVE_Y3 - LIFO_RESERVE_Y2)

# Books are kept on FIFO; converting to LIFO when costs rise raises COGS and
# lowers the carrying amount of inventory through a contra/allowance account.
je_a = {
    "part": "a",
    "description": (
        "Year-end entry converting FIFO internal records to LIFO for external "
        "reporting (increase in LIFO reserve)"
    ),
    "lines": [
        {"account": "Cost of Goods Sold", "debit": reserve_increase,
         "credit": Decimal("0")},
        {"account": "Allowance to Reduce Inventory to LIFO (LIFO Reserve)",
         "debit": Decimal("0"), "credit": reserve_increase},
    ],
}

# ---------------------------------------------------------------------------
# (b) FIFO inventory at each date, and FIFO COGS for Year 3
# ---------------------------------------------------------------------------
# FIFO inventory = LIFO inventory (as reported) + LIFO reserve.
fifo_inv_y2 = money(LIFO_INV_Y2 + LIFO_RESERVE_Y2)
fifo_inv_y3 = money(LIFO_INV_Y3 + LIFO_RESERVE_Y3)

# FIFO COGS = LIFO COGS - increase in the LIFO reserve (back out the entry).
fifo_cogs_y3 = money(LIFO_COGS_Y3 - reserve_increase)

# Internal consistency check (not reported): purchases implied by each basis
# must agree.  LIFO: BI + P - EI = COGS  ->  P = COGS - BI + EI
_purchases_from_lifo = LIFO_COGS_Y3 - LIFO_INV_Y2 + LIFO_INV_Y3
_fifo_cogs_check = fifo_inv_y2 + _purchases_from_lifo - fifo_inv_y3
assert _fifo_cogs_check == fifo_cogs_y3, (_fifo_cogs_check, fifo_cogs_y3)


# ---------------------------------------------------------------------------
# (c) Ratio comparison schedule for Harborcrest, Year 3
# ---------------------------------------------------------------------------
def ratio_block(beg_inv: Decimal, end_inv: Decimal, cogs: Decimal,
                sales: Decimal):
    """Average inventory, turnover, days, gross profit, gross profit %."""
    avg_inv = money((beg_inv + end_inv) / Decimal("2"))
    turnover_exact = cogs / avg_inv
    turnover = ratio2(turnover_exact)
    # Chained rounding: divide 365 by the ROUNDED turnover (see docstring).
    days = one_dp(DAYS_IN_YEAR / turnover)
    days_alt = one_dp(DAYS_IN_YEAR / turnover_exact)  # round-at-end variant
    gross_profit = money(sales - cogs)
    gp_pct = one_dp(gross_profit / sales * Decimal("100"))
    return {
        "average_inventory": avg_inv,
        "inventory_turnover": turnover,
        "average_days_in_inventory": days,
        "average_days_in_inventory_round_at_end": days_alt,
        "gross_profit": gross_profit,
        "gross_profit_percentage": gp_pct,
    }


lifo_block = ratio_block(LIFO_INV_Y2, LIFO_INV_Y3, LIFO_COGS_Y3, NET_SALES_Y3)
fifo_block = ratio_block(fifo_inv_y2, fifo_inv_y3, fifo_cogs_y3, NET_SALES_Y3)

# ---------------------------------------------------------------------------
# (d) Maplebridge (FIFO peer) Year 3 turnover and average days in inventory
# ---------------------------------------------------------------------------
peer_avg_inv = money((PEER_BEG_INV + PEER_END_INV) / Decimal("2"))
peer_turnover_exact = PEER_COGS / peer_avg_inv
peer_turnover = ratio2(peer_turnover_exact)
peer_days = one_dp(DAYS_IN_YEAR / peer_turnover)
peer_days_alt = one_dp(DAYS_IN_YEAR / peer_turnover_exact)

# ---------------------------------------------------------------------------
# (e) Interpretation - narrative, no figures reported.
# ---------------------------------------------------------------------------

answers = [
    {"label": "a: increase in LIFO reserve for Year 3",
     "value": reserve_increase},

    {"label": "b: FIFO inventory at Dec 31, Year 2", "value": fifo_inv_y2},
    {"label": "b: FIFO inventory at Dec 31, Year 3", "value": fifo_inv_y3},
    {"label": "b: FIFO cost of goods sold for Year 3", "value": fifo_cogs_y3},

    {"label": "c: LIFO (as reported) average inventory",
     "value": lifo_block["average_inventory"]},
    {"label": "c: LIFO (as reported) inventory turnover",
     "value": lifo_block["inventory_turnover"]},
    {"label": "c: LIFO (as reported) average days in inventory",
     "value": lifo_block["average_days_in_inventory"]},
    {"label": "c: LIFO (as reported) gross profit",
     "value": lifo_block["gross_profit"]},
    {"label": "c: LIFO (as reported) gross profit percentage",
     "value": lifo_block["gross_profit_percentage"]},

    {"label": "c: FIFO (as if) average inventory",
     "value": fifo_block["average_inventory"]},
    {"label": "c: FIFO (as if) inventory turnover",
     "value": fifo_block["inventory_turnover"]},
    {"label": "c: FIFO (as if) average days in inventory",
     "value": fifo_block["average_days_in_inventory"]},
    {"label": "c: FIFO (as if) gross profit",
     "value": fifo_block["gross_profit"]},
    {"label": "c: FIFO (as if) gross profit percentage",
     "value": fifo_block["gross_profit_percentage"]},

    {"label": "d: Maplebridge Year 3 inventory turnover",
     "value": peer_turnover},
    {"label": "d: Maplebridge Year 3 average days in inventory",
     "value": peer_days},
]

# Debits must equal credits on every entry prepared.
for _je in (je_a,):
    _d = sum((ln["debit"] for ln in _je["lines"]), Decimal("0"))
    _c = sum((ln["credit"] for ln in _je["lines"]), Decimal("0"))
    assert _d == _c, (_je["part"], _d, _c)

notes = (
    "Rising costs, so the LIFO reserve grows: LIFO COGS exceeds FIFO COGS by "
    "the $23,000 increase, and LIFO ending inventory is $95,000 below FIFO. "
    "(e) Interpretation: as reported, Harborcrest turns inventory 5.76 times "
    "(63.4 days) versus Maplebridge's 4.78 times (76.4 days), so Harborcrest "
    "looks markedly faster - but that is a measurement artifact: LIFO puts "
    "old, low costs in inventory (small denominator) and current, high costs "
    "in COGS (large numerator), inflating turnover on both sides of the "
    "fraction. Restated to FIFO, Harborcrest turns 4.89 times (74.6 days), "
    "essentially the same as the FIFO peer, so the apparent advantage nearly "
    "disappears; method matters because ratios are only comparable across "
    "firms after they are placed on the same cost-flow assumption, which the "
    "LIFO reserve disclosure makes possible. "
    "Rounding sensitivity: average days computed instead as 365 divided by "
    "the UNROUNDED turnover would give LIFO 63.4, FIFO 74.7, Maplebridge "
    "76.3; the reported figures use the rounded (2-dp) turnover as divisor."
)

out = {
    "id": "agent_187#02",
    "rounding_convention": (
        "ROUND_HALF_UP throughout; dollars to the cent (all figures whole "
        "dollars); inventory turnover to 2 decimals; average days in "
        "inventory = 365 / rounded turnover, to 1 decimal (round-per-step); "
        "gross profit percentage to 1 decimal"
    ),
    "answers": answers,
    "journal_entries": [je_a],
    "insufficient_info": False,
    "notes": notes,
}


def _plain(x):
    """Serialize Decimal as a plain JSON number (int when integral)."""
    if isinstance(x, Decimal):
        return int(x) if x == x.to_integral_value() else float(x)
    raise TypeError(repr(x))


if __name__ == "__main__":
    print(json.dumps(out, indent=2, default=_plain))
