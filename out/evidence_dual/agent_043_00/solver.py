"""
Cascade Outfitters Co. -- zero-interest (noninterest-bearing) note receivable
received for inventory, 3-year term, face $15,000, market rate 10%.

INDEPENDENT COLD DERIVATION.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal.  Present values are computed at FULL precision
(28 significant digits) and every amount that lands in a journal entry or a
schedule row is rounded to WHOLE DOLLARS using ROUND_HALF_UP, applied
per period (each period's interest is rounded independently, then added to
the carrying amount, so rounding does not compound).

Full-precision PV = 15,000 / 1.10^3 = 11,269.7220...  The stem states the
inventory's clearly determinable fair value -- and therefore the note's
initial carrying amount -- as $11,269, so $11,269 is the recorded figure.
With that basis the whole-dollar schedule closes EXACTLY to face $15,000
(discount amortized exactly to zero) with no forced plug in the final row;
no balancing adjustment was needed anywhere.

For part (d) the interim (December 31) allocation splits each note-year's
already-rounded annual interest on a straight-line 6/12 basis within that
note-year (the conventional interim allocation: effective interest is
accrued annually, then apportioned by months elapsed inside the annual
period).  The first half-year is rounded ROUND_HALF_UP and the second half
is taken as the annual remainder, so each note-year's two halves sum exactly
to the annual interest and the four interim accruals sum exactly to the
original discount.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d0(x):
    """Round to whole dollars, ROUND_HALF_UP."""
    return Decimal(x).quantize(DOLLAR, rounding=ROUND_HALF_UP)


def d2(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- given facts
FACE = Decimal("15000")           # single principal payment, June 30 Year 4
N = 3                             # years
STATED_RATE = Decimal("0")        # noninterest-bearing
MARKET_RATE = Decimal("0.10")     # imputed / effective rate
FV_INVENTORY = Decimal("11269")   # clearly determinable fair value per stem

# ---------------------------------------------------- (a) initial recognition
one_plus_i = Decimal("1") + MARKET_RATE
disc_factor = one_plus_i ** N                       # 1.331
pv_full = FACE / disc_factor                        # 11269.7220...
pv_full_2dp = d2(pv_full)

# verify the stem's assertion that PV == fair value of inventory (to the dollar)
pv_rounded_dollar = d0(pv_full)                     # 11270 (half-up)
pv_matches_fv = (FV_INVENTORY == d0(pv_full)) or (
    abs(FV_INVENTORY - pv_full) < Decimal("1"))

# initial carrying amount = fair value of consideration given up
carrying_initial = FV_INVENTORY
cash_interest_per_year = FACE * STATED_RATE          # 0
discount_initial = FACE - carrying_initial           # 3731

# independent check of the effective rate: RATE(3,0,-11269,15000)
implied_rate = (FACE / carrying_initial) ** (Decimal(1) / Decimal(N)) - 1
implied_rate_pct = d2(implied_rate * 100)            # ~10.00%

# ------------------------------ (b) effective-interest amortization schedule
schedule = []
cm = carrying_initial
unamortized = discount_initial
total_interest = Decimal("0")
for yr in range(1, N + 1):
    begin = cm
    cash_int = d0(cash_interest_per_year)
    if yr < N:
        int_rev = d0(begin * MARKET_RATE)
    else:
        # final period: close the schedule exactly to face / zero discount
        int_rev = FACE - begin
        int_rev_unforced = d0(begin * MARKET_RATE)
    amort = int_rev - cash_int
    end = begin + amort
    unamortized = unamortized - amort
    total_interest += int_rev
    schedule.append({
        "note_year": yr,
        "period": f"June 30, Year {yr} to June 30, Year {yr+1}",
        "interest_date": f"June 30, Year {yr+1}",
        "beginning_carrying_amount": begin,
        "cash_interest_received": cash_int,
        "interest_revenue_at_10pct": int_rev,
        "discount_amortization": amort,
        "unamortized_discount_end": unamortized,
        "ending_carrying_amount": end,
    })
    cm = end

final_row_forced = schedule[-1]["interest_revenue_at_10pct"] != d0(
    schedule[-1]["beginning_carrying_amount"] * MARKET_RATE)
schedule_closes_to_face = (cm == FACE) and (unamortized == Decimal("0"))
totals_tie = (total_interest == discount_initial)

# -------------------------- (d) December 31 year-end interim reallocation
# Each note-year runs July 1 -> June 30.  Calendar year 1 (to Dec 31 Yr 1)
# captures 6 months of note-year 1; each later Dec 31 captures the last
# 6 months of note-year k and the first 6 months of note-year k+1.
half = Decimal("6") / Decimal("12")
first_half = []   # Jul 1 -> Dec 31 portion of each note-year
second_half = []  # Jan 1 -> Jun 30 portion of each note-year
for row in schedule:
    ann = row["interest_revenue_at_10pct"]
    fh = d0(ann * half)
    sh = ann - fh          # remainder keeps each note-year exact
    first_half.append(fh)
    second_half.append(sh)

interim = []
cm2 = carrying_initial
unam2 = discount_initial

# Dec 31, Year 1: first half of note-year 1 only
accr = first_half[0]
cm2 += accr
unam2 -= accr
interim.append({
    "accrual_date": "December 31, Year 1",
    "months": 6,
    "components": f"6/12 of note-year 1 interest {first_half[0]}",
    "interest_revenue": accr,
    "discount_amortization": accr,
    "unamortized_discount_end": unam2,
    "carrying_amount_end": cm2,
})

# Dec 31, Years 2 and 3: tail of note-year k + head of note-year k+1
for k in (1, 2):
    accr = second_half[k - 1] + first_half[k]
    cm2 += accr
    unam2 -= accr
    interim.append({
        "accrual_date": f"December 31, Year {k+1}",
        "months": 12,
        "components": (f"6/12 of note-year {k} interest {second_half[k-1]}"
                       f" + 6/12 of note-year {k+1} interest {first_half[k]}"),
        "interest_revenue": accr,
        "discount_amortization": accr,
        "unamortized_discount_end": unam2,
        "carrying_amount_end": cm2,
    })

# June 30, Year 4: final stub, tail of note-year 3
accr = second_half[2]
cm2 += accr
unam2 -= accr
interim.append({
    "accrual_date": "June 30, Year 4",
    "months": 6,
    "components": f"6/12 of note-year 3 interest {second_half[2]}",
    "interest_revenue": accr,
    "discount_amortization": accr,
    "unamortized_discount_end": unam2,
    "carrying_amount_end": cm2,
})

interim_total = sum((r["interest_revenue"] for r in interim), Decimal("0"))
interim_ties = (interim_total == discount_initial) and (cm2 == FACE) and (
    unam2 == Decimal("0"))

# -------------------- (e) Dec 31, Year 1 balance sheet presentation figures
bs_face = FACE
bs_unamortized = interim[0]["unamortized_discount_end"]     # 3,167
bs_net = interim[0]["carrying_amount_end"]                  # 11,833
# maturity June 30, Year 4 is 2.5 years after Dec 31, Year 1 -> noncurrent
months_to_maturity_from_dec31_y1 = 30
bs_classification = "noncurrent"

# ---------------------------------------------------------- journal entries
def line(acct, dr=None, cr=None):
    return {"account": acct,
            "debit": int(dr) if dr is not None else 0,
            "credit": int(cr) if cr is not None else 0}

jes = []

# (a)
jes.append({
    "part": "a",
    "date": "June 30, Year 1",
    "description": "Receipt of 3-year noninterest-bearing note for inventory sold (PV at 10%)",
    "lines": [
        line("Notes Receivable", dr=FACE),
        line("Discount on Notes Receivable", cr=discount_initial),
        line("Sales Revenue", cr=carrying_initial),
    ],
})

# (c) June 30 fiscal year-end accruals
for row in schedule:
    jes.append({
        "part": "c",
        "date": row["interest_date"],
        "description": (f"Interest accrual, note-year {row['note_year']}: "
                        f"10% x {row['beginning_carrying_amount']} carrying amount "
                        f"(no cash interest received)"),
        "lines": [
            line("Discount on Notes Receivable", dr=row["discount_amortization"]),
            line("Interest Revenue", cr=row["interest_revenue_at_10pct"]),
        ],
    })

# (c) settlement
settlement_lines = [
    line("Cash", dr=FACE),
    line("Notes Receivable", cr=FACE),
]
jes.append({
    "part": "c",
    "date": "June 30, Year 4",
    "description": "Collection of note face value at maturity (discount fully amortized)",
    "lines": settlement_lines,
})

# (d) December 31 year-end accruals
for r in interim:
    jes.append({
        "part": "d",
        "date": r["accrual_date"],
        "description": f"Interest accrual ({r['months']} months): {r['components']}",
        "lines": [
            line("Discount on Notes Receivable", dr=r["discount_amortization"]),
            line("Interest Revenue", cr=r["interest_revenue"]),
        ],
    })
jes.append({
    "part": "d",
    "date": "June 30, Year 4",
    "description": "Collection of note face value at maturity (unchanged from part c)",
    "lines": list(settlement_lines),
})

# Dr = Cr proof on every entry
for je in jes:
    tot_dr = sum(l["debit"] for l in je["lines"])
    tot_cr = sum(l["credit"] for l in je["lines"])
    assert tot_dr == tot_cr, (je["date"], tot_dr, tot_cr)
    je["total_debits"] = tot_dr
    je["total_credits"] = tot_cr
balanced = all(je["total_debits"] == je["total_credits"] for je in jes)

# --------------------------------------------------------------- answers
A = []
def add(label, value):
    A.append({"label": label, "value": value})

def i(x):
    return int(x)

# (a)
add("a: Discount factor (1.10)^3", str(disc_factor))
add("a: PV of $15,000 face at 10% for 3 years, full precision", str(pv_full_2dp))
add("a: Initial carrying amount = fair value of inventory = PV of note (recorded)", i(carrying_initial))
add("a: Face (stated) value of note", i(FACE))
add("a: Initial Discount on Notes Receivable = 15,000 - 11,269", i(discount_initial))
add("a: Stated cash interest per year (0% x 15,000)", i(cash_interest_per_year))
add("a: Sales Revenue recognized June 30, Year 1", i(carrying_initial))
add("a: Effective rate check, (15,000/11,269)^(1/3) - 1, percent", str(implied_rate_pct))
add("a: PV equals stated fair value of inventory (stem assertion verified)", bool(pv_matches_fv))
add("a: JE June 30 Yr 1 -- Dr Notes Receivable", i(FACE))
add("a: JE June 30 Yr 1 -- Cr Discount on Notes Receivable", i(discount_initial))
add("a: JE June 30 Yr 1 -- Cr Sales Revenue", i(carrying_initial))

# (b) full schedule, every row and running balance
add("b: Schedule rounding -- closes exactly to face $15,000 with no forced final-row plug", bool(schedule_closes_to_face and not final_row_forced))
for row in schedule:
    y = row["note_year"]
    add(f"b: Row {y} ({row['interest_date']}) -- beginning carrying amount", i(row["beginning_carrying_amount"]))
    add(f"b: Row {y} ({row['interest_date']}) -- cash interest received (0%)", i(row["cash_interest_received"]))
    add(f"b: Row {y} ({row['interest_date']}) -- interest revenue at 10% effective", i(row["interest_revenue_at_10pct"]))
    add(f"b: Row {y} ({row['interest_date']}) -- discount amortization", i(row["discount_amortization"]))
    add(f"b: Row {y} ({row['interest_date']}) -- unamortized discount balance, end", i(row["unamortized_discount_end"]))
    add(f"b: Row {y} ({row['interest_date']}) -- ending carrying amount", i(row["ending_carrying_amount"]))
add("b: Total cash interest received over 3 years", i(cash_interest_per_year * 3))
add("b: Total interest revenue over 3 years", i(total_interest))
add("b: Total discount amortized over 3 years", i(discount_initial))
add("b: Total interest revenue equals initial discount", bool(totals_tie))
add("b: Final carrying amount at maturity equals face", i(cm))

# (c) June 30 year-end
add("c: JE June 30 Yr 2 -- Dr Discount on Notes Receivable", i(schedule[0]["discount_amortization"]))
add("c: JE June 30 Yr 2 -- Cr Interest Revenue", i(schedule[0]["interest_revenue_at_10pct"]))
add("c: Carrying amount after June 30 Yr 2 accrual", i(schedule[0]["ending_carrying_amount"]))
add("c: JE June 30 Yr 3 -- Dr Discount on Notes Receivable", i(schedule[1]["discount_amortization"]))
add("c: JE June 30 Yr 3 -- Cr Interest Revenue", i(schedule[1]["interest_revenue_at_10pct"]))
add("c: Carrying amount after June 30 Yr 3 accrual", i(schedule[1]["ending_carrying_amount"]))
add("c: JE June 30 Yr 4 -- Dr Discount on Notes Receivable", i(schedule[2]["discount_amortization"]))
add("c: JE June 30 Yr 4 -- Cr Interest Revenue", i(schedule[2]["interest_revenue_at_10pct"]))
add("c: Carrying amount after June 30 Yr 4 accrual (= face)", i(schedule[2]["ending_carrying_amount"]))
add("c: JE June 30 Yr 4 settlement -- Dr Cash", i(FACE))
add("c: JE June 30 Yr 4 settlement -- Cr Notes Receivable", i(FACE))
add("c: No Interest Receivable is recorded (0% stated rate, no cash interest)", True)

# (d) December 31 year-end
add("d: Interim allocation basis -- each note-year's interest split straight-line 6/12 within the note-year", True)
for k, row in enumerate(schedule, start=1):
    add(f"d: Note-year {k} interest {i(row['interest_revenue_at_10pct'])} -- Jul 1 to Dec 31 portion (6 months)", i(first_half[k-1]))
    add(f"d: Note-year {k} interest {i(row['interest_revenue_at_10pct'])} -- Jan 1 to Jun 30 portion (6 months)", i(second_half[k-1]))
for r in interim:
    add(f"d: {r['accrual_date']} -- months accrued", r["months"])
    add(f"d: {r['accrual_date']} -- interest revenue (Cr) = discount amortization (Dr)", i(r["interest_revenue"]))
    add(f"d: {r['accrual_date']} -- unamortized discount after accrual", i(r["unamortized_discount_end"]))
    add(f"d: {r['accrual_date']} -- carrying amount after accrual", i(r["carrying_amount_end"]))
add("d: Sum of the four interim interest accruals", i(interim_total))
add("d: Original discount for comparison", i(discount_initial))
add("d: Total interest revenue equals original discount (verified)", bool(interim_ties))
add("d: Carrying amount at June 30 Yr 4 before collection (= face)", i(cm2))
add("d: JE June 30 Yr 4 settlement -- Dr Cash", i(FACE))
add("d: JE June 30 Yr 4 settlement -- Cr Notes Receivable", i(FACE))
add("d: Initial recognition entry unchanged from part (a)", True)

# (e) presentation
add("e: Notes Receivable, face, December 31 Year 1", i(bs_face))
add("e: Less unamortized Discount on Notes Receivable, December 31 Year 1", i(bs_unamortized))
add("e: Net carrying amount presented, December 31 Year 1", i(bs_net))
add("e: Months from December 31 Year 1 to maturity June 30 Year 4", months_to_maturity_from_dec31_y1)
add("e: Balance sheet classification at December 31 Year 1", bs_classification)
add("e: Current portion at December 31 Year 1", 0)
add("e: All journal entries balance (Dr = Cr)", bool(balanced))

notes = (
    "Independent cold derivation. Full-precision PV = 15,000/1.10^3 = 11,269.72; the stem "
    "states the inventory's clearly determinable fair value as $11,269, so $11,269 is the "
    "initial carrying amount and the discount is 15,000 - 11,269 = 3,731. "
    "Whole-dollar journal entries with full-precision PV, ROUND_HALF_UP per period. "
    "The schedule closes EXACTLY to face 15,000 / zero discount with no forced plug "
    "(1,127 + 1,240 + 1,364 = 3,731), which corroborates 11,269 as the intended basis: "
    "starting instead at a half-up 11,270 would overshoot face by $1 and require a plug. "
    "Because the stated rate is 0% there is no cash interest and no Interest Receivable; "
    "every accrual is Dr Discount on Notes Receivable / Cr Interest Revenue, and the note's "
    "carrying amount is presented net of the unamortized discount (a valuation account). "
    "Part (d) allocates each note-year's rounded annual interest straight-line 6/12 inside "
    "the note-year: Dec 31 Yr 1 = 564; Dec 31 Yr 2 = 563 + 620 = 1,183; Dec 31 Yr 3 = "
    "620 + 682 = 1,302; Jun 30 Yr 4 = 682; total 3,731 = original discount. "
    "At Dec 31 Yr 1 maturity is 30 months away, so the note is noncurrent: 15,000 face "
    "less 3,167 unamortized discount = 11,833 net, no current portion. "
    "Discount amortization equals interest revenue in every period because cash interest is zero."
)

out = {
    "id": "agent_043#00",
    "rounding_convention": (
        "decimal.Decimal throughout; PVs at full precision (getcontext().prec=28); "
        "all journal-entry and schedule amounts rounded to whole dollars with "
        "ROUND_HALF_UP applied per period (interest rounded independently each period, "
        "then added to carrying amount, so rounding never compounds). Interim (Dec 31) "
        "amounts split each note-year's rounded annual interest straight-line 6/12, "
        "first half rounded ROUND_HALF_UP and second half taken as the remainder. "
        "The schedule closes exactly to face $15,000 and zero unamortized discount with "
        "no forced final-row plug."
    ),
    "answers": A,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=1))
