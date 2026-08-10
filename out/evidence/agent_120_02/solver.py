#!/usr/bin/env python3
"""Blind solver for item agent_120#02.

Topic: LO 20-6 -- if-converted method for convertible preferred stock,
preferred issuance / dividend / conversion journal entries, and diluted EPS
in a net-loss year (antidilutive exclusion + disclosure).

ROUNDING CONVENTION
-------------------
All monetary and per-share amounts are computed with `decimal.Decimal`
(never floats), with a working precision of 28 significant digits.

  * Money (journal-entry amounts, dividends, interest, tax effects) is exact
    to the cent and quantized to 0.01 with ROUND_HALF_UP.
  * Per-share EPS amounts are rounded ONCE, at the end, to $0.01 using
    ROUND_HALF_UP.  Numerators and denominators are carried at full exact
    value into the division -- no intermediate per-share rounding, and no
    rounding of the numerator before dividing (round-at-end, not
    round-per-step).  ROUND_HALF_UP on a negative quantity rounds away from
    zero at an exact half (e.g. -2.005 -> -2.01); none of the figures here
    land on an exact half.
  * No present-value factors are involved in this item, so the table-factor
    vs. exact-formula question does not arise.
  * Share counts are exact integers and are never rounded.

DERIVATION NOTES (authority: ASC 260-10-45-40, 260-10-45-19, 260-10-50-1)
  * Convertible preferred, if-converted: add back preferred dividends to the
    numerator, add the conversion shares to the denominator.
  * Cumulative preferred: the annual dividend is deducted for basic EPS
    whether or not declared; here it is declared and paid.
  * Loss from continuing operations: including potential common shares
    ALWAYS produces an antidilutive per-share amount, so no potential common
    shares are included; basic EPS and diluted EPS are reported as the same
    amount, and the excluded securities are disclosed.
  * Preferred conversion: derecognize Preferred Stock and its related paid-in
    capital, credit Common Stock at par for the shares issued, and credit
    Paid-In Capital in Excess of Par -- Common Stock for the remainder.

Run:  python3 solver.py     (prints one JSON object on stdout)
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 28

CENT = Decimal("0.01")
ITEM_ID = "agent_120#02"


def money(x: Decimal) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def per_share(numerator: Decimal, denominator: Decimal) -> Decimal:
    """EPS: divide exact numerator by exact share count, round once to cents."""
    return (numerator / denominator).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Fact pattern, taken verbatim from the stem
# ---------------------------------------------------------------------------

# Part A -- convertible preferred, Year 1 (profitable)
PFD_SHARES = Decimal("8000")            # shares issued 1/1/Yr1
PFD_PAR = Decimal("50")                 # $50 par
PFD_RATE = Decimal("0.06")              # 6% cumulative
PFD_ISSUE_PROCEEDS = Decimal("400000")  # issued for cash at par
CONV_RATIO = Decimal("4")               # each pfd share -> 4 common shares
COMMON_PAR = Decimal("5")               # $5 par common
NET_INCOME_Y1 = Decimal("480000")
WACS_Y1 = Decimal("120000")             # weighted-average common shares
TAX_RATE = Decimal("0.25")

# Part C -- separate loss year with convertible bonds
NET_LOSS = Decimal("-600000")
BOND_COUNT = Decimal("1000")
BOND_FACE = Decimal("1000")
BOND_RATE = Decimal("0.06")
BOND_CONV_SHARES = Decimal("20")        # each bond -> 20 common shares
WACS_LOSS_YEAR = Decimal("200000")

# ---------------------------------------------------------------------------
# (a) 1/1/Year 1 -- issuance of convertible preferred at par
# ---------------------------------------------------------------------------
pfd_par_total = money(PFD_SHARES * PFD_PAR)                 # 400,000
pfd_apic = money(PFD_ISSUE_PROCEEDS - pfd_par_total)        # 0 -- issued at par
cash_in = money(PFD_ISSUE_PROCEEDS)

je_a_lines = [
    {"account": "Cash", "debit": cash_in, "credit": Decimal("0")},
    {"account": "Preferred Stock", "debit": Decimal("0"), "credit": pfd_par_total},
]
if pfd_apic != 0:  # not triggered here: proceeds equal par
    je_a_lines.append({
        "account": "Paid-In Capital in Excess of Par-Preferred Stock",
        "debit": Decimal("0"), "credit": pfd_apic,
    })

# ---------------------------------------------------------------------------
# (b) Year 1 preferred dividends -- declared and paid
# ---------------------------------------------------------------------------
pfd_dividend = money(PFD_SHARES * PFD_PAR * PFD_RATE)       # 8,000 x 50 x 6%

je_b_declare = [
    {"account": "Retained Earnings", "debit": pfd_dividend, "credit": Decimal("0")},
    {"account": "Dividends Payable", "debit": Decimal("0"), "credit": pfd_dividend},
]
je_b_pay = [
    {"account": "Dividends Payable", "debit": pfd_dividend, "credit": Decimal("0")},
    {"account": "Cash", "debit": Decimal("0"), "credit": pfd_dividend},
]

# ---------------------------------------------------------------------------
# (c) Year 1 basic and diluted EPS (if-converted)
# ---------------------------------------------------------------------------
income_avail_common = money(NET_INCOME_Y1 - pfd_dividend)   # 480,000 - 24,000
basic_eps_y1 = per_share(income_avail_common, WACS_Y1)      # 456,000 / 120,000

conv_common_shares = PFD_SHARES * CONV_RATIO                # 32,000
diluted_numerator = money(income_avail_common + pfd_dividend)   # add back divs
diluted_denominator = WACS_Y1 + conv_common_shares          # 152,000
diluted_eps_y1 = per_share(diluted_numerator, diluted_denominator)

# Dilutive test (check figure -- reported in notes, not in `answers`)
eps_per_incremental_share = (pfd_dividend / conv_common_shares).quantize(
    CENT, rounding=ROUND_HALF_UP)
is_dilutive = diluted_eps_y1 < basic_eps_y1

# ---------------------------------------------------------------------------
# (d) 1/1/Year 2 -- conversion settlement of all preferred
# ---------------------------------------------------------------------------
pfd_carrying_value = money(pfd_par_total + pfd_apic)        # 400,000
common_par_issued = money(conv_common_shares * COMMON_PAR)  # 32,000 x $5
common_apic = money(pfd_carrying_value - common_par_issued) # plug

je_d_lines = [
    {"account": "Preferred Stock", "debit": pfd_par_total, "credit": Decimal("0")},
]
if pfd_apic != 0:
    je_d_lines.append({
        "account": "Paid-In Capital in Excess of Par-Preferred Stock",
        "debit": pfd_apic, "credit": Decimal("0"),
    })
je_d_lines.append(
    {"account": "Common Stock", "debit": Decimal("0"), "credit": common_par_issued})
if common_apic > 0:
    je_d_lines.append({
        "account": "Paid-In Capital in Excess of Par-Common Stock",
        "debit": Decimal("0"), "credit": common_apic,
    })
elif common_apic < 0:  # carrying value below common par -> debit Retained Earnings
    je_d_lines.insert(-1, {
        "account": "Retained Earnings",
        "debit": -common_apic, "credit": Decimal("0"),
    })

# ---------------------------------------------------------------------------
# (e) Loss year -- hypothetical if-converted, antidilution, reported EPS
# ---------------------------------------------------------------------------
basic_eps_loss = per_share(NET_LOSS, WACS_LOSS_YEAR)        # -600,000 / 200,000

bond_interest = money(BOND_COUNT * BOND_FACE * BOND_RATE)   # 60,000
interest_after_tax = money(bond_interest * (Decimal("1") - TAX_RATE))  # 45,000
bond_conv_common = BOND_COUNT * BOND_CONV_SHARES            # 20,000

hypo_numerator = money(NET_LOSS + interest_after_tax)       # -555,000
hypo_denominator = WACS_LOSS_YEAR + bond_conv_common        # 220,000
hypothetical_diluted_eps = per_share(hypo_numerator, hypo_denominator)

# Antidilutive because the loss per share shrinks (moves toward zero).
antidilutive = hypothetical_diluted_eps > basic_eps_loss
reported_basic_eps_loss = basic_eps_loss
reported_diluted_eps_loss = basic_eps_loss if antidilutive else hypothetical_diluted_eps

# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------
journal_entries = [
    {"part": "a",
     "description": "January 1, Year 1 - issuance of 8,000 shares of 6%, $50 par "
                    "cumulative convertible preferred stock at par",
     "lines": je_a_lines},
    {"part": "b",
     "description": "Year 1 - declaration of preferred dividend "
                    "(8,000 x $50 par x 6%)",
     "lines": je_b_declare},
    {"part": "b",
     "description": "Year 1 - payment of preferred dividend",
     "lines": je_b_pay},
    {"part": "d",
     "description": "January 1, Year 2 - conversion of all 8,000 preferred shares "
                    "into 32,000 shares of $5 par common stock",
     "lines": je_d_lines},
]

# Balance check -- derivation must be fixed if this ever trips.
for entry in journal_entries:
    dr = sum((ln["debit"] for ln in entry["lines"]), Decimal("0"))
    cr = sum((ln["credit"] for ln in entry["lines"]), Decimal("0"))
    assert dr == cr, f"part {entry['part']} out of balance: {dr} vs {cr}"

answers = [
    {"label": "c: basic EPS, Year 1", "value": basic_eps_y1},
    {"label": "c: diluted EPS, Year 1 (if-converted)", "value": diluted_eps_y1},
    {"label": "e: hypothetical if-converted diluted EPS, loss year",
     "value": hypothetical_diluted_eps},
    {"label": "e: reported basic EPS, loss year", "value": reported_basic_eps_loss},
    {"label": "e: reported diluted EPS, loss year", "value": reported_diluted_eps_loss},
]

notes = (
    "c: Basic EPS = ($480,000 net income - $24,000 cumulative preferred dividend) "
    "/ 120,000 wtd-avg shares. If-converted diluted EPS adds the $24,000 preferred "
    "dividend back to the numerator ($480,000) and adds 8,000 x 4 = 32,000 "
    "conversion shares to the denominator (152,000). Dilutive test: earnings per "
    "incremental share = $24,000 / 32,000 = $" + str(eps_per_incremental_share) +
    ", which is below basic EPS of $" + str(basic_eps_y1) + ", so the preferred is "
    "DILUTIVE and is included (EPS falls from $" + str(basic_eps_y1) + " to $" +
    str(diluted_eps_y1) + "). "
    "d: The preferred was issued at par, so there is no Paid-In Capital in Excess "
    "of Par-Preferred to derecognize; the $400,000 carrying value exceeds the "
    "$160,000 common par issued (32,000 x $5), and the $240,000 remainder is "
    "credited to Paid-In Capital in Excess of Par-Common Stock. Equity is unchanged. "
    "e: Hypothetical if-converted figure = (-$600,000 net loss + $45,000 after-tax "
    "interest add-back [1,000 x $1,000 x 6% = $60,000, x (1 - 25%)]) / (200,000 + "
    "1,000 x 20 = 220,000 shares) = -$2.52. It is ANTIDILUTIVE because the assumed "
    "conversion makes the loss per share SMALLER (-$2.52 versus -$3.00) rather than "
    "reducing EPS. Under the loss-from-continuing-operations rule (ASC 260-10-45-19), "
    "when a loss from continuing operations exists no potential common shares are "
    "included in any diluted per-share amount, so reported basic EPS and reported "
    "diluted EPS are both -$3.00 (a $3.00 loss per share). "
    "Disclosure (ASC 260-10-50-1c): disclose that 20,000 potential common shares "
    "issuable on conversion of the 1,000 6% $1,000 convertible bonds were excluded "
    "from the computation of diluted EPS because their effect would have been "
    "antidilutive, together with full disclosure of the terms and conditions of "
    "those convertible bonds. "
    "b is shown as the textbook two-step (declaration then payment); the combined "
    "one-line form debits Retained Earnings $24,000 and credits Cash $24,000."
)

payload = {
    "id": ITEM_ID,
    "rounding_convention": (
        "decimal.Decimal throughout, never floats. Money quantized to $0.01 with "
        "ROUND_HALF_UP. EPS rounded once at the end to $0.01 with ROUND_HALF_UP "
        "(exact numerator / exact share count; no per-step rounding). No PV factors "
        "in this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}


# --- JSON emission: Decimals become bare JSON numbers, keeping exact digits ----
def _encode(obj, sink):
    if isinstance(obj, Decimal):
        token = "@@DEC%d@@" % len(sink)
        sink.append(str(obj))
        return token
    if isinstance(obj, dict):
        return {k: _encode(v, sink) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_encode(v, sink) for v in obj]
    return obj


def dumps_decimal(obj) -> str:
    sink = []
    text = json.dumps(_encode(obj, sink), indent=2)
    for i, literal in enumerate(sink):
        text = text.replace('"@@DEC%d@@"' % i, literal)
    return text


if __name__ == "__main__":
    print(dumps_decimal(payload))
