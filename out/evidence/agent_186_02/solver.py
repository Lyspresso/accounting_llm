#!/usr/bin/env python3
"""
Solver for item agent_186#02 — Harborline Sporting Goods LLC.

Topic: LO 9-8 dollar-value LIFO (single pool), multi-year layer build-up followed
by a Year 4 liquidation, plus the LIFO reserve rollforward and the December 31,
Year 4 adjusting entry (LO 9-6 / LO 9-7).

FACT PATTERN (taken from stem.md, nothing else):
    FIFO for internal books, dollar-value LIFO (single pool) for external/tax.
    Base year = Year 1.
        Year | Ending inventory at FIFO | Price index
        1    | 120,000                  | 1.00
        2    | 151,200                  | 1.20
        3    | 175,500                  | 1.30
        4    | 137,500                  | 1.25

METHOD (textbook four steps, chapter 9 LO 9-8):
    1. Restate ending inventory at base-year dollars:  FIFO EI / current index.
    2. Arrange the restated balance into layers, oldest first. A new layer is
       added when the restated balance rises; when it falls, layers are
       liquidated NEWEST FIRST (and a liquidation may cut into the base layer).
    3. Match each surviving layer to the index of the year it originated in.
       If no new layer is created in a year, that year's index is never used in
       the DV LIFO total (it is used only in step 1 to deflate).
    4. Restate each layer to current dollars (layer at base-year $ x its own
       index) and sum.

    LIFO reserve = FIFO inventory - DV LIFO inventory (an allowance/contra
    account: "Allowance to Reduce FIFO Inventory to LIFO Basis").
    The year-end adjusting entry records the CHANGE in that allowance against
    Cost of Goods Sold.  Reserve increases -> debit COGS / credit Allowance.
    Reserve decreases (layer liquidation settlement) -> debit Allowance /
    credit COGS.

ROUNDING CONVENTION:
    ROUND_HALF_UP, applied per period (never at the end only), using
    decimal.Decimal exclusively — no binary floats anywhere.
      * Base-year-dollar restatements (FIFO EI / index) are rounded to the cent
        (0.01) in the period they are computed, and that rounded figure is the
        one carried into the layer schedule for the following year.
      * Each layer extended to current dollars (base-year layer x index) is
        rounded to the cent, then the rounded extensions are summed.
      * Reserve balances and the adjusting-entry amount are differences of
        already-rounded figures, so no further rounding is introduced.
      * Price indices are exact Decimals as stated (1.00 / 1.20 / 1.30 / 1.25);
        no PV table factors are involved in this item.
    Every figure in this particular fact pattern happens to land on a whole
    dollar, so the convention does not change any reported number — it is
    applied deliberately all the same.

Run:  python3 solver.py      -> prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """ROUND_HALF_UP to the cent, applied at the point of computation."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly: whole dollars as int, otherwise float-free string->float."""
    x = money(x)
    if x == x.to_integral_value():
        return int(x)
    return float(x)  # only reached if a cent remainder exists; none here


# ---------------------------------------------------------------- fact pattern
YEARS = [1, 2, 3, 4]
FIFO_EI = {
    1: Decimal("120000"),
    2: Decimal("151200"),
    3: Decimal("175500"),
    4: Decimal("137500"),
}
INDEX = {
    1: Decimal("1.00"),
    2: Decimal("1.20"),
    3: Decimal("1.30"),
    4: Decimal("1.25"),
}
BASE_YEAR = 1


# ------------------------------------------------- steps 1-4, year by year
# A layer is a dict: {"year": origin year, "base": base-year dollars, "index": index}
layers = []                 # oldest first
prior_base_total = Decimal("0")

dv_lifo = {}                # year -> DV LIFO ending inventory
base_restated = {}          # year -> ending inventory at base-year dollars
layer_detail = {}           # year -> surviving layers after that year's activity
liquidations = {}           # year -> list of (origin year, base-$ removed)
indices_used = {}           # year -> sorted list of origin years whose index is used
new_layer_added = {}        # year -> bool

for yr in YEARS:
    # Step 1: restate ending inventory at base-year dollars.
    restated = money(FIFO_EI[yr] / INDEX[yr])
    base_restated[yr] = restated

    # Step 2: arrange into layers, oldest first; newest layers drop first.
    removed = []
    if restated > prior_base_total:
        increment = restated - prior_base_total
        layers.append({"year": yr, "base": increment, "index": INDEX[yr]})
        new_layer_added[yr] = True
    elif restated < prior_base_total:
        new_layer_added[yr] = False
        shortfall = prior_base_total - restated
        # liquidate from the newest layer backwards
        while shortfall > 0 and layers:
            top = layers[-1]
            take = top["base"] if top["base"] <= shortfall else shortfall
            top["base"] -= take
            removed.append((top["year"], take))
            shortfall -= take
            if top["base"] == 0:
                layers.pop()
        if shortfall > 0:
            raise ValueError("Restated balance below zero — impossible layering.")
    else:
        new_layer_added[yr] = False

    liquidations[yr] = removed

    # Steps 3 and 4: match each surviving layer to its origin-year index and
    # extend to current dollars; round each extension, then sum.
    total = Decimal("0")
    detail = []
    for lay in layers:
        extended = money(lay["base"] * lay["index"])
        total += extended
        detail.append(
            {
                "layer_year": lay["year"],
                "base_year_dollars": num(lay["base"]),
                "index": str(lay["index"]),
                "at_current_dollars": num(extended),
            }
        )
    dv_lifo[yr] = money(total)
    layer_detail[yr] = detail
    indices_used[yr] = sorted({lay["year"] for lay in layers})
    prior_base_total = restated


# ------------------------------------------------- LIFO reserve rollforward
reserve = {}        # year -> ending LIFO reserve balance
adjustment = {}     # year -> change in the reserve (positive = increase)
prior_reserve = Decimal("0")
for yr in YEARS:
    reserve[yr] = money(FIFO_EI[yr] - dv_lifo[yr])
    adjustment[yr] = money(reserve[yr] - prior_reserve)
    prior_reserve = reserve[yr]


# ------------------------------------------------- (c) December 31, Year 4 JE
adj4 = adjustment[4]
ALLOWANCE = "Allowance to Reduce FIFO Inventory to LIFO Basis"
if adj4 < 0:
    # reserve decreased -> debit the allowance, credit COGS
    amt = -adj4
    je_lines = [
        {"account": ALLOWANCE, "debit": num(amt), "credit": 0},
        {"account": "Cost of Goods Sold", "debit": 0, "credit": num(amt)},
    ]
elif adj4 > 0:
    je_lines = [
        {"account": "Cost of Goods Sold", "debit": num(adj4), "credit": 0},
        {"account": ALLOWANCE, "debit": 0, "credit": num(adj4)},
    ]
else:
    je_lines = []

# proof: debits must equal credits
dr = sum(Decimal(str(l["debit"])) for l in je_lines)
cr = sum(Decimal(str(l["credit"])) for l in je_lines)
assert dr == cr, f"Entry out of balance: {dr} vs {cr}"


# ------------------------------------------------- narrative for (a) and (d)
liq4 = liquidations[4]
liq_words = []
for origin, amt in liq4:
    tag = "base layer" if origin == BASE_YEAR else f"Year {origin} layer"
    liq_words.append(f"{tag} reduced by ${num(amt):,} of base-year dollars")

unused = [y for y in YEARS if not new_layer_added[y] and y != BASE_YEAR]
unused_txt = ", ".join(f"Year {y} (index {INDEX[y]})" for y in unused) or "none"

notes = (
    "(a) Layers at base-year dollars after each year: "
    + "; ".join(
        f"Yr {y}: " + ", ".join(
            f"{'base' if d['layer_year'] == BASE_YEAR else 'Yr ' + str(d['layer_year'])}"
            f"={d['base_year_dollars']:,}"
            for d in layer_detail[y]
        )
        for y in YEARS
    )
    + f". Year 4 restated balance ${num(base_restated[4]):,} at base-year dollars is below the "
      f"prior Year 3 balance of ${num(base_restated[3]):,}, so layers liquidate newest first: "
    + "; ".join(liq_words)
    + ". Only the base layer survives at Year 4 year-end. "
    + f"Index not used in the DV LIFO extension: {unused_txt}. "
    "(d) The Year 4 index of 1.25 is used only in Step 1, to deflate the $137,500 FIFO balance "
    "to base-year dollars. Because that restated balance fell rather than rose, no Year 4 layer "
    "was created, and Step 3 matches each surviving layer to the index of the year it originated "
    "in — so 1.25 never multiplies anything in the Year 4 total, which is carried entirely at the "
    "base-year index of 1.00. Presentation: inventory stays a current asset, reported on the "
    "external balance sheet at the dollar-value LIFO amount — FIFO inventory of $137,500 less the "
    "Allowance to Reduce FIFO Inventory to LIFO Basis (a contra-inventory account) of $27,500, "
    "net $110,000. The LIFO reserve balance and the fact that Year 4 income includes the effect of "
    "a LIFO liquidation (older, lower-cost layers charged to cost of goods sold) should be "
    "disclosed in the notes."
)

answers = []
for y in YEARS:
    answers.append(
        {"label": f"a: dollar-value LIFO ending inventory, Year {y}", "value": num(dv_lifo[y])}
    )
for y in YEARS:
    answers.append(
        {"label": f"b: LIFO reserve balance at end of Year {y}", "value": num(reserve[y])}
    )
for y in YEARS:
    answers.append(
        {
            "label": f"b: LIFO reserve adjustment for Year {y} (positive = increase)",
            "value": num(adjustment[y]),
        }
    )

out = {
    "id": "agent_186#02",
    "rounding_convention": (
        "decimal.Decimal only, ROUND_HALF_UP to the cent applied per period: base-year "
        "restatements (FIFO EI / index) rounded when computed and carried forward rounded; each "
        "layer extension (base-year layer x origin-year index) rounded before summing. No PV "
        "factors in this item. All figures land on whole dollars."
    ),
    "answers": answers,
    "journal_entries": [{"part": "c", "date": "December 31, Year 4", "lines": je_lines}],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
