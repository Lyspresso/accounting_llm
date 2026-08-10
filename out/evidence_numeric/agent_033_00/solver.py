"""
Solver for agent_033#00 — Meridian Forge Co. (ASC 230 statement of cash flows).

Rounding convention: all amounts are exact whole dollars (no fractional cents in
the fact pattern). Every Decimal quantization uses ROUND_HALF_UP to the cent and
is presented in whole dollars; no floats are used anywhere. Nothing is
hard-coded downstream: subtotals, net change, ending cash and all journal-entry
plugs (gain/loss, APIC) are derived from the transaction table.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def q(x): return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)
def money(x): return int(q(x))  # whole dollars for reporting

# ---------------------------------------------------------------- inputs
BEGIN_CASH = Decimal("25000")

# (item, description, cash amount, direction(+1 in / -1 out), section)
TX = [
    (1,  "Issued 4,000 shares of $5-par preferred stock at $30 cash",      Decimal("120000"), +1, "F"),
    (2,  "Cash paid to retire long-term bonds early",                       Decimal("80000"),  -1, "F"),
    (3,  "Cash collected from customers",                                   Decimal("400000"), +1, "O"),
    (4,  "Nontrade loan advanced to affiliate",                             Decimal("50000"),  -1, "I"),
    (5,  "Sold patent for cash",                                            Decimal("30000"),  +1, "I"),
    (6,  "Purchased equity securities (not held for trading)",              Decimal("45000"),  -1, "I"),
    (7,  "Issued bonds payable at par for cash",                            Decimal("200000"), +1, "F"),
    (8,  "Purchased treasury stock",                                        Decimal("35000"),  -1, "F"),
    (9,  "Sold land for cash",                                              Decimal("70000"),  +1, "I"),
    (10, "Issued short-term trade note payable (inventory/operating)",      Decimal("20000"),  +1, "O"),
    (11, "Paid cash dividends to preferred shareholders",                   Decimal("25000"),  -1, "F"),
    (12, "Paid cash operating expenses",                                    Decimal("280000"), -1, "O"),
    (13, "Purchased equipment for cash",                                    Decimal("90000"),  -1, "I"),
    (14, "Collected principal on nontrade note receivable",                 Decimal("12000"),  +1, "I"),
    (15, "Paid interest on bonds payable",                                  Decimal("16000"),  -1, "O"),
]
SEC = {"O": "operating", "I": "investing", "F": "financing"}
AMT = {n: a for n, d, a, s, c in TX}

PREF_SHARES, PREF_PAR, PREF_PRICE = Decimal("4000"), Decimal("5"), Decimal("30")
BOND_CA_RETIRED = Decimal("78000")
PATENT_CA = Decimal("22000")
LAND_CA = Decimal("55000")

answers, jes = [], []

# ---------------------------------------------------------------- (a)
for n, desc, amt, dirn, sec in TX:
    flow = "inflow" if dirn > 0 else "outflow"
    answers.append({"label": f"a: item {n} — {desc} — {flow}, {SEC[sec]} ({sec})",
                    "value": money(dirn * amt)})

# ---------------------------------------------------------------- (b)
def je(part, label, lines):
    d = sum(Decimal(l[1]) for l in lines if l[1] is not None)
    c = sum(Decimal(l[2]) for l in lines if l[2] is not None)
    assert q(d) == q(c), (label, d, c)
    jes.append({"part": part, "label": label,
                "lines": [{"account": a, "debit": money(dr or 0), "credit": money(cr or 0)}
                          for a, dr, cr in lines]})

# 1 — preferred stock issuance: par derived, APIC is the plug
pref_par_total = PREF_SHARES * PREF_PAR
pref_cash = PREF_SHARES * PREF_PRICE
assert pref_cash == AMT[1]
pref_apic = pref_cash - pref_par_total
je("b", "Item 1 — issuance of preferred stock for cash", [
    ("Cash", pref_cash, None),
    ("Preferred Stock ($5 par)", None, pref_par_total),
    ("Paid-in Capital in Excess of Par — Preferred", None, pref_apic)])

# 2 — early retirement of bonds: loss is the plug
loss_ext = AMT[2] - BOND_CA_RETIRED
je("b", "Item 2 — early retirement of bonds payable", [
    ("Bonds Payable (carrying amount)", BOND_CA_RETIRED, None),
    ("Loss on Extinguishment of Debt", loss_ext, None),
    ("Cash", None, AMT[2])])

# 5 — sale of patent: gain is the plug
gain_patent = AMT[5] - PATENT_CA
je("b", "Item 5 — sale of patent for cash", [
    ("Cash", AMT[5], None),
    ("Patent (carrying amount)", None, PATENT_CA),
    ("Gain on Sale of Patent", None, gain_patent)])

# 7 — bonds issued at par
je("b", "Item 7 — issuance of bonds payable at par", [
    ("Cash", AMT[7], None),
    ("Bonds Payable", None, AMT[7])])

# 8 — treasury stock (cost method)
je("b", "Item 8 — purchase of treasury stock (cost method)", [
    ("Treasury Stock", AMT[8], None),
    ("Cash", None, AMT[8])])

# 9 — sale of land: gain is the plug
gain_land = AMT[9] - LAND_CA
je("b", "Item 9 — sale of land for cash", [
    ("Cash", AMT[9], None),
    ("Land", None, LAND_CA),
    ("Gain on Sale of Land", None, gain_land)])

# 13 — equipment purchase
je("b", "Item 13 — purchase of equipment for cash", [
    ("Equipment", AMT[13], None),
    ("Cash", None, AMT[13])])

# ---------------------------------------------------------------- (c)
net = {s: sum((d * a for n, ds, a, d, sec in TX if sec == s), Decimal("0")) for s in "OIF"}
net_change = net["O"] + net["I"] + net["F"]
end_cash = BEGIN_CASH + net_change

answers += [
    {"label": "c: Net cash provided by operating activities", "value": money(net["O"])},
    {"label": "c: Net cash used in investing activities", "value": money(net["I"])},
    {"label": "c: Net cash provided by financing activities", "value": money(net["F"])},
    {"label": "c: Net increase in cash, cash equivalents and restricted cash", "value": money(net_change)},
    {"label": "c: Beginning cash, cash equivalents and restricted cash (1/1/2025)", "value": money(BEGIN_CASH)},
    {"label": "c: Ending cash, cash equivalents and restricted cash (12/31/2025) — proof", "value": money(end_cash)},
]

# ---------------------------------------------------------------- (d) SCF format
LINE_NAMES = {
    3:  "Cash received from customers",
    10: "Proceeds from short-term trade note payable (operating)",
    12: "Cash paid for operating expenses",
    15: "Interest paid on bonds payable",
    5:  "Proceeds from sale of patent",
    9:  "Proceeds from sale of land",
    14: "Collection of principal on nontrade note receivable",
    4:  "Nontrade loan advanced to affiliate",
    6:  "Purchase of equity securities (non-trading)",
    13: "Purchase of equipment",
    1:  "Proceeds from issuance of preferred stock",
    7:  "Proceeds from issuance of bonds payable at par",
    2:  "Cash paid to retire bonds payable early",
    8:  "Purchase of treasury stock",
    11: "Cash dividends paid on preferred stock",
}
ORDER = {"O": [3, 10, 12, 15], "I": [5, 9, 14, 4, 6, 13], "F": [1, 7, 2, 8, 11]}
HEAD = {"O": "Cash flows from operating activities",
        "I": "Cash flows from investing activities",
        "F": "Cash flows from financing activities"}
SUBTOTAL = {"O": "Net cash provided by operating activities",
            "I": "Net cash used in investing activities",
            "F": "Net cash provided by financing activities"}
for s in "OIF":
    for n in ORDER[s]:
        dirn = next(d for i, ds, a, d, sec in TX if i == n)
        answers.append({"label": f"d: {HEAD[s]} — {LINE_NAMES[n]}", "value": money(dirn * AMT[n])})
    answers.append({"label": f"d: {SUBTOTAL[s]}", "value": money(net[s])})
answers += [
    {"label": "d: Net increase in cash, cash equivalents and restricted cash", "value": money(net_change)},
    {"label": "d: Cash, cash equivalents and restricted cash, beginning of year", "value": money(BEGIN_CASH)},
    {"label": "d: Cash, cash equivalents and restricted cash, end of year", "value": money(end_cash)},
]

notes = (
    "Whole-dollar presentation; ROUND_HALF_UP; all Decimal, no floats; every JE proved Dr = Cr in code. "
    "Classification logic (ASC 230): interest paid (item 15) is OPERATING under US GAAP; dividends PAID "
    "(item 11) are FINANCING; the short-term note in item 10 is trade/inventory-related operating financing, "
    "so its proceeds are OPERATING (a nontrade short-term borrowing would have been financing); the item 4 "
    "advance and the item 14 principal collection are NONTRADE, so both are INVESTING; equity securities in "
    "item 6 are not held for trading, so the purchase is INVESTING; the item 2 payment to extinguish debt is "
    "FINANCING in full ($80,000) even though $2,000 is a loss, and the item 5/9 gains ($8,000 patent, "
    "$15,000 land) are non-operating gains — the full cash proceeds are INVESTING. "
    "Part (d) 'cash' under ASC 230/ASU 2016-18 = cash on hand and demand deposits, plus cash equivalents "
    "(short-term, highly liquid investments readily convertible to known amounts of cash and so near maturity "
    "that interest-rate risk is insignificant — generally original maturity of three months or less, e.g. "
    "T-bills, commercial paper, money market funds), plus amounts generally described as restricted cash and "
    "restricted cash equivalents; the total of these is what the beginning ($25,000) and ending ($256,000) "
    "amounts reconcile to. Bank overdrafts are not netted into cash. Only the direct-method operating lines "
    "actually given were presented; no noncash investing/financing transactions occurred."
)

print(json.dumps({
    "id": "agent_033#00",
    "rounding_convention": "Decimal arithmetic, ROUND_HALF_UP to the cent each period, presented in whole dollars (all inputs are exact whole dollars); no floats",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
