#!/usr/bin/env python3
"""
Blind solver for item agent_263#02 -- HTM debt investment purchased at a PREMIUM.

FACT PATTERN (from stem.md, nothing else)
-----------------------------------------
Cascade Harbor Holdings buys $200,000 face of Meridian Telecom Corp. 8% bonds on
January 1, Year 1 when the market yield is 5%.  Interest is paid ANNUALLY each
December 31.  Bonds mature December 31, Year 3 (3 annual periods).  Intent and
ability to hold to maturity -> HTM, carried at amortized cost, effective
interest method.  Reporting year ends December 31, which is an interest date, so
no accrual stub is ever needed.

Because interest is annual, the period rate IS the annual rate: i = 5% per
period, n = 3 periods, cash coupon = 8% x $200,000 = $16,000 per period.
Stated 8% > market 5%, so the bonds price at a PREMIUM.

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal.  No floats anywhere.
* Purchase price: the present value is computed from the EXACT effective-interest
  formula at 40 significant digits -- PV = 16,000 * (1 - 1.05^-3)/0.05
  + 200,000 * 1.05^-3 -- and only then rounded to the nearest whole dollar with
  ROUND_HALF_UP.  This mirrors the course textbook (Ch. 14, Demo 14-1C), which
  prices the bond with Excel's =PV(rate, nper, pmt, fv) and reports the single
  rounded dollar figure ($103,663), rather than multiplying 5-decimal PV table
  factors.  The stem asks for the price "(nearest dollar)".
  NOTE: the two routes differ by $1 here (exact 216,339.49 -> $216,339;
  5-decimal table factors -> $216,340).  The exact/Excel route is the one that
  self-proves: only $216,339 amortizes down to exactly $200,000 at maturity with
  no forced plug in the final period (see the assertion at the end of build_schedule).
* Amortization schedule: ROUND_HALF_UP PER PERIOD, carried forward.  Each
  period's interest revenue = ROUND_HALF_UP(beginning whole-dollar carrying
  amount x 5%) to the nearest dollar; premium amortization = cash interest -
  interest revenue; ending carrying amount = beginning carrying amount -
  amortization.  No end-of-life plug is applied; the schedule closes on its own.
* Every journal entry is checked for debits == credits before it is emitted.

Run:  python3 solver.py     (prints one JSON object on stdout)
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 40

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d(x):
    return Decimal(str(x))


def to_dollar(x):
    """Round to the nearest whole dollar, ROUND_HALF_UP."""
    return x.quantize(DOLLAR, rounding=ROUND_HALF_UP)


def num(x):
    """Emit a Decimal as a plain JSON number (int when it is a whole dollar)."""
    x = x.quantize(CENT, rounding=ROUND_HALF_UP)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Given facts
# ---------------------------------------------------------------------------
FACE = d("200000")
STATED_RATE_ANNUAL = d("0.08")
MARKET_RATE_ANNUAL = d("0.05")
PAYMENTS_PER_YEAR = 1          # "Interest is paid annually each December 31"
YEARS = 3                      # Jan 1 Year 1 -> Dec 31 Year 3

N = YEARS * PAYMENTS_PER_YEAR                        # 3 periods
I = MARKET_RATE_ANNUAL / PAYMENTS_PER_YEAR           # 0.05 per period
CASH_INTEREST = FACE * STATED_RATE_ANNUAL / PAYMENTS_PER_YEAR   # 16,000


# ---------------------------------------------------------------------------
# a. Purchase price = PV of the coupon annuity + PV of the face amount
# ---------------------------------------------------------------------------
def pv_single(rate, periods):
    return Decimal(1) / ((Decimal(1) + rate) ** periods)


def pv_ordinary_annuity(rate, periods):
    return (Decimal(1) - pv_single(rate, periods)) / rate


pv_of_face_exact = FACE * pv_single(I, N)
pv_of_coupons_exact = CASH_INTEREST * pv_ordinary_annuity(I, N)
purchase_price_exact = pv_of_face_exact + pv_of_coupons_exact
PURCHASE_PRICE = to_dollar(purchase_price_exact)

# Sanity: stated > market must produce a premium.
assert PURCHASE_PRICE > FACE, "8% stated vs 5% yield must price at a premium"
PREMIUM = PURCHASE_PRICE - FACE


# ---------------------------------------------------------------------------
# b. Effective-interest amortization schedule (premium)
# ---------------------------------------------------------------------------
def build_schedule(opening):
    rows = []
    carrying = opening
    for period in range(1, N + 1):
        interest_revenue = to_dollar(carrying * I)
        amortization = CASH_INTEREST - interest_revenue      # premium: cash > revenue
        ending = carrying - amortization
        rows.append(
            {
                "period": period,
                "date": "December 31, Year %d" % period,
                "beginning_carrying_amount": carrying,
                "cash_interest": CASH_INTEREST,
                "interest_revenue": interest_revenue,
                "premium_amortization": amortization,
                "ending_carrying_amount": ending,
            }
        )
        carrying = ending

    # The schedule must retire the entire premium and land on face value with no
    # forced plug.  If this trips, the opening price is wrong, not the schedule.
    assert carrying == FACE, "schedule must close at face value, got %s" % carrying
    assert sum(r["premium_amortization"] for r in rows) == PREMIUM
    return rows


SCHEDULE = build_schedule(PURCHASE_PRICE)

Y1 = SCHEDULE[0]
Y2 = SCHEDULE[1]
Y3 = SCHEDULE[2]


# ---------------------------------------------------------------------------
# Journal entry helper (enforces debits == credits)
# ---------------------------------------------------------------------------
def entry(part, lines):
    total_dr = sum(l[1] for l in lines)
    total_cr = sum(l[2] for l in lines)
    assert total_dr == total_cr, "part %s out of balance: Dr %s / Cr %s" % (
        part,
        total_dr,
        total_cr,
    )
    return {
        "part": part,
        "lines": [
            {"account": a, "debit": num(dr), "credit": num(cr)} for (a, dr, cr) in lines
        ],
    }


ZERO = Decimal("0")

# a. January 1, Year 1 -- initial recognition at cost (premium rolled into the
#    investment account, per the course handout: the investor does not use a
#    separate premium account).
je_a = entry(
    "a",
    [
        ("Investment in HTM Securities—Meridian Telecom Bonds", PURCHASE_PRICE, ZERO),
        ("Cash", ZERO, PURCHASE_PRICE),
    ],
)

# c. December 31, Year 1 -- cash coupon received, premium amortized (credit to
#    the investment account reduces amortized cost), interest revenue plugged.
je_c = entry(
    "c",
    [
        ("Cash", Y1["cash_interest"], ZERO),
        (
            "Investment in HTM Securities—Meridian Telecom Bonds",
            ZERO,
            Y1["premium_amortization"],
        ),
        ("Interest Revenue", ZERO, Y1["interest_revenue"]),
    ],
)

# d. January 1, Year 3 sale at $204,800.  The Dec 31, Year 2 interest entry has
#    already been recorded, so the carrying amount is the Year 2 ending balance;
#    no additional amortization accrues between Dec 31, Year 2 and Jan 1, Year 3.
#    The sale is triggered by a significant deterioration in the issuer's
#    creditworthiness -- an ASC 320-10-25-6(a) circumstance -- so it does not
#    taint the remaining HTM classification.  It is still a plain derecognition:
#    gain/loss = proceeds - amortized cost.
SALE_PROCEEDS = d("204800")
CARRYING_AT_SALE = Y2["ending_carrying_amount"]
SALE_RESULT = SALE_PROCEEDS - CARRYING_AT_SALE          # negative => loss
SALE_LOSS = -SALE_RESULT if SALE_RESULT < 0 else ZERO
SALE_GAIN = SALE_RESULT if SALE_RESULT > 0 else ZERO

sale_lines = [("Cash", SALE_PROCEEDS, ZERO)]
if SALE_LOSS > 0:
    sale_lines.append(("Loss on Sale of Investment", SALE_LOSS, ZERO))
sale_lines.append(
    ("Investment in HTM Securities—Meridian Telecom Bonds", ZERO, CARRYING_AT_SALE)
)
if SALE_GAIN > 0:
    sale_lines.append(("Gain on Sale of Investment", ZERO, SALE_GAIN))
je_d = entry("d", sale_lines)

# e. December 31, Year 3 -- after the final interest entry the amortized cost is
#    exactly face value, so maturity collection produces no gain or loss.
MATURITY_CARRYING = Y3["ending_carrying_amount"]
je_e = entry(
    "e",
    [
        ("Cash", FACE, ZERO),
        ("Investment in HTM Securities—Meridian Telecom Bonds", ZERO, MATURITY_CARRYING),
    ],
)


# ---------------------------------------------------------------------------
# Output -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: January 1, Year 1 purchase price of the bond investment",
     "value": num(PURCHASE_PRICE)},

    {"label": "b: Year 1 cash interest received",
     "value": num(Y1["cash_interest"])},
    {"label": "b: Year 1 interest revenue (effective interest)",
     "value": num(Y1["interest_revenue"])},
    {"label": "b: Year 1 premium amortization",
     "value": num(Y1["premium_amortization"])},
    {"label": "b: carrying amount (amortized cost) at December 31, Year 1",
     "value": num(Y1["ending_carrying_amount"])},

    {"label": "b: Year 2 cash interest received",
     "value": num(Y2["cash_interest"])},
    {"label": "b: Year 2 interest revenue (effective interest)",
     "value": num(Y2["interest_revenue"])},
    {"label": "b: Year 2 premium amortization",
     "value": num(Y2["premium_amortization"])},
    {"label": "b: carrying amount (amortized cost) at December 31, Year 2",
     "value": num(Y2["ending_carrying_amount"])},

    {"label": "b: Year 3 cash interest received",
     "value": num(Y3["cash_interest"])},
    {"label": "b: Year 3 interest revenue (effective interest)",
     "value": num(Y3["interest_revenue"])},
    {"label": "b: Year 3 premium amortization",
     "value": num(Y3["premium_amortization"])},
    {"label": "b: carrying amount (amortized cost) at December 31, Year 3",
     "value": num(Y3["ending_carrying_amount"])},

    {"label": "c: Investment in HTM securities on the December 31, Year 1 balance sheet",
     "value": num(Y1["ending_carrying_amount"])},
    {"label": "c: Interest revenue on the Year 1 income statement",
     "value": num(Y1["interest_revenue"])},

    {"label": "d: Loss on sale of investment, January 1, Year 3",
     "value": num(SALE_LOSS)},
]

notes = (
    "Annual coupons, so the effective-interest period rate is the full 5% market "
    "yield and n = 3. Price = 16,000 x PVOA(5%,3) + 200,000 x PV(5%,3) = "
    "216,339.49 exact -> $216,339 at the nearest dollar (course textbook Ch. 14 "
    "Demo 14-1C prices bonds with the exact Excel =PV formula, not 5-decimal "
    "table factors). $216,339 is confirmed by the schedule closing on face value "
    "with no final-period plug; the 5-decimal-table alternative ($216,340) "
    "overshoots to $200,001. Premium = $16,339. Part b schedule (cash / revenue / "
    "amortization / ending amortized cost): Y1 16,000 / 10,817 / 5,183 / 211,156; "
    "Y2 16,000 / 10,558 / 5,442 / 205,714; Y3 16,000 / 10,286 / 5,714 / 200,000. "
    "Part d: the Jan 1, Year 3 sale happens after the Dec 31, Year 2 interest "
    "entry, so amortized cost is $205,714; proceeds of $204,800 give a $914 loss. "
    "The sale is due to significant deterioration in the issuer's creditworthiness "
    "(ASC 320-10-25-6(a)), so it does not call the remaining HTM classification "
    "into question. Part e: amortized cost equals face at maturity, so collection "
    "of $200,000 produces no gain or loss. Premium is rolled into the investment "
    "account rather than a separate premium account, per the course handout."
)

result = {
    "id": "agent_263#02",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats. Purchase price from the exact "
        "effective-interest PV formula at 40-digit precision, then ROUND_HALF_UP "
        "to the nearest whole dollar (Excel =PV convention used by the course "
        "textbook, not 5-decimal PV table factors). Amortization schedule rounded "
        "ROUND_HALF_UP to the nearest dollar PER PERIOD and carried forward: "
        "interest revenue = round(beginning carrying amount x 5%), amortization = "
        "cash interest - interest revenue, ending carrying = beginning - "
        "amortization. No final-period plug; the schedule closes on face value on "
        "its own."
    ),
    "answers": answers,
    "journal_entries": [je_a, je_c, je_d, je_e],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2, ensure_ascii=False))
