#!/usr/bin/env python3
"""Blind solver — Q1 CORE (LO 8-1): Summit Peak Manufacturing Co.

Cash / cash-equivalent / restricted-cash classification path:
initial recognition JEs, rolling classification schedule, Dec 31 NSF
reclass, Dec 31 classification schedule, balance-sheet totals.

ROUNDING CONVENTION
-------------------
All money is ``decimal.Decimal``; floats are never used.
Quantization is ROUND_HALF_UP to the cent (0.01) applied per computed
amount at the moment it is recorded (round-per-period, not round-at-end).
Every figure in this fact pattern resolves to an exact whole dollar, so
the rounding step never actually changes a value here -- it is applied
anyway so the derivation is convention-explicit and re-runnable.

No present-value work is required by this item, so no PV table factors
and no exact-formula discounting are involved.

The only rate applied is the 8% legally required compensating balance
(0.08 x $360,000 = $28,800).  The 7% note interest is NOT accrued: the
stem restricts the events to "classification-affecting only" and no
Required part asks for an interest accrual.  The commercial-paper
discount interest is given by the stem ($486), not rate-derived.

ACCOUNTING RULES APPLIED (Chapter 8, LO 8-1)
--------------------------------------------
* Cash equivalent = short-term, highly liquid, insignificant risk, and
  ORIGINAL maturity to the holder of three months or less.  A security
  bought with more than three months left to run is a short-term
  investment, not a cash equivalent, regardless of time remaining at
  the balance-sheet date.
* Legally restricted compensating balance -> separate restricted asset,
  classified current/noncurrent by the term of the related borrowing.
* Restricted cash is classified current or noncurrent by when the
  restricted funds will be used.
* NSF check -> reclassified out of cash back to Accounts Receivable.
* Postdated customer check -> Accounts Receivable (not immediately
  depositable).
* Employee travel advance -> other current asset (prepaid expense).
* Bank overdraft with NO offsetting positive balance at the same bank
  -> current liability (accounts payable); it may not be netted.

Run:  python3 solver.py   ->  prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(x) -> Decimal:
    """Money constructor: exact Decimal, quantized ROUND_HALF_UP to cents."""
    return Decimal(str(x)).quantize(CENT, rounding=ROUND_HALF_UP)


def q(d: Decimal) -> Decimal:
    """Re-quantize a computed Decimal, ROUND_HALF_UP to cents."""
    return d.quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-safe number: int when integral, else float of the cent value."""
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# GIVENS (transcribed from the stem; nothing below is a hard-coded result)
# ---------------------------------------------------------------------------

# Pre-October 1, Year 1 classification balances
OPEN_UNRESTRICTED = m(168_000)
OPEN_CASH_EQUIV = m(0)
OPEN_RESTR_CURR = m(0)
OPEN_RESTR_NONCURR = m(0)

# Event 1 - Oct 1 borrowing
NOTE_PRINCIPAL = m(360_000)
COMP_BAL_RATE = Decimal("0.08")          # 8% legally required
# Note term = one year from Oct 1, Y1 -> matures Oct 1, Y2 -> within 12
# months of the Dec 31, Y1 balance-sheet date -> restriction is CURRENT.
NOTE_RESTRICTION_IS_CURRENT = True

# Event 2 - Oct 15 commercial paper
CP_COST = m(54_000)
CP_TERM_DAYS = 45                        # original term to Summit Peak
CP_DISCOUNT_INTEREST = m(486)            # given by the stem

# Event 3 - Nov 20 T-bill
TBILL_NOV_COST = m(36_800)
TBILL_NOV_MONTHS_TO_MATURITY_AT_PURCHASE = 2

# Event 4 - Dec 5 dividend fund (dividends paid Jan 15, Y2 -> current)
DIVIDEND_FUND = m(14_200)

# Event 5 - Dec 12 bond sinking fund (bonds mature in 5 years -> noncurrent)
SINKING_FUND = m(63_500)

# December 31, Year 1 items on hand / on books
CRESTVIEW_CHECKING = m(76_400)           # includes the restricted comp balance
PRAIRIE_CHECKING = m(42_800)             # includes an NSF check
NSF_CHECK = m(1_150)
SAVINGS = m(18_600)
PETTY_CASH = m(650)
CASHIERS_CHECK = m(3_400)
MONEY_MARKET_FUND = m(33_000)            # original maturity 1 month, low risk
TBILL_AUG_COST = m(27_000)               # bought with 4 months left to run
TRAVEL_ADVANCE = m(2_250)
POSTDATED_CHECK = m(1_880)
REDROCK_OVERDRAFT = m(3_750)             # no other account at Redrock

CE_MAX_ORIGINAL_MATURITY_MONTHS = 3      # stated policy


def is_cash_equivalent(original_months: Decimal, low_risk: bool) -> bool:
    """Policy test: original maturity to Summit Peak <= 3 months AND low risk."""
    return low_risk and original_months <= CE_MAX_ORIGINAL_MATURITY_MONTHS


# ---------------------------------------------------------------------------
# DERIVED AMOUNTS
# ---------------------------------------------------------------------------

# (a) legally required compensating balance
COMP_BALANCE = q(NOTE_PRINCIPAL * COMP_BAL_RATE)          # 360,000 x 8%

# (c) commercial-paper maturity proceeds
CP_PROCEEDS = q(CP_COST + CP_DISCOUNT_INTEREST)

# Cash-equivalent qualification tests (derived, not asserted)
CP_IS_CE = is_cash_equivalent(
    Decimal(CP_TERM_DAYS) / Decimal(30), True)            # 45 days = 1.5 months
TBILL_NOV_IS_CE = is_cash_equivalent(
    Decimal(TBILL_NOV_MONTHS_TO_MATURITY_AT_PURCHASE), True)
TBILL_AUG_IS_CE = is_cash_equivalent(Decimal(4), True)    # 4 months -> False
MMF_IS_CE = is_cash_equivalent(Decimal(1), True)

# Crestview presentation split
CRESTVIEW_UNRESTRICTED = q(CRESTVIEW_CHECKING - COMP_BALANCE)

# Prairie after the Dec 31 NSF reclass
PRAIRIE_AFTER_NSF = q(PRAIRIE_CHECKING - NSF_CHECK)


# ---------------------------------------------------------------------------
# PARTS (a)-(d), (f): JOURNAL ENTRIES
# ---------------------------------------------------------------------------

def entry(part, date, description, lines):
    out = {"part": part, "date": date, "description": description, "lines": []}
    for account, debit, credit in lines:
        out["lines"].append(
            {"account": account, "debit": num(debit), "credit": num(credit)}
        )
    return out


journal_entries = [
    # (a) borrowing
    entry("a", "Year 1 October 1",
          "Borrowed on a one-year, 7% note payable; full proceeds deposited "
          "at Crestview National Bank.",
          [("Cash", NOTE_PRINCIPAL, m(0)),
           ("Notes Payable", m(0), NOTE_PRINCIPAL)]),
    # (a) initial-recognition reclass of the legally restricted comp balance
    entry("a", "Year 1 October 1",
          "Initial recognition reclassification of the legally restricted 8% "
          "compensating balance out of unrestricted cash.",
          [("Restricted Cash-Compensating Balance (current asset)",
            COMP_BALANCE, m(0)),
           ("Cash", m(0), COMP_BALANCE)]),
    # (b) commercial paper purchase
    entry("b", "Year 1 October 15",
          "Purchased 45-day commercial paper; qualifies as a cash equivalent "
          "under the three-month original-maturity policy.",
          [("Cash Equivalents-Commercial Paper", CP_COST, m(0)),
           ("Cash", m(0), CP_COST)]),
    # (c) commercial paper maturity / settlement
    entry("c", "Year 1 November 29",
          "Commercial paper matured; discount interest earned.",
          [("Cash", CP_PROCEEDS, m(0)),
           ("Cash Equivalents-Commercial Paper", m(0), CP_COST),
           ("Interest Revenue", m(0), CP_DISCOUNT_INTEREST)]),
    # (d) T-bill purchase
    entry("d", "Year 1 November 20",
          "Purchased U.S. Treasury bill with two months remaining to "
          "maturity; cash equivalent.",
          [("Cash Equivalents-U.S. Treasury Bill", TBILL_NOV_COST, m(0)),
           ("Cash", m(0), TBILL_NOV_COST)]),
    # (d) dividend fund transfer
    entry("d", "Year 1 December 5",
          "Transferred general cash to the restricted dividend fund "
          "(dividends payable January 15, Year 2 -> current).",
          [("Restricted Cash-Dividend Fund (current asset)",
            DIVIDEND_FUND, m(0)),
           ("Cash", m(0), DIVIDEND_FUND)]),
    # (d) bond sinking fund deposit
    entry("d", "Year 1 December 12",
          "Deposited cash with a trustee for the bond sinking fund; related "
          "bonds mature in five years -> noncurrent.",
          [("Restricted Cash-Bond Sinking Fund (noncurrent asset)",
            SINKING_FUND, m(0)),
           ("Cash", m(0), SINKING_FUND)]),
    # (f) period-end NSF reclass
    entry("f", "Year 1 December 31",
          "Period-end reclassifying entry: NSF check returned; remove from "
          "cash and reinstate the customer receivable.",
          [("Accounts Receivable", NSF_CHECK, m(0)),
           ("Cash", m(0), NSF_CHECK)]),
]

# Self-check: debits must equal credits in every entry.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"Unbalanced entry in part {je['part']}: {dr} vs {cr}"


# ---------------------------------------------------------------------------
# PART (e): ROLLING CLASSIFICATION SCHEDULE
# ---------------------------------------------------------------------------
# Columns: Unrestricted cash | Cash equivalents | Restricted-current |
#          Restricted-noncurrent.  Only the listed events move the columns.

unr, ce, rc_c, rc_nc = (OPEN_UNRESTRICTED, OPEN_CASH_EQUIV,
                        OPEN_RESTR_CURR, OPEN_RESTR_NONCURR)

schedule_rows = [{
    "point": "Immediately before October 1, Year 1 (opening)",
    "unrestricted_cash": num(unr), "cash_equivalents": num(ce),
    "restricted_cash_current": num(rc_c),
    "restricted_cash_noncurrent": num(rc_nc),
}]


def roll(point, d_unr=m(0), d_ce=m(0), d_rc_c=m(0), d_rc_nc=m(0)):
    global unr, ce, rc_c, rc_nc
    unr, ce = q(unr + d_unr), q(ce + d_ce)
    rc_c, rc_nc = q(rc_c + d_rc_c), q(rc_nc + d_rc_nc)
    schedule_rows.append({
        "point": point,
        "unrestricted_cash": num(unr), "cash_equivalents": num(ce),
        "restricted_cash_current": num(rc_c),
        "restricted_cash_noncurrent": num(rc_nc),
    })


# Oct 1 - borrowing proceeds in, then the legally restricted portion out.
roll("After October 1, Year 1 (borrowing + compensating-balance reclass)",
     d_unr=q(NOTE_PRINCIPAL - COMP_BALANCE),
     d_rc_c=COMP_BALANCE if NOTE_RESTRICTION_IS_CURRENT else m(0),
     d_rc_nc=m(0) if NOTE_RESTRICTION_IS_CURRENT else COMP_BALANCE)

# Oct 15 - commercial paper purchased (cash -> cash equivalents).
roll("After October 15, Year 1 (commercial paper purchased)",
     d_unr=-CP_COST, d_ce=CP_COST if CP_IS_CE else m(0))

# Nov 20 - T-bill purchased (cash -> cash equivalents).
roll("After November 20, Year 1 (T-bill purchased)",
     d_unr=-TBILL_NOV_COST,
     d_ce=TBILL_NOV_COST if TBILL_NOV_IS_CE else m(0))

# Nov 29 - commercial paper matures; principal + interest land in cash.
roll("After November 29, Year 1 (commercial paper matured)",
     d_unr=CP_PROCEEDS, d_ce=-CP_COST if CP_IS_CE else m(0))

# Dec 5 - dividend fund segregated (current restriction).
roll("After December 5, Year 1 (dividend fund segregated)",
     d_unr=-DIVIDEND_FUND, d_rc_c=DIVIDEND_FUND)

# Dec 12 - bond sinking fund deposited with trustee (noncurrent restriction).
roll("After December 12, Year 1 (bond sinking fund deposited)",
     d_unr=-SINKING_FUND, d_rc_nc=SINKING_FUND)


# ---------------------------------------------------------------------------
# PART (g): DECEMBER 31 CLASSIFICATION SCHEDULE (after the NSF reclass)
# ---------------------------------------------------------------------------

CASH = "Cash"
CE = "Cash equivalents"
RC_C = "Restricted cash-current"
RC_NC = "Restricted cash-noncurrent"
AR = "Accounts receivable (not cash)"
STI = "Short-term investment (not a cash equivalent)"
OCA = "Other current asset - prepaid (not cash)"
CL = "Current liability (not netted against cash)"

classification_rows = [
    {"item": "Checking-Crestview National - unrestricted portion",
     "amount": num(CRESTVIEW_UNRESTRICTED), "classification": CASH,
     "reason": "$76,400 account balance less the $28,800 legally restricted "
               "compensating balance."},
    {"item": "Checking-Crestview National - legally restricted compensating "
             "balance",
     "amount": num(COMP_BALANCE), "classification": RC_C,
     "reason": "Legally restricted; the related note matures October 1, "
               "Year 2, so the restriction is current."},
    {"item": "Checking-Prairie Credit Union - after NSF reclass",
     "amount": num(PRAIRIE_AFTER_NSF), "classification": CASH,
     "reason": "$42,800 less the $1,150 NSF check reclassified in part (f)."},
    {"item": "NSF check from customer (removed from Prairie balance)",
     "amount": num(NSF_CHECK), "classification": AR,
     "reason": "Uncollected; reinstated as a customer receivable."},
    {"item": "Savings account", "amount": num(SAVINGS), "classification": CASH,
     "reason": "Deposit with a financial institution, available on demand."},
    {"item": "Petty cash", "amount": num(PETTY_CASH), "classification": CASH,
     "reason": "Coin and currency on hand."},
    {"item": "Cashier's check payable to Summit Peak (dated Dec 29)",
     "amount": num(CASHIERS_CHECK), "classification": CASH,
     "reason": "Cashier's check on hand is cash even though not yet "
               "deposited."},
    {"item": "U.S. T-bill purchased November 20 (2 months to maturity)",
     "amount": num(TBILL_NOV_COST),
     "classification": CE if TBILL_NOV_IS_CE else STI,
     "reason": "Original maturity to Summit Peak of two months, low risk."},
    {"item": "Money market fund (original maturity 1 month, low risk)",
     "amount": num(MONEY_MARKET_FUND),
     "classification": CE if MMF_IS_CE else STI,
     "reason": "Highly liquid, insignificant risk, original maturity under "
               "three months."},
    {"item": "Restricted cash-dividend fund (segregated Dec 5)",
     "amount": num(DIVIDEND_FUND), "classification": RC_C,
     "reason": "Dividends are paid January 15, Year 2 - used within one "
               "year."},
    {"item": "Restricted cash-bond sinking fund (segregated Dec 12)",
     "amount": num(SINKING_FUND), "classification": RC_NC,
     "reason": "Related bonds mature in five years."},
    {"item": "T-bill purchased August 1 with 4 months remaining",
     "amount": num(TBILL_AUG_COST),
     "classification": CE if TBILL_AUG_IS_CE else STI,
     "reason": "Original maturity to Summit Peak exceeded three months, so "
               "it fails the cash-equivalent policy."},
    {"item": "Travel advance to employee for January trip",
     "amount": num(TRAVEL_ADVANCE), "classification": OCA,
     "reason": "Advance for future business travel; a prepaid expense, not "
               "cash."},
    {"item": "Customer check dated January 12, Year 2 (postdated)",
     "amount": num(POSTDATED_CHECK), "classification": AR,
     "reason": "Not available for immediate deposit."},
    {"item": "Overdraft at Redrock Bank (no other Redrock account)",
     "amount": num(REDROCK_OVERDRAFT), "classification": CL,
     "reason": "No offsetting positive balance at the same bank, so the "
               "negative balance is reported as a liability."},
]


def total_for(label: str) -> Decimal:
    t = m(0)
    for row in classification_rows:
        if row["classification"] == label:
            t = q(t + m(row["amount"]))
    return t


# ---------------------------------------------------------------------------
# PART (h): BALANCE-SHEET TOTALS
# ---------------------------------------------------------------------------

TOTAL_CASH = total_for(CASH)
TOTAL_CE = total_for(CE)
TOTAL_RC_C = total_for(RC_C)
TOTAL_RC_NC = total_for(RC_NC)
TOTAL_OVERDRAFT_LIAB = total_for(CL)

# Internal consistency: every year-end item must land in exactly one bucket.
_assigned = q(sum((m(r["amount"]) for r in classification_rows), m(0)))
_listed = q(CRESTVIEW_CHECKING + PRAIRIE_CHECKING + SAVINGS + PETTY_CASH
            + CASHIERS_CHECK + TBILL_NOV_COST + MONEY_MARKET_FUND
            + DIVIDEND_FUND + SINKING_FUND + TBILL_AUG_COST + TRAVEL_ADVANCE
            + POSTDATED_CHECK + REDROCK_OVERDRAFT)
assert _assigned == _listed, f"Schedule does not tie: {_assigned} vs {_listed}"


# ---------------------------------------------------------------------------
# ANSWERS (only figures the Required parts ask for)
# ---------------------------------------------------------------------------

answers = []

# (e) rolling schedule
for row in schedule_rows:
    for key, col in (("unrestricted_cash", "Unrestricted cash"),
                     ("cash_equivalents", "Cash equivalents"),
                     ("restricted_cash_current", "Restricted cash-current"),
                     ("restricted_cash_noncurrent",
                      "Restricted cash-noncurrent")):
        answers.append({"label": f"e: {row['point']} - {col}",
                        "value": row[key]})

# (g) December 31 classification schedule
for row in classification_rows:
    answers.append({
        "label": f"g: {row['item']} -> {row['classification']}",
        "value": row["amount"],
    })

# (h) balance-sheet totals
answers.extend([
    {"label": "h: Cash (balance-sheet total, Dec 31 Year 1)",
     "value": num(TOTAL_CASH)},
    {"label": "h: Cash equivalents (balance-sheet total, Dec 31 Year 1)",
     "value": num(TOTAL_CE)},
    {"label": "h: Restricted cash-current (Dec 31 Year 1)",
     "value": num(TOTAL_RC_C)},
    {"label": "h: Restricted cash-noncurrent (Dec 31 Year 1)",
     "value": num(TOTAL_RC_NC)},
    {"label": "h: Current liability from the Redrock bank overdraft",
     "value": num(TOTAL_OVERDRAFT_LIAB)},
])


NOTES = (
    "(i) If the compensating balance had NOT been legally restricted, no "
    "reclassification would be made: the $28,800 would stay inside the "
    "Crestview checking balance and be reported with Cash (Cash would then "
    "be $140,700). Under ASC 210-10-S99-1 the arrangement would instead be "
    "described in the notes to the financial statements, disclosing the "
    "nature and terms of the compensating-balance arrangement and the amount "
    "involved; compensating balances maintained to ensure future credit "
    "availability are likewise note-disclosed with their amount and terms. "
    "| Part (e) rolls only the listed classification events, as instructed, "
    "so it does not tie to the separate Dec 31 item table in part (g). "
    "| The 7% note interest is not accrued: the stem limits the events to "
    "classification-affecting ones and no Required part asks for it. "
    "| The Aug 1 T-bill ($27,000) fails the three-month ORIGINAL-maturity "
    "policy and is a short-term investment, excluded from cash equivalents."
)

result = {
    "id": "agent_301#00",
    "rounding_convention": (
        "decimal.Decimal throughout, never floats; ROUND_HALF_UP quantized "
        "to the cent per computed amount (round-per-period, not at end). "
        "All figures here are exact whole dollars, so no rounding is "
        "actually invoked. No PV work required, so no table factors used."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": NOTES,
}

print(json.dumps(result, indent=2))
