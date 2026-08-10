"""Solver for agent_248#01 - ESPP number-variant twin (LO 20-3).

Rounding convention: all money is decimal.Decimal, quantized to cents
(0.01) using ROUND_HALF_UP at each period / each computed amount.
Share counts are whole shares (exact fit stated in the problem).
Every figure is derived from the stated inputs; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def m(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---- given inputs -------------------------------------------------------
par            = Decimal("2")
mkt_sep30      = Decimal("48")
planN_pct      = Decimal("0.95")
planC_pct      = Decimal("0.90")
shares_N_cash  = Decimal("3000")
shares_C_cash  = Decimal("2000")
monthly_wh     = Decimal("11400")
months         = 6
mkt_jun30      = Decimal("40")

# ---- a. classification --------------------------------------------------
# Plan N: substantially all employees, equitable, discount 5% (<=5% safe
# harbor), refunds permitted, enrollment window <=31 days -> noncompensatory.
planN_disc_pct = (Decimal("1") - planN_pct) * Decimal("100")
planC_disc_pct = (Decimal("1") - planC_pct) * Decimal("100")

# ---- b. Plan N Sept 30 cash purchase ------------------------------------
priceN   = m(mkt_sep30 * planN_pct)
cashN    = m(shares_N_cash * priceN)
csN      = m(shares_N_cash * par)
apicN    = m(cashN - csN)

# ---- c. Plan C Sept 30 cash purchase ------------------------------------
priceC   = m(mkt_sep30 * planC_pct)
cashC    = m(shares_C_cash * priceC)
compC    = m(shares_C_cash * (mkt_sep30 - priceC))
csC      = m(shares_C_cash * par)
apicC    = m(cashC + compC - csC)

# ---- d. six-month liability accumulation schedule -----------------------
rows = []
bal = Decimal("0.00")
for i in range(1, months + 1):
    beg = bal
    bal = m(bal + monthly_wh)
    rows.append((i, m(beg), m(monthly_wh), bal))
total_wh   = bal
priceJun   = m(mkt_jun30 * planN_pct)
shares_pay = int((total_wh / priceJun).to_integral_value(rounding=ROUND_HALF_UP))

# ---- e. settlement ------------------------------------------------------
csPay   = m(Decimal(shares_pay) * par)
apicPay = m(total_wh - csPay)

# ---- f. total Year 1 compensation expense -------------------------------
comp_total = m(compC + Decimal("0"))   # Plan N (noncompensatory) adds nil

month_names = ["January 31","February 28","March 31","April 30","May 31","June 30"]

answers = [
 {"label":"a: Plan N classification","value":"Noncompensatory - substantially all employees participate equitably, discount of %s%% does not exceed the 5%% safe harbor, withholdings refundable on cancellation, and the enrollment window after the price is fixed is not more than 31 days; no compensation expense is recognized" % planN_disc_pct.quantize(Decimal("1"))},
 {"label":"a: Plan C classification","value":"Compensatory - participation is limited to designated high performers (not substantially all employees) and the %s%% discount exceeds the 5%% safe harbor; the discount is compensation expense" % planC_disc_pct.quantize(Decimal("1"))},
 {"label":"b: Plan N purchase price per share (95% x $48 market)","value":float(priceN)},
 {"label":"b: Plan N cash received (3,000 shares)","value":float(cashN)},
 {"label":"b: Plan N compensation expense","value":0.00},
 {"label":"c: Plan C purchase price per share (90% x $48 market)","value":float(priceC)},
 {"label":"c: Plan C cash received (2,000 shares)","value":float(cashC)},
 {"label":"c: Plan C compensation expense (2,000 x $48 - $43.20)","value":float(compC)},
]
for i, beg, wh, end in rows:
    answers.append({"label":"d: %s Year 1 - withholding for the month" % month_names[i-1], "value":float(wh)})
    answers.append({"label":"d: %s Year 1 - cumulative Liability-ESPP balance" % month_names[i-1], "value":float(end)})
answers += [
 {"label":"d: total withholdings accumulated over the six-month offering","value":float(total_wh)},
 {"label":"d: June 30 Plan N purchase price per share (95% x $40 market)","value":float(priceJun)},
 {"label":"d: shares issued to the payroll cohort at June 30 ($68,400 / $38)","value":shares_pay},
 {"label":"f: total compensation expense recognized in Year 1 from these ESPP transactions","value":float(comp_total)},
]

jes = [
 {"part":"b","lines":[
   {"account":"Cash","debit":float(cashN),"credit":0},
   {"account":"Common Stock ($2 par, 3,000 shares)","debit":0,"credit":float(csN)},
   {"account":"Paid-in Capital in Excess of Par - Common Stock","debit":0,"credit":float(apicN)}]},
 {"part":"c","lines":[
   {"account":"Cash","debit":float(cashC),"credit":0},
   {"account":"Compensation Expense","debit":float(compC),"credit":0},
   {"account":"Common Stock ($2 par, 2,000 shares)","debit":0,"credit":float(csC)},
   {"account":"Paid-in Capital in Excess of Par - Common Stock","debit":0,"credit":float(apicC)}]},
 {"part":"e","lines":[
   {"account":"Salaries and Wages Expense (January 31 payroll withholding)","debit":float(m(monthly_wh)),"credit":0},
   {"account":"Liability - ESPP","debit":0,"credit":float(m(monthly_wh))}]},
 {"part":"e","lines":[
   {"account":"Liability - ESPP (June 30 settlement)","debit":float(total_wh),"credit":0},
   {"account":"Common Stock ($2 par, %d shares)" % shares_pay,"debit":0,"credit":float(csPay)},
   {"account":"Paid-in Capital in Excess of Par - Common Stock","debit":0,"credit":float(apicPay)}]},
]

for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)
assert m(Decimal(shares_pay) * priceJun) == total_wh

out = {"id":"agent_248#01",
 "rounding_convention":"decimal.Decimal throughout; every monetary amount quantized to cents (0.01) with ROUND_HALF_UP at each period/computation; whole shares only",
 "answers":answers,
 "journal_entries":jes,
 "insufficient_info":False,
 "notes":"Plan N is noncompensatory, so neither the September 30 cash purchase nor the June 30 payroll-cohort issuance produces compensation expense; the full proceeds are credited to Common Stock and APIC. Plan C is compensatory, so the $4.80 per-share discount ($48 market - $43.20 price) on 2,000 shares is compensation expense on September 30, and APIC is credited for cash plus expense less par. The January 31 withholding entry reclassifies the amount withheld from the payroll charge to Liability-ESPP; if gross payroll were given, the same debit would appear inside the full payroll entry with Cash credited for net pay. June 30: $68,400 / $38 = 1,800 whole shares, an exact fit with no residual liability."}
print(json.dumps(out, indent=1))
