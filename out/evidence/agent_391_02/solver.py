#!/usr/bin/env python3
"""Blind solver for item agent_391#02 - Riverside Caliper Co. cash flow worksheet.

QUESTION
--------
Reconstructed cash-flow-worksheet entries (indirect method), LO 22-6, for seven
items; classification of every lower-half amount as Operating add / Operating
deduct / Investing inflow-outflow / Financing inflow-outflow; and the net effect
on operating cash flows from items (1)-(4) and (6)-(7).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal, never float. Rounding is ROUND_HALF_UP applied per
period (i.e. each amount is quantized to cents as it is computed, not only at the
end). Every input in this fact pattern is a whole dollar amount and every derived
figure (book value, loss on sale, carrying value, loss on retirement, issue
proceeds, section subtotals) is an exact sum or difference of whole dollars, so
the ROUND_HALF_UP step is a no-op here; it is applied anyway so the convention is
explicit and re-runnable. No present-value factors are involved in this item.

WORKSHEET CONVENTIONS APPLIED (textbook LO 22-6, Demo 22-6 and Review 22-6)
--------------------------------------------------------------------------
* Additions in the statement of cash flows are entered as DEBITS in the lower
  half of the worksheet; deductions are entered as CREDITS.
* Balance-sheet (upper-half) accounts are debited/credited to explain their
  change for the period.
* A change in accounts receivable is carried to the lower half NET of the change
  in the allowance for doubtful accounts, as a single operating line (Demo 22-6
  entry b; Review 22-6 entry a).
* Debits must equal credits in every reconstructed entry; the script asserts this.

DERIVATIONS (nothing below is hard-coded from an answer key)
------------------------------------------------------------
Item 1  Net decrease in AR = 12,000 gross decrease + 2,000 allowance increase
        = 14,000 -> operating add.
Item 2  Inventory increase 6,500 -> operating deduct.
Item 3  Depreciation 28,000 -> operating add (noncash).
Item 4  Book value = 90,000 cost - 55,000 accum. dep. = 35,000.
        Proceeds 30,000 < 35,000 book value -> loss 5,000 (operating add-back);
        30,000 proceeds -> investing inflow.
Item 5  Cash proceeds = 80,000 face x 95/100 = 76,000; discount = 80,000 - 76,000
        = 4,000 (agrees with the stem) -> 76,000 financing inflow.
Item 6  Discount amortization 800 increases interest expense without cash ->
        operating add.
Item 7  Carrying value = 80,000 face - 2,400 unamortized discount = 77,600.
        Cash paid 79,000 > 77,600 -> loss on retirement 1,400 (operating add);
        79,000 -> financing outflow.
Part c  Net operating effect = sum of the operating-section amounts arising from
        items 1-4 and 6-7 (adds positive, deducts negative).

Run:  python3 solver.py       (prints one JSON object on stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(value) -> Decimal:
    """Quantize to cents with ROUND_HALF_UP (applied per period / per amount)."""
    return Decimal(value).quantize(CENTS, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly number: int when the cents are zero, else float-free string-safe."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)  # only reached for non-whole cents; not the case in this item


# ---------------------------------------------------------------------------
# Given facts (stem only)
# ---------------------------------------------------------------------------
AR_DECREASE = money("12000")
ALLOWANCE_INCREASE = money("2000")
INVENTORY_INCREASE = money("6500")
DEPRECIATION = money("28000")

EQUIP_COST = money("90000")
EQUIP_ACCUM_DEP = money("55000")
EQUIP_PROCEEDS = money("30000")

BOND_FACE = money("80000")
BOND_ISSUE_PRICE_PCT = Decimal("95")          # "at 95" = 95% of face
BOND_DISCOUNT_AMORT = money("800")
BOND_UNAMORT_DISCOUNT_AT_RETIREMENT = money("2400")
BOND_RETIREMENT_CASH = money("79000")

# ---------------------------------------------------------------------------
# Derivations
# ---------------------------------------------------------------------------
# Item 1 - net change in accounts receivable carried to the operating section
ar_net_decrease = money(AR_DECREASE + ALLOWANCE_INCREASE)

# Item 4 - disposal of equipment
equip_book_value = money(EQUIP_COST - EQUIP_ACCUM_DEP)
equip_gain_or_loss = money(EQUIP_PROCEEDS - equip_book_value)   # negative => loss
equip_loss = money(-equip_gain_or_loss) if equip_gain_or_loss < 0 else money(0)
equip_gain = equip_gain_or_loss if equip_gain_or_loss > 0 else money(0)

# Item 5 - issuance of bonds at a discount
bond_issue_cash = money(BOND_FACE * BOND_ISSUE_PRICE_PCT / Decimal("100"))
bond_issue_discount = money(BOND_FACE - bond_issue_cash)

# Item 7 - early retirement
bond_carrying_at_retirement = money(BOND_FACE - BOND_UNAMORT_DISCOUNT_AT_RETIREMENT)
retirement_gain_or_loss = money(bond_carrying_at_retirement - BOND_RETIREMENT_CASH)
retirement_loss = money(-retirement_gain_or_loss) if retirement_gain_or_loss < 0 else money(0)
retirement_gain = retirement_gain_or_loss if retirement_gain_or_loss > 0 else money(0)

assert equip_gain == 0, "fact pattern yields a loss on sale, not a gain"
assert retirement_gain == 0, "fact pattern yields a loss on retirement, not a gain"
assert bond_issue_discount == money("4000"), "issue discount must agree with the stem"


# ---------------------------------------------------------------------------
# Part a - reconstructed worksheet entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


entries = [
    {
        "part": "a",
        "item": 1,
        "description": "Period-end WC: change in accounts receivable, net of allowance",
        "lines": [
            line("Decrease in Accounts Receivable-Operating Section", debit=ar_net_decrease),
            line("Accounts Receivable", credit=AR_DECREASE),
            line("Allowance for Doubtful Accounts", credit=ALLOWANCE_INCREASE),
        ],
    },
    {
        "part": "a",
        "item": 2,
        "description": "Period-end WC: increase in inventory",
        "lines": [
            line("Inventory", debit=INVENTORY_INCREASE),
            line("Increase in Inventory-Operating Section", credit=INVENTORY_INCREASE),
        ],
    },
    {
        "part": "a",
        "item": 3,
        "description": "Period-end adjusting: depreciation expense on equipment",
        "lines": [
            line("Depreciation Expense-Operating Section", debit=DEPRECIATION),
            line("Accumulated Depreciation-Equipment", credit=DEPRECIATION),
        ],
    },
    {
        "part": "a",
        "item": 4,
        "description": "Disposal of equipment at a loss",
        "lines": [
            line("Proceeds from Sale of Equipment-Investing Section", debit=EQUIP_PROCEEDS),
            line("Accumulated Depreciation-Equipment", debit=EQUIP_ACCUM_DEP),
            line("Loss on Sale of Equipment-Operating Section", debit=equip_loss),
            line("Equipment", credit=EQUIP_COST),
        ],
    },
    {
        "part": "a",
        "item": 5,
        "description": "Initial recognition: bonds issued at 95 (a discount)",
        "lines": [
            line("Issuance of Bonds Payable-Financing Section", debit=bond_issue_cash),
            line("Discount on Bonds Payable", debit=bond_issue_discount),
            line("Bonds Payable", credit=BOND_FACE),
        ],
    },
    {
        "part": "a",
        "item": 6,
        "description": "Period-end: amortization of bond discount",
        "lines": [
            line("Amortization of Bond Discount-Operating Section", debit=BOND_DISCOUNT_AMORT),
            line("Discount on Bonds Payable", credit=BOND_DISCOUNT_AMORT),
        ],
    },
    {
        "part": "a",
        "item": 7,
        "description": "Settlement: early retirement of bonds at a loss",
        "lines": [
            line("Bonds Payable", debit=BOND_FACE),
            line("Loss on Bond Retirement-Operating Section", debit=retirement_loss),
            line("Discount on Bonds Payable", credit=BOND_UNAMORT_DISCOUNT_AT_RETIREMENT),
            line("Payment for Bond Retirement-Financing Section", credit=BOND_RETIREMENT_CASH),
        ],
    },
]

# Dr = Cr check on every reconstructed entry
for e in entries:
    dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert money(dr) == money(cr), f"item {e['item']} out of balance: {dr} vs {cr}"

# ---------------------------------------------------------------------------
# Part b - every lower-half amount, classified
# ---------------------------------------------------------------------------
OP_ADD = "Operating add"
OP_DED = "Operating deduct"
INV_IN = "Investing inflow"
FIN_IN = "Financing inflow"
FIN_OUT = "Financing outflow"

lower_half = [
    (1, "Decrease in accounts receivable, net of the increase in the allowance", ar_net_decrease, OP_ADD),
    (2, "Increase in inventory", INVENTORY_INCREASE, OP_DED),
    (3, "Depreciation expense", DEPRECIATION, OP_ADD),
    (4, "Loss on sale of equipment", equip_loss, OP_ADD),
    (4, "Proceeds from sale of equipment", EQUIP_PROCEEDS, INV_IN),
    (5, "Issuance of bonds payable", bond_issue_cash, FIN_IN),
    (6, "Amortization of bond discount", BOND_DISCOUNT_AMORT, OP_ADD),
    (7, "Loss on bond retirement", retirement_loss, OP_ADD),
    (7, "Payment for bond retirement", BOND_RETIREMENT_CASH, FIN_OUT),
]

# ---------------------------------------------------------------------------
# Part c - net effect on operating cash flows, items (1)-(4) and (6)-(7)
# ---------------------------------------------------------------------------
PART_C_ITEMS = {1, 2, 3, 4, 6, 7}
net_operating = money(0)
for item_no, _label, amount, section in lower_half:
    if item_no not in PART_C_ITEMS:
        continue
    if section == OP_ADD:
        net_operating = money(net_operating + amount)
    elif section == OP_DED:
        net_operating = money(net_operating - amount)

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
answers = []
for item_no, label, amount, section in lower_half:
    answers.append({
        "label": f"b: item ({item_no}) lower-half amount - {label} - {section}",
        "value": num(amount),
    })
answers.append({
    "label": "c: net effect on operating cash flows from items (1)-(4) and (6)-(7) "
             "(positive = increase in operating cash flows)",
    "value": num(net_operating),
})

result = {
    "id": "agent_391#02",
    "rounding_convention": (
        "decimal.Decimal only, never float; ROUND_HALF_UP quantized to cents per "
        "period/per amount as computed (all figures here are whole dollars, so the "
        "rounding step is a no-op); no PV factors used"
    ),
    "answers": answers,
    "journal_entries": [
        {
            "part": e["part"],
            "item": e["item"],
            "description": e["description"],
            "lines": e["lines"],
        }
        for e in entries
    ],
    "insufficient_info": False,
    "notes": (
        "Part a: seven reconstructed worksheet entries, each balanced (Dr = Cr asserted "
        "in code). Worksheet convention per LO 22-6: SCF additions are debits and SCF "
        "deductions are credits in the lower half; lower-half lines carry the section "
        "name. Item 1 follows the textbook practice of carrying accounts receivable to "
        "the operating section NET of the allowance change (12,000 + 2,000 = 14,000 as a "
        "single operating add), so item 1 produces one lower-half amount rather than two. "
        "Item 4: book value 35,000 vs proceeds 30,000 gives a 5,000 loss added back in "
        "operating, with the 30,000 proceeds an investing inflow. Item 5: 80,000 x 95% = "
        "76,000 cash, a financing inflow (its lower-half amount is listed in part b but "
        "excluded from part c, which is operating-only). Item 7: carrying value 77,600 vs "
        "79,000 paid gives a 1,400 loss added back in operating, with the 79,000 a "
        "financing outflow. Part c sums only the operating-section pieces of items 1-4 "
        "and 6-7: +14,000 - 6,500 + 28,000 + 5,000 + 800 + 1,400. Note the stem's "
        "unamortized discount at retirement (2,400) is a given and is not the 3,200 that "
        "4,000 less one year of 800 amortization would imply; the stem figure is used as "
        "stated and this does not affect any required amount other than through the "
        "1,400 loss, which is computed from it."
    ),
}

print(json.dumps(result, indent=2))
