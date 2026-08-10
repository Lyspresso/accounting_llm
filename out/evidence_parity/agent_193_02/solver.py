"""Solver for agent_193#02 — LO 10-6 accounting changes in inventory method.

Rounding convention: all monetary amounts are decimal.Decimal, quantized to
cents with ROUND_HALF_UP applied independently per period / per computed
figure (no chained rounding, no floats anywhere).

Part A (Pinecrest, FIFO -> LIFO): a change TO LIFO when prior layers cannot be
reconstructed is applied PROSPECTIVELY -- no cumulative-effect JE, prior years
are not restated, and the carrying amount of inventory at the beginning of the
year of change becomes the LIFO base layer.

Part B (Oakridge, average -> FIFO): retrospective application. The cumulative
effect at the beginning of the year of change equals the difference between the
old-method and new-method inventory at the END of the immediately preceding
year; the portion attributable to periods before the earliest year presented is
the difference at the end of the year before that.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
def r(x): return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)
def n(d): return int(d) if d == d.to_integral_value() else float(d)

# ---------------- Given data (transcribed from the question only) -----------
# Part A -- Pinecrest Retail Group
pinecrest = {
    1: {"ni": r("200000"), "ei": r("150000")},
    2: {"ni": r("240000"), "ei": r("180000")},
    3: {"ni": r("210000"), "ei": r("165000")},
}
YEAR_OF_CHANGE = 3          # Jan 1, Year 3
# Method label is derived: FIFO for years before the change, LIFO from it on.
def method_a(y): return "FIFO" if y < YEAR_OF_CHANGE else "LIFO"

# Part B -- Oakridge Parts Co.  (inventory at December 31)
oak_avg = {2: r("180000"), 1: r("140000")}
oak_fifo = {2: r("150000"), 1: r("120000")}

# ---------------- Part A derivations ---------------------------------------
# Prospective: no cumulative effect is computed, so the JE amount is zero.
je_a_amount = r("0")
# LIFO base layer = carrying amount of inventory at the date of change
# = ending inventory of the last pre-change year (Dec 31, Year 2, FIFO).
lifo_base_layer = pinecrest[YEAR_OF_CHANGE - 1]["ei"]

# ---------------- Part B derivations ---------------------------------------
# Difference (FIFO minus average cost) at each December 31.
diff = {y: r(oak_fifo[y] - oak_avg[y]) for y in (1, 2)}   # negative => FIFO lower
cum_effect_bd_y3 = diff[2]                # cumulative effect at 1/1/Year 3
prior_to_y2_effect = diff[1]              # portion relating to periods before Year 2
y2_income_effect = r(cum_effect_bd_y3 - prior_to_y2_effect)  # Year 2 restatement effect

# Retrospective entry at 1/1/Year 3: FIFO inventory is LOWER than average cost,
# so inventory is credited (reduced) and retained earnings is debited.
je_c_amount = r(abs(cum_effect_bd_y3))
inventory_is_reduced = cum_effect_bd_y3 < 0

# Dec 31, Year 2 inventory reported on Year 3 comparative balance sheets = FIFO.
inv_dec31_y2_reported = oak_fifo[2]

# ---------------- Settlement of the cumulative effect (part e) --------------
delta_assets = r(cum_effect_bd_y3)        # inventory (an asset) change
delta_liabilities = r("0")
delta_equity = r(cum_effect_bd_y3)        # all of it flows to retained earnings
balanced = (delta_assets == r(delta_liabilities + delta_equity))

# ---------------- Journal entries -------------------------------------------
journal_entries = [
    {"part": "a",
     "lines": [
         {"account": "No entry required — change to LIFO applied prospectively; "
                     "Dec 31 Year 2 FIFO carrying amount becomes the LIFO base layer",
          "debit": n(je_a_amount), "credit": n(je_a_amount)}
     ]},
    {"part": "c",
     "lines": (
         [{"account": "Retained Earnings", "debit": n(je_c_amount), "credit": 0},
          {"account": "Inventory", "debit": 0, "credit": n(je_c_amount)}]
         if inventory_is_reduced else
         [{"account": "Inventory", "debit": n(je_c_amount), "credit": 0},
          {"account": "Retained Earnings", "debit": 0, "credit": n(je_c_amount)}]
     )},
]
for je in journal_entries:
    assert r(sum(Decimal(str(l["debit"])) for l in je["lines"])) == \
           r(sum(Decimal(str(l["credit"])) for l in je["lines"]))
assert balanced

# ---------------- Answers ----------------------------------------------------
answers = [
    {"label": "a: Part A — Jan 1, Year 3 journal entry amount for the change to LIFO "
              "(no entry: change to LIFO with impracticable prior layers is applied "
              "prospectively, so there is no cumulative effect to record)",
     "value": n(je_a_amount)},

    {"label": "b: Year 1 — inventory method reported after the change",
     "value": method_a(1)},
    {"label": "b: Year 1 — net income", "value": n(pinecrest[1]["ni"])},
    {"label": "b: Year 1 — ending inventory", "value": n(pinecrest[1]["ei"])},
    {"label": "b: Year 2 — inventory method reported after the change",
     "value": method_a(2)},
    {"label": "b: Year 2 — net income", "value": n(pinecrest[2]["ni"])},
    {"label": "b: Year 2 — ending inventory", "value": n(pinecrest[2]["ei"])},
    {"label": "b: Year 3 — inventory method reported after the change",
     "value": method_a(3)},
    {"label": "b: Year 3 — net income", "value": n(pinecrest[3]["ni"])},
    {"label": "b: Year 3 — ending inventory", "value": n(pinecrest[3]["ei"])},
    {"label": "b: LIFO base-layer amount (Jan 1, Year 3 beginning inventory)",
     "value": n(lifo_base_layer)},

    {"label": "c: Part B — cumulative effect at Jan 1, Year 3 (FIFO $150,000 less "
              "average cost $180,000): debit Retained Earnings / credit Inventory",
     "value": n(je_c_amount)},

    {"label": "d: Inventory reported at December 31, Year 2 on the Year 3 "
              "comparative balance sheets (restated to FIFO)",
     "value": n(inv_dec31_y2_reported)},
    {"label": "d: Decrease in beginning retained earnings of Year 2 for periods "
              "prior to Year 2 (FIFO $120,000 less average cost $140,000)",
     "value": n(abs(prior_to_y2_effect))},

    {"label": "e: Settlement — change in assets (Inventory), decrease",
     "value": n(delta_assets)},
    {"label": "e: Settlement — change in liabilities", "value": n(delta_liabilities)},
    {"label": "e: Settlement — change in equity (Retained Earnings), decrease",
     "value": n(delta_equity)},
]

notes = (
    "Part A(a): no journal entry — a change to LIFO whose prior-year layers cannot be "
    "reconstructed is applied prospectively; the Dec 31, Year 2 FIFO carrying amount of "
    "$180,000 is simply carried forward as the Year 3 beginning inventory and becomes the "
    "LIFO base layer. Part A(b): Years 1 and 2 are NOT restated — they stay on FIFO as "
    "originally reported; only Year 3 is on LIFO, and disclosure of the nature of and "
    "reason for the change plus the reason prior-period restatement is impracticable is "
    "required. Part B: FIFO ending inventory is lower than average cost in both years, so "
    "the cumulative effect is a reduction. Difference at Dec 31, Year 1 = $20,000 (relates "
    "to periods before Year 2, adjusting beginning retained earnings of Year 2); difference "
    "at Dec 31, Year 2 = $30,000; the $10,000 increment restates Year 2 income (higher cost "
    "of goods sold, lower net income) and is not a retained-earnings-only adjustment. "
    "Part e: Assets -$30,000 = Liabilities $0 + Equity -$30,000; equation stays in balance, "
    "with the entire equity change absorbed by retained earnings (no income-statement "
    "account of Year 3 is touched)."
)

print(json.dumps({
    "id": "agent_193#02",
    "rounding_convention": "decimal.Decimal throughout; every amount quantized to "
                           "$0.01 with ROUND_HALF_UP, applied independently per period "
                           "(no float arithmetic, no chained rounding). Given data are "
                           "whole dollars, so all results are exact whole dollars.",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
