"""Solver for agent_130#00 - Ridgeview Outfitters Inc. full cash T-account method.

Rounding convention: all monetary amounts are decimal.Decimal, quantized to
whole dollars (0.01 precision carried, ROUND_HALF_UP applied once per period /
per reported figure). No floats are used anywhere. Every figure below is derived
from the given comparative balance sheets, income statement, and additional
information; nothing is hard-coded as an answer.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
def R(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)
def D(x):
    # money out: whole dollars (inputs are whole dollars)
    return R(x)
def num(x):
    x = R(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------------- GIVENS ----------------
# Comparative balance sheets (prior, current)
BS = {
    "Cash and cash equivalents":            (Decimal("80000"),  Decimal("55000")),
    "Restricted cash":                      (Decimal("15000"),  Decimal("25000")),
    "Accounts receivable, net":             (Decimal("220000"), Decimal("150000")),
    "Inventory":                            (Decimal("90000"),  Decimal("240000")),
    "Equipment":                            (Decimal("1600000"),Decimal("2200000")),
    "Accumulated depreciation-equipment":   (Decimal("-160000"),Decimal("-420000")),
    "Accounts payable":                     (Decimal("200000"), Decimal("160000")),
    "Salaries payable":                     (Decimal("40000"),  Decimal("20000")),
    "Bonds payable":                        (Decimal("500000"), Decimal("650000")),
    "Common stock, no-par":                 (Decimal("900000"), Decimal("1000000")),
    "Retained earnings":                    (Decimal("205000"), Decimal("420000")),
}
sales      = Decimal("2400000")
cogs       = Decimal("1350000")
salary_exp = Decimal("100000")
interest_exp = Decimal("48000")
dep_exp    = Decimal("320000")
loss_given = Decimal("160000")
net_income = sales - cogs - salary_exp - interest_exp - dep_exp - loss_given
assert net_income == Decimal("422000")

cost_sold      = Decimal("320000")   # add'l info 1
ad_on_sold     = Decimal("60000")    # add'l info 1
proceeds_sale  = Decimal("100000")   # add'l info 1

def chg(k):
    p, c = BS[k]
    return c - p

# ---------------- (a) SCHEDULE OF ACCOUNT CHANGES ----------------
d_cash      = chg("Cash and cash equivalents")
d_restr     = chg("Restricted cash")
d_ar        = chg("Accounts receivable, net")
d_inv       = chg("Inventory")
d_equip     = chg("Equipment")
d_ad        = chg("Accumulated depreciation-equipment")   # negative = contra grew
d_ap        = chg("Accounts payable")
d_salpay    = chg("Salaries payable")
d_bonds     = chg("Bonds payable")
d_cs        = chg("Common stock, no-par")
d_re        = chg("Retained earnings")

beg_total_cash = BS["Cash and cash equivalents"][0] + BS["Restricted cash"][0]
end_total_cash = BS["Cash and cash equivalents"][1] + BS["Restricted cash"][1]
d_total_cash = end_total_cash - beg_total_cash

# ---------------- (c) ROLLFORWARDS ----------------
# Equipment: beg - cost of equipment sold + purchases = end  -> solve purchases
equip_beg = BS["Equipment"][0]; equip_end = BS["Equipment"][1]
equip_purchases = equip_end - equip_beg + cost_sold

# Accumulated depreciation (stated as positive balances)
ad_beg = -BS["Accumulated depreciation-equipment"][0]
ad_end = -BS["Accumulated depreciation-equipment"][1]
assert ad_beg + dep_exp - ad_on_sold == ad_end   # proves dep expense / AD removed

book_value_sold = cost_sold - ad_on_sold
loss_on_sale = book_value_sold - proceeds_sale
assert loss_on_sale == loss_given

# Retained earnings: beg + NI - dividends = end -> solve dividends
re_beg = BS["Retained earnings"][0]; re_end = BS["Retained earnings"][1]
dividends = re_beg + net_income - re_end

bonds_issued = d_bonds
stock_issued = d_cs

# ---------------- (e) DIRECT-METHOD OPERATING AMOUNTS ----------------
cash_from_customers = sales - d_ar                 # AR decreased -> collections exceed sales
inventory_purchases = cogs + d_inv                 # inventory increased -> bought more than sold
cash_to_suppliers   = inventory_purchases - d_ap   # AP decreased -> paid more than purchased
cash_for_salaries   = salary_exp - d_salpay        # salaries payable decreased
cash_for_interest   = interest_exp                 # add'l info 5: no accrual

net_operating = cash_from_customers - cash_to_suppliers - cash_for_salaries - cash_for_interest
net_investing = proceeds_sale - equip_purchases
net_financing = bonds_issued + stock_issued - dividends
net_change = net_operating + net_investing + net_financing
assert net_change == d_total_cash

# ---------------- (d) CASH T-ACCOUNT ----------------
debits = [
    ("Operating - Receipts from customers", cash_from_customers),
    ("Investing - Proceeds from sale of equipment", proceeds_sale),
    ("Financing - Proceeds from issuing bonds payable", bonds_issued),
    ("Financing - Proceeds from issuing common stock", stock_issued),
]
credits = [
    ("Operating - Payments to suppliers of inventory", cash_to_suppliers),
    ("Operating - Payments for salaries", cash_for_salaries),
    ("Operating - Payments for interest", cash_for_interest),
    ("Investing - Purchases of equipment", equip_purchases),
    ("Financing - Dividends paid", dividends),
]
total_debits = sum((v for _, v in debits), Decimal("0"))
total_credits = sum((v for _, v in credits), Decimal("0"))
assert beg_total_cash + total_debits - total_credits == end_total_cash

# ---------------- (b) RECONSTRUCTED JOURNAL ENTRIES ----------------
def je(part, lines):
    dr = sum((Decimal(str(l[1])) for l in lines), Decimal("0"))
    cr = sum((Decimal(str(l[2])) for l in lines), Decimal("0"))
    assert dr == cr, (part, dr, cr)
    return {"part": part, "lines": [
        {"account": a, "debit": num(d), "credit": num(c)} for a, d, c in lines]}

Z = Decimal("0")
journal_entries = [
    je("b - entry (a) collections from customers / sales", [
        ("Cash", cash_from_customers, Z),
        ("Accounts receivable, net", Z, -d_ar),
        ("Sales revenue", Z, sales)]),
    je("b - entry (b) purchases and payments for inventory", [
        ("Cost of goods sold", cogs, Z),
        ("Inventory", d_inv, Z),
        ("Accounts payable", -d_ap, Z),
        ("Cash", Z, cash_to_suppliers)]),
    je("b - entry (c) salary expense and payments", [
        ("Salary expense", salary_exp, Z),
        ("Salaries payable", -d_salpay, Z),
        ("Cash", Z, cash_for_salaries)]),
    je("b - entry (d) interest expense paid in cash", [
        ("Interest expense", interest_exp, Z),
        ("Cash", Z, cash_for_interest)]),
    je("b - entry (e) depreciation expense (noncash)", [
        ("Depreciation expense", dep_exp, Z),
        ("Accumulated depreciation-equipment", Z, dep_exp)]),
    je("b - entry (f) sale of equipment at a loss", [
        ("Cash", proceeds_sale, Z),
        ("Accumulated depreciation-equipment", ad_on_sold, Z),
        ("Loss on sale of equipment", loss_on_sale, Z),
        ("Equipment", Z, cost_sold)]),
    je("b - entry (g) equipment purchased for cash", [
        ("Equipment", equip_purchases, Z),
        ("Cash", Z, equip_purchases)]),
    je("b - entry (h) bonds payable issued for cash", [
        ("Cash", bonds_issued, Z),
        ("Bonds payable", Z, bonds_issued)]),
    je("b - entry (i) common stock issued for cash", [
        ("Cash", stock_issued, Z),
        ("Common stock, no-par", Z, stock_issued)]),
    je("b - entry (j) dividends declared and paid", [
        ("Retained earnings (Dividends)", dividends, Z),
        ("Cash", Z, dividends)]),
    je("b - entry (k) transfer of cash to restricted cash (within the total cash pool; no effect on total cash)", [
        ("Restricted cash", d_restr, Z),
        ("Cash and cash equivalents", Z, d_restr)]),
]
# cash-column proof across entries (a)-(j) plus the internal transfer
cash_effect = (cash_from_customers - cash_to_suppliers - cash_for_salaries
               - cash_for_interest + proceeds_sale - equip_purchases
               + bonds_issued + stock_issued - dividends)
assert cash_effect == d_total_cash
assert cash_effect - d_restr == d_cash   # unrestricted cash line proves to -25,000

A = []
def add(label, value):
    A.append({"label": label, "value": num(value) if isinstance(value, Decimal) else value})

# ---- (a) ----
add("a: Change in Cash and cash equivalents (decrease)", d_cash)
add("a: Change in Restricted cash (increase)", d_restr)
add("a: Change in Accounts receivable, net (decrease)", d_ar)
add("a: Change in Inventory (increase)", d_inv)
add("a: Change in Equipment (increase)", d_equip)
add("a: Change in Accumulated depreciation-equipment (contra increase of 260,000; net asset change)", d_ad)
add("a: Change in Accounts payable (decrease)", d_ap)
add("a: Change in Salaries payable (decrease)", d_salpay)
add("a: Change in Bonds payable (increase)", d_bonds)
add("a: Change in Common stock, no-par (increase)", d_cs)
add("a: Change in Retained earnings (increase)", d_re)
add("a: Beginning cash + cash equivalents + restricted cash", beg_total_cash)
add("a: Ending cash + cash equivalents + restricted cash", end_total_cash)
add("a: Change in cash + cash equivalents + restricted cash (decrease)", d_total_cash)

# ---- (c) ----
add("c: Equipment rollforward - beginning balance", equip_beg)
add("c: Equipment rollforward - less original cost of equipment sold", -cost_sold)
add("c: Equipment rollforward - add equipment purchased for cash (derived)", equip_purchases)
add("c: Equipment rollforward - ending balance", equip_end)
add("c: Accumulated depreciation rollforward - beginning balance", ad_beg)
add("c: Accumulated depreciation rollforward - add depreciation expense", dep_exp)
add("c: Accumulated depreciation rollforward - less accumulated depreciation on equipment sold", -ad_on_sold)
add("c: Accumulated depreciation rollforward - ending balance", ad_end)
add("c: Book value of equipment sold (cost 320,000 less accumulated depreciation 60,000)", book_value_sold)
add("c: Loss on sale of equipment (book value less 100,000 proceeds)", loss_on_sale)
add("c: Retained earnings rollforward - beginning balance", re_beg)
add("c: Retained earnings rollforward - add net income", net_income)
add("c: Retained earnings rollforward - less dividends declared and paid (derived)", -dividends)
add("c: Retained earnings rollforward - ending balance", re_end)

# ---- (d) ----
add("d: Cash T-account - beginning balance (cash + restricted cash)", beg_total_cash)
for lbl, v in debits:
    add("d: Cash T-account debit - " + lbl, v)
for lbl, v in credits:
    add("d: Cash T-account credit - " + lbl, v)
add("d: Cash T-account - total debits (cash receipts)", total_debits)
add("d: Cash T-account - total credits (cash payments)", total_credits)
add("d: Cash T-account - net cash provided by operating activities", net_operating)
add("d: Cash T-account - net cash used in investing activities", net_investing)
add("d: Cash T-account - net cash provided by financing activities", net_financing)
add("d: Cash T-account - net change in cash proved to balance sheet change", net_change)
add("d: Cash T-account - ending balance (cash + restricted cash)", end_total_cash)

# ---- (e) ----
add("e: Operating - Cash received from customers", cash_from_customers)
add("e: Operating - Cash paid for inventory (merchandise)", -cash_to_suppliers)
add("e: Operating - Cash paid for salaries", -cash_for_salaries)
add("e: Operating - Cash paid for interest", -cash_for_interest)
add("e: Net cash provided by operating activities", net_operating)
add("e: Investing - Cash received from sale of equipment", proceeds_sale)
add("e: Investing - Cash paid for equipment purchases", -equip_purchases)
add("e: Net cash used in investing activities", net_investing)
add("e: Financing - Cash received from issuing bonds payable", bonds_issued)
add("e: Financing - Cash received from issuing common stock", stock_issued)
add("e: Financing - Cash paid for dividends", -dividends)
add("e: Net cash provided by financing activities", net_financing)
add("e: Net decrease in cash, cash equivalents, and restricted cash", net_change)
add("e: Cash, cash equivalents, and restricted cash, beginning of year", beg_total_cash)
add("e: Cash, cash equivalents, and restricted cash, end of year", end_total_cash)
add("e: Supplemental - purchases of inventory during the year (COGS + inventory increase)", inventory_purchases)

# ---- (f) ----
add("f: Why the 160,000 loss is not a separate cash outflow",
    "The loss is a noncash bookkeeping figure, not a payment. No cash left the company "
    "because of it: it is simply the excess of the equipment's 260,000 carrying amount "
    "(320,000 cost less 60,000 accumulated depreciation) over the 100,000 cash received. "
    "A statement built from the cash T-account records only amounts that actually ran "
    "through Cash, and the only cash entry for the disposal was the 100,000 debit.")
add("f: Where the equipment disposal appears",
    "In investing activities, as a single 100,000 cash inflow, 'Cash received from sale of "
    "equipment' (the full proceeds). The cost, the accumulated depreciation removed, and the "
    "160,000 loss appear only in the reconstructing journal entry / the equipment and "
    "accumulated depreciation rollforwards, not on the statement of cash flows. Under the "
    "indirect method the same loss would instead be added back to net income; under the "
    "direct method used here there is no add-back line at all.")

out = {
    "id": "agent_130#00",
    "rounding_convention": "decimal.Decimal throughout (no floats); ROUND_HALF_UP applied once per period to whole dollars; all source amounts are exact whole dollars so no rounding differences arise",
    "answers": A,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": ("Restricted cash is included in the total-cash pool reconciled by the statement "
              "(cash + cash equivalents + restricted cash: 95,000 beginning, 80,000 ending, "
              "15,000 decrease), so the 10,000 transfer into restricted cash is an internal "
              "movement within that pool and is not an investing outflow; entry (k) records it. "
              "Derivations: equipment purchases 920,000 solved from the equipment rollforward; "
              "dividends 207,000 solved from the retained earnings rollforward; the accumulated "
              "depreciation rollforward (160,000 + 320,000 - 60,000 = 420,000) and the loss "
              "(260,000 book value - 100,000 proceeds = 160,000) both check against the givens. "
              "Cash T-account proof: 95,000 + 2,820,000 debits - 2,835,000 credits = 80,000.")
}
print(json.dumps(out, indent=1))
