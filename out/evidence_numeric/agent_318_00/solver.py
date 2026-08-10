"""Ashwick Merchandising Co. — Q1 (agent_318#00), solved cold.

Rounding convention: decimal.Decimal throughout (never floats for money).
All money is exact to the cent and lands on whole dollars here; ratios and
percentages are quantized with ROUND_HALF_UP per period (two decimals).
Days in inventory = 365 / (turnover already rounded to two decimals), then
that quotient is itself rounded HALF_UP to two decimals, per the Required.
Nothing is hard-coded downstream: every figure is derived from the inputs.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

D = Decimal
CENTS = D("0.01")


def r2(x):
    return D(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def n(x):
    x = D(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------- inputs (given) ----------------
inv_y0 = D("400000")          # Inventory, Dec 31 Year 0
inv_y1 = D("440000")          # Inventory, Dec 31 Year 1
sales_y1 = D("2800000")
cogs_y1 = D("1680000")
sales_y2 = D("3150000")

purchases = D("1950000")      # gross invoice, on account
freight_in = D("48000")       # cash, inventoriable
purch_returns = D("32000")    # AP reduced
inv_y2 = D("465000")          # physical count Dec 31 Year 2

# ---------------- (b) settlement ----------------
ap_settled = purchases - purch_returns

# ---------------- (d) inventory bridge ----------------
net_purchases = purchases - purch_returns
cost_goods_purchased = net_purchases + freight_in
goods_available = inv_y1 + cost_goods_purchased
cogs_y2 = goods_available - inv_y2

adj_debits = inv_y2 + purch_returns + cogs_y2
adj_credits = inv_y1 + purchases + freight_in
assert adj_debits == adj_credits

# ---------------- (e) ratios ----------------
avg_inv_y1 = (inv_y0 + inv_y1) / 2
avg_inv_y2 = (inv_y1 + inv_y2) / 2
turn_y1 = r2(cogs_y1 / avg_inv_y1)
turn_y2 = r2(cogs_y2 / avg_inv_y2)
days_y1 = r2(D(365) / turn_y1)
days_y2 = r2(D(365) / turn_y2)
gp_y1 = sales_y1 - cogs_y1
gp_y2 = sales_y2 - cogs_y2
gpp_y1 = r2(gp_y1 / sales_y1 * 100)
gpp_y2 = r2(gp_y2 / sales_y2 * 100)

journal_entries = [
    {"part": "a", "lines": [
        {"account": "Purchases", "debit": n(purchases), "credit": 0},
        {"account": "Accounts Payable", "debit": 0, "credit": n(purchases)},
    ]},
    {"part": "a", "lines": [
        {"account": "Freight-in", "debit": n(freight_in), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": n(freight_in)},
    ]},
    {"part": "b", "lines": [
        {"account": "Accounts Payable", "debit": n(purch_returns), "credit": 0},
        {"account": "Purchase Returns and Allowances", "debit": 0, "credit": n(purch_returns)},
    ]},
    {"part": "b", "lines": [
        {"account": "Accounts Payable", "debit": n(ap_settled), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": n(ap_settled)},
    ]},
    {"part": "c", "lines": [
        {"account": "Accounts Receivable", "debit": n(sales_y2), "credit": 0},
        {"account": "Sales Revenue", "debit": 0, "credit": n(sales_y2)},
    ]},
    {"part": "d", "lines": [
        {"account": "Inventory (ending, Dec 31 Year 2)", "debit": n(inv_y2), "credit": 0},
        {"account": "Purchase Returns and Allowances", "debit": n(purch_returns), "credit": 0},
        {"account": "Cost of Goods Sold", "debit": n(cogs_y2), "credit": 0},
        {"account": "Inventory (beginning, Dec 31 Year 1)", "debit": 0, "credit": n(inv_y1)},
        {"account": "Purchases", "debit": 0, "credit": n(purchases)},
        {"account": "Freight-in", "debit": 0, "credit": n(freight_in)},
    ]},
]

for je in journal_entries:
    assert sum(D(str(l["debit"])) for l in je["lines"]) == sum(D(str(l["credit"])) for l in je["lines"])

answers = [
    {"label": "a: Purchases debited (gross invoice, on account)", "value": n(purchases)},
    {"label": "a: Freight-in debited (cash paid)", "value": n(freight_in)},
    {"label": "b: Purchase Returns and Allowances credited (AP reduced)", "value": n(purch_returns)},
    {"label": "b: Cash paid to settle remaining Year 2 accounts payable", "value": n(ap_settled)},
    {"label": "c: Sales Revenue credited (on account)", "value": n(sales_y2)},
    {"label": "d: Bridge - Beginning inventory (Dec 31, Year 1)", "value": n(inv_y1)},
    {"label": "d: Bridge - Purchases", "value": n(purchases)},
    {"label": "d: Bridge - Less: Purchase returns and allowances", "value": n(purch_returns)},
    {"label": "d: Bridge - Net purchases", "value": n(net_purchases)},
    {"label": "d: Bridge - Add: Freight-in", "value": n(freight_in)},
    {"label": "d: Bridge - Cost of goods purchased", "value": n(cost_goods_purchased)},
    {"label": "d: Bridge - Cost of goods available for sale", "value": n(goods_available)},
    {"label": "d: Bridge - Less: Ending inventory (Dec 31, Year 2)", "value": n(inv_y2)},
    {"label": "d: Year 2 cost of goods sold", "value": n(cogs_y2)},
    {"label": "d: Adjusting entry total debits", "value": n(adj_debits)},
    {"label": "d: Adjusting entry total credits", "value": n(adj_credits)},
    {"label": "e: Year 1 average inventory", "value": n(avg_inv_y1)},
    {"label": "e: Year 1 inventory turnover (times)", "value": float(turn_y1)},
    {"label": "e: Year 1 average days in inventory", "value": float(days_y1)},
    {"label": "e: Year 1 gross profit", "value": n(gp_y1)},
    {"label": "e: Year 1 gross profit percentage (%)", "value": float(gpp_y1)},
    {"label": "e: Year 2 average inventory", "value": n(avg_inv_y2)},
    {"label": "e: Year 2 inventory turnover (times)", "value": float(turn_y2)},
    {"label": "e: Year 2 average days in inventory", "value": float(days_y2)},
    {"label": "e: Year 2 gross profit", "value": n(gp_y2)},
    {"label": "e: Year 2 gross profit percentage (%)", "value": float(gpp_y2)},
]

notes = (
    "(d) Combined period-end adjusting entry proves Dr = Cr at {dr:,} = {cr:,}. "
    "(f) Efficiency improved: turnover rose {t1} -> {t2} times and average days in inventory "
    "fell {d1} -> {d2} days, so Ashwick moved goods faster despite carrying more inventory. "
    "Margin weakened: gross profit percentage slipped {g1}% -> {g2}% (COGS grew faster than sales), "
    "though gross profit dollars still rose from ${gp1:,} to ${gp2:,} on the higher sales volume. "
    "Net read: the company traded a little margin for volume and inventory efficiency. "
    "Schedule convention: money is exact whole dollars (no rounding needed); ratios/percentages "
    "quantized HALF_UP to two decimals, and days = 365 / rounded turnover as instructed."
).format(dr=int(adj_debits), cr=int(adj_credits), t1=turn_y1, t2=turn_y2, d1=days_y1, d2=days_y2,
         g1=gpp_y1, g2=gpp_y2, gp1=int(gp_y1), gp2=int(gp_y2))

print(json.dumps({
    "id": "agent_318#00",
    "rounding_convention": ("decimal.Decimal with ROUND_HALF_UP per period; money exact to whole "
                           "dollars in journal entries, ratios and percentages to two decimals; "
                           "days in inventory = 365 / turnover rounded to two decimals first"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
