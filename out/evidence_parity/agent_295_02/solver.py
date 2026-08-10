"""Solver for agent_295#02 (LO 22-1, Tidewater Specialty Brands LLC, FY2027).

Rounding convention: all monetary amounts use decimal.Decimal with
ROUND_HALF_UP applied once per period (per-period rounding to the cent);
inputs are whole dollars so results are exact whole dollars. No floats.
Every figure is derived from the scenario inputs; nothing is hard-coded
as an answer.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def r(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------------- inputs (scenario facts) ----------------
bldg_proceeds   = r("140000")
bldg_cost       = r("220000")
bldg_accum_dep  = r("95000")
bonds_face      = r("80000")
interest_paid   = r("9600")
interest_accr   = r("2400")
equip_purchase  = r("55000")
land_note       = r("90000")
bank_note_in    = r("50000")
lease_principal = r("12000")
div_declared    = r("10000")
div_paid_prior  = r("7500")
collections     = r("285000")
paid_suppliers  = r("240000")
taxes_paid      = r("14000")
trading_buy     = r("16000")

cash_bank       = r("71000")
cash_equiv      = r("9500")
restricted_cash = r("4000")
st_equity_inv   = r("19000")   # NOT cash / not an equivalent -> excluded

# ---------------- part a: journal entries ----------------
bldg_bv   = bldg_cost - bldg_accum_dep
bldg_gain = bldg_proceeds - bldg_bv

def je(part, lines):
    d = sum((r(l[1]) for l in lines), Decimal("0"))
    c = sum((r(l[2]) for l in lines), Decimal("0"))
    assert d == c, (part, d, c)
    return {"part": part,
            "lines": [{"account": a, "debit": n(dr), "credit": n(cr)} for a, dr, cr in lines]}, d

jes = []
totals = {}
for key, part, lines in [
    ("1", "a: item 1 - sale of building for cash", [
        ("Cash", bldg_proceeds, 0),
        ("Accumulated Depreciation - Building", bldg_accum_dep, 0),
        ("Building", 0, bldg_cost),
        ("Gain on Sale of Building", 0, bldg_gain)]),
    ("2", "a: item 2 - bonds payable settled at maturity (face, no gain/loss)", [
        ("Bonds Payable", bonds_face, 0),
        ("Cash", 0, bonds_face)]),
    ("4", "a: item 4 - period-end adjusting JE, accrued interest", [
        ("Interest Expense", interest_accr, 0),
        ("Interest Payable", 0, interest_accr)]),
    ("5", "a: item 5 - purchase of production equipment for cash", [
        ("Equipment", equip_purchase, 0),
        ("Cash", 0, equip_purchase)]),
    ("7", "a: item 7 - long-term bank note issued for cash", [
        ("Cash", bank_note_in, 0),
        ("Notes Payable (long-term)", 0, bank_note_in)]),
    ("9", "a: item 9 - period-end adjusting JE, dividends declared", [
        ("Retained Earnings", div_declared, 0),
        ("Dividends Payable", 0, div_declared)]),
]:
    entry, tot = je(part, lines)
    jes.append(entry)
    totals[key] = tot

# ---------------- part c: sections ----------------
operating = collections - paid_suppliers - taxes_paid - interest_paid - trading_buy
investing = bldg_proceeds - equip_purchase
financing = bank_note_in - bonds_face - lease_principal - div_paid_prior
net_change = operating + investing + financing
ending_cash = cash_bank + cash_equiv + restricted_cash   # excludes st_equity_inv
beginning_cash = ending_cash - net_change

answers = []
def A(label, value): answers.append({"label": label, "value": value})

# a - proof each entry balances (equal debit and credit totals)
for k in ["1", "2", "4", "5", "7", "9"]:
    A("a: item %s JE proof - total debits = total credits" % k, n(totals[k]))
A("a: item 1 supporting - book value of building at sale (cost - accum. dep.)", n(bldg_bv))
A("a: item 1 supporting - gain on sale of building", n(bldg_gain))

# b - classification of cash effects
A("b: item 1 - sale of building, $140,000", "Investing INFLOW (I, +$140,000); the $15,000 gain is not a cash flow")
A("b: item 2 - bonds paid at maturity, $80,000", "Financing OUTFLOW (F, -$80,000)")
A("b: item 3 - interest paid in cash, $9,600", "Operating OUTFLOW (O, -$9,600)")
A("b: item 5 - equipment purchased, $55,000", "Investing OUTFLOW (I, -$55,000)")
A("b: item 7 - long-term bank note borrowed, $50,000", "Financing INFLOW (F, +$50,000)")
A("b: item 8 - finance lease principal paid, $12,000", "Financing OUTFLOW (F, -$12,000)")
A("b: item 10 - prior-year dividends paid, $7,500", "Financing OUTFLOW (F, -$7,500)")
A("b: item 11 - collections from customers, $285,000", "Operating INFLOW (O, +$285,000)")
A("b: item 11 - cash paid to suppliers and employees, $240,000", "Operating OUTFLOW (O, -$240,000)")
A("b: item 11 - income taxes paid, $14,000", "Operating OUTFLOW (O, -$14,000)")
A("b: item 12 - trading securities purchased, $16,000", "Operating OUTFLOW (O, -$16,000); securities held for resale/trading are classified by the nature/purpose for which they are held, so they are operating, not investing")
A("b: item 4 - accrued interest, $2,400", "NOT a cash flow on Dec 31 - no cash moved. Under the indirect method it appears only as a noncash add-back / increase in interest payable in the operating reconciliation; under the direct method it is simply excluded (only the $9,600 actually paid is shown).")
A("b: item 6 - land acquired by issuing a $90,000 note", "NOT in any of the three sections - a noncash investing and financing transaction; disclosed in the supplemental noncash schedule (or notes) at $90,000")
A("b: item 9 - dividends declared, $10,000", "NOT a financing cash outflow in 2027 - declaration only; no cash on Dec 31. It becomes a financing outflow when paid in January 2028; the dividends payable increase is a noncash item.")

# c - amounts
A("c: ending cash total per SCF reconciliation (cash + equivalents + restricted cash)", n(ending_cash))
A("c: short-term equity investments excluded from the SCF cash total", n(st_equity_inv))
A("c: net cash provided by operating activities", n(operating))
A("c: net cash provided by investing activities", n(investing))
A("c: net cash used in financing activities", n(financing))
A("c: net change in cash, cash equivalents and restricted cash", n(net_change))
A("c: beginning cash, cash equivalents and restricted cash (solved)", n(beginning_cash))

# d - presentation
A("d: SCF section order",
  "1) Cash flows from OPERATING activities; 2) Cash flows from INVESTING activities; "
  "3) Cash flows from FINANCING activities; 4) Net increase (decrease) in cash, cash equivalents "
  "and restricted cash; 5) Cash, cash equivalents and restricted cash at beginning of year; "
  "6) Cash, cash equivalents and restricted cash at end of year; followed by the supplemental "
  "schedule of noncash investing and financing activities (land acquired by issuing a $90,000 note).")
A("d: reconciliation line 1 - net increase in cash, cash equivalents and restricted cash", n(net_change))
A("d: reconciliation line 2 - beginning cash, cash equivalents and restricted cash", n(beginning_cash))
A("d: reconciliation line 3 - ending cash, cash equivalents and restricted cash", n(ending_cash))
A("d: three-line proof", "Net change $%s + beginning $%s = ending $%s" %
  ("{:,}".format(n(net_change)), "{:,}".format(n(beginning_cash)), "{:,}".format(n(ending_cash))))

# e
A("e: true/false", "False")
A("e: correction",
  "Investing (and financing) cash flows must generally be reported GROSS: major classes of gross "
  "cash receipts and gross cash payments are shown separately - here the $140,000 proceeds from the "
  "building sale and the $55,000 equipment purchase are reported on separate lines, not netted to "
  "$85,000. Net reporting is permitted only in limited cases (items with quick turnover, large "
  "amounts and short maturities), which does not include purchases and sales of PPE.")

print(json.dumps({
    "id": "agent_295#02",
    "rounding_convention": "decimal.Decimal throughout, ROUND_HALF_UP applied once per period (quantized to the cent); all scenario inputs are whole dollars so every reported amount is an exact whole dollar. No floating point used.",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "Cash total per ASU 2016-18 = unrestricted cash $71,000 + money-market equivalents $9,500 + restricted cash $4,000 = $84,500; the $19,000 short-term equity investments are not cash or cash equivalents and are excluded. Operating = 285,000 - 240,000 - 14,000 - 9,600 - 16,000 = 5,400 (trading securities bought for resale are operating). Investing = 140,000 - 55,000 = 85,000. Financing = 50,000 - 80,000 - 12,000 - 7,500 = -49,500. Net change 40,900; beginning cash = 84,500 - 40,900 = 43,600. Items 4 and 9 are period-end accruals with no Dec 31 cash effect; item 6 is a noncash investing/financing transaction disclosed supplementally."
}, indent=1))
