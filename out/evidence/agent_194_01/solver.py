#!/usr/bin/env python3
"""
Solver for item agent_194#01 — Redline Cycle Parts Co.

Fact pattern (from stem.md only):
  December 31, Year 1 ending inventory was UNDERSTATED by $15,600 (two storage
  bays omitted from the physical count). Purchases were correct in both years.
  Year 2 ending inventory is correct. Periodic-style COGS presentation. Ignore
  taxes.

  Amounts AS RECORDED (with the error):
                          Year 1      Year 2
    Beginning inventory   52,000      61,000 (understated)
    Net purchases        198,000     215,000
    Ending inventory      61,000 (understated)   70,000 (correct)
    Net sales            310,000     355,000
    Other expenses        48,000      51,000

Method
------
Everything below is derived, not asserted. The only inputs are the six recorded
figures per year plus the single error amount.

  COGS            = Beginning inventory + Net purchases - Ending inventory
  Gross profit    = Net sales - COGS
  Pretax income   = Gross profit - Other expenses

The corrected column rebuilds the same identities after pushing the $15,600
understatement into (i) Year 1 ending inventory and (ii) Year 2 beginning
inventory (they are the same physical count). Year 2 ending inventory is stated
as correct, so it is untouched.

"Effect" convention used throughout: effect = (as recorded) - (correct).
  positive  -> the recorded amount is OVERSTATED by that amount
  negative  -> the recorded amount is UNDERSTATED by that amount
The reported effect values are signed this way, with a plain-English direction
label alongside each.

Correcting-entry treatment follows Exhibit 10-2 / Demo 10-7 (LO 10-7):
  - discovered in the year of the error, before closing -> fix Inventory and
    Cost of Goods Sold directly;
  - discovered in the following period, before the error self-corrects -> prior
    period adjustment to Retained Earnings and Inventory;
  - discovered after the error has self-corrected (a counterbalancing error) ->
    no entry; prior statements are restated only.

Rounding convention
-------------------
ROUND_HALF_UP to the cent, applied per computed line item (round-per-period, no
deferred rounding). All money is decimal.Decimal; no float ever touches a
monetary value. This particular fact pattern is whole-dollar, so no rounding is
actually triggered — the quantizer is applied anyway so the convention is
explicit and enforced rather than incidental.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def q(x: Decimal) -> Decimal:
    """Quantize to the cent, ROUND_HALF_UP (per-line-item)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly plain number: int when whole, else float-free string-safe."""
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Inputs straight off the stem
# ---------------------------------------------------------------------------
ERROR = Decimal("15600")  # Year 1 ending inventory UNDERSTATED by this amount

REC = {
    1: {
        "BI": Decimal("52000"),
        "PUR": Decimal("198000"),
        "EI": Decimal("61000"),   # understated
        "SALES": Decimal("310000"),
        "OTHEXP": Decimal("48000"),
    },
    2: {
        "BI": Decimal("61000"),   # understated (carried from Year 1 count)
        "PUR": Decimal("215000"),
        "EI": Decimal("70000"),   # correct
        "SALES": Decimal("355000"),
        "OTHEXP": Decimal("51000"),
    },
}

# Corrected inventory figures: the single bad count appears twice — as Year 1
# ending inventory and as Year 2 beginning inventory. Purchases, sales and other
# expenses are stated as correct, so they carry over unchanged.
COR = {
    1: dict(REC[1], EI=REC[1]["EI"] + ERROR),
    2: dict(REC[2], BI=REC[2]["BI"] + ERROR),   # EI Year 2 already correct
}


def build(year_data):
    """Apply the periodic COGS / gross profit / pretax identities."""
    cogs = q(year_data["BI"] + year_data["PUR"] - year_data["EI"])
    gross_profit = q(year_data["SALES"] - cogs)
    pretax = q(gross_profit - year_data["OTHEXP"])
    return {"EI": q(year_data["EI"]), "COGS": cogs, "PRETAX": pretax}


rec = {y: build(REC[y]) for y in (1, 2)}
cor = {y: build(COR[y]) for y in (1, 2)}

# Cumulative pretax income
rec_cum = {1: rec[1]["PRETAX"], 2: q(rec[1]["PRETAX"] + rec[2]["PRETAX"])}
cor_cum = {1: cor[1]["PRETAX"], 2: q(cor[1]["PRETAX"] + cor[2]["PRETAX"])}


def direction(effect: Decimal) -> str:
    """Plain-English direction phrase for a signed effect amount."""
    if effect > 0:
        return f"overstated by {abs(effect)}"
    if effect < 0:
        return f"understated by {abs(effect)}"
    return "correctly stated, no effect"


answers = []


def add(label, value):
    answers.append({"label": label, "value": num(value)})


def add_row(part_letter, year, line_name, rec_v, cor_v):
    eff = q(rec_v - cor_v)
    add(f"{part_letter}: Year {year} {line_name} as recorded", rec_v)
    add(f"{part_letter}: Year {year} {line_name} correct", cor_v)
    add(
        f"{part_letter}: Year {year} {line_name} effect of error "
        f"(as recorded - correct; {direction(eff)})",
        eff,
    )


# ---------------------------------------------------------------------------
# (a) two-year subsequent measurement schedule
# ---------------------------------------------------------------------------
for y in (1, 2):
    add_row("a", y, "ending inventory", rec[y]["EI"], cor[y]["EI"])
    add_row("a", y, "cost of goods sold", rec[y]["COGS"], cor[y]["COGS"])
    add_row("a", y, "pretax income", rec[y]["PRETAX"], cor[y]["PRETAX"])
    add_row("a", y, "cumulative pretax income", rec_cum[y], cor_cum[y])

# ---------------------------------------------------------------------------
# (b) balance-sheet misstatement, books left uncorrected
#
#     Inventory misstatement at a balance sheet date = recorded EI - correct EI.
#     Retained earnings misstatement = cumulative pretax effect through that
#     date (taxes ignored, so pretax = the whole hit to RE).
# ---------------------------------------------------------------------------
for y in (1, 2):
    inv_eff = q(rec[y]["EI"] - cor[y]["EI"])
    re_eff = q(rec_cum[y] - cor_cum[y])
    add(
        f"b: Inventory misstatement at Dec 31, Year {y}, books uncorrected "
        f"({direction(inv_eff)})",
        inv_eff,
    )
    add(
        f"b: Retained earnings misstatement at Dec 31, Year {y}, books uncorrected "
        f"({direction(re_eff)})",
        re_eff,
    )

# ---------------------------------------------------------------------------
# (f) counterbalancing test and two-year net pretax effect
# ---------------------------------------------------------------------------
two_year_net = q((rec[1]["PRETAX"] + rec[2]["PRETAX"]) - (cor[1]["PRETAX"] + cor[2]["PRETAX"]))
counterbalancing = two_year_net == 0 and q(rec[2]["EI"] - cor[2]["EI"]) == 0
answers.append(
    {
        "label": "f: Is the error counterbalancing?",
        "value": "Yes" if counterbalancing else "No",
    }
)
add("f: Two-year net effect on pretax income", two_year_net)

# ---------------------------------------------------------------------------
# Correcting entries (c) (d) (e)
#
# The Year 1 ending inventory is understated, so every correction DEBITS
# Inventory for the omitted 15,600. The credit depends on whether the Year 1
# books are still open and whether the error has already reversed.
# ---------------------------------------------------------------------------
amt = num(ERROR)

# (c) discovered Dec 31, Year 1 — the year of the error, before closing.
#     Understating ending inventory overstated COGS, so COGS is credited.
entry_c = {
    "part": "c",
    "description": "December 31, Year 1 - to correct the Year 1 ending inventory count error (books still open)",
    "lines": [
        {"account": "Inventory", "debit": amt, "credit": 0},
        {"account": "Cost of Goods Sold", "debit": 0, "credit": amt},
    ],
}

# (d) discovered Jan 1, Year 2 — Year 1 is closed but the error has NOT yet
#     self-corrected, so a prior period adjustment is recorded.
entry_d = {
    "part": "d",
    "description": "January 1, Year 2 - prior period adjustment; Year 1 is closed and the error has not yet self-corrected",
    "lines": [
        {"account": "Inventory", "debit": amt, "credit": 0},
        {"account": "Retained Earnings - Prior Period Adjustment", "debit": 0, "credit": amt},
    ],
}

# (e) discovered Jan 1, Year 3 — the error self-corrected during Year 2, so
#     both Inventory and Retained Earnings are already right: no entry.
entry_e = {
    "part": "e",
    "description": "January 1, Year 3 - no entry required; the counterbalancing error self-corrected during Year 2 (prior-year statements are still restated)",
    "lines": [],
}

journal_entries = [entry_c, entry_d, entry_e]

# Debits must equal credits in every entry.
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert q(d) == q(c), f"entry {je['part']} out of balance: {d} vs {c}"

# Internal consistency checks (not reported as answers).
assert COR[1]["EI"] == COR[2]["BI"], "Year 1 correct EI must roll into Year 2 BI"
assert two_year_net == 0, "an inventory-count error of this type must counterbalance"

out = {
    "id": "agent_194#01",
    "rounding_convention": (
        "ROUND_HALF_UP to the cent, applied per line item as computed "
        "(round-per-period, not deferred to the end); decimal.Decimal only, no floats. "
        "Effect = as recorded minus correct: positive = overstated, negative = understated."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Part (e) requires no journal entry, so its 'lines' array is empty. "
        "Correcting-entry pattern follows Exhibit 10-2 / Demo 10-7 (LO 10-7): correct "
        "Inventory and COGS in the year of the error; prior period adjustment to Retained "
        "Earnings if discovered after closing but before self-correction; nothing once the "
        "counterbalancing error has reversed. Taxes ignored per the stem, so the retained "
        "earnings misstatement equals the cumulative pretax misstatement."
    ),
}

print(json.dumps(out, indent=2))
