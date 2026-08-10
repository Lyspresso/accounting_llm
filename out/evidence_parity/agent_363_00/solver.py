"""Riverbend Packaging Co. — detachable warrants (proportional method), straight-line
premium amortization, period-end interest, exercise, expiration, maturity.

Rounding convention: all money is decimal.Decimal, quantized to the cent with
ROUND_HALF_UP independently in each period (no float arithmetic anywhere).
Every figure is derived from the fact table; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---- Given facts -----------------------------------------------------------
face            = Decimal("600000")
coupon          = Decimal("0.07")
term_years      = 5
bond_denom      = Decimal("1000")
warrants_per_b  = Decimal("10")
ex_price        = Decimal("22")
par_per_share   = Decimal("5")
issue_pct       = Decimal("105") / Decimal("100")
bonds_only_pct  = Decimal("102") / Decimal("100")
warrant_fv      = Decimal("3")
n_exercised     = Decimal("4500")

n_bonds     = face / bond_denom
n_warrants  = q(n_bonds * warrants_per_b)
proceeds    = q(face * issue_pct)

# ---- (a) proportional allocation -------------------------------------------
fv_bonds    = q(face * bonds_only_pct)
fv_warrants = q(n_warrants * warrant_fv)
fv_total    = q(fv_bonds + fv_warrants)
alloc_bonds    = q(proceeds * fv_bonds / fv_total)
alloc_warrants = q(proceeds - alloc_bonds)
premium        = q(alloc_bonds - face)
carrying0      = alloc_bonds

# ---- (c) straight-line amortization schedule -------------------------------
cash_int    = q(face * coupon)
amort_yr    = q(premium / Decimal(term_years))
rows, cv, unamort = [], carrying0, premium
for yr in range(1, term_years + 1):
    beg = cv
    am  = amort_yr if yr < term_years else q(unamort)   # plug final year
    exp = q(cash_int - am)
    cv  = q(beg - am)
    unamort = q(unamort - am)
    rows.append({"year": yr, "beg": beg, "cash": cash_int, "amort": am, "exp": exp, "end": cv})

# ---- (e) exercise ----------------------------------------------------------
cash_ex     = q(n_exercised * ex_price)
pic_ex      = q(alloc_warrants * n_exercised / n_warrants)
par_ex      = q(n_exercised * par_per_share)
apic_ex     = q(cash_ex + pic_ex - par_ex)

# ---- (f) expiration --------------------------------------------------------
n_expired   = q(n_warrants - n_exercised)
pic_exp     = q(alloc_warrants - pic_ex)

answers = [
 {"label": "a: Number of detachable warrants issued (600 bonds x 10)", "value": float(n_warrants)},
 {"label": "a: Cash proceeds of package (600,000 x 105%)", "value": float(proceeds)},
 {"label": "a: Fair value of bonds without warrants (600,000 x 102%)", "value": float(fv_bonds)},
 {"label": "a: Fair value of warrants (6,000 x $3)", "value": float(fv_warrants)},
 {"label": "a: Total fair value of the two components", "value": float(fv_total)},
 {"label": "a: Proceeds allocated to bonds (proportional)", "value": float(alloc_bonds)},
 {"label": "a: Proceeds allocated to warrants (proportional)", "value": float(alloc_warrants)},
 {"label": "a: Initial bond carrying amount, Jan 1 Year 1", "value": float(carrying0)},
 {"label": "a: Premium on bonds payable at issuance", "value": float(premium)},
 {"label": "c: Annual cash interest (600,000 x 7%)", "value": float(cash_int)},
 {"label": "c: Annual straight-line premium amortization (12,000 / 5)", "value": float(amort_yr)},
]
for r in rows:
    y = r["year"]
    answers += [
      {"label": f"c: Year {y} beginning carrying amount", "value": float(r["beg"])},
      {"label": f"c: Year {y} cash interest paid", "value": float(r["cash"])},
      {"label": f"c: Year {y} premium amortization", "value": float(r["amort"])},
      {"label": f"c: Year {y} interest expense", "value": float(r["exp"])},
      {"label": f"c: Year {y} ending carrying amount", "value": float(r["end"])},
    ]
answers += [
 {"label": "e: Cash received on exercise (4,500 x $22)", "value": float(cash_ex)},
 {"label": "e: Paid-In Capital-Stock Warrants transferred (18,000 x 4,500/6,000)", "value": float(pic_ex)},
 {"label": "e: Common stock par issued (4,500 x $5)", "value": float(par_ex)},
 {"label": "e: Paid-in capital in excess of par on exercise", "value": float(apic_ex)},
 {"label": "f: Warrants expiring unexercised", "value": float(n_expired)},
 {"label": "f: Paid-In Capital-Stock Warrants reclassified on expiration", "value": float(pic_exp)},
 {"label": "g: Cash paid at maturity (face amount)", "value": float(face)},
 {"label": "g: Unamortized premium remaining at Dec 31 Year 5", "value": float(unamort)},
]

def L(a, d=None, c=None):
    return {"account": a, "debit": float(d or Decimal("0")), "credit": float(c or Decimal("0"))}

jes = [
 {"part": "b", "lines": [
    L("Cash", d=proceeds),
    L("Bonds Payable", c=face),
    L("Premium on Bonds Payable", c=premium),
    L("Paid-In Capital-Stock Warrants", c=alloc_warrants)]},
 {"part": "d", "lines": [
    L("Interest Expense", d=rows[0]["exp"]),
    L("Premium on Bonds Payable", d=rows[0]["amort"]),
    L("Cash", c=rows[0]["cash"])]},
 {"part": "e", "lines": [
    L("Cash", d=cash_ex),
    L("Paid-In Capital-Stock Warrants", d=pic_ex),
    L("Common Stock ($5 par)", c=par_ex),
    L("Paid-In Capital in Excess of Par-Common", c=apic_ex)]},
 {"part": "f", "lines": [
    L("Paid-In Capital-Stock Warrants", d=pic_exp),
    L("Paid-In Capital-Expired Stock Warrants", c=pic_exp)]},
 {"part": "g", "lines": [
    L("Bonds Payable", d=face),
    L("Cash", c=face)]},
]
for je in jes:
    assert abs(sum(Decimal(str(l["debit"])) - Decimal(str(l["credit"])) for l in je["lines"])) == 0

notes = ("h: The warrants are a separate EQUITY instrument, not a liability: once the "
         "$18,000 is allocated to Paid-In Capital-Stock Warrants at issuance it is a "
         "permanent equity balance with no maturity, interest or repayment obligation, so "
         "there is nothing to allocate to expense over the bond term. Only the $12,000 bond "
         "premium (a liability valuation account) is amortized against interest expense; the "
         "warrant account merely stays in equity until it is reclassified to paid-in capital "
         "on exercise or on expiration. "
         "Straight-line premium amortization = $2,400 per year; final-year amortization is the "
         "unamortized remainder so the carrying amount closes exactly at the $600,000 face.")

print(json.dumps({
 "id": "agent_363#00",
 "rounding_convention": "decimal.Decimal throughout; each period's amount quantized to the cent with ROUND_HALF_UP; final-year premium amortization takes the unamortized plug so carrying amount ends at face.",
 "answers": answers,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": notes}, indent=1))
