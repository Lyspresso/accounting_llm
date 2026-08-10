#!/usr/bin/env python3
"""Solver for item agent_164#02 — Maplewick Analytics LLC, SCF (LO 22-1).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to the cent (Decimal quantize to 0.01) applied at every point a
money figure is produced; results are then emitted as whole dollars because
every fact in the stem is a whole-dollar amount and no rate, allocation, or
present-value factor appears anywhere in the fact pattern. All arithmetic uses
decimal.Decimal exclusively — no binary floats touch a money value at any stage.
No per-period compounding or PV table factors are involved in this item.

DERIVATION BASIS (ASC 230, as presented in the ACCOUNT-343 Ch. 22 material)
---------------------------------------------------------------------------
Part A — classification is driven by a small rule table rather than a lookup of
memorized answers. Each item is described by the attributes that ASC 230 keys
on (is the counterparty relationship trade or nontrade? is the cash principal
or interest? is the security held in a trading account? is the instrument debt/
equity financing?), and the classifier applies these rules:

  R1  ASC 230-10-45-19 / 45-18: purchases and sales of trading debt and equity
      securities are classified by the nature and purpose of acquisition; held
      specifically for resale in a trading account  ->  OPERATING.
  R2  ASC 230-10-45-12/13: purchases and sales of non-trading investments,
      PP&E, and intangibles  ->  INVESTING.
  R3  Trade receivables arise from selling goods/services, so collecting their
      principal is a normal operating collection  ->  OPERATING. Only NONTRADE
      loans receivable are investing (Ch. 22: "collection of a loan (nontrade)").
  R4  Interest received and interest paid are OPERATING; dividends received are
      OPERATING; dividends PAID are FINANCING (Ch. 22 handout, LO 22-1).
  R5  ASC 230-10-45-14/15: proceeds from issuing debt (short- or long-term,
      nontrade) are FINANCING inflows; repayments of borrowed principal,
      including finance-lease liability principal and bond extinguishment, are
      FINANCING outflows.

Part B — "Cash" on the SCF reconciliation means cash + cash equivalents +
restricted cash (ASC 230-10-45-24; Ch. 22 line: "'Cash' includes cash, cash
equivalents, and restricted cash"). Investments that are not cash equivalents
are excluded. Beginning cash is then solved from the reconciliation identity
  ending = beginning + (operating + investing + financing)
=> beginning = ending - net change.

Part C — patent sale: cash proceeds recognized, carrying (book) value derecog-
nized, difference is gain/loss (plug). Finance-lease principal payment reduces
the lease liability dollar for dollar.

Part D — ASC 230-10-45-26 requires investing and financing inflows and outflows
to be reported separately (gross). The only exception (ASC 230-10-45-8/45-9) is
for items whose original maturity is three months or less; equipment purchases
and sales never qualify.

Part E — Ch. 22 handout format: Operating, Investing, Financing, net change,
beginning cash, ending cash.

Run:  python3 solver.py   -> prints one JSON object to stdout.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: str | Decimal) -> Decimal:
    """Every money value enters as a Decimal and is quantized ROUND_HALF_UP."""
    return (x if isinstance(x, Decimal) else Decimal(x)).quantize(
        CENT, rounding=ROUND_HALF_UP
    )


def out(d: Decimal):
    """Emit whole dollars when exact, else a 2-dp float-free string->number."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# PART A — rule-based classifier
# ---------------------------------------------------------------------------

# Each item is described by facts drawn from the stem, never by an answer.
#   kind:      what economic event occurred
#   direction: "in" if cash is received, "out" if cash is paid
#   flags:     the attributes ASC 230 keys on
ITEMS = [
    (1, "Payment of principal on a finance lease liability",
     dict(kind="debt_principal_repayment", direction="out", nontrade_debt=True)),
    (2, "Cash purchase of trading equity securities held for short-term resale profits",
     dict(kind="security_purchase", direction="out", trading_account=True)),
    (3, "Cash proceeds from sale of those same trading securities",
     dict(kind="security_sale", direction="in", trading_account=True)),
    (4, "Cash purchase of available-for-sale debt securities held for long-term yield",
     dict(kind="security_purchase", direction="out", trading_account=False)),
    (5, "Collection of principal on a short-term trade note receivable from an inventory sale",
     dict(kind="receivable_principal_collection", direction="in", trade_receivable=True)),
    (6, "Collection of interest on that same trade note",
     dict(kind="interest_received", direction="in")),
    (7, "Cash paid for early extinguishment of long-term bonds (principal and premium)",
     dict(kind="debt_principal_repayment", direction="out", nontrade_debt=True)),
    (8, "Cash proceeds from sale of a patent",
     dict(kind="longterm_asset_sale", direction="in")),
    (9, "Cash received from issuance of a short-term nontrade note payable for general financing",
     dict(kind="debt_issuance", direction="in", nontrade_debt=True)),
    (10, "Payment of a cash dividend declared in the prior year",
     dict(kind="dividend_paid", direction="out")),
]


def classify(f: dict) -> tuple[str, str]:
    """Return (section, rule) for a fact bundle. Raises if no rule fits."""
    k = f["kind"]

    # R1 — trading securities follow the purpose of acquisition -> operating.
    if k in ("security_purchase", "security_sale"):
        if f.get("trading_account"):
            return "O", "R1 ASC 230-10-45-19: trading-account securities -> operating"
        # R2 — every other investment purchase/sale is investing.
        return "I", "R2 ASC 230-10-45-12/13: non-trading investment -> investing"

    # R2 — long-term / intangible asset disposals are investing.
    if k == "longterm_asset_sale":
        return "I", "R2 ASC 230-10-45-12(c): sale of intangible (patent) -> investing"

    # R3 — trade receivable principal is operating; nontrade loans are investing.
    if k == "receivable_principal_collection":
        if f.get("trade_receivable"):
            return "O", "R3 trade receivable from sale of goods -> operating"
        return "I", "R3 collection of a NONTRADE loan -> investing"

    # R4 — interest and dividends received are operating; dividends paid financing.
    if k == "interest_received":
        return "O", "R4 interest received -> operating"
    if k == "dividend_paid":
        return "F", "R4/R5 ASC 230-10-45-15(a): dividends paid -> financing"

    # R5 — debt financing flows.
    if k == "debt_issuance":
        return "F", "R5 ASC 230-10-45-14(b): proceeds from issuing debt -> financing"
    if k == "debt_principal_repayment":
        return "F", "R5 ASC 230-10-45-15(b): repayment of borrowed principal -> financing"

    raise ValueError(f"no classification rule for {k!r}")


def part_a():
    rows = []
    for num, text, facts in ITEMS:
        section, rule = classify(facts)
        flow = "inflow" if facts["direction"] == "in" else "outflow"
        rows.append(
            {
                "n": num,
                "text": text,
                "code": f"{section} {flow}",
                "rule": rule,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# PART B — period-end cash total and beginning cash
# ---------------------------------------------------------------------------

# (label, amount, is it cash / cash equivalent / restricted cash?)
BALANCES = [
    ("Cash in bank (unrestricted)", money("48000"), True),
    ("Money-market cash equivalents", money("12000"), True),
    ("Restricted cash (compensating balance, long-term debt agreement)", money("5000"), True),
    ("Short-term AFS equity investments (not cash equivalents)", money("22000"), False),
]

NET_OPERATING = money("90000")
NET_INVESTING = money("-70000")
NET_FINANCING = money("-15000")


def part_b():
    ending = sum((amt for _, amt, incl in BALANCES if incl), Decimal("0"))
    ending = money(ending)
    net_change = money(NET_OPERATING + NET_INVESTING + NET_FINANCING)
    beginning = money(ending - net_change)
    return ending, beginning, net_change


# ---------------------------------------------------------------------------
# PART C — journal entries
# ---------------------------------------------------------------------------

PATENT_BOOK_VALUE = money("18000")
PATENT_PROCEEDS = money("22500")
LEASE_PRINCIPAL = money("9000")


def part_c():
    # Patent sale: gain/loss is the plug between proceeds and carrying amount.
    gain = money(PATENT_PROCEEDS - PATENT_BOOK_VALUE)
    patent_lines = [
        {"account": "Cash", "debit": out(PATENT_PROCEEDS), "credit": 0},
        {"account": "Patent", "debit": 0, "credit": out(PATENT_BOOK_VALUE)},
    ]
    if gain > 0:
        patent_lines.append(
            {"account": "Gain on Sale of Patent", "debit": 0, "credit": out(gain)}
        )
    elif gain < 0:
        patent_lines.insert(
            1, {"account": "Loss on Sale of Patent", "debit": out(-gain), "credit": 0}
        )

    lease_lines = [
        {"account": "Lease Liability", "debit": out(LEASE_PRINCIPAL), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": out(LEASE_PRINCIPAL)},
    ]

    entries = [
        {
            "part": "c",
            "description": (
                "Sale of patent (book value 18,000) for 22,500 cash — "
                "SCF: Investing inflow 22,500; the 4,500 gain is deducted from "
                "net income in the operating section under the indirect method"
            ),
            "lines": patent_lines,
        },
        {
            "part": "c",
            "description": (
                "Cash principal payment on finance lease liability — "
                "SCF: Financing outflow 9,000 (interest paid is operating)"
            ),
            "lines": lease_lines,
        },
    ]

    # Debits must equal credits in every entry.
    for e in entries:
        dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
        cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
        assert money(dr) == money(cr), f"unbalanced entry: {e['description']}"

    return entries, gain


# ---------------------------------------------------------------------------
# PARTS D and E
# ---------------------------------------------------------------------------

PART_D = (
    "False. ASC 230-10-45-26 requires investing (and financing) cash inflows and "
    "outflows to be reported separately on a GROSS basis: cash paid to purchase "
    "equipment must be shown apart from cash received from selling equipment; "
    "they may not be netted to simplify the statement. The only exception "
    "(ASC 230-10-45-8/45-9) permits net reporting for investments other than "
    "cash equivalents, loans receivable, and debt whose ORIGINAL MATURITY is "
    "three months or less (e.g., a revolving line of credit) — which never "
    "covers equipment purchases and sales."
)

PART_E = (
    "1) Cash flows from operating activities; 2) Cash flows from investing "
    "activities; 3) Cash flows from financing activities; = Net change in cash, "
    "cash equivalents, and restricted cash for the period; + Cash, cash "
    "equivalents, and restricted cash at the beginning of the period; = Cash, "
    "cash equivalents, and restricted cash at the end of the period."
)


def main() -> None:
    a_rows = part_a()
    ending, beginning, _net_change = part_b()
    entries, _gain = part_c()

    answers = []
    for r in a_rows:
        answers.append({"label": f"a{r['n']}: {r['text']}", "value": r["code"]})

    answers.append(
        {
            "label": "b: ending cash total on the SCF reconciliation "
                     "(cash + cash equivalents + restricted cash)",
            "value": out(ending),
        }
    )
    answers.append({"label": "b: beginning cash", "value": out(beginning)})

    answers.append(
        {"label": "c: SCF section for the patent sale proceeds",
         "value": "Investing inflow 22500 (gain 4500 deducted from net income in operating)"}
    )
    answers.append(
        {"label": "c: SCF section for the finance-lease principal payment",
         "value": "Financing outflow 9000"}
    )

    answers.append({"label": "d: true/false with correction", "value": PART_D})
    answers.append({"label": "e: required section order on the face of the SCF",
                    "value": PART_E})

    result = {
        "id": "agent_164#02",
        "rounding_convention": (
            "decimal.Decimal throughout, ROUND_HALF_UP quantized to the cent at "
            "every money step; all stem facts are whole dollars so results are "
            "exact whole dollars. No PV factors or per-period compounding apply."
        ),
        "answers": answers,
        "journal_entries": entries,
        "insufficient_info": False,
        "notes": (
            "Part A rules: trading securities follow purpose of acquisition "
            "(operating, items 2-3); non-trading AFS investment purchase is "
            "investing (4); trade-note principal and interest are both operating "
            "(5-6) because only NONTRADE loan collections are investing; patent "
            "proceeds are investing (8); finance-lease principal, bond "
            "extinguishment, nontrade note issuance, and dividends paid are all "
            "financing (1, 7, 9, 10). Part B includes restricted cash per "
            "ASC 230-10-45-24 and excludes the 22,000 AFS equity investments, "
            "which are not cash equivalents."
        ),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
