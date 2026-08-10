#!/usr/bin/env python3
"""
Blind solver -- item agent_132#02
ACCOUNT-343 (Intermediate Accounting), LO 14-1: held-to-maturity debt investment
purchased at a PREMIUM; effective-interest amortization schedule; period-end
interest/amortization JE; sale before maturity; classification/presentation.

FACT PATTERN (taken verbatim from stem.md, nothing invented)
------------------------------------------------------------
  Investor .............. Solstice Beverage Co.
  Issuer/security ....... Redwood Partners 7% bonds
  Face amount ........... $180,000
  Purchase date ......... January 1, 2025
  Maturity .............. December 31, 2027   (3 years -> 6 semiannual periods)
  Coupon ................ 7% annual, paid semiannually June 30 / December 31
  Market (effective) .... 5% annual
  Classification ........ HTM, net investment recording (premium rolled into
                          the investment account -- no separate premium account,
                          per the CH 14 handout)
  Alternate event ....... January 1, 2027, immediately after the 12/31/2026
                          interest entry, ALL bonds sold for $183,200 cash
                          because of significant deterioration in the issuer's
                          creditworthiness (an ASC 320 circumstance that does
                          not taint the remaining HTM portfolio).

Stated rate (3.5%/period) > market rate (2.5%/period) => price > face =>
purchased at a premium, so the carrying amount amortizes DOWN toward $180,000
and interest revenue each period is LESS than the $6,300 cash coupon.

ROUNDING CONVENTION
-------------------
  * All money is decimal.Decimal. No floats anywhere in the money path.
  * Present value is computed with the EXACT closed-form annuity/lump-sum
    formulas at 28 significant digits, then the purchase price is rounded ONCE
    to the nearest dollar (ROUND_HALF_UP) as the Required part directs
    ("nearest dollar"). That rounded price is the opening carrying amount and
    the basis for the whole schedule.
    (Cross-check: the 5-decimal PV table factors for i = 2.5%, n = 6 --
    PVA 5.50813 and PV$1 0.86230 -- give $189,915.22, which rounds to the same
    $189,915, so the answer does not depend on table-vs-formula.)
  * ROUND_HALF_UP PER PERIOD, not at the end: each period's effective interest
    revenue = beginning carrying amount x 2.5%, rounded to the nearest dollar
    immediately; premium amortization = $6,300 cash - that rounded revenue; the
    rounded amortization then rolls into the next period's carrying amount.
    Rounding is therefore carried forward, never accumulated and trued up midway.
  * FINAL-PERIOD PLUG: in the last period (12/31/2027) the amortization is set
    to whatever drives the carrying amount exactly to the $180,000 face, and
    interest revenue is the $6,300 coupon less that plug. This absorbs the
    accumulated per-period rounding drift (here $1) so the investment retires
    at face -- the standard textbook treatment.
  * Nothing else is rounded: every reported figure is already a whole dollar.

USAGE
-----
  python3 solver.py            -> prints one JSON object on stdout
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 28

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d(x):
    return Decimal(str(x))


def to_dollar(x):
    """Round to the nearest whole dollar, ROUND_HALF_UP."""
    return x.quantize(DOLLAR, rounding=ROUND_HALF_UP)


def num(x):
    """Emit a Decimal as a plain JSON number (int when whole)."""
    x = x.quantize(CENT, rounding=ROUND_HALF_UP)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Given facts
# ---------------------------------------------------------------------------
FACE = d(180000)
STATED_ANNUAL = d("0.07")
MARKET_ANNUAL = d("0.05")
PERIODS_PER_YEAR = 2
YEARS = 3
N = YEARS * PERIODS_PER_YEAR                      # 6 semiannual periods
COUPON = FACE * STATED_ANNUAL / d(PERIODS_PER_YEAR)   # 180,000 x 3.5% = 6,300
I = MARKET_ANNUAL / d(PERIODS_PER_YEAR)               # 2.5% per period
SALE_PROCEEDS = d(183200)

PERIOD_DATES = [
    "2025-06-30", "2025-12-31",
    "2026-06-30", "2026-12-31",
    "2027-06-30", "2027-12-31",
]

INVEST_ACCT = "Investment in HTM Securities"

# ---------------------------------------------------------------------------
# (a) Purchase price = PV of the coupons + PV of the face, at 2.5% for 6 periods
# ---------------------------------------------------------------------------
one_plus_i_n = (Decimal(1) + I) ** N
pv_factor_lump = Decimal(1) / one_plus_i_n            # PV of $1, n=6, i=2.5%
pv_factor_annuity = (Decimal(1) - pv_factor_lump) / I  # PV of ordinary annuity

pv_exact = COUPON * pv_factor_annuity + FACE * pv_factor_lump
PURCHASE_PRICE = to_dollar(pv_exact)                   # rounded ONCE, per (a)
PREMIUM = PURCHASE_PRICE - FACE

# ---------------------------------------------------------------------------
# (b) Full effective-interest premium amortization schedule
# ---------------------------------------------------------------------------
schedule = []
carrying = PURCHASE_PRICE
for k in range(1, N + 1):
    beginning = carrying
    if k < N:
        interest_rev = to_dollar(beginning * I)        # round per period
        amortization = COUPON - interest_rev
        ending = beginning - amortization
    else:
        # final period: plug amortization so carrying retires exactly at face
        amortization = beginning - FACE
        interest_rev = COUPON - amortization
        ending = FACE
    schedule.append({
        "period": k,
        "date": PERIOD_DATES[k - 1],
        "cash_interest": COUPON,
        "interest_revenue": interest_rev,
        "premium_amortization": amortization,
        "carrying_amount_end": ending,
    })
    carrying = ending

# sanity: schedule must retire at face and premium must fully amortize
assert schedule[-1]["carrying_amount_end"] == FACE
assert sum(r["premium_amortization"] for r in schedule) == PREMIUM

# ---------------------------------------------------------------------------
# (c) June 30, 2025 interest / premium amortization  (period 1)
# ---------------------------------------------------------------------------
p1 = schedule[0]

# ---------------------------------------------------------------------------
# (d) Amortized cost at January 1, 2027 and the sale JE
#     "Immediately after the December 31, 2026 interest entry" == the ending
#     carrying amount of period 4 (12/31/2026).  No accrued interest carries
#     over: the 12/31/2026 coupon was already received on 12/31/2026.
# ---------------------------------------------------------------------------
AMORTIZED_COST_20270101 = schedule[3]["carrying_amount_end"]
gain_loss = SALE_PROCEEDS - AMORTIZED_COST_20270101     # negative => loss
IS_LOSS = gain_loss < 0
ABS_GAIN_LOSS = abs(gain_loss)

# ---------------------------------------------------------------------------
# (e) Presentation at June 30, 2025
#     Maturity 12/31/2027 is more than one year past 6/30/2025 -> NONCURRENT,
#     carried at amortized cost (HTM gets no fair-value adjustment).
# ---------------------------------------------------------------------------
BS_CARRYING_20250630 = p1["carrying_amount_end"]
INTEREST_REVENUE_6MO_20250630 = p1["interest_revenue"]

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------


def line(account, debit=Decimal(0), credit=Decimal(0)):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


je_a = {
    "part": "a",
    "date": "2025-01-01",
    "description": "Purchase of Redwood Partners 7% bonds classified as HTM "
                   "(net investment recording -- premium rolled into the "
                   "investment account).",
    "lines": [
        line(INVEST_ACCT, debit=PURCHASE_PRICE),
        line("Cash", credit=PURCHASE_PRICE),
    ],
}

je_c = {
    "part": "c",
    "date": "2025-06-30",
    "description": "Semiannual interest received and effective-interest "
                   "premium amortization (period 1).",
    "lines": [
        line("Cash", debit=p1["cash_interest"]),
        line("Interest Revenue", credit=p1["interest_revenue"]),
        line(INVEST_ACCT, credit=p1["premium_amortization"]),
    ],
}

sale_lines = [line("Cash", debit=SALE_PROCEEDS)]
if IS_LOSS:
    sale_lines.append(line("Loss on Sale of Investment", debit=ABS_GAIN_LOSS))
sale_lines.append(line(INVEST_ACCT, credit=AMORTIZED_COST_20270101))
if not IS_LOSS and ABS_GAIN_LOSS != 0:
    sale_lines.append(line("Gain on Sale of Investment", credit=ABS_GAIN_LOSS))

je_d = {
    "part": "d",
    "date": "2027-01-01",
    "description": "Sale of the entire HTM position for cash; realized "
                   "gain/loss recognized in net income.",
    "lines": sale_lines,
}

journal_entries = [je_a, je_c, je_d]

for je in journal_entries:
    td = sum(Decimal(str(l["debit"])) for l in je["lines"])
    tc = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert td == tc, (je["part"], td, tc)

# ---------------------------------------------------------------------------
# Answers -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: purchase price of the bonds on January 1, 2025 (nearest dollar)",
     "value": num(PURCHASE_PRICE)},
]

for r in schedule:
    answers.append({
        "label": "b: schedule period {p} ({dt}) -- cash interest".format(
            p=r["period"], dt=r["date"]),
        "value": num(r["cash_interest"]),
    })
    answers.append({
        "label": "b: schedule period {p} ({dt}) -- interest revenue".format(
            p=r["period"], dt=r["date"]),
        "value": num(r["interest_revenue"]),
    })
    answers.append({
        "label": "b: schedule period {p} ({dt}) -- premium amortization".format(
            p=r["period"], dt=r["date"]),
        "value": num(r["premium_amortization"]),
    })
    answers.append({
        "label": "b: schedule period {p} ({dt}) -- carrying amount (amortized cost) at end".format(
            p=r["period"], dt=r["date"]),
        "value": num(r["carrying_amount_end"]),
    })

answers.append({
    "label": "d: amortized cost of the investment on January 1, 2027",
    "value": num(AMORTIZED_COST_20270101),
})
answers.append({
    "label": "d: realized {w} on the January 1, 2027 sale (recognized in net income)".format(
        w="loss" if IS_LOSS else "gain"),
    "value": num(ABS_GAIN_LOSS),
})
answers.append({
    "label": "e(i): carrying amount reported on the June 30, 2025 balance sheet "
             "(noncurrent investment, at amortized cost)",
    "value": num(BS_CARRYING_20250630),
})
answers.append({
    "label": "e(i): interest revenue for the six months ended June 30, 2025",
    "value": num(INTEREST_REVENUE_6MO_20250630),
})

notes = (
    "e(i) Presentation: HTM debt securities are reported at AMORTIZED COST -- no "
    "fair-value adjustment and no unrealized holding gain/loss. Because the bonds "
    "mature 12/31/2027, more than one year after 6/30/2025, the investment is "
    "presented as a NONCURRENT asset (long-term investments), reported at its "
    "${bs} amortized cost; the original ${prem} premium is embedded in that one "
    "net investment account rather than shown separately. Interest revenue for the "
    "six months ended 6/30/2025 is ${ir} -- the effective yield (2.5% x ${pp} "
    "opening carrying amount), which is LESS than the ${cpn} cash coupon because "
    "the bonds were bought at a premium; the ${amt} difference reduces the carrying "
    "amount. Fair value of the bonds is disclosed in the notes only. "
    "e(ii) NO -- the sale does not taint the remaining HTM portfolio and does not "
    "call Solstice's intent into question. ASC 320 lists a significant deterioration "
    "in the ISSUER's creditworthiness as a change in circumstance in which a sale "
    "is not inconsistent with the original held-to-maturity intent (it is a change "
    "in the issuer's credit, not a change in Solstice's intent or ability, and is "
    "not a response to interest-rate, liquidity, or yield-management motives). "
    "Solstice may continue to classify its other debt securities as HTM. "
    "Note also that the sale occurred with only one year (2 of 6 periods) left to "
    "maturity and after roughly {pct}% of the premium had already amortized, which "
    "further supports the classification; the realized loss is reported in net "
    "income as a nonoperating item."
).format(
    bs=BS_CARRYING_20250630,
    prem=PREMIUM,
    ir=INTEREST_REVENUE_6MO_20250630,
    pp=PURCHASE_PRICE,
    cpn=COUPON,
    amt=p1["premium_amortization"],
    pct=int((PURCHASE_PRICE - AMORTIZED_COST_20270101) * 100 / PREMIUM),
)

out = {
    "id": "agent_132#02",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP. Purchase price computed with "
        "the exact PV formulas (i=2.5%, n=6) and rounded ONCE to the nearest dollar "
        "= 189,915 (5-decimal PV table factors 5.50813 / 0.86230 give 189,915.22, "
        "the same rounded answer). Effective-interest revenue is then rounded to "
        "the nearest dollar PER PERIOD and that rounded amount is carried forward; "
        "premium amortization = 6,300 cash coupon less the rounded interest "
        "revenue. Final period (12/31/2027) amortization is plugged so the carrying "
        "amount retires exactly at the 180,000 face, absorbing the $1 of "
        "accumulated rounding drift."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
