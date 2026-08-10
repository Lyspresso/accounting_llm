"""
Solver for agent_268#00 — Equity method with basis difference (LO 14-5).

Fact pattern (from stem.md, nothing hard-coded beyond the given facts):
    Cost of 30% interest in Meridian Forge Co. (Jan 1, Yr 1)   $240,000
    Meridian book value of net assets at acquisition            $700,000
    Equipment undervalued (total, on Meridian's books)           $40,000
    Remaining life of that equipment                              8 years, SL, no residual
    Meridian Year 1 net income                                   $80,000
    Meridian dividends declared & paid Dec 31, Yr 1              $20,000
    Fair value of the 30% interest at Dec 31, Yr 1              $255,000

Derivation:
    share of book value      = ownership x book value of net assets
    basis difference (equip) = ownership x total undervaluation
    goodwill                 = cost - share of book value - basis difference (plug)
    excess depreciation      = basis difference / remaining life
    share of investee NI     = ownership x investee net income
    dividends received       = ownership x investee dividends (return OF investment)
    net equity-method income = share of NI - excess depreciation
    carrying amount          = cost + share of NI - excess depreciation - dividends

    Under the equity method the investment is NOT remeasured to fair value, so the
    $255,000 Dec 31 fair value is a disclosure-only figure; no fair-value
    adjusting entry is recorded (no unrealized gain/loss).

ROUNDING CONVENTION
    All money is decimal.Decimal (never float). Every monetary result is
    quantized to the cent with ROUND_HALF_UP, applied per period / per computed
    line rather than only at the end, so the schedule's period amounts are the
    same amounts that roll forward into the carrying value. Ownership percentage
    is an exact Decimal ratio (30/100), not a float. Straight-line depreciation
    of the basis difference is computed per year (basis / life) and rounded per
    period. In this fact pattern every amount is exact to the cent, so the
    convention does not change any figure, but it is applied deliberately.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to the cent using ROUND_HALF_UP (applied per period/per line)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """Render a Decimal for JSON: int when whole cents land on a whole dollar."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ----------------------------------------------------------------- given facts
COST = Decimal("240000")
OWNERSHIP = Decimal("30") / Decimal("100")
INVESTEE_BOOK_VALUE = Decimal("700000")
EQUIPMENT_UNDERVALUATION_TOTAL = Decimal("40000")
EQUIPMENT_REMAINING_LIFE_YEARS = Decimal("8")
INVESTEE_NET_INCOME = Decimal("80000")
INVESTEE_DIVIDENDS = Decimal("20000")
FAIR_VALUE_OF_INTEREST_DEC31 = Decimal("255000")  # disclosure only; not recorded

# ------------------------------------------- b. allocation of the $240,000 cost
share_of_book_value = money(OWNERSHIP * INVESTEE_BOOK_VALUE)
basis_difference_equipment = money(OWNERSHIP * EQUIPMENT_UNDERVALUATION_TOTAL)
goodwill = money(COST - share_of_book_value - basis_difference_equipment)

# --------------------------------------------------- Year 1 period-end amounts
share_of_net_income = money(OWNERSHIP * INVESTEE_NET_INCOME)
excess_depreciation = money(basis_difference_equipment / EQUIPMENT_REMAINING_LIFE_YEARS)
dividends_received = money(OWNERSHIP * INVESTEE_DIVIDENDS)

# ------------------------------------- e. net equity-method income recognized
net_equity_method_income = money(share_of_net_income - excess_depreciation)

# ------------------------------ d. investment schedule / Dec 31 carrying amount
carrying_amount_dec31 = money(
    COST + share_of_net_income - excess_depreciation - dividends_received
)

# --------------------------------------------------------------- self-checks
assert goodwill == COST - share_of_book_value - basis_difference_equipment
assert carrying_amount_dec31 == money(COST + net_equity_method_income - dividends_received)

journal_entries = [
    {
        "part": "a",
        "description": "Jan 1, Year 1 — initial recognition of the equity-method investment at cost",
        "lines": [
            {"account": "Investment in Meridian Forge Co.", "debit": num(COST), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": num(COST)},
        ],
    },
    {
        "part": "c",
        "description": "Dec 31, Year 1 — share of Meridian's net income (30% x $80,000)",
        "lines": [
            {"account": "Investment in Meridian Forge Co.", "debit": num(share_of_net_income), "credit": 0},
            {"account": "Investment Income (Equity in Investee Income)", "debit": 0, "credit": num(share_of_net_income)},
        ],
    },
    {
        "part": "c",
        "description": "Dec 31, Year 1 — excess depreciation on the equipment basis difference ($12,000 / 8 yrs)",
        "lines": [
            {"account": "Investment Income (Equity in Investee Income)", "debit": num(excess_depreciation), "credit": 0},
            {"account": "Investment in Meridian Forge Co.", "debit": 0, "credit": num(excess_depreciation)},
        ],
    },
    {
        "part": "c",
        "description": "Dec 31, Year 1 — cash dividends received (30% x $20,000), a return of investment",
        "lines": [
            {"account": "Cash", "debit": num(dividends_received), "credit": 0},
            {"account": "Investment in Meridian Forge Co.", "debit": 0, "credit": num(dividends_received)},
        ],
    },
]

for entry in journal_entries:
    debits = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    credits = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert debits == credits, f"unbalanced entry in part {entry['part']}"

answers = [
    {"label": "b: share of book value of net assets acquired (30% x $700,000)",
     "value": num(share_of_book_value)},
    {"label": "b: depreciable basis difference — undervalued equipment (30% x $40,000)",
     "value": num(basis_difference_equipment)},
    {"label": "b: goodwill (not amortized)",
     "value": num(goodwill)},
    {"label": "c: fair-value adjustment recorded at Dec 31, Year 1 (equity method — none)",
     "value": 0},
    {"label": "d: investment schedule — cost at Jan 1, Year 1",
     "value": num(COST)},
    {"label": "d: investment schedule — add share of investee net income",
     "value": num(share_of_net_income)},
    {"label": "d: investment schedule — less excess depreciation on basis difference",
     "value": num(-excess_depreciation)},
    {"label": "d: investment schedule — less dividends received",
     "value": num(-dividends_received)},
    {"label": "d: Investment in Meridian Forge Co. carrying amount, Dec 31, Year 1",
     "value": num(carrying_amount_dec31)},
    {"label": "e: net equity-method income recognized in Year 1 (after excess depreciation)",
     "value": num(net_equity_method_income)},
]

output = {
    "id": "agent_268#00",
    "rounding_convention": (
        "decimal.Decimal only (no floats); ROUND_HALF_UP quantized to the cent, "
        "applied per period / per computed line (share of NI, excess depreciation, "
        "dividends) before rolling forward into the carrying amount; ownership is the "
        "exact ratio 30/100; straight-line excess depreciation = basis difference / 8 "
        "computed per year. All figures here are exact to the cent."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "a: Equity method applies because Cascade holds 30% of the voting common stock "
        "and can exercise significant influence (20%-50% presumption), so the investment "
        "is recorded at cost and then adjusted for the investor's share of investee "
        "results. c: No fair-value adjustment is recorded — under the equity method the "
        "investment is not remeasured to fair value, so the $255,000 Dec 31 fair value is "
        "disclosure only and produces no unrealized gain/loss. Dividends are a return of "
        "investment (credit the investment account), not income. Goodwill of $18,000 is "
        "not amortized, so only the $12,000 equipment basis difference is depreciated "
        "($1,500 per year over 8 years)."
    ),
}

print(json.dumps(output, indent=2))
