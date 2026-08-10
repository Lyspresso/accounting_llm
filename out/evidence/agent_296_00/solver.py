#!/usr/bin/env python3
"""Blind solver for item agent_296#00 -- Silverpine Logistics Inc.

Topic: LO 22-2. Period-end adjusting JEs, equipment disposal JE, bond
retirement JE, working-capital change schedule, and the indirect-method
cash flows from operating activities section.

ROUNDING CONVENTION
-------------------
All figures in this fact pattern are whole dollars supplied directly by the
comparative balance sheets, the income statement, and the additional
information. Every derived amount is an exact addition/subtraction of those
inputs, so no rounding step is actually reached. Nonetheless, per course
convention, every money value is carried as ``decimal.Decimal`` (never float)
and every quantization uses ``ROUND_HALF_UP`` applied per period / per line
item (never a single round-at-the-end). Output is quantized to cents and then
emitted as an integer when the cents are zero. No present-value work is
required by this item, so no PV table factor vs. exact formula choice arises.

DERIVATION NOTES
----------------
* Gain/loss on disposal is derived from proceeds less book value, then compared
  against the reported income-statement figure as an internal proof.
* Bond premium amortization for the year is NOT given. It is backed out of the
  Premium on Bonds Payable roll-forward: beginning premium, less the premium
  written off with the retired bonds, less ending premium.
* Premium amortization reduces reported interest expense below cash interest
  paid, so on the indirect method it is a DEDUCTION from net income.
* The full statement of cash flows is reconciled to the change in Cash as an
  internal proof; only the figures the Required parts ask for are reported.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def D(x: str | int) -> Decimal:
    return Decimal(str(x))


def q(x: Decimal) -> Decimal:
    """Quantize to cents using ROUND_HALF_UP (applied per line item)."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly money: int when whole, else float-free string-safe Decimal."""
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# GIVEN -- comparative balance sheets (December 31)
# ---------------------------------------------------------------------------
BS = {
    #                         prior            current
    "cash":                  (D(95_000),      D(112_000)),
    "ar_net":                (D(68_000),      D(79_000)),
    "inventory":             (D(55_000),      D(48_000)),
    "prepaid":               (D(8_000),       D(5_000)),
    "equipment":             (D(420_000),     D(510_000)),
    "accum_dep":             (D(140_000),     D(165_000)),   # contra, stated positive
    "patent_net":            (D(48_000),      D(36_000)),
    "ap":                    (D(42_000),      D(51_000)),
    "salaries_payable":      (D(14_000),      D(10_000)),
    "interest_payable":      (D(5_000),       D(7_500)),
    "taxes_payable":         (D(11_000),      D(14_000)),
    "bonds_payable":         (D(150_000),     D(100_000)),
    "premium_on_bonds":      (D(6_000),       D(2_200)),
    "common_stock":          (D(200_000),     D(230_000)),
    "retained_earnings":     (D(126_000),     D(210_300)),
}

PRIOR, CURRENT = 0, 1


def beg(k: str) -> Decimal:
    return BS[k][PRIOR]


def end(k: str) -> Decimal:
    return BS[k][CURRENT]


def change(k: str) -> Decimal:
    return end(k) - beg(k)


# ---------------------------------------------------------------------------
# GIVEN -- income statement (current year)
# ---------------------------------------------------------------------------
SALES              = D(680_000)
COGS               = D(340_000)
DEPRECIATION_EXP   = D(67_000)
PATENT_AMORT_EXP   = D(12_000)
OTHER_OP_EXP       = D(95_000)
GAIN_ON_SALE_RPT   = D(7_000)
LOSS_ON_RETIRE_RPT = D(1_000)
INTEREST_EXP       = D(16_200)
INCOME_TAX_EXP     = D(53_500)
NET_INCOME_RPT     = D(102_300)

# ---------------------------------------------------------------------------
# GIVEN -- additional information
# ---------------------------------------------------------------------------
DIVIDENDS_PAID          = D(18_000)
SALE_PROCEEDS           = D(35_000)
SOLD_EQUIP_COST         = D(70_000)
SOLD_EQUIP_ACCUM_DEP    = D(42_000)
BONDS_RETIRED_FACE      = D(50_000)
BONDS_RETIRED_CASH      = D(53_000)
PREMIUM_WRITTEN_OFF     = D(2_000)

assertions: list[str] = []


def check(name: str, computed: Decimal, expected: Decimal) -> None:
    if q(computed) != q(expected):
        raise AssertionError(f"{name}: computed {computed} != expected {expected}")
    assertions.append(name)


# ---------------------------------------------------------------------------
# Internal proof: income statement foots to reported net income
# ---------------------------------------------------------------------------
ni_computed = (
    SALES - COGS - DEPRECIATION_EXP - PATENT_AMORT_EXP - OTHER_OP_EXP
    + GAIN_ON_SALE_RPT - LOSS_ON_RETIRE_RPT - INTEREST_EXP - INCOME_TAX_EXP
)
check("income statement foots", ni_computed, NET_INCOME_RPT)
NET_INCOME = ni_computed

# Internal proof: retained earnings roll-forward
check(
    "retained earnings roll-forward",
    beg("retained_earnings") + NET_INCOME - DIVIDENDS_PAID,
    end("retained_earnings"),
)

# ---------------------------------------------------------------------------
# (a) Equipment disposal JE -- derive and verify the gain
# ---------------------------------------------------------------------------
book_value_sold = SOLD_EQUIP_COST - SOLD_EQUIP_ACCUM_DEP        # 70,000 - 42,000
gain_on_sale = SALE_PROCEEDS - book_value_sold                  # 35,000 - 28,000
check("(a) gain agrees with income statement", gain_on_sale, GAIN_ON_SALE_RPT)

je_a = {
    "part": "a",
    "description": "Sale of equipment for cash",
    "lines": [
        {"account": "Cash", "debit": num(SALE_PROCEEDS), "credit": 0},
        {"account": "Accumulated Depreciation-Equipment",
         "debit": num(SOLD_EQUIP_ACCUM_DEP), "credit": 0},
        {"account": "Equipment", "debit": 0, "credit": num(SOLD_EQUIP_COST)},
        {"account": "Gain on Sale of Equipment", "debit": 0, "credit": num(gain_on_sale)},
    ],
}

# ---------------------------------------------------------------------------
# (b) Bond retirement (settlement) JE -- derive and verify the loss
# ---------------------------------------------------------------------------
carrying_value_retired = BONDS_RETIRED_FACE + PREMIUM_WRITTEN_OFF   # 50,000 + 2,000
loss_on_retirement = BONDS_RETIRED_CASH - carrying_value_retired    # 53,000 - 52,000
check("(b) loss agrees with income statement", loss_on_retirement, LOSS_ON_RETIRE_RPT)

je_b = {
    "part": "b",
    "description": "Retirement of $50,000 face bonds at 106 on January 1",
    "lines": [
        {"account": "Bonds Payable", "debit": num(BONDS_RETIRED_FACE), "credit": 0},
        {"account": "Premium on Bonds Payable", "debit": num(PREMIUM_WRITTEN_OFF), "credit": 0},
        {"account": "Loss on Bond Retirement", "debit": num(loss_on_retirement), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(BONDS_RETIRED_CASH)},
    ],
}

# Internal proof: Bonds Payable roll-forward
check("bonds payable roll-forward",
      beg("bonds_payable") - BONDS_RETIRED_FACE, end("bonds_payable"))

# ---------------------------------------------------------------------------
# (c) Period-end adjusting JEs with supporting roll-forwards
# ---------------------------------------------------------------------------

# (c1) Depreciation -- Accumulated Depreciation T-account roll-forward:
#      beginning + expense - accumulated dep removed on sale = ending
depreciation_expense = end("accum_dep") - beg("accum_dep") + SOLD_EQUIP_ACCUM_DEP
check("(c1) depreciation agrees with income statement",
      depreciation_expense, DEPRECIATION_EXP)

je_c1 = {
    "part": "c1",
    "description": "Adjusting entry -- depreciation on equipment",
    "lines": [
        {"account": "Depreciation Expense", "debit": num(depreciation_expense), "credit": 0},
        {"account": "Accumulated Depreciation-Equipment",
         "debit": 0, "credit": num(depreciation_expense)},
    ],
}

# (c2) Patent amortization -- Patent, net roll-forward (no purchases or sales):
#      beginning - amortization = ending
patent_amortization = beg("patent_net") - end("patent_net")
check("(c2) patent amortization agrees with income statement",
      patent_amortization, PATENT_AMORT_EXP)

je_c2 = {
    "part": "c2",
    "description": "Adjusting entry -- amortization of patent",
    "lines": [
        {"account": "Amortization Expense-Patent", "debit": num(patent_amortization), "credit": 0},
        {"account": "Patent, net", "debit": 0, "credit": num(patent_amortization)},
    ],
}

# (c3) Bond premium amortization -- Premium on Bonds Payable roll-forward:
#      beginning - premium written off on retirement - amortization = ending
premium_after_retirement = beg("premium_on_bonds") - PREMIUM_WRITTEN_OFF
premium_amortization = premium_after_retirement - end("premium_on_bonds")

je_c3 = {
    "part": "c3",
    "description": "Adjusting entry -- amortization of bond premium (reduces interest expense)",
    "lines": [
        {"account": "Premium on Bonds Payable", "debit": num(premium_amortization), "credit": 0},
        {"account": "Interest Expense", "debit": 0, "credit": num(premium_amortization)},
    ],
}

# ---------------------------------------------------------------------------
# (d) Working-capital change schedule -- SCF sign of each change
#     Operating asset increase  -> deduct;  decrease -> add
#     Operating liability increase -> add;  decrease -> deduct
# ---------------------------------------------------------------------------
OPERATING_ASSETS = [
    ("Accounts receivable (net)", "ar_net"),
    ("Inventory", "inventory"),
    ("Prepaid expenses", "prepaid"),
]
OPERATING_LIABILITIES = [
    ("Accounts payable", "ap"),
    ("Salaries payable", "salaries_payable"),
    ("Interest payable", "interest_payable"),
    ("Income taxes payable", "taxes_payable"),
]

wc_schedule = []
for label, key in OPERATING_ASSETS:
    delta = change(key)
    scf = -delta                       # asset up -> cash down
    wc_schedule.append({
        "item": label,
        "beginning": num(beg(key)),
        "ending": num(end(key)),
        "balance_change": ("increase" if delta > 0 else "decrease"),
        "balance_change_amount": num(abs(delta)),
        "scf_effect": num(scf),
        "scf_sign": ("add" if scf > 0 else "deduct"),
    })
for label, key in OPERATING_LIABILITIES:
    delta = change(key)
    scf = delta                        # liability up -> cash up
    wc_schedule.append({
        "item": label,
        "beginning": num(beg(key)),
        "ending": num(end(key)),
        "balance_change": ("increase" if delta > 0 else "decrease"),
        "balance_change_amount": num(abs(delta)),
        "scf_effect": num(scf),
        "scf_sign": ("add" if scf > 0 else "deduct"),
    })

net_wc_effect = (
    sum((-change(k) for _, k in OPERATING_ASSETS), D(0))
    + sum((change(k) for _, k in OPERATING_LIABILITIES), D(0))
)

# ---------------------------------------------------------------------------
# (e) Cash flows from operating activities -- indirect method
# ---------------------------------------------------------------------------
operating_lines = [
    ("Net income", NET_INCOME),
    ("Add: Depreciation expense", depreciation_expense),
    ("Add: Amortization of patent", patent_amortization),
    ("Deduct: Amortization of bond premium", -premium_amortization),
    ("Deduct: Gain on sale of equipment", -gain_on_sale),
    ("Add: Loss on bond retirement", loss_on_retirement),
]
for row in wc_schedule:
    prefix = "Add" if row["scf_sign"] == "add" else "Deduct"
    direction = row["balance_change"]
    operating_lines.append(
        (f"{prefix}: {direction.capitalize()} in {row['item']}", D(row["scf_effect"]))
    )

net_cash_operating = sum((amt for _, amt in operating_lines), D(0))

# Proof of the total -- direct-method recomputation of the same subtotal.
cash_from_customers = SALES - change("ar_net")
cash_to_suppliers = COGS + change("inventory") - change("ap")
cash_other_operating = OTHER_OP_EXP + change("prepaid") - change("salaries_payable")
cash_interest_paid = INTEREST_EXP + premium_amortization - change("interest_payable")
cash_taxes_paid = INCOME_TAX_EXP - change("taxes_payable")
direct_total = (
    cash_from_customers - cash_to_suppliers - cash_other_operating
    - cash_interest_paid - cash_taxes_paid
)
check("(e) indirect total proved by direct method", net_cash_operating, direct_total)

# Whole-statement proof: operating + investing + financing == change in cash.
equipment_purchases = end("equipment") - (beg("equipment") - SOLD_EQUIP_COST)
stock_issued_for_cash = change("common_stock")
net_investing = SALE_PROCEEDS - equipment_purchases
net_financing = stock_issued_for_cash - BONDS_RETIRED_CASH - DIVIDENDS_PAID
check("statement of cash flows reconciles to change in Cash",
      net_cash_operating + net_investing + net_financing, change("cash"))

# ---------------------------------------------------------------------------
# Journal-entry balance check
# ---------------------------------------------------------------------------
all_entries = [je_a, je_b, je_c1, je_c2, je_c3]
for entry in all_entries:
    dr = sum((D(line["debit"]) for line in entry["lines"]), D(0))
    cr = sum((D(line["credit"]) for line in entry["lines"]), D(0))
    if q(dr) != q(cr):
        raise AssertionError(f"JE {entry['part']} out of balance: {dr} vs {cr}")

# ---------------------------------------------------------------------------
# Answers -- ONLY figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: gain on sale of equipment (verified)", "value": num(gain_on_sale)},
    {"label": "b: loss on bond retirement (verified)", "value": num(loss_on_retirement)},
    {"label": "c1: depreciation expense adjusting entry amount",
     "value": num(depreciation_expense)},
    {"label": "c2: patent amortization adjusting entry amount",
     "value": num(patent_amortization)},
    {"label": "c3: bond premium amortization adjusting entry amount",
     "value": num(premium_amortization)},
]

for row in wc_schedule:
    answers.append({
        "label": f"d: {row['item']} - SCF effect ({row['scf_sign']})",
        "value": row["scf_effect"],
    })
answers.append({
    "label": "d: net working-capital change effect on operating cash flow",
    "value": num(net_wc_effect),
})

for label, amt in operating_lines:
    answers.append({"label": f"e: {label}", "value": num(amt)})
answers.append({
    "label": "e: Net cash provided by operating activities",
    "value": num(net_cash_operating),
})

answers.append({
    "label": "f: $35,000 equipment sale proceeds - section",
    "value": "Investing activities (cash inflow)",
})
answers.append({
    "label": "f: $53,000 bond redemption cash - section",
    "value": "Financing activities (cash outflow)",
})

# ---------------------------------------------------------------------------
# Supporting roll-forward schedules requested in part (c)
# ---------------------------------------------------------------------------
roll_forwards = {
    "accumulated_depreciation_equipment": {
        "beginning_balance": num(beg("accum_dep")),
        "less_removed_on_disposal": num(SOLD_EQUIP_ACCUM_DEP),
        "plus_depreciation_expense": num(depreciation_expense),
        "ending_balance": num(end("accum_dep")),
    },
    "patent_net": {
        "beginning_balance": num(beg("patent_net")),
        "less_amortization": num(patent_amortization),
        "ending_balance": num(end("patent_net")),
    },
    "premium_on_bonds_payable": {
        "beginning_balance": num(beg("premium_on_bonds")),
        "less_premium_written_off_on_retirement": num(PREMIUM_WRITTEN_OFF),
        "balance_after_retirement": num(premium_after_retirement),
        "less_amortization_for_year": num(premium_amortization),
        "ending_balance": num(end("premium_on_bonds")),
    },
}

result = {
    "id": "agent_296#00",
    "rounding_convention": (
        "decimal.Decimal only, never float; ROUND_HALF_UP applied per line item / "
        "per period (not round-at-end); all inputs and results are whole dollars so "
        "no rounding step is actually reached; no PV factors required by this item"
    ),
    "answers": answers,
    "journal_entries": all_entries,
    "supporting_schedules": {
        "c_roll_forwards": roll_forwards,
        "d_working_capital_changes": wc_schedule,
    },
    "insufficient_info": False,
    "notes": (
        "Bond premium amortization of 1,800 is backed out of the Premium on Bonds "
        "Payable roll-forward (6,000 beginning - 2,000 written off with the retired "
        "bonds = 4,000; 4,000 - 2,200 ending = 1,800) and is DEDUCTED on the indirect "
        "method because it made cash interest paid exceed reported interest expense. "
        "The operating total of 183,000 was independently proved by a direct-method "
        "recomputation, and the full statement (183,000 operating, -125,000 investing, "
        "-41,000 financing) reconciles to the 17,000 increase in Cash."
    ),
}

if __name__ == "__main__":
    print(json.dumps(result, indent=2))
