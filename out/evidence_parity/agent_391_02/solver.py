"""Riverside Caliper Co. — SCF worksheet reconstructed entries (LO 22-6).

Rounding convention: all money handled with decimal.Decimal, quantized to
$0.01 using ROUND_HALF_UP once per period (per computed amount). No floats.
Worksheet convention: lower-half DEBIT = cash inflow / operating add;
lower-half CREDIT = cash outflow / operating deduct. Every figure derived.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---- given inputs (question data only) ----
ar_decrease      = q("12000")
allow_increase   = q("2000")
inv_increase     = q("6500")
depr             = q("28000")
eq_cost          = q("90000")
eq_accum         = q("55000")
eq_proceeds      = q("30000")
bond_face        = q("80000")
issue_pct        = Decimal("95") / Decimal("100")
disc_amort       = q("800")
unamort_at_ret   = q("2400")
cash_paid_retire = q("79000")

# ---- derived ----
eq_bookvalue = q(eq_cost - eq_accum)                 # 35,000
eq_loss      = q(eq_bookvalue - eq_proceeds)         # 5,000 loss (BV > proceeds)
issue_cash   = q(bond_face * issue_pct)              # 76,000
issue_disc   = q(bond_face - issue_cash)             # 4,000
ret_carry    = q(bond_face - unamort_at_ret)         # 77,600
ret_loss     = q(cash_paid_retire - ret_carry)       # 1,400 loss

def E(part, title, lines):
    dr = q(sum((Decimal(str(l[1])) for l in lines), Decimal("0")))
    cr = q(sum((Decimal(str(l[2])) for l in lines), Decimal("0")))
    assert dr == cr, (title, dr, cr)
    return ({"part": part, "entry": title,
             "lines": [{"account": a, "debit": n(d), "credit": n(c)} for a, d, c in lines]}, dr)

Z = Decimal("0")
entries = []
totals = {}

e, t = E("a", "(1) Period-end WC: AR decrease and allowance increase", [
    ("Operating — Decrease in accounts receivable (lower half)", ar_decrease, Z),
    ("Operating — Increase in allowance for doubtful accounts (lower half)", allow_increase, Z),
    ("Accounts receivable", Z, ar_decrease),
    ("Allowance for doubtful accounts", Z, allow_increase)]); entries.append(e); totals["1"] = t

e, t = E("a", "(2) Period-end WC: Inventory increase", [
    ("Inventory", inv_increase, Z),
    ("Operating — Increase in inventory (lower half)", Z, inv_increase)]); entries.append(e); totals["2"] = t

e, t = E("a", "(3) Period-end adjusting: Depreciation expense", [
    ("Operating — Depreciation expense (lower half)", depr, Z),
    ("Accumulated depreciation — equipment", Z, depr)]); entries.append(e); totals["3"] = t

e, t = E("a", "(4) Disposal of equipment", [
    ("Investing — Proceeds from sale of equipment (lower half)", eq_proceeds, Z),
    ("Accumulated depreciation — equipment", eq_accum, Z),
    ("Operating — Loss on sale of equipment (lower half)", eq_loss, Z),
    ("Equipment", Z, eq_cost)]); entries.append(e); totals["4"] = t

e, t = E("a", "(5) Initial recognition: bonds issued at 95", [
    ("Financing — Proceeds from issuance of bonds payable (lower half)", issue_cash, Z),
    ("Discount on bonds payable", issue_disc, Z),
    ("Bonds payable", Z, bond_face)]); entries.append(e); totals["5"] = t

e, t = E("a", "(6) Period-end: amortization of bond discount", [
    ("Operating — Amortization of bond discount (lower half)", disc_amort, Z),
    ("Discount on bonds payable", Z, disc_amort)]); entries.append(e); totals["6"] = t

e, t = E("a", "(7) Settlement: early retirement of bonds", [
    ("Bonds payable", bond_face, Z),
    ("Operating — Loss on early retirement of bonds (lower half)", ret_loss, Z),
    ("Discount on bonds payable", Z, unamort_at_ret),
    ("Financing — Cash paid to retire bonds payable (lower half)", Z, cash_paid_retire)]); entries.append(e); totals["7"] = t

# ---- part c: operating pieces from items (1)-(4) and (6)-(7) ----
op_net = q(ar_decrease + allow_increase - inv_increase + depr + eq_loss + disc_amort + ret_loss)

ans = []
ans.append({"label": "a: derived — equipment book value at disposal (cost 90,000 - accum. dep. 55,000)", "value": n(eq_bookvalue)})
ans.append({"label": "a: derived — loss on sale of equipment (BV 35,000 - proceeds 30,000)", "value": n(eq_loss)})
ans.append({"label": "a: derived — cash proceeds on bond issuance (80,000 x 95%)", "value": n(issue_cash)})
ans.append({"label": "a: derived — discount on bonds payable at issuance", "value": n(issue_disc)})
ans.append({"label": "a: derived — carrying value of bonds at retirement (80,000 - 2,400 unamortized discount)", "value": n(ret_carry)})
ans.append({"label": "a: derived — loss on early retirement (cash paid 79,000 - carrying value 77,600)", "value": n(ret_loss)})
for k in ["1", "2", "3", "4", "5", "6", "7"]:
    ans.append({"label": "a: Dr = Cr check, entry (%s) — total debits = total credits" % k, "value": n(totals[k])})

lower = [
    ("b: (1) Decrease in accounts receivable — Operating add", ar_decrease),
    ("b: (1) Increase in allowance for doubtful accounts — Operating add", allow_increase),
    ("b: (2) Increase in inventory — Operating deduct", inv_increase),
    ("b: (3) Depreciation expense — Operating add", depr),
    ("b: (4) Proceeds from sale of equipment — Investing inflow", eq_proceeds),
    ("b: (4) Loss on sale of equipment — Operating add", eq_loss),
    ("b: (5) Proceeds from bond issuance — Financing inflow", issue_cash),
    ("b: (6) Amortization of bond discount — Operating add", disc_amort),
    ("b: (7) Loss on early retirement of bonds — Operating add", ret_loss),
    ("b: (7) Cash paid to retire bonds — Financing outflow", cash_paid_retire),
]
for lbl, v in lower:
    ans.append({"label": lbl, "value": n(v)})

ans.append({"label": "c: net effect on operating cash flows from items (1)-(4) and (6)-(7) (net addition to net income)", "value": n(op_net)})

print(json.dumps({
    "id": "agent_391#02",
    "rounding_convention": "decimal.Decimal throughout; each computed amount quantized to $0.01 with ROUND_HALF_UP once per period; amounts are whole dollars as given",
    "answers": ans,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": "Worksheet convention: lower-half debit = inflow/operating add, lower-half credit = outflow/operating deduct; upper-half lines are balance-sheet account changes. Item 1 allowance increase is a non-cash contra-asset build (bad debt expense) added back separately from the gross AR change. Item 4: full 30,000 proceeds shown as one Investing inflow with the 5,000 loss added back in Operating (no double count). Item 7: full 79,000 cash paid is a Financing outflow with the 1,400 loss added back in Operating. As given, item 7's unamortized discount (2,400) is not the 4,000 - 800 = 3,200 roll-forward from items 5-6; the question's stated 2,400 is used as the governing fact. Part c excludes item 5 (purely Financing) and counts only Operating-section lines: 12,000 + 2,000 - 6,500 + 28,000 + 5,000 + 800 + 1,400 = 42,700."
}, indent=1))
