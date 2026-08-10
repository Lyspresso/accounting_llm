"""
agent_150#02 -- ASC 842 lessee: lease identification, five classification criteria,
finance vs operating presentation.  SECOND independent derivation.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal.  Present-value factors are carried at full
precision (28 significant digits, no intermediate rounding).  Every reported
money figure is rounded ONCE, at the point of report, to the cent using
ROUND_HALF_UP.  Percentages are reported rounded HALF_UP to 2 decimals.
The illustrative Year-1 finance-lease amortization schedule row for Option 2
is stated in cents and closes exactly: opening liability - principal reduction
= closing liability, and Dr = Cr in every entry.

DERIVATION (nothing hard-coded but the stem's own facts)
--------------------------------------------------------
Stem facts used: FV = $250,000; economic life = 10 yrs; term test 75%;
PV test 90%; no title transfer in any option; not specialized / no
alternative-use restriction in any option.  Discount rate = lessee IBR 6%
where the rate implicit in the lease is unknown (Options 1, 2, 4); the
implicit rate 5.5% where it is known to the lessee (Option 3).
Lease payments include the exercise price of a purchase option the lessee is
reasonably certain to exercise (Option 3).
"""

from decimal import Decimal as D, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 40

CENT = D("0.01")
PCT = D("0.01")


def money(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def pct(x):
    return x.quantize(PCT, rounding=ROUND_HALF_UP)


def f(x):
    return float(money(x))


def c(x):
    """Format a Decimal as $#,##0.00 for use inside derived labels."""
    return "${:,.2f}".format(money(x))


# ---------- stem facts ----------
FV = D("250000")
ECON_LIFE = D("10")
TERM_TEST = D("0.75")
PV_TEST = D("0.90")
PV_THRESHOLD = FV * PV_TEST          # derived, not hard-coded
TERM_THRESHOLD_YRS = ECON_LIFE * TERM_TEST


def pv_ordinary_annuity(pmt, rate, n):
    """PV of an ordinary annuity: PMT * (1 - (1+i)^-n)/i, full precision."""
    disc = (D(1) + rate) ** int(n)
    factor = (D(1) - D(1) / disc) / rate
    return pmt * factor, factor


def pv_annuity_due(pmt, rate, n):
    """Annuity-due factor = ordinary factor * (1+i)."""
    _, ord_factor = pv_ordinary_annuity(pmt, rate, n)
    factor = ord_factor * (D(1) + rate)
    return pmt * factor, factor


def pv_single(amt, rate, n):
    disc = (D(1) + rate) ** int(n)
    factor = D(1) / disc
    return amt * factor, factor


answers = []
notes_bits = []

# =====================================================================
# CASE A -- is there a lease?
# =====================================================================
# Identified asset test: a supplier substitution right is SUBSTANTIVE when
# (1) the supplier has the practical ability to substitute alternative assets
#     throughout the period of use, and
# (2) the supplier would benefit economically from substituting.
# Stem: identical servers in a large pool (practical ability), routinely
# reallocates for its own cost savings (economic benefit), lessee cannot
# prevent it, and only a level of capacity -- not a machine -- is promised.
# Both conditions met -> substitution right substantive -> NO identified asset
# -> no right to control the use of an identified asset -> NOT a lease.
case_a_is_lease = False
answers.append({
    "label": "a: Case A -- does the CloudRail contract contain a lease?",
    "value": "No -- it is a service contract, not a lease"
})
answers.append({
    "label": "a: Case A -- identified asset present?",
    "value": "No. CloudRail's substitution right is SUBSTANTIVE: it has the practical ability to swap among identical pooled servers throughout the period of use, and it benefits economically from doing so (routine reallocation for its own cost savings). With no identified asset there is nothing for Redrock to control."
})
answers.append({
    "label": "a: Case A -- control analysis (right to obtain substantially all economic benefits AND right to direct use)",
    "value": "Fails. Redrock is promised only a specified level of processing capacity, not a particular machine; it cannot prevent substitution and does not decide how or for what purpose any specific server is used. CloudRail directs use of its own assets. Both control elements therefore fail."
})
answers.append({
    "label": "a: Case A -- accounting consequence",
    "value": "No ROU asset and no lease liability are recognized. The hosting fees are expensed as a service/operating expense as the capacity is consumed over the 3 years (ASC 842 does not apply)."
})

# =====================================================================
# CASE B -- classify Options 1-4
# =====================================================================
IBR = D("0.06")
IMPLICIT_3 = D("0.055")

options = []

# ---- Option 1: 6 yrs, $40,000 ordinary annuity, IBR 6% ----
o1_n = D("6")
o1_pmt = D("40000")
o1_pv, o1_fac = pv_ordinary_annuity(o1_pmt, IBR, o1_n)
o1_term_ratio = o1_n / ECON_LIFE * D(100)
o1_pv_ratio = o1_pv / FV * D(100)
o1_finance = (o1_n / ECON_LIFE >= TERM_TEST) or (o1_pv >= PV_THRESHOLD)

# ---- Option 2: 8 yrs, $40,000 ordinary annuity, IBR 6% ----
o2_n = D("8")
o2_pmt = D("40000")
o2_pv, o2_fac = pv_ordinary_annuity(o2_pmt, IBR, o2_n)
o2_term_ratio = o2_n / ECON_LIFE * D(100)
o2_pv_ratio = o2_pv / FV * D(100)
o2_term_pass = o2_n / ECON_LIFE >= TERM_TEST
o2_pv_pass = o2_pv >= PV_THRESHOLD
o2_finance = o2_term_pass or o2_pv_pass

# ---- Option 3: 6 yrs, $42,000 ordinary annuity + $15,000 bargain-ish
#      purchase option reasonably certain, implicit 5.5% known ----
o3_n = D("6")
o3_pmt = D("42000")
o3_strike = D("15000")
o3_exp_fv = D("55000")
o3_bargain = o3_exp_fv - o3_strike           # economic incentive, derived
o3_pv_ann, o3_fac = pv_ordinary_annuity(o3_pmt, IMPLICIT_3, o3_n)
o3_pv_opt, o3_disc = pv_single(o3_strike, IMPLICIT_3, o3_n)
o3_pv_total = o3_pv_ann + o3_pv_opt
o3_term_ratio = o3_n / ECON_LIFE * D(100)
o3_pv_ratio = o3_pv_total / FV * D(100)
o3_term_pass = o3_n / ECON_LIFE >= TERM_TEST
o3_pv_pass = o3_pv_total >= PV_THRESHOLD
o3_option_pass = True                        # stem: reasonably certain
o3_finance = o3_option_pass or o3_term_pass or o3_pv_pass

# ---- Option 4: 6 yrs, $45,000 annuity DUE, IBR 6% ----
o4_n = D("6")
o4_pmt = D("45000")
o4_pv, o4_fac = pv_annuity_due(o4_pmt, IBR, o4_n)
o4_term_ratio = o4_n / ECON_LIFE * D(100)
o4_pv_ratio = o4_pv / FV * D(100)
o4_term_pass = o4_n / ECON_LIFE >= TERM_TEST
o4_pv_pass = o4_pv >= PV_THRESHOLD
o4_finance = o4_term_pass or o4_pv_pass

answers.append({"label": "b: PV test threshold (90% x $250,000 FV)", "value": f(PV_THRESHOLD)})
answers.append({"label": "b: Term test threshold (75% x 10-yr economic life, in years)",
                "value": float(TERM_THRESHOLD_YRS)})

# --- Option 1 reporting ---
answers.append({"label": "b: Option 1 -- discount rate used", "value": "6% lessee IBR (rate implicit in the lease is unknown)"})
answers.append({"label": "b: Option 1 -- PV annuity factor, ordinary, 6%, 6 yrs (6 dp)",
                "value": float(o1_fac.quantize(D("0.000001"), rounding=ROUND_HALF_UP))})
answers.append({"label": f"b: Option 1 -- PV of lease payments ($40,000 x {o1_fac.quantize(D('0.000001'), rounding=ROUND_HALF_UP)})", "value": f(o1_pv)})
answers.append({"label": "b: Option 1 -- PV as % of fair value", "value": float(pct(o1_pv_ratio))})
answers.append({"label": "b: Option 1 -- criterion 1 transfer of ownership", "value": "Not met (no transfer)"})
answers.append({"label": "b: Option 1 -- criterion 2 purchase option reasonably certain", "value": "Not met (no option)"})
answers.append({"label": "b: Option 1 -- criterion 3 term test (6/10 = 60% < 75%)", "value": "Not met"})
answers.append({"label": f"b: Option 1 -- criterion 4 PV test ({c(o1_pv)} < {c(PV_THRESHOLD)})", "value": "Not met"})
answers.append({"label": "b: Option 1 -- criterion 5 specialized asset / no alternative use", "value": "Not met"})
answers.append({"label": "b: Option 1 -- classification", "value": "Operating lease"})

# --- Option 2 reporting ---
answers.append({"label": "b: Option 2 -- discount rate used", "value": "6% lessee IBR (implicit rate unknown)"})
answers.append({"label": "b: Option 2 -- PV annuity factor, ordinary, 6%, 8 yrs (6 dp)",
                "value": float(o2_fac.quantize(D("0.000001"), rounding=ROUND_HALF_UP))})
answers.append({"label": f"b: Option 2 -- PV of lease payments ($40,000 x {o2_fac.quantize(D('0.000001'), rounding=ROUND_HALF_UP)})", "value": f(o2_pv)})
answers.append({"label": "b: Option 2 -- PV as % of fair value", "value": float(pct(o2_pv_ratio))})
answers.append({"label": "b: Option 2 -- criterion 3 term test (8/10 = 80% >= 75%)", "value": "MET"})
answers.append({"label": f"b: Option 2 -- criterion 4 PV test ({c(o2_pv)} >= {c(PV_THRESHOLD)})", "value": "MET"})
answers.append({"label": "b: Option 2 -- criteria 1, 2, 5", "value": "Not met (no transfer, no purchase option, not specialized)"})
answers.append({"label": "b: Option 2 -- classification",
                "value": "Finance lease (term test met; PV test also met -- only one criterion is needed)"})

# --- Option 3 reporting ---
answers.append({"label": "b: Option 3 -- discount rate used",
                "value": "5.5% rate implicit in the lease (known to lessee, so it is used instead of the IBR)"})
answers.append({"label": "b: Option 3 -- lease payments include the $15,000 option price",
                "value": "Yes -- exercise price of a purchase option reasonably certain of exercise is a lease payment"})
answers.append({"label": "b: Option 3 -- bargain element at end of term (expected FV $55,000 - $15,000 strike)",
                "value": f(o3_bargain)})
answers.append({"label": "b: Option 3 -- PV annuity factor, ordinary, 5.5%, 6 yrs (6 dp)",
                "value": float(o3_fac.quantize(D("0.000001"), rounding=ROUND_HALF_UP))})
answers.append({"label": "b: Option 3 -- PV of the six $42,000 payments", "value": f(o3_pv_ann)})
answers.append({"label": "b: Option 3 -- PV single-sum factor, 5.5%, 6 yrs (6 dp)",
                "value": float(o3_disc.quantize(D("0.000001"), rounding=ROUND_HALF_UP))})
answers.append({"label": "b: Option 3 -- PV of the $15,000 purchase option price", "value": f(o3_pv_opt)})
answers.append({"label": "b: Option 3 -- total PV of lease payments", "value": f(o3_pv_total)})
answers.append({"label": "b: Option 3 -- PV as % of fair value", "value": float(pct(o3_pv_ratio))})
answers.append({"label": "b: Option 3 -- criterion 2 purchase option reasonably certain of exercise", "value": "MET"})
answers.append({"label": "b: Option 3 -- criterion 3 term test (6/10 = 60% < 75%)", "value": "Not met"})
answers.append({"label": f"b: Option 3 -- criterion 4 PV test ({c(o3_pv_total)} < {c(PV_THRESHOLD)}; {pct(o3_pv_ratio)}% of FV)", "value": "Not met"})
answers.append({"label": "b: Option 3 -- criteria 1 and 5", "value": "Not met (no automatic transfer; not specialized)"})
answers.append({"label": "b: Option 3 -- classification",
                "value": "Finance lease -- solely because the purchase option is reasonably certain of exercise; note it FAILS both the 75% term test and the 90% PV test, so meeting any ONE criterion is decisive"})
answers.append({"label": "b: Option 3 -- amortization period if finance (purchase option expected to be exercised)",
                "value": "Economic life of 10 years (to the asset's estimated residual), not the 6-year lease term, because Redrock expects to own the asset"})

# --- Option 4 reporting ---
answers.append({"label": "b: Option 4 -- discount rate used", "value": "6% lessee IBR (implicit rate unknown)"})
answers.append({"label": "b: Option 4 -- PV annuity-DUE factor, 6%, 6 yrs (6 dp) = ordinary factor x 1.06",
                "value": float(o4_fac.quantize(D("0.000001"), rounding=ROUND_HALF_UP))})
answers.append({"label": f"b: Option 4 -- PV of lease payments ($45,000 x {o4_fac.quantize(D('0.000001'), rounding=ROUND_HALF_UP)}, payments at BEGINNING of year)",
                "value": f(o4_pv)})
answers.append({"label": "b: Option 4 -- PV as % of fair value", "value": float(pct(o4_pv_ratio))})
answers.append({"label": "b: Option 4 -- criterion 3 term test (6/10 = 60% < 75%)", "value": "Not met"})
answers.append({"label": f"b: Option 4 -- criterion 4 PV test ({c(o4_pv)} >= {c(PV_THRESHOLD)})", "value": "MET"})
answers.append({"label": "b: Option 4 -- criteria 1, 2, 5", "value": "Not met"})
answers.append({"label": "b: Option 4 -- classification",
                "value": "Finance lease (PV test met). Contrast with Option 1: same 6-year term and same 6% rate, but the larger payment made at the BEGINNING of each period lifts the PV above the 90% line"})
answers.append({"label": "b: Options 1 vs 4 -- PV increase from advance timing and higher payment",
                "value": f(o4_pv - o1_pv)})

# =====================================================================
# CASE C -- Year 1 income statement presentation contrast
# =====================================================================
# Illustrative figures use Option 2 (finance): ROU asset = liability = PV.
o2_liab0 = money(o2_pv)
o2_rou0 = o2_liab0
o2_int1 = money(o2_liab0 * IBR)
o2_amort1 = money(o2_rou0 / o2_n)
o2_princ1 = money(o2_pmt - o2_int1)
o2_liab1 = o2_liab0 - o2_princ1            # closes exactly in cents
o2_total_exp1 = o2_int1 + o2_amort1
o2_rou1 = o2_rou0 - o2_amort1
front_load = o2_total_exp1 - o2_pmt

answers.append({"label": "c: Finance lease -- number of expense lines in Year 1 income statement",
                "value": "Two separate expenses: (1) straight-line amortization of the ROU asset, presented with depreciation/amortization in operating expenses, and (2) interest expense on the lease liability, presented as a non-operating financing cost"})
answers.append({"label": "c: Operating lease -- number of expense lines in Year 1 income statement",
                "value": "One single line: 'Lease expense' (rent expense), a straight-line operating expense equal to total lease payments divided by the lease term; no interest expense and no separate amortization are shown, even though the ROU amortization is computed as a plug"})
answers.append({"label": "c: Pattern of total expense over the lease term -- finance",
                "value": "Front-loaded / decreasing: interest declines as the liability amortizes while ROU amortization is level, so total expense is highest in Year 1 and falls each year"})
answers.append({"label": "c: Pattern of total expense over the lease term -- operating",
                "value": "Level: the same straight-line amount every year"})
answers.append({"label": "c: Effect on operating income / EBITDA",
                "value": "Finance: only the amortization portion is an operating expense and it is added back in EBITDA, so operating income and EBITDA are higher and interest is below the operating line. Operating: the whole payment-based expense sits in operating income and reduces EBITDA"})
answers.append({"label": "c: Total expense over the full lease term",
                "value": "Identical under both models -- only the timing and the classification of the expense differ, not the cumulative amount"})
answers.append({"label": "c: illustrative -- Option 2 initial ROU asset = initial lease liability", "value": f(o2_rou0)})
answers.append({"label": f"c: illustrative -- Option 2 Year 1 interest expense (6% x {c(o2_liab0)})", "value": f(o2_int1)})
answers.append({"label": f"c: illustrative -- Option 2 Year 1 ROU amortization ({c(o2_rou0)} / 8 yrs straight line)", "value": f(o2_amort1)})
answers.append({"label": "c: illustrative -- Option 2 Year 1 TOTAL finance-lease expense", "value": f(o2_total_exp1)})
answers.append({"label": "c: illustrative -- straight-line expense had Option 2 been operating ($40,000 payment, level)",
                "value": f(o2_pmt)})
answers.append({"label": "c: illustrative -- Year 1 expense higher under finance than operating by", "value": f(front_load)})
answers.append({"label": f"c: illustrative -- Option 2 Year 1 principal reduction ($40,000 - {c(o2_int1)})", "value": f(o2_princ1)})
answers.append({"label": "c: illustrative -- Option 2 lease liability balance, end of Year 1", "value": f(o2_liab1)})
answers.append({"label": "c: illustrative -- Option 2 ROU asset carrying amount, end of Year 1", "value": f(o2_rou1)})
answers.append({"label": "c: cash flow statement contrast (secondary)",
                "value": "Finance: principal portion is a financing outflow and interest is operating (or financing under IFRS policy). Operating: the entire payment is a single operating outflow"})

# =====================================================================
# Illustrative journal entries supporting Case C (Option 2, finance)
# No Required part demands entries; these are shown only to make the
# presentation contrast concrete.  Dr = Cr in each entry.
# =====================================================================
journal_entries = [
    {"part": "c", "lines": [
        {"account": "Right-of-Use Asset (finance lease) [Option 2, commencement]", "debit": f(o2_rou0), "credit": 0},
        {"account": "Lease Liability", "debit": 0, "credit": f(o2_rou0)},
    ]},
    {"part": "c", "lines": [
        {"account": "Interest Expense (non-operating) [Option 2, end of Year 1]", "debit": f(o2_int1), "credit": 0},
        {"account": "Lease Liability", "debit": f(o2_princ1), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": f(o2_pmt)},
    ]},
    {"part": "c", "lines": [
        {"account": "Amortization Expense -- Right-of-Use Asset (operating expense) [Year 1]", "debit": f(o2_amort1), "credit": 0},
        {"account": "Right-of-Use Asset (finance lease)", "debit": 0, "credit": f(o2_amort1)},
    ]},
    {"part": "c", "lines": [
        {"account": "Lease Expense (single straight-line line item) [operating warehouse lease, form only]", "debit": 0, "credit": 0},
        {"account": "Lease Liability / Right-of-Use Asset (net plug) and Cash", "debit": 0, "credit": 0},
    ]},
]

# integrity checks
for je in journal_entries:
    dr = sum(D(str(l["debit"])) for l in je["lines"])
    cr = sum(D(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je, dr, cr)
assert o2_liab0 - o2_princ1 == o2_liab1
assert o1_pv < PV_THRESHOLD and o4_pv >= PV_THRESHOLD and o2_pv >= PV_THRESHOLD
assert o3_pv_total < PV_THRESHOLD

out = {
    "id": "agent_150#02",
    "rounding_convention": ("decimal.Decimal throughout; PV factors carried at full 40-digit precision with no "
                            "intermediate rounding; every reported money figure rounded once to the cent with "
                            "ROUND_HALF_UP; percentages ROUND_HALF_UP to 2 dp. The illustrative Option 2 Year-1 "
                            "finance-lease row closes exactly in cents (opening liability - principal = closing "
                            "liability) and Dr = Cr in every entry."),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Case A: the substitution right is substantive (practical ability across identical pooled servers plus "
        "economic benefit from routine reallocation), so there is no identified asset and therefore no lease -- a "
        "pure service contract, expensed as incurred. Case B: only ONE of the five criteria must be met. "
        f"Option 1 fails all five (term 60%, PV {pct(o1_pv_ratio)}% of FV) -> OPERATING. "
        f"Option 2 meets the term test at {pct(o2_term_ratio)}% and also the PV test at {pct(o2_pv_ratio)}% -> FINANCE. "
        f"Option 3 is FINANCE solely on the reasonably-certain purchase option, even though it fails the 75% term "
        f"test (60%) and the 90% PV test ({pct(o3_pv_ratio)}%); its payments include the $15,000 strike and are "
        "discounted at the KNOWN 5.5% implicit rate rather than the IBR. Note 1.055^6 = 1.378842806761, giving an "
        f"ordinary annuity factor of {o3_fac.quantize(D('0.000001'), rounding=ROUND_HALF_UP)} and a single-sum factor "
        f"of {o3_disc.quantize(D('0.000001'), rounding=ROUND_HALF_UP)}. "
        f"Option 4 is FINANCE solely on the PV test ({pct(o4_pv_ratio)}%); the annuity-DUE timing plus the larger "
        "payment is what pushes it over the line relative to Option 1's identical 6-year term and 6% rate. "
        "Case C: finance splits Year 1 expense into ROU amortization (operating) plus interest (financing), a "
        "front-loaded declining total; operating reports ONE level straight-line lease expense inside operating "
        "income. Cumulative expense over the term is the same either way. The fourth journal entry is shown in form "
        "only (zero amounts) because the stem gives no dollar facts for the warehouse lease. No Required part asked "
        "for journal entries; the Option 2 entries are illustrative support for part c."
    ),
}
print(json.dumps(out, indent=1))
