"""Cedar Ridge Works — 4-year, 6% semiannual bonds issued at a discount (market 8%).

Rounding convention: all money is decimal.Decimal. Present values are computed at
full precision (getcontext().prec = 50); every reported dollar figure is rounded to
the nearest whole dollar with ROUND_HALF_UP, applied per period (interest expense is
rounded each period and the rounded figure drives the next period's carrying amount).
The final period's discount amortization is PLUGGED so the schedule closes exactly to
$200,000 face (carrying amount) and zero unamortized discount.
Nothing is hard-coded: every figure below is derived from face, stated rate, market
rate, term and payment frequency. Debits equal credits in every entry.
"""
import json
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 50
CENT = Decimal(1)

def d(x):  # round to whole dollars, HALF_UP
    return x.quantize(CENT, rounding=ROUND_HALF_UP)

# ---- given facts (inputs, not answers) ----
FACE = Decimal("200000")
STATED_ANNUAL = Decimal("0.06")
MARKET_ANNUAL = Decimal("0.08")
YEARS = 4
PER_YEAR = 2
ISSUE_DATE = "January 1, Year 1"
AUTH_DATE = "January 1, Year 1"
PAY_DATES = "June 30 and December 31 each year"
MATURITY = "December 31, Year 4"
CONV_SHARES_PER_1000 = 20

n = YEARS * PER_YEAR                      # 8 semiannual periods
i = STATED_ANNUAL / PER_YEAR              # 3% stated per period
r = MARKET_ANNUAL / PER_YEAR              # 4% market (effective) per period
coupon = FACE * i                         # cash interest per period

# ---- issue price (full-precision PV, then round to nearest dollar) ----
disc_factor = Decimal(1) / ((Decimal(1) + r) ** n)
pv_face = FACE * disc_factor
pv_interest = coupon * ((Decimal(1) - disc_factor) / r)
price_exact = pv_face + pv_interest
price = d(price_exact)
discount = FACE - price
price_pct = (price / FACE * Decimal(100)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
conv_total_shares = int(FACE / Decimal(1000)) * CONV_SHARES_PER_1000

# ---- effective-interest amortization schedule ----
rows = []
cv = price
for p in range(1, n + 1):
    beg = cv
    if p < n:
        exp = d(beg * r)
        amort = exp - d(coupon)
    else:
        amort = FACE - beg          # plug so carrying amount = face at maturity
        exp = d(coupon) + amort
    end = beg + amort
    rows.append({"period": p, "beg": beg, "exp": exp, "cash": d(coupon),
                 "amort": amort, "end": end,
                 "unamort": FACE - end})
    cv = end
assert rows[-1]["end"] == FACE and rows[-1]["unamort"] == 0

tot_exp = sum((x["exp"] for x in rows), Decimal(0))
tot_cash = sum((x["cash"] for x in rows), Decimal(0))
tot_amort = sum((x["amort"] for x in rows), Decimal(0))
assert tot_amort == discount and tot_exp == tot_cash + tot_amort

p1, p2 = rows[0], rows[1]
y1_exp = p1["exp"] + p2["exp"]
y1_cash = p1["cash"] + p2["cash"]
y1_amort = p1["amort"] + p2["amort"]
cv_dec31_y1 = p2["end"]
unamort_dec31_y1 = p2["unamort"]

PDATE = {1: "June 30, Year 1", 2: "December 31, Year 1", 3: "June 30, Year 2",
         4: "December 31, Year 2", 5: "June 30, Year 3", 6: "December 31, Year 3",
         7: "June 30, Year 4", 8: "December 31, Year 4"}

I = lambda x: int(x)
A = []
def add(label, value):
    A.append({"label": label, "value": value})

# a
add("a: bond type — unsecured bonds (debentures): backed only by Cedar Ridge's general credit, no lien on specific assets", "debenture (unsecured) bonds")
add("a: bond type — convertible bonds: holders may convert into common stock after two years at %d shares per $1,000 bond (%d shares if all converted)" % (CONV_SHARES_PER_1000, conv_total_shares), "convertible bonds")
add("a: bond type — term bonds: entire $%s principal matures on a single date (%s), not in installments" % (I(FACE), MATURITY), "term bonds")
add("a: bond type — bonds issued at a discount: stated rate %s%% < market rate %s%%" % ((STATED_ANNUAL*100).normalize(), (MARKET_ANNUAL*100).normalize()), "issued at a discount")

# b
add("b(1): face (par) value", I(FACE))
add("b(2): maturity date", MATURITY)
add("b(3): stated (contract) rate per interest period = 6% annual / 2", float(i))
add("b(4): interest payment dates", PAY_DATES)
add("b(5): bond authorization date", AUTH_DATE)
add("b(6): market (effective) rate per interest period = 8% annual / 2", float(r))
add("b(7): bond selling price (issue price, rounded to nearest dollar)", I(price))
add("b(8): bond issue date", ISSUE_DATE)
add("b(7)-supporting: selling price as a percent of face", float(price_pct))

# c
add("c: cash interest payment per period ($200,000 x 3%)", I(d(coupon)))
add("c: PV of $%s face discounted 8 periods at 4%% (component, rounded)" % I(FACE), I(d(pv_face)))
add("c: PV of the 8 interest payments of $%s at 4%% (component, rounded)" % I(d(coupon)), I(d(pv_interest)))
add("c: issue price (proceeds) at January 1, Year 1", I(price))
add("c: discount on bonds payable at issuance", I(discount))

# d — full schedule
for x in rows:
    p, dt = x["period"], PDATE[x["period"]]
    add("d: period %d (%s) beginning carrying amount" % (p, dt), I(x["beg"]))
    add("d: period %d (%s) interest expense (4%% x beginning carrying amount)" % (p, dt), I(x["exp"]))
    add("d: period %d (%s) cash interest paid (3%% x face)" % (p, dt), I(x["cash"]))
    add("d: period %d (%s) discount amortization%s" % (p, dt, " (plug)" if p == n else ""), I(x["amort"]))
    add("d: period %d (%s) ending carrying amount" % (p, dt), I(x["end"]))
    add("d: period %d (%s) unamortized discount remaining" % (p, dt), I(x["unamort"]))
add("d: schedule total — interest expense over the 4-year term", I(tot_exp))
add("d: schedule total — cash interest paid over the 4-year term", I(tot_cash))
add("d: schedule total — discount amortized over the 4-year term", I(tot_amort))

# e
add("e: June 30, Year 1 interest expense", I(p1["exp"]))
add("e: June 30, Year 1 cash paid", I(p1["cash"]))
add("e: June 30, Year 1 discount amortized", I(p1["amort"]))
add("e: December 31, Year 1 interest expense", I(p2["exp"]))
add("e: December 31, Year 1 cash paid", I(p2["cash"]))
add("e: December 31, Year 1 discount amortized", I(p2["amort"]))

# f
add("f: December 31, Year 1 balance sheet — Bonds payable (face), long-term liability (matures December 31, Year 4)", I(FACE))
add("f: December 31, Year 1 balance sheet — Less: unamortized discount on bonds payable", I(unamort_dec31_y1))
add("f: December 31, Year 1 balance sheet — Carrying amount (book value) of bonds payable, reported as long-term debt", I(cv_dec31_y1))
add("f: Year 1 total interest expense (income statement)", I(y1_exp))
add("f: Year 1 total cash interest paid", I(y1_cash))
add("f: Year 1 total discount amortized", I(y1_amort))

JE = [
 {"part": "c", "lines": [
   {"account": "Cash", "debit": I(price), "credit": 0},
   {"account": "Discount on Bonds Payable", "debit": I(discount), "credit": 0},
   {"account": "Bonds Payable", "debit": 0, "credit": I(FACE)}]},
 {"part": "e", "lines": [
   {"account": "Interest Expense", "debit": I(p1["exp"]), "credit": 0},
   {"account": "Discount on Bonds Payable", "debit": 0, "credit": I(p1["amort"])},
   {"account": "Cash", "debit": 0, "credit": I(p1["cash"])}]},
 {"part": "e", "lines": [
   {"account": "Interest Expense", "debit": I(p2["exp"]), "credit": 0},
   {"account": "Discount on Bonds Payable", "debit": 0, "credit": I(p2["amort"])},
   {"account": "Cash", "debit": 0, "credit": I(p2["cash"])}]},
]
for e in JE:
    assert sum(l["debit"] for l in e["lines"]) == sum(l["credit"] for l in e["lines"])

notes = (
 f"Semiannual: n={n} periods, stated 3 percent/period, market (effective) 4 percent/period. "
 f"Issue price = PV(face) + PV(annuity of ${I(d(coupon))}) at 4 percent "
 f"= ${I(d(pv_face))} + ${I(d(pv_interest))} (components rounded separately; exact total "
 f"${price_exact.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}) = ${I(price)} "
 f"({float(price_pct)} percent of face), "
 f"a discount of ${I(discount)} because the 6 percent stated rate is below the 8 percent market rate. "
 "The conversion option is not separated: under U.S. GAAP the convertible bonds are recorded wholly "
 "as debt at the issue price, which is why the market rate on similar NONCONVERTIBLE debt (8 percent) "
 "is the pricing rate; no equity component or beneficial-conversion amount is recognized, and no entry "
 f"is made for the conversion feature until holders convert (after two years, {CONV_SHARES_PER_1000} "
 f"shares per $1,000 bond = {conv_total_shares} shares if all bonds convert). Authorization on "
 "January 1, Year 1 requires no journal entry - only issuance does. Interest expense each period = "
 "4 percent of the beginning carrying amount, rounded HALF_UP to whole dollars; cash interest is fixed "
 f"at ${I(d(coupon))}; the difference amortizes the discount and raises carrying amount toward face. "
 f"Period {n} amortization is plugged at ${I(rows[-1]['amort'])} (expense ${I(rows[-1]['exp'])} vs. "
 f"${I(d(rows[-1]['beg'] * r))} unrounded) so carrying amount closes exactly at ${I(FACE)} and "
 "unamortized discount at $0. At December 31, Year 1 the bonds are long-term (mature December 31, Year 4).")

out = {"id": "agent_011#00",
       "rounding_convention": ("decimal.Decimal throughout; PVs computed at full precision "
                               "(prec=50) then rounded to the nearest whole dollar with "
                               "ROUND_HALF_UP; interest expense rounded HALF_UP to whole dollars "
                               "each period and the rounded amount carries forward; final-period "
                               "discount amortization plugged so the schedule closes exactly to "
                               "$200,000 face / $0 unamortized discount"),
       "answers": A, "journal_entries": JE, "insufficient_info": False, "notes": notes}
print(json.dumps(out, indent=1))
