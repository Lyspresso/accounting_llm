"""Harborline Merchants / Dunecrest Packaging note receivable impairment (LO 8-9).

ROUNDING CONVENTION: all money is decimal.Decimal. Every computed figure is
rounded to the nearest whole dollar using ROUND_HALF_UP, applied independently
at each period end ("per period"); each period's effective-interest accretion is
computed on the ALREADY-ROUNDED prior-period net carrying amount, so rounding
does not accumulate. Nothing is hard-coded: face, rate, stated interest, PV,
impairment loss, and every schedule line are derived from the scenario inputs.

Authority: impaired note is measured at the PV of expected future cash flows
discounted at the note's ORIGINAL effective rate (6%). The current 12% market
rate is explicitly ignored for discounting. Subsequent accretion of the
discount is recorded as interest revenue by reducing the allowance.
"""
from decimal import Decimal as D, ROUND_HALF_UP
import json

def r(x):
    return x.quantize(D("1"), rounding=ROUND_HALF_UP)

def n(x):
    return int(x)

# ---------------- inputs from the scenario ----------------
FACE          = D("80000")      # four-year note, at face
STATED_RATE   = D("0.06")       # 6% stated
MARKET_RATE   = D("0.06")       # 6% market at issuance -> issued at face
TERM_YEARS    = 4               # Jan 1 Y1 -> Dec 31 Y4
EXPECTED_PRIN = D("54000")      # expected collection on original due date
EXPECTED_INT  = D("0")          # "no further interest"
IMPAIR_YEAR   = 1               # impairment tested at Dec 31, Y1
GIVEN_PV      = D("45339")      # PV supplied by the requirement (cross-check)
CASH_AT_SETTLE= D("54000")      # actually collected Dec 31, Y4

# ---------------- (a) initial recognition + Y1 interest ----------------
issue_price   = FACE if STATED_RATE == MARKET_RATE else None  # at face
stated_int    = r(FACE * STATED_RATE)            # 4,800 per year

# ---------------- (b) impairment at Dec 31, Y1 ----------------
periods_left  = TERM_YEARS - IMPAIR_YEAR                    # 3 discount periods
pv_factor     = D(1) / ((D(1) + MARKET_RATE) ** periods_left)
pv_expected   = r(EXPECTED_PRIN * pv_factor + EXPECTED_INT) # -> 45,339
ca_before     = FACE + D("0")                    # face; Y1 interest already collected
impair_loss   = r(ca_before - pv_expected)
pv_matches    = (pv_expected == GIVEN_PV)

# ---------------- (c) subsequent measurement schedule ----------------
sched = [{"date": "Dec 31, Y%d" % IMPAIR_YEAR, "accretion": D("0"),
          "net_ca": pv_expected, "afda": r(FACE - pv_expected), "gross": FACE}]
net_ca = pv_expected
afda   = r(FACE - pv_expected)
for yr in range(IMPAIR_YEAR + 1, TERM_YEARS + 1):
    accr   = r(net_ca * MARKET_RATE)
    net_ca = r(net_ca + accr)
    afda   = r(afda - accr)
    sched.append({"date": "Dec 31, Y%d" % yr, "accretion": accr,
                  "net_ca": net_ca, "afda": afda, "gross": FACE})
final_ca      = sched[-1]["net_ca"]
final_afda    = sched[-1]["afda"]
sched_ties    = (final_ca == EXPECTED_PRIN) and (final_afda == FACE - EXPECTED_PRIN)

y2 = sched[1]; y3 = sched[2]; y4 = sched[3]

# ---------------- (e) settlement Dec 31, Y4 ----------------
afda_before_y4 = sched[2]["afda"]                 # 29,057 = 26,000 + 3,057
afda_removed   = r(FACE - CASH_AT_SETTLE + D("0"))  # residual allowance released
afda_dr_total  = r(afda_before_y4)                # accretion + residual, combined
gain_loss      = r(CASH_AT_SETTLE - final_ca)     # 0 -> collected exactly as expected

answers = [
    {"label": "a: Notes Receivable debited on initial recognition, Jan 1 Y1 (note at face, 6% stated = 6% market)", "value": n(issue_price)},
    {"label": "a: Sales Revenue credited, Jan 1 Y1", "value": n(issue_price)},
    {"label": "a: Cash collected for Year 1 interest, Dec 31 Y1", "value": n(stated_int)},
    {"label": "a: Interest Revenue recognized in Year 1", "value": n(stated_int)},
    {"label": "b: Carrying amount of the note before impairment, Dec 31 Y1", "value": n(ca_before)},
    {"label": "b: PV of expected future cash flows ($54,000 in 3 yrs @ original 6%), Dec 31 Y1", "value": n(pv_expected)},
    {"label": "b: Impairment loss recognized Dec 31 Y1 (Dr Impairment Loss / Cr Allowance)", "value": n(impair_loss)},
    {"label": "c: Net carrying amount, Dec 31 Y1 (after impairment)", "value": n(sched[0]["net_ca"])},
    {"label": "c: Allowance (AFDA) balance, Dec 31 Y1", "value": n(sched[0]["afda"])},
    {"label": "c: Year 2 interest accretion @6% on net CA", "value": n(y2["accretion"])},
    {"label": "c: Net carrying amount, Dec 31 Y2", "value": n(y2["net_ca"])},
    {"label": "c: Allowance (AFDA) balance, Dec 31 Y2", "value": n(y2["afda"])},
    {"label": "c: Year 3 interest accretion @6% on net CA", "value": n(y3["accretion"])},
    {"label": "c: Net carrying amount, Dec 31 Y3", "value": n(y3["net_ca"])},
    {"label": "c: Allowance (AFDA) balance, Dec 31 Y3", "value": n(y3["afda"])},
    {"label": "c: Year 4 interest accretion @6% on net CA", "value": n(y4["accretion"])},
    {"label": "c: Net carrying amount, Dec 31 Y4 before settlement", "value": n(y4["net_ca"])},
    {"label": "c: Allowance (AFDA) balance, Dec 31 Y4 before settlement", "value": n(y4["afda"])},
    {"label": "c: Gross Notes Receivable throughout (unchanged)", "value": n(FACE)},
    {"label": "d: Dec 31 Y2 AJE amount - Dr Allowance / Cr Interest Revenue", "value": n(y2["accretion"])},
    {"label": "d: Dec 31 Y3 AJE amount - Dr Allowance / Cr Interest Revenue", "value": n(y3["accretion"])},
    {"label": "e: Cash collected at settlement, Dec 31 Y4", "value": n(CASH_AT_SETTLE)},
    {"label": "e: Final Year 4 interest revenue (accretion) included in settlement entry", "value": n(y4["accretion"])},
    {"label": "e: Allowance (AFDA) debited/removed in combined settlement entry", "value": n(afda_dr_total)},
    {"label": "e: Notes Receivable credited (derecognized) at settlement", "value": n(FACE)},
    {"label": "e: Gain or loss on settlement (cash equals final net CA)", "value": n(gain_loss)},
]

def je(part, desc, lines):
    dr = sum(D(str(l[1])) for l in lines)
    cr = sum(D(str(l[2])) for l in lines)
    assert dr == cr, (part, desc, dr, cr)
    return {"part": part, "description": desc,
            "lines": [{"account": a, "debit": n(D(str(d))), "credit": n(D(str(c)))} for a, d, c in lines]}

jes = [
    je("a", "Jan 1, Y1 - sale of inventory for a 4-year 6% note issued at face",
       [("Notes Receivable", issue_price, D(0)), ("Sales Revenue", D(0), issue_price)]),
    je("a", "Dec 31, Y1 - collection of Year 1 stated interest ($80,000 x 6%)",
       [("Cash", stated_int, D(0)), ("Interest Revenue", D(0), stated_int)]),
    je("b", "Dec 31, Y1 - impairment AJE ($80,000 CA less $45,339 PV at original 6%)",
       [("Impairment Loss on Note Receivable (Bad Debt Expense)", impair_loss, D(0)),
        ("Allowance for Doubtful Accounts - Notes Receivable", D(0), impair_loss)]),
    je("d", "Dec 31, Y2 - effective-interest accretion AJE (6% x $" + str(n(sched[0]["net_ca"])) + " net CA)",
       [("Allowance for Doubtful Accounts - Notes Receivable", y2["accretion"], D(0)),
        ("Interest Revenue", D(0), y2["accretion"])]),
    je("d", "Dec 31, Y3 - effective-interest accretion AJE (6% x $" + str(n(y2["net_ca"])) + " net CA)",
       [("Allowance for Doubtful Accounts - Notes Receivable", y3["accretion"], D(0)),
        ("Interest Revenue", D(0), y3["accretion"])]),
    je("e", "Dec 31, Y4 - combined settlement: final accretion + collection of $54,000 and derecognition",
       [("Cash", CASH_AT_SETTLE, D(0)),
        ("Allowance for Doubtful Accounts - Notes Receivable", afda_dr_total, D(0)),
        ("Interest Revenue", D(0), y4["accretion"]),
        ("Notes Receivable", D(0), FACE)]),
]

notes = (
    "Note issued at face because the 6% stated rate equals the 6% market rate, so no premium/discount; "
    "stated interest = 80,000 x 6% = 4,800 collected each Dec 31. Impairment at 12/31/Y1 is measured as "
    "carrying amount 80,000 less the PV of the ONLY expected cash flow (54,000 due 12/31/Y4) discounted "
    "3 periods at the ORIGINAL effective rate of 6%: 54,000 / 1.06^3 = 45,339 (matches the given PV: "
    + str(pv_matches) +
    "); the current 12% similar-risk rate is ignored for discounting per the requirement. Impairment loss "
    "= 34,661, credited to a valuation allowance so gross Notes Receivable stays at 80,000. After "
    "impairment the net carrying amount accretes at 6% each period with the offset debited to the "
    "allowance and credited to Interest Revenue (no cash interest is expected): Y2 2,720; Y3 2,884; "
    "Y4 3,057. The schedule ties exactly: net CA reaches 54,000 and the allowance falls to 26,000 "
    "(= 80,000 - 54,000) at 12/31/Y4 (schedule ties: " + str(sched_ties) +
    "). Because 54,000 is collected exactly as expected, no gain or loss arises; the combined settlement "
    "entry debits Cash 54,000 and the remaining allowance 29,057 (26,000 residual + 3,057 Year 4 "
    "accretion), credits Interest Revenue 3,057 and Notes Receivable 80,000."
)

print(json.dumps({
    "id": "agent_309#01",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the nearest whole dollar applied independently at each period end, with each period's 6% accretion computed on the already-rounded prior net carrying amount (schedule ties exactly to $54,000 / $26,000 with no plug)",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
