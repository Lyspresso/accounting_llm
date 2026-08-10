#!/usr/bin/env python3
"""
Blind solver for item agent_135#01 (ACCOUNT-343, LO 14-3).

FACT PATTERN (taken only from stem.md)
--------------------------------------
Jan 1 Year 1: Riverton Mutual Fund Services buys, FOR PAR, $55,000 of Oakmont
Industries 9% bonds maturing Dec 31 Year 4.  Cash interest annually each Dec 31.
Classified AFS (FV-OCI).  Year-end Dec 31.  Beginning AOCI = 0.
    Dec 31 Y1 fair value $52,250
    Dec 31 Y2 fair value $57,200 (no sales in Y2)
    Jan  1 Y3 entire holding sold for $57,750 cash

METHOD
------
Purchased AT PAR, so there is no premium or discount: the effective rate equals
the stated rate and the AMORTIZED COST BASIS STAYS AT $55,000 on every
measurement date through the sale.  No amortization table is therefore needed,
and interest revenue each period equals the cash coupon.

AFS / FV-OCI per the course text (Demo 14-3A), "fair value adjustments at sale
date and period-end":
  * Investment account is carried at amortized cost; all fair-value movement is
    parked in a separate valuation account, Fair Value Adjustment--AFS (FVA).
  * Required FVA balance at any date = fair value - amortized cost
    (positive = debit balance, negative = credit balance).
  * Adjustment booked = required balance - existing balance, with the offset to
    Unrealized Gain or Loss--OCI.
  * On sale the investment is FIRST marked to fair value through OCI at the sale
    date; THEN the sale is recorded, which (1) removes the investment at
    amortized cost, (2) eliminates the FVA balance, (3) recognizes a realized
    Gain on Sale of Investment equal to cash proceeds - amortized cost, and
    (4) reclassifies the cumulative holding gain/loss out of AOCI by debiting
    Unrealized Gain or Loss--OCI for that same realized amount.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal, never float.  Every monetary result is quantized
to the cent with ROUND_HALF_UP, applied PER PERIOD / PER LINE at the moment the
figure is computed (round-per-period, not round-at-end), which is this course's
convention.  No present-value work is required for this item -- the bond was
purchased at par -- so no PV table factor versus exact formula choice arises.
Interest is a simple annual coupon: par x stated rate x 12/12.  Given the inputs
every figure here happens to land on a whole dollar, but the quantization is
still applied explicitly so the script would stay correct for cent-level inputs.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def q(x: Decimal) -> Decimal:
    """Quantize a money amount to the cent, ROUND_HALF_UP, per period/per line."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly plain number: int when whole, else float of the cent value."""
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ----------------------------------------------------------------------------
# Given facts (stem only)
# ----------------------------------------------------------------------------
PAR = Decimal("55000")            # face amount purchased "for par"
STATED_RATE = Decimal("0.09")     # 9% bonds
PERIODS_PER_YEAR = Decimal("1")   # cash interest paid annually
BEGINNING_AOCI = Decimal("0")     # "Beginning AOCI related to AFS is zero"

FV_Y1 = Decimal("52250")          # Dec 31, Year 1 fair value
FV_Y2 = Decimal("57200")          # Dec 31, Year 2 fair value
SALE_PROCEEDS = Decimal("57750")  # Jan 1, Year 3 cash received (entire holding)

INVESTMENT_ACCOUNT = "Investment in AFS Securities—Oakmont Bonds"

# ----------------------------------------------------------------------------
# (a) Purchase.  Bought at par => cost = face => amortized cost basis = par.
# ----------------------------------------------------------------------------
purchase_cost = q(PAR)

# Bought at par: no discount/premium, so amortized cost never moves off par.
amortized_cost = q(PAR)

# ----------------------------------------------------------------------------
# (b) Annual cash interest = par x stated rate x (1 / payments per year).
#     At par, interest revenue == cash interest (no amortization component).
# ----------------------------------------------------------------------------
cash_interest_y1 = q(PAR * STATED_RATE / PERIODS_PER_YEAR)
interest_revenue_y1 = cash_interest_y1

# ----------------------------------------------------------------------------
# (c) Subsequent measurement (FVA) schedule.
#     required FVA balance = fair value - amortized cost
#     adjustment needed    = required balance - existing balance
#     (signed: + = debit FVA / OCI gain, - = credit FVA / OCI loss)
# ----------------------------------------------------------------------------
schedule = []
existing_fva = q(Decimal("0"))          # zero FVA balance at inception
for date_label, fair_value in (
    ("Dec 31, Year 1", FV_Y1),
    ("Dec 31, Year 2", FV_Y2),
    ("Jan 1, Year 3 (sale date)", SALE_PROCEEDS),  # sale-date FV = sale price
):
    fair_value = q(fair_value)
    cumulative_unrealized = q(fair_value - amortized_cost)   # required FVA bal.
    adjustment = q(cumulative_unrealized - existing_fva)
    schedule.append(
        {
            "date": date_label,
            "amortized_cost": amortized_cost,
            "fair_value": fair_value,
            "cumulative_unrealized_gain_loss": cumulative_unrealized,
            "existing_fva_balance": existing_fva,
            "adjustment_to_fva_needed": adjustment,
        }
    )
    existing_fva = cumulative_unrealized   # roll forward

y1_row, y2_row, sale_row = schedule

# ----------------------------------------------------------------------------
# (e) Year 1 statement presentation.
#     AOCI end of Y1 = beginning AOCI + Y1 OCI movement.
# ----------------------------------------------------------------------------
oci_y1 = y1_row["adjustment_to_fva_needed"]          # negative => holding loss
aoci_end_y1 = q(BEGINNING_AOCI + oci_y1)
bs_investment_carrying_y1 = q(amortized_cost + y1_row["cumulative_unrealized_gain_loss"])

# ----------------------------------------------------------------------------
# (f) Year 2 adjustment / AOCI roll-forward.
# ----------------------------------------------------------------------------
oci_y2 = y2_row["adjustment_to_fva_needed"]
aoci_end_y2 = q(aoci_end_y1 + oci_y2)

# ----------------------------------------------------------------------------
# (g) Jan 1 Year 3 sale.
#     (i)  mark to fair value at sale date through OCI
#     (ii) record sale: remove investment at amortized cost, eliminate FVA,
#          recognize realized gain, reclassify cumulative AOCI to net income.
# ----------------------------------------------------------------------------
sale_date_oci = sale_row["adjustment_to_fva_needed"]
fva_balance_at_sale = sale_row["cumulative_unrealized_gain_loss"]   # to eliminate
realized_gain = q(SALE_PROCEEDS - amortized_cost)                   # to net income
reclass_out_of_aoci = realized_gain   # reclass adj. equals the realized gain

# ----------------------------------------------------------------------------
# (h) Year 3 AOCI reconciliation after the sale.
# ----------------------------------------------------------------------------
aoci_begin_y3 = aoci_end_y2
oci_y3_net = q(sale_date_oci - reclass_out_of_aoci)
aoci_end_y3 = q(aoci_begin_y3 + oci_y3_net)

# ----------------------------------------------------------------------------
# Journal entries
# ----------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = []

# (a) Jan 1, Year 1 — purchase
journal_entries.append(
    {
        "part": "a",
        "date": "January 1, Year 1",
        "description": "To record purchase of AFS bond investment at par",
        "lines": [
            line(INVESTMENT_ACCOUNT, debit=purchase_cost),
            line("Cash", credit=purchase_cost),
        ],
    }
)

# (b) Dec 31, Year 1 — cash interest
journal_entries.append(
    {
        "part": "b",
        "date": "December 31, Year 1",
        "description": "To record receipt of annual cash interest ($55,000 x 9%)",
        "lines": [
            line("Cash", debit=cash_interest_y1),
            line("Interest Revenue", credit=interest_revenue_y1),
        ],
    }
)

# (d) Dec 31, Year 1 — FV-OCI adjustment (holding loss: credit FVA, debit OCI)
journal_entries.append(
    {
        "part": "d",
        "date": "December 31, Year 1",
        "description": "To adjust AFS investment to fair value (FV-OCI)",
        "lines": (
            [
                line("Unrealized Gain or Loss—OCI", debit=-oci_y1),
                line("Fair Value Adjustment—AFS", credit=-oci_y1),
            ]
            if oci_y1 < 0
            else [
                line("Fair Value Adjustment—AFS", debit=oci_y1),
                line("Unrealized Gain or Loss—OCI", credit=oci_y1),
            ]
        ),
    }
)

# (f) Dec 31, Year 2 — FV-OCI adjustment (holding gain: debit FVA, credit OCI)
journal_entries.append(
    {
        "part": "f",
        "date": "December 31, Year 2",
        "description": "To adjust AFS investment to fair value (FV-OCI)",
        "lines": (
            [
                line("Fair Value Adjustment—AFS", debit=oci_y2),
                line("Unrealized Gain or Loss—OCI", credit=oci_y2),
            ]
            if oci_y2 > 0
            else [
                line("Unrealized Gain or Loss—OCI", debit=-oci_y2),
                line("Fair Value Adjustment—AFS", credit=-oci_y2),
            ]
        ),
    }
)

# (g)(i) Jan 1, Year 3 — sale-date mark to fair value through OCI
journal_entries.append(
    {
        "part": "g(i)",
        "date": "January 1, Year 3",
        "description": "To adjust AFS investment to fair value at the date of sale (FV-OCI)",
        "lines": (
            [
                line("Fair Value Adjustment—AFS", debit=sale_date_oci),
                line("Unrealized Gain or Loss—OCI", credit=sale_date_oci),
            ]
            if sale_date_oci > 0
            else [
                line("Unrealized Gain or Loss—OCI", debit=-sale_date_oci),
                line("Fair Value Adjustment—AFS", credit=-sale_date_oci),
            ]
        ),
    }
)

# (g)(ii) Jan 1, Year 3 — sale + reclassification + elimination of FVA
sale_lines = [line("Cash", debit=SALE_PROCEEDS)]
if reclass_out_of_aoci > 0:
    # cumulative net gain sitting in AOCI is reclassified out with a debit
    sale_lines.append(line("Unrealized Gain or Loss—OCI", debit=reclass_out_of_aoci))
sale_lines.append(line(INVESTMENT_ACCOUNT, credit=amortized_cost))
if realized_gain > 0:
    sale_lines.append(line("Gain on Sale of Investment", credit=realized_gain))
else:
    sale_lines.insert(1, line("Loss on Sale of Investment", debit=-realized_gain))
if fva_balance_at_sale > 0:
    sale_lines.append(line("Fair Value Adjustment—AFS", credit=fva_balance_at_sale))
elif fva_balance_at_sale < 0:
    sale_lines.append(line("Fair Value Adjustment—AFS", debit=-fva_balance_at_sale))
if reclass_out_of_aoci < 0:
    sale_lines.append(line("Unrealized Gain or Loss—OCI", credit=-reclass_out_of_aoci))

journal_entries.append(
    {
        "part": "g(ii)",
        "date": "January 1, Year 3",
        "description": (
            "To record sale of the AFS bond investment, reclassify the holding "
            "gain from AOCI to net income, and eliminate the FVA balance"
        ),
        "lines": sale_lines,
    }
)

# Debits must equal credits in every entry.
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert q(d) == q(c), f"entry {je['part']} out of balance: {d} vs {c}"

# ----------------------------------------------------------------------------
# Answers — only figures the Required parts ask for
# ----------------------------------------------------------------------------
answers = [
    # (c) subsequent measurement (FVA) schedule
    {"label": "c: Dec 31 Y1 — amortized cost", "value": num(y1_row["amortized_cost"])},
    {"label": "c: Dec 31 Y1 — fair value", "value": num(y1_row["fair_value"])},
    {"label": "c: Dec 31 Y1 — cumulative unrealized holding gain (loss) = required FVA balance",
     "value": num(y1_row["cumulative_unrealized_gain_loss"])},
    {"label": "c: Dec 31 Y1 — existing FVA balance", "value": num(y1_row["existing_fva_balance"])},
    {"label": "c: Dec 31 Y1 — increase (decrease) to FVA needed",
     "value": num(y1_row["adjustment_to_fva_needed"])},

    {"label": "c: Dec 31 Y2 — amortized cost", "value": num(y2_row["amortized_cost"])},
    {"label": "c: Dec 31 Y2 — fair value", "value": num(y2_row["fair_value"])},
    {"label": "c: Dec 31 Y2 — cumulative unrealized holding gain (loss) = required FVA balance",
     "value": num(y2_row["cumulative_unrealized_gain_loss"])},
    {"label": "c: Dec 31 Y2 — existing FVA balance", "value": num(y2_row["existing_fva_balance"])},
    {"label": "c: Dec 31 Y2 — increase (decrease) to FVA needed",
     "value": num(y2_row["adjustment_to_fva_needed"])},

    {"label": "c: Jan 1 Y3 sale date — amortized cost", "value": num(sale_row["amortized_cost"])},
    {"label": "c: Jan 1 Y3 sale date — fair value", "value": num(sale_row["fair_value"])},
    {"label": "c: Jan 1 Y3 sale date — cumulative unrealized holding gain (loss) = required FVA balance",
     "value": num(sale_row["cumulative_unrealized_gain_loss"])},
    {"label": "c: Jan 1 Y3 sale date — existing FVA balance", "value": num(sale_row["existing_fva_balance"])},
    {"label": "c: Jan 1 Y3 sale date — increase (decrease) to FVA needed",
     "value": num(sale_row["adjustment_to_fva_needed"])},

    # (e) Year 1 presentation
    {"label": "e: Year 1 income statement — Interest revenue", "value": num(interest_revenue_y1)},
    {"label": "e: Year 1 statement of comprehensive income — Unrealized holding gain (loss) on AFS securities, OCI",
     "value": num(oci_y1)},
    {"label": "e: Dec 31 Y1 balance sheet — Investment in available-for-sale securities (at fair value)",
     "value": num(bs_investment_carrying_y1)},
    {"label": "e: Dec 31 Y1 balance sheet — Accumulated other comprehensive income (loss)",
     "value": num(aoci_end_y1)},

    # (h) Year 3 AOCI reconciliation after the sale
    {"label": "h: Accumulated OCI, January 1, Year 3", "value": num(aoci_begin_y3)},
    {"label": "h: Current period unrealized gain (loss) on AFS securities", "value": num(sale_date_oci)},
    {"label": "h: Reclassification adjustment for gain included in net income",
     "value": num(-reclass_out_of_aoci)},
    {"label": "h: Net change in AOCI during Year 3", "value": num(oci_y3_net)},
    {"label": "h: Accumulated OCI, December 31, Year 3", "value": num(aoci_end_y3)},
]

out = {
    "id": "agent_135#01",
    "rounding_convention": (
        "decimal.Decimal only, never float; every money figure quantized to the "
        "cent with ROUND_HALF_UP applied per period/per line as computed "
        "(round-per-period, not round-at-end). Bond purchased at par, so "
        "amortized cost stays $55,000 and no PV table factor / effective-interest "
        "amortization is involved; interest is the simple annual coupon "
        "par x 9% x 12/12."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Purchased for par, so there is no premium/discount and amortized cost is "
        "$55,000 at every measurement date; interest revenue equals the $4,950 "
        "annual cash coupon. FVA schedule signs: positive = debit FVA (cumulative "
        "holding gain), negative = credit FVA (cumulative holding loss). Sale-date "
        "fair value is taken as the $57,750 proceeds. Realized gain reclassified "
        "out of AOCI equals proceeds minus amortized cost, leaving ending Year 3 "
        "AOCI of zero."
    ),
}

print(json.dumps(out, indent=2, ensure_ascii=False))
