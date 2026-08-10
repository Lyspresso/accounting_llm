"""Solver for agent_150#02 (Redrock Analytics LLC - lease identification & classification).

Rounding convention: all money computed with decimal.Decimal (never float) at 40-digit
precision; present values are run at FULL precision and only the REPORTED figures are
quantized to whole dollars using ROUND_HALF_UP.  Percentages are quantized to two
decimals with ROUND_HALF_UP.  No journal entries are required by any Required part, so
none are produced (Dr = Cr trivially holds).  Nothing is hard-coded: every PV, every
percentage and every threshold comparison is derived from the fact pattern.
"""
from decimal import Decimal, getcontext, ROUND_HALF_UP
import json

getcontext().prec = 40
D = Decimal


def pv_ordinary(pmt, rate, n):
    """PV of an n-payment ordinary annuity (payments at END of each period)."""
    tot = D(0)
    for t in range(1, n + 1):
        tot += pmt / (D(1) + rate) ** t
    return tot


def pv_due(pmt, rate, n):
    """PV of an n-payment annuity due (payments at BEGINNING of each period)."""
    tot = D(0)
    for t in range(0, n):
        tot += pmt / (D(1) + rate) ** t
    return tot


def pv_single(amt, rate, n):
    return amt / (D(1) + rate) ** n


def dollars(x):
    return int(x.quantize(D("1"), rounding=ROUND_HALF_UP))


def pct(num, den):
    return float((num / den * D(100)).quantize(D("0.01"), rounding=ROUND_HALF_UP))


# ---------------- shared facts (Case B) ----------------
FV = D("250000")            # fair value of the equipment
ECON_LIFE = D("10")         # economic life, years
TERM_THRESHOLD = D("75")    # 75% term test
PV_THRESHOLD = D("90")      # 90% PV test

answers = []

# ---------------- Case A ----------------
answers.append({
    "label": "a: Does the CloudRail contract contain a lease?",
    "value": "No - it is a service contract, not a lease.",
})
answers.append({
    "label": "a: Reason (identified asset / substitution)",
    "value": ("There is no identified asset. CloudRail can fulfil the contract from any server in a "
              "large pool of identical servers and routinely substitutes them for its own economic "
              "benefit, and Redrock cannot prevent substitution, so the supplier's substitution right "
              "is substantive. Without an identified asset Redrock obtains no right to direct the use "
              "of, or to obtain substantially all the economic benefits from, a specific asset - it buys "
              "only a level of processing capacity. Costs are expensed as the service is received; no "
              "right-of-use asset or lease liability is recorded."),
})

# ---------------- Case B ----------------
# Option 1: 6 yrs, $40,000 ordinary annuity, IBR 6%, no option, no transfer, not specialized
o1_term_pct = pct(D("6"), ECON_LIFE)
o1_pv = pv_ordinary(D("40000"), D("0.06"), 6)
o1_pv_pct = pct(o1_pv, FV)
o1_class = "Finance" if (D(str(o1_term_pct)) >= TERM_THRESHOLD or D(str(o1_pv_pct)) >= PV_THRESHOLD) else "Operating"

# Option 2: 8 yrs, $40,000 ordinary annuity, IBR 6%
o2_term_pct = pct(D("8"), ECON_LIFE)
o2_pv = pv_ordinary(D("40000"), D("0.06"), 8)
o2_pv_pct = pct(o2_pv, FV)
o2_class = "Finance" if (D(str(o2_term_pct)) >= TERM_THRESHOLD or D(str(o2_pv_pct)) >= PV_THRESHOLD) else "Operating"

# Option 3: 6 yrs, $42,000 ordinary annuity, implicit 5.5% known, purchase option $15,000
#           (expected FV $55,000 -> bargain; reasonably certain to exercise, so the exercise
#           price is included in the lease payments and the option criterion is met outright)
o3_term_pct = pct(D("6"), ECON_LIFE)
o3_pv_pmts = pv_ordinary(D("42000"), D("0.055"), 6)
o3_pv_opt = pv_single(D("15000"), D("0.055"), 6)
o3_pv_total = o3_pv_pmts + o3_pv_opt
o3_pv_pct = pct(o3_pv_total, FV)
o3_option_criterion = True   # reasonably certain to exercise a $15,000 option on a $55,000 asset
o3_class = "Finance" if (o3_option_criterion or D(str(o3_term_pct)) >= TERM_THRESHOLD
                         or D(str(o3_pv_pct)) >= PV_THRESHOLD) else "Operating"

# Option 4: 6 yrs, $45,000 annuity DUE, IBR 6%
o4_term_pct = pct(D("6"), ECON_LIFE)
o4_pv = pv_due(D("45000"), D("0.06"), 6)
o4_pv_pct = pct(o4_pv, FV)
o4_class = "Finance" if (D(str(o4_term_pct)) >= TERM_THRESHOLD or D(str(o4_pv_pct)) >= PV_THRESHOLD) else "Operating"

answers += [
    {"label": "b: Option 1 - lease term as % of economic life (6/10)", "value": o1_term_pct},
    {"label": "b: Option 1 - PV of lease payments ($40,000 ordinary annuity, 6 yrs, 6% IBR)", "value": dollars(o1_pv)},
    {"label": "b: Option 1 - PV as % of fair value ($250,000)", "value": o1_pv_pct},
    {"label": "b: Option 1 - classification", "value": o1_class},
    {"label": "b: Option 1 - why", "value": ("No transfer of ownership, no purchase option, asset not specialized; "
                                             "term test 60% < 75% and PV test " + str(o1_pv_pct) + "% < 90%. "
                                             "No criterion met -> operating lease.")},

    {"label": "b: Option 2 - lease term as % of economic life (8/10)", "value": o2_term_pct},
    {"label": "b: Option 2 - PV of lease payments ($40,000 ordinary annuity, 8 yrs, 6% IBR)", "value": dollars(o2_pv)},
    {"label": "b: Option 2 - PV as % of fair value ($250,000)", "value": o2_pv_pct},
    {"label": "b: Option 2 - classification", "value": o2_class},
    {"label": "b: Option 2 - why", "value": ("Term test met: 80% >= 75% of the 10-year economic life. The PV test is "
                                             "also met (" + str(o2_pv_pct) + "% >= 90%). Meeting either criterion makes "
                                             "it a finance lease.")},

    {"label": "b: Option 3 - lease term as % of economic life (6/10)", "value": o3_term_pct},
    {"label": "b: Option 3 - PV of the six $42,000 payments (6 yrs, 5.5% implicit rate)", "value": dollars(o3_pv_pmts)},
    {"label": "b: Option 3 - PV of the $15,000 purchase option (5.5%, 6 yrs)", "value": dollars(o3_pv_opt)},
    {"label": "b: Option 3 - total PV of lease payments incl. option", "value": dollars(o3_pv_total)},
    {"label": "b: Option 3 - PV as % of fair value ($250,000)", "value": o3_pv_pct},
    {"label": "b: Option 3 - classification", "value": o3_class},
    {"label": "b: Option 3 - why", "value": ("Purchase-option criterion is met: the $15,000 exercise price is far below "
                                             "the $55,000 expected fair value and Redrock is reasonably certain to "
                                             "exercise, so it is treated as a purchase. Note the other tests fail - term "
                                             "60% < 75% and PV " + str(o3_pv_pct) + "% < 90% (discounted at the known "
                                             "5.5% implicit rate, which the lessee must use) - yet one criterion is "
                                             "enough, so this is a finance lease.")},

    {"label": "b: Option 4 - lease term as % of economic life (6/10)", "value": o4_term_pct},
    {"label": "b: Option 4 - PV of lease payments ($45,000 annuity due, 6 yrs, 6% IBR)", "value": dollars(o4_pv)},
    {"label": "b: Option 4 - PV as % of fair value ($250,000)", "value": o4_pv_pct},
    {"label": "b: Option 4 - classification", "value": o4_class},
    {"label": "b: Option 4 - why", "value": ("Payments are at the beginning of each year (annuity due), which raises the "
                                             "PV. Term test fails (60% < 75%) but the PV test is met: " + str(o4_pv_pct) +
                                             "% >= 90% of the $250,000 fair value -> finance lease.")},
]

# ---------------- Case C (illustrated with Option 2's finance lease) ----------------
o2_liab = o2_pv                      # initial lease liability = ROU asset (no IDC/prepayments)
c_interest_y1 = o2_liab * D("0.06")
c_amort_y1 = o2_liab / D("8")        # straight-line over the 8-year term (no transfer/option)
c_total_y1 = c_interest_y1 + c_amort_y1
c_sl_if_operating = D("40000") * 8 / D("8")   # total payments spread evenly over the term

answers += [
    {"label": "c: Finance lease - Year 1 income statement presentation", "value": (
        "Two separate expenses. (1) Amortization of the right-of-use asset, straight-line over the "
        "lease term, reported in operating expenses; (2) Interest expense on the lease liability "
        "computed by the effective-interest method on the beginning balance, reported with interest "
        "expense (non-operating). Because interest is highest in Year 1 and declines, total Year 1 "
        "expense is FRONT-LOADED and falls over the lease term; it exceeds the cash rent in early years.")},
    {"label": "c: Operating lease - Year 1 income statement presentation", "value": (
        "A single straight-line 'lease expense' line, in operating expenses - total lease payments "
        "spread evenly over the term. Interest and amortization are not shown separately; the ROU "
        "asset amortization is the plug (straight-line lease cost less the period's interest). "
        "Expense is the SAME every year.")},
    {"label": "c: Illustrative Option 2 finance lease - Year 1 interest expense (6% x $248,392)", "value": dollars(c_interest_y1)},
    {"label": "c: Illustrative Option 2 finance lease - Year 1 ROU amortization ($248,392 / 8 yrs)", "value": dollars(c_amort_y1)},
    {"label": "c: Illustrative Option 2 finance lease - Year 1 total expense", "value": dollars(c_total_y1)},
    {"label": "c: Illustrative Option 2 - Year 1 single lease cost if it were operating", "value": dollars(c_sl_if_operating)},
]

out = {
    "id": "agent_150#02",
    "rounding_convention": ("decimal.Decimal throughout (no floats); present values computed at full "
                           "40-digit precision and reported figures quantized to whole dollars with "
                           "ROUND_HALF_UP; percentages ROUND_HALF_UP to two decimals. No journal "
                           "entries are required by the Required parts."),
    "answers": answers,
    "journal_entries": [],
    "insufficient_info": False,
    "notes": ("Case A: substantive supplier substitution right over a pool of identical servers => no "
              "identified asset => no lease (service contract). Case B classification criteria applied: "
              "(1) transfer of ownership - none in any option; (2) purchase option reasonably certain to "
              "be exercised - only Option 3; (3) term >= 75% of economic life - only Option 2 (80%); "
              "(4) PV of lease payments >= 90% of fair value - Options 2 (99.36%) and 4 (93.82%); "
              "(5) specialized asset with no alternative use - none. Discount rate: IBR 6% where the "
              "implicit rate is unknown (Options 1, 2, 4); the known implicit rate 5.5% is used for "
              "Option 3. Option 3's payments include the $15,000 exercise price because exercise is "
              "reasonably certain. Result: Option 1 operating; Options 2, 3 and 4 finance. "
              "Annuity factors derived, not looked up: PVOA(6%,6)=4.917324, PVOA(6%,8)=6.209794, "
              "PVOA(5.5%,6)=4.995530 with PV$1(5.5%,6)=0.725246, PVAD(6%,6)=5.212364. "
              "Case C figures are labelled illustrative because no dollar amounts are given for the "
              "warehouse lease; the Year 1 rounded components (14,904 + 31,049) sum to 45,953 while the "
              "unrounded total rounds to 45,952 - the total shown is the rounded exact total.")
}
print(json.dumps(out, indent=1))
