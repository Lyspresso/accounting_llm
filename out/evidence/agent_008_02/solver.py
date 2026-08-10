#!/usr/bin/env python3
"""Solver for item agent_008#02 - Multi-security FV-NI (trading) schedule with a
mid-year disposal, where the Fair Value Adjustment account is trued up ONLY at
period end.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; floats are never used. Every amount is quantized
to cents with ROUND_HALF_UP at the point it is recorded (round-per-amount, not
round-at-end). No present-value or interest computation is required by this fact
pattern, so no PV table factors are involved; the stem also says to ignore
interest. Because every input in the stem is an exact dollar figure, the
ROUND_HALF_UP quantization is a formality here - it changes no result - but it
is applied deliberately so the arithmetic is reproducible.

METHOD (period-end-only Fair Value Adjustment)
----------------------------------------------
Under the period-end-only approach the Fair Value Adjustment-TS account is a
portfolio-level valuation account that is touched exactly once a year, on
December 31. Consequences used below:

1. On the sale date the FVA account is NOT adjusted and the sold security's
   share of the existing FVA balance is NOT backed out. The security is removed
   at its amortized cost (its own ledger carrying amount), so
       realized gain/(loss) = cash proceeds - amortized cost.
2. At December 31 the required ending balance of Fair Value Adjustment-TS is
   determined from the securities STILL HELD:
       required balance = total fair value - total amortized cost
   (positive => debit balance, negative => credit balance).
3. The adjusting entry is the difference between that required ending balance
   and the balance already in the account, and the offset for trading (FV-NI)
   securities is Unrealized Holding Gain or Loss-Income.
4. Balance sheet carrying amount = amortized cost of securities held +/- the
   ending FVA balance = fair value of securities held.

Sign convention in this file: FVA balances are signed, debit-positive. A credit
balance of $3,200 is therefore stored as Decimal("-3200").

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(value) -> Decimal:
    """Quantize to cents with ROUND_HALF_UP (the course convention)."""
    return Decimal(value).quantize(CENTS, rounding=ROUND_HALF_UP)


def out(amount: Decimal):
    """JSON-friendly number: int when whole, else float-free string-parsed cents."""
    amount = money(amount)
    if amount == amount.to_integral_value():
        return int(amount)
    return json.loads(str(amount))  # exact 2-dp decimal literal, no float math upstream


# ---------------------------------------------------------------------------
# Facts from the stem (nothing below is hard-coded output; all results derived)
# ---------------------------------------------------------------------------

# Fair Value Adjustment-TS at 1/1/Y2: CREDIT balance $3,200 -> debit-negative.
fva_beginning = money("-3200")

# June 12 disposal of the entire Crest 4.5% position.
crest_amortized_cost = money("35000")
crest_proceeds = money("33800")

# Securities still held at 12/31/Y2: (name, amortized cost, fair value)
held = [
    ("Dune 5% bonds", money("25000"), money("24100")),
    ("Pier 4% bonds", money("60000"), money("61500")),
]

# ---------------------------------------------------------------------------
# (a) June 12 sale under the period-end-only method
# ---------------------------------------------------------------------------
# FVA is untouched on the sale date; the security leaves at amortized cost.
realized_gain_loss = money(crest_proceeds - crest_amortized_cost)  # negative = loss
realized_loss = money(-realized_gain_loss) if realized_gain_loss < 0 else money(0)
realized_gain = money(realized_gain_loss) if realized_gain_loss > 0 else money(0)

sale_lines = [{"account": "Cash", "debit": out(crest_proceeds), "credit": 0}]
if realized_loss > 0:
    sale_lines.append(
        {
            "account": "Loss on Sale of Investments",
            "debit": out(realized_loss),
            "credit": 0,
        }
    )
sale_lines.append(
    {
        "account": "Debt Investments (Trading)",
        "debit": 0,
        "credit": out(crest_amortized_cost),
    }
)
if realized_gain > 0:
    sale_lines.append(
        {
            "account": "Gain on Sale of Investments",
            "debit": 0,
            "credit": out(realized_gain),
        }
    )

# ---------------------------------------------------------------------------
# (b) Year-end FVA schedule for the remaining portfolio
# ---------------------------------------------------------------------------
total_cost_held = money(sum((c for _, c, _ in held), Decimal("0")))
total_fv_held = money(sum((fv for _, _, fv in held), Decimal("0")))

# Required ending FVA balance (debit-positive).
fva_required_ending = money(total_fv_held - total_cost_held)

# (c) Adjusting entry amount: required ending less balance already there.
fva_adjustment = money(fva_required_ending - fva_beginning)  # positive = debit FVA

adj_lines = []
if fva_adjustment > 0:
    adj_lines.append(
        {
            "account": "Fair Value Adjustment-Trading Securities",
            "debit": out(fva_adjustment),
            "credit": 0,
        }
    )
    adj_lines.append(
        {
            "account": "Unrealized Holding Gain or Loss-Income",
            "debit": 0,
            "credit": out(fva_adjustment),
        }
    )
elif fva_adjustment < 0:
    adj_lines.append(
        {
            "account": "Unrealized Holding Gain or Loss-Income",
            "debit": out(-fva_adjustment),
            "credit": 0,
        }
    )
    adj_lines.append(
        {
            "account": "Fair Value Adjustment-Trading Securities",
            "debit": 0,
            "credit": out(-fva_adjustment),
        }
    )

# ---------------------------------------------------------------------------
# (d) Balance sheet carrying amount at 12/31/Y2
# ---------------------------------------------------------------------------
balance_sheet_carrying = money(total_cost_held + fva_required_ending)

# ---------------------------------------------------------------------------
# (e) Year 2 income statement effect (interest ignored)
# ---------------------------------------------------------------------------
sale_income_effect = money(realized_gain_loss)          # negative = reduces income
fva_income_effect = money(fva_adjustment)               # positive = unrealized gain
net_income_effect = money(sale_income_effect + fva_income_effect)

# ---------------------------------------------------------------------------
# Internal proof: every entry must balance. Fix derivations, not numbers.
# ---------------------------------------------------------------------------
for part, lines in (("a", sale_lines), ("c", adj_lines)):
    debits = sum(money(l["debit"]) for l in lines)
    credits = sum(money(l["credit"]) for l in lines)
    assert debits == credits, f"part {part} out of balance: {debits} vs {credits}"

# Carrying amount must equal fair value of securities held.
assert balance_sheet_carrying == total_fv_held

result = {
    "id": "agent_008#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; every amount quantized to cents with "
        "ROUND_HALF_UP as recorded (round-per-amount). No PV factors needed. "
        "Period-end-only method: FVA untouched on the sale date, so the realized "
        "loss is proceeds less amortized cost, and the 12/31 FVA balance is trued "
        "up to (fair value - amortized cost) of the securities still held."
    ),
    "answers": [
        {
            "label": "a: realized loss on June 12 sale of Crest (proceeds 33,800 less amortized cost 35,000)",
            "value": out(realized_loss),
        },
        {
            "label": "b: total amortized cost of remaining trading portfolio at 12/31/Y2",
            "value": out(total_cost_held),
        },
        {
            "label": "b: total fair value of remaining trading portfolio at 12/31/Y2",
            "value": out(total_fv_held),
        },
        {
            "label": "b: required Fair Value Adjustment-TS ending balance at 12/31/Y2 (debit balance)",
            "value": out(fva_required_ending),
        },
        {
            "label": "b/c: FVA adjustment needed at 12/31/Y2 (debit to Fair Value Adjustment-TS)",
            "value": out(fva_adjustment),
        },
        {
            "label": "d: Investment in trading securities reported on the 12/31/Y2 balance sheet (current asset, at fair value)",
            "value": out(balance_sheet_carrying),
        },
        {
            "label": "e(i): Year 2 income statement effect of the Crest sale (loss, decreases income)",
            "value": out(sale_income_effect),
        },
        {
            "label": "e(ii): Year 2 income statement effect of the period-end FVA adjustment (unrealized holding gain, increases income)",
            "value": out(fva_income_effect),
        },
        {
            "label": "e: net Year 2 income statement effect (increase)",
            "value": out(net_income_effect),
        },
    ],
    "journal_entries": [
        {"part": "a", "date": "June 12, Year 2", "lines": sale_lines},
        {"part": "c", "date": "December 31, Year 2", "lines": adj_lines},
    ],
    "insufficient_info": False,
    "notes": (
        "Part b schedule: Dune cost 25,000 / FV 24,100 (-900); Pier cost 60,000 / "
        "FV 61,500 (+1,500); totals cost 85,000 / FV 85,600, so the FVA-TS account "
        "must end with a 600 DEBIT balance. It began the year with a 3,200 CREDIT "
        "balance and was not touched on the June 12 sale date, so the 12/31 entry "
        "debits FVA-TS 3,800 (3,200 + 600). Part d: shown as a current asset, "
        "Investment in trading securities 85,600, i.e. amortized cost 85,000 plus "
        "the 600 debit Fair Value Adjustment. Part e: 1,200 realized loss plus "
        "3,800 unrealized holding gain = 2,600 net increase in Year 2 pretax "
        "income (interest ignored per the stem). Negative values in e(i) denote a "
        "decrease in income."
    ),
}

print(json.dumps(result, indent=2))
