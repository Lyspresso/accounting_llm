#!/usr/bin/env python3
"""Blind solver for item agent_302#01 (Copperfinch Merchants Co., gross method, 3/15 n/45).

ROUNDING CONVENTION
-------------------
All money is `decimal.Decimal`; no binary floats are used anywhere in the
computation.  Every derived money amount is quantized to cents with
ROUND_HALF_UP at the point it is computed (round-per-amount, i.e. per period /
per transaction), never accumulated at full precision and rounded once at the
end.  Percentages (40% of the gross invoice, the 3% cash discount) are exact
Decimal ratios, so each product is applied to an already-rounded base and the
result is re-quantized to cents immediately.  No present-value work is required
by this fact pattern, so no PV table factors are involved.

FACT PATTERN AND REASONING
--------------------------
Copperfinch uses the GROSS method (ASC 606 variable consideration; textbook
LO 8-2).  Under the gross method:
  * Receivables and revenue are recorded at 100% of the invoice (gross) amount.
  * `Sales Discounts` (a contra-revenue account) is recorded only when a
    customer actually pays inside the discount window.
  * At period end an adjusting entry REDUCES accounts receivable and revenue by
    the cash discounts EXPECTED to be taken on receivables open at year end.
    The stem directs that this estimate run through `Allowance for Sales
    Discounts` (a contra-asset valuation account against AR), with the debit to
    `Sales Discounts` (contra-revenue).
  * When the estimated discount is actually taken in the following period, it is
    charged against the allowance, not against income again.

Timeline derived from the stem:
  Dec 12 Yr1  Arden sale $90,000 (cost $54,000).  3/15 window runs through
              Dec 27 Yr1.
  Dec 20 Yr1  Arden pays 40% of its GROSS invoice, inside the window, so the 3%
              discount applies to that 40% slice.
  Dec 30 Yr1  Bristol sale $60,000 (cost $36,000).  Window runs through
              Jan 14 Yr2.
  Dec 31 Yr1  YE estimate: Bristol expected to take 3% on 100% of its open
              balance; Arden's remaining balance is past its window, so no
              discount is expected on it.
  Jan 10 Yr2  Bristol pays in full and takes the discount -> relieve the
              allowance.
  Jan 25 Yr2  Arden pays its remaining balance after the discount period -> no
              discount, cash equals the gross balance.

OUTPUT
------
Prints one JSON object on stdout.  Only the figures the Required parts (a-f)
ask for are reported; intermediate/check figures are not emitted as answers.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents with ROUND_HALF_UP (applied per amount, as computed)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly rendering: int when the cents are zero, else float-free str->float."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)  # only reached for non-integral cents; not the case here


# ---------------------------------------------------------------------------
# Stem facts (the only hard-coded values: they come straight from the stem)
# ---------------------------------------------------------------------------
DISCOUNT_RATE = Decimal("3") / Decimal("100")   # 3/15, n/45 -> 3%
ARDEN_SALE = money("90000")
ARDEN_COST = money("54000")
ARDEN_EARLY_PCT = Decimal("40") / Decimal("100")  # 40% of gross invoice
BRISTOL_SALE = money("60000")
BRISTOL_COST = money("36000")
BEGINNING_AR = money("0")

# ---------------------------------------------------------------------------
# (a) Dec 12 and Dec 30 sale + COGS entries  -- gross method: AR/Sales at gross
# ---------------------------------------------------------------------------
je_a = [
    {
        "part": "a",
        "date": "Dec 12, Year 1",
        "description": "Credit sale to Arden Supply (gross method)",
        "lines": [
            {"account": "Accounts Receivable - Arden Supply",
             "debit": num(ARDEN_SALE), "credit": 0},
            {"account": "Sales Revenue", "debit": 0, "credit": num(ARDEN_SALE)},
        ],
    },
    {
        "part": "a",
        "date": "Dec 12, Year 1",
        "description": "Cost of the Arden Supply sale",
        "lines": [
            {"account": "Cost of Goods Sold", "debit": num(ARDEN_COST), "credit": 0},
            {"account": "Inventory", "debit": 0, "credit": num(ARDEN_COST)},
        ],
    },
    {
        "part": "a",
        "date": "Dec 30, Year 1",
        "description": "Credit sale to Bristol Outlet (gross method)",
        "lines": [
            {"account": "Accounts Receivable - Bristol Outlet",
             "debit": num(BRISTOL_SALE), "credit": 0},
            {"account": "Sales Revenue", "debit": 0, "credit": num(BRISTOL_SALE)},
        ],
    },
    {
        "part": "a",
        "date": "Dec 30, Year 1",
        "description": "Cost of the Bristol Outlet sale",
        "lines": [
            {"account": "Cost of Goods Sold", "debit": num(BRISTOL_COST), "credit": 0},
            {"account": "Inventory", "debit": 0, "credit": num(BRISTOL_COST)},
        ],
    },
]

# ---------------------------------------------------------------------------
# (b) Dec 20 collection from Arden -- 40% of gross, WITHIN the 15-day window
#     (sale Dec 12 + 15 days -> window ends Dec 27), so 3% discount applies to
#     the 40% slice only.
# ---------------------------------------------------------------------------
arden_gross_paid_dec20 = money(ARDEN_SALE * ARDEN_EARLY_PCT)          # 36,000.00
arden_discount_dec20 = money(arden_gross_paid_dec20 * DISCOUNT_RATE)  #  1,080.00
arden_cash_dec20 = money(arden_gross_paid_dec20 - arden_discount_dec20)  # 34,920.00

je_b = [
    {
        "part": "b",
        "date": "Dec 20, Year 1",
        "description": "Collection of 40% of Arden gross invoice within the discount period",
        "lines": [
            {"account": "Cash", "debit": num(arden_cash_dec20), "credit": 0},
            {"account": "Sales Discounts", "debit": num(arden_discount_dec20), "credit": 0},
            {"account": "Accounts Receivable - Arden Supply",
             "debit": 0, "credit": num(arden_gross_paid_dec20)},
        ],
    },
]

# ---------------------------------------------------------------------------
# (c) Subsequent-measurement schedule at Dec 31, Year 1
# ---------------------------------------------------------------------------
arden_ar_ye = money(BEGINNING_AR + ARDEN_SALE - arden_gross_paid_dec20)   # 54,000.00
bristol_ar_ye = money(BEGINNING_AR + BRISTOL_SALE)                        # 60,000.00
gross_ar_ye = money(arden_ar_ye + bristol_ar_ye)                          # 114,000.00

# Arden's remaining balance is past its discount window (ended Dec 27) -> $0 expected.
allowance_arden = money("0")
# Bristol: 3% expected on 100% of its open balance.
allowance_bristol = money(bristol_ar_ye * DISCOUNT_RATE)                  #  1,800.00
allowance_ye = money(allowance_arden + allowance_bristol)                 #  1,800.00

net_ar_ye = money(gross_ar_ye - allowance_ye)                             # 112,200.00

# ---------------------------------------------------------------------------
# (d) December 31, Year 1 period-end adjusting entry for expected discounts
#     Beginning allowance balance is $0 (beginning AR is $0 and no prior
#     estimate exists), so the required entry equals the full required balance.
# ---------------------------------------------------------------------------
beginning_allowance = money("0")
adjusting_amount = money(allowance_ye - beginning_allowance)              # 1,800.00

je_d = [
    {
        "part": "d",
        "date": "Dec 31, Year 1",
        "description": "Period-end adjusting entry for cash discounts expected to be taken",
        "lines": [
            {"account": "Sales Discounts", "debit": num(adjusting_amount), "credit": 0},
            {"account": "Allowance for Sales Discounts",
             "debit": 0, "credit": num(adjusting_amount)},
        ],
    },
]

# ---------------------------------------------------------------------------
# (e) Jan 10 and Jan 25, Year 2 settlements
#     Bristol takes the discount that was already estimated -> charge the
#     allowance, no new contra-revenue.  Arden pays after its window -> no
#     discount; cash equals the gross balance.
# ---------------------------------------------------------------------------
bristol_discount_jan10 = money(bristol_ar_ye * DISCOUNT_RATE)             #  1,800.00
bristol_cash_jan10 = money(bristol_ar_ye - bristol_discount_jan10)        # 58,200.00
arden_cash_jan25 = money(arden_ar_ye)                                     # 54,000.00

je_e = [
    {
        "part": "e",
        "date": "Jan 10, Year 2",
        "description": "Bristol Outlet pays in full and takes the cash discount",
        "lines": [
            {"account": "Cash", "debit": num(bristol_cash_jan10), "credit": 0},
            {"account": "Allowance for Sales Discounts",
             "debit": num(bristol_discount_jan10), "credit": 0},
            {"account": "Accounts Receivable - Bristol Outlet",
             "debit": 0, "credit": num(bristol_ar_ye)},
        ],
    },
    {
        "part": "e",
        "date": "Jan 25, Year 2",
        "description": "Arden Supply pays remaining balance after the discount period",
        "lines": [
            {"account": "Cash", "debit": num(arden_cash_jan25), "credit": 0},
            {"account": "Accounts Receivable - Arden Supply",
             "debit": 0, "credit": num(arden_ar_ye)},
        ],
    },
]

# ---------------------------------------------------------------------------
# (f) Year 1 net sales excerpt and Dec 31 net AR
#     Gross method: net sales = gross sales - discounts actually taken in Yr 1
#     - discounts estimated at year end.
# ---------------------------------------------------------------------------
gross_sales_y1 = money(ARDEN_SALE + BRISTOL_SALE)                         # 150,000.00
discounts_taken_y1 = money(arden_discount_dec20)                          #   1,080.00
discounts_estimated_y1 = money(adjusting_amount)                          #   1,800.00
total_sales_discounts_y1 = money(discounts_taken_y1 + discounts_estimated_y1)  # 2,880.00
net_sales_y1 = money(gross_sales_y1 - total_sales_discounts_y1)           # 147,120.00

journal_entries = je_a + je_b + je_d + je_e

# ---------------------------------------------------------------------------
# Internal integrity check: every entry must balance.
# ---------------------------------------------------------------------------
for entry in journal_entries:
    dr = sum((money(line["debit"]) for line in entry["lines"]), Decimal("0"))
    cr = sum((money(line["credit"]) for line in entry["lines"]), Decimal("0"))
    if dr != cr:
        raise AssertionError(
            f"Unbalanced entry (part {entry['part']}, {entry['date']}): "
            f"debits {dr} != credits {cr}"
        )

# AR roll-forward must clear to zero after both Year 2 settlements.
_ar_remaining = money(
    gross_ar_ye - bristol_ar_ye - arden_ar_ye
)
if _ar_remaining != Decimal("0.00"):
    raise AssertionError("AR does not clear after the Year 2 settlements")

answers = [
    # (c) Subsequent measurement schedule at Dec 31, Year 1
    {"label": "c: gross AR - Arden Supply at Dec 31, Year 1", "value": num(arden_ar_ye)},
    {"label": "c: gross AR - Bristol Outlet at Dec 31, Year 1", "value": num(bristol_ar_ye)},
    {"label": "c: total gross AR at Dec 31, Year 1", "value": num(gross_ar_ye)},
    {"label": "c: Allowance for Sales Discounts at Dec 31, Year 1", "value": num(allowance_ye)},
    {"label": "c: AR, net at Dec 31, Year 1", "value": num(net_ar_ye)},
    # (f) Year 1 net sales excerpt and Dec 31 net AR
    {"label": "f: Year 1 sales revenue (gross)", "value": num(gross_sales_y1)},
    {"label": "f: Year 1 less sales discounts (taken and estimated)",
     "value": num(total_sales_discounts_y1)},
    {"label": "f: Year 1 net sales revenue", "value": num(net_sales_y1)},
    {"label": "f: net AR at Dec 31, Year 1", "value": num(net_ar_ye)},
]

result = {
    "id": "agent_302#01",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP quantized to cents per "
        "amount as computed (round-per-period, not round-at-end); discount "
        "percentages applied to already-rounded bases; no PV factors required"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Gross method: AR and Sales recorded at gross; Sales Discounts (contra-revenue) "
        "recorded when taken. Dec 20 Arden payment of 40% x $90,000 = $36,000 falls inside "
        "the 3/15 window (Dec 12 + 15 days = Dec 27), so a 3% discount of $1,080 applies to "
        "that slice only and cash is $34,920. At Dec 31 the only open balance still inside a "
        "discount window is Bristol's $60,000 (window through Jan 14), so the estimated "
        "discount is 3% x $60,000 = $1,800; Arden's remaining $54,000 is past its window and "
        "carries no allowance. Beginning AR and beginning allowance are $0, so the Dec 31 "
        "adjusting entry equals the full required allowance balance of $1,800. In Year 2 "
        "Bristol's discount is charged against the allowance (no second hit to revenue) and "
        "Arden pays its $54,000 gross with no discount."
    ),
}

print(json.dumps(result, indent=2))
