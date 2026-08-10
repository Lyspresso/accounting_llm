"""Solver for agent_303#02 — Silverbrook Home Appliances (LO 8-3).

Rounding convention: all money uses decimal.Decimal quantized to cents
(0.01) with ROUND_HALF_UP, applied per computed period figure (no float
arithmetic anywhere). Every figure is derived from the stated inputs.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def m(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def f(x):
    return float(m(x))

# ---- Inputs -------------------------------------------------------------
beg_refund_liab = m("11500")
beg_inv_est_ret = m("6900")
credit_sales    = m("550000")
cost_ratio      = Decimal("0.60")
cogs_stated     = m("330000")
actual_returns  = m("19800")
allowances      = m("1650")
est_rate        = Decimal("0.045")
settle_returns  = m("7200")   # part (e)
settle_cost     = m("4320")   # part (e)

# ---- (a) sales and COGS -------------------------------------------------
cogs = m(credit_sales * cost_ratio)          # 330,000 (agrees with stated)
assert cogs == cogs_stated

# ---- (b) actual returns + allowances ------------------------------------
returns_cost = m(actual_returns * cost_ratio)

# ---- (c) year-end true-up ----------------------------------------------
target_liab = m(credit_sales * est_rate)
adj_liab    = m(target_liab - beg_refund_liab)      # returns were charged to Sales Returns,
                                                    # so liability moves beg -> target directly
target_inv_est = m(target_liab * cost_ratio)
adj_inv_est    = m(target_inv_est - beg_inv_est_ret)

# ---- (d) rollforwards ---------------------------------------------------
liab_charged   = m("0")   # no returns charged against the liability under this method
inv_est_relieved = m("0")
end_liab    = m(beg_refund_liab - liab_charged + adj_liab)
end_inv_est = m(beg_inv_est_ret - inv_est_relieved + adj_inv_est)
tie_check   = (end_inv_est == m(end_liab * cost_ratio))

# ---- (f) net sales ------------------------------------------------------
total_sales_returns = m(actual_returns + adj_liab)
net_sales = m(credit_sales - total_sales_returns - allowances)

answers = [
    {"label": "a: Accounts receivable debited for Year 2 credit sales", "value": f(credit_sales)},
    {"label": "a: Sales revenue credited", "value": f(credit_sales)},
    {"label": "a: Cost of goods sold recorded (60% of sales)", "value": f(cogs)},
    {"label": "a: Inventory credited for cost of sales", "value": f(cogs)},

    {"label": "b: Sales Returns debited for actual cash refunds", "value": f(actual_returns)},
    {"label": "b: Cash credited for actual refunds", "value": f(actual_returns)},
    {"label": "b: Inventory restored on actual returns (60% of $19,800)", "value": f(returns_cost)},
    {"label": "b: Cost of goods sold credited on actual returns", "value": f(returns_cost)},
    {"label": "b: Sales allowances on account", "value": f(allowances)},

    {"label": "c: Target ending Refund Liability (4.5% x $550,000)", "value": f(target_liab)},
    {"label": "c: Beginning Refund Liability", "value": f(beg_refund_liab)},
    {"label": "c: Year-end adjusting entry - Sales Returns debit / Refund Liability credit (increase)", "value": f(adj_liab)},
    {"label": "c: Target ending Inventory-Estimated Returns (60% of target liability)", "value": f(target_inv_est)},
    {"label": "c: Year-end adjusting entry - Inventory-Estimated Returns debit / COGS credit (increase)", "value": f(adj_inv_est)},

    {"label": "d: Refund Liability rollforward - beginning balance Jan 1, Yr 2", "value": f(beg_refund_liab)},
    {"label": "d: Refund Liability rollforward - actual returns charged against the liability", "value": f(liab_charged)},
    {"label": "d: Refund Liability rollforward - year-end adjustment (true-up)", "value": f(adj_liab)},
    {"label": "d: Refund Liability rollforward - ending balance Dec 31, Yr 2", "value": f(end_liab)},
    {"label": "d: Inventory-Estimated Returns rollforward - beginning balance Jan 1, Yr 2", "value": f(beg_inv_est_ret)},
    {"label": "d: Inventory-Estimated Returns rollforward - amounts relieved for actual returns", "value": f(inv_est_relieved)},
    {"label": "d: Inventory-Estimated Returns rollforward - year-end adjustment (true-up)", "value": f(adj_inv_est)},
    {"label": "d: Inventory-Estimated Returns rollforward - ending balance Dec 31, Yr 2", "value": f(end_inv_est)},
    {"label": "d: Confirmation - ending Refund Liability x 60%", "value": f(end_liab * cost_ratio)},
    {"label": "d: Confirmation - ending Inv-Est Returns equals liability x 60% (1 = yes)", "value": 1 if tie_check else 0},

    {"label": "e: Settlement - Refund Liability debited (Year 1 returns identified Jan 18)", "value": f(settle_returns)},
    {"label": "e: Settlement - Cash credited for refunds", "value": f(settle_returns)},
    {"label": "e: Settlement - Inventory debited for cost of goods returned", "value": f(settle_cost)},
    {"label": "e: Settlement - Inventory-Estimated Returns credited", "value": f(settle_cost)},

    {"label": "f: Gross credit sales", "value": f(credit_sales)},
    {"label": "f: Total Sales Returns contra (actual $19,800 + true-up $13,250)", "value": f(total_sales_returns)},
    {"label": "f: Sales allowances contra", "value": f(allowances)},
    {"label": "f: Net Sales for Year 2", "value": f(net_sales)},
]

journal_entries = [
    {"part": "a", "lines": [
        {"account": "Accounts Receivable", "debit": f(credit_sales), "credit": 0},
        {"account": "Sales Revenue", "debit": 0, "credit": f(credit_sales)}]},
    {"part": "a", "lines": [
        {"account": "Cost of Goods Sold", "debit": f(cogs), "credit": 0},
        {"account": "Inventory", "debit": 0, "credit": f(cogs)}]},
    {"part": "b", "lines": [
        {"account": "Sales Returns", "debit": f(actual_returns), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": f(actual_returns)}]},
    {"part": "b", "lines": [
        {"account": "Inventory", "debit": f(returns_cost), "credit": 0},
        {"account": "Cost of Goods Sold", "debit": 0, "credit": f(returns_cost)}]},
    {"part": "b", "lines": [
        {"account": "Sales Allowances", "debit": f(allowances), "credit": 0},
        {"account": "Accounts Receivable", "debit": 0, "credit": f(allowances)}]},
    {"part": "c", "lines": [
        {"account": "Sales Returns", "debit": f(adj_liab), "credit": 0},
        {"account": "Refund Liability", "debit": 0, "credit": f(adj_liab)}]},
    {"part": "c", "lines": [
        {"account": "Inventory-Estimated Returns", "debit": f(adj_inv_est), "credit": 0},
        {"account": "Cost of Goods Sold", "debit": 0, "credit": f(adj_inv_est)}]},
    {"part": "e", "lines": [
        {"account": "Refund Liability", "debit": f(settle_returns), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": f(settle_returns)}]},
    {"part": "e", "lines": [
        {"account": "Inventory", "debit": f(settle_cost), "credit": 0},
        {"account": "Inventory-Estimated Returns", "debit": 0, "credit": f(settle_cost)}]},
]

for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, je

notes = (
    "Method (Review 8-3 subsequent-period approach): all actual Year 2 cash refunds are debited to "
    "Sales Returns (and cost restored to Inventory against COGS) as if they arose from Year 2 sales, so "
    "the Refund Liability and Inventory-Estimated Returns are NOT relieved during the year; at year-end "
    "each account is trued up directly from its beginning balance to the required ending balance. "
    "(c) Target ending Refund Liability = 4.5% x $550,000 = $24,750; true-up = $24,750 - $11,500 = $13,250 "
    "(Dr Sales Returns / Cr Refund Liability). Cost side target = $24,750 x 60% = $14,850; true-up = "
    "$14,850 - $6,900 = $7,950 (Dr Inventory-Estimated Returns / Cr COGS). "
    "(d) Refund Liability: $11,500 + $13,250 = $24,750; Inventory-Estimated Returns: $6,900 + $7,950 = "
    "$14,850 = $24,750 x 60%, confirmed. "
    "(e) Alternate settlement of previously accrued Year 1 returns: Dr Refund Liability $7,200 / Cr Cash "
    "$7,200 and Dr Inventory $4,320 / Cr Inventory-Estimated Returns $4,320 - no Sales Returns or COGS "
    "effect, because the revenue and cost effects were already recognized in Year 1. "
    "(f) Presentation: Refund Liability is a current liability (not netted against receivables); "
    "Inventory-Estimated Returns is a separate current asset reported with/next to Inventory (the right to "
    "recover goods, carried at former carrying amount). Sales Returns and Sales Allowances are contra-revenue "
    "accounts deducted from gross sales to reach Net Sales of $515,300."
)

print(json.dumps({
    "id": "agent_303#02",
    "rounding_convention": "decimal.Decimal, quantized to cents (0.01) with ROUND_HALF_UP per period figure; no floats used in computation",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
