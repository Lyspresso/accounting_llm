#!/usr/bin/env python3
"""Blind solver for item agent_392#00 — Northpine Logistics Corp.

Topic: LO 22-8. Reconstruct entries from comparative balance sheets and an
income statement, build subsequent-measurement (roll-forward) schedules,
complete a full cash T-account, and prepare a direct-method statement of
cash flows.

ROUNDING CONVENTION
-------------------
All money is ``decimal.Decimal``; floats are never used. Every amount in this
fact pattern is a whole dollar and every schedule is a plug from exact
integers, so no rounding is actually triggered. Nevertheless the course
convention is applied deliberately and uniformly: **ROUND_HALF_UP to the cent
(0.01) at each individual step / period** (round-per-period, not
round-at-end). No present-value work is required by this item, so no table
factor vs. exact formula choice arises.

METHOD (all figures derived, nothing hard-coded except the stem's given data)
---------------------------------------------------------------------------
a. Schedule of account changes; change in the total of cash + cash equivalents
   + restricted cash (this combined total is the reconciling subtotal required
   by ASC 230, so internal transfers between unrestricted and restricted cash
   never appear).
b. Roll-forwards, each solved for its single unknown:
     AR:            beg + sales - collections = end
     Inventory:     beg + purchases - COGS = end
     AP:            beg + purchases - payments to suppliers = end
     Sal. payable:  beg + salary expense - payments to employees = end
     Equipment:     beg + acquisitions - cost of disposals = end
     Accum. depr.:  beg + depreciation expense - AD on disposals = end (proof)
     Ret. earnings: beg + net income - dividends = end
c. Ten reconstructed journal entries (a-j). The depreciation adjusting entry
   is flagged ``period_end_adjusting = True`` and ``noncash = True``.
d. Cash T-account, three sections, proved to the part-(a) change.
e. Direct-method statement of cash flows.
f. Qualitative; the loss is not a cash flow at all — the entire $390,000 of
   disposal proceeds is one investing inflow, and the loss is only the
   bookkeeping difference between that inflow and the $480,000 carrying
   amount removed.

Run:  python3 solver.py     -> prints one JSON object on stdout
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def d(x: str) -> Decimal:
    """Money literal from the stem."""
    return Decimal(x)


def r(x: Decimal) -> Decimal:
    """Course rounding convention: ROUND_HALF_UP to the cent, applied per step."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def out(x: Decimal):
    """JSON-friendly number: int when whole, else float-free string-parsed decimal."""
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# GIVEN — comparative balance sheets (prior, current)
# ---------------------------------------------------------------------------
BS = {
    "cash":                {"prior": d("140000"), "current": d("95000")},
    "restricted_cash":     {"prior": d("30000"),  "current": d("45000")},
    "accounts_receivable": {"prior": d("400000"), "current": d("310000")},
    "inventory":           {"prior": d("180000"), "current": d("280000")},
    "equipment":           {"prior": d("2800000"), "current": d("3500000")},
    # carried as a positive balance; it is a contra-asset
    "accumulated_depreciation": {"prior": d("350000"), "current": d("620000")},
    "accounts_payable":    {"prior": d("220000"), "current": d("185000")},
    "salaries_payable":    {"prior": d("60000"),  "current": d("35000")},
    "bonds_payable":       {"prior": d("800000"), "current": d("950000")},
    "common_stock":        {"prior": d("1600000"), "current": d("1750000")},
    "retained_earnings":   {"prior": d("520000"), "current": d("690000")},
}

# GIVEN — income statement (expenses/losses as positive magnitudes)
SALES = d("4200000")
COGS = d("2400000")
SALARY_EXPENSE = d("210000")
INTEREST_EXPENSE = d("84000")
DEPRECIATION_EXPENSE = d("340000")
LOSS_ON_SALE = d("90000")

# GIVEN — additional information
DISPOSAL_COST = d("550000")
DISPOSAL_ACCUM_DEP = d("70000")
DISPOSAL_PROCEEDS = d("390000")

# ---------------------------------------------------------------------------
# Internal consistency checks on the given data (not reported as answers)
# ---------------------------------------------------------------------------
net_income = r(SALES - COGS - SALARY_EXPENSE - INTEREST_EXPENSE
               - DEPRECIATION_EXPENSE - LOSS_ON_SALE)
assert net_income == d("1076000"), net_income

for side in ("prior", "current"):
    assets = (BS["cash"][side] + BS["restricted_cash"][side]
              + BS["accounts_receivable"][side] + BS["inventory"][side]
              + BS["equipment"][side] - BS["accumulated_depreciation"][side])
    le = (BS["accounts_payable"][side] + BS["salaries_payable"][side]
          + BS["bonds_payable"][side] + BS["common_stock"][side]
          + BS["retained_earnings"][side])
    assert assets == le, (side, assets, le)

# ---------------------------------------------------------------------------
# (a) Schedule of account changes
# ---------------------------------------------------------------------------
changes = {k: r(v["current"] - v["prior"]) for k, v in BS.items()}

total_cash_prior = r(BS["cash"]["prior"] + BS["restricted_cash"]["prior"])
total_cash_current = r(BS["cash"]["current"] + BS["restricted_cash"]["current"])
change_total_cash = r(total_cash_current - total_cash_prior)   # part (a) answer

# ---------------------------------------------------------------------------
# (b) Subsequent measurement (roll-forward) schedules — each solves one plug
# ---------------------------------------------------------------------------
# (1) Accounts receivable -> collections from customers
collections = r(BS["accounts_receivable"]["prior"] + SALES
                - BS["accounts_receivable"]["current"])

# (2) Inventory -> purchases; then Accounts payable -> payments to suppliers
purchases = r(BS["inventory"]["current"] + COGS - BS["inventory"]["prior"])
payments_to_suppliers = r(BS["accounts_payable"]["prior"] + purchases
                          - BS["accounts_payable"]["current"])

# (3) Salaries payable -> payments to employees
payments_to_employees = r(BS["salaries_payable"]["prior"] + SALARY_EXPENSE
                          - BS["salaries_payable"]["current"])

# (4) Equipment -> cash acquisitions
equipment_purchases = r(BS["equipment"]["current"] + DISPOSAL_COST
                        - BS["equipment"]["prior"])

# (5) Accumulated depreciation -> proof of the ending balance
accum_dep_check = r(BS["accumulated_depreciation"]["prior"]
                    + DEPRECIATION_EXPENSE - DISPOSAL_ACCUM_DEP)
assert accum_dep_check == BS["accumulated_depreciation"]["current"], accum_dep_check

# (6) Retained earnings -> dividends declared and paid
dividends = r(BS["retained_earnings"]["prior"] + net_income
              - BS["retained_earnings"]["current"])

# Disposal proof: carrying amount vs proceeds must reproduce the stated loss
carrying_amount = r(DISPOSAL_COST - DISPOSAL_ACCUM_DEP)
assert r(carrying_amount - DISPOSAL_PROCEEDS) == LOSS_ON_SALE

# Financing plugs (stem: bond and stock changes were cash transactions)
bonds_issued = changes["bonds_payable"]
stock_issued = changes["common_stock"]
assert bonds_issued > 0 and stock_issued > 0

# Interest: no accrued interest payable at either year-end
interest_paid = INTEREST_EXPENSE

# ---------------------------------------------------------------------------
# (c) Reconstructed journal entries a-j
# ---------------------------------------------------------------------------
def L(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": out(debit), "credit": out(credit)}


journal_entries = [
    {
        "part": "c",
        "ref": "a",
        "description": "Sales on account and collections from customers "
                       "(AR decreased $90,000)",
        "lines": [
            L("Cash", debit=collections),
            L("Accounts Receivable, net",
              credit=-changes["accounts_receivable"]),
            L("Sales Revenue", credit=SALES),
        ],
    },
    {
        "part": "c",
        "ref": "b",
        "description": "Purchases, cost of goods sold, and payments to suppliers "
                       "(Inventory up $100,000; AP down $35,000)",
        "lines": [
            L("Cost of Goods Sold", debit=COGS),
            L("Inventory", debit=changes["inventory"]),
            L("Accounts Payable", debit=-changes["accounts_payable"]),
            L("Cash", credit=payments_to_suppliers),
        ],
    },
    {
        "part": "c",
        "ref": "c",
        "description": "Salary expense and payments to employees "
                       "(Salaries payable down $25,000)",
        "lines": [
            L("Salary Expense", debit=SALARY_EXPENSE),
            L("Salaries Payable", debit=-changes["salaries_payable"]),
            L("Cash", credit=payments_to_employees),
        ],
    },
    {
        "part": "c",
        "ref": "d",
        "description": "Interest expense paid in cash (no accrued interest "
                       "payable at either year-end)",
        "lines": [
            L("Interest Expense", debit=INTEREST_EXPENSE),
            L("Cash", credit=interest_paid),
        ],
    },
    {
        "part": "c",
        "ref": "e",
        "description": "PERIOD-END ADJUSTING ENTRY (December 31) — depreciation "
                       "expense for the year. NONCASH: this is the entry that "
                       "does NOT post to the cash T-account.",
        "period_end_adjusting": True,
        "noncash": True,
        "highlight": True,
        "lines": [
            L("Depreciation Expense", debit=DEPRECIATION_EXPENSE),
            L("Accumulated Depreciation—Equipment", credit=DEPRECIATION_EXPENSE),
        ],
    },
    {
        "part": "c",
        "ref": "f",
        "description": "Sale of equipment: cost $550,000 less accumulated "
                       "depreciation $70,000 = carrying amount $480,000, "
                       "sold for $390,000 cash",
        "lines": [
            L("Cash", debit=DISPOSAL_PROCEEDS),
            L("Accumulated Depreciation—Equipment", debit=DISPOSAL_ACCUM_DEP),
            L("Loss on Sale of Equipment", debit=LOSS_ON_SALE),
            L("Equipment", credit=DISPOSAL_COST),
        ],
    },
    {
        "part": "c",
        "ref": "g",
        "description": "Purchases of equipment for cash",
        "lines": [
            L("Equipment", debit=equipment_purchases),
            L("Cash", credit=equipment_purchases),
        ],
    },
    {
        "part": "c",
        "ref": "h",
        "description": "Issued bonds payable for cash",
        "lines": [
            L("Cash", debit=bonds_issued),
            L("Bonds Payable", credit=bonds_issued),
        ],
    },
    {
        "part": "c",
        "ref": "i",
        "description": "Issued no-par common stock for cash",
        "lines": [
            L("Cash", debit=stock_issued),
            L("Common Stock, no-par", credit=stock_issued),
        ],
    },
    {
        "part": "c",
        "ref": "j",
        "description": "Dividends declared and paid in cash",
        "lines": [
            L("Retained Earnings (Dividends)", debit=dividends),
            L("Cash", credit=dividends),
        ],
    },
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je["ref"], dr, cr)

# ---------------------------------------------------------------------------
# (d) Cash T-account
# ---------------------------------------------------------------------------
operating_inflows = [("Collections from customers", collections)]
operating_outflows = [
    ("Payments to suppliers", payments_to_suppliers),
    ("Payments to employees", payments_to_employees),
    ("Interest paid", interest_paid),
]
investing_inflows = [("Proceeds from sale of equipment", DISPOSAL_PROCEEDS)]
investing_outflows = [("Purchases of equipment", equipment_purchases)]
financing_inflows = [
    ("Proceeds from issuing bonds payable", bonds_issued),
    ("Proceeds from issuing common stock", stock_issued),
]
financing_outflows = [("Dividends paid", dividends)]

net_operating = r(sum((a for _, a in operating_inflows), Decimal("0"))
                  - sum((a for _, a in operating_outflows), Decimal("0")))
net_investing = r(sum((a for _, a in investing_inflows), Decimal("0"))
                  - sum((a for _, a in investing_outflows), Decimal("0")))
net_financing = r(sum((a for _, a in financing_inflows), Decimal("0"))
                  - sum((a for _, a in financing_outflows), Decimal("0")))
net_change = r(net_operating + net_investing + net_financing)

# The T-account must prove to the part (a) change in cash + restricted cash
assert net_change == change_total_cash, (net_change, change_total_cash)
assert r(total_cash_prior + net_change) == total_cash_current

# ---------------------------------------------------------------------------
# Assemble the reported answers (only figures the Required parts ask for)
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: change in cash + cash equivalents + restricted cash "
              "(decrease; $170,000 -> $140,000)",
     "value": out(change_total_cash)},

    {"label": "b(1): cash collected from customers",
     "value": out(collections)},
    {"label": "b(2): cash paid to suppliers",
     "value": out(payments_to_suppliers)},
    {"label": "b(3): cash paid to employees",
     "value": out(payments_to_employees)},
    {"label": "b(4): equipment acquired for cash",
     "value": out(equipment_purchases)},
    {"label": "b(5): accumulated depreciation—equipment, ending balance "
              "(350,000 + 340,000 - 70,000)",
     "value": out(accum_dep_check)},
    {"label": "b(6): dividends declared and paid",
     "value": out(dividends)},

    {"label": "d/e: net cash provided by operating activities (direct method)",
     "value": out(net_operating)},
    {"label": "d/e: net cash used in investing activities",
     "value": out(net_investing)},
    {"label": "d/e: net cash used in financing activities",
     "value": out(net_financing)},
    {"label": "d/e: net decrease in cash, cash equivalents, and restricted cash",
     "value": out(net_change)},

    {"label": "e: cash paid for interest", "value": out(interest_paid)},
    {"label": "e: proceeds from sale of equipment (investing inflow)",
     "value": out(DISPOSAL_PROCEEDS)},
    {"label": "e: proceeds from issuing bonds payable",
     "value": out(bonds_issued)},
    {"label": "e: proceeds from issuing common stock",
     "value": out(stock_issued)},
    {"label": "e: cash, cash equivalents, and restricted cash — beginning of year",
     "value": out(total_cash_prior)},
    {"label": "e: cash, cash equivalents, and restricted cash — end of year",
     "value": out(total_cash_current)},
]

notes = (
    "a. Schedule of account changes (current less prior): cash -45,000; "
    "restricted cash +15,000; AR -90,000; inventory +100,000; equipment "
    "+700,000; accumulated depreciation +270,000; AP -35,000; salaries payable "
    "-25,000; bonds payable +150,000; common stock +150,000; retained earnings "
    "+170,000. Combined cash + cash equivalents + restricted cash fell from "
    "170,000 to 140,000, a decrease of 30,000. "
    "d. Every reconstructed entry posts to the cash T-account EXCEPT entry (e), "
    "the December 31 period-end depreciation adjusting entry (Depreciation "
    "Expense 340,000 / Accumulated Depreciation 340,000): it is purely an "
    "allocation of previously recorded cost, touches no cash account, and so "
    "has no side of the cash T-account to enter. It is the reason net income "
    "and operating cash differ without ever appearing as a cash flow. "
    "f. The 90,000 loss is not a separate outflow because no 90,000 of cash "
    "ever moved. The loss is the difference between the 480,000 carrying "
    "amount removed (550,000 cost less 70,000 accumulated depreciation) and "
    "the 390,000 actually received; the cash T-account records only what hit "
    "cash. The disposal appears once, as a single 390,000 INVESTING inflow, "
    "'Proceeds from sale of equipment.' Under the direct method the loss never "
    "appears at all (there is no net-income starting line to adjust); showing "
    "the loss separately would double count the disposal."
)

result = {
    "id": "agent_392#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP to the cent applied "
        "per step/period (round-per-period, not round-at-end). All amounts in "
        "this item are whole dollars, so no rounding is triggered. No present "
        "value computation is required."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

if __name__ == "__main__":
    print(json.dumps(result, indent=2))
