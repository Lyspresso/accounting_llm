#!/usr/bin/env python3
"""Blind solver for item agent_221#00 (ACCOUNT-343, LO 13-5).

Fact pattern (from stem.md only)
-------------------------------
Solstice Media Group (calendar-year, PUBLIC company) buys 100% of Tidewater
Podcasts LLC for $875,000 cash on 1/1/Year 1. Identifiable assets and
liabilities are recorded at fair value; the residual is goodwill.

Acquisition-date fair values
    Cash                                     55,000
    Accounts receivable                     125,000
    Inventory                               110,000
    Property, plant, and equipment (net)    480,000
    Brand name (indefinite, renewable)       90,000
    Customer relationships (6-yr finite)     48,000
    Acquired IPR&D (incomplete project)      65,000
    ---------------------------------------------------
    Total assets at fair value              973,000

    Accounts payable                         80,000
    Long-term debt                          210,000
    ---------------------------------------------------
    Total liabilities at fair value         290,000

No private-company goodwill amortization alternative is elected.  No
impairment in Years 1-2.  Customer relationships amortize straight-line over
6 years, zero residual.  On 6/30/Year 3 the brand name is sold for $78,000
cash; no amortization was ever recorded on it.

Accounting policy applied
-------------------------
* Goodwill = consideration transferred - fair value of identifiable net
  assets (ASC 805-30-30-1).  Goodwill is NOT amortized (ASC 350-20-35-1);
  the private-company alternative is expressly not elected, and the entity
  is public, so it would not be available regardless.
* Brand name renewable indefinitely  -> indefinite life -> no amortization
  (ASC 350-30-35-1).
* Acquired IPR&D from a business combination is capitalized at fair value
  as an INDEFINITE-life intangible and is not amortized until the project is
  completed (then reclassified to finite-life) or abandoned.  The project is
  still incomplete through Year 2, so no amortization.
* Customer relationships: finite 6-year life, straight-line, zero residual.
  Acquired 1/1/Year 1, so a full year of amortization in Year 1 and Year 2.
  Following the textbook's most-common presentation (Chapter 13, Demo 13-2),
  amortization is credited directly to the intangible asset account; crediting
  an "Accumulated Amortization" contra account is an accepted alternative and
  does not change any carrying amount below.
* Disposal of the brand name: derecognize the full $90,000 carrying amount
  (no amortization, no impairment), recognize gain/loss versus proceeds.
  Because the asset is not amortized, no partial-year catch-up is needed at
  the 6/30/Year 3 disposal date.

Rounding convention
-------------------
ROUND_HALF_UP to the cent, applied per period (each year's amortization is
rounded on its own before being carried forward), using decimal.Decimal
throughout -- no binary floats anywhere.  Every figure in this fact pattern
happens to divide evenly ($48,000 / 6 = $8,000.00 exactly), so rounding never
actually bites here, but the convention is applied deliberately rather than
assumed away.  No present-value work is required by this item, so no PV table
factors are used.  Output values are emitted as whole dollars when the cent
component is zero.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Coerce to Decimal and round HALF_UP to the cent (per-period rounding)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def out(d: Decimal):
    """Emit a Decimal as int when whole, else as a 2-dp float-free string."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem; nothing here is an answer figure)
# ---------------------------------------------------------------------------
CONSIDERATION = money("875000")

FV_ASSETS = {
    "Cash": money("55000"),
    "Accounts Receivable": money("125000"),
    "Inventory": money("110000"),
    "Property, Plant, and Equipment": money("480000"),
    "Brand Name": money("90000"),
    "Customer Relationships": money("48000"),
    "Acquired In-Process Research and Development": money("65000"),
}

FV_LIABILITIES = {
    "Accounts Payable": money("80000"),
    "Long-Term Debt": money("210000"),
}

CR_LIFE_YEARS = 6                       # customer relationships useful life
CR_RESIDUAL = money("0")
BRAND_PROCEEDS = money("78000")         # 6/30/Year 3 sale


# ---------------------------------------------------------------------------
# (a) Fair value of identifiable net assets and goodwill
# ---------------------------------------------------------------------------
total_fv_assets = money(sum(FV_ASSETS.values()))
total_fv_liabilities = money(sum(FV_LIABILITIES.values()))
fv_identifiable_net_assets = money(total_fv_assets - total_fv_liabilities)
goodwill = money(CONSIDERATION - fv_identifiable_net_assets)

# Cross-check against the stem's stated fair-value totals (not reported).
assert total_fv_assets == money("973000"), total_fv_assets
assert total_fv_liabilities == money("290000"), total_fv_liabilities


# ---------------------------------------------------------------------------
# (b) January 1, Year 1 initial recognition journal entry
# ---------------------------------------------------------------------------
je_b_lines = []
for acct, amt in FV_ASSETS.items():
    je_b_lines.append({"account": acct, "debit": out(amt), "credit": 0})
je_b_lines.append({"account": "Goodwill", "debit": out(goodwill), "credit": 0})
for acct, amt in FV_LIABILITIES.items():
    je_b_lines.append({"account": acct, "debit": 0, "credit": out(amt)})
je_b_lines.append(
    {"account": "Cash (consideration paid)", "debit": 0,
     "credit": out(CONSIDERATION)}
)


# ---------------------------------------------------------------------------
# (c) Two-year subsequent measurement / carrying-amount schedule
# ---------------------------------------------------------------------------
def straight_line(cost: Decimal, residual: Decimal, life: int) -> Decimal:
    """Annual straight-line amortization, rounded HALF_UP per period."""
    return money((cost - residual) / Decimal(life))


cr_annual_amort = straight_line(FV_ASSETS["Customer Relationships"],
                                CR_RESIDUAL, CR_LIFE_YEARS)

schedule = {}


def roll(name: str, cost: Decimal, annual_amort: Decimal, years=(1, 2)):
    """Build a beginning/amortization/ending schedule for `years`."""
    rows = []
    carrying = cost
    for yr in years:
        begin = carrying
        amort = money(annual_amort)
        end = money(begin - amort)
        rows.append({
            "year": yr,
            "beginning_carrying_amount": out(begin),
            "amortization": out(amort),
            "ending_carrying_amount": out(end),
        })
        carrying = end
    schedule[name] = rows
    return rows


ZERO = money("0")
roll("Brand name (indefinite life)", FV_ASSETS["Brand Name"], ZERO)
roll("Acquired IPR&D (indefinite until complete)",
     FV_ASSETS["Acquired In-Process Research and Development"], ZERO)
roll("Goodwill (not amortized)", goodwill, ZERO)
roll("Customer relationships (6-year finite life)",
     FV_ASSETS["Customer Relationships"], cr_annual_amort)

cr_end_y1 = Decimal(str(schedule["Customer relationships (6-year finite life)"][0]
                        ["ending_carrying_amount"]))
cr_end_y2 = Decimal(str(schedule["Customer relationships (6-year finite life)"][1]
                        ["ending_carrying_amount"]))


# ---------------------------------------------------------------------------
# (d) December 31, Year 1 and Year 2 period-end adjusting entries
# ---------------------------------------------------------------------------
def amort_entry(part_label: str, amount: Decimal):
    return {
        "part": part_label,
        "lines": [
            {"account": "Amortization Expense", "debit": out(amount),
             "credit": 0},
            {"account": "Customer Relationships", "debit": 0,
             "credit": out(amount)},
        ],
    }


je_d_y1 = amort_entry("d (December 31, Year 1)", cr_annual_amort)
je_d_y2 = amort_entry("d (December 31, Year 2)", cr_annual_amort)


# ---------------------------------------------------------------------------
# (e) Goodwill roll-forward, 1/1/Year 1 through 12/31/Year 2
# ---------------------------------------------------------------------------
gw_rollforward = []
gw_balance = money("0")
for yr, additions in ((1, goodwill), (2, money("0"))):
    begin = gw_balance
    end = money(begin + additions)          # amortization is zero by policy
    gw_rollforward.append({
        "year": yr,
        "beginning_balance": out(begin),
        "goodwill_from_acquisitions": out(additions),
        "amortization": 0,
        "ending_balance": out(end),
    })
    gw_balance = end


# ---------------------------------------------------------------------------
# (f) June 30, Year 3 disposal of the brand name
# ---------------------------------------------------------------------------
brand_carrying_at_disposal = FV_ASSETS["Brand Name"]   # never amortized
gain_loss = money(BRAND_PROCEEDS - brand_carrying_at_disposal)   # negative=loss
loss_on_sale = money(-gain_loss) if gain_loss < 0 else money("0")
gain_on_sale = money(gain_loss) if gain_loss > 0 else money("0")

je_f_lines = [{"account": "Cash", "debit": out(BRAND_PROCEEDS), "credit": 0}]
if loss_on_sale > 0:
    je_f_lines.append({"account": "Loss on Sale of Intangible Asset",
                       "debit": out(loss_on_sale), "credit": 0})
je_f_lines.append({"account": "Brand Name", "debit": 0,
                   "credit": out(brand_carrying_at_disposal)})
if gain_on_sale > 0:
    je_f_lines.append({"account": "Gain on Sale of Intangible Asset",
                       "debit": 0, "credit": out(gain_on_sale)})


# ---------------------------------------------------------------------------
# (g) Year-2 balance-sheet presentation
# ---------------------------------------------------------------------------
other_intangibles_y2 = money(
    FV_ASSETS["Brand Name"]
    + FV_ASSETS["Acquired In-Process Research and Development"]
    + cr_end_y2
)

presentation_g = (
    "Goodwill is presented as a separate line item in the balance sheet, apart "
    "from all other intangible assets (ASC 350-20-45-1): Goodwill $"
    f"{out(goodwill):,}. The other intangibles are reported together as "
    "'Intangible assets, net' of $"
    f"{out(other_intangibles_y2):,} at December 31, Year 2 - indefinite-life "
    "brand name $"
    f"{out(FV_ASSETS['Brand Name']):,} and acquired IPR&D $"
    f"{out(FV_ASSETS['Acquired In-Process Research and Development']):,} "
    "carried at cost with no amortization, plus finite-life customer "
    "relationships net of accumulated amortization $"
    f"{out(cr_end_y2):,}. Goodwill and the indefinite-life intangibles are not "
    "amortized (they are tested for impairment instead); only the customer "
    "relationships are amortized, and finite- versus indefinite-life "
    "intangibles are disclosed separately in the notes."
)


# ---------------------------------------------------------------------------
# Journal-entry balance proof
# ---------------------------------------------------------------------------
journal_entries = [
    {"part": "b (January 1, Year 1 - acquisition)", "lines": je_b_lines},
    je_d_y1,
    je_d_y2,
    {"part": "f (June 30, Year 3 - sale of brand name)", "lines": je_f_lines},
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), (je["part"], dr, cr)


# ---------------------------------------------------------------------------
# Required-part answers only
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: fair value of identifiable net assets acquired, January 1, Year 1",
     "value": out(fv_identifiable_net_assets)},
    {"label": "a: goodwill recorded, January 1, Year 1",
     "value": out(goodwill)},

    {"label": "c: Brand name - Year 1 amortization", "value": 0},
    {"label": "c: Brand name - carrying amount, December 31, Year 1",
     "value": out(FV_ASSETS["Brand Name"])},
    {"label": "c: Brand name - Year 2 amortization", "value": 0},
    {"label": "c: Brand name - carrying amount, December 31, Year 2",
     "value": out(FV_ASSETS["Brand Name"])},

    {"label": "c: Acquired IPR&D - Year 1 amortization", "value": 0},
    {"label": "c: Acquired IPR&D - carrying amount, December 31, Year 1",
     "value": out(FV_ASSETS["Acquired In-Process Research and Development"])},
    {"label": "c: Acquired IPR&D - Year 2 amortization", "value": 0},
    {"label": "c: Acquired IPR&D - carrying amount, December 31, Year 2",
     "value": out(FV_ASSETS["Acquired In-Process Research and Development"])},

    {"label": "c: Goodwill - Year 1 amortization", "value": 0},
    {"label": "c: Goodwill - carrying amount, December 31, Year 1",
     "value": out(goodwill)},
    {"label": "c: Goodwill - Year 2 amortization", "value": 0},
    {"label": "c: Goodwill - carrying amount, December 31, Year 2",
     "value": out(goodwill)},

    {"label": "c: Customer relationships - Year 1 amortization",
     "value": out(cr_annual_amort)},
    {"label": "c: Customer relationships - carrying amount, December 31, Year 1",
     "value": out(cr_end_y1)},
    {"label": "c: Customer relationships - Year 2 amortization",
     "value": out(cr_annual_amort)},
    {"label": "c: Customer relationships - carrying amount, December 31, Year 2",
     "value": out(cr_end_y2)},

    {"label": "e: goodwill roll-forward - beginning balance, January 1, Year 1",
     "value": out(Decimal(str(gw_rollforward[0]["beginning_balance"])))},
    {"label": "e: goodwill roll-forward - goodwill acquired, Year 1",
     "value": out(goodwill)},
    {"label": "e: goodwill roll-forward - amortization, Years 1-2", "value": 0},
    {"label": "e: goodwill roll-forward - ending balance, December 31, Year 1",
     "value": out(Decimal(str(gw_rollforward[0]["ending_balance"])))},
    {"label": "e: goodwill roll-forward - ending balance, December 31, Year 2",
     "value": out(Decimal(str(gw_rollforward[1]["ending_balance"])))},

    {"label": "f: loss on sale of brand name, June 30, Year 3",
     "value": out(loss_on_sale)},

    {"label": "g: Year-2 balance-sheet presentation of goodwill vs. other intangibles",
     "value": presentation_g},
]

result = {
    "id": "agent_221#00",
    "rounding_convention": (
        "decimal.Decimal only (no floats); ROUND_HALF_UP to the cent applied "
        "per period, each year's amortization rounded before being carried "
        "forward; straight-line amortization computed from acquisition-date "
        "fair value less zero residual over the 6-year life; no present-value "
        "work required, so no PV table factors used"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "supporting_schedules": {
        "c_subsequent_measurement": schedule,
        "e_goodwill_rollforward": gw_rollforward,
    },
    "insufficient_info": False,
    "notes": (
        "Goodwill = $875,000 consideration - $683,000 fair value of "
        "identifiable net assets ($973,000 assets - $290,000 liabilities). "
        "Brand name, acquired IPR&D, and goodwill are all indefinite-lived and "
        "are not amortized, so the only period-end entries in part d are the "
        "$8,000 annual customer-relationship amortization ($48,000 / 6). "
        "Amortization is credited directly to the intangible account per the "
        "textbook's most-common presentation; an Accumulated Amortization "
        "contra account is an equally acceptable alternative. The brand name "
        "carries at $90,000 on 6/30/Year 3, so the $78,000 sale produces a "
        "$12,000 loss."
    ),
}

print(json.dumps(result, indent=2))
