#!/usr/bin/env python3
"""
Blind solver — agent_283#02
Ironclad Components Corp. / Harbor Trust Leasing: recognized sale-leaseback with
an OPERATING leaseback and lease payments in ADVANCE (annuity due).

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal. No floats anywhere in the money path.
* ROUND_HALF_UP, per period, to the cent ($0.01).
  - The commencement PV is computed from the exact annuity-due formula
      PVAD = PMT * ((1 - (1+i)^-n) / i) * (1 + i)
    carried at 12 significant decimals and then rounded ONCE to the cent.
    (The 5-decimal textbook table factor for PVAD n=8, i=8% is 6.20637, which
    gives the identical cent: 45,000 x 6.20637 = 279,286.65.)
  - Interest for each period is then computed on the ROUNDED beginning-of-period
    liability balance and rounded to the cent BEFORE it is posted
    (round-per-period, not round-at-end). Balances therefore roll forward from
    rounded numbers, exactly as a hand-prepared amortization schedule would.
  - Straight-line lease expense = (total payments + IDC - incentives) / n, and
    the ROU-asset reduction is the PLUG (lease expense less interest), which is
    what keeps the schedule self-clearing to exactly zero at the end of term.
* Percentages are rounded HALF_UP to 2 decimal places, expressed as percent.

MODEL / AUTHORITY (ASC 842; course text ch. 17, LO 17-12)
--------------------------------------------------------
Leaseback classification (seller-lessee) — none of the five finance-lease
criteria is met, so the leaseback is an OPERATING lease; because the leaseback
is operating, control transferred and the transfer IS a recognized sale
(a finance leaseback would have made it a "failed sale"/financing).
Seller-lessee therefore: derecognizes the building, recognizes the full gain,
and books an ordinary operating-lease ROU asset and lease liability.

Operating lease with payments in advance means the December 31 entry is a pure
adjusting entry with NO cash: cash moved on January 1 instead.

Run:  python3 solver.py      (prints one JSON object on stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 40

CENT = Decimal("0.01")
PCT = Decimal("0.01")


def money(x):
    """ROUND_HALF_UP to the cent."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def pct(x):
    return Decimal(x).quantize(PCT, rounding=ROUND_HALF_UP)


def num(d):
    """JSON-friendly: int when the cents are zero, else float of the exact cent."""
    d = Decimal(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- fact pattern
SALE_PRICE = Decimal("320000")        # cash selling price = fair value
FAIR_VALUE = Decimal("320000")
COST = Decimal("700000")              # building cost
ACC_DEP = Decimal("430000")           # accumulated depreciation
CARRYING = COST - ACC_DEP             # 270,000 (agrees with the stem)
USEFUL_LIFE = 25                      # remaining useful life, years
TERM = 8                              # lease term, years
PMT = Decimal("45000")                # annual payment, due January 1 (annuity due)
RATE = Decimal("0.08")                # implicit rate, known to lessee
IDC = Decimal("0")                    # no initial direct costs
INCENTIVES = Decimal("0")             # no lease incentives

assert CARRYING == Decimal("270000"), "carrying amount does not tie to the stem"


# ------------------------------------------------------- (a) classification
def pv_annuity_due(pmt, rate, n):
    """PMT * PVOA(n, i) * (1 + i)  -- payments at the BEGINNING of each period."""
    one = Decimal(1)
    disc = (one + rate) ** n
    pvoa_factor = (one - one / disc) / rate
    pvad_factor = pvoa_factor * (one + rate)
    return pmt * pvad_factor, pvad_factor


pv_exact, pvad_factor = pv_annuity_due(PMT, RATE, TERM)
PV = money(pv_exact)                                   # ROU / liability at commencement

term_pct = pct(Decimal(TERM) / Decimal(USEFUL_LIFE) * 100)         # 32.00%
pv_threshold = money(FAIR_VALUE * Decimal("0.90"))                 # 288,000 (90% of FV)
pv_pct_of_fv = pct(PV / FAIR_VALUE * 100)                          # 87.28%

criteria = {
    "1_transfer_of_ownership": False,          # stem: no title transfer
    "2_purchase_option": False,                # stem: no purchase option
    "3_major_part_of_life": term_pct >= Decimal("75"),   # 32% -> False
    "4_pv_substantially_all_fv": PV >= pv_threshold,     # 279,286.65 < 288,000 -> False
    "5_specialized_no_alt_use": False,         # stem: alternative use at end = yes
}
is_operating = not any(criteria.values())
recognized_sale = is_operating              # operating leaseback => sale is recognized
assert is_operating and recognized_sale

GAIN = money(SALE_PRICE - CARRYING)         # 50,000


# --------------------------------------------- (d)(e)(f) operating-lease schedule
# Straight-line lease expense per the course handout:
#   Lease Expense = [(payment x #payments) + IDC - incentives] / #payments
LEASE_EXPENSE = money((PMT * TERM + IDC - INCENTIVES) / Decimal(TERM))   # 45,000

# Payments are in ADVANCE, so the sequence inside each lease year is:
#   Jan 1  -> pay (liability down by the full payment; no interest yet)
#   Dec 31 -> adjusting entry only, NO cash:
#             Dr Lease Expense / Cr Lease Liability (interest accrued)
#                              / Cr Right-of-Use Asset (plug)
liab = PV
rou = PV
schedule = []
for year in range(1, TERM + 1):
    liab_before_pmt = liab
    liab_after_pmt = liab_before_pmt - PMT                 # January 1 payment
    interest = money(liab_after_pmt * RATE)                # accrues over the year
    rou_change = money(LEASE_EXPENSE - interest)           # plug
    liab_end = money(liab_after_pmt + interest)            # after Dec 31 adjusting JE
    rou_end = money(rou - rou_change)
    schedule.append({
        "year": year,
        "jan1_payment": PMT,
        "liability_after_payment": money(liab_after_pmt),
        "lease_expense": LEASE_EXPENSE,
        "interest_on_liability": interest,
        "rou_asset_change": rou_change,
        "liability_end": liab_end,
        "rou_end": rou_end,
    })
    liab, rou = liab_end, rou_end

# Self-clearing check: both must land exactly on zero at the end of the term.
assert liab == Decimal("0.00"), f"lease liability did not clear: {liab}"
assert rou == Decimal("0.00"), f"ROU asset did not clear: {rou}"

y1, y2, y3 = schedule[0], schedule[1], schedule[2]
y8 = schedule[7]


# ------------------------------------------------------------- journal entries
def line(acct, dr=None, cr=None):
    return {"account": acct,
            "debit": num(dr) if dr is not None else 0,
            "credit": num(cr) if cr is not None else 0}


journal_entries = [
    # (c)(1) January 1, Year 1 — record the sale of the building
    {"part": "c", "date": "January 1, Year 1", "description": "Sale of building",
     "lines": [
         line("Cash", dr=SALE_PRICE),
         line("Accumulated Depreciation - Buildings", dr=ACC_DEP),
         line("Buildings", cr=COST),
         line("Gain on Sale-Leaseback", cr=GAIN),
     ]},
    # (c)(2) January 1, Year 1 — record ROU asset and lease liability (before payment)
    {"part": "c", "date": "January 1, Year 1",
     "description": "Right-of-use asset and lease liability at commencement",
     "lines": [
         line("Right-of-Use Asset", dr=PV),
         line("Lease Liability", cr=PV),
     ]},
    # (c)(3) January 1, Year 1 — first lease payment (annuity due)
    {"part": "c", "date": "January 1, Year 1", "description": "First lease payment",
     "lines": [
         line("Lease Liability", dr=PMT),
         line("Cash", cr=PMT),
     ]},
    # (d) December 31, Year 1 — period-end adjusting entry only, no cash
    {"part": "d", "date": "December 31, Year 1",
     "description": "Period-end adjusting entry (no cash)",
     "lines": [
         line("Lease Expense", dr=LEASE_EXPENSE),
         line("Lease Liability", cr=y1["interest_on_liability"]),
         line("Right-of-Use Asset", cr=y1["rou_asset_change"]),
     ]},
    # (f)(1) January 1, Year 8 — eighth and final lease payment
    {"part": "f", "date": "January 1, Year 8", "description": "Final lease payment",
     "lines": [
         line("Lease Liability", dr=PMT),
         line("Cash", cr=PMT),
     ]},
    # (f)(2) December 31, Year 8 — final adjusting entry; liability already zero,
    #        so there is no interest and the whole expense reduces the ROU asset.
    {"part": "f", "date": "December 31, Year 8",
     "description": "Final period-end adjusting entry; clears ROU asset and liability",
     "lines": [
         line("Lease Expense", dr=LEASE_EXPENSE),
         line("Right-of-Use Asset", cr=y8["rou_asset_change"]),
     ]},
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"unbalanced JE in part {je['part']}: {dr} vs {cr}"

assert y8["interest_on_liability"] == Decimal("0.00")
assert y8["rou_asset_change"] == LEASE_EXPENSE


# -------------------------------------------------------------------- answers
answers = [
    # a — the PV test inside the classification proof
    # (pv_pct_of_fv is computed and reported in `notes` only -- it is a
    #  presentational restatement of the same test, not a required figure.)
    {"label": "a: 90% of fair value (PV test threshold)", "value": num(pv_threshold)},

    # b — commencement PV of the annuity-due payments
    {"label": "b: commencement PV of lease payments (ROU asset = lease liability, "
              "before the first payment)", "value": num(PV)},

    # e — Years 1-3 roll-forward rows (after each December 31 adjusting entry)
    {"label": "e: Year 1 interest on lease liability",
     "value": num(y1["interest_on_liability"])},
    {"label": "e: Year 1 ROU asset reduction", "value": num(y1["rou_asset_change"])},
    {"label": "e: Year 1 ending lease liability (Dec 31, Year 1)",
     "value": num(y1["liability_end"])},
    {"label": "e: Year 1 ending ROU asset (Dec 31, Year 1)", "value": num(y1["rou_end"])},

    {"label": "e: Year 2 interest on lease liability",
     "value": num(y2["interest_on_liability"])},
    {"label": "e: Year 2 ROU asset reduction", "value": num(y2["rou_asset_change"])},
    {"label": "e: Year 2 ending lease liability (Dec 31, Year 2)",
     "value": num(y2["liability_end"])},
    {"label": "e: Year 2 ending ROU asset (Dec 31, Year 2)", "value": num(y2["rou_end"])},

    {"label": "e: Year 3 interest on lease liability",
     "value": num(y3["interest_on_liability"])},
    {"label": "e: Year 3 ROU asset reduction", "value": num(y3["rou_asset_change"])},
    {"label": "e: Year 3 ending lease liability (Dec 31, Year 3)",
     "value": num(y3["liability_end"])},
    {"label": "e: Year 3 ending ROU asset (Dec 31, Year 3)", "value": num(y3["rou_end"])},
]

notes = (
    "a. None of the five ASC 842 finance-lease criteria is met: no title transfer, "
    "no purchase option, lease term 8/25 = 32.00% (< 75% major part), PV of payments "
    f"${PV:,} < ${pv_threshold:,} (90% of the $320,000 fair value, i.e. "
    f"{pv_pct_of_fv}% of fair value), and the space has an alternative use. "
    "The leaseback is therefore an OPERATING lease, which means control passed to "
    "Harbor Trust and the transfer is a RECOGNIZED sale-leaseback (a finance "
    "leaseback would have been a failed sale). Ironclad derecognizes the building "
    "and recognizes the full $50,000 gain (320,000 sale price - 270,000 carrying "
    "amount). "
    "d. Because payments are in advance, cash moved on January 1, so the December 31 "
    "entry is purely an accrual: it debits the single straight-line Lease Expense of "
    "$45,000 and credits Lease Liability for the $18,742.93 of interest accrued on "
    "the post-payment balance plus Right-of-Use Asset for the $26,257.07 plug. It "
    "differs from an arrears (Q1-style) year-end package because there is no "
    "December 31 cash payment entry alongside it - the liability GROWS at year-end "
    "here instead of being paid down, and interest accrues on the balance net of a "
    "payment already made. "
    "f. After the January 1, Year 8 payment the liability is exactly $0, so the "
    "December 31, Year 8 adjusting entry carries no interest and the entire $45,000 "
    "of lease expense writes the remaining ROU asset off to zero. "
    "g. With a 20-year term (20/25 = 80%, a major part of the remaining economic "
    "life) the leaseback would be a FINANCE lease, so control would not transfer and "
    "the transaction would be a FAILED SALE: Ironclad would keep the building on its "
    "books at cost less accumulated depreciation and keep depreciating it over the "
    "25-year life, recognize NO gain, record the $320,000 proceeds as a financing "
    "liability (note payable), and split each $ payment between interest expense at "
    "8% and principal - no ROU asset, no lease liability, no single straight-line "
    "lease expense."
)

out = {
    "id": "agent_283#02",
    "rounding_convention": (
        "ROUND_HALF_UP per period to the cent; decimal.Decimal throughout. "
        "Commencement PV from the exact annuity-due formula PMT * PVOA(8, 8%) * 1.08 "
        "(= 6.206370 factor, identical to the 5-decimal table factor 6.20637), "
        "rounded once to the cent. Interest each period computed on the rounded "
        "beginning balance and rounded before posting; ROU-asset reduction is the "
        "plug (straight-line lease expense less interest). Percentages HALF_UP to 2dp."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=1))
