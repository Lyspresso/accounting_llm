"""Cascade Outfitters — zero-interest note receivable (LO 8-5).

Rounding convention: decimal.Decimal throughout (no floats). Present values are
computed at full precision (28 sig digits) and every reported/journalized figure
is rounded to whole dollars using ROUND_HALF_UP, applied once per period (the
effective-interest schedule is run off the whole-dollar carrying amount, and the
final period is plugged if needed so the schedule closes EXACTLY to the $15,000
face / zero unamortized discount).  Semiannual allocation for the Dec-31 year-end
splits each annual period's interest revenue pro-rata by months (6/12), rounding
the first half ROUND_HALF_UP and assigning the remainder to the second half so
the annual periods and the grand total tie exactly to the original discount.
Dr = Cr on every entry.
"""
from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 28
D = Decimal
CENT = D("0.01")
ONE = D("1")


def whole(x: Decimal) -> Decimal:
    return x.quantize(ONE, rounding=ROUND_HALF_UP)


# ---------------- given facts ----------------
face = D("15000")            # stated/face value, single principal payment 6/30/Y4
n = 3                        # years
i = D("0.10")                # market rate for similar-risk notes
stated_rate = D("0")         # noninterest-bearing
fv_inventory = D("11269")    # clearly determinable fair value of inventory given up

# ---------------- (a) initial recognition ----------------
# ASC 835-30 / LO 8-5: when the fair value of the property exchanged is clearly
# determinable, that fair value measures the note.  The problem states FV = 11,269
# and PV(10%,3) = 11,269 (the exact discounted figure is 11,269.72; the problem
# rounds it down and uses 11,269 as BOTH the FV and the PV, which is what makes
# the schedule tie to face).  We record at the given fair value.
pv_exact = face / (ONE + i) ** n            # full precision cross-check
pv = fv_inventory                           # initial carrying amount of the note
discount0 = face - pv                       # initial Discount on Note Receivable

# ---------------- (b) effective-interest schedule ----------------
rows = []
carry = pv
disc_remaining = discount0
for k in range(1, n + 1):
    cash_int = D("0")                       # 0% stated rate -> no cash interest
    if k < n:
        int_rev = whole(carry * i)
    else:
        int_rev = disc_remaining            # plug final period: closes to face exactly
    amort = int_rev - cash_int              # discount amortization
    carry_beg = carry
    carry = carry + amort
    disc_remaining -= amort
    rows.append({
        "period": k,
        "carrying_beg": carry_beg,
        "cash_interest": cash_int,
        "interest_revenue": int_rev,
        "discount_amortization": amort,
        "carrying_end": carry,
        "unamortized_discount_end": disc_remaining,
    })
assert carry == face and disc_remaining == D("0")
total_int = sum((r["interest_revenue"] for r in rows), D("0"))
total_cash_int = sum((r["cash_interest"] for r in rows), D("0"))
total_amort = sum((r["discount_amortization"] for r in rows), D("0"))
assert total_int == discount0

# ---------------- (d) allocation to Dec-31 reporting periods ----------------
halves = []
for r in rows:
    h1 = whole(r["interest_revenue"] * D("6") / D("12"))
    h2 = r["interest_revenue"] - h1
    halves.append((h1, h2))
dec_y1 = halves[0][0]                              # 6/30/Y1 -> 12/31/Y1
dec_y2 = halves[0][1] + halves[1][0]               # 1/1-6/30/Y2 + 7/1-12/31/Y2
dec_y3 = halves[1][1] + halves[2][0]
jun_y4 = halves[2][1]                              # 1/1/Y4 -> 6/30/Y4
cal_total = dec_y1 + dec_y2 + dec_y3 + jun_y4
assert cal_total == discount0

# ---------------- (e) 12/31/Y1 presentation ----------------
carry_1231_y1 = pv + dec_y1
unamort_1231_y1 = face - carry_1231_y1

answers = [
    {"label": "a: Present value of note = fair value of inventory (Sales Revenue credited), 6/30/Y1", "value": float(pv)},
    {"label": "a: Note Receivable recorded at face", "value": float(face)},
    {"label": "a: Initial Discount on Note Receivable", "value": float(discount0)},

    {"label": "b: Period 1 (6/30/Y1-6/30/Y2) carrying amount, beginning", "value": float(rows[0]["carrying_beg"])},
    {"label": "b: Period 1 cash interest received", "value": float(rows[0]["cash_interest"])},
    {"label": "b: Period 1 interest revenue (10% of carrying amount)", "value": float(rows[0]["interest_revenue"])},
    {"label": "b: Period 1 discount amortization", "value": float(rows[0]["discount_amortization"])},
    {"label": "b: Period 1 carrying amount, ending 6/30/Y2", "value": float(rows[0]["carrying_end"])},
    {"label": "b: Period 2 (6/30/Y2-6/30/Y3) carrying amount, beginning", "value": float(rows[1]["carrying_beg"])},
    {"label": "b: Period 2 cash interest received", "value": float(rows[1]["cash_interest"])},
    {"label": "b: Period 2 interest revenue", "value": float(rows[1]["interest_revenue"])},
    {"label": "b: Period 2 discount amortization", "value": float(rows[1]["discount_amortization"])},
    {"label": "b: Period 2 carrying amount, ending 6/30/Y3", "value": float(rows[1]["carrying_end"])},
    {"label": "b: Period 3 (6/30/Y3-6/30/Y4) carrying amount, beginning", "value": float(rows[2]["carrying_beg"])},
    {"label": "b: Period 3 cash interest received", "value": float(rows[2]["cash_interest"])},
    {"label": "b: Period 3 interest revenue", "value": float(rows[2]["interest_revenue"])},
    {"label": "b: Period 3 discount amortization", "value": float(rows[2]["discount_amortization"])},
    {"label": "b: Period 3 carrying amount, ending 6/30/Y4 (= face)", "value": float(rows[2]["carrying_end"])},
    {"label": "b: Total cash interest over term", "value": float(total_cash_int)},
    {"label": "b: Total interest revenue over term", "value": float(total_int)},
    {"label": "b: Total discount amortization over term", "value": float(total_amort)},

    {"label": "c: Interest revenue accrued 6/30/Y2 (June 30 year-end)", "value": float(rows[0]["interest_revenue"])},
    {"label": "c: Interest revenue accrued 6/30/Y3", "value": float(rows[1]["interest_revenue"])},
    {"label": "c: Interest revenue accrued 6/30/Y4", "value": float(rows[2]["interest_revenue"])},
    {"label": "c: Cash collected at maturity 6/30/Y4", "value": float(face)},

    {"label": "d: Interest revenue accrued 12/31/Y1 (6 months of period 1)", "value": float(dec_y1)},
    {"label": "d: Interest revenue accrued 12/31/Y2 (2nd half period 1 + 1st half period 2)", "value": float(dec_y2)},
    {"label": "d: Interest revenue accrued 12/31/Y3 (2nd half period 2 + 1st half period 3)", "value": float(dec_y3)},
    {"label": "d: Interest revenue accrued 6/30/Y4 (2nd half period 3)", "value": float(jun_y4)},
    {"label": "d: Total interest revenue recognized = original discount", "value": float(cal_total)},

    {"label": "e: Note Receivable face on 12/31/Y1 balance sheet", "value": float(face)},
    {"label": "e: Unamortized Discount on Note Receivable at 12/31/Y1", "value": float(unamort_1231_y1)},
    {"label": "e: Carrying (net) amount of note at 12/31/Y1 - reported as NONCURRENT", "value": float(carry_1231_y1)},
]


def je(part, date, lines):
    dr = sum(D(str(l[1])) for l in lines)
    cr = sum(D(str(l[2])) for l in lines)
    assert dr == cr, (part, date, dr, cr)
    return {"part": part, "date": date,
            "lines": [{"account": a, "debit": float(d), "credit": float(c)} for a, d, c in lines]}


jes = [
    je("a", "Year 1 June 30", [
        ("Notes Receivable", face, D("0")),
        ("Discount on Notes Receivable", D("0"), discount0),
        ("Sales Revenue", D("0"), pv),
    ]),
    je("c", "Year 2 June 30", [
        ("Discount on Notes Receivable", rows[0]["interest_revenue"], D("0")),
        ("Interest Revenue", D("0"), rows[0]["interest_revenue"]),
    ]),
    je("c", "Year 3 June 30", [
        ("Discount on Notes Receivable", rows[1]["interest_revenue"], D("0")),
        ("Interest Revenue", D("0"), rows[1]["interest_revenue"]),
    ]),
    je("c", "Year 4 June 30", [
        ("Discount on Notes Receivable", rows[2]["interest_revenue"], D("0")),
        ("Interest Revenue", D("0"), rows[2]["interest_revenue"]),
    ]),
    je("c", "Year 4 June 30 (settlement)", [
        ("Cash", face, D("0")),
        ("Notes Receivable", D("0"), face),
    ]),
    je("d", "Year 1 December 31", [
        ("Discount on Notes Receivable", dec_y1, D("0")),
        ("Interest Revenue", D("0"), dec_y1),
    ]),
    je("d", "Year 2 December 31", [
        ("Discount on Notes Receivable", dec_y2, D("0")),
        ("Interest Revenue", D("0"), dec_y2),
    ]),
    je("d", "Year 3 December 31", [
        ("Discount on Notes Receivable", dec_y3, D("0")),
        ("Interest Revenue", D("0"), dec_y3),
    ]),
    je("d", "Year 4 June 30", [
        ("Discount on Notes Receivable", jun_y4, D("0")),
        ("Interest Revenue", D("0"), jun_y4),
    ]),
    je("d", "Year 4 June 30 (settlement)", [
        ("Cash", face, D("0")),
        ("Notes Receivable", D("0"), face),
    ]),
]

notes = (
    "Note measured at the clearly determinable fair value of the inventory given up, 11,269, which the "
    "problem also states as the PV; the unrounded discounted figure is 15,000/(1.10)^3 = 11,269.72, "
    "rounded down to 11,269 by the problem - using the stated 11,269 is what makes the schedule tie "
    "exactly to face. Initial discount 3,731. Schedule run off the "
    "whole-dollar carrying amount with ROUND_HALF_UP per period; the final period is the plug, and "
    "here it required no adjustment (1,127+1,240+1,364 = 3,731 exactly and carrying closes to 15,000). "
    "No cash interest in any period (0% stated). (c) June-30 year-end: accruals equal the annual "
    "schedule amounts. (d) Dec-31 year-end: each schedule year is split 6/12 by months - 12/31/Y1 = "
    "1,127 x 1/2 = 564 (half-up); 12/31/Y2 = 563 + 620 = 1,183; 12/31/Y3 = 620 + 682 = 1,302; "
    "6/30/Y4 = 682; total 3,731 = original discount (verified). (e) At 12/31/Y1 the note is presented "
    "as a NONCURRENT (long-term) receivable because the single principal payment is not due until "
    "6/30/Year 4, more than one year (and beyond the operating cycle) after the balance sheet date: "
    "Notes Receivable 15,000 less Discount on Notes Receivable 3,167 = net carrying amount 11,833. "
    "The discount is a contra-asset presented as a direct deduction from the note; it is not reported "
    "as an asset or deferred credit."
)

print(json.dumps({
    "id": "agent_043#00",
    "rounding_convention": "decimal.Decimal only; PVs at full precision; all reported/journalized amounts rounded to whole dollars with ROUND_HALF_UP once per period; schedule closes exactly to 15,000 face / zero discount (final period plugged); semiannual split pro-rata by months with remainder to the second half",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
