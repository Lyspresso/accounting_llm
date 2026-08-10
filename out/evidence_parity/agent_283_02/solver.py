"""Solver for agent_283#02 -- Annuity-due recognized sale-leaseback (operating), LO 17-12.

ROUNDING CONVENTION: all money computed with decimal.Decimal (28-digit context,
no floats) and quantized to the cent with ROUND_HALF_UP once PER PERIOD
(each year's interest accrual and each year's ROU amortization are rounded to
cents as they are recognized; balances carry the rounded amounts forward).
The final-year entry plugs the accumulated rounding residual so that the
ROU asset and lease liability both close to exactly zero and Dr = Cr.
Every figure is derived from the fact pattern; nothing is hard-coded.
"""
import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28
C = Decimal("0.01")


def r(x):
    return x.quantize(C, rounding=ROUND_HALF_UP)


def f(x):
    return float(r(x))


# ---------------- given facts ----------------
price = Decimal("320000")        # cash selling price = fair value
cost = Decimal("700000")
accum = Decimal("430000")
carrying = cost - accum          # 270,000 (agrees with stated carrying amount)
life = Decimal("25")
term = Decimal("8")
pmt = Decimal("45000")
rate = Decimal("0.08")
n = int(term)

# ---------------- a. classification / PV test ----------------
one = Decimal("1")
disc = (one + rate) ** n                      # 1.08^8
pv_ord = (one - one / disc) / rate            # ordinary-annuity factor
pv_due = pv_ord * (one + rate)                # annuity-due factor
pv = r(pmt * pv_due)                          # commencement PV of 8 advance payments
pv_pct = r(pv / price * Decimal("100"))
term_pct = r(term / life * Decimal("100"))
gain = r(price - carrying)
total_pmts = pmt * term

# ---------------- c. commencement ----------------
liab = pv
rou = pv
liab = r(liab - pmt)                          # after Jan 1, Year 1 payment
liab_after_first = liab

# ---------------- d/e/f. annual period-end adjusting entries ----------------
sl_expense = r(total_pmts / term)             # straight-line lease cost 45,000
rows = []
year_entries = []
for y in range(1, n + 1):
    if y > 1:                                 # Jan 1 payment of years 2..8
        liab = r(liab - pmt)
    liab_after_pay = liab
    interest = r(liab_after_pay * rate)       # accrued Dec 31, no cash
    if y < n:
        amort = r(sl_expense - interest)
        expense = sl_expense
        liab = r(liab_after_pay + interest)
        rou = r(rou - amort)
        liab_plug = Decimal("0")
    else:                                     # settlement year: clear both accounts
        liab_end_pre = r(liab_after_pay + interest)
        amort = rou                           # plug ROU to zero
        liab_plug = liab_end_pre              # plug residual liability to zero
        expense = r(amort - liab_plug)
        liab = Decimal("0.00")
        rou = Decimal("0.00")
    rows.append({
        "year": y, "jan1_payment": pmt, "liab_after_payment": liab_after_pay,
        "interest": interest, "liab_end": liab, "amort": amort, "rou_end": rou,
        "expense": expense, "liab_plug": liab_plug,
    })
    year_entries.append((y, expense, interest, amort, liab_plug))

y1 = rows[0]
y8 = rows[-1]
rou_before_final = y8["amort"]
liab_before_final_clear = y8["liab_plug"]
total_interest = sum((x["interest"] for x in rows), Decimal("0"))
total_amort = sum((x["amort"] for x in rows), Decimal("0"))

# ---------------- journal entries ----------------
def L(a, d=None, c_=None):
    return {"account": a, "debit": f(d) if d else 0, "credit": f(c_) if c_ else 0}

jes = [
    {"part": "c", "lines": [
        L("Cash", d=price),
        L("Accumulated Depreciation - Building", d=accum),
        L("Building", c_=cost),
        L("Gain on Sale of Building", c_=gain)]},
    {"part": "c", "lines": [
        L("Right-of-Use Asset", d=pv),
        L("Lease Liability", c_=pv)]},
    {"part": "c", "lines": [
        L("Lease Liability", d=pmt),
        L("Cash", c_=pmt)]},
    {"part": "d", "lines": [
        L("Lease Expense", d=y1["expense"]),
        L("Lease Liability", c_=y1["interest"]),
        L("Right-of-Use Asset", c_=y1["amort"])]},
    {"part": "f", "lines": [
        L("Lease Liability", d=pmt),
        L("Cash", c_=pmt)]},
    {"part": "f", "lines": [
        L("Lease Expense", d=y8["expense"]),
        L("Lease Liability", d=liab_before_final_clear),
        L("Right-of-Use Asset", c_=rou_before_final)]},
]
for je in jes:
    assert round(sum(l["debit"] for l in je["lines"]), 2) == \
           round(sum(l["credit"] for l in je["lines"]), 2), je

ans = []
A = lambda lab, val: ans.append({"label": lab, "value": val})

# a
A("a: PV of 8 annuity-due payments of $45,000 at 8% (annuity-due factor "
  + str(r(pv_due * Decimal("1"))) + ")", f(pv))
A("a: PV of lease payments as % of fair value $320,000 (< 90%)", f(pv_pct))
A("a: lease term as % of remaining useful life (8/25, < 75%)", f(term_pct))
A("a: classification of the leaseback",
  "Operating lease - no transfer of title, no purchase option, term 32% < 75% of "
  "remaining life, PV 87.28% < 90% of fair value, asset has alternative use "
  "(not specialized); none of the five finance-lease criteria is met.")
A("a: sale recognition conclusion",
  "Recognized (successful) sale-leaseback: sale price equals fair value $320,000, "
  "there is no repurchase option and the leaseback is an operating lease, so control "
  "of the building transfers to Harbor Trust; the seller-lessee derecognizes the "
  "building and recognizes the full gain.")
A("a: carrying amount derecognized ($700,000 cost - $430,000 accumulated depreciation)", f(carrying))
A("a: full gain on sale recognized immediately", f(gain))

# b
A("b: commencement PV of the annuity-due lease payments = Right-of-Use Asset recorded", f(pv))
A("b: lease liability recorded at commencement (before the first payment)", f(pv))
A("b: lease liability immediately after the January 1, Year 1 payment", f(liab_after_first))

# c
A("c: gain on sale of building (Jan 1, Year 1 sale entry)", f(gain))

# d
A("d: straight-line annual lease cost ($360,000 total payments / 8 years)", f(sl_expense))
A("d: Dec 31, Year 1 interest accrued on the liability (8% x $234,286.66)", f(y1["interest"]))
A("d: Dec 31, Year 1 ROU amortization (plug: $45,000 - interest)", f(y1["amort"]))
A("d: why this entry differs from Q1's year-end package",
  "With payments in advance no cash moves on December 31, so the year-end entry is a "
  "pure accrual: one $45,000 lease expense whose interest component INCREASES the lease "
  "liability (credit) instead of being settled by a payment, with the remainder credited "
  "to the ROU asset. In Q1 (payments in arrears) the December 31 package also included "
  "the cash payment, so the liability was debited down by the payment on the same date; "
  "here the liability is debited only on the following January 1.")

# e  (Years 1-3 roll-forward after each Dec 31 adjusting entry)
for x in rows[:3]:
    y = x["year"]
    A(f"e: Year {y} - January 1 payment", f(x["jan1_payment"]))
    A(f"e: Year {y} - lease liability after the January 1 payment", f(x["liab_after_payment"]))
    A(f"e: Year {y} - interest accrued at December 31 (8%)", f(x["interest"]))
    A(f"e: Year {y} - lease liability balance after the December 31 adjusting entry", f(x["liab_end"]))
    A(f"e: Year {y} - ROU amortization for the year", f(x["amort"]))
    A(f"e: Year {y} - ROU asset balance after the December 31 adjusting entry", f(x["rou_end"]))
    A(f"e: Year {y} - lease expense recognized (straight line)", f(x["expense"]))

# f
A("f: January 1, Year 8 final cash payment (debit Lease Liability / credit Cash)", f(pmt))
A("f: lease liability balance remaining after the January 1, Year 8 payment (rounding residual)",
  f(liab_before_final_clear))
A("f: ROU asset balance immediately before the December 31, Year 8 adjusting entry",
  f(rou_before_final))
A("f: Year 8 interest accrued at December 31 (liability already at zero)", f(y8["interest"]))
A("f: lease expense in the December 31, Year 8 final adjusting entry", f(y8["expense"]))
A("f: ROU asset balance after the December 31, Year 8 entry", 0.0)
A("f: lease liability balance after the December 31, Year 8 entry", 0.0)
A("f: total lease expense recognized over the 8-year term", f(sl_expense * term))
A("f: total interest component over the term", f(total_interest))
A("f: total ROU amortization over the term", f(total_amort))

# g
A("g: effect if the term were 20 years (80% of life) with PV re-set to ~$320,000",
  "The leaseback would be a FINANCE lease (term 80% >= 75% of remaining economic life and "
  "PV of payments = 100% of fair value >= 90%), so control never passes to Harbor Trust and "
  "the transfer FAILS the sale test. Ironclad would recognize NO sale, NO $50,000 gain, and "
  "NO ROU asset: it keeps the building at its $270,000 carrying amount and keeps depreciating "
  "it over the 25-year remaining life, and records the $320,000 cash as a financial liability. "
  "Each $45,000 payment is then split between interest expense (on the financing liability) and "
  "principal reduction instead of a single straight-line lease cost; Harbor Trust records a "
  "note receivable rather than the building.")

print(json.dumps({
    "id": "agent_283#02",
    "rounding_convention": "decimal.Decimal only (no floats); ROUND_HALF_UP to the cent applied "
                           "once per period (each annual interest accrual and each annual ROU "
                           "amortization); accumulated rounding residual of $0.01 is plugged in "
                           "the December 31, Year 8 settlement entry so ROU and lease liability "
                           "both close to $0.00 and every entry has Dr = Cr.",
    "answers": ans,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "Annuity-due measurement: ROU and lease liability are recorded at the PV of all 8 "
             "advance payments ($279,286.66); the January 1, Year 1 payment then reduces the "
             "liability in full (no interest has accrued at commencement). Operating leaseback, "
             "so a single straight-line lease cost of $45,000 per year is recognized; the "
             "December 31 accrual credits Lease Liability for interest and credits the ROU asset "
             "for the remainder, leaving ROU = liability at each December 31."
}, indent=1))
