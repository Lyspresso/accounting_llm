"""Cold derivation: agent_240#00 — ASC 480 mandatorily redeemable preferred stock.

Rounding convention: all money is decimal.Decimal; every per-period figure is
quantized to whole dollars with ROUND_HALF_UP as it is computed (rounding is
applied per period, not at the end), and the accretion schedule is forced to
close EXACTLY to the fixed redemption (face) amount by taking the final
period's interest as the plug (face - prior ending carrying amount). With the
stem's facts the plug equals the unrounded amount, so no rounding difference
arises. Effective-interest math itself is run at full Decimal precision.

Derivation (nothing hard-coded but the stem's own facts):
  proceeds = 150,000 ; redemption = 199,650 ; r = 10% ; n = 3 annual periods
  Internal check that r reproduces the fixed redemption:
      proceeds * (1+r)^n  ==  redemption
  Each period: interest = beginning carrying amount * r ; ending = beg + int.
"""
from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 40
C = Decimal("1")


def d(x):
    return Decimal(str(x))


def q(x):
    return x.quantize(C, rounding=ROUND_HALF_UP)


# ---------------- stem facts ----------------
proceeds = d("150000")
redemption = d("199650")
rate = d("0.10")
years = [1, 2, 3]           # Jan 1 Yr1 issuance -> Dec 31 Yr3 mandatory redemption
par_per_share = d("40")
shares = d("3000")
par_total = q(par_per_share * shares)

# internal consistency: does 10% compound the proceeds to the fixed redemption?
compounded = proceeds * (Decimal(1) + rate) ** len(years)
rate_reproduces_face = (q(compounded) == redemption)

# ---------------- b. accretion schedule ----------------
schedule = []
beg = proceeds
for i, yr in enumerate(years):
    last = (i == len(years) - 1)
    if last:
        # force exact close to the fixed redemption amount
        interest = redemption - beg
    else:
        interest = q(beg * rate)
    end = q(beg + interest)
    schedule.append({"year": yr, "beginning": beg, "interest": interest, "ending": end})
    beg = end

closes_to_face = (schedule[-1]["ending"] == redemption)
total_interest = sum((r["interest"] for r in schedule), Decimal(0))
accretion_check = (total_interest == redemption - proceeds)

LIAB = "Mandatorily redeemable preferred stock (liability)"

answers = []
A = lambda label, value: answers.append({"label": label, "value": value})

# ---- a ----
A("a: Jan 1 Yr 1 — Dr Cash", int(proceeds))
A("a: Jan 1 Yr 1 — Cr Mandatorily redeemable preferred stock (liability)", int(proceeds))
A("a: initial carrying amount of the liability (proceeds; = PV of the $199,650 fixed "
  "redemption discounted 3 yrs at 10%)", int(proceeds))
A("a: classification immediately after issuance — ASC 480-10-25-4: shares embodying an "
  "unconditional obligation to redeem a FIXED amount ($199,650) at a FIXED date "
  "(12/31 Yr 3), not solely upon liquidation, are a LIABILITY, not equity; presented as a "
  "NONCURRENT (long-term) liability at 1/1/Yr 1 since redemption is >12 months away. "
  "Nothing is reported in stockholders' equity; the $120,000 aggregate par "
  "(3,000 sh x $40) never appears in equity", "Liability (noncurrent) — no amount in equity")
A("a: aggregate par of the preferred (form only; NOT recorded in equity)", int(par_total))
A("a: subsequent-measurement basis — accrete to redemption amount using the interest "
  "method at the 10% inception effective rate (ASC 480-10-35-3); accretion is charged to "
  "INTEREST EXPENSE, not to dividends/retained earnings",
  "Interest method at 10%; accretion = interest expense")

# ---- b ---- every row, every running balance
for r in schedule:
    A(f"b: Year {r['year']} — beginning carrying amount", int(r["beginning"]))
    A(f"b: Year {r['year']} — interest expense (accretion) @10% of beginning balance", int(r["interest"]))
    A(f"b: Year {r['year']} — ending carrying amount", int(r["ending"]))
A("b: schedule total interest expense (accretion), Years 1-3", int(total_interest))
A("b: Year 3 ending carrying amount equals the fixed redemption amount", int(redemption))
A("b: rate check — $150,000 x 1.10^3 = $199,650 (10% reproduces the fixed redemption)",
  bool(rate_reproduces_face))

# ---- c ----
A("c: Dec 31 Yr 1 — Dr Interest expense", int(schedule[0]["interest"]))
A("c: Dec 31 Yr 1 — Cr Mandatorily redeemable preferred stock (liability)", int(schedule[0]["interest"]))
A("c: carrying amount reported at Dec 31 Yr 1 (noncurrent liability)", int(schedule[0]["ending"]))
A("c: Dec 31 Yr 2 — Dr Interest expense", int(schedule[1]["interest"]))
A("c: Dec 31 Yr 2 — Cr Mandatorily redeemable preferred stock (liability)", int(schedule[1]["interest"]))
A("c: carrying amount reported at Dec 31 Yr 2 (now CURRENT liability — redeemable within "
  "12 months)", int(schedule[1]["ending"]))

# ---- d ----
A("d: Dec 31 Yr 3 entry 1 — Dr Interest expense", int(schedule[2]["interest"]))
A("d: Dec 31 Yr 3 entry 1 — Cr Mandatorily redeemable preferred stock (liability)", int(schedule[2]["interest"]))
A("d: liability balance immediately before settlement", int(redemption))
A("d: Dec 31 Yr 3 entry 2 — Dr Mandatorily redeemable preferred stock (liability)", int(redemption))
A("d: Dec 31 Yr 3 entry 2 — Cr Cash", int(redemption))
A("d: gain or loss on settlement (carrying amount equals the cash paid)", 0)
A("d: liability carrying amount after settlement", 0)

# ---- e ----
A("e: redemption amount", int(redemption))
A("e: less issue proceeds", int(proceeds))
A("e: redemption - proceeds", int(redemption - proceeds))
A("e: sum of interest expense Yr 1 + Yr 2 + Yr 3 "
  f"({int(schedule[0]['interest'])} + {int(schedule[1]['interest'])} + {int(schedule[2]['interest'])})",
  int(total_interest))
A("e: reconciles (total interest expense == redemption - proceeds)", bool(accretion_check))
A("e: total cash flows — cash in at issuance vs cash out at redemption "
  "(dividends ignored per stem)", int(redemption - proceeds))

# ---------------- journal entries ----------------
def je(part, memo, lines):
    dr = sum(d(l[1]) for l in lines)
    cr = sum(d(l[2]) for l in lines)
    assert dr == cr, (part, memo, dr, cr)
    return {"part": part, "memo": memo,
            "lines": [{"account": a, "debit": int(d(x)), "credit": int(d(y))} for a, x, y in lines]}

jes = [
    je("a", "Jan 1, Year 1 — issuance of mandatorily redeemable preferred; recorded as a "
            "liability at proceeds (= PV of $199,650 at 10% for 3 yrs); no equity credit",
       [("Cash", proceeds, 0), (LIAB, 0, proceeds)]),
    je("c", "Dec 31, Year 1 — adjusting entry, accretion of the liability toward the "
            "$199,650 redemption at the 10% effective rate",
       [("Interest expense", schedule[0]["interest"], 0), (LIAB, 0, schedule[0]["interest"])]),
    je("c", "Dec 31, Year 2 — adjusting entry, accretion at 10% of the $165,000 beginning "
            "carrying amount",
       [("Interest expense", schedule[1]["interest"], 0), (LIAB, 0, schedule[1]["interest"])]),
    je("d", "Dec 31, Year 3 (entry 1 of 2) — final accretion; brings the liability to the "
            "$199,650 mandatory redemption amount",
       [("Interest expense", schedule[2]["interest"], 0), (LIAB, 0, schedule[2]["interest"])]),
    je("d", "Dec 31, Year 3 (entry 2 of 2) — mandatory cash redemption; liability retired at "
            "carrying amount, no gain or loss",
       [(LIAB, redemption, 0), ("Cash", 0, redemption)]),
]

notes = (
    "ASC 480-10-25-4: preferred shares with an unconditional obligation to redeem a FIXED "
    "amount ($199,650) on a FIXED date (12/31 Yr 3) — not solely upon liquidation — are "
    "classified as a LIABILITY; the $120,000 aggregate par (3,000 sh x $40) is never shown in "
    "equity. Initial measurement = $150,000 cash proceeds, which is the PV of $199,650 for 3 "
    "years at 10% (150,000 x 1.10^3 = 199,650, so 10% is the implicit rate). Subsequent "
    "measurement (ASC 480-10-35-3) accretes the liability to the redemption amount using the "
    "interest method; the accretion is INTEREST EXPENSE (not a dividend / not a charge to "
    "retained earnings) because the instrument is a liability. Schedule: Yr1 150,000 + 15,000 = "
    "165,000; Yr2 165,000 + 16,500 = 181,500; Yr3 181,500 + 18,150 = 199,650. Total accretion "
    "49,650 = 199,650 - 150,000. Presentation: noncurrent liability at 1/1/Yr1 and 12/31/Yr1; "
    "current liability at 12/31/Yr2 (due within 12 months). Settlement at maturity is at "
    "carrying amount, so no gain or loss. Periodic preferred dividends ignored per the stem; had "
    "they been paid they would also be interest expense. Whole-dollar journal entries with the "
    "schedule forced to close exactly to the $199,650 face; here every period's interest is "
    "already an exact whole dollar, so the forced close produced no rounding plug."
)

out = {
    "id": "agent_240#00",
    "rounding_convention": (
        "decimal.Decimal throughout; per-period interest quantized to whole dollars with "
        "ROUND_HALF_UP; effective-interest math at full Decimal precision; final period's "
        "interest taken as the plug so the schedule closes EXACTLY to the $199,650 fixed "
        "redemption amount (plug was zero here — all periods are exact whole dollars)"
    ),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}

assert closes_to_face and accretion_check and rate_reproduces_face
print(json.dumps(out, indent=1))
