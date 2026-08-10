#!/usr/bin/env python3
"""
Solver for item agent_130#00 — Ridgeview Outfitters Inc.
Full cash T-account method / direct-method statement of cash flows (LO 22-8).

ROUNDING CONVENTION
-------------------
All monetary amounts are carried as ``decimal.Decimal`` — never floats — with a
working precision of 28 significant digits. Every figure in this fact pattern is
a whole dollar amount and every derived figure is produced by exact addition and
subtraction of whole dollars, so no rounding step is actually exercised. The
convention that WOULD be applied if a quotient or product ever arose is the one
used throughout ACCOUNT-343: ROUND_HALF_UP, applied per period (i.e. each
period's amount is rounded to the cent before being carried into the next
computation), quantized to $0.01. That policy is implemented in ``money()`` and
every reported figure is passed through it, so the discipline is enforced even
though the inputs are exact.

Presentation convention for signs
---------------------------------
Statement-of-cash-flows line items are reported SIGNED: cash inflows positive,
cash outflows negative. Subtotals (net operating / investing / financing and the
net change in cash) are therefore straight sums of their component lines.
Balance-sheet "change" figures in part (a) are reported as
(current year - prior year) for the account's own normal balance, so an increase
in the credit balance of Accumulated depreciation is reported as a positive
260,000 rather than as a negative movement in the asset column.

Nothing below is hard-coded from an answer key. The only inputs are the two
comparative balance sheets, the income statement, and the five "additional
information" facts printed in the stem. Everything else — equipment purchased,
dividends declared, each direct-method operating line, and the proof of the
cash T-account — is solved for.

Run:  python3 solver.py   (prints one JSON object on stdout)
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Coerce to Decimal and apply the course convention: ROUND_HALF_UP to cents."""
    if not isinstance(x, Decimal):
        x = Decimal(str(x))
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def D(x) -> Decimal:
    return Decimal(str(x))


def out(x) -> float | int:
    """JSON-friendly rendering: exact int when whole dollars, else 2dp float."""
    q = money(x)
    return int(q) if q == q.to_integral_value() else float(q)


# ---------------------------------------------------------------------------
# INPUTS — transcribed verbatim from the stem, nothing else.
# ---------------------------------------------------------------------------

# Comparative balance sheets, December 31.  Values are stated at their NORMAL
# balance (assets/contra-assets/liabilities/equity all positive magnitudes);
# accumulated depreciation is a credit balance carried positive here.
PRIOR = {
    "cash": D(80_000),
    "restricted_cash": D(15_000),
    "accounts_receivable_net": D(220_000),
    "inventory": D(90_000),
    "equipment": D(1_600_000),
    "accumulated_depreciation": D(160_000),   # credit balance
    "accounts_payable": D(200_000),
    "salaries_payable": D(40_000),
    "bonds_payable": D(500_000),
    "common_stock": D(900_000),
    "retained_earnings": D(205_000),
}

CURRENT = {
    "cash": D(55_000),
    "restricted_cash": D(25_000),
    "accounts_receivable_net": D(150_000),
    "inventory": D(240_000),
    "equipment": D(2_200_000),
    "accumulated_depreciation": D(420_000),   # credit balance
    "accounts_payable": D(160_000),
    "salaries_payable": D(20_000),
    "bonds_payable": D(650_000),
    "common_stock": D(1_000_000),
    "retained_earnings": D(420_000),
}

# Income statement for the current year (expenses/losses as positive magnitudes)
SALES_REVENUE = D(2_400_000)
COGS = D(1_350_000)
SALARY_EXPENSE = D(100_000)
INTEREST_EXPENSE = D(48_000)
DEPRECIATION_EXPENSE = D(320_000)
LOSS_ON_SALE_OF_EQUIPMENT = D(160_000)

# Additional information
DISPOSAL_ORIGINAL_COST = D(320_000)          # (1)
DISPOSAL_ACCUM_DEPR = D(60_000)              # (1)
DISPOSAL_PROCEEDS = D(100_000)               # (1) cash
# (2) all equipment purchases were for cash
# (3) all dividends declared were paid in cash
# (4) bond and common stock changes were cash transactions
# (5) no accrued interest payable at either year-end


def chg(key: str) -> Decimal:
    """Current-year balance less prior-year balance, on the account's own side."""
    return CURRENT[key] - PRIOR[key]


# ---------------------------------------------------------------------------
# INTERNAL CONSISTENCY CHECKS ON THE GIVEN DATA
# ---------------------------------------------------------------------------

net_income = (
    SALES_REVENUE
    - COGS
    - SALARY_EXPENSE
    - INTEREST_EXPENSE
    - DEPRECIATION_EXPENSE
    - LOSS_ON_SALE_OF_EQUIPMENT
)
assert net_income == D(422_000), f"income statement does not foot: {net_income}"

prior_assets = (
    PRIOR["cash"] + PRIOR["restricted_cash"] + PRIOR["accounts_receivable_net"]
    + PRIOR["inventory"] + PRIOR["equipment"] - PRIOR["accumulated_depreciation"]
)
prior_le = (
    PRIOR["accounts_payable"] + PRIOR["salaries_payable"] + PRIOR["bonds_payable"]
    + PRIOR["common_stock"] + PRIOR["retained_earnings"]
)
assert prior_assets == prior_le == D(1_845_000), "prior balance sheet does not balance"

curr_assets = (
    CURRENT["cash"] + CURRENT["restricted_cash"] + CURRENT["accounts_receivable_net"]
    + CURRENT["inventory"] + CURRENT["equipment"] - CURRENT["accumulated_depreciation"]
)
curr_le = (
    CURRENT["accounts_payable"] + CURRENT["salaries_payable"] + CURRENT["bonds_payable"]
    + CURRENT["common_stock"] + CURRENT["retained_earnings"]
)
assert curr_assets == curr_le == D(2_250_000), "current balance sheet does not balance"

# The loss reported must equal proceeds less book value of the equipment sold.
disposal_book_value = DISPOSAL_ORIGINAL_COST - DISPOSAL_ACCUM_DEPR
derived_loss = disposal_book_value - DISPOSAL_PROCEEDS
assert derived_loss == LOSS_ON_SALE_OF_EQUIPMENT, (
    f"disposal facts imply a loss of {derived_loss}, "
    f"income statement reports {LOSS_ON_SALE_OF_EQUIPMENT}"
)


# ---------------------------------------------------------------------------
# (a) SCHEDULE OF ACCOUNT CHANGES + CHANGE IN CASH, CASH EQUIVALENTS
#     AND RESTRICTED CASH
# ---------------------------------------------------------------------------

d_cash = chg("cash")                              # -25,000
d_restricted = chg("restricted_cash")             # +10,000
d_ar = chg("accounts_receivable_net")             # -70,000
d_inventory = chg("inventory")                    # +150,000
d_equipment = chg("equipment")                    # +600,000
d_accum_depr = chg("accumulated_depreciation")    # +260,000 (credit balance up)
d_ap = chg("accounts_payable")                    # -40,000
d_salaries_payable = chg("salaries_payable")      # -20,000
d_bonds = chg("bonds_payable")                    # +150,000
d_common_stock = chg("common_stock")              # +100,000
d_retained_earnings = chg("retained_earnings")    # +215,000

# ASU 2016-18: the statement of cash flows explains the change in the TOTAL of
# cash, cash equivalents, and restricted cash.
prior_total_cash = PRIOR["cash"] + PRIOR["restricted_cash"]
current_total_cash = CURRENT["cash"] + CURRENT["restricted_cash"]
change_total_cash = current_total_cash - prior_total_cash   # -15,000


# ---------------------------------------------------------------------------
# (c) ROLLFORWARDS — solve for equipment purchased and dividends declared/paid
# ---------------------------------------------------------------------------

# Equipment (debit balance):
#   beginning + purchases - cost of equipment sold = ending
equipment_purchased = (
    CURRENT["equipment"] - PRIOR["equipment"] + DISPOSAL_ORIGINAL_COST
)

# Accumulated depreciation (credit balance):
#   beginning + depreciation expense - accum. depr. removed on disposal = ending
accum_depr_ending_derived = (
    PRIOR["accumulated_depreciation"] + DEPRECIATION_EXPENSE - DISPOSAL_ACCUM_DEPR
)
assert accum_depr_ending_derived == CURRENT["accumulated_depreciation"], (
    "accumulated depreciation rollforward does not tie to the ending balance"
)

# Retained earnings (credit balance):
#   beginning + net income - dividends declared = ending
dividends_declared = (
    PRIOR["retained_earnings"] + net_income - CURRENT["retained_earnings"]
)
dividends_paid = dividends_declared          # additional information (3)

# Bonds and stock: additional information (4) makes both changes cash
proceeds_from_bonds = d_bonds
proceeds_from_stock = d_common_stock


# ---------------------------------------------------------------------------
# (b) RECONSTRUCTED JOURNAL ENTRIES a–j
# ---------------------------------------------------------------------------
# Each entry explains one income statement account (or group) or one balance
# sheet movement.  Cash is the combined "cash + restricted cash" pool that the
# T-account in part (d) proves out; the $10,000 shifted from unrestricted to
# restricted cash is an internal transfer within that pool and therefore has no
# reconstructing entry of its own on the statement.

# (a) Collections from customers: sales less the increase in receivables.
cash_collected_from_customers = SALES_REVENUE - d_ar          # 2,400,000 + 70,000

# (b) Payments to suppliers: COGS grossed up for the inventory build and the
#     decrease in accounts payable.
inventory_purchased = COGS + d_inventory                       # 1,500,000
cash_paid_to_suppliers = inventory_purchased - d_ap            # 1,540,000

# (c) Payments to employees: salary expense plus the decrease in salaries payable.
cash_paid_to_employees = SALARY_EXPENSE - d_salaries_payable   # 120,000

# (d) Interest: no accrual at either year-end, so paid = expense.
cash_paid_for_interest = INTEREST_EXPENSE                      # 48,000

journal_entries = [
    {
        "part": "b",
        "entry": "a",
        "description": "Collections from customers (sales and the decrease in A/R)",
        "lines": [
            {"account": "Cash", "debit": out(cash_collected_from_customers), "credit": 0},
            {"account": "Accounts Receivable, net", "debit": 0, "credit": out(-d_ar)},
            {"account": "Sales Revenue", "debit": 0, "credit": out(SALES_REVENUE)},
        ],
    },
    {
        "part": "b",
        "entry": "b",
        "description": "Payments to suppliers (COGS, inventory build, A/P decrease)",
        "lines": [
            {"account": "Cost of Goods Sold", "debit": out(COGS), "credit": 0},
            {"account": "Inventory", "debit": out(d_inventory), "credit": 0},
            {"account": "Accounts Payable", "debit": out(-d_ap), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": out(cash_paid_to_suppliers)},
        ],
    },
    {
        "part": "b",
        "entry": "c",
        "description": "Payments to employees (salary expense and salaries payable decrease)",
        "lines": [
            {"account": "Salary Expense", "debit": out(SALARY_EXPENSE), "credit": 0},
            {"account": "Salaries Payable", "debit": out(-d_salaries_payable), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": out(cash_paid_to_employees)},
        ],
    },
    {
        "part": "b",
        "entry": "d",
        "description": "Interest paid in cash (no accrued interest at either year-end)",
        "lines": [
            {"account": "Interest Expense", "debit": out(INTEREST_EXPENSE), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": out(cash_paid_for_interest)},
        ],
    },
    {
        "part": "b",
        "entry": "e",
        "description": "Depreciation expense for the year (noncash)",
        "lines": [
            {"account": "Depreciation Expense", "debit": out(DEPRECIATION_EXPENSE), "credit": 0},
            {"account": "Accumulated Depreciation—Equipment", "debit": 0,
             "credit": out(DEPRECIATION_EXPENSE)},
        ],
    },
    {
        "part": "b",
        "entry": "f",
        "description": "Sale of equipment for cash at a loss",
        "lines": [
            {"account": "Cash", "debit": out(DISPOSAL_PROCEEDS), "credit": 0},
            {"account": "Accumulated Depreciation—Equipment",
             "debit": out(DISPOSAL_ACCUM_DEPR), "credit": 0},
            {"account": "Loss on Sale of Equipment",
             "debit": out(LOSS_ON_SALE_OF_EQUIPMENT), "credit": 0},
            {"account": "Equipment", "debit": 0, "credit": out(DISPOSAL_ORIGINAL_COST)},
        ],
    },
    {
        "part": "b",
        "entry": "g",
        "description": "Purchase of equipment for cash (plug in the equipment rollforward)",
        "lines": [
            {"account": "Equipment", "debit": out(equipment_purchased), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": out(equipment_purchased)},
        ],
    },
    {
        "part": "b",
        "entry": "h",
        "description": "Issuance of bonds payable for cash",
        "lines": [
            {"account": "Cash", "debit": out(proceeds_from_bonds), "credit": 0},
            {"account": "Bonds Payable", "debit": 0, "credit": out(proceeds_from_bonds)},
        ],
    },
    {
        "part": "b",
        "entry": "i",
        "description": "Issuance of no-par common stock for cash",
        "lines": [
            {"account": "Cash", "debit": out(proceeds_from_stock), "credit": 0},
            {"account": "Common Stock, no-par", "debit": 0, "credit": out(proceeds_from_stock)},
        ],
    },
    {
        "part": "b",
        "entry": "j",
        "description": "Dividends declared and paid in cash (plug in the retained earnings rollforward)",
        "lines": [
            {"account": "Retained Earnings", "debit": out(dividends_paid), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": out(dividends_paid)},
        ],
    },
]

for je in journal_entries:
    dr = sum(money(l["debit"]) for l in je["lines"])
    cr = sum(money(l["credit"]) for l in je["lines"])
    assert dr == cr, f"entry {je['entry']} does not balance: Dr {dr} vs Cr {cr}"


# ---------------------------------------------------------------------------
# (d) CASH T-ACCOUNT / (e) STATEMENT OF CASH FLOWS — DIRECT METHOD
# ---------------------------------------------------------------------------

net_cash_operating = (
    cash_collected_from_customers
    - cash_paid_to_suppliers
    - cash_paid_to_employees
    - cash_paid_for_interest
)

net_cash_investing = DISPOSAL_PROCEEDS - equipment_purchased

net_cash_financing = proceeds_from_bonds + proceeds_from_stock - dividends_paid

net_change_in_cash = net_cash_operating + net_cash_investing + net_cash_financing

# Prove the T-account to the change in cash + cash equivalents + restricted cash
assert net_change_in_cash == change_total_cash, (
    f"cash T-account does not prove: activity {net_change_in_cash} "
    f"vs balance sheet change {change_total_cash}"
)

ending_total_cash = prior_total_cash + net_change_in_cash
assert ending_total_cash == current_total_cash, "ending total cash does not tie"


# ---------------------------------------------------------------------------
# REPORTED ANSWERS — only figures the Required parts ask for
# ---------------------------------------------------------------------------

answers = [
    # (a) schedule of account changes (current year less prior year)
    {"label": "a: change in Cash and cash equivalents", "value": out(d_cash)},
    {"label": "a: change in Restricted cash", "value": out(d_restricted)},
    {"label": "a: change in Accounts receivable, net", "value": out(d_ar)},
    {"label": "a: change in Inventory", "value": out(d_inventory)},
    {"label": "a: change in Equipment", "value": out(d_equipment)},
    {"label": "a: change in Accumulated depreciation—equipment (credit balance increase)",
     "value": out(d_accum_depr)},
    {"label": "a: change in Accounts payable", "value": out(d_ap)},
    {"label": "a: change in Salaries payable", "value": out(d_salaries_payable)},
    {"label": "a: change in Bonds payable", "value": out(d_bonds)},
    {"label": "a: change in Common stock, no-par", "value": out(d_common_stock)},
    {"label": "a: change in Retained earnings", "value": out(d_retained_earnings)},
    {"label": "a: change in cash + cash equivalents + restricted cash (decrease)",
     "value": out(change_total_cash)},

    # (c) rollforwards
    {"label": "c: Equipment purchased for cash (equipment rollforward plug)",
     "value": out(equipment_purchased)},
    {"label": "c: Equipment, ending balance", "value": out(CURRENT["equipment"])},
    {"label": "c: Accumulated depreciation removed on disposal",
     "value": out(DISPOSAL_ACCUM_DEPR)},
    {"label": "c: Accumulated depreciation, ending balance",
     "value": out(accum_depr_ending_derived)},
    {"label": "c: Dividends declared and paid (retained earnings rollforward plug)",
     "value": out(dividends_paid)},
    {"label": "c: Retained earnings, ending balance",
     "value": out(CURRENT["retained_earnings"])},

    # (d) cash T-account sections, proved to the change in total cash
    {"label": "d: Cash T-account — net cash provided by operating activities",
     "value": out(net_cash_operating)},
    {"label": "d: Cash T-account — net cash used in investing activities",
     "value": out(net_cash_investing)},
    {"label": "d: Cash T-account — net cash provided by financing activities",
     "value": out(net_cash_financing)},
    {"label": "d: Cash T-account — net decrease in cash, cash equivalents and restricted cash",
     "value": out(net_change_in_cash)},

    # (e) statement of cash flows, direct method (inflows +, outflows -)
    {"label": "e: Operating — cash collected from customers",
     "value": out(cash_collected_from_customers)},
    {"label": "e: Operating — cash paid to suppliers",
     "value": out(-cash_paid_to_suppliers)},
    {"label": "e: Operating — cash paid to employees",
     "value": out(-cash_paid_to_employees)},
    {"label": "e: Operating — cash paid for interest",
     "value": out(-cash_paid_for_interest)},
    {"label": "e: Net cash provided by operating activities", "value": out(net_cash_operating)},
    {"label": "e: Investing — proceeds from sale of equipment", "value": out(DISPOSAL_PROCEEDS)},
    {"label": "e: Investing — purchase of equipment", "value": out(-equipment_purchased)},
    {"label": "e: Net cash used in investing activities", "value": out(net_cash_investing)},
    {"label": "e: Financing — proceeds from issuance of bonds payable",
     "value": out(proceeds_from_bonds)},
    {"label": "e: Financing — proceeds from issuance of common stock",
     "value": out(proceeds_from_stock)},
    {"label": "e: Financing — dividends paid", "value": out(-dividends_paid)},
    {"label": "e: Net cash provided by financing activities", "value": out(net_cash_financing)},
    {"label": "e: Net decrease in cash, cash equivalents and restricted cash",
     "value": out(net_change_in_cash)},
    {"label": "e: Cash, cash equivalents and restricted cash, beginning of year",
     "value": out(prior_total_cash)},
    {"label": "e: Cash, cash equivalents and restricted cash, end of year",
     "value": out(ending_total_cash)},
]

notes = (
    "Signs: inflows positive, outflows negative; balance-sheet changes are current "
    "year less prior year stated on each account's normal balance (so the increase "
    "in the credit balance of accumulated depreciation is +260,000). "
    "Part (f), classification/presentation: the $160,000 loss on sale is not a cash "
    "outflow at all — it is the difference between the equipment's $260,000 book "
    "value ($320,000 cost less $60,000 accumulated depreciation) and the $100,000 "
    "received, i.e. a bookkeeping measure of value already consumed and written off, "
    "not cash that left the company. Building the statement from the cash T-account "
    "makes this automatic: the only cash the disposal touched was the $100,000 "
    "received, which is posted to the T-account once, in the investing section, as "
    "'Proceeds from sale of equipment $100,000.' The loss never enters the T-account "
    "because it was never a debit or credit to cash; the entry that recorded it "
    "(Dr Cash 100,000, Dr Accumulated depreciation 60,000, Dr Loss 160,000, "
    "Cr Equipment 320,000) moves the loss against the noncash equipment and "
    "accumulated depreciation accounts. Under the direct method the loss therefore "
    "appears nowhere in the operating section either — there is nothing to add back, "
    "since operating cash flows are built from actual receipts and payments rather "
    "than from net income. (It is only under the indirect method that the loss must "
    "be added back to net income, precisely to undo its noncash effect and to keep "
    "the whole disposal in investing where it belongs.) The disposal's income "
    "statement effect appears solely in the reported net income; its cash effect "
    "appears solely as the $100,000 investing inflow."
)

result = {
    "id": "agent_130#00",
    "rounding_convention": (
        "decimal.Decimal only, never floats; ROUND_HALF_UP quantized to $0.01 applied "
        "per period. All inputs and derived figures are whole dollars, so no rounding "
        "is exercised. Inflows positive / outflows negative in the statement lines."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
