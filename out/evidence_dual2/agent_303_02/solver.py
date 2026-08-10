"""Silverbrook Home Appliances — subsequent-year true-up (Review 8-3 approach).

Rounding: decimal.Decimal throughout, ROUND_HALF_UP to whole dollars applied
once per period/figure (no PV schedule in this item; all inputs are exact).
Every figure is derived from the fact pattern; nothing is hard-coded except
the stated facts.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("1")
def r(x): return x.quantize(C, rounding=ROUND_HALF_UP)

# ---- given facts ----
COST_RATIO      = Decimal("0.60")
beg_refund_liab = Decimal("11500")
beg_inv_est_ret = Decimal("6900")
credit_sales    = Decimal("550000")
cogs_given      = Decimal("330000")
actual_returns  = Decimal("19800")
allowances      = Decimal("1650")
est_rate        = Decimal("0.045")
settle_sales    = Decimal("7200")
settle_cost_giv = Decimal("4320")

# ---- (a) ----
cogs = r(credit_sales * COST_RATIO)
assert cogs == cogs_given

# ---- (b) ----
returns_cost = r(actual_returns * COST_RATIO)

# ---- (c) ----
target_end_liab = r(credit_sales * est_rate)          # ending Refund Liability
sales_side_adj  = target_end_liab - beg_refund_liab   # actual returns hit Sales Returns, not the liability
target_end_asset= r(target_end_liab * COST_RATIO)
cost_side_adj   = target_end_asset - beg_inv_est_ret

# ---- (d) rollforward ----
liab_charged  = Decimal("0")   # nothing charged to the liability under this approach
asset_charged = Decimal("0")
end_liab  = beg_refund_liab + liab_charged + sales_side_adj
end_asset = beg_inv_est_ret + asset_charged + cost_side_adj
check_asset = r(end_liab * COST_RATIO)
assert end_liab == target_end_liab and end_asset == target_end_asset == check_asset

# ---- (e) settlement alternate ----
settle_cost = r(settle_sales * COST_RATIO)
assert settle_cost == settle_cost_giv

# ---- (f) ----
total_sales_returns = actual_returns + sales_side_adj
net_sales = credit_sales - total_sales_returns - allowances

answers = [
 {"label":"a: Sales revenue recorded on credit sales","value":int(credit_sales)},
 {"label":"a: Cost of goods sold recorded (60% of sales)","value":int(cogs)},
 {"label":"b: Sales Returns debited for actual cash refunds","value":int(actual_returns)},
 {"label":"b: Cost of actual returns restored to Inventory (credit COGS)","value":int(returns_cost)},
 {"label":"b: Sales allowances granted on account","value":int(allowances)},
 {"label":"c: Target ending Refund Liability (4.5% x $550,000)","value":int(target_end_liab)},
 {"label":"c: Year-end sales-side adjustment (Dr Sales Returns / Cr Refund Liability)","value":int(sales_side_adj)},
 {"label":"c: Target ending Inventory-Estimated Returns (60% of ending liability)","value":int(target_end_asset)},
 {"label":"c: Year-end cost-side adjustment (Dr Inv-Est Returns / Cr COGS)","value":int(cost_side_adj)},
 {"label":"d: Refund Liability rollforward - beginning balance Jan 1, Yr 2","value":int(beg_refund_liab)},
 {"label":"d: Refund Liability rollforward - actual returns charged to the liability during Yr 2 (none; charged to Sales Returns)","value":int(liab_charged)},
 {"label":"d: Refund Liability rollforward - year-end true-up adjustment","value":int(sales_side_adj)},
 {"label":"d: Refund Liability rollforward - ending balance Dec 31, Yr 2","value":int(end_liab)},
 {"label":"d: Inventory-Estimated Returns rollforward - beginning balance Jan 1, Yr 2","value":int(beg_inv_est_ret)},
 {"label":"d: Inventory-Estimated Returns rollforward - amounts charged to the asset during Yr 2 (none; cost of actual returns went to Inventory/COGS)","value":int(asset_charged)},
 {"label":"d: Inventory-Estimated Returns rollforward - year-end true-up adjustment","value":int(cost_side_adj)},
 {"label":"d: Inventory-Estimated Returns rollforward - ending balance Dec 31, Yr 2","value":int(end_asset)},
 {"label":"d: Confirmation - ending Refund Liability x 60%","value":int(check_asset)},
 {"label":"e: Settlement - Refund Liability debited for Year 1 returns settled","value":int(settle_sales)},
 {"label":"e: Settlement - Inventory-Estimated Returns credited (cost)","value":int(settle_cost)},
 {"label":"f: Net Sales for Year 2","value":int(net_sales)},
 {"label":"f: Balance-sheet presentation - Refund Liability","value":"Current liability, reported separately (not netted against accounts receivable); it is the obligation to refund customers for goods expected to be returned within the 45-day window."},
 {"label":"f: Balance-sheet presentation - Inventory-Estimated Returns","value":"Current asset, reported separately from Inventory (a right to recover product from customers, carried at 60% of the expected refund); not netted against the refund liability."},
]

jes = [
 {"part":"a","lines":[
   {"account":"Accounts Receivable","debit":int(credit_sales),"credit":0},
   {"account":"Sales Revenue","debit":0,"credit":int(credit_sales)}]},
 {"part":"a","lines":[
   {"account":"Cost of Goods Sold","debit":int(cogs),"credit":0},
   {"account":"Inventory","debit":0,"credit":int(cogs)}]},
 {"part":"b","lines":[
   {"account":"Sales Returns","debit":int(actual_returns),"credit":0},
   {"account":"Cash","debit":0,"credit":int(actual_returns)}]},
 {"part":"b","lines":[
   {"account":"Inventory","debit":int(returns_cost),"credit":0},
   {"account":"Cost of Goods Sold","debit":0,"credit":int(returns_cost)}]},
 {"part":"b","lines":[
   {"account":"Sales Allowances","debit":int(allowances),"credit":0},
   {"account":"Accounts Receivable","debit":0,"credit":int(allowances)}]},
 {"part":"c","lines":[
   {"account":"Sales Returns","debit":int(sales_side_adj),"credit":0},
   {"account":"Refund Liability","debit":0,"credit":int(sales_side_adj)}]},
 {"part":"c","lines":[
   {"account":"Inventory-Estimated Returns","debit":int(cost_side_adj),"credit":0},
   {"account":"Cost of Goods Sold","debit":0,"credit":int(cost_side_adj)}]},
 {"part":"e","lines":[
   {"account":"Refund Liability","debit":int(settle_sales),"credit":0},
   {"account":"Cash","debit":0,"credit":int(settle_sales)}]},
 {"part":"e","lines":[
   {"account":"Inventory","debit":int(settle_cost),"credit":0},
   {"account":"Inventory-Estimated Returns","debit":0,"credit":int(settle_cost)}]},
]
for je in jes:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"])

out = {
 "id":"agent_303#02",
 "rounding_convention":"decimal.Decimal with ROUND_HALF_UP, whole dollars in journal entries and schedules; all inputs are exact so no rounding residual arose. Refund Liability schedule closes exactly to the computed ending balance of 4.5% x credit sales, and Inventory-Estimated Returns closes exactly to 60% of that ending liability.",
 "answers":answers,
 "journal_entries":jes,
 "insufficient_info":False,
 "notes":("Review 8-3 subsequent-period approach: actual returns during Year 2 are debited to Sales Returns (not charged against the beginning Refund Liability), "
          "so the year-end entry must move the liability from its $11,500 beginning balance all the way to the $24,750 target, a $13,250 credit; "
          "the cost side mirrors it at 60% ($6,900 -> $14,850, a $7,950 debit). Cost of actual returns ($11,880) goes to Inventory with a credit to COGS. "
          "Part (e) is an alternate treatment of $7,200 of the year's cash returns: because those Year 1 returns were already accrued, they are settled against "
          "Refund Liability and Inventory-Estimated Returns instead of Sales Returns / COGS. Sales allowances do not carry a cost side (no goods come back). "
          "Net sales = 550,000 - (19,800 + 13,250) sales returns - 1,650 allowances = 515,300.")
}
print(json.dumps(out, indent=1))
