#!/usr/bin/env python3
"""Blind solver — Q1 CORE: basic operating lease full life cycle (LO 17-3).

Riverglen Industrial Supply Co. (lessee) / Summit Asset Finance (lessor).
4-year noncancellable lease, four $22,000 annual payments due Jan 1 of Years
1-4 (annuity due), FV of equipment $140,000, economic life 10 years, asset
reverts to lessor, no purchase/renewal option, no residual value guarantee,
lessor's implicit rate 5% and known by the lessee (lessee IBR 6%).

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal. No floats anywhere.
* Commencement present value is computed with the EXACT annuity-due formula,
  i.e. the Excel form the course handout prescribes:
      =PV(rate, nper, pmt, 0, 1)  ==  sum_{t=0}^{n-1} PMT / (1+i)^t
  evaluated at 50 significant digits, NOT a 5-decimal PV table factor.
  (CH 17 Handout, "PV of lease payments" section, specifies the Excel PV
  function; Demo 17-3 in chapter 17 works the same way.)
* ROUND_HALF_UP to the nearest whole dollar, applied PER PERIOD (round each
  period's interest as it is computed and carry the rounded balance forward),
  never round-at-end. Stem item 8 requires nearest-dollar amounts.
* Interest for the FINAL period of the liability schedule is PLUGGED so the
  liability clears to exactly zero (stem item 8; same as Demo 17-3's
  "certain amounts adjusted for rounding differences").
* Right-of-use asset is credited DIRECTLY for the period reduction (chapter
  convention / single lease-expense form of the period-end adjusting entry).
  The ROU change is itself a plug: straight-line lease expense less the
  period's interest on the liability.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 50

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d(x):
    return Decimal(str(x))


def r0(x):
    """Round to the nearest whole dollar, ROUND_HALF_UP."""
    return x.quantize(DOLLAR, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- fact pattern
PAYMENT = d(22000)          # annual lease payment
N = 4                        # number of payments / lease term in years
FAIR_VALUE = d(140000)
ECONOMIC_LIFE = d(10)        # years
LEASE_TERM = d(4)            # years
IMPLICIT_RATE = d("0.05")    # known by lessee -> this is the discount rate
IBR = d("0.06")              # lessee incremental borrowing rate (not used)
MAJOR_PART = d("0.75")       # course threshold for criterion 3
SUBSTANTIALLY_ALL = d("0.90")  # course threshold for criterion 4

RATE = IMPLICIT_RATE  # criterion: implicit rate is readily determinable/known


# ------------------------------------------------- (b) commencement PV / ROU
def pv_annuity_due(pmt, rate, n):
    """Exact PV of an annuity due: sum_{t=0}^{n-1} pmt / (1+rate)^t."""
    total = Decimal(0)
    one_plus = Decimal(1) + rate
    for t in range(n):
        total += pmt / (one_plus ** t)
    return total


pv_exact = pv_annuity_due(PAYMENT, RATE, N)
lease_liability_0 = r0(pv_exact)      # commencement lease liability
rou_asset_0 = lease_liability_0       # no IDC, no incentive, no prepaid rent

total_payments = PAYMENT * N


# ------------------------------------------------------- (a) classification
pv_pct_of_fv = (pv_exact / FAIR_VALUE)
term_pct_of_life = LEASE_TERM / ECONOMIC_LIFE

criteria = [
    {
        "criterion": "1. Transfer of ownership",
        "met": False,
        "analysis": "Equipment reverts to Summit at the end of the 4-year term; "
                    "no transfer of ownership.",
    },
    {
        "criterion": "2. Purchase option",
        "met": False,
        "analysis": "The lease contains no purchase option.",
    },
    {
        "criterion": "3. Lease term for a major part of remaining economic life",
        "met": bool(term_pct_of_life >= MAJOR_PART),
        "analysis": "4-year lease term / 10-year remaining economic life = "
                    f"{(term_pct_of_life * 100).quantize(CENT)}%, which is less "
                    "than the 75% major-part threshold (7.5 years).",
    },
    {
        "criterion": "4. PV of lease payments equals substantially all of fair value",
        "met": bool(pv_pct_of_fv >= SUBSTANTIALLY_ALL),
        "analysis": f"PV of lease payments ${lease_liability_0:,} / fair value "
                    f"${FAIR_VALUE:,} = "
                    f"{(pv_pct_of_fv * 100).quantize(CENT)}%, which is less than "
                    "90% of fair value ($126,000).",
    },
    {
        "criterion": "5. Specialized asset with no alternative use",
        "met": False,
        "analysis": "Summit routinely leases this forklift equipment to other "
                    "customers, so it has alternative use.",
    },
]
classification = "Finance" if any(c["met"] for c in criteria) else "Operating"


# ------------------------------------ (c) lease liability schedule (payment dates)
# Rows are dated at payment dates (Jan 1), per Demo 17-3 layout.
liability_rows = []
balance = lease_liability_0

# Jan 1, Year 1: commencement payment, no interest has accrued yet.
interest = Decimal(0)
change = PAYMENT - interest
balance = balance + interest - PAYMENT
liability_rows.append({
    "date": "Jan 1, Year 1",
    "lease_payment": int(PAYMENT),
    "interest_on_liability": int(interest),
    "lease_liability_change": int(change),
    "lease_liability_balance": int(balance),
})

for k in range(2, N + 1):
    if k == N:
        # Final period interest is PLUGGED so the liability clears exactly.
        interest = PAYMENT - balance
    else:
        interest = r0(balance * RATE)
    change = PAYMENT - interest
    balance = balance + interest - PAYMENT
    liability_rows.append({
        "date": f"Jan 1, Year {k}",
        "lease_payment": int(PAYMENT),
        "interest_on_liability": int(interest),
        "lease_liability_change": int(change),
        "lease_liability_balance": int(balance),
    })

assert balance == 0, f"liability did not clear: {balance}"
total_interest = sum(d(r["interest_on_liability"]) for r in liability_rows)
assert total_interest == total_payments - lease_liability_0


# ------------------------------------------ (c) right-of-use asset schedule
# Straight-line single lease cost = total lease payments / number of periods.
straight_line_expense = r0(total_payments / d(N))

# Interest for the Dec 31, Year k ROU row is the interest from the
# Jan 1, Year k+1 liability row (handout: dates are offset by one line).
rou_rows = []
rou_balance = rou_asset_0
for k in range(1, N + 1):
    if k < N:
        per_interest = d(liability_rows[k]["interest_on_liability"])
    else:
        per_interest = Decimal(0)  # liability already zero after final payment
    rou_change = straight_line_expense - per_interest
    rou_balance = rou_balance - rou_change
    rou_rows.append({
        "date": f"Dec 31, Year {k}",
        "lease_expense": int(straight_line_expense),
        "interest_on_liability": int(per_interest),
        "rou_asset_change": int(rou_change),
        "rou_asset_balance": int(rou_balance),
    })

assert rou_balance == 0, f"ROU did not clear: {rou_balance}"


# --------------------------------------------------- period-end liability balances
# Balance at Dec 31 of Year k = balance after the Jan 1 Year k payment plus the
# interest accrued during Year k (which is the Jan 1 Year k+1 row's interest).
dec31_liability = {}
for k in range(1, N + 1):
    after_payment = d(liability_rows[k - 1]["lease_liability_balance"])
    accrued = d(liability_rows[k]["interest_on_liability"]) if k < N else Decimal(0)
    dec31_liability[k] = after_payment + accrued

# Sanity: ROU balance equals lease liability balance at each Dec 31 in this
# basic case (no IDC / incentive / prepaid rent).
for k in range(1, N + 1):
    assert dec31_liability[k] == d(rou_rows[k - 1]["rou_asset_balance"])

# (e) Dec 31, Year 1 balance-sheet split.
# Current portion = reduction of the liability within the next 12 months, i.e.
# the Jan 1, Year 2 payment of $22,000 (Demo 17-3 presents it exactly this way).
bs_rou_y1 = d(rou_rows[0]["rou_asset_balance"])
bs_total_liab_y1 = dec31_liability[1]
bs_current_liab_y1 = PAYMENT
bs_noncurrent_liab_y1 = bs_total_liab_y1 - bs_current_liab_y1
is_lease_expense_y1 = straight_line_expense


# ----------------------------------------------------------- journal entries
def je(part, date, memo, lines):
    dr = sum(d(l["debit"]) for l in lines)
    cr = sum(d(l["credit"]) for l in lines)
    assert dr == cr, f"{part} {date} out of balance: Dr {dr} vs Cr {cr}"
    return {"part": part, "date": date, "memo": memo, "lines": lines}


def line(account, debit=0, credit=0):
    return {"account": account, "debit": int(debit), "credit": int(credit)}


journal_entries = []

# (d) Year 1
journal_entries.append(je(
    "d", "Jan 1, Year 1",
    "Commencement: recognize right-of-use asset and lease liability",
    [line("Right-of-Use Asset", debit=rou_asset_0),
     line("Lease Liability", credit=lease_liability_0)],
))
journal_entries.append(je(
    "d", "Jan 1, Year 1", "First annual lease payment",
    [line("Lease Liability", debit=PAYMENT),
     line("Cash", credit=PAYMENT)],
))
journal_entries.append(je(
    "d", "Dec 31, Year 1",
    "Period-end adjusting entry - single lease expense",
    [line("Lease Expense", debit=straight_line_expense),
     line("Lease Liability", credit=d(rou_rows[0]["interest_on_liability"])),
     line("Right-of-Use Asset", credit=d(rou_rows[0]["rou_asset_change"]))],
))

# (f) Years 2 and 3
for part_year in (2, 3):
    journal_entries.append(je(
        "f", f"Jan 1, Year {part_year}", f"Year {part_year} annual lease payment",
        [line("Lease Liability", debit=PAYMENT),
         line("Cash", credit=PAYMENT)],
    ))
    row = rou_rows[part_year - 1]
    journal_entries.append(je(
        "f", f"Dec 31, Year {part_year}",
        "Period-end adjusting entry - single lease expense",
        [line("Lease Expense", debit=straight_line_expense),
         line("Lease Liability", credit=d(row["interest_on_liability"])),
         line("Right-of-Use Asset", credit=d(row["rou_asset_change"]))],
    ))

# (g) Year 4 maturity / settlement
journal_entries.append(je(
    "g", "Jan 1, Year 4", "Final annual lease payment - lease liability settled",
    [line("Lease Liability", debit=PAYMENT),
     line("Cash", credit=PAYMENT)],
))
journal_entries.append(je(
    "g", "Dec 31, Year 4",
    "Final period-end adjusting entry - no interest remains; ROU asset written off",
    [line("Lease Expense", debit=straight_line_expense),
     line("Right-of-Use Asset", credit=d(rou_rows[3]["rou_asset_change"]))],
))


# ------------------------------------------------------------------- answers
answers = []

# a
answers.append({"label": "a: lease classification for Riverglen (lessee)",
                "value": classification})
answers.append({"label": "a: discount rate used (%) - rate implicit in the lease, known by lessee",
                "value": 5})

# b
answers.append({"label": "b: lease liability at commencement (Jan 1, Year 1, before first payment)",
                "value": int(lease_liability_0)})
answers.append({"label": "b: right-of-use asset at commencement (Jan 1, Year 1)",
                "value": int(rou_asset_0)})

# c - lease liability schedule
for row in liability_rows:
    answers.append({"label": f"c: lease liability schedule - {row['date']} - lease payment",
                    "value": row["lease_payment"]})
    answers.append({"label": f"c: lease liability schedule - {row['date']} - interest on liability",
                    "value": row["interest_on_liability"]})
    answers.append({"label": f"c: lease liability schedule - {row['date']} - lease liability change",
                    "value": row["lease_liability_change"]})
    answers.append({"label": f"c: lease liability schedule - {row['date']} - lease liability balance after payment",
                    "value": row["lease_liability_balance"]})
answers.append({"label": "c: lease liability schedule - total lease payments",
                "value": int(total_payments)})
answers.append({"label": "c: lease liability schedule - total interest",
                "value": int(total_interest)})

# c - right-of-use asset schedule
for row in rou_rows:
    answers.append({"label": f"c: ROU asset schedule - {row['date']} - lease expense",
                    "value": row["lease_expense"]})
    answers.append({"label": f"c: ROU asset schedule - {row['date']} - interest on liability",
                    "value": row["interest_on_liability"]})
    answers.append({"label": f"c: ROU asset schedule - {row['date']} - ROU asset change",
                    "value": row["rou_asset_change"]})
    answers.append({"label": f"c: ROU asset schedule - {row['date']} - ROU asset balance",
                    "value": row["rou_asset_balance"]})

# e
answers.append({"label": "e: Year 1 income statement - lease expense (single operating lease cost)",
                "value": int(is_lease_expense_y1)})
answers.append({"label": "e: Dec 31, Year 1 balance sheet - right-of-use asset",
                "value": int(bs_rou_y1)})
answers.append({"label": "e: Dec 31, Year 1 balance sheet - current lease liability",
                "value": int(bs_current_liab_y1)})
answers.append({"label": "e: Dec 31, Year 1 balance sheet - noncurrent lease liability",
                "value": int(bs_noncurrent_liab_y1)})
answers.append({"label": "e: Dec 31, Year 1 balance sheet - total lease liability",
                "value": int(bs_total_liab_y1)})

# g - confirmation both accounts are zero after lease end
answers.append({"label": "g: right-of-use asset balance after Dec 31, Year 4",
                "value": int(rou_balance)})
answers.append({"label": "g: lease liability balance after Jan 1, Year 4 final payment",
                "value": int(balance)})


notes = (
    "Operating lease: none of the five ASC 842 classification criteria is met "
    "(no ownership transfer, no purchase option, 4/10 = 40% < 75% of economic "
    "life, PV $81,911 / $140,000 = 58.51% < 90% of fair value, and the "
    "equipment is not specialized since Summit routinely leases it to others). "
    "Discount rate is the 5% implicit rate because it is known to Riverglen; "
    "the 6% IBR is not used. PV of the annuity due uses the exact Excel "
    "=PV(0.05,4,-22000,0,1) formula = $81,911.4566, rounded to $81,911. "
    "Interest on the Jan 1, Year 4 row ($1,048) is the plug that clears the "
    "liability; it equals the unrounded 5% calculation anyway. Single lease "
    "cost is $88,000 / 4 = $22,000 per year, and each period's ROU reduction "
    "is that expense less the period's interest, credited directly to the ROU "
    "asset. Dec 31, Year 1 current lease liability is the $22,000 Jan 1, Year 2 "
    "payment; noncurrent is the $62,907 total less that $22,000. Both the ROU "
    "asset and the lease liability are zero after lease end. Convention note: "
    "a 5-decimal PV table factor (3.72325) would give $81,911.50 -> $81,912 and "
    "shift the schedule by $1; the exact Excel PV formula prescribed by the CH 17 "
    "handout and used in Demo 17-3 gives $81,911, which is what is reported here."
)

out = {
    "id": "agent_285#00",
    "rounding_convention": (
        "decimal.Decimal only; ROUND_HALF_UP to the nearest whole dollar applied "
        "per period (rounded balances carried forward, never round-at-end); PV of "
        "the annuity due from the exact formula =PV(0.05,4,-22000,0,1) at 50-digit "
        "precision per the course handout, not a 5-decimal table factor; "
        "final-period interest plugged so the lease liability clears to zero"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
    "supporting_detail": {
        "classification_criteria": criteria,
        "pv_of_lease_payments_unrounded": str(pv_exact.quantize(Decimal("0.0001"))),
        "lease_liability_schedule": liability_rows,
        "right_of_use_asset_schedule": rou_rows,
        "dec31_lease_liability_balances": {
            f"Dec 31, Year {k}": int(v) for k, v in dec31_liability.items()
        },
    },
}

print(json.dumps(out, indent=2))
