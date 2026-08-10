"""
Independent (second) cold derivation of agent_248#01 -- Silverbrook Medical Devices ESPP twin.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Every monetary result is quantized to cents with
ROUND_HALF_UP applied once per period / per computed amount (never on floats,
never chained).  Share counts are exact integers (whole shares only; the stem
states the payroll cohort is an exact fit, which the solver asserts rather than
assumes).  The withholding schedule closes exactly to the accumulated face
amount of $68,400 (no plug, no residual) -- convention: close-to-face.
Every figure is derived from the stem's facts; nothing is hard-coded except the
stem's own inputs.

DERIVATION LOGIC
----------------
(a) Noncompensatory ESPP conditions (ASC 718-50, legacy APB 25 criteria):
    substantially all employees participate on an equitable basis; the discount
    is no greater than a reasonable per-share offering to shareholders (the 5%
    safe harbor); refunds available on cancellation before purchase; the
    enrollment window after the price is fixed is limited (<= 31 days).
    Plan N meets all four (5% discount = 95% of market) -> NONCOMPENSATORY,
    no compensation cost.  Plan C restricts participation to designated high
    performers and grants a 10% discount -> COMPENSATORY; compensation cost =
    the discount (market less purchase price) recognized at the purchase date,
    with equity credited for full market value.

(b)/(c) Cash purchases 9/30 at market $48: price_N = 95% x 48, price_C = 90% x 48.
    Par $2/share drives Common Stock; remainder to APIC.

(d) Liability--ESPP accumulates $11,400/month for six months; shares at 6/30 =
    accumulated balance / (95% x $40).

(e) Representative 1/31 withholding entry (one month) and the 6/30 settlement
    entry retiring the whole liability into equity at the 5% discount price.

(f) Total Year 1 compensation expense = Plan C discount only (Plan N: zero).
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("0.01")
def m(x):  # money: one ROUND_HALF_UP per amount
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---------------- stem inputs ----------------
PAR              = Decimal("2")
MKT_SEP          = Decimal("48")
PCT_N            = Decimal("0.95")   # Plan N: 95% of market
PCT_C            = Decimal("0.90")   # Plan C: 90% of market
SH_N_SEP         = 3000
SH_C_SEP         = 2000
MONTHLY_WITHHELD = Decimal("11400")
MONTHS           = 6
MKT_JUN          = Decimal("40")
MONTH_ENDS = ["Jan 31", "Feb 28", "Mar 31", "Apr 30", "May 31", "Jun 30"]

answers, jes = [], []
def A(label, value):
    answers.append({"label": label, "value": value})

# ---------------- (a) classification ----------------
A("a: Plan N classification (substantially all employees, equitable, 5% discount "
  "(95% of market) within the safe harbor, refunds on cancellation, enrollment "
  "window <= 31 days after price fixed)", "Noncompensatory")
A("a: Plan N discount percentage from market", "5%")
A("a: Plan N compensation cost recognized", m(0))
A("a: Plan C classification (participation limited to designated high performers; "
  "10% discount exceeds the reasonable-offer safe harbor)", "Compensatory")
A("a: Plan C discount percentage from market", "10%")

# ---------------- (b) Plan N cash purchase 9/30 ----------------
price_N   = m(PCT_N * MKT_SEP)                  # 45.60
cash_N    = m(price_N * SH_N_SEP)               # 136,800
cs_N      = m(PAR * SH_N_SEP)                   # 6,000
apic_N    = m(cash_N - cs_N)                    # 130,800
A("b: Plan N purchase price per share (95% x $48)", price_N)
A("b: Plan N shares issued 9/30", SH_N_SEP)
A("b: Plan N cash received 9/30", cash_N)
A("b: Plan N Common Stock (par $2 x 3,000)", cs_N)
A("b: Plan N APIC in excess of par", apic_N)
A("b: Plan N compensation expense at 9/30 purchase", m(0))
jes.append({"part": "b", "description": "Sep 30, Year 1 -- Plan N (noncompensatory) cash purchase, 3,000 sh @ $45.60",
            "lines": [
              {"account": "Cash", "debit": cash_N, "credit": m(0)},
              {"account": "Common Stock ($2 par)", "debit": m(0), "credit": cs_N},
              {"account": "Additional Paid-in Capital in Excess of Par", "debit": m(0), "credit": apic_N},
            ]})

# ---------------- (c) Plan C cash purchase 9/30 ----------------
price_C     = m(PCT_C * MKT_SEP)                # 43.20
cash_C      = m(price_C * SH_C_SEP)             # 86,400
disc_ps_C   = m(MKT_SEP - price_C)              # 4.80
comp_C      = m(disc_ps_C * SH_C_SEP)           # 9,600
mktval_C    = m(MKT_SEP * SH_C_SEP)             # 96,000
cs_C        = m(PAR * SH_C_SEP)                 # 4,000
apic_C      = m(mktval_C - cs_C)                # 92,000
A("c: Plan C purchase price per share (90% x $48)", price_C)
A("c: Plan C shares issued 9/30", SH_C_SEP)
A("c: Plan C cash received 9/30", cash_C)
A("c: Plan C discount per share ($48 - $43.20)", disc_ps_C)
A("c: Plan C compensation expense at 9/30 (discount x 2,000 sh)", comp_C)
A("c: Plan C total market value credited to equity ($48 x 2,000)", mktval_C)
A("c: Plan C Common Stock (par $2 x 2,000)", cs_C)
A("c: Plan C APIC in excess of par", apic_C)
jes.append({"part": "c", "description": "Sep 30, Year 1 -- Plan C (compensatory) cash purchase, 2,000 sh @ $43.20; comp cost = $4.80 discount",
            "lines": [
              {"account": "Cash", "debit": cash_C, "credit": m(0)},
              {"account": "Compensation Expense", "debit": comp_C, "credit": m(0)},
              {"account": "Common Stock ($2 par)", "debit": m(0), "credit": cs_C},
              {"account": "Additional Paid-in Capital in Excess of Par", "debit": m(0), "credit": apic_C},
            ]})

# ---------------- (d) six-month Liability--ESPP accumulation schedule ----------------
sched, bal = [], m(0)
for i in range(MONTHS):
    beg = bal
    wh  = m(MONTHLY_WITHHELD)
    bal = m(beg + wh)
    sched.append({"month_end": MONTH_ENDS[i], "beginning_liability": beg,
                  "withholding_credited": wh, "ending_liability": bal})
    A(f"d: Liability--ESPP running balance after {MONTH_ENDS[i]} withholding", bal)
total_withheld = bal
assert total_withheld == m(MONTHLY_WITHHELD * MONTHS)
price_jun = m(PCT_N * MKT_JUN)                      # 38.00
shares_jun_q, rem = divmod(total_withheld, price_jun)
shares_jun = int(shares_jun_q)
assert rem == 0, "stem says exact fit / whole shares"
A("d: Total withheld over six months (6 x $11,400)", total_withheld)
A("d: Liability--ESPP balance at June 30 before settlement", total_withheld)
A("d: June 30 market price", m(MKT_JUN))
A("d: Plan N June 30 purchase price per share (95% x $40)", price_jun)
A("d: Shares issued to payroll cohort at June 30 ($68,400 / $38.00)", shares_jun)
A("d: Cash refunded for fractional/uninvested withholdings (exact fit)", m(0))

# ---------------- (e) representative 1/31 withholding + 6/30 settlement ----------------
jes.append({"part": "e", "description": "Jan 31, Year 1 -- representative period-end payroll withholding credited to the ESPP liability (one of six identical monthly entries)",
            "lines": [
              {"account": "Salaries and Wages Payable", "debit": m(MONTHLY_WITHHELD), "credit": m(0)},
              {"account": "Liability--ESPP", "debit": m(0), "credit": m(MONTHLY_WITHHELD)},
            ]})
cs_jun   = m(PAR * shares_jun)                      # 3,600
apic_jun = m(total_withheld - cs_jun)               # 64,800
A("e: January 31 withholding credited to Liability--ESPP", m(MONTHLY_WITHHELD))
A("e: June 30 settlement -- Liability--ESPP debited (fully extinguished)", total_withheld)
A("e: June 30 settlement -- Common Stock (par $2 x 1,800)", cs_jun)
A("e: June 30 settlement -- APIC in excess of par", apic_jun)
A("e: June 30 settlement -- compensation expense (Plan N noncompensatory)", m(0))
jes.append({"part": "e", "description": "Jun 30, Year 1 -- settlement of payroll-funded Plan N cohort; 1,800 sh issued @ $38.00, liability closed to zero",
            "lines": [
              {"account": "Liability--ESPP", "debit": total_withheld, "credit": m(0)},
              {"account": "Common Stock ($2 par)", "debit": m(0), "credit": cs_jun},
              {"account": "Additional Paid-in Capital in Excess of Par", "debit": m(0), "credit": apic_jun},
            ]})

# ---------------- (f) total Year 1 compensation expense ----------------
comp_N_sep = m(0); comp_N_jun = m(0)
total_comp = m(comp_N_sep + comp_C + comp_N_jun)
A("f: Compensation expense -- Plan N 9/30 cash purchase (noncompensatory)", comp_N_sep)
A("f: Compensation expense -- Plan C 9/30 cash purchase", comp_C)
A("f: Compensation expense -- Plan N payroll cohort 6/30 (noncompensatory)", comp_N_jun)
A("f: Total compensation expense recognized in Year 1 from these ESPP transactions", total_comp)

# ---------------- balance / consistency checks ----------------
for je in jes:
    d = sum((l["debit"] for l in je["lines"]), Decimal("0"))
    c = sum((l["credit"] for l in je["lines"]), Decimal("0"))
    assert d == c, (je["part"], d, c)
assert m(shares_jun * price_jun) == total_withheld
assert cash_C + comp_C == mktval_C

def enc(o):
    if isinstance(o, Decimal):
        return float(o) if o != o.to_integral_value() else int(o)
    raise TypeError
out = {
  "id": "agent_248#01",
  "rounding_convention": ("decimal.Decimal throughout; ROUND_HALF_UP to cents applied once per "
    "computed amount (no float arithmetic, no chained rounding). Whole shares only; the payroll "
    "cohort is an exact fit ($68,400 / $38.00 = 1,800 sh, zero remainder -- asserted, not assumed). "
    "The withholding schedule closes exactly to face ($68,400) and the June 30 settlement drives "
    "Liability--ESPP to exactly zero with no plug."),
  "answers": answers,
  "journal_entries": jes,
  "insufficient_info": False,
  "notes": ("(a) Plan N satisfies all noncompensatory conditions of ASC 718-50 (legacy APB 25): "
    "substantially all employees participate equitably, the 5% discount is within the safe harbor "
    "for a reasonable per-share offer to shareholders, withholdings are refundable on cancellation, "
    "and the post-pricing enrollment window is limited to 31 days -- so no compensation cost is "
    "recognized on either the 9/30 cash purchase or the 6/30 payroll settlement; cash/liability "
    "equals the full credit to contributed capital. Plan C fails the participation test (designated "
    "high performers only) and its 10% discount exceeds the safe harbor, so it is compensatory: "
    "compensation expense equals the aggregate discount, $4.80 x 2,000 = $9,600, and equity is "
    "credited for full market value $96,000 (Common Stock $4,000 + APIC $92,000). "
    "(e) The representative monthly entry debits Salaries and Wages Payable because the funding is "
    "payroll withholding (a reallocation of amounts already owed to employees, whose gross pay is "
    "expensed in payroll); an edition that records the withholding at the moment cash is disbursed "
    "would debit Cash instead -- amounts and the Liability--ESPP credit are identical either way. "
    "The six identical monthly entries produce the running balances 11,400 / 22,800 / 34,200 / "
    "45,600 / 57,000 / 68,400. No cancellations, so no refund entry. "
    "(f) Total Year 1 ESPP compensation expense = $9,600, entirely from Plan C.")
}
print(json.dumps(out, default=enc))
