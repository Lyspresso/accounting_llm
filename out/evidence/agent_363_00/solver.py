#!/usr/bin/env python3
"""Solver for agent_363#00 - Riverbend Packaging Co., detachable stock warrants.

Fact pattern (from stem.md only):
  - 1/1/Yr1: $600,000 face, 7%, 5-year nonconvertible bonds with DETACHABLE warrants.
  - Interest payable annually each December 31 (cash interest = 600,000 * 7%).
  - Each $1,000 bond carries 10 detachable warrants -> 600 bonds * 10 = 6,000 warrants.
  - Each warrant buys one share of $5 par common for $22 cash.
  - Package issued at 105 -> cash proceeds 600,000 * 1.05 = $630,000.
  - Shortly after issuance: bonds ex-warrants quoted at 102 (FV 612,000);
    warrants trade at $3 each (FV 6,000 * 3 = 18,000).
  - Premium amortized STRAIGHT-LINE over 5 years.
  - 3/1/Yr3: 4,500 warrants exercised. 1/15/Yr4: remaining 1,500 expire.
  - 12/31/Yr5: bonds mature and are settled (interest recorded separately).

Method notes:
  - PROPORTIONAL METHOD (both fair values known): each component gets
        proceeds * (component FV / sum of both FVs).
    Here sum of FVs = 612,000 + 18,000 = 630,000, which happens to equal the
    proceeds, so the allocation lands on the fair values themselves. That is
    derived below, not assumed.
  - Warrant proceeds are credited to Paid-In Capital - Stock Warrants, an EQUITY
    account. It is never amortized; it is reclassified within equity on exercise
    (to Common Stock + APIC) or on expiration (to PIC - Expired Stock Warrants).
  - Straight-line premium amortization: premium / 5, identical every year, so
    interest expense = cash interest - annual amortization each year.

ROUNDING CONVENTION:
  All money is decimal.Decimal, quantized to cents (0.01) with ROUND_HALF_UP,
  applied PER PERIOD (each year's amortization and interest expense is rounded
  as computed, not derived from a rounded cumulative total). No present-value
  table factors are needed for this item: the premium is amortized straight-line,
  not by the effective-interest method, so every figure here is exact at the cent
  and the rounding rule never actually bites. Any residual rounding drift in the
  final year would be forced into the last period's amortization so that the
  ending carrying amount equals face; that guard is implemented and asserted.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP (per-period application)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly: int when the value is a whole number, else float-free str->float."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)


# ---------------------------------------------------------------- given facts
FACE = money("600000")
STATED_RATE = Decimal("0.07")
TERM_YEARS = 5
BOND_DENOM = money("1000")
WARRANTS_PER_BOND = 10
PAR_PER_SHARE = money("5")
EXERCISE_PRICE = money("22")
ISSUE_PRICE_PCT = Decimal("1.05")          # package issued at 105
BONDS_EX_WARRANTS_PCT = Decimal("1.02")    # bonds without warrants quoted at 102
WARRANT_FV_EACH = money("3")
WARRANTS_EXERCISED = 4500
WARRANTS_EXPIRED = 1500

# ------------------------------------------------- a. proportional allocation
num_bonds = int(FACE / BOND_DENOM)                       # 600 bonds
total_warrants = num_bonds * WARRANTS_PER_BOND           # 6,000 warrants
assert WARRANTS_EXERCISED + WARRANTS_EXPIRED == total_warrants

proceeds = money(FACE * ISSUE_PRICE_PCT)                 # 630,000
fv_bonds = money(FACE * BONDS_EX_WARRANTS_PCT)           # 612,000
fv_warrants = money(WARRANT_FV_EACH * total_warrants)    # 18,000
fv_total = money(fv_bonds + fv_warrants)                 # 630,000

alloc_bonds = money(proceeds * (fv_bonds / fv_total))
alloc_warrants = money(proceeds - alloc_bonds)           # plug so the two tie to proceeds
assert alloc_bonds + alloc_warrants == proceeds

bond_carrying_initial = alloc_bonds
premium = money(alloc_bonds - FACE)                      # positive => premium
assert premium > 0, "allocation should produce a premium at 102"

# ------------------------------- c. straight-line premium amortization schedule
cash_interest = money(FACE * STATED_RATE)                # 42,000 per year
annual_amort = money(premium / TERM_YEARS)               # 2,400 per year

schedule = []
carrying = bond_carrying_initial
for yr in range(1, TERM_YEARS + 1):
    beginning = carrying
    if yr == TERM_YEARS:
        # force the final period to drive carrying amount exactly to face
        amort = money(beginning - FACE)
    else:
        amort = annual_amort
    interest_expense = money(cash_interest - amort)
    ending = money(beginning - amort)
    schedule.append(
        {
            "year": yr,
            "beginning_carrying_amount": beginning,
            "cash_interest": cash_interest,
            "premium_amortization": amort,
            "interest_expense": interest_expense,
            "ending_carrying_amount": ending,
        }
    )
    carrying = ending

assert carrying == FACE, "schedule must amortize to face at maturity"
assert sum(r["premium_amortization"] for r in schedule) == premium

# ------------------------------------------------ e. exercise of 4,500 warrants
cash_on_exercise = money(EXERCISE_PRICE * WARRANTS_EXERCISED)
warrants_pic_per_warrant = alloc_warrants / total_warrants          # exact, $3.00
pic_warrants_exercised = money(warrants_pic_per_warrant * WARRANTS_EXERCISED)
shares_issued = WARRANTS_EXERCISED                                   # 1 share per warrant
common_stock_par = money(PAR_PER_SHARE * shares_issued)
apic_common = money(cash_on_exercise + pic_warrants_exercised - common_stock_par)

# --------------------------------------------- f. expiration of 1,500 warrants
pic_warrants_expired = money(alloc_warrants - pic_warrants_exercised)
assert pic_warrants_expired == money(warrants_pic_per_warrant * WARRANTS_EXPIRED)

# ----------------------------------------------------- journal entry assembly
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


entries = [
    {
        "part": "b",
        "date": "January 1, Year 1",
        "lines": [
            line("Cash", debit=proceeds),
            line("Bonds Payable", credit=FACE),
            line("Premium on Bonds Payable", credit=premium),
            line("Paid-In Capital-Stock Warrants", credit=alloc_warrants),
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 1",
        "lines": [
            line("Interest Expense", debit=schedule[0]["interest_expense"]),
            line("Premium on Bonds Payable", debit=schedule[0]["premium_amortization"]),
            line("Cash", credit=cash_interest),
        ],
    },
    {
        "part": "e",
        "date": "March 1, Year 3",
        "lines": [
            line("Cash", debit=cash_on_exercise),
            line("Paid-In Capital-Stock Warrants", debit=pic_warrants_exercised),
            line("Common Stock", credit=common_stock_par),
            line("Paid-In Capital in Excess of Par-Common Stock", credit=apic_common),
        ],
    },
    {
        "part": "f",
        "date": "January 15, Year 4",
        "lines": [
            line("Paid-In Capital-Stock Warrants", debit=pic_warrants_expired),
            line("Paid-In Capital-Expired Stock Warrants", credit=pic_warrants_expired),
        ],
    },
    {
        "part": "g",
        "date": "December 31, Year 5",
        "lines": [
            line("Bonds Payable", debit=FACE),
            line("Cash", credit=FACE),
        ],
    },
]

for e in entries:
    d = sum(Decimal(str(l["debit"])) for l in e["lines"])
    c = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert d == c, f"part {e['part']} does not balance: {d} vs {c}"

# ------------------------------------------------------ answers (Required only)
answers = [
    {"label": "a: proceeds allocated to bonds (proportional method)", "value": num(alloc_bonds)},
    {"label": "a: proceeds allocated to warrants (proportional method)", "value": num(alloc_warrants)},
    {"label": "a: initial bond carrying amount", "value": num(bond_carrying_initial)},
    {"label": "a: premium on bonds payable at issuance", "value": num(premium)},
]

for r in schedule:
    y = r["year"]
    answers.extend(
        [
            {"label": f"c: Year {y} beginning carrying amount", "value": num(r["beginning_carrying_amount"])},
            {"label": f"c: Year {y} cash interest", "value": num(r["cash_interest"])},
            {"label": f"c: Year {y} premium amortization", "value": num(r["premium_amortization"])},
            {"label": f"c: Year {y} interest expense", "value": num(r["interest_expense"])},
            {"label": f"c: Year {y} ending carrying amount", "value": num(r["ending_carrying_amount"])},
        ]
    )

notes = (
    "h (explanation, no figure): Paid-In Capital-Stock Warrants is an equity account, "
    "not a liability or a valuation account on the debt, so nothing about it flows through "
    "interest expense. Only the bond premium/discount is amortized, because that is the "
    "adjustment that brings the bond's carrying amount to face and its effective borrowing "
    "cost into interest expense over the 5-year term. The warrant proceeds simply sit in "
    "equity until the warrants are exercised (reclassified to Common Stock and APIC) or "
    "expire (reclassified to Paid-In Capital-Expired Stock Warrants); either way the total "
    "in equity is unchanged, so amortizing it would understate equity and misstate income. "
    "Because the two fair values (bonds ex-warrants 612,000 + warrants 18,000) sum exactly "
    "to the 630,000 proceeds, the proportional allocation equals the fair values themselves."
)

out = {
    "id": "agent_363#00",
    "rounding_convention": (
        "decimal.Decimal throughout; quantized to cents with ROUND_HALF_UP applied per period. "
        "Straight-line premium amortization (premium / 5 per year), not effective-interest, so no "
        "PV table factors are used; final-period amortization is forced to drive carrying amount "
        "exactly to face (no drift arises here - all figures are exact)."
    ),
    "answers": answers,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
