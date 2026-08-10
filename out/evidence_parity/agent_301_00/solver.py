"""Summit Peak Manufacturing Co. — cash / cash equivalents / restricted cash.

Rounding convention: all money is decimal.Decimal, quantized to 0.01 (cents)
using ROUND_HALF_UP at each period/step. No floats are used for money.
Every figure is derived from the scenario inputs; nothing is hard-coded as a
result. Dr = Cr is asserted for every journal entry.
"""
import json
from decimal import Decimal as D, ROUND_HALF_UP

CENT = D("0.01")
def m(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)

def num(x):
    x = m(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------------- inputs (scenario facts only) ----------------
open_unrestricted = m("168000")
open_ce           = m("0")
open_rc_cur       = m("0")
open_rc_noncur    = m("0")

note_principal    = m("360000")
note_rate         = D("0.07")
comp_pct          = D("0.08")

cp_cost           = m("54000")
cp_maturity_value = m("54486")

tbill_nov_cost    = m("36800")
div_fund          = m("14200")
sinking_fund      = m("63500")

crestview_total   = m("76400")
prairie_total     = m("42800")
nsf_check         = m("1150")
savings           = m("18600")
petty_cash        = m("650")
cashiers_check    = m("3400")
money_market      = m("33000")
tbill_aug_cost    = m("27000")
travel_advance    = m("2250")
postdated_check   = m("1880")
overdraft_redrock = m("3750")

# ---------------- derived ----------------
comp_balance = m(note_principal * comp_pct)            # 8% legally restricted
cp_interest  = m(cp_maturity_value - cp_cost)          # discount interest

JE = []
def je(part, lines):
    dr = sum((m(l[1]) for l in lines), D("0"))
    cr = sum((m(l[2]) for l in lines), D("0"))
    assert dr == cr, (part, dr, cr)
    JE.append({"part": part, "lines": [
        {"account": a, "debit": num(d), "credit": num(c)} for a, d, c in lines]})

# (a) October 1
je("a (Oct 1 — borrowing on one-year 7% note)", [
    ("Cash (Checking—Crestview National)", note_principal, D(0)),
    ("Notes Payable (current)", D(0), note_principal),
])
je("a (Oct 1 — initial recognition reclass of legally restricted compensating balance)", [
    ("Restricted Cash—Compensating Balance (current)", comp_balance, D(0)),
    ("Cash (Checking—Crestview National)", D(0), comp_balance),
])
# (b) October 15
je("b (Oct 15 — purchase of 45-day commercial paper as a cash equivalent)", [
    ("Cash Equivalents—Commercial Paper", cp_cost, D(0)),
    ("Cash", D(0), cp_cost),
])
# (c) November 29
je("c (Nov 29 — maturity/settlement of commercial paper)", [
    ("Cash", cp_maturity_value, D(0)),
    ("Cash Equivalents—Commercial Paper", D(0), cp_cost),
    ("Interest Revenue", D(0), cp_interest),
])
# (d) three entries
je("d (Nov 20 — purchase of U.S. Treasury bill, 2 months to maturity, cash equivalent)", [
    ("Cash Equivalents—U.S. Treasury Bill", tbill_nov_cost, D(0)),
    ("Cash", D(0), tbill_nov_cost),
])
je("d (Dec 5 — transfer to restricted dividend fund)", [
    ("Restricted Cash—Dividend Fund (current)", div_fund, D(0)),
    ("Cash", D(0), div_fund),
])
je("d (Dec 12 — deposit with trustee for bond sinking fund, bonds mature in 5 years)", [
    ("Restricted Cash—Bond Sinking Fund (noncurrent)", sinking_fund, D(0)),
    ("Cash", D(0), sinking_fund),
])
# (f) December 31 NSF reclass
je("f (Dec 31 — period-end reclassifying entry for NSF check)", [
    ("Accounts Receivable", nsf_check, D(0)),
    ("Cash (Checking—Prairie Credit Union)", D(0), nsf_check),
])

ANS = []
def a(label, value):
    ANS.append({"label": label, "value": num(value) if isinstance(value, (D, int)) else value})

# ---------- (e) rolling classification schedule (chronological) ----------
u, ce, rcc, rcn = open_unrestricted, open_ce, open_rc_cur, open_rc_noncur

def row(tag):
    a("e: %s — Unrestricted cash" % tag, u)
    a("e: %s — Cash equivalents" % tag, ce)
    a("e: %s — Restricted cash—current" % tag, rcc)
    a("e: %s — Restricted cash—noncurrent" % tag, rcn)

row("Balances immediately before Oct 1, Year 1")

u = m(u + note_principal - comp_balance); rcc = m(rcc + comp_balance)
row("After Oct 1 borrowing and compensating-balance reclass")

u = m(u - cp_cost); ce = m(ce + cp_cost)
row("After Oct 15 commercial-paper purchase")

u = m(u - tbill_nov_cost); ce = m(ce + tbill_nov_cost)
row("After Nov 20 T-bill purchase")

u = m(u + cp_maturity_value); ce = m(ce - cp_cost)
row("After Nov 29 commercial-paper maturity (incl. $%s interest)" % cp_interest)

u = m(u - div_fund); rcc = m(rcc + div_fund)
row("After Dec 5 dividend-fund transfer")

u = m(u - sinking_fund); rcn = m(rcn + sinking_fund)
row("After Dec 12 bond-sinking-fund deposit")

# ---------- (g) December 31 classification schedule ----------
crestview_unrestricted = m(crestview_total - comp_balance)
prairie_net            = m(prairie_total - nsf_check)

a("g: Checking—Crestview National $%s — unrestricted Cash portion" % crestview_total, crestview_unrestricted)
a("g: Checking—Crestview National — legally restricted compensating balance to Restricted cash—current", comp_balance)
a("g: Checking—Prairie Credit Union $%s less NSF check $%s — Cash" % (prairie_total, nsf_check), prairie_net)
a("g: NSF check reclassified out of Cash to Accounts Receivable", nsf_check)
a("g: Savings account — Cash", savings)
a("g: Petty cash — Cash", petty_cash)
a("g: Cashier's check dated Dec 29, on hand — Cash", cashiers_check)
a("g: U.S. T-bill purchased Nov 20 (2 months original maturity to Summit Peak) — Cash equivalents", tbill_nov_cost)
a("g: Money market fund (1-month original maturity, low risk) — Cash equivalents", money_market)
a("g: Restricted cash—Dividend fund (paid Jan 15, Year 2) — Restricted cash—current", div_fund)
a("g: Restricted cash—Bond sinking fund (bonds mature in 5 years) — Restricted cash—noncurrent", sinking_fund)
a("g: T-bill bought Aug 1 with 4 months to maturity — NOT a cash equivalent; short-term investment (current asset)", tbill_aug_cost)
a("g: Travel advance to employee for January trip — NOT cash; receivable from employee / prepaid travel", travel_advance)
a("g: Customer check postdated Jan 12, Year 2 — NOT cash; Accounts Receivable", postdated_check)
a("g: Overdraft at Redrock Bank (no other Redrock account, no right of offset) — NOT a reduction of cash; current liability", overdraft_redrock)

# ---------- (h) balance-sheet totals ----------
cash_total = m(crestview_unrestricted + prairie_net + savings + petty_cash + cashiers_check)
ce_total   = m(tbill_nov_cost + money_market)
rcc_total  = m(comp_balance + div_fund)
rcn_total  = m(sinking_fund)

a("h: Cash (Dec 31, Year 1)", cash_total)
a("h: Cash equivalents (Dec 31, Year 1)", ce_total)
a("h: Restricted cash—current (Dec 31, Year 1)", rcc_total)
a("h: Restricted cash—noncurrent (Dec 31, Year 1)", rcn_total)
a("h: Current liability—bank overdraft payable (Redrock)", overdraft_redrock)

# ---------- (i) note disclosure if not legally restricted ----------
a("i: Note-disclosure treatment if the compensating balance were NOT legally restricted",
  "No reclassification would be made: the $%s would stay inside unrestricted Cash on the "
  "balance sheet (Cash would be $%s and Restricted cash—current only $%s). The arrangement "
  "would instead be described in the notes — the existence and nature of the compensating-"
  "balance agreement with Crestview National, the amount involved, the related borrowing it "
  "supports, and the fact that it raises the effective cost of the borrowing above the 7%% "
  "stated rate. Segregation as a separate restricted asset is required only when the "
  "compensating balance is legally restricted." % (comp_balance, m(cash_total + comp_balance), div_fund))

print(json.dumps({
  "id": "agent_301#00",
  "rounding_convention": "decimal.Decimal throughout; every money amount quantized to 0.01 with ROUND_HALF_UP at each step/period; no floats used for money; all amounts derived, none hard-coded",
  "answers": ANS,
  "journal_entries": JE,
  "insufficient_info": False,
  "notes": ("Chronological ordering used for the (e) roll-forward: Oct 1, Oct 15, Nov 20, Nov 29, Dec 5, Dec 12. "
            "Compensating balance = 8% x $360,000 = $28,800; note matures Oct 1, Year 2, so the restriction lapses "
            "within 12 months of the balance-sheet date and it is Restricted cash—CURRENT. Commercial-paper discount "
            "interest = $54,486 - $54,000 = $486, credited to Interest Revenue and added to unrestricted cash. "
            "Cash-equivalent test is original maturity TO SUMMIT PEAK of three months or less: the Nov 20 T-bill "
            "(2 months) and money market fund (1 month) qualify; the Aug 1 T-bill had 4 months remaining when "
            "acquired and is a short-term investment, not a cash equivalent. Postdated check, employee travel "
            "advance and the NSF check are receivables, not cash. The Redrock overdraft cannot be netted because "
            "Summit Peak holds no other account at that bank, so it is reported as a current liability. "
            "Cash $111,900 + cash equivalents $69,800 are presented as separate captions per part (h).")
}, indent=1))
