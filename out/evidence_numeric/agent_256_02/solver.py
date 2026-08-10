"""
Q3 agent_256#02 -- Change to LIFO when retrospective application is impracticable.

Rounding convention: decimal.Decimal throughout, ROUND_HALF_UP applied per period
(each period's computed figure is rounded to the cent independently, never floats).
All inputs are whole dollars, so no residual rounding arises; the convention is
stated and enforced anyway.

Derivation only -- every reported figure is computed from the scenario data table.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def r(x):
    """ROUND_HALF_UP to the cent, per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


D = Decimal

# ---- Scenario data (given) ----
data = {
    1: {"bi": D("0"),      "pur": D("200000"), "ei": D("58000"), "sales": D("250000"), "opex": D("42000")},
    2: {"bi": D("58000"),  "pur": D("235000"), "ei": D("72000"), "sales": D("310000"), "opex": D("45000")},
    3: {"bi": D("72000"),  "pur": D("260000"), "ei": D("64000"), "sales": D("340000"), "opex": D("47000")},
}
fifo_y3_ei_hypothetical = D("90000")

# ---- Core COGS engine: COGS = BI + Purchases - EI ----
def cogs_of(bi, pur, ei):
    return r(bi + pur - ei)


def gap(bi, pur):
    """Goods available for sale."""
    return r(bi + pur)


sched = {}
for yr, d in data.items():
    g = gap(d["bi"], d["pur"])
    c = cogs_of(d["bi"], d["pur"], d["ei"])
    gp = r(d["sales"] - c)
    ni = r(gp - d["opex"])
    sched[yr] = {"bi": r(d["bi"]), "pur": r(d["pur"]), "gap": g, "ei": r(d["ei"]),
                 "cogs": c, "sales": r(d["sales"]), "gp": gp, "opex": d["opex"], "ni": ni}

# ---- Part b: cumulative effect at 1/1/Y3 ----
# Prospective application: LIFO base layer = FIFO ending inventory at 12/31/Y2
# carried forward unchanged as the Y3 beginning (base) LIFO layer.
lifo_base_layer = r(data[2]["ei"])
carry_in_y3 = r(data[3]["bi"])
cumulative_effect = r(carry_in_y3 - lifo_base_layer)   # must be zero -> no JE

# ---- Part d: Year 3 under prospective LIFO (period-end measurement) ----
y3 = sched[3]

# LIFO layer decomposition of Y3 ending inventory ($64,000 vs base $72,000):
# ending LIFO inventory is BELOW the base layer -> base layer partially liquidated.
y3_layer_liquidation = r(lifo_base_layer - data[3]["ei"])
y3_new_layer = r(max(D("0"), data[3]["ei"] - lifo_base_layer))
y3_base_layer_remaining = r(min(lifo_base_layer, data[3]["ei"]))

# ---- Part e: contrast, continued FIFO in Year 3 ----
e_cogs = cogs_of(data[3]["bi"], data[3]["pur"], fifo_y3_ei_hypothetical)
e_gp = r(data[3]["sales"] - e_cogs)
e_ni = r(e_gp - data[3]["opex"])
e_ni_diff = r(e_ni - y3["ni"])
e_cogs_diff = r(y3["cogs"] - e_cogs)

# ---- Balance check for the (nil) JE ----
je_b_lines = []  # deliberately empty: no entry is made
dr = sum((D(l["debit"]) for l in je_b_lines), D("0"))
cr = sum((D(l["credit"]) for l in je_b_lines), D("0"))
assert dr == cr, "Dr must equal Cr"
assert cumulative_effect == 0, "prospective adoption must carry BI forward unchanged"
# schedule ties out: total COGS over 3 yrs = total GAFS - final EI chain
assert sched[3]["gap"] - sched[3]["ei"] == sched[3]["cogs"]


def f(x):
    return float(x)


answers = [
    # a
    {"label": "a: Retrospective application required? (1 = yes, 0 = no -- not required; ASC 250-10-45-9 impracticability exception applies)", "value": 0},
    {"label": "a: LIFO is applied prospectively beginning January 1, Year 3; number of prior years restated", "value": 0},
    # b
    {"label": "b: Cumulative-effect adjustment to January 1, Year 3 retained earnings (none is recorded)", "value": f(cumulative_effect)},
    {"label": "b: LIFO base layer at January 1, Year 3 = Year 2 FIFO ending inventory carried forward", "value": f(lifo_base_layer)},
    # c -- three-year comparative COGS schedule
    {"label": "c: Year 1 (FIFO) beginning inventory", "value": f(sched[1]["bi"])},
    {"label": "c: Year 1 (FIFO) purchases", "value": f(sched[1]["pur"])},
    {"label": "c: Year 1 (FIFO) goods available for sale", "value": f(sched[1]["gap"])},
    {"label": "c: Year 1 (FIFO) ending inventory", "value": f(sched[1]["ei"])},
    {"label": "c: Year 1 (FIFO) cost of goods sold", "value": f(sched[1]["cogs"])},
    {"label": "c: Year 2 (FIFO) beginning inventory", "value": f(sched[2]["bi"])},
    {"label": "c: Year 2 (FIFO) purchases", "value": f(sched[2]["pur"])},
    {"label": "c: Year 2 (FIFO) goods available for sale", "value": f(sched[2]["gap"])},
    {"label": "c: Year 2 (FIFO) ending inventory", "value": f(sched[2]["ei"])},
    {"label": "c: Year 2 (FIFO) cost of goods sold", "value": f(sched[2]["cogs"])},
    {"label": "c: Year 3 (LIFO) beginning inventory (FIFO carryover = LIFO base layer)", "value": f(sched[3]["bi"])},
    {"label": "c: Year 3 (LIFO) purchases", "value": f(sched[3]["pur"])},
    {"label": "c: Year 3 (LIFO) goods available for sale", "value": f(sched[3]["gap"])},
    {"label": "c: Year 3 (LIFO) ending inventory", "value": f(sched[3]["ei"])},
    {"label": "c: Year 3 (LIFO) cost of goods sold", "value": f(sched[3]["cogs"])},
    # d -- Year 3 net income under prospective LIFO
    {"label": "d: Year 3 sales", "value": f(sched[3]["sales"])},
    {"label": "d: Year 3 cost of goods sold (LIFO)", "value": f(sched[3]["cogs"])},
    {"label": "d: Year 3 gross profit (LIFO)", "value": f(sched[3]["gp"])},
    {"label": "d: Year 3 operating expenses", "value": f(sched[3]["opex"])},
    {"label": "d: Year 3 net income under prospective LIFO", "value": f(sched[3]["ni"])},
    {"label": "d: Year 3 LIFO base layer remaining at 12/31/Year 3", "value": f(y3_base_layer_remaining)},
    {"label": "d: Year 3 new LIFO layer added", "value": f(y3_new_layer)},
    {"label": "d: Year 3 base-layer liquidation (decrement below the $72,000 base)", "value": f(y3_layer_liquidation)},
    # e -- contrast under continued FIFO
    {"label": "e: Year 3 COGS if FIFO continued (ending inventory $90,000)", "value": f(e_cogs)},
    {"label": "e: Year 3 gross profit if FIFO continued", "value": f(e_gp)},
    {"label": "e: Year 3 net income if FIFO continued", "value": f(e_ni)},
    {"label": "e: Year 3 COGS higher under LIFO than continued FIFO", "value": f(e_cogs_diff)},
    {"label": "e: Year 3 net income higher under continued FIFO than under LIFO", "value": f(e_ni_diff)},
    # f
    {"label": "f: Number of comparative years on the Year 3 report presented under FIFO (Year 1 and Year 2, unrestated)", "value": 2},
    {"label": "f: Number of years presented under LIFO on the Year 3 report (Year 3 only)", "value": 1},
    {"label": "f: Prior-period financial statements restated or retrospectively adjusted", "value": 0},
]

notes = (
    "a. No. ASC 250-10-45-5 requires retrospective application, but ASC 250-10-45-9 provides that when "
    "retrospective application to all prior periods is impracticable -- here the purchase-price history "
    "needed to reconstruct pre-Year 3 LIFO layers is unavailable after every reasonable effort, so the "
    "period-specific effects cannot be determined and no objective, contemporaneous assumptions can be made "
    "without hindsight -- the change is applied as of the earliest date practicable. A change to LIFO is the "
    "classic case: because LIFO cost flows depend on layer-by-layer historical purchase data, retrospective "
    "application is generally impracticable, so the change is applied PROSPECTIVELY from January 1, Year 3. "
    "b. No cumulative-effect journal entry is made. The Year 2 FIFO ending inventory of $72,000 becomes the "
    "Year 3 opening LIFO base layer without adjustment, so the cumulative effect on January 1, Year 3 retained "
    "earnings is $0 and no entry (Dr = Cr = $0) is recorded. "
    "c. Comparative schedule uses MIXED methods: Year 1 and Year 2 remain on FIFO exactly as originally "
    "reported (COGS $142,000 and $221,000); Year 3 is on LIFO ($72,000 + $260,000 - $64,000 = $268,000). "
    "d. Year 3: $340,000 - $268,000 = $72,000 gross profit, less $47,000 operating expenses = $25,000 net "
    "income (ignoring income taxes, which the problem does not supply). Period-end measurement: the $64,000 "
    "LIFO ending inventory is $8,000 BELOW the $72,000 base layer, so the base layer was partially liquidated "
    "-- $64,000 of base remains, no new layer was added, and $8,000 of old base-layer cost was charged to COGS. "
    "e. Under continued FIFO with $90,000 ending inventory: COGS $242,000, gross profit $98,000, net income "
    "$51,000 -- $26,000 more than under LIFO, because LIFO COGS is $26,000 higher. "
    "f. Presentation: the Year 3 report is internally inconsistent by design -- Year 1 and Year 2 columns stay "
    "on FIFO as previously issued (no restatement, no retained-earnings adjustment, no per-share restatement), "
    "while the Year 3 column is on LIFO. Disclose: (1) the nature of and reason for the change, including why "
    "LIFO is preferable; (2) that retrospective application was IMPRACTICABLE and the specific reasons -- prior "
    "LIFO layers cannot be reconstructed because purchase-price history for old layers is unavailable; (3) the "
    "method of applying the change and the date/earliest period from which it was applied prospectively "
    "(January 1, Year 3); (4) that the opening Year 3 inventory of $72,000 became the LIFO base layer; and "
    "(5) the effect of the change on Year 3 income from continuing operations, net income and per-share amounts, "
    "with the caution that comparability across the three years is impaired. Also note the base-layer "
    "liquidation of $8,000 and, if the LIFO conformity rule applies, that LIFO is used for tax purposes."
)

out = {
    "id": "agent_256#02",
    "rounding_convention": (
        "decimal.Decimal for all money; ROUND_HALF_UP applied per period (each period's "
        "COGS, gross profit and net income quantized to the cent independently). All source "
        "figures are whole dollars, so every reported amount is exact and the comparative "
        "schedule closes exactly: COGS = BI + Purchases - EI for each year, and the Year 3 "
        "LIFO layer roll-forward closes exactly to the $64,000 ending inventory."
    ),
    "answers": answers,
    "journal_entries": [
        {
            "part": "b",
            "lines": [],
            "memo": ("No January 1, Year 3 cumulative-effect journal entry is made. Retrospective "
                     "application is impracticable, so the change to LIFO is applied prospectively: the "
                     "$72,000 FIFO carrying amount at 12/31/Year 2 becomes the Year 3 opening LIFO base "
                     "layer with no adjustment. Cumulative effect on retained earnings = $0 (Dr = Cr = $0).")
        }
    ],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=None))
