"""Solver for agent_164#02 - SCF edge classifications, period-end cash, gross presentation.

Rounding convention: decimal.Decimal throughout; ROUND_HALF_UP applied once per
period to cents (2 dp). No floats anywhere. Every figure derived from the inputs
stated in the question; nothing hard-coded as an answer.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")
def r(x):
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)
def m(x):
    return str(r(x))

# ---------- Part A: edge classifications ----------
partA = [
    ("1. Principal payment on finance lease liability",
     "F outflow", "Lease principal repays a borrowing-type liability -> financing outflow."),
    ("2. Cash purchase of trading equity securities (short-term resale profits)",
     "O outflow", "Trading securities bought for short-term resale -> operating outflow."),
    ("3. Cash proceeds from sale of those same trading securities",
     "O inflow", "Sale of trading securities -> operating inflow (same section as the purchase)."),
    ("4. Cash purchase of available-for-sale debt securities held for long-term yield",
     "I outflow", "Non-trading investment purchase -> investing outflow."),
    ("5. Collection of principal on a short-term TRADE note receivable (from inventory sale)",
     "O inflow", "Trade receivable/note from selling inventory -> operating inflow."),
    ("6. Collection of interest on that same trade note",
     "O inflow", "Interest received is operating under GAAP."),
    ("7. Cash paid for early extinguishment of long-term bonds (principal + cash premium)",
     "F outflow", "Retirement of debt principal (and premium, per this LO) -> financing outflow."),
    ("8. Cash proceeds from sale of a patent",
     "I inflow", "Disposal of a long-lived (intangible) asset -> investing inflow."),
    ("9. Cash from issuance of a short-term NONTRADE note payable for general financing",
     "F inflow", "Nontrade borrowing, regardless of term -> financing inflow."),
    ("10. Payment of cash dividend declared in the prior year",
     "F outflow", "Dividends paid to owners -> financing outflow."),
]

# ---------- Part B: period-end cash total and beginning cash ----------
cash_in_bank      = Decimal("48000")
cash_equivalents  = Decimal("12000")
restricted_cash   = Decimal("5000")
afs_equity_st     = Decimal("22000")   # NOT cash / not a cash equivalent -> excluded

ending_cash_total = cash_in_bank + cash_equivalents + restricted_cash

net_operating = Decimal("90000")
net_investing = Decimal("-70000")
net_financing = Decimal("-15000")
net_change    = net_operating + net_investing + net_financing
beginning_cash = ending_cash_total - net_change

# ---------- Part C: JEs ----------
patent_bv        = Decimal("18000")
patent_proceeds  = Decimal("22500")
gain_on_patent   = patent_proceeds - patent_bv
lease_principal  = Decimal("9000")

je_patent = {
    "part": "c",
    "description": "Sale of patent (book value $18,000) for $22,500 cash - SCF: INVESTING INFLOW $22,500 (full proceeds); gain deducted from net income in the operating section under the indirect method.",
    "lines": [
        {"account": "Cash", "debit": m(patent_proceeds), "credit": m(0)},
        {"account": "Patent", "debit": m(0), "credit": m(patent_bv)},
        {"account": "Gain on Sale of Patent", "debit": m(0), "credit": m(gain_on_patent)},
    ],
}
je_lease = {
    "part": "c",
    "description": "Cash principal payment on finance lease liability - SCF: FINANCING OUTFLOW $9,000 (interest portion paid separately is operating).",
    "lines": [
        {"account": "Lease Liability (finance lease)", "debit": m(lease_principal), "credit": m(0)},
        {"account": "Cash", "debit": m(0), "credit": m(lease_principal)},
    ],
}
for je in (je_patent, je_lease):
    dr = sum(Decimal(l["debit"]) for l in je["lines"])
    cr = sum(Decimal(l["credit"]) for l in je["lines"])
    assert dr == cr, (je["part"], dr, cr)

# ---------- Part D ----------
partD = ("FALSE. Investing (and financing) cash flows must be reported GROSS on the face of the "
         "statement: gross cash receipts (e.g., proceeds from sales of equipment) and gross cash "
         "payments (e.g., purchases of equipment) are shown as separate line items; they may not be "
         "netted against each other merely to simplify the statement. (Net reporting is allowed only "
         "in the narrow exception for items with quick turnover, large amounts, and short maturities, "
         "such as demand-loan or commercial-paper activity.)")

# ---------- Part E ----------
partE = ["1. Operating activities",
         "2. Investing activities",
         "3. Financing activities",
         "4. Net increase (decrease) in cash, cash equivalents, and restricted cash",
         "5. Cash, cash equivalents, and restricted cash - beginning of period",
         "6. Cash, cash equivalents, and restricted cash - end of period",
         "7. Supplemental disclosure of noncash investing and financing activities"]

answers = []
for label, cls, why in partA:
    answers.append({"label": "a: " + label, "value": cls, "note": why})

answers += [
    {"label": "b: Cash in bank (unrestricted) included in period-end cash total", "value": m(cash_in_bank)},
    {"label": "b: Money-market cash equivalents included", "value": m(cash_equivalents)},
    {"label": "b: Restricted cash included (ASU 2016-18 requires inclusion)", "value": m(restricted_cash)},
    {"label": "b: Short-term AFS equity investments EXCLUDED (not a cash equivalent)", "value": m(afs_equity_st)},
    {"label": "b: Ending cash, cash equivalents, and restricted cash (SCF reconciliation total)", "value": m(ending_cash_total)},
    {"label": "b: Net cash provided by operating activities", "value": m(net_operating)},
    {"label": "b: Net cash used by investing activities", "value": m(net_investing)},
    {"label": "b: Net cash used by financing activities", "value": m(net_financing)},
    {"label": "b: Net increase in cash, cash equivalents, and restricted cash", "value": m(net_change)},
    {"label": "b: Beginning cash, cash equivalents, and restricted cash (solved)", "value": m(beginning_cash)},
    {"label": "c: Patent sale - Dr Cash", "value": m(patent_proceeds)},
    {"label": "c: Patent sale - Cr Patent (book value removed)", "value": m(patent_bv)},
    {"label": "c: Patent sale - Cr Gain on Sale of Patent", "value": m(gain_on_patent)},
    {"label": "c: Patent sale - SCF section", "value": "Investing inflow $22,500.00 (gain of $4,500.00 subtracted from net income in operating under the indirect method)"},
    {"label": "c: Finance lease principal payment - Dr Lease Liability", "value": m(lease_principal)},
    {"label": "c: Finance lease principal payment - Cr Cash", "value": m(lease_principal)},
    {"label": "c: Finance lease principal payment - SCF section", "value": "Financing outflow $9,000.00 (interest paid is reported as operating)"},
    {"label": "d: True/False with correction", "value": partD},
    {"label": "e: Required section order on the face of the SCF", "value": " | ".join(partE)},
]

out = {
    "id": "agent_164#02",
    "rounding_convention": "decimal.Decimal for all money; ROUND_HALF_UP to 2 decimal places, applied once per period. No floats.",
    "answers": answers,
    "journal_entries": [je_patent, je_lease],
    "insufficient_info": False,
    "notes": ("Part A: trading securities bought for short-term resale profit are operating (both purchase and sale); "
              "AFS/held-for-yield investments are investing; trade notes receivable arising from inventory sales are "
              "operating for BOTH principal and interest, while a nontrade note payable is financing; interest "
              "received/paid is operating under US GAAP; finance-lease PRINCIPAL is financing. "
              "Part B: under ASU 2016-18 restricted cash is included in the SCF total, so ending total = "
              "48,000 + 12,000 + 5,000 = 65,000; short-term AFS equity securities of 22,000 are excluded. "
              "Net change = 90,000 - 70,000 - 15,000 = +5,000, so beginning cash = 65,000 - 5,000 = 60,000. "
              "Part C: gain on patent = 22,500 - 18,000 = 4,500; the FULL 22,500 proceeds go in investing. "
              "Part D: gross presentation is required for investing and financing.")
}
print(json.dumps(out, indent=1))
