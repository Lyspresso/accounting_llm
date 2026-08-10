#!/usr/bin/env python3
"""
Blind solver for item agent_309#01 — Harborline Merchants / Dunecrest Packaging
note receivable: initial recognition, DCF impairment, effective-interest
accretion of the allowance, and settlement.

FACT PATTERN (from stem.md only)
--------------------------------
Jan 1, Y1  Harborline sells inventory to Dunecrest, takes a 4-year, 6%,
           $80,000 note issued at face (market rate 6%, so no premium/discount).
           Interest of $4,800 due each Dec 31; principal due Dec 31, Y4.
Dec 31, Y1 Y1 interest collected on schedule.  After collection, Harborline
           expects NO further interest and only $54,000 of principal, still on
           the original due date of Dec 31, Y4.  Current market rate is 12% but
           the stem says to ignore it for discounting (ASC 326-20-30-4 requires
           the note's ORIGINAL effective rate, 6%).  Stem supplies PV = $45,339.
Dec 31, Y4 Exactly $54,000 collected.

METHOD
------
* Because the note was issued at face with market = stated = 6%, its amortized
  cost basis at Dec 31, Y1 (after the Y1 interest receipt) is the $80,000 face.
  No interest receivable is outstanding at the impairment date, so — unlike the
  textbook demo where an uncollected accrual is reversed — the whole impairment
  loss is measured on principal alone.
* Impairment loss = amortized cost basis - PV of expected cash flows
                  = 80,000 - 45,339 = 34,661, credited to Allowance for
  Doubtful Accounts (net CA is reduced via the allowance, face stays $80,000).
* Subsequent measurement: the net carrying amount accretes to the expected
  $54,000 at the original 6% effective rate.  Each period's accretion is
  DEBITED to Allowance for Doubtful Accounts and CREDITED to Interest Revenue,
  so AFDA = 80,000 - net CA at every date.
* Settlement at Dec 31, Y4 is presented as one combined entry that folds in the
  final Y4 accretion, per Required part (e).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to whole dollars, applied PER PERIOD (each year's effective-
interest accretion is rounded to the dollar before it is added to the net
carrying amount; the rounded balance is the base for the next period).  This is
the course convention and it is self-proving here: 45,339 -> 48,059 -> 50,943
-> 54,000 lands exactly on the expected $54,000 with no plug.

The present value itself is the $45,339 the stem instructs us to use.  The
script independently cross-checks it two ways (exact 54,000 / 1.06**3 and the
5-decimal PV table factor 0.83962 for n=3, i=6%); both round HALF_UP to the
same $45,339.  All money is decimal.Decimal — no floats anywhere.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 40

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d(x: str | int) -> Decimal:
    return Decimal(str(x))


def dollars(x: Decimal) -> Decimal:
    """ROUND_HALF_UP to the whole dollar (this course's convention)."""
    return x.quantize(DOLLAR, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly: emit an int when the value is whole, else a float-free str."""
    if x == x.to_integral_value():
        return int(x)
    return float(x)  # never reached for this item; money here is whole dollars


# ---------------------------------------------------------------- given facts
FACE = d(80000)              # note face / amortized cost basis at issuance
STATED = d("0.06")           # stated rate = market rate at issuance
EFFECTIVE = STATED           # ASC 326: discount at the ORIGINAL effective rate
ANNUAL_INTEREST = d(4800)    # 80,000 x 6%, stated in the stem
EXPECTED_PRINCIPAL = d(54000)
YEARS_TO_COLLECTION = 3      # Dec 31 Y1 -> Dec 31 Y4
PV_GIVEN = d(45339)          # stem: "use PV = $45,339"
MARKET_RATE_NOW = d("0.12")  # stem says explicitly to IGNORE for discounting

# ------------------------------------------------- cross-check the given PV
one_plus_i = Decimal(1) + EFFECTIVE
pv_exact = dollars(EXPECTED_PRINCIPAL / (one_plus_i ** YEARS_TO_COLLECTION))
TABLE_FACTOR_N3_I6 = d("0.83962")  # PV of $1, n=3, i=6%
pv_table = dollars(EXPECTED_PRINCIPAL * TABLE_FACTOR_N3_I6)
pv_checks_agree = (pv_exact == PV_GIVEN) and (pv_table == PV_GIVEN)

PV = PV_GIVEN

# ------------------------------------------------------ (b) impairment loss
# Interest through Dec 31, Y1 was collected in cash, so there is no interest
# receivable to write off.  Basis is the $80,000 face.
IMPAIRMENT_LOSS = FACE - PV                      # 80,000 - 45,339 = 34,661
AFDA_AT_IMPAIRMENT = IMPAIRMENT_LOSS             # allowance established

# --------------------------- (c) subsequent measurement schedule, Y1 -> Y4
schedule = []
net_ca = PV
afda = FACE - net_ca
schedule.append(
    {
        "date": "Dec 31, Year 1 (after impairment)",
        "accretion": 0,
        "net_carrying_amount": num(net_ca),
        "afda": num(afda),
    }
)

accretion_by_year = {}
for yr in (2, 3, 4):
    accretion = dollars(net_ca * EFFECTIVE)      # round PER PERIOD
    accretion_by_year[yr] = accretion
    net_ca = net_ca + accretion
    afda = FACE - net_ca
    label = "Dec 31, Year %d" % yr
    if yr == 4:
        label += " (before settlement)"
    schedule.append(
        {
            "date": label,
            "accretion": num(accretion),
            "net_carrying_amount": num(net_ca),
            "afda": num(afda),
        }
    )

# The schedule must land exactly on the expected cash flow with no plug.
assert net_ca == EXPECTED_PRINCIPAL, (net_ca, EXPECTED_PRINCIPAL)
assert afda == FACE - EXPECTED_PRINCIPAL

Y2_ACCRETION = accretion_by_year[2]
Y3_ACCRETION = accretion_by_year[3]
Y4_ACCRETION = accretion_by_year[4]

# AFDA balance carried into the settlement entry, BEFORE the Y4 accretion.
AFDA_BEFORE_Y4_ACCRETION = FACE - (EXPECTED_PRINCIPAL - Y4_ACCRETION)

# --------------------------------------------------------- journal entries
def line(account, debit=Decimal(0), credit=Decimal(0)):
    return {"account": account, "debit": num(d(debit)), "credit": num(d(credit))}


journal_entries = [
    {
        "part": "a",
        "date": "Jan 1, Year 1",
        "description": "Receipt of note in exchange for merchandise (cost of goods sold entry not given)",
        "lines": [
            line("Note Receivable", debit=FACE),
            line("Sales Revenue", credit=FACE),
        ],
    },
    {
        "part": "a",
        "date": "Dec 31, Year 1",
        "description": "Collection of Year 1 interest ($80,000 x 6%)",
        "lines": [
            line("Cash", debit=ANNUAL_INTEREST),
            line("Interest Revenue", credit=ANNUAL_INTEREST),
        ],
    },
    {
        "part": "b",
        "date": "Dec 31, Year 1",
        "description": (
            "Impairment AJE: amortized cost $80,000 less PV of expected cash flows "
            "$45,339 discounted at the original 6% effective rate"
        ),
        "lines": [
            line("Bad Debt Expense", debit=IMPAIRMENT_LOSS),
            line("Allowance for Doubtful Accounts", credit=AFDA_AT_IMPAIRMENT),
        ],
    },
    {
        "part": "d",
        "date": "Dec 31, Year 2",
        "description": "Effective-interest accretion ($45,339 x 6%)",
        "lines": [
            line("Allowance for Doubtful Accounts", debit=Y2_ACCRETION),
            line("Interest Revenue", credit=Y2_ACCRETION),
        ],
    },
    {
        "part": "d",
        "date": "Dec 31, Year 3",
        "description": "Effective-interest accretion ($48,059 x 6%)",
        "lines": [
            line("Allowance for Doubtful Accounts", debit=Y3_ACCRETION),
            line("Interest Revenue", credit=Y3_ACCRETION),
        ],
    },
    {
        "part": "e",
        "date": "Dec 31, Year 4",
        "description": (
            "Combined settlement: final accretion ($50,943 x 6% = $3,057) plus "
            "derecognition of the note on collection of $54,000"
        ),
        "lines": [
            line("Cash", debit=EXPECTED_PRINCIPAL),
            line("Allowance for Doubtful Accounts", debit=AFDA_BEFORE_Y4_ACCRETION),
            line("Note Receivable", credit=FACE),
            line("Interest Revenue", credit=Y4_ACCRETION),
        ],
    },
]

for je in journal_entries:
    dr = sum(d(l["debit"]) for l in je["lines"])
    cr = sum(d(l["credit"]) for l in je["lines"])
    assert dr == cr, (je["part"], je["date"], dr, cr)

# --------------------------------------------------------------- answers
answers = [
    {"label": "b: impairment loss (bad debt expense) at Dec 31, Y1",
     "value": num(IMPAIRMENT_LOSS)},
    {"label": "c: net carrying amount, Dec 31, Y1 (after impairment)",
     "value": num(d(schedule[0]["net_carrying_amount"]))},
    {"label": "c: AFDA balance, Dec 31, Y1 (after impairment)",
     "value": num(d(schedule[0]["afda"]))},
    {"label": "c: net carrying amount, Dec 31, Y2",
     "value": num(d(schedule[1]["net_carrying_amount"]))},
    {"label": "c: AFDA balance, Dec 31, Y2",
     "value": num(d(schedule[1]["afda"]))},
    {"label": "c: net carrying amount, Dec 31, Y3",
     "value": num(d(schedule[2]["net_carrying_amount"]))},
    {"label": "c: AFDA balance, Dec 31, Y3",
     "value": num(d(schedule[2]["afda"]))},
    {"label": "c: net carrying amount, Dec 31, Y4 before settlement",
     "value": num(d(schedule[3]["net_carrying_amount"]))},
    {"label": "c: AFDA balance, Dec 31, Y4 before settlement",
     "value": num(d(schedule[3]["afda"]))},
]

notes = (
    "Discounted at the original 6% effective rate; the 12% current market rate is "
    "ignored per ASC 326-20-30-4 and per the stem. Interest through Dec 31, Y1 was "
    "collected in cash, so no interest receivable is written off in the impairment "
    "entry and the loss is the full $80,000 - $45,339. Accretion is recorded against "
    "the allowance (face stays $80,000): "
    f"Y2 ${Y2_ACCRETION}, Y3 ${Y3_ACCRETION}, Y4 ${Y4_ACCRETION}; "
    "the schedule closes exactly on the $54,000 expected collection. PV cross-check "
    "(exact 54,000/1.06^3 and table factor 0.83962) agrees with the given $45,339: "
    f"{str(pv_checks_agree).lower()}. "
    "The part (c) schedule rows are in the top-level 'schedule' field."
)

out = {
    "id": "agent_309#01",
    "rounding_convention": (
        "ROUND_HALF_UP to whole dollars, applied per period: each year's "
        "effective-interest accretion is rounded before it updates the net carrying "
        "amount. PV is the $45,339 the stem directs us to use (cross-checked against "
        "both the exact 6% formula and the 5-decimal PV table factor 0.83962)."
    ),
    "answers": answers,
    "schedule": schedule,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
