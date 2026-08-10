#!/usr/bin/env python3
"""Blind solver for item agent_167#01 - Cedarline Packaging Co. (LO 22-4).

Cash flow statement financing section + subsequent-measurement schedules for
bonds/discount, an installment note, a finance lease, and dividends payable,
plus the related journal entries (stock issuance, bond retirement, discount
amortization).

ROUNDING CONVENTION
-------------------
All money is carried as ``decimal.Decimal`` constructed from strings; no binary
floats are used anywhere. The convention for this course is ROUND_HALF_UP
applied per period (each period's figure is rounded before it is carried into
the next period), quantized to the cent (0.01).

In this particular item every amount in the fact pattern is a whole dollar and
every derived amount is obtained by exact addition/subtraction of whole-dollar
amounts (roll-forward reconciliations), so no rounding is actually triggered.
The ROUND_HALF_UP/cent quantization is nonetheless applied to every reported
figure so the convention is enforced rather than merely asserted. There is no
effective-interest computation to perform: interest on the note and on the
lease is given, and the bond discount amortization is a plug derived from the
discount roll-forward, so no PV table factor versus exact formula choice
arises.

SIGN CONVENTION
---------------
Reported financing-activities figures are signed as they appear in the
statement: inflows positive, outflows negative. Journal-entry lines carry
non-negative debit/credit amounts.

Run with: python3 solver.py
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(x: str) -> Decimal:
    """Money constructor: string -> Decimal, quantized ROUND_HALF_UP to cents."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def q(x: Decimal) -> Decimal:
    """Re-apply the per-period rounding convention to a derived amount."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def out(x: Decimal):
    """Render a Decimal for JSON: int when whole, else float-free string->float."""
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Fact pattern from the stem (comparative balance sheet, 12/31/20X4 -> 12/31/20X5)
# ---------------------------------------------------------------------------
BEG = {
    "cash": m("390000"),
    "note": m("120000"),            # installment note payable (nontrade)
    "bonds": m("600000"),           # bonds payable, face
    "discount": m("18000"),         # discount on bonds payable (contra)
    "lease": m("110000"),           # finance lease liability
    "common_stock": m("300000"),    # $5 par
    "apic": m("140000"),
    "treasury": m("0"),
    "div_payable": m("22000"),
    "retained_earnings": m("450000"),
}
END = {
    "cash": m("210000"),
    "note": m("88000"),
    "bonds": m("400000"),
    "discount": m("9000"),
    "lease": m("82000"),
    "common_stock": m("380000"),
    "apic": m("220000"),
    "treasury": m("55000"),
    "div_payable": m("14000"),
    "retained_earnings": m("615000"),
}

# Additional information for 20X5
NET_INCOME = m("250000")                 # (1)
RETIRED_FACE = m("200000")               # (2) bonds retired 3/1/20X5
RETIRE_CASH_PAID = m("196000")           # (2)
RETIRED_UNAMORT_DISCOUNT = m("5500")     # (2)
NOTE_CASH_PAID = m("40400")              # (3) no new borrowings
NOTE_INTEREST = m("8400")                # (3)
LEASE_CASH_PAID = m("40000")             # (4) no new leases
LEASE_INTEREST = m("12000")              # (4)
# (5) common stock issued for cash only
TREASURY_PURCHASED = m("55000")          # (6) cost method, for cash
# (7) dividends payable change relates only to cash dividends declared and paid
# (8) remaining discount amortization recorded 12/31/20X5


# ---------------------------------------------------------------------------
# (a) Cash issuance of common stock
# ---------------------------------------------------------------------------
# Stock was issued for cash only (5) and no treasury shares were reissued (6),
# so the entire change in Common Stock and APIC comes from the cash issuance.
par_issued = q(END["common_stock"] - BEG["common_stock"])
apic_issued = q(END["apic"] - BEG["apic"])
stock_cash_proceeds = q(par_issued + apic_issued)

entry_a = {
    "part": "a",
    "description": "Issuance of common stock for cash",
    "lines": [
        {"account": "Cash", "debit": out(stock_cash_proceeds), "credit": 0},
        {"account": "Common Stock ($5 par)", "debit": 0, "credit": out(par_issued)},
        {"account": "Additional Paid-in Capital", "debit": 0, "credit": out(apic_issued)},
    ],
}


# ---------------------------------------------------------------------------
# (b) Bond retirement, 3/1/20X5
# ---------------------------------------------------------------------------
retired_carrying = q(RETIRED_FACE - RETIRED_UNAMORT_DISCOUNT)
# Cash paid exceeds carrying amount -> loss on early extinguishment.
retire_gain_loss = q(RETIRE_CASH_PAID - retired_carrying)   # positive => loss
loss_on_retirement = retire_gain_loss if retire_gain_loss > 0 else m("0")
gain_on_retirement = q(-retire_gain_loss) if retire_gain_loss < 0 else m("0")

entry_b_lines = [
    {"account": "Bonds Payable", "debit": out(RETIRED_FACE), "credit": 0},
]
if loss_on_retirement > 0:
    entry_b_lines.append(
        {"account": "Loss on Retirement of Bonds", "debit": out(loss_on_retirement), "credit": 0}
    )
entry_b_lines.append(
    {"account": "Discount on Bonds Payable", "debit": 0, "credit": out(RETIRED_UNAMORT_DISCOUNT)}
)
if gain_on_retirement > 0:
    entry_b_lines.append(
        {"account": "Gain on Retirement of Bonds", "debit": 0, "credit": out(gain_on_retirement)}
    )
entry_b_lines.append({"account": "Cash", "debit": 0, "credit": out(RETIRE_CASH_PAID)})

entry_b = {
    "part": "b",
    "description": "Retirement of bonds payable (face $200,000) on March 1, 20X5",
    "lines": entry_b_lines,
}

# Financing classification: the entire cash paid to extinguish the debt is a
# financing outflow. The loss is a non-cash charge included in net income, so
# it is added back in the operating section under the indirect method.
retirement_financing_outflow = q(-RETIRE_CASH_PAID)
loss_operating_addback = loss_on_retirement


# ---------------------------------------------------------------------------
# (c) Subsequent measurement schedules
# ---------------------------------------------------------------------------
# Bonds payable roll-forward (no issuances; only the 3/1 retirement).
bonds_end_derived = q(BEG["bonds"] - RETIRED_FACE)

# Discount roll-forward: beginning discount, less the unamortized discount
# written off with the retired bonds, less amortization for the year, equals
# ending discount. Per (8) the remaining amortization is the 12/31 plug.
discount_after_retirement = q(BEG["discount"] - RETIRED_UNAMORT_DISCOUNT)
discount_amortization = q(discount_after_retirement - END["discount"])

bond_carrying_beg = q(BEG["bonds"] - BEG["discount"])
bond_carrying_end = q(END["bonds"] - END["discount"])

# Installment note: cash paid less interest = principal reduction (no new debt).
note_principal_paid = q(NOTE_CASH_PAID - NOTE_INTEREST)
note_end_derived = q(BEG["note"] - note_principal_paid)

# Finance lease: cash paid less interest = principal reduction (no new leases).
lease_principal_paid = q(LEASE_CASH_PAID - LEASE_INTEREST)
lease_end_derived = q(BEG["lease"] - lease_principal_paid)

# Dividends: retained earnings roll-forward gives declarations; the dividends
# payable roll-forward then gives cash paid.
dividends_declared = q(BEG["retained_earnings"] + NET_INCOME - END["retained_earnings"])
dividends_paid = q(BEG["div_payable"] + dividends_declared - END["div_payable"])


# ---------------------------------------------------------------------------
# (d) Period-end adjusting entry for the remaining discount amortization
# ---------------------------------------------------------------------------
entry_d = {
    "part": "d",
    "description": "December 31, 20X5 amortization of remaining bond discount",
    "lines": [
        {"account": "Interest Expense", "debit": out(discount_amortization), "credit": 0},
        {"account": "Discount on Bonds Payable", "debit": 0, "credit": out(discount_amortization)},
    ],
}


# ---------------------------------------------------------------------------
# (e) Financing activities section
# ---------------------------------------------------------------------------
financing_lines = [
    ("Proceeds from issuance of common stock", stock_cash_proceeds),
    ("Cash paid to retire bonds payable", q(-RETIRE_CASH_PAID)),
    ("Principal payments on installment note payable", q(-note_principal_paid)),
    ("Principal payments on finance lease liability", q(-lease_principal_paid)),
    ("Purchase of treasury stock", q(-TREASURY_PURCHASED)),
    ("Cash dividends paid", q(-dividends_paid)),
]
net_financing = q(sum((amt for _, amt in financing_lines), Decimal("0")))


# ---------------------------------------------------------------------------
# Internal consistency checks (not reported as answers)
# ---------------------------------------------------------------------------
assert bonds_end_derived == END["bonds"], (bonds_end_derived, END["bonds"])
assert note_end_derived == END["note"], (note_end_derived, END["note"])
assert lease_end_derived == END["lease"], (lease_end_derived, END["lease"])
assert q(discount_after_retirement - discount_amortization) == END["discount"]
assert q(BEG["treasury"] + TREASURY_PURCHASED) == END["treasury"]

for e in (entry_a, entry_b, entry_d):
    dr = sum((Decimal(str(l["debit"])) for l in e["lines"]), Decimal("0"))
    cr = sum((Decimal(str(l["credit"])) for l in e["lines"]), Decimal("0"))
    assert q(dr) == q(cr), (e["part"], dr, cr)


# ---------------------------------------------------------------------------
# Reported answers - only figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    # (b) explicitly asks for the financing cash amount and the operating effect
    {"label": "b: financing cash outflow for the bond retirement", "value": out(retirement_financing_outflow)},
    {"label": "b: operating (indirect) effect - add back loss on bond retirement", "value": out(loss_operating_addback)},

    # (c) subsequent measurement schedules
    {"label": "c: bonds payable, face retired March 1, 20X5", "value": out(RETIRED_FACE)},
    {"label": "c: bonds payable, face balance December 31, 20X5", "value": out(bonds_end_derived)},
    {"label": "c: discount on bonds payable removed with retired bonds", "value": out(RETIRED_UNAMORT_DISCOUNT)},
    {"label": "c: remaining bond discount amortization for 20X5", "value": out(discount_amortization)},
    {"label": "c: discount on bonds payable, December 31, 20X5", "value": out(q(discount_after_retirement - discount_amortization))},
    {"label": "c: bonds payable carrying amount, December 31, 20X5", "value": out(bond_carrying_end)},
    {"label": "c: installment note principal reduction in 20X5", "value": out(note_principal_paid)},
    {"label": "c: installment note payable balance, December 31, 20X5", "value": out(note_end_derived)},
    {"label": "c: finance lease principal reduction in 20X5", "value": out(lease_principal_paid)},
    {"label": "c: finance lease liability balance, December 31, 20X5", "value": out(lease_end_derived)},
    {"label": "c: cash dividends declared in 20X5", "value": out(dividends_declared)},
    {"label": "c: cash dividends paid in 20X5", "value": out(dividends_paid)},

    # (e) financing activities section
    {"label": "e: financing - proceeds from issuance of common stock", "value": out(stock_cash_proceeds)},
    {"label": "e: financing - cash paid to retire bonds payable", "value": out(q(-RETIRE_CASH_PAID))},
    {"label": "e: financing - principal payments on installment note payable", "value": out(q(-note_principal_paid))},
    {"label": "e: financing - principal payments on finance lease liability", "value": out(q(-lease_principal_paid))},
    {"label": "e: financing - purchase of treasury stock", "value": out(q(-TREASURY_PURCHASED))},
    {"label": "e: financing - cash dividends paid", "value": out(q(-dividends_paid))},
    {"label": "e: net cash used in financing activities", "value": out(net_financing)},
]

result = {
    "id": "agent_167#01",
    "rounding_convention": (
        "decimal.Decimal only (no floats); ROUND_HALF_UP quantized to the cent "
        "applied per period. All fact-pattern and derived amounts are whole "
        "dollars obtained by exact roll-forward addition/subtraction, so no "
        "rounding is triggered; no PV table factor is required because interest "
        "on the note and lease is given and the bond discount amortization is "
        "the discount roll-forward plug."
    ),
    "answers": answers,
    "journal_entries": [entry_a, entry_b, entry_d],
    "insufficient_info": False,
    "notes": (
        "Financing amounts are signed as presented: inflows positive, outflows "
        "negative. Bond retirement carrying amount 200,000 - 5,500 = 194,500 vs "
        "196,000 cash paid gives a 1,500 loss, a non-cash charge added back in "
        "operating while the full 196,000 is a financing outflow. Interest paid "
        "on the installment note (8,400) and the finance lease (12,000) is "
        "operating under the indirect method and is excluded from financing; "
        "only the principal portions appear there."
    ),
}

print(json.dumps(result, indent=2))
