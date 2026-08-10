"""Rivermist Outfitters - average cost retail inventory method (Q1, LO 10-8).

Rounding convention: decimal.Decimal throughout, never floats.
Money is rounded to whole dollars using ROUND_HALF_UP per period.
Cost-to-retail ratios are carried at full precision internally and
reported rounded to 4 decimal places (percent shown to 2 dp);
the ending-inventory-at-cost figure is the rounded product, and
COGS is derived as (goods available at cost - ending inventory at cost)
so the schedule closes exactly.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

D = Decimal
CENT = D("1")          # whole dollars
RATIO_Q = D("0.0001")  # ratio display precision


def money(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def ratio(x):
    return D(x).quantize(RATIO_Q, rounding=ROUND_HALF_UP)


def pct(x):
    return (D(x) * 100).quantize(D("0.01"), rounding=ROUND_HALF_UP)


# ---------------- Given data ----------------
beg_cost = D("48000")
beg_ret = D("80000")
pur_cost = D("320000")
pur_ret = D("400000")
freight = D("12000")
pret_cost = D("20000")   # purchase returns (reduction)
pret_ret = D("30000")
markups = D("35000")
markup_canc = D("5000")
markdowns = D("40000")
markdown_canc = D("10000")
sales_gross = D("410000")
sales_returns = D("20000")

# ---------------- (a)(b) journal entries ----------------
jes = []
jes.append({"part": "a", "lines": [
    {"account": "Purchases", "debit": money(pur_cost), "credit": money(0)},
    {"account": "Accounts Payable", "debit": money(0), "credit": money(pur_cost)},
]})
jes.append({"part": "a", "lines": [
    {"account": "Freight-In (Transportation-In)", "debit": money(freight), "credit": money(0)},
    {"account": "Cash", "debit": money(0), "credit": money(freight)},
]})
jes.append({"part": "a", "lines": [
    {"account": "Accounts Payable", "debit": money(pret_cost), "credit": money(0)},
    {"account": "Purchase Returns", "debit": money(0), "credit": money(pret_cost)},
]})
net_sales = sales_gross - sales_returns
jes.append({"part": "b", "lines": [
    {"account": "Cash", "debit": money(net_sales), "credit": money(0)},
    {"account": "Sales Returns", "debit": money(sales_returns), "credit": money(0)},
    {"account": "Sales Revenue", "debit": money(0), "credit": money(sales_gross)},
]})

# ---------------- (c) average cost retail schedule ----------------
net_markups = markups - markup_canc               # 30,000
net_markdowns = markdowns - markdown_canc         # 30,000

net_pur_cost = pur_cost - pret_cost               # 300,000
net_pur_ret = pur_ret - pret_ret                  # 370,000

# Goods available for sale (average cost: include BOTH net markups and net markdowns)
gafs_cost = beg_cost + net_pur_cost + freight
gafs_ret_before_md = beg_ret + net_pur_ret + net_markups
gafs_ret = gafs_ret_before_md - net_markdowns

ctr_avg = gafs_cost / gafs_ret

end_ret = gafs_ret - net_sales
end_cost_avg = money(D(end_ret) * ctr_avg)

# ---------------- (d) COGS ----------------
cogs_avg = money(gafs_cost) - end_cost_avg

# ---------------- (f) conventional retail (LCM) ----------------
gafs_ret_conv = gafs_ret_before_md            # exclude net markdowns from denominator
ctr_conv = gafs_cost / gafs_ret_conv
end_ret_conv = end_ret                        # same retail ending inventory
end_cost_conv = money(D(end_ret_conv) * ctr_conv)
cogs_conv = money(gafs_cost) - end_cost_conv

# ---------------- (e) periodic closing entry ----------------
jes.append({"part": "e", "lines": [
    {"account": "Inventory (ending, Dec 31, Year 5)", "debit": end_cost_avg, "credit": money(0)},
    {"account": "Cost of Goods Sold", "debit": cogs_avg, "credit": money(0)},
    {"account": "Purchase Returns", "debit": money(pret_cost), "credit": money(0)},
    {"account": "Inventory (beginning, Jan 1, Year 5)", "debit": money(0), "credit": money(beg_cost)},
    {"account": "Purchases", "debit": money(0), "credit": money(pur_cost)},
    {"account": "Freight-In (Transportation-In)", "debit": money(0), "credit": money(freight)},
]})

# Dr = Cr check
for je in jes:
    dr = sum(D(l["debit"]) for l in je["lines"])
    cr = sum(D(l["credit"]) for l in je["lines"])
    assert dr == cr, (je["part"], dr, cr)

answers = [
    # (a)
    {"label": "a(1): Purchases on account - Dr Purchases", "value": money(pur_cost)},
    {"label": "a(1): Purchases on account - Cr Accounts Payable", "value": money(pur_cost)},
    {"label": "a(2): Freight-in paid in cash - Dr Freight-In", "value": money(freight)},
    {"label": "a(2): Freight-in paid in cash - Cr Cash", "value": money(freight)},
    {"label": "a(3): Purchase returns for credit - Dr Accounts Payable", "value": money(pret_cost)},
    {"label": "a(3): Purchase returns for credit - Cr Purchase Returns", "value": money(pret_cost)},
    # (b)
    {"label": "b: Gross sales revenue (credit Sales Revenue)", "value": money(sales_gross)},
    {"label": "b: Sales returns (debit Sales Returns)", "value": money(sales_returns)},
    {"label": "b: Net sales / net cash debited", "value": money(net_sales)},
    # (c) schedule
    {"label": "c: Beginning inventory at cost", "value": money(beg_cost)},
    {"label": "c: Beginning inventory at retail", "value": money(beg_ret)},
    {"label": "c: Net purchases at cost (320,000 - 20,000)", "value": money(net_pur_cost)},
    {"label": "c: Net purchases at retail (400,000 - 30,000)", "value": money(net_pur_ret)},
    {"label": "c: Freight-in at cost", "value": money(freight)},
    {"label": "c: Net markups (35,000 - 5,000)", "value": money(net_markups)},
    {"label": "c: Net markdowns (40,000 - 10,000)", "value": money(net_markdowns)},
    {"label": "c: Goods available for sale at cost", "value": money(gafs_cost)},
    {"label": "c: Goods available for sale at retail before markdowns", "value": money(gafs_ret_before_md)},
    {"label": "c: Goods available for sale at retail (average cost basis)", "value": money(gafs_ret)},
    {"label": "c: Net sales deducted at retail", "value": money(net_sales)},
    {"label": "c: Estimated ending inventory at retail", "value": money(end_ret)},
    {"label": "c: Average cost-to-retail ratio (decimal)", "value": ratio(ctr_avg)},
    {"label": "c: Average cost-to-retail ratio (percent)", "value": pct(ctr_avg)},
    {"label": "c: Estimated ending inventory at cost (average cost retail)", "value": end_cost_avg},
    # (d)
    {"label": "d: Cost of goods sold (average cost retail)", "value": cogs_avg},
    # (e)
    {"label": "e: Dr Inventory (ending)", "value": end_cost_avg},
    {"label": "e: Dr Cost of Goods Sold", "value": cogs_avg},
    {"label": "e: Dr Purchase Returns", "value": money(pret_cost)},
    {"label": "e: Cr Inventory (beginning)", "value": money(beg_cost)},
    {"label": "e: Cr Purchases", "value": money(pur_cost)},
    {"label": "e: Cr Freight-In", "value": money(freight)},
    # (f)
    {"label": "f: Conventional retail goods available at retail (markdowns excluded)", "value": money(gafs_ret_conv)},
    {"label": "f: Conventional cost-to-retail ratio (decimal)", "value": ratio(ctr_conv)},
    {"label": "f: Conventional cost-to-retail ratio (percent)", "value": pct(ctr_conv)},
    {"label": "f: Estimated ending inventory at retail (conventional)", "value": money(end_ret_conv)},
    {"label": "f: Estimated ending inventory at cost (conventional retail)", "value": end_cost_conv},
    {"label": "f: Difference, average cost less conventional", "value": money(end_cost_avg - end_cost_conv)},
    # (g)
    {"label": "g: Balance sheet - Inventory (current asset), Dec 31, Year 5", "value": end_cost_avg},
]

notes = (
    "(c) Average cost retail: net markups AND net markdowns are both included in the "
    "retail column of goods available, so one average ratio "
    f"({money(gafs_cost)}/{money(gafs_ret)} = {pct(ctr_avg)}%) is applied to ending inventory at retail "
    f"({money(gafs_ret)} - {money(net_sales)} net sales = {money(end_ret)}). "
    "Net sales (410,000 gross - 20,000 returns = 390,000) is the correct deduction because returned "
    "goods were restored to resale inventory. "
    "(f) Conventional retail (LCM/lower-of-average-cost-or-market) omits net markdowns from the ratio "
    f"denominator ({money(gafs_ret_before_md)}), producing a lower ratio ({pct(ctr_conv)}%) and therefore a lower "
    f"ending inventory at cost ({end_cost_conv} vs {end_cost_avg}); excluding markdowns treats the "
    "markdown as evidence of a decline in utility, approximating lower of cost or market, whereas the "
    "average cost method reflects the actual average relationship of cost to selling price. "
    "(g) Balance sheet, current assets: 'Inventories - $"
    f"{end_cost_avg:,}'. Disclosure: state that inventories are stated at the lower of cost or "
    "net realizable value with cost determined by the retail inventory method on an average cost basis, "
    "that amounts are estimates based on the cost-to-retail ratio, and that a periodic system is used. "
    "Ratios are unrounded internally; whole-dollar ROUND_HALF_UP is applied to the reported money figures "
    "and COGS is derived as goods available at cost less ending inventory at cost so the schedule closes exactly."
)

out = {
    "id": "agent_064#00",
    "rounding_convention": "decimal.Decimal only (no floats); money rounded to whole dollars with ROUND_HALF_UP per period; cost-to-retail ratios carried at full precision and displayed to 4 decimals (percent to 2 dp); COGS derived as goods available at cost minus ending inventory at cost so the schedule closes exactly to goods available.",
    "answers": [{"label": a["label"], "value": float(a["value"]) if a["value"] % 1 else int(a["value"])} for a in answers],
    "journal_entries": [{"part": je["part"], "lines": [{"account": l["account"], "debit": int(l["debit"]), "credit": int(l["credit"])} for l in je["lines"]]} for je in jes],
    "insufficient_info": False,
    "notes": notes,
}
print(json.dumps(out, indent=2))
