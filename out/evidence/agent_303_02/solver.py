#!/usr/bin/env python3
"""
Solver for item agent_303#02 — Silverbrook Home Appliances LLC (LO 8-3).

TOPIC
-----
Sales returns and allowances under the *subsequent-period* approach of
Review 8-3 (Intermediate Accounting, Ch. 8).  Under that approach:

  * ALL actual returns taken during the year are recorded as if they arose
    from the CURRENT year: debit Sales Returns, credit Cash/AR (sales side),
    and debit Inventory, credit Cost of Goods Sold (cost side).  The Refund
    Liability and Inventory—Estimated Returns accounts are NOT touched during
    the year.
  * At period end a single true-up entry moves Refund Liability so that the
    ENDING balance equals the estimated returns on current-year sales that are
    still expected to be taken in the next period.  Because the actual returns
    taken during the year were charged to Sales Returns rather than against the
    liability, the true-up amount is

        adjustment (credit to Refund Liability)
            = (estimate % x current-year credit sales) - actual returns taken

    and therefore

        ending Refund Liability
            = beginning balance - actual returns + estimated returns on
              current-year sales

    This is exactly the arithmetic the textbook uses in Review 8-3 part (d)
    ("beginning balance $10,000 - actual returns $12,400 + refunds estimated on
    current year sales $11,200 = ending balance $8,800").  The adjustment may
    be a debit to Refund Liability when actual returns exceed the new estimate,
    as it is in the textbook's own Review 8-3 solution.  A useful consequence
    of the mechanic: net Sales Returns recognized for the year always equals
    the estimate on current-year sales.

  * The cost-side true-up is the sales-side true-up x cost ratio, so the ending
    Inventory—Estimated Returns balance is always ending Refund Liability x
    cost ratio.

  * Sales allowances (price concessions, no goods returned) are recorded as
    incurred with no cost-side entry.

  * Part (e) is an INDEPENDENT alternative ("suppose instead"): returns that
    are identified as relating to PRIOR-year sales already accrued are settled
    against the accrued balances — debit Refund Liability / credit Cash on the
    sales side and debit Inventory / credit Inventory—Estimated Returns on the
    cost side — with no debit to Sales Returns.  It does not change (a)-(d),
    and part (f) explicitly asks for net sales under the main method.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal — never float.  Every monetary result is
quantized to cents (0.01) with ROUND_HALF_UP, applied per computed amount /
per period as it is derived (round-per-period, not round-at-end).  This item
involves no present-value work, so no PV table factors are used.  Percentages
(the 4.5% return estimate and the 60% cost ratio) are exact Decimals, so in
practice every figure here lands on an exact cent and the rounding is a
guard rather than a correction.

RUN
---
    python3 solver.py            # prints one JSON object on stdout
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents with ROUND_HALF_UP (the course convention)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly plain number: int when the cents are zero, else float-free
    string-parsed value.  We emit ints/floats via Decimal -> str -> json to keep
    the value exact for whole cents."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)  # only reachable for fractional cents, which cannot occur here


# ---------------------------------------------------------------------------
# Facts taken from the stem (nothing below is hard-coded from an answer key)
# ---------------------------------------------------------------------------
COST_RATIO = Decimal("0.60")          # cost of merchandise = 60% of selling price

BEG_REFUND_LIABILITY = money("11500")  # Jan 1, Year 2
BEG_INV_EST_RETURNS = money("6900")    # Jan 1, Year 2

CREDIT_SALES = money("550000")         # Year 2 credit sales
COGS_GIVEN = money("330000")           # Year 2 COGS (stem states it is 60%)
ACTUAL_RETURNS = money("19800")        # cash refunds, booked as current-year Sales Returns
SALES_ALLOWANCES = money("1650")       # allowances on account
RETURN_RATE = Decimal("0.045")         # 4.5% of Year 2 credit sales

# Part (e) alternate settlement facts
SETTLE_RETURNS_SALES = money("7200")   # Jan 18, Year 2 cash returns of Year 1 sales
SETTLE_RETURNS_COST = money("4320")    # cost of those returns


# ---------------------------------------------------------------------------
# (a) Year 2 sales and cost of sales
# ---------------------------------------------------------------------------
cogs_derived = money(CREDIT_SALES * COST_RATIO)
assert cogs_derived == COGS_GIVEN, (cogs_derived, COGS_GIVEN)

je_a_sales = {
    "part": "a",
    "memo": "Year 2 — record credit sales",
    "lines": [
        {"account": "Accounts Receivable", "debit": num(CREDIT_SALES), "credit": 0},
        {"account": "Sales Revenue", "debit": 0, "credit": num(CREDIT_SALES)},
    ],
}
je_a_cogs = {
    "part": "a",
    "memo": "Year 2 — record cost of goods sold (60% of selling price)",
    "lines": [
        {"account": "Cost of Goods Sold", "debit": num(cogs_derived), "credit": 0},
        {"account": "Inventory", "debit": 0, "credit": num(cogs_derived)},
    ],
}

# ---------------------------------------------------------------------------
# (b) Actual returns (both sides) and sales allowances
# ---------------------------------------------------------------------------
cost_of_actual_returns = money(ACTUAL_RETURNS * COST_RATIO)

je_b_returns_sales = {
    "part": "b",
    "memo": "Year 2 — actual returns, sales side (recorded as current-year returns)",
    "lines": [
        {"account": "Sales Returns", "debit": num(ACTUAL_RETURNS), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(ACTUAL_RETURNS)},
    ],
}
je_b_returns_cost = {
    "part": "b",
    "memo": "Year 2 — actual returns, cost side (goods back into inventory at 60%)",
    "lines": [
        {"account": "Inventory", "debit": num(cost_of_actual_returns), "credit": 0},
        {"account": "Cost of Goods Sold", "debit": 0, "credit": num(cost_of_actual_returns)},
    ],
}
je_b_allowances = {
    "part": "b",
    "memo": "Year 2 — sales allowances granted on account (no cost-side entry)",
    "lines": [
        {"account": "Sales Allowances", "debit": num(SALES_ALLOWANCES), "credit": 0},
        {"account": "Accounts Receivable", "debit": 0, "credit": num(SALES_ALLOWANCES)},
    ],
}

# ---------------------------------------------------------------------------
# (c) Target ending Refund Liability + period-end adjusting entries
# ---------------------------------------------------------------------------
estimated_returns_on_y2_sales = money(CREDIT_SALES * RETURN_RATE)      # 4.5% x 550,000

# True-up plug: actual returns were charged to Sales Returns instead of to the
# liability, so the liability must absorb (new estimate - actual returns).
adjustment_sales_side = money(estimated_returns_on_y2_sales - ACTUAL_RETURNS)
adjustment_cost_side = money(adjustment_sales_side * COST_RATIO)

target_ending_refund_liability = money(BEG_REFUND_LIABILITY + adjustment_sales_side)
ending_inv_est_returns = money(BEG_INV_EST_RETURNS + adjustment_cost_side)

# The adjustment is a credit to Refund Liability when positive, a debit when the
# actual returns exceeded the new estimate.
if adjustment_sales_side >= 0:
    je_c_sales_lines = [
        {"account": "Sales Returns", "debit": num(adjustment_sales_side), "credit": 0},
        {"account": "Refund Liability", "debit": 0, "credit": num(adjustment_sales_side)},
    ]
    je_c_cost_lines = [
        {"account": "Inventory—Estimated Returns", "debit": num(adjustment_cost_side), "credit": 0},
        {"account": "Cost of Goods Sold", "debit": 0, "credit": num(adjustment_cost_side)},
    ]
else:
    amt_s = money(-adjustment_sales_side)
    amt_c = money(-adjustment_cost_side)
    je_c_sales_lines = [
        {"account": "Refund Liability", "debit": num(amt_s), "credit": 0},
        {"account": "Sales Returns", "debit": 0, "credit": num(amt_s)},
    ]
    je_c_cost_lines = [
        {"account": "Cost of Goods Sold", "debit": num(amt_c), "credit": 0},
        {"account": "Inventory—Estimated Returns", "debit": 0, "credit": num(amt_c)},
    ]

je_c_sales = {
    "part": "c",
    "memo": ("December 31, Year 2 — adjust Refund Liability to estimated returns on "
             "Year 2 sales still expected next period (4.5% x $550,000 less actual "
             "returns already taken)"),
    "lines": je_c_sales_lines,
}
je_c_cost = {
    "part": "c",
    "memo": "December 31, Year 2 — cost-side true-up of Inventory—Estimated Returns (60%)",
    "lines": je_c_cost_lines,
}

# ---------------------------------------------------------------------------
# (d) Rollforward schedules
# ---------------------------------------------------------------------------
cost_of_estimated_returns = money(estimated_returns_on_y2_sales * COST_RATIO)

# Refund Liability: beginning - actual returns + estimated returns on Y2 sales
rf_check = money(BEG_REFUND_LIABILITY - ACTUAL_RETURNS + estimated_returns_on_y2_sales)
assert rf_check == target_ending_refund_liability, (rf_check, target_ending_refund_liability)

# Inventory—Estimated Returns: beginning - cost of actual returns + cost of estimate
inv_check = money(BEG_INV_EST_RETURNS - cost_of_actual_returns + cost_of_estimated_returns)
assert inv_check == ending_inv_est_returns, (inv_check, ending_inv_est_returns)

# Required confirmation: ending Inv—Est Returns = ending Refund Liability x 60%
confirm_ok = ending_inv_est_returns == money(target_ending_refund_liability * COST_RATIO)
assert confirm_ok

# ---------------------------------------------------------------------------
# (e) Settlement alternate (independent of a-d)
# ---------------------------------------------------------------------------
assert money(SETTLE_RETURNS_SALES * COST_RATIO) == SETTLE_RETURNS_COST

je_e_sales = {
    "part": "e",
    "memo": ("January 18, Year 2 — settle Year 1 returns already accrued, sales side "
             "(no debit to Sales Returns)"),
    "lines": [
        {"account": "Refund Liability", "debit": num(SETTLE_RETURNS_SALES), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(SETTLE_RETURNS_SALES)},
    ],
}
je_e_cost = {
    "part": "e",
    "memo": "January 18, Year 2 — settle Year 1 returns already accrued, cost side",
    "lines": [
        {"account": "Inventory", "debit": num(SETTLE_RETURNS_COST), "credit": 0},
        {"account": "Inventory—Estimated Returns", "debit": 0, "credit": num(SETTLE_RETURNS_COST)},
    ],
}

# ---------------------------------------------------------------------------
# (f) Net sales under the main method
# ---------------------------------------------------------------------------
# Sales Returns recognized in Year 2 income = actual returns booked + the
# period-end true-up (which nets to the estimate on Year 2 sales).
sales_returns_expense = money(ACTUAL_RETURNS + adjustment_sales_side)
net_sales = money(CREDIT_SALES - sales_returns_expense - SALES_ALLOWANCES)

# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------
journal_entries = [
    je_a_sales, je_a_cogs,
    je_b_returns_sales, je_b_returns_cost, je_b_allowances,
    je_c_sales, je_c_cost,
    je_e_sales, je_e_cost,
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), (je["memo"], dr, cr)

answers = [
    {"label": "c: target ending Refund Liability at December 31, Year 2",
     "value": num(target_ending_refund_liability)},

    {"label": "d: Refund Liability rollforward — beginning balance (Jan 1, Year 2)",
     "value": num(BEG_REFUND_LIABILITY)},
    {"label": "d: Refund Liability rollforward — less actual returns taken during Year 2",
     "value": num(ACTUAL_RETURNS)},
    {"label": "d: Refund Liability rollforward — add estimated returns on Year 2 sales",
     "value": num(estimated_returns_on_y2_sales)},
    {"label": "d: Refund Liability rollforward — ending balance (Dec 31, Year 2)",
     "value": num(target_ending_refund_liability)},

    {"label": "d: Inventory—Estimated Returns rollforward — beginning balance (Jan 1, Year 2)",
     "value": num(BEG_INV_EST_RETURNS)},
    {"label": "d: Inventory—Estimated Returns rollforward — less cost of actual returns",
     "value": num(cost_of_actual_returns)},
    {"label": "d: Inventory—Estimated Returns rollforward — add cost of estimated returns",
     "value": num(cost_of_estimated_returns)},
    {"label": "d: Inventory—Estimated Returns rollforward — ending balance (Dec 31, Year 2)",
     "value": num(ending_inv_est_returns)},

    {"label": "f: Net Sales for Year 2", "value": num(net_sales)},
]

notes = (
    "Method per Review 8-3 (subsequent-period approach): all actual returns during the "
    "year are debited to Sales Returns, so the year-end true-up to Refund Liability is "
    "(4.5% x $550,000) - $19,800 = $4,950 credit, giving ending Refund Liability of "
    "$11,500 + $4,950 = $16,450, equivalently $11,500 - $19,800 + $24,750. "
    "Confirmation required by (d): ending Inventory—Estimated Returns $9,870 = ending "
    "Refund Liability $16,450 x 60%. "
    "Part (f) presentation: Refund Liability is a current liability (it is not netted "
    "against the return asset, and academics' alternative of showing it as an Allowance "
    "for Sales Returns contra to Accounts Receivable is only noted as an aside); "
    "Inventory—Estimated Returns is a separate current asset reported with/next to "
    "inventory. Both are presented gross, not offset. Net sales = $550,000 sales revenue "
    "less $24,750 net Sales Returns less $1,650 Sales Allowances = $523,600. "
    "Part (e) is an independent alternative and does not change (a)-(d)."
)

output = {
    "id": "agent_303#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; every monetary amount quantized to cents with "
        "ROUND_HALF_UP as it is computed (round-per-period, not round-at-end). "
        "Percentages (4.5% return estimate, 60% cost ratio) held as exact Decimals. "
        "No present-value factors are involved in this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2, ensure_ascii=False))
