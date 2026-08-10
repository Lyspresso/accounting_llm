"""Riverside Caliper Co. - LO 22-6 cash flow worksheet reconstructed entries.

Rounding convention: all money is decimal.Decimal, quantized to cents
(0.01) using ROUND_HALF_UP, applied once per period (year ended 12/31/2025).
Every figure is derived from the scenario inputs; nothing is hard-coded
downstream of the givens. Each reconstructed worksheet entry is asserted Dr = Cr.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

# ---------------- givens ----------------
ar_decrease        = q("12000")
allowance_increase = q("2000")
inventory_increase = q("6500")
depreciation       = q("28000")

eq_cost      = q("90000")
eq_accum_dep = q("55000")
eq_proceeds  = q("30000")

bond_face       = q("80000")
issue_price_pct = Decimal("95") / Decimal("100")   # "at 95"
disc_amort      = q("800")
disc_unamort_at_retire = q("2400")
retire_cash     = q("79000")

# ---------------- derivations ----------------
bond_cash_in   = q(bond_face * issue_price_pct)          # 76,000
bond_discount  = q(bond_face - bond_cash_in)             # 4,000
eq_book_value  = q(eq_cost - eq_accum_dep)               # 35,000
eq_gain        = q(eq_proceeds - eq_book_value)          # (5,000) -> loss 5,000
eq_loss        = q(-eq_gain) if eq_gain < 0 else q(0)
eq_gain_pos    = eq_gain if eq_gain > 0 else q(0)
carry_at_retire = q(bond_face - disc_unamort_at_retire)  # 77,600
retire_gain    = q(carry_at_retire - retire_cash)        # (1,400) -> loss 1,400
retire_loss    = q(-retire_gain) if retire_gain < 0 else q(0)

D = "debit"; C = "credit"
entries = []
def E(part, lines):
    dr = sum((l[1] for l in lines), Decimal("0"))
    cr = sum((l[2] for l in lines), Decimal("0"))
    assert dr == cr, (part, dr, cr)
    entries.append({"part": part,
                    "lines": [{"account": a, "debit": float(d), "credit": float(c)} for a, d, c in lines],
                    "dr_total": float(dr), "cr_total": float(cr)})
    return dr

Z = q(0)
t1a = E("a-1a", [("Operating - Decrease in Accounts Receivable (lower half: Operating add)", ar_decrease, Z),
                 ("Accounts Receivable", Z, ar_decrease)])
t1b = E("a-1b", [("Operating - Increase in Allowance for Doubtful Accounts / bad debt expense (lower half: Operating add)", allowance_increase, Z),
                 ("Allowance for Doubtful Accounts", Z, allowance_increase)])
t2  = E("a-2", [("Inventory", inventory_increase, Z),
                ("Operating - Increase in Inventory (lower half: Operating deduct)", Z, inventory_increase)])
t3  = E("a-3", [("Operating - Depreciation Expense (lower half: Operating add)", depreciation, Z),
                ("Accumulated Depreciation - Equipment", Z, depreciation)])
t4  = E("a-4", [("Investing - Proceeds from Sale of Equipment (lower half: Investing inflow)", eq_proceeds, Z),
                ("Accumulated Depreciation - Equipment", eq_accum_dep, Z),
                ("Operating - Loss on Sale of Equipment (lower half: Operating add)", eq_loss, Z),
                ("Equipment", Z, eq_cost)])
t5  = E("a-5", [("Financing - Proceeds from Issuance of Bonds (lower half: Financing inflow)", bond_cash_in, Z),
                ("Discount on Bonds Payable", bond_discount, Z),
                ("Bonds Payable", Z, bond_face)])
t6  = E("a-6", [("Operating - Amortization of Bond Discount (lower half: Operating add)", disc_amort, Z),
                ("Discount on Bonds Payable", Z, disc_amort)])
t7  = E("a-7", [("Bonds Payable", bond_face, Z),
                ("Operating - Loss on Early Retirement of Bonds (lower half: Operating add)", retire_loss, Z),
                ("Discount on Bonds Payable", Z, disc_unamort_at_retire),
                ("Financing - Retirement of Bonds (lower half: Financing outflow)", Z, retire_cash)])

# ---------------- part c ----------------
op_adds = [ar_decrease, allowance_increase, depreciation, eq_loss, disc_amort, retire_loss]
op_deducts = [inventory_increase]
net_operating = q(sum(op_adds, Decimal("0")) - sum(op_deducts, Decimal("0")))

def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

answers = [
    {"label": "a: Item 1 entry total (Dr = Cr) - AR decrease", "value": n(t1a)},
    {"label": "a: Item 1 entry total (Dr = Cr) - allowance increase", "value": n(t1b)},
    {"label": "a: Item 2 entry total (Dr = Cr)", "value": n(t2)},
    {"label": "a: Item 3 entry total (Dr = Cr)", "value": n(t3)},
    {"label": "a: Item 4 - equipment book value (90,000 - 55,000)", "value": n(eq_book_value)},
    {"label": "a: Item 4 - loss on sale of equipment (35,000 - 30,000)", "value": n(eq_loss)},
    {"label": "a: Item 4 entry total (Dr = Cr)", "value": n(t4)},
    {"label": "a: Item 5 - cash proceeds from bond issuance (80,000 x 95/100)", "value": n(bond_cash_in)},
    {"label": "a: Item 5 - discount on bonds payable (80,000 - 76,000)", "value": n(bond_discount)},
    {"label": "a: Item 5 entry total (Dr = Cr)", "value": n(t5)},
    {"label": "a: Item 6 entry total (Dr = Cr)", "value": n(t6)},
    {"label": "a: Item 7 - carrying value of bonds at retirement (80,000 - 2,400)", "value": n(carry_at_retire)},
    {"label": "a: Item 7 - loss on early retirement (79,000 - 77,600)", "value": n(retire_loss)},
    {"label": "a: Item 7 entry total (Dr = Cr)", "value": n(t7)},
    {"label": "b: Item 1 - decrease in AR = Operating add", "value": n(ar_decrease)},
    {"label": "b: Item 1 - increase in allowance = Operating add", "value": n(allowance_increase)},
    {"label": "b: Item 2 - increase in inventory = Operating deduct", "value": n(inventory_increase)},
    {"label": "b: Item 3 - depreciation expense = Operating add", "value": n(depreciation)},
    {"label": "b: Item 4 - loss on sale of equipment = Operating add", "value": n(eq_loss)},
    {"label": "b: Item 4 - proceeds from sale of equipment = Investing inflow", "value": n(eq_proceeds)},
    {"label": "b: Item 5 - proceeds from bond issuance = Financing inflow", "value": n(bond_cash_in)},
    {"label": "b: Item 6 - amortization of bond discount = Operating add", "value": n(disc_amort)},
    {"label": "b: Item 7 - loss on early retirement of bonds = Operating add", "value": n(retire_loss)},
    {"label": "b: Item 7 - cash paid to retire bonds = Financing outflow", "value": n(retire_cash)},
    {"label": "c: Total operating adds from items (1)-(4) and (6)-(7)", "value": n(sum(op_adds, Decimal('0')))},
    {"label": "c: Total operating deducts from items (1)-(4) and (6)-(7)", "value": n(sum(op_deducts, Decimal('0')))},
    {"label": "c: Net effect on operating cash flows (indirect), items (1)-(4) and (6)-(7)", "value": n(net_operating)},
]

notes = (
    "Worksheet (reconstructed) entries only; no formal SCF prepared. Lower-half lines are labeled "
    "with their section inside the account name. Item 4: book value 35,000 > proceeds 30,000, so a "
    "5,000 loss is added back in Operating while the full 30,000 cash is an Investing inflow. Item 5: "
    "80,000 x 95/100 = 76,000 cash, a Financing inflow; the 4,000 discount is a balance-sheet (upper-half) "
    "debit with no cash effect. Item 7: carrying value 80,000 - 2,400 = 77,600 vs 79,000 paid = 1,400 loss "
    "added back in Operating, with the full 79,000 shown as a Financing outflow. Internal-consistency note: "
    "4,000 discount at issuance less 800 amortized would leave 3,200, but the problem states 2,400 unamortized "
    "at retirement; the stated 2,400 was used as given (implies additional amortization/other bond tranche). "
    "Part c excludes item 5 entirely (pure Financing) and excludes the Investing 30,000 and Financing 79,000 "
    "cash lines; only Operating-section pieces are counted: +12,000 +2,000 -6,500 +28,000 +5,000 +800 +1,400 = +42,700."
)

print(json.dumps({
    "id": "agent_391#02",
    "rounding_convention": "decimal.Decimal throughout; quantized to cents (0.01) with ROUND_HALF_UP, applied once per period (FY ended 12/31/2025); all amounts resolve to whole dollars",
    "answers": answers,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
