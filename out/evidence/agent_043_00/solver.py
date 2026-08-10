#!/usr/bin/env python3
"""
Solver for item agent_043#00 - Cascade Outfitters Co.
Zero-interest (0% stated / 10% market) three-year noncurrent note receivable
received on June 30, Year 1 for inventory with fair value $11,269; face $15,000
due in a single payment June 30, Year 4. (LO 8-5, effective-interest method.)

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. No floats anywhere.

1. Presentation currency unit: WHOLE DOLLARS. The stem states the present value
   as an exact whole dollar amount ($11,269 = 15,000 / 1.10^3 rounded), and the
   course text (Chapter 8, Demo 8-5C - the structurally identical 3-year 0%/10%
   note) presents the amortization schedule in whole dollars. Every period
   amount is therefore quantized to Decimal("1").

2. ROUND_HALF_UP, applied PER PERIOD (not round-at-end). Each year's interest
   revenue is computed as (carrying amount at start of that year) x 10% and
   immediately rounded half-up to whole dollars; the rounded amount is what
   rolls into the next period's carrying amount. Interest is compounded on the
   rounded carrying amount, matching the text's schedule.

3. FINAL-PERIOD PLUG. The last period's interest revenue / discount
   amortization is the plug that forces the ending carrying amount to equal the
   $15,000 face value, so total interest revenue exactly equals the initial
   discount. (Text does the same: 601 + 661 + 727 = 1,989 with 727 as a plug.)

4. INTERIM (Dec 31) ALLOCATION. Amounts are not re-derived at a new effective
   rate; the note-year amounts from the schedule are ALLOCATED to reporting
   periods 6 months / 6 months, per the text: the first half is ROUND_HALF_UP of
   (annual amount / 2) and the second half is the remainder, so the two halves
   always re-sum to the annual figure exactly (text: 601 -> 301 + 300).

5. Present value / initial measurement is the stem's clearly determinable fair
   value of the inventory exchanged, $11,269, which the stem states equals the
   PV of the note. Note: the exact formula gives 15,000 / 1.10^3 = 11,269.7220,
   which would round half-up to $11,270; the stem presents the truncated
   $11,269. The fair value of the consideration given is the measurement basis
   in the fact pattern, so $11,269 is used, and the script asserts the exact PV
   is within $1 of it (confirming the 10% market rate) rather than trusting the
   stem blindly.

Cash interest is $0 in every period (stated rate = 0%), so discount
amortization equals interest revenue in every period.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 50

DOLLAR = Decimal("1")


def d(x):
    """Round to whole dollars, ROUND_HALF_UP."""
    return Decimal(x).quantize(DOLLAR, rounding=ROUND_HALF_UP)


def num(x):
    """Decimal -> JSON number (int when integral)."""
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- fact pattern
FACE = Decimal("15000")          # stated / maturity value, due June 30 Year 4
MARKET_RATE = Decimal("0.10")    # market rate for notes of similar risk
TERM_YEARS = 3
STATED_RATE = Decimal("0")       # noninterest-bearing
FV_INVENTORY = Decimal("11269")  # clearly determinable fair value given in stem

# Independently re-derive PV = FACE / (1 + i)^n as a consistency check on the
# 10% market rate. Exact value is 15,000 / 1.331 = 11,269.7220..., which the
# stem presents (truncated) as $11,269. The MEASUREMENT BASIS is the stem's
# clearly determinable fair value of the inventory exchanged, so $11,269 is the
# initial carrying amount; we only verify the stem's figure is within $1 of the
# exact PV, which confirms the 10% market rate.
pv_exact = FACE / ((Decimal("1") + MARKET_RATE) ** TERM_YEARS)
assert abs(pv_exact - FV_INVENTORY) <= Decimal("1"), (
    f"exact PV {pv_exact} inconsistent with stem fair value {FV_INVENTORY}"
)
pv = FV_INVENTORY

# ------------------------------------------------------- (a) initial discount
# Discount = excess of face value over present value.
discount_initial = FACE - pv

# ------------------------------- (b) effective-interest amortization schedule
# Columns: cash interest (stated), interest revenue (market), discount
# amortization, carrying amount. Note years run June 30 Yr N -> June 30 Yr N+1.
schedule = []
carrying = pv
for yr in range(1, TERM_YEARS + 1):
    cash_interest = d(FACE * STATED_RATE)          # 0 every year
    if yr == TERM_YEARS:
        # final-period plug: force carrying amount to face
        interest_revenue = FACE - carrying
    else:
        interest_revenue = d(carrying * MARKET_RATE)
    amortization = interest_revenue - cash_interest  # cash interest is 0
    carrying = carrying + amortization
    schedule.append(
        {
            "note_year": yr,
            "date": f"June 30, Year {yr + 1}",
            "cash_interest": cash_interest,
            "interest_revenue": interest_revenue,
            "discount_amortization": amortization,
            "carrying_amount": carrying,
        }
    )

assert schedule[-1]["carrying_amount"] == FACE, "schedule must end at face value"
total_interest = sum((r["interest_revenue"] for r in schedule), Decimal("0"))
assert total_interest == discount_initial, "total interest must equal discount"

# ----------------------- (d) allocation of each note year across Dec 31 periods
# Each note year (July 1 -> June 30) splits 6 months into the calendar year that
# contains its first half and 6 months into the next.
halves = []
for row in schedule:
    first = d(row["discount_amortization"] / Decimal("2"))
    second = row["discount_amortization"] - first
    halves.append((first, second))

# Note year 1 (6/30/Y1-6/30/Y2): 1st half -> Dec 31 Yr1, 2nd half -> Dec 31 Yr2
# Note year 2 (6/30/Y2-6/30/Y3): 1st half -> Dec 31 Yr2, 2nd half -> Dec 31 Yr3
# Note year 3 (6/30/Y3-6/30/Y4): 1st half -> Dec 31 Yr3, 2nd half -> June 30 Yr4
dec31_y1 = halves[0][0]
dec31_y2 = halves[0][1] + halves[1][0]
dec31_y3 = halves[1][1] + halves[2][0]
jun30_y4 = halves[2][1]

calendar_accruals = [
    ("December 31, Year 1", dec31_y1),
    ("December 31, Year 2", dec31_y2),
    ("December 31, Year 3", dec31_y3),
    ("June 30, Year 4", jun30_y4),
]
total_calendar = sum((amt for _, amt in calendar_accruals), Decimal("0"))
assert total_calendar == discount_initial, "allocated interest must equal discount"

# ------------- (e) December 31, Year 1 balance sheet carrying amount / class'n
discount_unamortized_1231_y1 = discount_initial - dec31_y1
net_note_1231_y1 = FACE - discount_unamortized_1231_y1
# Maturity June 30, Year 4 is more than one year after December 31, Year 1.
classification = "noncurrent"

# ------------------------------------------------------------ journal entries
journal_entries = []


def entry(part, date, memo, lines):
    dr = sum((Decimal(str(l["debit"])) for l in lines), Decimal("0"))
    cr = sum((Decimal(str(l["credit"])) for l in lines), Decimal("0"))
    assert dr == cr, f"{part} {date} out of balance: {dr} vs {cr}"
    journal_entries.append({"part": part, "date": date, "memo": memo, "lines": lines})


def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


# (a) receipt of the note in exchange for inventory sold (ignore COGS)
entry(
    "a",
    "June 30, Year 1",
    "Receipt of noninterest-bearing note in exchange for inventory sold",
    [
        line("Note Receivable", debit=FACE),
        line("Discount on Note Receivable", credit=discount_initial),
        line("Sales Revenue", credit=pv),
    ],
)

# (c) June 30 fiscal year-end: accruals Years 2, 3, 4 and settlement
for row in schedule:
    entry(
        "c",
        row["date"],
        "To record amortization of discount (interest revenue accrual)",
        [
            line("Discount on Note Receivable", debit=row["discount_amortization"]),
            line("Interest Revenue", credit=row["interest_revenue"]),
        ],
    )
entry(
    "c",
    "June 30, Year 4",
    "To record receipt of the note's face value",
    [line("Cash", debit=FACE), line("Note Receivable", credit=FACE)],
)

# (d) December 31 year-end: accruals at 12/31 Yr1, Yr2, Yr3 and 6/30 Yr4
for date, amt in calendar_accruals:
    entry(
        "d",
        date,
        "To record amortization of discount (interest revenue accrual)",
        [
            line("Discount on Note Receivable", debit=amt),
            line("Interest Revenue", credit=amt),
        ],
    )

# ------------------------------------------------------------------- answers
answers = [
    {"label": "a: Discount on Note Receivable at June 30, Year 1 (initial)",
     "value": num(discount_initial)},
    {"label": "b: carrying amount at June 30, Year 1 (schedule opening balance)",
     "value": num(pv)},
]
for row in schedule:
    y = row["note_year"]
    answers += [
        {"label": f"b: cash interest, note year {y} (ended {row['date']})",
         "value": num(row["cash_interest"])},
        {"label": f"b: interest revenue, note year {y} (ended {row['date']})",
         "value": num(row["interest_revenue"])},
        {"label": f"b: discount amortization, note year {y} (ended {row['date']})",
         "value": num(row["discount_amortization"])},
        {"label": f"b: carrying amount at {row['date']}",
         "value": num(row["carrying_amount"])},
    ]
answers += [
    {"label": "b: total cash interest over term", "value": 0},
    {"label": "b: total interest revenue over term", "value": num(total_interest)},
    {"label": "b: total discount amortization over term", "value": num(total_interest)},
]
for date, amt in calendar_accruals:
    answers.append({"label": f"d: interest revenue recognized {date}", "value": num(amt)})
answers.append(
    {"label": "d: total interest revenue over term (equals initial discount)",
     "value": num(total_calendar)}
)
answers += [
    {"label": "e: unamortized Discount on Note Receivable at December 31, Year 1",
     "value": num(discount_unamortized_1231_y1)},
    {"label": "e: net Note Receivable presented at December 31, Year 1 "
              "(noncurrent asset)",
     "value": num(net_note_1231_y1)},
]

notes = (
    "(e) At December 31, Year 1 the note is presented as a NONCURRENT asset: it "
    "matures June 30, Year 4, more than one year (and more than one operating "
    f"cycle) after the balance sheet date. It is shown at face value ${FACE:,} "
    f"less the unamortized Discount on Note Receivable of "
    f"${discount_unamortized_1231_y1:,} (a contra-asset deducted from the face "
    f"value), i.e. a net carrying amount of ${net_note_1231_y1:,}. No portion is "
    "current because the entire principal is due in a single payment at "
    "maturity and no cash interest is receivable within the next year. "
    "Amounts are whole dollars per the course's schedule presentation; "
    "cash interest is $0 each period because the stated rate is 0%, so discount "
    "amortization equals interest revenue every period."
)

out = {
    "id": "agent_043#00",
    "rounding_convention": (
        "decimal.Decimal only. ROUND_HALF_UP to whole dollars, applied per "
        "period (interest compounds on the rounded carrying amount), not "
        "round-at-end. PV derived from the exact formula 15,000/(1.10)^3 and "
        "rounded half-up to $11,269. Final period's interest revenue is the "
        "plug that brings the carrying amount to the $15,000 face, so total "
        "interest revenue equals the initial discount exactly. Interim "
        "(Dec 31) figures are 6/6-month ALLOCATIONS of the note-year schedule "
        "amounts: first half = ROUND_HALF_UP(annual/2), second half = "
        "remainder, so the halves re-sum to the annual amount."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
