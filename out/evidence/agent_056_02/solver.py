#!/usr/bin/env python3
"""
Solver for item agent_056#02 -- Summitline Appliances Inc.
LIFO vs FIFO ratios, period-end LIFO conversion JE, comparability disclosure (LO 9-9).

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal. No floats anywhere. Ratio/percentage arithmetic
  also runs through Decimal (getcontext().prec = 28) so no binary float ever
  touches a reported figure.
* Money: ROUND_HALF_UP to 2 decimal places (every dollar figure in this fact
  pattern is a whole dollar, so no cent-level rounding is actually triggered).
* Inventory turnover: ROUND_HALF_UP to 2 decimals, as the stem directs.
* Average days in inventory: CHAINED rounding -- 365 / (turnover ALREADY ROUNDED
  to 2 decimals), then ROUND_HALF_UP the quotient to 2 decimals.
  This is the textbook's own convention, not a guess. Kieso/Intermediate
  Accounting 4e chapter 9 "Review 9-9" solution computes
      Year 2 turnover 5.36 ($10,077/$1,881), days 68.1 (365/5.36)
      Year 3 turnover 5.33 ($9,876/$1,852), days 68.5 (365/5.33)
  Year 3 is decisive: the unrounded turnover is 5.33261, and 365/5.33261 =
  68.4468 -> 68.4, but the book reports 68.5, which is 365/5.33 = 68.4803.
  So days is derived from the rounded turnover. Demo 9-9 shows the same
  notation ("365 / 2.82 = 129 days").
  The unrounded-turnover alternative is computed too and reported in notes as an
  acceptable-variant figure; it only differs for Summitline's LIFO basis
  (67.91 vs 67.84). It is NOT reported as an answer.
* Gross profit percentage: gross profit / net sales, ROUND_HALF_UP to 2 decimals
  expressed in percentage points (e.g. 38.57 means 38.57%).
* Average inventory = (beginning + ending) / 2, on the SAME cost-flow basis as
  the COGS in the numerator. This basis-matching is the whole point of part (e).

DERIVATION NOTES
----------------
(a) The Allowance to Reduce Inventory to LIFO (the LIFO reserve) is the
    FIFO-minus-LIFO spread. Its year-over-year INCREASE is the "LIFO effect" for
    the period and is the amount of the period-end conversion entry:
        Dr Cost of Goods Sold / Cr Allowance to Reduce Inventory to LIFO.
(b) Because the conversion entry is what turns FIFO COGS into LIFO COGS,
        LIFO COGS = FIFO COGS + increase in LIFO reserve
    so FIFO COGS = LIFO COGS - increase in reserve. (Costs rose, so the reserve
    grew and LIFO COGS is the larger of the two -- a directional sanity check.)
(c)-(e) Ratios computed from the matched basis; the FIFO "as if" column uses
    FIFO COGS from (b) over average FIFO inventory.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

CENT = Decimal("0.01")
DAYS_IN_YEAR = Decimal("365")


def money(x: Decimal) -> Decimal:
    """Round a dollar amount to cents, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def two_dp(x: Decimal) -> Decimal:
    """Round a ratio / percentage to two decimals, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """Render a Decimal for JSON as int when integral, else float-free string->float.

    Values are produced by Decimal arithmetic and only converted at the very
    last step, for JSON serialization.
    """
    if x == x.to_integral_value():
        return int(x)
    return float(x)


# ---------------------------------------------------------------------------
# Given fact pattern (stem only -- nothing here is an answer, all are inputs)
# ---------------------------------------------------------------------------
NET_SALES = Decimal("1400000")

# Summitline: internal FIFO records, external LIFO reporting
FIFO_INV_BEG = Decimal("180000")   # Dec 31, Year 2
FIFO_INV_END = Decimal("220000")   # Dec 31, Year 3
LIFO_INV_BEG = Decimal("150000")   # Dec 31, Year 2
LIFO_INV_END = Decimal("170000")   # Dec 31, Year 3
LIFO_COGS = Decimal("860000")      # Year 3, after conversion

# Peer: Flatiron Home Goods Co. (pure FIFO)
PEER_INV_BEG = Decimal("190000")
PEER_INV_END = Decimal("210000")
PEER_COGS = Decimal("830000")
PEER_NET_SALES = Decimal("1400000")


def average_inventory(beg: Decimal, end: Decimal) -> Decimal:
    return money((beg + end) / Decimal("2"))


def turnover(cogs: Decimal, avg_inv: Decimal) -> Decimal:
    """Inventory turnover = COGS / average inventory, rounded to 2 decimals."""
    return two_dp(cogs / avg_inv)


def days_from_rounded_turnover(rounded_turns: Decimal) -> Decimal:
    """Average days in inventory = 365 / (rounded turnover). Textbook chaining."""
    return two_dp(DAYS_IN_YEAR / rounded_turns)


def days_from_exact(cogs: Decimal, avg_inv: Decimal) -> Decimal:
    """Variant only: 365 / unrounded turnover. Reported in notes, not answers."""
    return two_dp(DAYS_IN_YEAR / (cogs / avg_inv))


def gross_profit(sales: Decimal, cogs: Decimal) -> Decimal:
    return money(sales - cogs)


def gross_profit_pct(gp: Decimal, sales: Decimal) -> Decimal:
    return two_dp(gp / sales * Decimal("100"))


# ---------------------------------------------------------------------------
# (a) Increase in the LIFO reserve + period-end conversion entry
# ---------------------------------------------------------------------------
reserve_beg = money(FIFO_INV_BEG - LIFO_INV_BEG)   # 30,000, agrees with stem table
reserve_end = money(FIFO_INV_END - LIFO_INV_END)   # 50,000, agrees with stem table
assert reserve_beg == Decimal("30000.00"), reserve_beg
assert reserve_end == Decimal("50000.00"), reserve_end

reserve_increase = money(reserve_end - reserve_beg)

# ---------------------------------------------------------------------------
# (b) FIFO COGS implied by the reserve change
# ---------------------------------------------------------------------------
fifo_cogs = money(LIFO_COGS - reserve_increase)
# Costs rose -> reserve grew -> LIFO COGS must exceed FIFO COGS.
assert LIFO_COGS > fifo_cogs

# Independent cross-check via the cost-of-goods-available identity:
# purchases are basis-independent, so
#   purchases = FIFO COGS - FIFO beg inv + FIFO end inv
#             = LIFO COGS - LIFO beg inv + LIFO end inv
purch_fifo = money(fifo_cogs - FIFO_INV_BEG + FIFO_INV_END)
purch_lifo = money(LIFO_COGS - LIFO_INV_BEG + LIFO_INV_END)
assert purch_fifo == purch_lifo, (purch_fifo, purch_lifo)

# ---------------------------------------------------------------------------
# (c) Summitline ratios: LIFO as reported vs FIFO as if
# ---------------------------------------------------------------------------
avg_inv_lifo = average_inventory(LIFO_INV_BEG, LIFO_INV_END)
avg_inv_fifo = average_inventory(FIFO_INV_BEG, FIFO_INV_END)

turns_lifo = turnover(LIFO_COGS, avg_inv_lifo)
turns_fifo = turnover(fifo_cogs, avg_inv_fifo)

days_lifo = days_from_rounded_turnover(turns_lifo)
days_fifo = days_from_rounded_turnover(turns_fifo)

gp_lifo = gross_profit(NET_SALES, LIFO_COGS)
gp_fifo = gross_profit(NET_SALES, fifo_cogs)

gp_pct_lifo = gross_profit_pct(gp_lifo, NET_SALES)
gp_pct_fifo = gross_profit_pct(gp_fifo, NET_SALES)

# Directional checks the textbook states for a rising-cost period:
assert LIFO_COGS > fifo_cogs          # COGS higher under LIFO
assert gp_lifo < gp_fifo              # gross profit lower under LIFO
assert turns_lifo > turns_fifo        # turnover higher under LIFO
assert days_lifo < days_fifo          # days lower under LIFO

# ---------------------------------------------------------------------------
# (d) Flatiron (FIFO peer)
# ---------------------------------------------------------------------------
avg_inv_peer = average_inventory(PEER_INV_BEG, PEER_INV_END)
turns_peer = turnover(PEER_COGS, avg_inv_peer)
days_peer = days_from_rounded_turnover(turns_peer)

# ---------------------------------------------------------------------------
# (e) FIFO-comparable restatement of Summitline for the peer comparison
# ---------------------------------------------------------------------------
turns_comparable = turnover(fifo_cogs, avg_inv_fifo)
days_comparable = days_from_rounded_turnover(turns_comparable)
# By construction this equals the FIFO "as if" column from (c).
assert turns_comparable == turns_fifo

# Variant days figures under the unrounded-turnover convention (notes only).
alt_days_lifo = days_from_exact(LIFO_COGS, avg_inv_lifo)
alt_days_fifo = days_from_exact(fifo_cogs, avg_inv_fifo)
alt_days_peer = days_from_exact(PEER_COGS, avg_inv_peer)

# ---------------------------------------------------------------------------
# Journal entry (a)
# ---------------------------------------------------------------------------
je_lines = [
    {
        "account": "Cost of Goods Sold",
        "debit": num(reserve_increase),
        "credit": 0,
    },
    {
        "account": "Allowance to Reduce Inventory to LIFO",
        "debit": 0,
        "credit": num(reserve_increase),
    },
]
assert sum(Decimal(str(l["debit"])) for l in je_lines) == sum(
    Decimal(str(l["credit"])) for l in je_lines
)

answers = [
    # (a)
    {"label": "a: increase in LIFO reserve (LIFO effect) for Year 3", "value": num(reserve_increase)},
    # (b)
    {"label": "b: Year 3 FIFO cost of goods sold", "value": num(fifo_cogs)},
    # (c) LIFO as reported
    {"label": "c: Summitline inventory turnover - LIFO (as reported)", "value": num(turns_lifo)},
    {"label": "c: Summitline average days in inventory - LIFO (as reported)", "value": num(days_lifo)},
    {"label": "c: Summitline gross profit - LIFO (as reported)", "value": num(gp_lifo)},
    {"label": "c: Summitline gross profit percentage - LIFO (as reported)", "value": num(gp_pct_lifo)},
    # (c) FIFO as if
    {"label": "c: Summitline inventory turnover - FIFO (as if)", "value": num(turns_fifo)},
    {"label": "c: Summitline average days in inventory - FIFO (as if)", "value": num(days_fifo)},
    {"label": "c: Summitline gross profit - FIFO (as if)", "value": num(gp_fifo)},
    {"label": "c: Summitline gross profit percentage - FIFO (as if)", "value": num(gp_pct_fifo)},
    # (d)
    {"label": "d: Flatiron inventory turnover", "value": num(turns_peer)},
    {"label": "d: Flatiron average days in inventory", "value": num(days_peer)},
    # (e)
    {"label": "e: Summitline inventory turnover restated on a FIFO-comparable basis", "value": num(turns_comparable)},
    {"label": "e: Summitline average days in inventory on a FIFO-comparable basis", "value": num(days_comparable)},
]

notes = (
    "Qualitative requirements. "
    "(e) The as-reported comparison is misleading because the two ratios are built from "
    "mismatched cost-flow bases: Summitline's numerator is LIFO COGS (which, in a rising-cost "
    "year, absorbs the newest and highest costs) while its denominator is LIFO inventory (frozen "
    "at old, low base-layer costs). Both effects push the ratio the same direction, so LIFO "
    "turnover of 5.38 overstates real inventory velocity relative to Flatiron's 4.15 and makes "
    "Summitline look far faster-moving than it is; the difference is an accounting-method "
    "artifact, not an operating difference. Adding the LIFO reserve back to both COGS and "
    "inventory puts Summitline on FIFO terms: turnover 4.20 (86.90 days) versus Flatiron's 4.15 "
    "(87.95 days) - essentially the same inventory velocity, which is the honest conclusion. "
    "(f) Two disclosure/presentation items: (1) state the inventory cost-flow method(s) used in "
    "the summary of significant accounting policies, including the fact that internal records are "
    "kept on FIFO and converted to LIFO for external reporting; and (2) disclose the LIFO reserve "
    "- the dollar amount of the Allowance to Reduce Inventory to LIFO at each balance sheet date "
    "(and the excess of FIFO/replacement cost over LIFO carrying amount), presenting the "
    "allowance as a deduction from inventory on the balance sheet so users can convert to a FIFO "
    "basis. Other acceptable items: disclose the current-year LIFO effect on COGS and income, "
    "any LIFO liquidation and its income effect, and the inventory composition by major class. "
    "Rounding variant: days computed from the UNROUNDED turnover instead of the rounded one "
    "would give LIFO 67.91 (vs 67.84 reported), FIFO 86.90, Flatiron 87.95; only the LIFO figure "
    "differs. The reported figures follow the textbook's own chained convention (Review 9-9 "
    "reports 68.5 = 365/5.33, not 68.4 = 365/5.33261)."
)

output = {
    "id": "agent_056#02",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats. Money ROUND_HALF_UP to 2dp. "
        "Inventory turnover ROUND_HALF_UP to 2dp. Average days in inventory = "
        "365 / (turnover already rounded to 2dp), then ROUND_HALF_UP to 2dp "
        "(textbook chained convention, Kieso 4e Review 9-9: 68.5 = 365/5.33). "
        "Gross profit % = GP / net sales x 100, ROUND_HALF_UP to 2dp. "
        "Average inventory = (beginning + ending)/2 on the same cost-flow basis "
        "as the COGS in the numerator."
    ),
    "answers": answers,
    "journal_entries": [
        {
            "part": "a",
            "description": (
                "Dec 31, Year 3 period-end adjusting entry to convert the FIFO "
                "internal records to LIFO for external reporting (the Year 3 LIFO effect)."
            ),
            "lines": je_lines,
        }
    ],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
