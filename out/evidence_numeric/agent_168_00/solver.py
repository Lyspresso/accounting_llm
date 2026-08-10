"""
Solver for agent_168#00 -- Harborline Industrial Systems Corp., SCF LO 22-5.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Every computed figure is quantized to whole
dollars using ROUND_HALF_UP, applied per period (each accrual period /
each schedule row is rounded on its own, never on a running float).
Interest is simple interest on face (face x rate x months/12), so every
figure lands exactly on a whole dollar and no rounding difference arises.
The note subsequent-measurement schedule is a face-value (non-amortizing)
schedule: it closes exactly to face $45,000 with interest payable driven
exactly to $0 immediately after the 9/30/20X9 coupon.
Nothing is hard-coded: every derived figure is computed from the given
account activity and additional information. Dr = Cr is proved for each entry.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("1")


def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)


def f(x):
    return float(q(x))


D = Decimal

# ---------------------------------------------------------------- given data
eq_beg = D("720000")
eq_additions = D("245000")
eq_sold_cost = D("55000")
eq_end_given = D("910000")

add_stock = D("70000")
add_note = D("45000")

sold_accum_dep = D("38000")
sale_proceeds = D("14000")
loss_given = D("3000")

lease_rou = D("112000")
lease_cash_paid = D("25000")
lease_interest = D("7000")
lease_principal = D("18000")

cash_stock_other = D("60000")
bonds_cash = D("200000")
notes_retired_cash = D("80000")
dividends_cash = D("42000")

draft_inv_purchase = D("-245000")
draft_inv_proceeds = D("14000")
draft_fin_stock = D("130000")
draft_fin_note = D("45000")
draft_fin_bonds = D("200000")
draft_fin_lease = D("112000")
draft_fin_retire = D("-80000")
draft_fin_lease_prin = D("-18000")
draft_fin_div = D("-42000")

int_exp_other = D("36000")
int_pay_beg = D("5500")
int_pay_end = D("4200")
cap_interest = D("0")
tax_exp = D("74000")
tax_pay_beg = D("16000")
tax_pay_end = D("19500")
tax_refunds = D("0")

restricted_cash = D("28000")

note_face = D("45000")
note_rate = D("0.08")
months_20x8 = D("3")     # Oct 1 -> Dec 31
months_to_coupon = D("9")  # Jan 1 -> Sep 30, 20X9
months_year = D("12")

answers = []
jes = []


def ans(label, value):
    answers.append({"label": label, "value": value})


def je(part, lines):
    dr = sum(D(str(l["debit"])) for l in lines)
    cr = sum(D(str(l["credit"])) for l in lines)
    assert q(dr) == q(cr), (part, dr, cr)
    jes.append({"part": part, "lines": lines})
    return q(dr)


# ------------------------------------------------------------------ part (a)
a1 = je("a(i)", [
    {"account": "Equipment", "debit": f(add_stock), "credit": 0},
    {"account": "Common Stock (and Paid-in Capital) - shares issued at fair value",
     "debit": 0, "credit": f(add_stock)},
])
a2 = je("a(ii)", [
    {"account": "Equipment", "debit": f(add_note), "credit": 0},
    {"account": "Notes Payable (3-year, 8%, dated Oct 1, 20X8)",
     "debit": 0, "credit": f(add_note)},
])
a3 = je("a(iii)", [
    {"account": "Right-of-Use Asset - finance lease", "debit": f(lease_rou), "credit": 0},
    {"account": "Lease Liability", "debit": 0, "credit": f(lease_rou)},
])

ans("a(i): Equipment acquired by issuing common stock - Dr Equipment", f(add_stock))
ans("a(i): Cr Common Stock (fair value of shares issued)", f(add_stock))
ans("a(i): proof entry balances (total debits = total credits)", f(a1))
ans("a(ii): Equipment acquired for Oct 1 note - Dr Equipment", f(add_note))
ans("a(ii): Cr Notes Payable", f(add_note))
ans("a(ii): proof entry balances (total debits = total credits)", f(a2))
ans("a(iii): Finance lease commencement - Dr Right-of-Use Asset", f(lease_rou))
ans("a(iii): Cr Lease Liability", f(lease_rou))
ans("a(iii): proof entry balances (total debits = total credits)", f(a3))
ans("a: no cash is involved in any of the three initial-recognition entries "
    "(cash effect)", 0)

# ------------------------------------------------------------------ part (b)
add_cash = eq_additions - add_stock - add_note
eq_end_calc = eq_beg + eq_additions - eq_sold_cost
assert eq_end_calc == eq_end_given
noncash_add_total = add_stock + add_note

ans("b: Equipment additions - cash purchases", f(add_cash))
ans("b: Equipment additions - noncash, issued common stock", f(add_stock))
ans("b: Equipment additions - noncash, signed Oct 1 3-yr 8% note", f(add_note))
ans("b: Equipment additions - total noncash component", f(noncash_add_total))
ans("b: Equipment additions - total additions per schedule", f(eq_additions))
ans("b: Investing cash outflow for equipment purchases", f(-add_cash))
ans("b: T-account rollforward - Equipment balance Jan 1, 20X8", f(eq_beg))
ans("b: T-account rollforward - add total additions", f(eq_additions))
ans("b: T-account rollforward - deduct cost of equipment sold", f(-eq_sold_cost))
ans("b: T-account rollforward - Equipment balance Dec 31, 20X8 (proved)", f(eq_end_calc))

# ------------------------------------------------------------------ part (c)
int_20x8_note = q(note_face * note_rate * months_20x8 / months_year)
je("c", [
    {"account": "Interest Expense", "debit": f(int_20x8_note), "credit": 0},
    {"account": "Interest Payable", "debit": 0, "credit": f(int_20x8_note)},
])
ans("c: 20X8 interest expense on the Oct 1 equipment note (45,000 x 8% x 3/12)",
    f(int_20x8_note))
ans("c: Dec 31, 20X8 adjusting entry - Dr Interest Expense", f(int_20x8_note))
ans("c: Dec 31, 20X8 adjusting entry - Cr Interest Payable", f(int_20x8_note))
ans("c: proof entry balances (total debits = total credits)", f(int_20x8_note))

# ------------------------------------------------------------------ part (d)
annual_coupon = q(note_face * note_rate)
int_20x9_to_coupon = q(note_face * note_rate * months_to_coupon / months_year)
coupon_check = int_20x8_note + int_20x9_to_coupon
assert coupon_check == annual_coupon
int_pay_after = annual_coupon - int_20x8_note - int_20x9_to_coupon

je("d (9/30/20X9 first coupon)", [
    {"account": "Interest Payable (reversal of 20X8 accrual)",
     "debit": f(int_20x8_note), "credit": 0},
    {"account": "Interest Expense (Jan 1 - Sep 30, 20X9)",
     "debit": f(int_20x9_to_coupon), "credit": 0},
    {"account": "Cash", "debit": 0, "credit": f(annual_coupon)},
])

ans("d: Note carrying amount (face, non-amortizing) at Oct 1, 20X8", f(note_face))
ans("d: Row 1 - 20X8 accrual period Oct 1-Dec 31 interest expense", f(int_20x8_note))
ans("d: Row 1 - cash interest paid in 20X8", 0.0)
ans("d: Row 1 - Interest Payable balance Dec 31, 20X8", f(int_20x8_note))
ans("d: Row 1 - note carrying amount Dec 31, 20X8", f(note_face))
ans("d: Row 2 - 20X9 accrual Jan 1-Sep 30 interest expense (45,000 x 8% x 9/12)",
    f(int_20x9_to_coupon))
ans("d: Row 2 - first annual coupon paid Sep 30, 20X9 (45,000 x 8%)", f(annual_coupon))
ans("d: Row 2 - coupon component: settlement of 20X8 accrued interest payable",
    f(int_20x8_note))
ans("d: Row 2 - coupon component: 20X9 interest expense", f(int_20x9_to_coupon))
ans("d: Row 2 - Interest Payable balance immediately after Sep 30, 20X9 coupon "
    "(schedule closes to zero)", f(int_pay_after))
ans("d: Row 2 - note carrying amount after first coupon (closes exactly to face)",
    f(note_face))

# ------------------------------------------------------------------ part (e)
inv_equip = -add_cash
inv_proceeds = sale_proceeds
inv_net = inv_equip + inv_proceeds

fin_stock = cash_stock_other
fin_bonds = bonds_cash
fin_retire = -notes_retired_cash
fin_lease_prin = -lease_principal
fin_div = -dividends_cash
fin_net = fin_stock + fin_bonds + fin_retire + fin_lease_prin + fin_div

draft_inv_net = draft_inv_purchase + draft_inv_proceeds
draft_fin_net = (draft_fin_stock + draft_fin_note + draft_fin_bonds +
                 draft_fin_lease + draft_fin_retire + draft_fin_lease_prin +
                 draft_fin_div)
draft_combined = draft_inv_net + draft_fin_net
corrected_combined = inv_net + fin_net
combined_diff = corrected_combined - draft_combined

ans("e: Investing - Purchase of equipment (cash portion only)", f(inv_equip))
ans("e: Investing - Proceeds from sale of equipment", f(inv_proceeds))
ans("e: Investing - Net cash used by investing activities (corrected)", f(inv_net))
ans("e: Financing - Issuance of common stock for cash", f(fin_stock))
ans("e: Financing - Proceeds from issuance of bonds payable", f(fin_bonds))
ans("e: Financing - Cash retirement of other notes payable", f(fin_retire))
ans("e: Financing - Principal payments on finance lease", f(fin_lease_prin))
ans("e: Financing - Cash dividends paid", f(fin_div))
ans("e: Financing - Net cash provided by financing activities (corrected)", f(fin_net))
ans("e: Staff draft net investing", f(draft_inv_net))
ans("e: Staff draft net financing", f(draft_fin_net))
ans("e: Staff draft combined investing + financing", f(draft_combined))
ans("e: Corrected combined investing + financing", f(corrected_combined))
ans("e: Change in the combined total caused by removing noncash items",
    f(combined_diff))
ans("e: Paired noncash items removed from BOTH sections - stock-for-equipment "
    "(no effect on combined total)", f(add_stock))
ans("e: Paired noncash items removed from BOTH sections - note-for-equipment "
    "(no effect on combined total)", f(add_note))
ans("e: Unpaired noncash item removed from financing only - lease liability "
    "recognized (drives the entire change in the combined total)", f(lease_rou))
ans("e: explanation",
    "The combined total is NOT unchanged. The two equipment-for-securities items "
    "were mis-shown on both sides of the draft (a $70,000 and a $45,000 investing "
    "outflow paired with the same amounts as financing inflows), so deleting them "
    "nets to zero: investing improves by $115,000 and financing falls by $115,000. "
    "The finance lease was different - the draft reported the $112,000 lease "
    "liability as a financing inflow but never reported an offsetting $112,000 "
    "investing outflow for the right-of-use asset, so it was an unpaired item that "
    "never should have been cash at all. Removing it lowers the combined total by "
    "$112,000, from $116,000 to $4,000. Corrected: investing $(116,000) + "
    "financing $120,000 = $4,000.")

# ------------------------------------------------------------------ part (f)
noncash_total = add_stock + add_note + lease_rou
total_stock_issued = cash_stock_other + add_stock

ans("f: Noncash schedule - Equipment acquired by issuing common stock", f(add_stock))
ans("f: Noncash schedule - Equipment acquired by issuing 3-year 8% note payable",
    f(add_note))
ans("f: Noncash schedule - Right-of-use asset obtained in exchange for finance "
    "lease liability", f(lease_rou))
ans("f: Noncash schedule - Total noncash investing and financing activities",
    f(noncash_total))
ans("f: Relating cash and noncash - total equipment acquired during 20X8",
    f(eq_additions))
ans("f: Relating cash and noncash - portion of equipment acquired for cash "
    "(reported in investing)", f(add_cash))
ans("f: Relating cash and noncash - portion of equipment acquired noncash "
    "(reported in the schedule)", f(noncash_add_total))
ans("f: Relating cash and noncash - total common stock issued during 20X8",
    f(total_stock_issued))
ans("f: Relating cash and noncash - common stock issued for cash", f(cash_stock_other))
ans("f: Relating cash and noncash - common stock issued for equipment", f(add_stock))

# ------------------------------------------------------------------ part (g)
int_paid_other = int_exp_other + int_pay_beg - int_pay_end
int_paid_note_20x8 = D("0")  # first coupon not due until 9/30/20X9
int_paid_total = int_paid_other + lease_interest + int_paid_note_20x8 - cap_interest
taxes_paid = tax_exp + tax_pay_beg - tax_pay_end - tax_refunds

ans("g: Interest paid on other obligations (36,000 + 5,500 - 4,200)", f(int_paid_other))
ans("g: Finance-lease interest paid in cash", f(lease_interest))
ans("g: Cash interest paid on the Oct 1 equipment note during 20X8 "
    "(first coupon not due until 9/30/20X9)", f(int_paid_note_20x8))
ans("g: Less capitalized interest", f(-cap_interest))
ans("g: Total cash paid for interest, net of capitalized interest", f(int_paid_total))
ans("g: Income taxes paid (74,000 + 16,000 - 19,500 - 0)", f(taxes_paid))
ans("g: Restricted cash held as a compensating balance", f(restricted_cash))
ans("g: Restricted cash disclosure requirement",
    "The $28,000 legally restricted compensating balance stays inside the "
    "'cash, cash equivalents, and restricted cash' beginning and ending totals "
    "that the statement of cash flows reconciles to. Harborline must (1) disclose "
    "the nature of the restriction and the long-term credit agreement that imposes "
    "it, and (2) present, on the face of the statement or in the notes, a "
    "reconciliation of the cash/restricted-cash totals used in the statement to "
    "the corresponding line items reported on the balance sheet. Because the "
    "restriction arises from a long-term credit agreement, the balance is also "
    "identified as noncurrent/segregated on the balance sheet.")

# ------------------------------------------------------------------ part (h)
h_items = [
    "1. Report significant noncash investing and financing activities "
    "(equipment for stock, equipment for a note, right-of-use assets obtained "
    "for lease liabilities) in a separate schedule or note - never in the body "
    "of the statement of cash flows.",
    "2. When the indirect method is used, disclose cash paid for interest "
    "(net of any amounts capitalized) and cash paid for income taxes.",
    "3. Report investing and financing cash flows gross - separate cash receipts "
    "from cash payments rather than netting them (e.g., bond proceeds and note "
    "retirements shown separately).",
    "4. Disclose the entity's policy for determining which highly liquid, "
    "short-term investments are treated as cash equivalents.",
    "5. Include restricted cash in the total cash amounts the statement "
    "reconciles, disclose the nature of the restrictions, and reconcile those "
    "totals to the related balance sheet line items.",
]
for i, t in enumerate(h_items, 1):
    ans("h: SCF reporting/disclosure requirement %d of 5" % i, t)

out = {
    "id": "agent_168#00",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to whole dollars applied per "
        "period/per schedule row (no float accumulation). Simple interest = face x "
        "rate x months/12, so every figure is an exact whole dollar and no rounding "
        "difference arises. The Oct 1 note is a face-value, non-amortizing "
        "instrument: the subsequent-measurement schedule closes exactly to face "
        "$45,000 and drives Interest Payable exactly to $0 right after the "
        "9/30/20X9 coupon. Journal entries are stated in whole dollars."
    ),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": (
        "Checks: Equipment rolls forward 720,000 + 245,000 - 55,000 = 910,000 "
        "(ties to the given ending balance). Sale check: book value 55,000 - "
        "38,000 = 17,000 vs. 14,000 proceeds = 3,000 loss, agreeing with the "
        "stated loss already in net income; the loss is added back in operating "
        "and the full 14,000 proceeds appear in investing. Draft correction check: "
        "investing +115,000 (remove the stock- and note-financed equipment), "
        "financing -227,000 (remove 70,000 stock, 45,000 note, 112,000 lease "
        "liability); combined falls 112,000 because the lease liability was the "
        "one unpaired noncash item in the draft. Every entry proved Dr = Cr in "
        "code via assertion. Operating section and the cash-flow reconciliation "
        "were not requested and are not reported."
    ),
}
print(json.dumps(out, indent=1))
