#!/usr/bin/env python3
"""Blind solver for item agent_295#02 (Tidewater Specialty Brands LLC, FY 2027 SCF).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to whole cents (Decimal quantize to 0.01) applied at each reported
figure. Every fact in this stem is a whole-dollar amount and every operation is
addition/subtraction of those amounts, so no rounding is actually triggered; the
convention is stated and applied so the arithmetic is reproducible. All money is
decimal.Decimal built from strings -- no floats anywhere. No present-value work is
required by this item, so no PV table factors are used.

AUTHORITIES APPLIED (ACCOUNT-343 Ch. 22, ASC 230)
-------------------------------------------------
* "Cash" on the SCF = cash + cash equivalents + restricted cash (ASC 230-10-45-24).
  Short-term equity investments that are not cash equivalents are excluded.
* Purchases of TRADING securities (acquired for resale / trading profits) are
  OPERATING cash flows (ASC 230-10-45-18; Ch. 22: "cash used to purchase trading
  securities" is an operating flow even though it does not enter net income).
* Interest paid = operating. Income taxes paid = operating.
* Proceeds from sale of PPE and payments to acquire PPE = investing, reported gross
  (ASC 230-10-45-12/13, 45-26).
* Proceeds from nontrade borrowing, repayment of debt principal at maturity, finance
  lease PRINCIPAL payments, and dividends PAID in cash = financing
  (ASC 230-10-45-14/15; Ch. 22 Exhibit 22-4 splits finance lease payments:
  interest = operating, principal = financing).
* Accruals with no cash movement (item 4 interest accrual, item 9 dividend
  declaration) and noncash investing/financing exchanges (item 6 land for note) are
  NOT cash flows; the noncash land-for-note exchange is disclosed in the supplemental
  schedule of noncash investing and financing activities (ASC 230-10-50-3/4).
* Beginning cash is solved by the reconciliation:
  beginning = ending - (operating + investing + financing).

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(s):
    """Money constructor: Decimal from a string, never a float."""
    return Decimal(s)


def r(x):
    """Apply the stated rounding convention: ROUND_HALF_UP to cents."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def out(x):
    """Render a Decimal as a plain JSON number (int when it is a whole dollar)."""
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Fact pattern (transcribed from the stem; nothing here is an answer)
# ---------------------------------------------------------------------------
# 1. Building sold for cash
BLDG_PROCEEDS = m("140000")
BLDG_COST = m("220000")
BLDG_ACC_DEP = m("95000")
# 2. Bonds settled at face on maturity
BONDS_FACE = m("80000")
# 3. Cash interest paid on those bonds during the year
INTEREST_PAID = m("9600")
# 4. Period-end accrual of unpaid interest (no cash)
INTEREST_ACCRUED = m("2400")
# 5. Equipment purchased for cash
EQUIP_PURCHASE = m("55000")
# 6. Land acquired by issuing a long-term note (no cash)
LAND_FOR_NOTE = m("90000")
# 7. Cash borrowed on a long-term (nontrade) bank note
BANK_NOTE_PROCEEDS = m("50000")
# 8. Cash principal paid on finance lease liability
LEASE_PRINCIPAL = m("12000")
# 9. Period-end declaration of dividends payable in Jan 2028 (no cash)
DIV_DECLARED = m("10000")
# 10. Cash paid on dividends declared in the prior year
DIV_PAID = m("7500")
# 11. Operating cash flows
COLLECTIONS = m("285000")
PAID_SUPPLIERS_EMPLOYEES = m("240000")
TAXES_PAID = m("14000")
# 12. Purchase of short-term TRADING equity securities for cash
TRADING_PURCHASE = m("16000")

# Dec 31, 2027 cash composition
CASH_IN_BANK = m("71000")
CASH_EQUIVALENTS = m("9500")
RESTRICTED_CASH = m("4000")
ST_EQUITY_INVESTMENTS = m("19000")  # not cash equivalents -> excluded from SCF cash


# ---------------------------------------------------------------------------
# Part a -- journal entries
# ---------------------------------------------------------------------------
def entry(part, lines):
    total_dr = sum((ln["_dr"] for ln in lines), Decimal("0"))
    total_cr = sum((ln["_cr"] for ln in lines), Decimal("0"))
    assert r(total_dr) == r(total_cr), (part, total_dr, total_cr)
    return {
        "part": part,
        "lines": [
            {"account": ln["account"], "debit": out(ln["_dr"]), "credit": out(ln["_cr"])}
            for ln in lines
        ],
    }


def dr(account, amt):
    return {"account": account, "_dr": amt, "_cr": Decimal("0")}


def cr(account, amt):
    return {"account": account, "_dr": Decimal("0"), "_cr": amt}


# 1 -- disposal of the building. Book value and gain are DERIVED, not given.
bldg_book_value = BLDG_COST - BLDG_ACC_DEP          # 220,000 - 95,000
gain_on_sale = BLDG_PROCEEDS - bldg_book_value      # 140,000 - 125,000

je_1 = entry("a-1 (item 1: disposal of building)", [
    dr("Cash", BLDG_PROCEEDS),
    dr("Accumulated Depreciation - Building", BLDG_ACC_DEP),
    cr("Building", BLDG_COST),
    cr("Gain on Sale of Building", gain_on_sale),
])

# 2 -- bonds settled at face on maturity date, no gain/loss
je_2 = entry("a-2 (item 2: bond maturity settlement)", [
    dr("Bonds Payable", BONDS_FACE),
    cr("Cash", BONDS_FACE),
])

# 4 -- period-end interest accrual (no cash)
je_4 = entry("a-4 (item 4: period-end interest accrual)", [
    dr("Interest Expense", INTEREST_ACCRUED),
    cr("Interest Payable", INTEREST_ACCRUED),
])

# 5 -- equipment purchased for cash
je_5 = entry("a-5 (item 5: PPE purchase)", [
    dr("Equipment", EQUIP_PURCHASE),
    cr("Cash", EQUIP_PURCHASE),
])

# 7 -- long-term bank note issued for cash
je_7 = entry("a-7 (item 7: long-term note borrowing)", [
    dr("Cash", BANK_NOTE_PROCEEDS),
    cr("Notes Payable (long-term)", BANK_NOTE_PROCEEDS),
])

# 9 -- period-end dividend declaration (no cash)
je_9 = entry("a-9 (item 9: dividend declaration)", [
    dr("Retained Earnings", DIV_DECLARED),
    cr("Dividends Payable", DIV_DECLARED),
])

journal_entries = [je_1, je_2, je_4, je_5, je_7, je_9]


# ---------------------------------------------------------------------------
# Part b -- classification of each cash effect (drives part c arithmetic)
# ---------------------------------------------------------------------------
# (item label, section, signed cash effect)
CASH_ITEMS = [
    ("1", "I", BLDG_PROCEEDS),                 # inflow  - proceeds from sale of PPE
    ("2", "F", -BONDS_FACE),                   # outflow - repayment of debt principal
    ("3", "O", -INTEREST_PAID),                # outflow - interest paid
    ("5", "I", -EQUIP_PURCHASE),               # outflow - purchase of PPE
    ("7", "F", BANK_NOTE_PROCEEDS),            # inflow  - nontrade borrowing
    ("8", "F", -LEASE_PRINCIPAL),              # outflow - finance lease principal
    ("10", "F", -DIV_PAID),                    # outflow - dividends paid in cash
    ("11a", "O", COLLECTIONS),                 # inflow  - collections from customers
    ("11b", "O", -PAID_SUPPLIERS_EMPLOYEES),   # outflow - suppliers and employees
    ("11c", "O", -TAXES_PAID),                 # outflow - income taxes paid
    ("12", "O", -TRADING_PURCHASE),            # outflow - trading securities purchase
]

CLASSIFICATION_TEXT = {
    "1": "I - inflow $140,000 (proceeds from sale of building; reported gross)",
    "2": "F - outflow $80,000 (repayment of bond principal at maturity)",
    "3": "O - outflow $9,600 (interest paid)",
    "5": "I - outflow $55,000 (purchase of production equipment)",
    "7": "F - inflow $50,000 (proceeds from long-term nontrade bank note)",
    "8": "F - outflow $12,000 (finance lease principal; lease interest would be O)",
    "10": "F - outflow $7,500 (cash dividends paid)",
    "11": "O - inflow $285,000 collections; O - outflow $240,000 suppliers/employees; "
          "O - outflow $14,000 income taxes",
    "12": "O - outflow $16,000 (trading securities bought for resale are operating, "
          "not investing)",
}

NONCASH_TEXT = {
    "4": "Item 4 (accrued $2,400 interest): no cash effect, so it is NOT a cash flow "
         "line. Under the indirect method it appears only as a reconciling add-back "
         "(increase in interest payable) within operating activities; under the direct "
         "method it does not appear at all.",
    "6": "Item 6 (land acquired for a $90,000 note): noncash investing and financing "
         "transaction. Excluded from the body of the SCF; disclosed in the supplemental "
         "schedule of noncash investing and financing activities.",
    "9": "Item 9 (declared $10,000 dividends payable in Jan 2028): no cash effect, so it "
         "is NOT reported in financing activities this year. It is a noncash declaration "
         "(disclosed / reflected as an increase in dividends payable); the cash outflow "
         "will be a financing outflow in 2028 when paid.",
}


def section_total(code):
    total = Decimal("0")
    for _, sec, amt in CASH_ITEMS:
        if sec == code:
            total += amt
    return total


operating = section_total("O")
investing = section_total("I")
financing = section_total("F")

# ---------------------------------------------------------------------------
# Part c -- ending cash total, section totals, net change, beginning cash
# ---------------------------------------------------------------------------
ending_cash = CASH_IN_BANK + CASH_EQUIVALENTS + RESTRICTED_CASH  # ST equities excluded
net_change = operating + investing + financing
beginning_cash = ending_cash - net_change

# Internal consistency check (not reported): reconciliation must close.
assert r(beginning_cash + net_change) == r(ending_cash)

# ---------------------------------------------------------------------------
# Part d -- presentation order and three-line reconciliation (narrative)
# ---------------------------------------------------------------------------
PRESENTATION = (
    "SCF section order: (1) Cash flows from operating activities; "
    "(2) Cash flows from investing activities; (3) Cash flows from financing "
    "activities; then net increase (decrease) in cash, cash equivalents, and "
    "restricted cash; plus cash, cash equivalents, and restricted cash at January 1, "
    "2027; equals cash, cash equivalents, and restricted cash at December 31, 2027. "
    "Supplemental disclosures follow: noncash investing and financing activities "
    "(land acquired by issuing a $90,000 note) and, under the indirect method, "
    "interest paid and income taxes paid. Three-line reconciliation: net change "
    "$%s + beginning $%s = ending $%s."
) % (f"{r(net_change):,}", f"{r(beginning_cash):,}", f"{r(ending_cash):,}")

# ---------------------------------------------------------------------------
# Part e -- true/false with correction
# ---------------------------------------------------------------------------
PART_E = (
    "False. Investing (and financing) cash flows must generally be reported GROSS - "
    "cash receipts and cash payments are shown separately (ASC 230-10-45-26), e.g. "
    "proceeds from the sale of the building ($140,000) shown apart from the purchase "
    "of equipment ($55,000), not netted to $85,000 on one line. The only exception "
    "(ASC 230-10-45-8/45-9) is net reporting for items with quick turnover, large "
    "amounts, and original maturities of three months or less - certain investments "
    "other than cash equivalents, loans receivable, and debt (e.g. a revolving line of "
    "credit) - which does not cover purchases and sales of PPE."
)

# ---------------------------------------------------------------------------
# Output -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = []

# Part b: classifications
for key in ["1", "2", "3", "5", "7", "8", "10", "11", "12"]:
    answers.append({"label": f"b: cash-effect classification of item {key}",
                    "value": CLASSIFICATION_TEXT[key]})
for key in ["4", "6", "9"]:
    answers.append({"label": f"b: SCF reporting of item {key}",
                    "value": NONCASH_TEXT[key]})

# Part c: the six required figures
answers.extend([
    {"label": "c: ending cash total on the SCF reconciliation "
              "(cash + cash equivalents + restricted cash, Dec 31 2027)",
     "value": out(ending_cash)},
    {"label": "c: net cash provided by operating activities", "value": out(operating)},
    {"label": "c: net cash provided by investing activities", "value": out(investing)},
    {"label": "c: net cash used by financing activities", "value": out(financing)},
    {"label": "c: net change in cash", "value": out(net_change)},
    {"label": "c: beginning cash (Jan 1, 2027), solved", "value": out(beginning_cash)},
])

# Part d: presentation order and three-line reconciliation
answers.append({"label": "d: SCF section order and three-line cash reconciliation",
                "value": PRESENTATION})

# Part e: true/false with correction
answers.append({"label": "e: True/False with correction", "value": PART_E})

result = {
    "id": "agent_295#02",
    "rounding_convention": (
        "ROUND_HALF_UP to whole cents (Decimal.quantize) applied to each reported "
        "figure; all inputs are whole dollars so no rounding is triggered. No PV "
        "factors needed for this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Trading securities (item 12) are an operating outflow per ASC 230-10-45-18 "
        "and Ch. 22; restricted cash is included in the SCF cash total per "
        "ASC 230-10-45-24, while the $19,000 short-term equity investments (not cash "
        "equivalents) are excluded. Items 4 and 9 are period-end accruals with no cash "
        "movement and item 6 is a noncash exchange, so none of the three enters any "
        "cash-flow section."
    ),
}

print(json.dumps(result, indent=2))
