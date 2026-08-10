"""Solver for agent_039#00 — Summit Peak Manufacturing Co., cash & cash equivalents (LO 8-1).

Rounding convention: all money is decimal.Decimal; every rounding step uses
ROUND_HALF_UP to whole dollars (cents=0) applied per period / per amount.
All figures in this item are exact whole dollars, so rounding is non-distorting;
journal entries are stated in whole dollars and every schedule column foots
exactly to the source amounts (no plug, no forced close needed).
Nothing is hard-coded: the compensating balance is derived as 12% of principal,
the unrestricted First Prairie balance and the Heartland balance are derived by
subtracting the derived restricted / NSF amounts, and every total is a sum of
schedule rows.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("1")
def r(x):  # ROUND_HALF_UP to whole dollars
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def num(d):
    d = r(d)
    return int(d)

# ---------------- inputs (given data only) ----------------
principal        = Decimal("300000")
note_rate        = Decimal("0.08")
comp_pct         = Decimal("0.12")
cp_cost          = Decimal("54000")
cp_maturity_amt  = Decimal("54810")
tbill_dec_cost   = Decimal("24900")
tbill_dec_face   = Decimal("25000")
payroll_fund     = Decimal("14000")
sinking_fund     = Decimal("60000")
first_prairie    = Decimal("71200")
heartland        = Decimal("28400")
nsf_check        = Decimal("650")
savings          = Decimal("12000")
petty_cash       = Decimal("600")
cashiers_check   = Decimal("1800")
money_market     = Decimal("33000")
tbill_june_cost  = Decimal("16000")
travel_advance   = Decimal("2200")
postdated_check  = Decimal("1100")
overdraft        = Decimal("3500")

# ---------------- derived amounts ----------------
comp_balance   = r(principal * comp_pct)                 # legally restricted deposit
fp_unrestr     = r(first_prairie - comp_balance)         # freely available First Prairie cash
heartland_cash = r(heartland - nsf_check)                # after NSF reclass to A/R
cp_interest    = r(cp_maturity_amt - cp_cost)            # discount accretion earned
tbill_dec_disc = r(tbill_dec_face - tbill_dec_cost)      # unearned discount (not asked as JE)

# ---------------- journal entries ----------------
def E(part, desc, lines):
    dr = sum(r(l[1]) for l in lines if l[1] is not None)
    cr = sum(r(l[2]) for l in lines if l[2] is not None)
    assert dr == cr, (part, dr, cr)
    return {"part": part, "description": desc,
            "lines": [{"account": a, "debit": num(d or 0), "credit": num(c or 0)} for a, d, c in lines]}

jes = [
 E("a", "Jul 1, Yr 1 - borrow on one-year 8% note payable, First Prairie Bank",
   [("Cash - First Prairie Bank (checking)", principal, None),
    ("Note payable - First Prairie Bank", None, principal)]),
 E("a", "Jul 1, Yr 1 - initial recognition reclass of legally restricted 12% compensating balance",
   [("Restricted cash - compensating balance (current asset)", comp_balance, None),
    ("Cash - First Prairie Bank (checking)", None, comp_balance)]),
 E("b", "Nov 1, Yr 1 - purchase Atlas Power commercial paper, 60-day original maturity (cash equivalent)",
   [("Cash equivalents - commercial paper", cp_cost, None),
    ("Cash", None, cp_cost)]),
 E("c", "Dec 31, Yr 1 - maturity/settlement of commercial paper",
   [("Cash", cp_maturity_amt, None),
    ("Cash equivalents - commercial paper", None, cp_cost),
    ("Interest revenue", None, cp_interest)]),
 E("d", "Dec 1, Yr 1 - purchase U.S. T-bill, two months to maturity (cash equivalent)",
   [("Cash equivalents - U.S. Treasury bill", tbill_dec_cost, None),
    ("Cash", None, tbill_dec_cost)]),
 E("e", "Dec 20, Yr 1 - transfer to restricted payroll fund",
   [("Restricted cash - payroll fund", payroll_fund, None),
    ("Cash", None, payroll_fund)]),
 E("e", "Dec 22, Yr 1 - deposit with trustee, bond sinking fund (bonds mature in 5 years)",
   [("Restricted cash - bond sinking fund (noncurrent)", sinking_fund, None),
    ("Cash", None, sinking_fund)]),
 E("f", "Dec 31, Yr 1 - reclassify returned NSF customer check out of cash",
   [("Accounts receivable", nsf_check, None),
    ("Cash - Heartland Credit Union", None, nsf_check)]),
]

# ---------------- (f) Dec 31 classification schedule ----------------
CASH, CE = "Cash", "Cash equivalents"
RC_CUR, RC_NON = "Restricted cash - current", "Restricted cash - noncurrent"
OCA, STI, AR, CL = "Other current asset", "Short-term investment", "Accounts receivable", "Current liability"

schedule = [
 ("Checking - First Prairie Bank, unrestricted portion (71,200 less 36,000 legally restricted)", fp_unrestr, CASH),
 ("Checking - First Prairie Bank, legally restricted compensating balance (note matures Jun 30, Yr 2)", comp_balance, RC_CUR),
 ("Checking - Heartland Credit Union, after removing NSF check", heartland_cash, CASH),
 ("Heartland NSF check returned from customer - reclassified", nsf_check, AR),
 ("Savings account", savings, CASH),
 ("Petty cash", petty_cash, CASH),
 ("Cashier's check payable to Summit, dated Dec 29, on hand", cashiers_check, CASH),
 ("U.S. T-bill purchased Dec 1 (2 months original maturity to Summit)", tbill_dec_cost, CE),
 ("Money market fund (1 month original maturity to Summit, low credit risk)", money_market, CE),
 ("Restricted cash - payroll fund (paid Jan 5, Yr 2)", payroll_fund, RC_CUR),
 ("Restricted cash - bond sinking fund (bonds mature in 5 years)", sinking_fund, RC_NON),
 ("T-bill bought Jun 1 with 7 months to maturity (original maturity > 3 months)", tbill_june_cost, STI),
 ("Travel advance to employee for January sales trip", travel_advance, OCA + " - employee travel advance (prepaid/receivable from employee)"),
 ("Customer check postdated Jan 20, Yr 2", postdated_check, AR),
 ("Overdraft at Lakeside Bank (no other account at Lakeside, no right of offset)", overdraft, CL + " - bank overdraft payable"),
]

def total(pred):
    return r(sum((amt for _, amt, cls in schedule if pred(cls)), Decimal("0")))

cash_total   = total(lambda c: c == CASH)
ce_total     = total(lambda c: c == CE)
cce_combined = r(cash_total + ce_total)
rc_cur       = total(lambda c: c == RC_CUR)
rc_non       = total(lambda c: c == RC_NON)
ar_total     = total(lambda c: c == AR)
sti_total    = total(lambda c: c == STI)
oca_total    = total(lambda c: c.startswith(OCA))
cl_total     = total(lambda c: c.startswith(CL))

# foot check: schedule must reproduce the listed items exactly
listed = r(first_prairie + heartland + savings + petty_cash + cashiers_check + tbill_dec_cost +
           money_market + payroll_fund + sinking_fund + tbill_june_cost + travel_advance +
           postdated_check + overdraft)
assert r(sum(a for _, a, _ in schedule)) == listed

A = []
def add(label, value):
    A.append({"label": label, "value": value if isinstance(value, str) else num(value)})

# (a)
add("a: Jul 1 - Dr Cash (note proceeds deposited to First Prairie)", principal)
add("a: Jul 1 - Cr Note payable (one-year, 8%)", principal)
add("a: Jul 1 - Dr Restricted cash - compensating balance (12% x $300,000)", comp_balance)
add("a: Jul 1 - Cr Cash for the compensating-balance reclassification", comp_balance)
# (b)
add("b: Nov 1 - Dr Cash equivalents - commercial paper", cp_cost)
add("b: Nov 1 - Cr Cash", cp_cost)
# (c)
add("c: Dec 31 - Dr Cash on commercial paper maturity", cp_maturity_amt)
add("c: Dec 31 - Cr Cash equivalents - commercial paper (carrying amount removed)", cp_cost)
add("c: Dec 31 - Cr Interest revenue (discount accretion)", cp_interest)
# (d)
add("d: Dec 1 - Dr Cash equivalents - U.S. T-bill", tbill_dec_cost)
add("d: Dec 1 - Cr Cash", tbill_dec_cost)
# (e)
add("e: Dec 20 - Dr Restricted cash - payroll fund / Cr Cash", payroll_fund)
add("e: Dec 22 - Dr Restricted cash - bond sinking fund / Cr Cash", sinking_fund)
# (f) schedule rows
for name, amt, cls in schedule:
    add("f: %s -> %s" % (name, cls), amt)
add("f: NSF reclassifying entry - Dr Accounts receivable / Cr Cash", nsf_check)
add("f: schedule foots to the listed Dec 31 items", listed)
# (g) balance-sheet totals
add("g: Cash", cash_total)
add("g: Cash equivalents", ce_total)
add("g: Cash and cash equivalents combined", cce_combined)
add("g: Restricted cash - current", rc_cur)
add("g: Restricted cash - noncurrent", rc_non)
add("g: Current liability - bank overdraft (Lakeside)", cl_total)
# (h)
add("h: Note disclosure if the compensating balance were NOT legally restricted",
    "No reclassification: the $%s would stay in unrestricted Cash (Cash would be $%s and cash and cash "
    "equivalents $%s). Because the arrangement is only an informal understanding with First Prairie rather "
    "than a legal restriction, it is not segregated on the face of the balance sheet; instead Summit discloses "
    "the compensating-balance arrangement in the notes - the amount, the related 8%% one-year $%s note, and the "
    "fact that the deposit is not legally restricted but its maintenance is expected under the borrowing "
    "arrangement (so it is not fully available for general use and the effective borrowing rate is higher)."
    % (f"{comp_balance:,.0f}", f"{r(cash_total+comp_balance):,.0f}", f"{r(cce_combined+comp_balance):,.0f}",
       f"{principal:,.0f}"))

out = {
 "id": "agent_039#00",
 "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to whole dollars applied per period/per amount. "
                        "Journal entries stated in whole dollars; the Dec 31 classification schedule foots exactly to "
                        "the listed item amounts with no plug (all inputs are exact whole dollars).",
 "answers": A,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": "Cash equivalent test is original maturity to Summit of 3 months or less: the Nov 1 commercial paper "
          "(60 days) and the Dec 1 T-bill (2 months) and the money market fund (1 month) qualify; the T-bill bought "
          "Jun 1 with 7 months to run does NOT qualify even though only 2 months remain - it is a short-term "
          "investment. Legally restricted compensating balance ($36,000) is restricted cash-current because the note "
          "matures Jun 30, Year 2. Payroll fund is restricted cash-current (paid Jan 5, Year 2); bond sinking fund is "
          "restricted cash-noncurrent (bonds mature in 5 years). NSF check and the postdated customer check go back to "
          "accounts receivable; the employee travel advance is an other current asset; the Lakeside overdraft is a "
          "current liability because Summit has no other Lakeside account to offset against. Interest accrual on the "
          "8% note (Jul 1-Dec 31) and accretion on the Dec 1 T-bill were not requested by any Required part."
}
print(json.dumps(out, indent=1))
