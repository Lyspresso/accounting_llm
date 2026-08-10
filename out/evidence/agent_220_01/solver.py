"""Blind solver — agent_220#01.

Q2 (LO 13-4): Glacier Peak Industrial, finite-life technology license.
Straight-line amortization, License credited directly (no accumulated
amortization contra account); prospective change in estimated useful life;
period-end amortization JE; disposal at a loss.

Fact pattern (from stem.md only):
  cost                       $150,000 cash, acquired January 1, Year 1
  original useful life       10 years, residual $0
  revision date              January 1, Year 5 (after 4 full years)
  revised total useful life  8 years from acquisition => 4 years remaining
  revised residual           $0
  disposal                   January 1, Year 7 for $40,000 cash
                             (Year-6 amortization already recorded)

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no floats anywhere. Amortization is computed
per period and each period's expense is quantized to the cent with
ROUND_HALF_UP before it is posted and before it reduces the carrying amount
(round-per-period, not round-at-end). Carrying amounts are therefore exact
running balances of already-rounded charges. No present-value work is
required by this item, so no PV factor convention applies.

A change in estimated useful life is a change in accounting estimate:
accounted for prospectively (ASC 250) — no restatement of Years 1-4. The
revised annual charge is the January 1, Year 5 carrying amount less revised
residual, spread over the 4 remaining years.

Run: python3 solver.py   (prints one JSON object to stdout)
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x):
    """Quantize to cents, ROUND_HALF_UP (applied per period)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    """JSON-friendly plain number: int when whole, else float-free string->float."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- facts
COST = Decimal("150000")
ORIG_LIFE_YEARS = 10
ORIG_RESIDUAL = Decimal("0")
YEARS_BEFORE_REVISION = 4          # revision on Jan 1, Year 5
REVISED_TOTAL_LIFE_YEARS = 8
REVISED_RESIDUAL = Decimal("0")
DISPOSAL_PROCEEDS = Decimal("40000")
DISPOSAL_AT_START_OF_YEAR = 7      # Jan 1, Year 7; Year-6 amortization recorded
SCHEDULE_LAST_YEAR = 6             # schedule requested for Years 1-6

# ------------------------------------------------- (a) initial recognition
entry_a = {
    "part": "a",
    "description": "January 1, Year 1 - initial recognition of purchased license",
    "lines": [
        {"account": "License", "debit": num(COST), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(COST)},
    ],
}

# --------------------------------------- original-estimate annual charge
orig_annual = money((COST - ORIG_RESIDUAL) / Decimal(ORIG_LIFE_YEARS))

# ------------------- build schedule Years 1..4 under the original estimate
schedule = []
carrying = COST
for year in range(1, YEARS_BEFORE_REVISION + 1):
    expense = orig_annual
    begin = carrying
    carrying = money(carrying - expense)
    schedule.append(
        {"year": year, "beginning": begin, "expense": expense, "ending": carrying}
    )

# ------------------------------- (b) carrying amount Jan 1 Yr 5 pre-revision
carrying_jan1_y5 = carrying  # = cost - 4 x original annual charge

# ------------------------------------ revised prospective annual charge
remaining_years = REVISED_TOTAL_LIFE_YEARS - YEARS_BEFORE_REVISION  # 4
revised_annual = money((carrying_jan1_y5 - REVISED_RESIDUAL) / Decimal(remaining_years))

# --------------------------- (c) continue schedule Years 5..6 (revised)
for year in range(YEARS_BEFORE_REVISION + 1, SCHEDULE_LAST_YEAR + 1):
    expense = revised_annual
    begin = carrying
    carrying = money(carrying - expense)
    schedule.append(
        {"year": year, "beginning": begin, "expense": expense, "ending": carrying}
    )

carrying_jan1_y7 = carrying  # after Year-6 amortization, before disposal

# ------------------------------ (d) December 31, Year 5 amortization JE
y5 = next(r for r in schedule if r["year"] == 5)
entry_d = {
    "part": "d",
    "description": "December 31, Year 5 - amortization under the revised estimate",
    "lines": [
        {"account": "Amortization Expense", "debit": num(y5["expense"]), "credit": 0},
        {"account": "License", "debit": 0, "credit": num(y5["expense"])},
    ],
}

# ------------------------------------------- (e) January 1, Year 7 disposal
gain_or_loss = money(DISPOSAL_PROCEEDS - carrying_jan1_y7)  # negative => loss
loss = money(-gain_or_loss) if gain_or_loss < 0 else Decimal("0.00")
gain = gain_or_loss if gain_or_loss > 0 else Decimal("0.00")

disposal_lines = [{"account": "Cash", "debit": num(DISPOSAL_PROCEEDS), "credit": 0}]
if loss > 0:
    disposal_lines.append(
        {"account": "Loss on Disposal of License", "debit": num(loss), "credit": 0}
    )
disposal_lines.append(
    {"account": "License", "debit": 0, "credit": num(carrying_jan1_y7)}
)
if gain > 0:
    disposal_lines.append(
        {"account": "Gain on Disposal of License", "debit": 0, "credit": num(gain)}
    )

entry_e = {
    "part": "e",
    "description": "January 1, Year 7 - sale of license for cash",
    "lines": disposal_lines,
}

# ------------------------- (f) total amortization Years 1-6 + reconciliation
total_amortization = money(sum((r["expense"] for r in schedule), Decimal("0")))
reconciliation = money(COST - carrying_jan1_y7)  # cost - carrying amount removed
assert total_amortization == reconciliation, (total_amortization, reconciliation)

# ------------------------------------------------------ integrity checks
for e in (entry_a, entry_d, entry_e):
    dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert dr == cr, (e["part"], dr, cr)

# ------------------------------------------------------------- output
answers = [
    {"label": "b: carrying amount January 1, Year 5 before the revision",
     "value": num(carrying_jan1_y5)},
]
for r in schedule:
    answers.append({
        "label": "c: Year %d amortization expense" % r["year"],
        "value": num(r["expense"]),
    })
    answers.append({
        "label": "c: Year %d ending carrying amount" % r["year"],
        "value": num(r["ending"]),
    })
answers.append({
    "label": "f: total amortization expense recognized Years 1-6",
    "value": num(total_amortization),
})
answers.append({
    "label": "f: reconciliation - cost less disposal carrying amount removed",
    "value": num(reconciliation),
})

out = {
    "id": "agent_220#01",
    "rounding_convention": (
        "decimal.Decimal only; ROUND_HALF_UP quantized to the cent per period "
        "(round-per-period, not round-at-end); change in useful life applied "
        "prospectively; no PV factors required"
    ),
    "answers": answers,
    "journal_entries": [entry_a, entry_d, entry_e],
    "insufficient_info": False,
    "notes": (
        "Years 1-4 amortize 150,000/10 = 15,000 per year, so the January 1, "
        "Year 5 carrying amount is 90,000. The estimate change is prospective: "
        "90,000 over the 4 remaining years = 22,500 per year for Years 5-8. "
        "After Year-6 amortization the carrying amount is 45,000, so the "
        "40,000 sale on January 1, Year 7 produces a 5,000 loss. Total "
        "amortization Years 1-6 = 105,000, which ties to cost 150,000 less "
        "the 45,000 carrying amount removed. License is credited directly, "
        "so no accumulated amortization account appears in any entry."
    ),
}

print(json.dumps(out, indent=2))
