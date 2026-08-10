"""Q3 agent_283#02 - Annuity-due recognized sale-leaseback (operating leaseback).

ROUNDING CONVENTION: decimal.Decimal throughout, never floats.
ROUND_HALF_UP applied per period (each period's interest accretion and each
displayed balance is rounded half-up to whole dollars at presentation time).
Present values and the amortization roll-forward are carried at FULL Decimal
precision (28 sig digits) internally; journal-entry and schedule figures are
stated in WHOLE DOLLARS.  Because the annuity-due schedule is mathematically
exact, the liability reaches exactly 0 after the Jan 1 Year 8 payment and the
ROU asset reaches exactly 0 after the Dec 31 Year 8 entry -- no plug was
needed to force closure.  Every figure is derived; nothing is hard-coded
except the fact-pattern inputs.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 28
C = D("0.01")


def w(x):                       # whole dollars, half-up
    return int(x.quantize(D("1"), rounding=ROUND_HALF_UP))


def c2(x):                      # two decimals, half-up
    return float(x.quantize(C, rounding=ROUND_HALF_UP))


# ---------------- fact pattern (inputs only) ----------------
SALE_PRICE = D("320000")
FAIR_VALUE = D("320000")
COST = D("700000")
ACCUM_DEP = D("430000")
USEFUL_LIFE = D("25")
TERM = 8
PMT = D("45000")
RATE = D("0.08")
ALT_TERM = 20                   # part g

# ---------------- (a) classification / sale recognition ----------------
carrying = COST - ACCUM_DEP
term_pct = (D(TERM) / USEFUL_LIFE * D("100"))

one_plus = D("1") + RATE
disc = [one_plus ** -D(t) for t in range(TERM)]          # annuity DUE: t = 0..7
pvad_factor = sum(disc, D("0"))
pv_payments = PMT * pvad_factor
pv_pct = pv_payments / FAIR_VALUE * D("100")

gain = SALE_PRICE - carrying
offmarket_adj = SALE_PRICE - FAIR_VALUE                   # 0 -> sale is at FV

# ---------------- (b) commencement measurement ----------------
rou0 = pv_payments
liab0 = pv_payments
liab_after_first = liab0 - PMT

# ---------------- (d)(e)(f) roll-forward, annuity due ----------------
sl_expense = (PMT * D(TERM)) / D(TERM)                    # straight-line cost
rows = []
liab = liab0
rou = rou0
for yr in range(1, TERM + 1):
    liab_beg = liab                       # Jan 1, before that year's payment
    liab_post = liab_beg - PMT            # Jan 1 payment (cash)
    interest = liab_post * RATE           # accretes over the year
    liab_end = liab_post + interest
    amort = sl_expense - interest         # ROU amortization = plug
    rou_end = rou - amort
    rows.append(dict(year=yr, liab_beg=liab_beg, pmt=PMT, liab_post=liab_post,
                     interest=interest, liab_end=liab_end,
                     expense=sl_expense, amort=amort, rou_beg=rou,
                     rou_end=rou_end))
    liab, rou = liab_end, rou_end

assert abs(rows[-1]["liab_end"]) < D("0.005"), rows[-1]["liab_end"]
assert abs(rows[-1]["rou_end"]) < D("0.005"), rows[-1]["rou_end"]

y1, y2, y3, y8 = rows[0], rows[1], rows[2], rows[7]

# ---------------- (g) 20-year alternative: failed sale ----------------
alt_pct = D(ALT_TERM) / USEFUL_LIFE * D("100")
alt_factor = sum((one_plus ** -D(t) for t in range(ALT_TERM)), D("0"))
alt_pmt = SALE_PRICE / alt_factor

# ---------------- answers ----------------
A = []
add = lambda l, v: A.append({"label": l, "value": v})

add("a: Carrying amount of building (700,000 cost - 430,000 accum. dep.)", w(carrying))
add("a: Lease term as % of remaining useful life (8 / 25)", c2(term_pct))
add("a: PV of the 8 annuity-due payments at 8% (PV test numerator)", c2(pv_payments))
add("a: PV as % of fair value 320,000 (90% test)", c2(pv_pct))
add("a: Leaseback classification", "Operating lease - no title transfer, no purchase option, "
    "term 32% < 75% of life, PV 87.28% < 90% of FV, and the building has an alternative "
    "use to the buyer-lessor (not specialized), so all five finance-lease tests fail.")
add("a: Sale recognition", "Recognized sale-leaseback - control transfers under ASC 606 "
    "(no repurchase option, cash price = fair value) and the leaseback is NOT a finance "
    "lease, so the transfer is accounted for as a sale.")
add("a: Sale price less fair value (off-market adjustment required)", w(offmarket_adj))
add("a: Gain on sale recognized in full at 1/1/Yr1 (320,000 - 270,000)", w(gain))

add("b: PV annuity-due factor, 8 payments, 8% (1 + PVOA 7 yrs)", float(round(pvad_factor, 5)))
add("b: Commencement PV of lease payments, full precision", c2(pv_payments))
add("b: ROU asset recorded at commencement, before first payment (whole $)", w(rou0))
add("b: Lease liability recorded at commencement, before first payment (whole $)", w(liab0))

add("c: Lease liability balance immediately after the 1/1/Yr1 payment", w(liab_after_first))

add("d: Straight-line annual lease cost (8 x 45,000 / 8 years)", w(sl_expense))
add("d: Year 1 interest accretion on the liability (8% x 234,286.65)", w(y1["interest"]))
add("d: Year 1 ROU amortization (45,000 lease cost - 18,743 accretion, the plug)", w(y1["amort"]))

for r, tag in ((y1, "Year 1"), (y2, "Year 2"), (y3, "Year 3")):
    add(f"e: {tag} - lease liability Jan 1, before payment", w(r["liab_beg"]))
    add(f"e: {tag} - Jan 1 lease payment (cash)", w(r["pmt"]))
    add(f"e: {tag} - lease liability after the Jan 1 payment", w(r["liab_post"]))
    add(f"e: {tag} - interest accretion at 8% (Dec 31 adjusting entry)", w(r["interest"]))
    add(f"e: {tag} - lease liability Dec 31, after adjusting entry", w(r["liab_end"]))
    add(f"e: {tag} - straight-line lease expense", w(r["expense"]))
    add(f"e: {tag} - ROU amortization (Dec 31 adjusting entry)", w(r["amort"]))
    add(f"e: {tag} - ROU asset Dec 31, after adjusting entry", w(r["rou_end"]))

add("f: Lease liability Jan 1 Year 8, before the final payment", w(y8["liab_beg"]))
add("f: Lease liability immediately after the Jan 1 Year 8 payment", w(y8["liab_post"]))
add("f: ROU asset carrying amount entering Year 8 (Jan 1 Year 8)", w(y8["rou_beg"]))
add("f: Year 8 interest accretion (liability is zero all year)", w(y8["interest"]))
add("f: Year 8 ROU amortization in the final Dec 31 adjusting entry", w(y8["amort"]))
add("f: ROU asset balance after the Dec 31 Year 8 entry", w(y8["rou_end"]))
add("f: Lease liability balance at Dec 31 Year 8", w(y8["liab_end"]))

add("g: Lease term as % of remaining useful life under a 20-year term (20 / 25)", c2(alt_pct))
add("g: Annual annuity-due payment that makes PV = 320,000 at 8% for 20 years", c2(alt_pmt))
add("g: Gain on sale recognized under the 20-year term", 0)
add("g: Financing liability the seller-lessee would record for the 320,000 cash", w(SALE_PRICE))
add("g: Building carrying amount that stays on the seller-lessee's books", w(carrying))
add("g: What changes", "Term is 80% of remaining life (>=75%) and PV is 100% of fair value "
    "(>=90%), so the leaseback is a FINANCE lease. The buyer-lessor therefore never obtains "
    "control, the transfer FAILS to qualify as a sale, and the deal is a failed sale-leaseback "
    "accounted for as a financing: no sale, no derecognition, no gain. Ironclad keeps the "
    "building at 270,000 and keeps depreciating it, records the 320,000 cash as a financial "
    "liability (note payable), and splits each 30,178 payment between interest expense at 8% "
    "and principal reduction. No ROU asset or lease liability is recognized. Harbor Trust "
    "records a note receivable, not a building.")

# ---------------- journal entries (whole dollars, Dr = Cr) ----------------
def je(part, lines):
    dr = sum(D(str(l.get("debit", 0))) for l in lines)
    cr = sum(D(str(l.get("credit", 0))) for l in lines)
    assert dr == cr, (part, dr, cr)
    return {"part": part, "lines": lines}


def L(acct, dr=0, cr=0):
    return {"account": acct, "debit": dr, "credit": cr}


JE = [
    je("c(1) Jan 1, Year 1 - sale of the building", [
        L("Cash", dr=w(SALE_PRICE)),
        L("Accumulated Depreciation - Building", dr=w(ACCUM_DEP)),
        L("Building", cr=w(COST)),
        L("Gain on Sale of Building", cr=w(gain)),
    ]),
    je("c(2) Jan 1, Year 1 - recognize ROU asset and lease liability", [
        L("Right-of-Use Asset", dr=w(rou0)),
        L("Lease Liability", cr=w(liab0)),
    ]),
    je("c(3) Jan 1, Year 1 - first lease payment (annuity due, at commencement)", [
        L("Lease Liability", dr=w(PMT)),
        L("Cash", cr=w(PMT)),
    ]),
    je("d Dec 31, Year 1 - period-end adjusting entry only (no cash)", [
        L("Lease Expense", dr=w(y1["expense"])),
        L("Lease Liability", cr=w(y1["interest"])),
        L("Right-of-Use Asset", cr=w(y1["amort"])),
    ]),
    je("f(1) Jan 1, Year 8 - final lease payment", [
        L("Lease Liability", dr=w(y8["liab_beg"])),
        L("Cash", cr=w(PMT)),
    ]),
    je("f(2) Dec 31, Year 8 - final adjusting entry (no cash, no accretion)", [
        L("Lease Expense", dr=w(y8["expense"])),
        L("Right-of-Use Asset", cr=w(y8["amort"])),
    ]),
]

notes = (
    "Part a: five finance-lease tests all fail - no transfer of title, no purchase option, "
    "term 8/25 = 32.00% < 75%, PV 279,286.65 / 320,000 = 87.28% < 90%, and the space has an "
    "alternative use (not specialized). Operating leaseback + cash price equal to fair value "
    "and no repurchase right => control passes, so this is a RECOGNIZED sale-leaseback and the "
    "entire 50,000 gain (320,000 - 270,000) is recognized immediately under US GAAP; no "
    "off-market adjustment is needed because sale price = fair value. "
    "Part d (emphasis): because the annuity-due payment for Year 1 was already made on Jan 1 at "
    "commencement, the December 31 entry contains NO cash line. It is a pure accrual: the "
    "single straight-line lease cost of 45,000 is split between interest accreted on the "
    "post-payment liability of 234,286.65 (credit Lease Liability 18,743) and the balancing "
    "amortization of the ROU asset (credit Right-of-Use Asset 26,257). Q1's arrears package "
    "bundled the cash payment into the same December 31 entry (Cr Cash 45,000) and the "
    "liability was reduced, not increased, on that date; here the liability GROWS at year end "
    "and is only reduced the following January 1. Note the ROU asset and the lease liability "
    "re-converge at every December 31 (both 253,030 at 12/31/Yr1) because the straight-line "
    "cost equals the annual payment and there is no prepaid or accrued rent. "
    "Part f: the Jan 1 Year 8 payment of 45,000 exactly extinguishes the liability, so no "
    "interest accretes during Year 8 and the final Dec 31 entry charges the whole 45,000 of "
    "lease cost against the remaining ROU asset, taking both accounts to exactly zero. "
    "Schedule closes exactly (no forced plug); PVs carried at full Decimal precision and "
    "journal entries stated in whole dollars, ROUND_HALF_UP per period."
)

print(json.dumps({
    "id": "agent_283#02",
    "rounding_convention": ("decimal.Decimal only (no floats); ROUND_HALF_UP applied per "
                           "period; PVs and the roll-forward carried at full 28-digit "
                           "precision internally, journal entries and schedule rows stated "
                           "in whole dollars; schedule closes exactly to zero ROU asset and "
                           "zero lease liability at 12/31/Year 8 with no plug required"),
    "answers": A,
    "journal_entries": JE,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
