"""
Solver — agent_283#02  (Q3 CORE alternate: annuity-due recognized sale-leaseback,
period-end adjusting JEs + end-of-term settlement).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal.  Present-value factors are carried at 28-digit
Decimal precision (no floats anywhere).  Journal entries and every schedule
figure are stated in WHOLE DOLLARS, rounded ROUND_HALF_UP per period.

Schedule mechanics: the opening ROU / lease liability is the full-precision PV
rounded HALF_UP to whole dollars ($279,287).  Each period's interest is then
8% x the *rounded* prior liability balance, itself rounded HALF_UP, and each
period's ROU amortization is the plug (straight-line lease cost - that period's
interest), so every individual entry has Dr = Cr and every row ties.  The final
interest-bearing period (Year 7) is plugged by $1 so the Dec 31, Year 7
liability equals exactly the last $45,000 payment; consequently the liability is
$0 for all of Year 8 (no interest) and BOTH the ROU asset and the lease
liability close to exactly $0 at Dec 31, Year 8.  Schedule closes exactly to
zero; the plug is disclosed.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 40
C = D("0.01")          # cents (analysis / display of exact PV)
W = D("1")             # whole dollars (JEs + schedule)

def w(x):  return x.quantize(W, rounding=ROUND_HALF_UP)
def c(x):  return x.quantize(C, rounding=ROUND_HALF_UP)
def f(x, n=6): return float(x.quantize(D(1).scaleb(-n), rounding=ROUND_HALF_UP))

# ----------------------------------------------------------------- stem facts
SALE_PRICE  = D("320000")     # = fair value
COST        = D("700000")
ACC_DEP     = D("430000")
CARRYING    = COST - ACC_DEP  # derive, do not trust the stem's label
LIFE        = D("25")
TERM        = D("8")
PMT         = D("45000")
RATE        = D("0.08")

assert CARRYING == D("270000")

# ------------------------------------------------- a. classification / PV test
term_pct = (TERM / LIFE)                                    # 8/25
# annuity-due PV factor, n=8, i=8%  (ordinary factor x (1+i))
one_plus = D(1) + RATE
disc_n   = one_plus ** int(TERM)
fac_ord  = (D(1) - D(1) / disc_n) / RATE
fac_due  = fac_ord * one_plus
PV_exact = PMT * fac_due
PV_round = w(PV_exact)
pv_pct   = PV_exact / SALE_PRICE                            # vs fair value

gain = SALE_PRICE - CARRYING

# ---------------------------------------------------- b/c/d/e/f  roll-forward
sl_cost = (PMT * TERM) / TERM        # straight-line single lease cost = 45,000
assert sl_cost == PMT

rows = []
liab = PV_round
rou  = PV_round
for yr in range(1, int(TERM) + 1):
    liab_begin = liab
    rou_begin  = rou
    liab_after_pmt = liab_begin - PMT
    if yr == int(TERM):
        interest = D("0")                      # liability is zero all of Yr 8
    else:
        interest = w(liab_after_pmt * RATE)
        if yr == int(TERM) - 1:
            # plug the last interest-bearing period so Dec 31 Yr 7 liability
            # equals exactly the final $45,000 payment
            interest = PMT - liab_after_pmt
    amort = sl_cost - interest                 # plug -> every JE balances
    liab_end = liab_after_pmt + interest
    rou_end  = rou_begin - amort
    assert liab_end == rou_end, (yr, liab_end, rou_end)
    rows.append(dict(year=yr, liab_begin=liab_begin, pmt=PMT,
                     liab_after_pmt=liab_after_pmt, interest=interest,
                     liab_end=liab_end, rou_begin=rou_begin, amort=amort,
                     rou_end=rou_end, lease_cost=sl_cost))
    liab, rou = liab_end, rou_end

assert liab == D("0") and rou == D("0")
tot_int   = sum(r["interest"] for r in rows)
tot_amort = sum(r["amort"] for r in rows)
tot_cost  = sum(r["lease_cost"] for r in rows)
assert tot_cost == PMT * TERM == D("360000")
assert tot_amort == PV_round
assert tot_int + tot_amort == tot_cost

# --------------------------------------------------------- g. failed sale (20y)
TERM20   = D("20")
pct20    = TERM20 / LIFE
disc20   = one_plus ** int(TERM20)
fac20o   = (D(1) - D(1) / disc20) / RATE
fac20due = fac20o * one_plus
pmt20    = w(SALE_PRICE / fac20due)                 # re-set so PV ~= 320,000
pv20_chk = c(pmt20 * fac20due)
fin_after_first = SALE_PRICE - pmt20
int20_y1 = w(fin_after_first * RATE)
dep_yr   = w(CARRYING / LIFE)                       # asset stays on the books

# ------------------------------------------------------------------- assembly
A = []
def add(label, value): A.append({"label": label, "value": value})

# a
add("a: carrying amount derived (cost 700,000 - accumulated depreciation 430,000)", int(CARRYING))
add("a: lease term as % of remaining useful life (8/25) -- fails the 'major part' (75%) test", f(term_pct*100, 2))
add("a: PV factor, annuity DUE, n=8, i=8% (5.746639 x 1.08)", f(fac_due))
add("a: PV of the 8 annuity-due lease payments (exact)", float(c(PV_exact)))
add("a: PV of lease payments as % of fair value $320,000 -- fails the 'substantially all' (90%) test", f(pv_pct*100, 2))
add("a: no title transfer / no purchase option / no guaranteed residual / alternative use exists -> no other finance criterion met; leaseback is OPERATING", "operating")
add("a: because the leaseback is NOT a finance lease and control passes under ASC 606, the transfer is a RECOGNIZED SALE (sale-leaseback accounting)", "recognized sale")
add("a: sale price $320,000 equals fair value, so the full gain is recognized immediately (320,000 - 270,000)", int(gain))
# b
add("b: commencement PV = ROU asset AND lease liability BEFORE the first payment (rounded, whole dollars)", int(PV_round))
add("b: same figure at full precision", float(c(PV_exact)))
add("b: lease liability immediately AFTER the Jan 1, Year 1 payment (279,287 - 45,000) = PV of the 7 remaining payments", int(PV_round - PMT))
# d
add("d: straight-line single lease cost per year (total payments 360,000 / 8 years)", int(sl_cost))
add("d: Year 1 interest accretion = 8% x 234,287 (liability AFTER the Jan 1 payment)", int(rows[0]["interest"]))
add("d: Year 1 ROU amortization plug = 45,000 - 18,743", int(rows[0]["amort"]))
add("d: Dec 31, Year 1 lease liability after the adjusting entry", int(rows[0]["liab_end"]))
add("d: Dec 31, Year 1 ROU asset after the adjusting entry", int(rows[0]["rou_end"]))
add("d: cash included in the Dec 31, Year 1 adjusting entry (none -- payment was made Jan 1)", 0)
add("d: why it differs from Q1's year-end package -- with payments in ADVANCE the Dec 31 entry is pure accrual: Lease Liability is CREDITED for interest and no Cash line appears. Q1 (payment in arrears) combined four lines at Dec 31 -- Dr Lease Expense 45,000, Dr Lease Liability (45,000 - interest), Cr Cash 45,000, Cr ROU (45,000 - interest) -- because the payment and the expense fell on the same date. Here the cash side sits in a separate Jan 1 entry, so the liability grows during the year instead of shrinking.", "accrual only, no cash; liability credited not debited")
# e + full schedule
for r in rows[:3]:
    y = r["year"]
    add(f"e: Year {y} row -- lease liability, Jan 1 before payment", int(r["liab_begin"]))
    add(f"e: Year {y} row -- lease payment (Jan 1)", int(r["pmt"]))
    add(f"e: Year {y} row -- lease liability, Jan 1 after payment", int(r["liab_after_pmt"]))
    add(f"e: Year {y} row -- interest accretion at 8% (Dec 31 adjusting entry)", int(r["interest"]))
    add(f"e: Year {y} row -- straight-line lease cost", int(r["lease_cost"]))
    add(f"e: Year {y} row -- ROU amortization (lease cost - interest)", int(r["amort"]))
    add(f"e: Year {y} row -- LEASE LIABILITY balance after the Dec 31 adjusting entry", int(r["liab_end"]))
    add(f"e: Year {y} row -- ROU ASSET balance after the Dec 31 adjusting entry", int(r["rou_end"]))
for r in rows[3:]:
    y = r["year"]
    add(f"e(cont.): Year {y} -- liab after Jan 1 pmt {int(r['liab_after_pmt'])}; interest {int(r['interest'])}; amortization {int(r['amort'])}; Dec 31 liability = Dec 31 ROU", int(r["liab_end"]))
add("e: ROU asset balance equals the lease liability balance at every Dec 31 (both start at 279,287 and one lease cost has been booked for each payment made)", True)
add("e: total interest accretion over the 8-year term", int(tot_int))
add("e: total ROU amortization over the term (= original ROU asset)", int(tot_amort))
add("e: total single lease cost over the term (= total cash payments)", int(tot_cost))
add("e: $1 plug applied to Year 7 interest (unrounded 8% x 41,668 = 3,333.44) so the schedule closes to exactly zero", int(rows[6]["interest"]))
# f
add("f: lease liability immediately before the Jan 1, Year 8 payment (= the final payment)", int(rows[7]["liab_begin"]))
add("f: lease liability immediately after the Jan 1, Year 8 payment", int(rows[7]["liab_after_pmt"]))
add("f: interest accrued during Year 8 (liability was zero the whole year)", int(rows[7]["interest"]))
add("f: Dec 31, Year 8 ROU amortization (entire final year's lease cost)", int(rows[7]["amort"]))
add("f: ROU asset balance after the Dec 31, Year 8 entry", int(rows[7]["rou_end"]))
add("f: lease liability balance after the Dec 31, Year 8 entry", int(rows[7]["liab_end"]))
# g
add("g: 20-year term as % of 25-year remaining life -- MAJOR PART, so the leaseback is a FINANCE lease", f(pct20*100, 2))
add("g: annuity-due PV factor, n=20, i=8%", f(fac20due))
add("g: re-set annual payment so PV ~= $320,000 (320,000 / 10.603599)", int(pmt20))
add("g: PV check of the re-set payments", float(pv20_chk))
add("g: FAILED SALE -- a finance leaseback means control never transferred, so NO sale is recognized; gain that is NOT recognized", int(gain))
add("g: building stays on Ironclad's books at its carrying amount (no derecognition, no ROU asset, no lease liability)", int(CARRYING))
add("g: continued annual depreciation on the retained building (270,000 / 25 years)", int(dep_yr))
add("g: the $320,000 cash is a FINANCIAL LIABILITY (borrowing), not sale proceeds", int(SALE_PRICE))
add("g: financial liability after the first advance payment (320,000 - 30,178)", int(fin_after_first))
add("g: Year 1 interest expense on the financial liability at the imputed 8% rate", int(int20_y1))
add("g: single lease cost / straight-line lease expense recognized under the failed sale", 0)

def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": int(dr) if dr else 0, "credit": int(cr) if cr else 0}

JE = []
def je(part, lines):
    assert sum(l["debit"] for l in lines) == sum(l["credit"] for l in lines), part
    JE.append({"part": part, "lines": lines})

je("c1 (Jan 1, Year 1 -- sale of the building to Harbor Trust)", [
    L("Cash", dr=SALE_PRICE),
    L("Accumulated Depreciation--Building", dr=ACC_DEP),
    L("Building", cr=COST),
    L("Gain on Sale of Building", cr=gain)])
je("c2 (Jan 1, Year 1 -- recognize the operating leaseback ROU asset and lease liability at PV, before the first payment)", [
    L("Right-of-Use Asset--Operating Lease", dr=PV_round),
    L("Lease Liability", cr=PV_round)])
je("c3 (Jan 1, Year 1 -- first annuity-due lease payment, all principal, no interest has accrued)", [
    L("Lease Liability", dr=PMT),
    L("Cash", cr=PMT)])
je("d (Dec 31, Year 1 -- period-end ADJUSTING entry only; no cash)", [
    L("Lease Expense", dr=sl_cost),
    L("Lease Liability", cr=rows[0]["interest"]),
    L("Right-of-Use Asset--Operating Lease", cr=rows[0]["amort"])])
je("d-alt (Dec 31, Year 2 adjusting entry, same pattern -- shown for the roll-forward)", [
    L("Lease Expense", dr=sl_cost),
    L("Lease Liability", cr=rows[1]["interest"]),
    L("Right-of-Use Asset--Operating Lease", cr=rows[1]["amort"])])
je("f1 (Jan 1, Year 8 -- final lease payment; clears the lease liability to zero)", [
    L("Lease Liability", dr=PMT),
    L("Cash", cr=PMT)])
je("f2 (Dec 31, Year 8 -- final adjusting entry; no interest because the liability was zero all year; clears the ROU asset)", [
    L("Lease Expense", dr=sl_cost),
    L("Right-of-Use Asset--Operating Lease", cr=rows[7]["amort"])])
je("g (Jan 1, Year 1 under the 20-year FAILED sale -- financing, not a sale)", [
    L("Cash", dr=SALE_PRICE),
    L("Financial Liability (Obligation to Harbor Trust)", cr=SALE_PRICE)])
je("g-cont. (Dec 31, Year 1 under the failed sale -- interest accrual and continued depreciation of the retained building)", [
    L("Interest Expense", dr=int20_y1),
    L("Depreciation Expense", dr=dep_yr),
    L("Financial Liability (Obligation to Harbor Trust)", cr=int20_y1),
    L("Accumulated Depreciation--Building", cr=dep_yr)])

notes = (
 "Classification (a): 8/25 = 32.00% of remaining life (<75%), PV 279,286.66 = 87.28% of the "
 "$320,000 fair value (<90%), no title transfer, no purchase option, no guaranteed residual, and the "
 "space has an alternative use -- so no ASC 842 finance criterion is met and the leaseback is OPERATING. "
 "Because the leaseback is not a finance lease and the ASC 606 control conditions are met, the transfer "
 "IS a sale, so the full $50,000 gain (320,000 - 270,000) hits income at once (sale price = fair value, "
 "so no off-market adjustment). "
 "Emphasis (d): with payments in advance the Dec 31 entry contains no Cash line -- Lease Expense 45,000 "
 "is split into a CREDIT to Lease Liability for interest (18,743 = 8% x 234,287, the post-payment "
 "balance) and a CREDIT to the ROU asset for the 26,257 plug. In Q1 (payment in arrears) the Dec 31 "
 "package also carried the cash payment, so Lease Liability was DEBITED for the net 45,000 - interest "
 "and Cash was credited 45,000; the liability shrank on the entry date instead of accreting. "
 "Settlement (f): the Jan 1, Year 8 payment of 45,000 retires the liability, so no interest accrues "
 "during Year 8 and the whole 45,000 of Year 8 lease cost is ROU amortization -- both accounts end at "
 "exactly $0 and total lease cost equals total cash paid, 360,000 (= 279,287 amortization + 80,713 interest). "
 "Rounding: whole-dollar schedule carried off the rounded 279,287 opening balance; the Year 7 interest "
 "figure is plugged by $1 (3,332 instead of the unrounded 3,333.44) so the Dec 31, Year 7 liability is "
 "exactly the final 45,000 payment and the schedule closes to exactly zero. A full-precision (to-the-cent) "
 "schedule reaches the same Dec 31, Year 7 balance of 45,000.00 and the identical Year 8 entries; "
 "only mid-term display figures can differ by $1. "
 "(g) A 20-year term is 80% of the 25-year remaining life -- a major part -- so the leaseback would be a "
 "FINANCE lease and, under ASC 842-40, the transfer would NOT qualify as a sale. Failed sale = financing: "
 "keep the building at 270,000 and keep depreciating it 10,800 a year, record the 320,000 cash as a "
 "financial liability, recognize NO gain, and split the re-set 30,178 annuity-due payments between "
 "interest at 8% (Year 1: 23,186 on the 289,822 post-payment balance) and principal. No ROU asset, no "
 "lease liability, and no single straight-line lease cost."
)

print(json.dumps({
  "id": "agent_283#02",
  "rounding_convention":
    "decimal.Decimal throughout; PV factors at 40-digit precision. Journal entries and all schedule "
    "figures in WHOLE DOLLARS, ROUND_HALF_UP per period. Opening ROU/liability = rounded PV 279,287; "
    "each period's interest = 8% x rounded prior liability (HALF_UP) and ROU amortization = 45,000 "
    "straight-line lease cost - that period's interest, so Dr = Cr on every entry. Year 7 interest is "
    "plugged $1 (3,332) so the schedule closes to exactly $0 for both ROU asset and lease liability.",
  "answers": A,
  "journal_entries": JE,
  "insufficient_info": False,
  "notes": notes
}, indent=1))
