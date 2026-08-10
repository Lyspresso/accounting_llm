"""Northpine Logistics Corp. — full cash T-account / direct-method SCF solver.

Rounding convention: all money is decimal.Decimal; every computed figure is
quantized to cents with ROUND_HALF_UP once per period (no float arithmetic
anywhere).  Nothing is hard-coded except the raw comparative balance sheet,
income statement, and the stated additional information; every other figure is
derived from those inputs.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

D = Decimal
CENT = D("0.01")


def q(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- raw inputs
prior = {
    "Cash and cash equivalents": D("140000"),
    "Restricted cash": D("30000"),
    "Accounts receivable, net": D("400000"),
    "Inventory": D("180000"),
    "Equipment": D("2800000"),
    "Accumulated depreciation-equipment": D("-350000"),
    "Accounts payable": D("220000"),
    "Salaries payable": D("60000"),
    "Bonds payable": D("800000"),
    "Common stock, no-par": D("1600000"),
    "Retained earnings": D("520000"),
}
current = {
    "Cash and cash equivalents": D("95000"),
    "Restricted cash": D("45000"),
    "Accounts receivable, net": D("310000"),
    "Inventory": D("280000"),
    "Equipment": D("3500000"),
    "Accumulated depreciation-equipment": D("-620000"),
    "Accounts payable": D("185000"),
    "Salaries payable": D("35000"),
    "Bonds payable": D("950000"),
    "Common stock, no-par": D("1750000"),
    "Retained earnings": D("690000"),
}
IS = {
    "Sales revenue": D("4200000"),
    "Cost of goods sold": D("2400000"),
    "Salary expense": D("210000"),
    "Interest expense": D("84000"),
    "Depreciation expense": D("340000"),
    "Loss on sale of equipment": D("90000"),
}
net_income = (IS["Sales revenue"] - IS["Cost of goods sold"] - IS["Salary expense"]
              - IS["Interest expense"] - IS["Depreciation expense"]
              - IS["Loss on sale of equipment"])
disp_cost = D("550000")
disp_ad = D("70000")
disp_proceeds = D("390000")

chg = {k: current[k] - prior[k] for k in prior}

# --------------------------------------------------- (a) cash + restricted cash
beg_cash_total = prior["Cash and cash equivalents"] + prior["Restricted cash"]
end_cash_total = current["Cash and cash equivalents"] + current["Restricted cash"]
chg_cash_total = end_cash_total - beg_cash_total

# ------------------------------------- (b) subsequent measurement schedules
collections = prior["Accounts receivable, net"] + IS["Sales revenue"] - current["Accounts receivable, net"]
purchases = current["Inventory"] + IS["Cost of goods sold"] - prior["Inventory"]
paid_suppliers = prior["Accounts payable"] + purchases - current["Accounts payable"]
paid_employees = prior["Salaries payable"] + IS["Salary expense"] - current["Salaries payable"]
equip_purchases = current["Equipment"] + disp_cost - prior["Equipment"]
ad_prior = -prior["Accumulated depreciation-equipment"]
ad_current = -current["Accumulated depreciation-equipment"]
ad_end_check = ad_prior + IS["Depreciation expense"] - disp_ad
book_value_sold = disp_cost - disp_ad
loss_check = book_value_sold - disp_proceeds
dividends = prior["Retained earnings"] + net_income - current["Retained earnings"]
interest_paid = IS["Interest expense"]
bonds_issued = chg["Bonds payable"]
stock_issued = chg["Common stock, no-par"]

# ------------------------------------------------- (c) reconstructed entries
def E(letter, desc, lines, cash_posting=True):
    dr = sum(D(l[1]) for l in lines if l[1] is not None)
    cr = sum(D(l[2]) for l in lines if l[2] is not None)
    assert dr == cr, (letter, dr, cr)
    return {
        "part": "c",
        "label": "(%s) %s" % (letter, desc),
        "posts_to_cash_t_account": cash_posting,
        "lines": [{"account": a, "debit": num(d or 0), "credit": num(cr_ or 0)}
                  for a, d, cr_ in lines],
    }


entries = [
    E("a", "Sales and collections from customers",
      [("Cash", collections, None),
       ("Accounts receivable, net", None, -chg["Accounts receivable, net"]),
       ("Sales revenue", None, IS["Sales revenue"])]),
    E("b", "Purchases of inventory and cash paid to suppliers",
      [("Cost of goods sold", IS["Cost of goods sold"], None),
       ("Inventory", chg["Inventory"], None),
       ("Accounts payable", -chg["Accounts payable"], None),
       ("Cash", None, paid_suppliers)]),
    E("c", "Salary expense and cash paid to employees",
      [("Salary expense", IS["Salary expense"], None),
       ("Salaries payable", -chg["Salaries payable"], None),
       ("Cash", None, paid_employees)]),
    E("d", "Interest expense paid in cash",
      [("Interest expense", IS["Interest expense"], None),
       ("Cash", None, interest_paid)]),
    E("e", "*** HIGHLIGHTED period-end (Dec 31) depreciation ADJUSTING ENTRY - NONCASH ***",
      [("Depreciation expense", IS["Depreciation expense"], None),
       ("Accumulated depreciation-equipment", None, IS["Depreciation expense"])],
      cash_posting=False),
    E("f", "Sale of equipment for cash (cost 550,000; AD 70,000; BV 480,000)",
      [("Cash", disp_proceeds, None),
       ("Accumulated depreciation-equipment", disp_ad, None),
       ("Loss on sale of equipment", loss_check, None),
       ("Equipment", None, disp_cost)]),
    E("g", "Purchase of equipment for cash",
      [("Equipment", equip_purchases, None),
       ("Cash", None, equip_purchases)]),
    E("h", "Issuance of bonds payable for cash",
      [("Cash", bonds_issued, None),
       ("Bonds payable", None, bonds_issued)]),
    E("i", "Issuance of no-par common stock for cash",
      [("Cash", stock_issued, None),
       ("Common stock, no-par", None, stock_issued)]),
    E("j", "Dividends declared and paid in cash",
      [("Retained earnings", dividends, None),
       ("Cash", None, dividends)]),
]

# ------------------------------------------------------- (d) cash T-account
op_in = collections
op_out = paid_suppliers + paid_employees + interest_paid
net_op = op_in - op_out
inv_in = disp_proceeds
inv_out = equip_purchases
net_inv = inv_in - inv_out
fin_in = bonds_issued + stock_issued
fin_out = dividends
net_fin = fin_in - fin_out
total_debits = op_in + inv_in + fin_in
total_credits = op_out + inv_out + fin_out
net_change = total_debits - total_credits
assert net_change == chg_cash_total
assert ad_end_check == ad_current
assert loss_check == IS["Loss on sale of equipment"]
assert end_cash_total == beg_cash_total + net_change

A = []
def add(label, value):
    A.append({"label": label, "value": value})


# (a) schedule of account changes
for k in ["Cash and cash equivalents", "Restricted cash", "Accounts receivable, net",
          "Inventory", "Equipment", "Accumulated depreciation-equipment",
          "Accounts payable", "Salaries payable", "Bonds payable",
          "Common stock, no-par", "Retained earnings"]:
    add("a: Change in %s (current less prior)" % k, num(chg[k]))
add("a: Beginning cash + cash equivalents + restricted cash", num(beg_cash_total))
add("a: Ending cash + cash equivalents + restricted cash", num(end_cash_total))
add("a: Change in cash + cash equivalents + restricted cash (decrease)", num(chg_cash_total))

# (b) subsequent measurement schedules
add("b1: Accounts receivable - beginning balance", num(prior["Accounts receivable, net"]))
add("b1: Accounts receivable - add sales revenue on account", num(IS["Sales revenue"]))
add("b1: Accounts receivable - less cash collections from customers (SOLVED)", num(collections))
add("b1: Accounts receivable - ending balance", num(current["Accounts receivable, net"]))
add("b2: Inventory - beginning balance", num(prior["Inventory"]))
add("b2: Inventory - add purchases (SOLVED)", num(purchases))
add("b2: Inventory - less cost of goods sold", num(IS["Cost of goods sold"]))
add("b2: Inventory - ending balance", num(current["Inventory"]))
add("b2: Accounts payable - beginning balance", num(prior["Accounts payable"]))
add("b2: Accounts payable - add purchases on account", num(purchases))
add("b2: Accounts payable - less cash payments to suppliers (SOLVED)", num(paid_suppliers))
add("b2: Accounts payable - ending balance", num(current["Accounts payable"]))
add("b3: Salaries payable - beginning balance", num(prior["Salaries payable"]))
add("b3: Salaries payable - add salary expense", num(IS["Salary expense"]))
add("b3: Salaries payable - less cash payments to employees (SOLVED)", num(paid_employees))
add("b3: Salaries payable - ending balance", num(current["Salaries payable"]))
add("b4: Equipment - beginning balance", num(prior["Equipment"]))
add("b4: Equipment - add cash purchases of equipment (SOLVED)", num(equip_purchases))
add("b4: Equipment - less original cost of equipment sold", num(disp_cost))
add("b4: Equipment - ending balance", num(current["Equipment"]))
add("b5: Accumulated depreciation - beginning balance", num(ad_prior))
add("b5: Accumulated depreciation - add depreciation expense (period-end AJE)", num(IS["Depreciation expense"]))
add("b5: Accumulated depreciation - less accumulated depreciation removed on disposal", num(disp_ad))
add("b5: Accumulated depreciation - ending balance", num(ad_end_check))
add("b5: Book value of equipment sold (550,000 - 70,000)", num(book_value_sold))
add("b5: Loss on sale proved (book value less 390,000 proceeds)", num(loss_check))
add("b6: Retained earnings - beginning balance", num(prior["Retained earnings"]))
add("b6: Retained earnings - add net income", num(net_income))
add("b6: Retained earnings - less cash dividends declared and paid (SOLVED)", num(dividends))
add("b6: Retained earnings - ending balance", num(current["Retained earnings"]))

# (d) cash T-account
add("d: Cash T-account beginning balance (cash + restricted cash)", num(beg_cash_total))
add("d: Operating debit - collections from customers", num(collections))
add("d: Operating credit - payments to suppliers", num(paid_suppliers))
add("d: Operating credit - payments to employees", num(paid_employees))
add("d: Operating credit - interest paid", num(interest_paid))
add("d: Net cash provided by operating activities", num(net_op))
add("d: Investing debit - proceeds from sale of equipment", num(inv_in))
add("d: Investing credit - purchase of equipment", num(inv_out))
add("d: Net cash used in investing activities", num(net_inv))
add("d: Financing debit - proceeds from issuing bonds payable", num(bonds_issued))
add("d: Financing debit - proceeds from issuing common stock", num(stock_issued))
add("d: Financing credit - dividends paid", num(fin_out))
add("d: Net cash used in financing activities", num(net_fin))
add("d: Total cash T-account debits", num(total_debits))
add("d: Total cash T-account credits", num(total_credits))
add("d: Net change per cash T-account (proves to change in cash + restricted cash)", num(net_change))
add("d: Cash T-account ending balance (cash + restricted cash)", num(end_cash_total))
add("d: Entry that does NOT post to the cash T-account",
    "Entry (e), the December 31 period-end depreciation adjusting entry (Dr Depreciation "
    "expense 340,000 / Cr Accumulated depreciation 340,000). It is a purely internal, "
    "noncash allocation of equipment cost already paid for in a prior investing outflow, "
    "so it touches no cash or restricted-cash account and never enters the T-account. "
    "(The 15,000 internal shift of cash into restricted cash likewise nets to zero because "
    "the T-account is kept on a combined cash + restricted cash basis.)")

# (e) direct-method statement of cash flows
add("e: SCF operating - cash collected from customers", num(collections))
add("e: SCF operating - cash paid to suppliers", num(-paid_suppliers))
add("e: SCF operating - cash paid to employees", num(-paid_employees))
add("e: SCF operating - cash paid for interest", num(-interest_paid))
add("e: SCF - net cash provided by operating activities", num(net_op))
add("e: SCF investing - proceeds from sale of equipment", num(inv_in))
add("e: SCF investing - purchase of equipment", num(-inv_out))
add("e: SCF - net cash used in investing activities", num(net_inv))
add("e: SCF financing - proceeds from issuing bonds payable", num(bonds_issued))
add("e: SCF financing - proceeds from issuing common stock", num(stock_issued))
add("e: SCF financing - dividends paid", num(-fin_out))
add("e: SCF - net cash used in financing activities", num(net_fin))
add("e: SCF - net decrease in cash, cash equivalents and restricted cash", num(net_change))
add("e: SCF - cash, cash equivalents and restricted cash, beginning of year", num(beg_cash_total))
add("e: SCF - cash, cash equivalents and restricted cash, end of year", num(end_cash_total))

# (f) classification
add("f: Why the 90,000 loss is not a separate cash outflow",
    "The loss is not a cash flow at all - it is only the difference between the equipment's "
    "480,000 book value (550,000 cost less 70,000 accumulated depreciation) and the 390,000 "
    "cash received. A cash T-account records only actual cash debits and credits, so the "
    "disposal enters it once, as the 390,000 debit. Deducting the loss again would "
    "double-count. It is a noncash income statement item that exists only because "
    "depreciation had not yet written the asset down to its selling price.")
add("f: Where the equipment disposal appears on the SCF",
    "In investing activities as a single line, 'Proceeds from sale of equipment 390,000' "
    "(the full cash received). Under the direct method the 90,000 loss appears nowhere on "
    "the statement; it would only surface as an add-back in the indirect-method operating "
    "reconciliation, which this presentation does not use. The 1,250,000 equipment purchase "
    "is the other investing line, for net cash used in investing of 860,000.")

out = {
    "id": "agent_392#00",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent, applied once per period; all amounts are whole dollars",
    "answers": A,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": "Net income recomputed from the income statement = 1,076,000 (ties to the given figure). "
             "Accumulated depreciation rolls forward 350,000 + 340,000 - 70,000 = 620,000, and book value "
             "480,000 - proceeds 390,000 = the given 90,000 loss, so the data are internally consistent. "
             "The cash T-account is maintained on the ASU 2016-18 combined cash + cash equivalents + "
             "restricted cash basis, so the 15,000 transfer into restricted cash is an internal transfer "
             "with no entry of its own; total debits 4,980,000 less total credits 5,010,000 = (30,000), "
             "which proves to the 170,000 -> 140,000 combined balance change. Ten entries (a)-(j) explain "
             "every income statement account and every balance sheet change; only entry (e), the "
             "highlighted period-end depreciation AJE, is noncash.",
}
print(json.dumps(out, indent=1))
