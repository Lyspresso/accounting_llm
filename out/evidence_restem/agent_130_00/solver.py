"""
Solver for agent_130#00 — Ridgeview Outfitters Inc.
Full cash T-account method, direct operating section (LO 22-8).

ROUNDING CONVENTION: decimal.Decimal throughout, ROUND_HALF_UP applied per
period/per figure. All amounts here are exact whole dollars (no PV work in this
item), so no rounding differences arise; the cash T-account closes exactly to
the change in cash + restricted cash. Nothing is hard-coded: every derived
figure is computed from the given balance sheet / income statement inputs.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

D = Decimal
CENT = D("1")


def r(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------- GIVENS ----------------
# Comparative balance sheets (prior, current)
bs = {
    "Cash and cash equivalents": (D(80000), D(55000)),
    "Restricted cash": (D(15000), D(25000)),
    "Accounts receivable, net": (D(220000), D(150000)),
    "Inventory": (D(90000), D(240000)),
    "Equipment": (D(1600000), D(2200000)),
    "Accumulated depreciation-equipment": (D(-160000), D(-420000)),
    "Accounts payable": (D(200000), D(160000)),
    "Salaries payable": (D(40000), D(20000)),
    "Bonds payable": (D(500000), D(650000)),
    "Common stock, no-par": (D(900000), D(1000000)),
    "Retained earnings": (D(205000), D(420000)),
}

# Income statement
sales = D(2400000)
cogs = D(1350000)
salary_exp = D(100000)
interest_exp = D(48000)
depr_exp = D(320000)
loss_on_sale = D(160000)
net_income = sales - cogs - salary_exp - interest_exp - depr_exp - loss_on_sale

# Additional info
eq_sold_cost = D(320000)
eq_sold_ad = D(60000)
eq_sale_proceeds = D(100000)

# ---------------- (a) SCHEDULE OF ACCOUNT CHANGES ----------------
chg = {k: (v[1] - v[0]) for k, v in bs.items()}
cash_bal_prior = bs["Cash and cash equivalents"][0] + bs["Restricted cash"][0]
cash_bal_curr = bs["Cash and cash equivalents"][1] + bs["Restricted cash"][1]
chg_total_cash = cash_bal_curr - cash_bal_prior

# Balance-sheet integrity checks (derived, not asserted from given totals)
ta_prior = sum(bs[k][0] for k in ["Cash and cash equivalents", "Restricted cash",
               "Accounts receivable, net", "Inventory", "Equipment",
               "Accumulated depreciation-equipment"])
ta_curr = sum(bs[k][1] for k in ["Cash and cash equivalents", "Restricted cash",
              "Accounts receivable, net", "Inventory", "Equipment",
              "Accumulated depreciation-equipment"])
le_prior = sum(bs[k][0] for k in ["Accounts payable", "Salaries payable",
               "Bonds payable", "Common stock, no-par", "Retained earnings"])
le_curr = sum(bs[k][1] for k in ["Accounts payable", "Salaries payable",
              "Bonds payable", "Common stock, no-par", "Retained earnings"])
assert ta_prior == le_prior and ta_curr == le_curr

# ---------------- (c) ROLLFORWARDS ----------------
# Equipment: begin + purchases - cost of disposal = end
eq_purchases = bs["Equipment"][1] - bs["Equipment"][0] + eq_sold_cost
# Accumulated depreciation (stated as positive balances)
ad_prior = -bs["Accumulated depreciation-equipment"][0]
ad_curr = -bs["Accumulated depreciation-equipment"][1]
# begin + depr expense - AD removed on disposal = end  (proves depr expense)
ad_end_check = ad_prior + depr_exp - eq_sold_ad
assert ad_end_check == ad_curr, (ad_end_check, ad_curr)

# Disposal proof: BV and loss
eq_sold_bv = eq_sold_cost - eq_sold_ad
loss_check = eq_sold_bv - eq_sale_proceeds
assert loss_check == loss_on_sale

# Retained earnings: begin + NI - dividends = end -> solve dividends
dividends = bs["Retained earnings"][0] + net_income - bs["Retained earnings"][1]

# Financing amounts
bonds_issued = bs["Bonds payable"][1] - bs["Bonds payable"][0]
stock_issued = bs["Common stock, no-par"][1] - bs["Common stock, no-par"][0]

# ---------------- DIRECT-METHOD OPERATING CASH FLOWS ----------------
# Cash collected from customers = sales - increase in AR (AR decreased -> add)
ar_decrease = bs["Accounts receivable, net"][0] - bs["Accounts receivable, net"][1]
cash_from_customers = sales + ar_decrease

# Cash paid for inventory = COGS + inventory increase + AP decrease
inv_increase = bs["Inventory"][1] - bs["Inventory"][0]
ap_decrease = bs["Accounts payable"][0] - bs["Accounts payable"][1]
purchases = cogs + inv_increase
cash_paid_inventory = purchases + ap_decrease

# Cash paid for salaries = salary expense + decrease in salaries payable
sal_pay_decrease = bs["Salaries payable"][0] - bs["Salaries payable"][1]
cash_paid_salaries = salary_exp + sal_pay_decrease

# Cash paid for interest (no accruals)
cash_paid_interest = interest_exp

net_operating = (cash_from_customers - cash_paid_inventory
                 - cash_paid_salaries - cash_paid_interest)

# ---------------- INVESTING / FINANCING ----------------
net_investing = eq_sale_proceeds - eq_purchases
net_financing = bonds_issued + stock_issued - dividends

net_change = net_operating + net_investing + net_financing
assert net_change == chg_total_cash, (net_change, chg_total_cash)

# Cash T-account totals
t_debits = cash_from_customers + eq_sale_proceeds + bonds_issued + stock_issued
t_credits = (cash_paid_inventory + cash_paid_salaries + cash_paid_interest
             + eq_purchases + dividends)
t_end = cash_bal_prior + t_debits - t_credits
assert t_end == cash_bal_curr

# ---------------- (b) JOURNAL ENTRIES a-k ----------------
JE = []


def je(part, label, lines):
    dr = sum(D(l[1]) for l in lines if l[1])
    cr = sum(D(l[2]) for l in lines if l[2])
    assert dr == cr, (label, dr, cr)
    JE.append({"part": part, "label": label, "lines": [
        {"account": a, "debit": float(r(d or 0)), "credit": float(r(c or 0))}
        for (a, d, c) in lines]})


je("b", "a: Sales on account", [
    ("Accounts receivable, net", sales, None),
    ("Sales revenue", None, sales)])
je("b", "b: Collections from customers", [
    ("Cash", cash_from_customers, None),
    ("Accounts receivable, net", None, cash_from_customers)])
je("b", "c: Inventory purchased on account", [
    ("Inventory", purchases, None),
    ("Accounts payable", None, purchases)])
je("b", "d: Cost of goods sold", [
    ("Cost of goods sold", cogs, None),
    ("Inventory", None, cogs)])
je("b", "e: Cash paid to suppliers", [
    ("Accounts payable", cash_paid_inventory, None),
    ("Cash", None, cash_paid_inventory)])
je("b", "f: Salary expense accrued and salaries paid", [
    ("Salary expense", salary_exp, None),
    ("Salaries payable", sal_pay_decrease, None),
    ("Cash", None, cash_paid_salaries)])
je("b", "g: Interest paid in cash", [
    ("Interest expense", interest_exp, None),
    ("Cash", None, cash_paid_interest)])
je("b", "h: Depreciation expense", [
    ("Depreciation expense", depr_exp, None),
    ("Accumulated depreciation-equipment", None, depr_exp)])
je("b", "i: Sale of equipment for cash at a loss", [
    ("Cash", eq_sale_proceeds, None),
    ("Accumulated depreciation-equipment", eq_sold_ad, None),
    ("Loss on sale of equipment", loss_on_sale, None),
    ("Equipment", None, eq_sold_cost)])
je("b", "j: Purchase of equipment for cash", [
    ("Equipment", eq_purchases, None),
    ("Cash", None, eq_purchases)])
je("b", "k: Issued bonds payable for cash", [
    ("Cash", bonds_issued, None),
    ("Bonds payable", None, bonds_issued)])
je("b", "l: Issued no-par common stock for cash", [
    ("Cash", stock_issued, None),
    ("Common stock, no-par", None, stock_issued)])
je("b", "m: Declared and paid cash dividends", [
    ("Retained earnings (Dividends)", dividends, None),
    ("Cash", None, dividends)])
je("b", "n: Close net income to retained earnings", [
    ("Income summary", net_income, None),
    ("Retained earnings", None, net_income)])

# ---------------- ANSWERS ----------------
A = []


def add(label, value):
    A.append({"label": label, "value": float(r(value))})


# (a) schedule of account changes
add("a: Change in Cash and cash equivalents (decrease)", chg["Cash and cash equivalents"])
add("a: Change in Restricted cash (increase)", chg["Restricted cash"])
add("a: Change in Accounts receivable, net (decrease)", chg["Accounts receivable, net"])
add("a: Change in Inventory (increase)", chg["Inventory"])
add("a: Change in Equipment (increase)", chg["Equipment"])
add("a: Change in Accumulated depreciation-equipment (increase in contra balance)", ad_curr - ad_prior)
add("a: Change in Accounts payable (decrease)", chg["Accounts payable"])
add("a: Change in Salaries payable (decrease)", chg["Salaries payable"])
add("a: Change in Bonds payable (increase)", chg["Bonds payable"])
add("a: Change in Common stock, no-par (increase)", chg["Common stock, no-par"])
add("a: Change in Retained earnings (increase)", chg["Retained earnings"])
add("a: Beginning cash + cash equivalents + restricted cash", cash_bal_prior)
add("a: Ending cash + cash equivalents + restricted cash", cash_bal_curr)
add("a: Net change in cash + cash equivalents + restricted cash (decrease)", chg_total_cash)

# (c) rollforwards
add("c: Equipment - beginning balance", bs["Equipment"][0])
add("c: Equipment - purchases for cash", eq_purchases)
add("c: Equipment - cost of equipment sold", eq_sold_cost)
add("c: Equipment - ending balance", bs["Equipment"][1])
add("c: Accumulated depreciation - beginning balance", ad_prior)
add("c: Accumulated depreciation - depreciation expense", depr_exp)
add("c: Accumulated depreciation - removed on disposal", eq_sold_ad)
add("c: Accumulated depreciation - ending balance", ad_curr)
add("c: Book value of equipment sold", eq_sold_bv)
add("c: Loss on sale of equipment (proof)", loss_on_sale)
add("c: Retained earnings - beginning balance", bs["Retained earnings"][0])
add("c: Retained earnings - net income", net_income)
add("c: Retained earnings - dividends declared and paid (solved)", dividends)
add("c: Retained earnings - ending balance", bs["Retained earnings"][1])

# (d) cash T-account
add("d: Cash T-account beginning balance (cash + restricted)", cash_bal_prior)
add("d: Cash T-account debit - collections from customers", cash_from_customers)
add("d: Cash T-account credit - payments to suppliers of inventory", cash_paid_inventory)
add("d: Cash T-account credit - payments to employees", cash_paid_salaries)
add("d: Cash T-account credit - interest paid", cash_paid_interest)
add("d: Net cash provided by operating activities", net_operating)
add("d: Cash T-account debit - proceeds from sale of equipment", eq_sale_proceeds)
add("d: Cash T-account credit - purchase of equipment", eq_purchases)
add("d: Net cash used in investing activities", net_investing)
add("d: Cash T-account debit - proceeds from issuing bonds payable", bonds_issued)
add("d: Cash T-account debit - proceeds from issuing common stock", stock_issued)
add("d: Cash T-account credit - dividends paid", dividends)
add("d: Net cash provided by financing activities", net_financing)
add("d: Cash T-account total debits", t_debits)
add("d: Cash T-account total credits", t_credits)
add("d: Cash T-account ending balance (cash + restricted)", t_end)
add("d: Proof - net change per T-account equals change in cash + restricted cash", net_change)

# (e) statement of cash flows - direct method
add("e: Cash received from customers", cash_from_customers)
add("e: Cash paid for inventory (to suppliers)", -cash_paid_inventory)
add("e: Cash paid for salaries", -cash_paid_salaries)
add("e: Cash paid for interest", -cash_paid_interest)
add("e: Net cash provided by operating activities", net_operating)
add("e: Proceeds from sale of equipment", eq_sale_proceeds)
add("e: Cash paid to purchase equipment", -eq_purchases)
add("e: Net cash used in investing activities", net_investing)
add("e: Proceeds from issuance of bonds payable", bonds_issued)
add("e: Proceeds from issuance of common stock", stock_issued)
add("e: Dividends paid", -dividends)
add("e: Net cash provided by financing activities", net_financing)
add("e: Net decrease in cash, cash equivalents, and restricted cash", net_change)
add("e: Cash, cash equivalents, and restricted cash at beginning of year", cash_bal_prior)
add("e: Cash, cash equivalents, and restricted cash at end of year", cash_bal_curr)

# (f) classification - the figures the part references
add("f: Loss on sale of equipment (noncash, not a separate cash outflow)", loss_on_sale)
add("f: Cash inflow reported for the disposal, in investing activities", eq_sale_proceeds)

notes = (
    "Direct method: only actual cash receipts/payments hit the cash T-account, so no "
    "noncash items and no reconciliation lines appear in the operating section. "
    "(f) The $160,000 loss is not a cash outflow at all - it is the bookkeeping "
    "difference between the $260,000 book value of the equipment sold ($320,000 cost "
    "less $60,000 accumulated depreciation) and the $100,000 cash actually received. "
    "No cash left the company because of the loss; the only cash event was the "
    "$100,000 received. Under the direct method the operating section lists only cash "
    "collected from customers and cash paid to suppliers, employees, and lenders, so "
    "an accrual-only item like a loss never appears there (it would only surface as an "
    "add-back if the indirect method were used). The equipment disposal therefore "
    "appears once, in INVESTING ACTIVITIES, as 'Proceeds from sale of equipment "
    "$100,000' - the full cash inflow, not netted against the loss. "
    "Derivations: equipment purchases $920,000 = $2,200,000 - $1,600,000 + $320,000 "
    "cost removed; accumulated depreciation rolls $160,000 + $320,000 - $60,000 = "
    "$420,000; dividends $207,000 = $205,000 + $422,000 - $420,000; collections "
    "$2,470,000 = $2,400,000 sales + $70,000 AR decrease; payments for inventory "
    "$1,540,000 = $1,350,000 COGS + $150,000 inventory increase + $40,000 AP decrease; "
    "salaries paid $120,000 = $100,000 expense + $20,000 salaries payable decrease. "
    "Cash + restricted cash falls $15,000 ($95,000 to $80,000), which equals "
    "operating $762,000 + investing (-$820,000) + financing $43,000. "
    "Journal entries are labeled a-n; the item asked for 'a-k in Demo 22-8 style' but "
    "explaining every income statement account and every balance sheet change requires "
    "fourteen entries, so the sequence runs a through n."
)

out = {
    "id": "agent_130#00",
    "rounding_convention": ("decimal.Decimal with ROUND_HALF_UP applied per period; "
                            "whole dollars. All figures are exact whole dollars, so no "
                            "rounding differences arise and the cash T-account closes "
                            "exactly to the $15,000 decrease in cash + restricted cash."),
    "answers": A,
    "journal_entries": JE,
    "insufficient_info": False,
    "notes": notes,
}
print(json.dumps(out, indent=1))
