"""Solver for agent_150#02 — ASC 842 lessee: lease identification, five-criteria
classification across four option sets, and finance vs operating presentation.

ROUNDING CONVENTION: all money is decimal.Decimal. Present-value factors are
carried at 28 significant digits (no intermediate rounding); every monetary
result is rounded ONCE, per period / per computation, to the cent using
ROUND_HALF_UP. Percentages are rounded to two decimals with ROUND_HALF_UP.
Nothing is hard-coded: every factor is derived from the stated rate and term.
"""
import json
from decimal import Decimal as D, getcontext, ROUND_HALF_UP

getcontext().prec = 28
C = D("0.01")


def money(x):
    return x.quantize(C, rounding=ROUND_HALF_UP)


def pct(x):
    return (x * D(100)).quantize(C, rounding=ROUND_HALF_UP)


def pv_factor(rate, n):
    """PV of $1 received n periods hence."""
    f = D(1)
    for _ in range(n):
        f *= (D(1) + rate)
    return D(1) / f


def annuity_ordinary(rate, n):
    return (D(1) - pv_factor(rate, n)) / rate


def annuity_due(rate, n):
    return annuity_ordinary(rate, n) * (D(1) + rate)


FV = D("250000")
ECON_LIFE = D("10")
TERM_TEST = D("0.75")
PV_TEST = D("0.90")

answers = []

# ---------- Case A ----------
answers.append({
    "label": "a: Case A — does the CloudRail contract contain a lease?",
    "value": "No — it is a service contract, not a lease. There is no identified asset: "
             "CloudRail has a SUBSTANTIVE substitution right (it has the practical ability to "
             "swap in any of many identical servers and it routinely does so for its own "
             "economic benefit / cost savings, and Redrock cannot prevent substitution). "
             "Because no asset is identified, Redrock cannot obtain the right to direct the use "
             "of, or substantially all the economic benefits from, a specified asset — it buys "
             "only a level of processing capacity. Fails the ASC 842-10-15 control test, so the "
             "3-year arrangement is expensed as a service as capacity is consumed."
})

# ---------- Case B ----------
term_pct_6 = (D("6") / ECON_LIFE)
term_pct_8 = (D("8") / ECON_LIFE)

# Option 1: 6 yrs, $40,000 ordinary, IBR 6%
r1 = D("0.06")
af1 = annuity_ordinary(r1, 6)
pv1 = money(D("40000") * af1)
ratio1 = pv1 / FV

# Option 2: 8 yrs, $40,000 ordinary, IBR 6%
af2 = annuity_ordinary(r1, 8)
pv2 = money(D("40000") * af2)
ratio2 = pv2 / FV

# Option 3: 6 yrs, $42,000 ordinary, implicit 5.5%, purchase option $15,000 (RC to exercise)
r3 = D("0.055")
af3 = annuity_ordinary(r3, 6)
pv3_pmts = money(D("42000") * af3)
pv3_opt = money(D("15000") * pv_factor(r3, 6))
pv3 = pv3_pmts + pv3_opt
ratio3 = pv3 / FV

# Option 4: 6 yrs, $45,000 annuity-due, IBR 6%
af4 = annuity_due(r1, 6)
pv4 = money(D("45000") * af4)
ratio4 = pv4 / FV

answers += [
    {"label": "b: Option 1 — PV factor, ordinary annuity, 6 yrs @ 6% (IBR)",
     "value": str(af1.quantize(D("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "b: Option 1 — PV of lease payments ($40,000 x factor)", "value": str(pv1)},
    {"label": "b: Option 1 — PV as % of fair value $250,000 (90% test)",
     "value": str(pct(ratio1)) + "% — FAILS"},
    {"label": "b: Option 1 — lease term as % of 10-yr economic life (75% test)",
     "value": str(pct(term_pct_6)) + "% — FAILS"},
    {"label": "b: Option 1 — classification",
     "value": "OPERATING — no transfer of ownership, no purchase option, term 60% < 75%, "
              "PV 78.68% < 90%, asset is not specialized (no alternative-use restriction). "
              "All five criteria fail."},

    {"label": "b: Option 2 — lease term as % of 10-yr economic life (75% test)",
     "value": str(pct(term_pct_8)) + "% — MET"},
    {"label": "b: Option 2 — PV factor, ordinary annuity, 8 yrs @ 6% (IBR)",
     "value": str(af2.quantize(D("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "b: Option 2 — PV of lease payments ($40,000 x factor)", "value": str(pv2)},
    {"label": "b: Option 2 — PV as % of fair value $250,000 (90% test)",
     "value": str(pct(ratio2)) + "% — MET"},
    {"label": "b: Option 2 — classification",
     "value": "FINANCE — the 8-year term is 80% of the 10-year economic life (major part, >= 75%), "
              "and the PV of payments is 99.36% of fair value (substantially all, >= 90%). "
              "Meeting even one criterion is sufficient; two are met."},

    {"label": "b: Option 3 — PV factor, ordinary annuity, 6 yrs @ 5.5% (implicit rate, known)",
     "value": str(af3.quantize(D("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "b: Option 3 — PV of six $42,000 payments", "value": str(pv3_pmts)},
    {"label": "b: Option 3 — PV of $15,000 purchase-option price (single sum, 6 yrs @ 5.5%)",
     "value": str(pv3_opt)},
    {"label": "b: Option 3 — total PV of lease payments (payments + option price)",
     "value": str(pv3)},
    {"label": "b: Option 3 — PV as % of fair value $250,000 (90% test)",
     "value": str(pct(ratio3)) + "% — FAILS"},
    {"label": "b: Option 3 — lease term as % of 10-yr economic life (75% test)",
     "value": str(pct(term_pct_6)) + "% — FAILS"},
    {"label": "b: Option 3 — classification",
     "value": "FINANCE — the $15,000 option is far below the $55,000 expected fair value and "
              "Redrock is reasonably certain to exercise it, so the purchase-option criterion is "
              "met and classification is finance regardless of the other tests (term 60% and "
              "PV 88.28% both fail). The exercise price is included in the lease payments and "
              "the ROU asset is amortized over the 10-year ECONOMIC LIFE, not the 6-year term, "
              "because ownership is expected to transfer."},

    {"label": "b: Option 4 — PV factor, annuity DUE, 6 yrs @ 6% (IBR)",
     "value": str(af4.quantize(D("0.000001"), rounding=ROUND_HALF_UP))},
    {"label": "b: Option 4 — PV of lease payments ($45,000 x factor)", "value": str(pv4)},
    {"label": "b: Option 4 — PV as % of fair value $250,000 (90% test)",
     "value": str(pct(ratio4)) + "% — MET"},
    {"label": "b: Option 4 — lease term as % of 10-yr economic life (75% test)",
     "value": str(pct(term_pct_6)) + "% — FAILS"},
    {"label": "b: Option 4 — classification",
     "value": "FINANCE — the 90% test is met: PV of the beginning-of-year payments is "
              "$234,556.37, or 93.82% of the $250,000 fair value (substantially all). The larger "
              "payment plus the annuity-due timing is what pushes it over, even though the term "
              "is only 60% of economic life and there is no ownership transfer or purchase option."},

    {"label": "c: Case C — finance lease, Year 1 income statement (Option 2)",
     "value": "TWO expense lines, and total expense is FRONT-LOADED. (1) Amortization of the "
              "right-of-use asset, straight-line over the 8-year lease term, reported with "
              "operating/amortization expense; (2) Interest expense on the lease liability, "
              "computed by the effective-interest method on the declining liability balance and "
              "reported with interest/finance costs. Because interest is highest in Year 1 and "
              "declines, total Year 1 expense exceeds the cash payment and exceeds the "
              "straight-line amount; cash outflows split into operating (interest) and financing "
              "(principal) on the cash flow statement."},
    {"label": "c: Case C — operating lease, Year 1 income statement (warehouse)",
     "value": "ONE expense line: a single straight-line 'lease expense' equal to total lease "
              "payments divided by the lease term, reported entirely in operating expenses — no "
              "separate interest or amortization is shown. The amount is the SAME every year. "
              "Interest is still accreted on the liability internally, but ROU-asset amortization "
              "is the plug that forces the total to the straight-line amount, and the entire cash "
              "outflow is operating."},
    {"label": "c: Case C — the contrast in one sentence",
     "value": "Same total expense over the life of the lease, but the finance lease reports it as "
              "amortization plus interest on a decreasing pattern (more expense early, less late) "
              "while the operating lease reports one level amount each year — so early-year net "
              "income and operating income differ even though the cash paid is identical."},
]

out = {
    "id": "agent_150#02",
    "rounding_convention": "decimal.Decimal throughout; PV factors carried at 28 significant "
                           "digits with no intermediate rounding; each monetary result rounded "
                           "once to the cent (and each percentage to 0.01%) using ROUND_HALF_UP.",
    "answers": answers,
    "journal_entries": [],
    "insufficient_info": False,
    "notes": "Five criteria applied to every option: (1) ownership transfer, (2) purchase option "
             "reasonably certain of exercise, (3) term = major part (75%) of remaining economic "
             "life, (4) PV of lease payments + any residual value guarantee = substantially all "
             "(90%) of fair value, (5) specialized asset with no alternative use. Options 1, 3 "
             "and 4 use the 6-year term = 60% of the 10-year life; none of the four is a "
             "specialized asset and none transfers ownership outright. Option 3 uses the known "
             "5.5% implicit rate (a lessee must use the rate implicit in the lease when it is "
             "readily determinable); Options 1, 2 and 4 use the 6% incremental borrowing rate. "
             "Option 4's payments are an annuity due, so the ordinary-annuity factor is "
             "multiplied by 1.06."
}
print(json.dumps(out, indent=1))
