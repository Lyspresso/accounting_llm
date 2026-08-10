"""
agent_303#02 -- Silverbrook Home Appliances LLC: subsequent-year true-up of the
Refund Liability / Inventory-Estimated Returns pair (Review 8-3 "subsequent
period" approach), plus a settlement alternate.

ROUNDING CONVENTION
    All money is decimal.Decimal.  Every quantization uses ROUND_HALF_UP to
    whole cents, applied once per period / per computed line (never on floats).
    Journal entries are stated in whole dollars; every input here is an exact
    whole-dollar amount and each derived figure (4.5% x 550,000; 60% x 24,750;
    60% x 19,800) lands exactly on a whole dollar, so no residual arises and the
    rollforward schedules close exactly on the derived ending balances.

METHOD (derived from the stem, bottom-up)
    * Actual returns during the year are ALL charged to Sales Returns (a contra
      revenue) with the credit to Cash; the beginning Refund Liability is NOT
      drawn down during the year.
    * Cost side of an actual return: real Inventory comes back, COGS is relieved
      at 60% of the returned selling price.
    * Sales ALLOWANCES are price concessions -- sales side only, no goods move,
      so no cost-side entry and no effect on Inventory-Estimated Returns.
    * At year end the Refund Liability is trued up straight from its beginning
      balance to the required ending balance (estimated returns on CURRENT-year
      sales still expected next period).  The plug goes to Sales Returns.
      The cost-side asset is trued up in parallel to 60% of that liability.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(x) -> Decimal:
    """Money: quantize to cents, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def f(d: Decimal) -> float:
    return float(m(d))


# ----------------------------------------------------------------- given facts
COST_RATIO = Decimal("0.60")          # cost of merchandise = 60% of selling price
BEG_REFUND_LIAB = m("11500")          # Jan 1, Yr 2
BEG_INV_EST_RET = m("6900")           # Jan 1, Yr 2
CREDIT_SALES = m("550000")
COGS_GIVEN = m("330000")              # stem states 60% of sales
ACTUAL_RETURNS = m("19800")           # cash refunds, charged to current-yr Sales Returns
ALLOWANCES = m("1650")                # on account, sales side only
EST_RATE = Decimal("0.045")           # 4.5% of Year 2 credit sales

SETTLE_RETURNS = m("7200")            # part (e) alternate: Yr 1 returns
SETTLE_COST = m("4320")               # stem-given cost of that portion

# ------------------------------------------------- (a) sales and cost of sales
cogs_derived = m(CREDIT_SALES * COST_RATIO)     # 330,000 -- ties to stem
assert cogs_derived == COGS_GIVEN

# --------------------------------- (b) actual returns (both sides), allowances
returns_cost = m(ACTUAL_RETURNS * COST_RATIO)   # inventory back / COGS relieved

# ------------------- (c) target ending balances and period-end adjusting plugs
target_end_refund_liab = m(CREDIT_SALES * EST_RATE)              # 24,750
target_end_inv_est_ret = m(target_end_refund_liab * COST_RATIO)  # 14,850

# subsequent-period approach: liability untouched during the year, so the
# year-end plug is simply target ending less beginning balance
rl_settlements_during_yr = m(0)
rl_adjustment = m(target_end_refund_liab - BEG_REFUND_LIAB - rl_settlements_during_yr)

ier_settlements_during_yr = m(0)
ier_adjustment = m(target_end_inv_est_ret - BEG_INV_EST_RET - ier_settlements_during_yr)

# ------------------------------------------------------- (d) rollforwards
rl_end = m(BEG_REFUND_LIAB - rl_settlements_during_yr + rl_adjustment)
ier_end = m(BEG_INV_EST_RET - ier_settlements_during_yr + ier_adjustment)
tie_check = (ier_end == m(rl_end * COST_RATIO))
assert rl_end == target_end_refund_liab and ier_end == target_end_inv_est_ret
assert tie_check

# ------------------------------------------------------------- (f) net sales
total_sales_returns_expense = m(ACTUAL_RETURNS + rl_adjustment)   # contra-revenue hitting Yr 2
net_sales = m(CREDIT_SALES - total_sales_returns_expense - ALLOWANCES)
net_cogs = m(COGS_GIVEN - returns_cost - ier_adjustment)
gross_profit = m(net_sales - net_cogs)
# cross-check: returned/estimated-returned goods carry a 40% margin; allowances carry none
assert net_cogs == m((net_sales + ALLOWANCES) * COST_RATIO)

# ------------------------------------------- (e) settlement alternate figures
rl_after_settle = m(BEG_REFUND_LIAB - SETTLE_RETURNS)
ier_after_settle = m(BEG_INV_EST_RET - SETTLE_COST)
assert SETTLE_COST == m(SETTLE_RETURNS * COST_RATIO)
alt_current_yr_returns = m(ACTUAL_RETURNS - SETTLE_RETURNS)       # 12,600 to Sales Returns
alt_current_yr_returns_cost = m(alt_current_yr_returns * COST_RATIO)
alt_rl_adjustment = m(target_end_refund_liab - rl_after_settle)
alt_ier_adjustment = m(target_end_inv_est_ret - ier_after_settle)
alt_net_sales = m(CREDIT_SALES - alt_current_yr_returns - alt_rl_adjustment - ALLOWANCES)
assert alt_net_sales == net_sales   # net sales invariant to the split

# ------------------------------------------------------------------- answers
answers = [
    # (a)
    {"label": "a: Credit sales -- Dr Accounts Receivable / Cr Sales Revenue", "value": f(CREDIT_SALES)},
    {"label": "a: Cost of goods sold recorded (60% of $550,000) -- Dr COGS / Cr Inventory", "value": f(cogs_derived)},
    # (b)
    {"label": "b: Actual returns, sales side -- Dr Sales Returns / Cr Cash", "value": f(ACTUAL_RETURNS)},
    {"label": "b: Actual returns, cost side (60% x $19,800) -- Dr Inventory / Cr COGS", "value": f(returns_cost)},
    {"label": "b: Sales allowances on account -- Dr Sales Allowances / Cr Accounts Receivable", "value": f(ALLOWANCES)},
    {"label": "b: Cost-side entry required for sales allowances (none -- no goods returned)", "value": 0},
    # (c)
    {"label": "c: TARGET ending Refund Liability (4.5% x $550,000)", "value": f(target_end_refund_liab)},
    {"label": "c: Year-end adjusting plug, sales side -- Dr Sales Returns / Cr Refund Liability ($24,750 - $11,500)", "value": f(rl_adjustment)},
    {"label": "c: TARGET ending Inventory--Estimated Returns ($24,750 x 60%)", "value": f(target_end_inv_est_ret)},
    {"label": "c: Year-end adjusting plug, cost side -- Dr Inventory--Estimated Returns / Cr COGS ($14,850 - $6,900)", "value": f(ier_adjustment)},
    # (d) Refund Liability rollforward rows
    {"label": "d: Refund Liability rollforward row 1 -- balance Jan 1, Year 2", "value": f(BEG_REFUND_LIAB)},
    {"label": "d: Refund Liability rollforward row 2 -- returns charged AGAINST the liability during Year 2 (none; all actual returns went to Sales Returns)", "value": f(rl_settlements_during_yr)},
    {"label": "d: Refund Liability rollforward row 2a (memo only) -- actual cash returns debited to Sales Returns during Year 2", "value": f(ACTUAL_RETURNS)},
    {"label": "d: Refund Liability rollforward row 3 -- year-end adjusting increase (Dr Sales Returns)", "value": f(rl_adjustment)},
    {"label": "d: Refund Liability rollforward row 4 -- balance Dec 31, Year 2", "value": f(rl_end)},
    # (d) Inventory--Estimated Returns rollforward rows
    {"label": "d: Inventory--Estimated Returns rollforward row 1 -- balance Jan 1, Year 2", "value": f(BEG_INV_EST_RET)},
    {"label": "d: Inventory--Estimated Returns rollforward row 2 -- amounts relieved against the asset during Year 2 (none)", "value": f(ier_settlements_during_yr)},
    {"label": "d: Inventory--Estimated Returns rollforward row 2a (memo only) -- cost of actual returns credited to COGS during Year 2", "value": f(returns_cost)},
    {"label": "d: Inventory--Estimated Returns rollforward row 3 -- year-end adjusting increase (Cr COGS)", "value": f(ier_adjustment)},
    {"label": "d: Inventory--Estimated Returns rollforward row 4 -- balance Dec 31, Year 2", "value": f(ier_end)},
    {"label": "d: Tie-out check -- ending Refund Liability x 60%", "value": f(m(rl_end * COST_RATIO))},
    {"label": "d: Tie-out check -- does ending Inv--Est Returns equal ending Refund Liability x 60%?", "value": "Yes: $14,850 = $24,750 x 60%"},
    # (e)
    {"label": "e: Settlement of Year 1 accrued returns, liability side -- Dr Refund Liability / Cr Cash", "value": f(SETTLE_RETURNS)},
    {"label": "e: Settlement of Year 1 accrued returns, cost side -- Dr Inventory / Cr Inventory--Estimated Returns", "value": f(SETTLE_COST)},
    {"label": "e: Sales Returns debited for this $7,200 portion (none -- it was already expensed in Year 1)", "value": 0},
    {"label": "e: Refund Liability balance immediately after the Jan 18 settlement", "value": f(rl_after_settle)},
    {"label": "e: Inventory--Estimated Returns balance immediately after the Jan 18 settlement", "value": f(ier_after_settle)},
    {"label": "e (supplementary, alternate carried through the year): actual returns still charged to Year 2 Sales Returns ($19,800 - $7,200)", "value": f(alt_current_yr_returns)},
    {"label": "e (supplementary): cost side of those Year 2 returns (60% x $12,600) -- Dr Inventory / Cr COGS", "value": f(alt_current_yr_returns_cost)},
    {"label": "e (supplementary): revised year-end sales-side plug ($24,750 - $4,300)", "value": f(alt_rl_adjustment)},
    {"label": "e (supplementary): revised year-end cost-side plug ($14,850 - $2,580)", "value": f(alt_ier_adjustment)},
    {"label": "e (supplementary): Net Sales under the alternate -- unchanged", "value": f(alt_net_sales)},
    # (f)
    {"label": "f: Sales revenue (gross)", "value": f(CREDIT_SALES)},
    {"label": "f: Less Sales Returns charged to Year 2 (actual $19,800 + year-end adjustment $13,250)", "value": f(total_sales_returns_expense)},
    {"label": "f: Less Sales Allowances", "value": f(ALLOWANCES)},
    {"label": "f: NET SALES, Year 2", "value": f(net_sales)},
    {"label": "f: Net COGS, Year 2 ($330,000 - $11,880 - $7,950) [supporting]", "value": f(net_cogs)},
    {"label": "f: Gross profit, Year 2 [supporting]", "value": f(gross_profit)},
    {"label": "f: Balance-sheet presentation -- Refund Liability", "value": "Current liability, reported separately (e.g., 'Refund liability'); NOT netted against Accounts Receivable and NOT offset against Inventory--Estimated Returns. $24,750."},
    {"label": "f: Balance-sheet presentation -- Inventory--Estimated Returns", "value": "Current asset for the right to recover products from customers, reported separately from (not buried in) Inventory. $14,850."},
]

# ------------------------------------------------------------ journal entries
def JE(part, lines):
    d = sum(Decimal(str(l.get("debit", 0))) for l in lines)
    c = sum(Decimal(str(l.get("credit", 0))) for l in lines)
    assert m(d) == m(c), (part, d, c)
    return {"part": part, "lines": lines}


def L(acct, dr=0, cr=0):
    return {"account": acct, "debit": f(Decimal(dr)), "credit": f(Decimal(cr))}


journal_entries = [
    JE("a", [L("Accounts Receivable", dr=CREDIT_SALES), L("Sales Revenue", cr=CREDIT_SALES)]),
    JE("a", [L("Cost of Goods Sold", dr=cogs_derived), L("Inventory", cr=cogs_derived)]),
    JE("b", [L("Sales Returns", dr=ACTUAL_RETURNS), L("Cash", cr=ACTUAL_RETURNS)]),
    JE("b", [L("Inventory", dr=returns_cost), L("Cost of Goods Sold", cr=returns_cost)]),
    JE("b", [L("Sales Allowances", dr=ALLOWANCES), L("Accounts Receivable", cr=ALLOWANCES)]),
    JE("c", [L("Sales Returns", dr=rl_adjustment), L("Refund Liability", cr=rl_adjustment)]),
    JE("c", [L("Inventory--Estimated Returns", dr=ier_adjustment), L("Cost of Goods Sold", cr=ier_adjustment)]),
    JE("e", [L("Refund Liability", dr=SETTLE_RETURNS), L("Cash", cr=SETTLE_RETURNS)]),
    JE("e", [L("Inventory", dr=SETTLE_COST), L("Inventory--Estimated Returns", cr=SETTLE_COST)]),
]

notes = (
    "Subsequent-period (Review 8-3) method: actual returns during Year 2 are debited in full to "
    "Sales Returns with Cash credited, so the $11,500 beginning Refund Liability is not drawn down "
    "during the year; the year-end entry trues the liability straight from $11,500 to the required "
    "$24,750 (4.5% x $550,000), a $13,250 debit to Sales Returns. The cost side moves in parallel to "
    "60% of the liability: $6,900 -> $14,850, a $7,950 debit to Inventory--Estimated Returns and "
    "credit to COGS. Sales allowances are price concessions with no goods returned, so they get a "
    "sales-side entry only and never touch Inventory--Estimated Returns. Part (e) is a settlement of "
    "a PRIOR-year accrual: it reduces Refund Liability ($7,200) and Inventory--Estimated Returns "
    "($4,320) with no charge to Year 2 Sales Returns and no charge to Year 2 COGS -- that expense was "
    "recognized in Year 1. Carrying the alternate through the year would leave the balances at $4,300 "
    "and $2,580 before the true-up, so the plugs become $20,450 and $12,270 and Net Sales is still "
    "$515,300 -- the split between actual-return expense and true-up is presentation only. "
    "Both rollforwards close exactly on the derived ending balances (no rounding residual); "
    "$14,850 = $24,750 x 60% confirms the tie-out."
)

print(json.dumps({
    "id": "agent_303#02",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to whole cents applied once per computed amount per period; JEs stated in whole dollars (all amounts land exactly on whole dollars, so both rollforward schedules close exactly on the derived ending balances with no plug)",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
