"""SummitRidge Packaging Corp. — stock dividends (small/large) and a true split.

Rounding convention: all monetary amounts use decimal.Decimal, quantized to the
cent with ROUND_HALF_UP applied once per period/amount (no float arithmetic
anywhere). Share counts are exact integers; par per share is a Decimal.
Every figure is derived from the Dec 15 Year 1 trial balance inputs and the
scenario rates -- nothing is hard-coded downstream. Dr = Cr is asserted for
each journal entry.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def m(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(d):
    d = m(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---- Given (Dec 15, Year 1, immediately before any action) ----
PAR0        = Decimal("3")
SHARES0     = 60000
CS0         = m(PAR0 * SHARES0)              # 180,000
PIC0        = m("540000")
RE0         = m("750000")
TOTAL0      = m(CS0 + PIC0 + RE0)            # 1,470,000
MKT         = Decimal("22")
RATE_A      = Decimal("0.12")
RATE_B      = Decimal("0.50")
SPLIT_C     = Decimal("2")

assert TOTAL0 == m("1470000")

# ================= Scenario A — 12% SMALL stock dividend (FV) =================
sh_A      = int(Decimal(SHARES0) * RATE_A)          # 7,200 whole shares
fv_A      = m(Decimal(sh_A) * MKT)                  # charge to RE at fair value
par_A     = m(Decimal(sh_A) * PAR0)                 # credit CSDD at par
pic_A     = m(fv_A - par_A)                         # excess over par

# (1) immediately before declaration
r1 = dict(CS=CS0, CSDD=m(0), PIC=PIC0, RE=RE0, total=m(CS0+PIC0+RE0),
          shares=SHARES0, par=PAR0)
# (2) Dec 31 Year 1 — after declaration, before distribution
r2_CS, r2_CSDD = CS0, par_A
r2_PIC = m(PIC0 + pic_A)
r2_RE  = m(RE0 - fv_A)
r2 = dict(CS=r2_CS, CSDD=r2_CSDD, PIC=r2_PIC, RE=r2_RE,
          total=m(r2_CS + r2_CSDD + r2_PIC + r2_RE), shares=SHARES0, par=PAR0)
# (3) after distribution Jan 12 Year 2
r3_CS = m(r2_CS + r2_CSDD)
r3 = dict(CS=r3_CS, CSDD=m(0), PIC=r2_PIC, RE=r2_RE,
          total=m(r3_CS + r2_PIC + r2_RE), shares=SHARES0 + sh_A, par=PAR0)
assert r1["total"] == r2["total"] == r3["total"] == TOTAL0
assert m(Decimal(r3["shares"]) * PAR0) == r3_CS

# ================= Scenario B — 50% LARGE stock dividend (par) ================
sh_B   = int(Decimal(SHARES0) * RATE_B)             # 30,000 shares
par_B  = m(Decimal(sh_B) * PAR0)                    # measured at par, not FV
B_CS   = m(CS0 + par_B)
B_PIC  = PIC0
B_RE   = m(RE0 - par_B)
B_SH   = SHARES0 + sh_B
B_TOT  = m(B_CS + B_PIC + B_RE)
assert B_TOT == TOTAL0 and m(Decimal(B_SH) * PAR0) == B_CS

# ================= Scenario C — true 2-for-1 split (par reduced) =============
C_SH   = int(Decimal(SHARES0) * SPLIT_C)            # 120,000
C_PAR  = (PAR0 / SPLIT_C).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
C_CS   = m(Decimal(C_SH) * C_PAR)
assert C_CS == CS0

def je(part, desc, lines):
    d = sum(m(l[1]) for l in lines if l[1] is not None)
    c = sum(m(l[2]) for l in lines if l[2] is not None)
    assert d == c, (part, d, c)
    return {"part": part, "description": desc,
            "lines": [{"account": a, "debit": n(dr or 0), "credit": n(cr or 0)}
                      for a, dr, cr in lines]}

jes = [
 je("a", "Dec 15, Year 1 — declaration of 12% small stock dividend at fair value", [
    ("Retained Earnings (Stock Dividends Declared)", fv_A, None),
    ("Common Stock Dividends Distributable", None, par_A),
    ("Paid-in Capital in Excess of Par—Common Stock", None, pic_A)]),
 je("b", "Dec 31, Year 1 — no adjusting entry required (memo only)", [
    ("No entry required", Decimal(0), None),
    ("No entry required", None, Decimal(0))]),
 je("d", "Jan 12, Year 2 — distribution/settlement of the 12% stock dividend", [
    ("Common Stock Dividends Distributable", par_A, None),
    ("Common Stock, $3 par", None, par_A)]),
 je("e-1", "Dec 15, Year 1 — declaration of 50% large stock dividend at par", [
    ("Retained Earnings (Stock Dividends Declared)", par_B, None),
    ("Common Stock Dividends Distributable", None, par_B)]),
 je("e-2", "Jan 12, Year 2 — distribution of the 50% large stock dividend", [
    ("Common Stock Dividends Distributable", par_B, None),
    ("Common Stock, $3 par", None, par_B)]),
 je("f", "Dec 15, Year 1 — true 2-for-1 split: no journal entry (memorandum only)", [
    ("No entry required", Decimal(0), None),
    ("No entry required", None, Decimal(0))]),
]

A = []
def add(label, value): A.append({"label": label, "value": value})

# --- a ---
add("a: Scenario A — shares issued as 12% small stock dividend (60,000 x 12%)", sh_A)
add("a: Scenario A — measurement basis = fair value per share", n(MKT))
add("a: Dr Retained Earnings (Stock Dividends) at fair value 7,200 x $22", n(fv_A))
add("a: Cr Common Stock Dividends Distributable at par 7,200 x $3", n(par_A))
add("a: Cr Paid-in Capital in Excess of Par—Common Stock ($158,400 - $21,600)", n(pic_A))
add("a: total debits = total credits (Dr = Cr)", n(fv_A))

# --- b ---
add("b: Dec 31, Year 1 adjusting journal entry required for the stock dividend",
    "None — no adjusting entry. The declaration entry was already recorded Dec 15; "
    "a stock dividend requires no accrual, no interest, and no year-end remeasurement.")
add("b: Dec 31, Year 1 classification/presentation of Common Stock Dividends Distributable",
    "Stockholders' equity — reported in the paid-in capital section immediately below "
    "(or as an addition to) Common Stock; it is NOT a liability because it will be settled "
    "by issuing shares, not by transferring assets.")
add("b: Common Stock Dividends Distributable balance at Dec 31, Year 1", n(par_A))

# --- c: schedule, three columns ---
for tag, r in (("(1) immediately before declaration (Dec 15, Yr 1)", r1),
               ("(2) Dec 31, Yr 1 — after declaration, before distribution", r2),
               ("(3) after distribution (Jan 12, Yr 2)", r3)):
    add(f"c: {tag} — Common Stock", n(r["CS"]))
    add(f"c: {tag} — Common Stock Dividends Distributable", n(r["CSDD"]))
    add(f"c: {tag} — Paid-in Capital in Excess of Par—Common Stock", n(r["PIC"]))
    add(f"c: {tag} — Retained Earnings", n(r["RE"]))
    add(f"c: {tag} — Total stockholders' equity", n(r["total"]))
    add(f"c: {tag} — Shares outstanding", r["shares"])
    add(f"c: {tag} — Par value per share", n(r["par"]))

# --- d ---
add("d: Jan 12, Year 2 — Dr Common Stock Dividends Distributable", n(par_A))
add("d: Jan 12, Year 2 — Cr Common Stock ($3 par, 7,200 shares issued)", n(par_A))
add("d: effect on total stockholders' equity of the distribution", 0)

# --- e ---
add("e: Scenario B — additional shares (60,000 x 50%)", sh_B)
add("e: Scenario B — Dec 15 Dr Retained Earnings at par (30,000 x $3)", n(par_B))
add("e: Scenario B — Dec 15 Cr Common Stock Dividends Distributable", n(par_B))
add("e: Scenario B — Jan 12 Dr Common Stock Dividends Distributable", n(par_B))
add("e: Scenario B — Jan 12 Cr Common Stock", n(par_B))
add("e: Scenario B — ending Common Stock after distribution", n(B_CS))
add("e: Scenario B — ending Paid-in Capital in Excess of Par (unchanged)", n(B_PIC))
add("e: Scenario B — ending Retained Earnings", n(B_RE))
add("e: Scenario B — ending shares outstanding", B_SH)
add("e: Scenario B — ending total stockholders' equity", n(B_TOT))

# --- f ---
add("f: Scenario C — journal entry required for the true 2-for-1 split",
    "None — a true stock split is recorded by memorandum entry only; no account "
    "balances change (par per share is halved and shares are doubled).")
add("f: Scenario C — shares outstanding after the split", C_SH)
add("f: Scenario C — par value per share after the split", n(C_PAR))
add("f: Scenario C — total Common Stock dollar amount after the split", n(C_CS))

print(json.dumps({
 "id": "agent_373#00",
 "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent, applied once per amount/period; no floats; share counts exact integers.",
 "answers": A,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": "Small (12%) dividend measured at fair value $22 (RE charged $158,400 = par $21,600 + PIC $136,800); large (50%) dividend measured at par ($90,000 to RE), market ignored. CSDD is an equity account, never a liability. Total stockholders' equity stays $1,470,000 in all three scenarios; only its composition and share count change. True split = memo only, so Common Stock stays $180,000 with par cut to $1.50 on 120,000 shares."
}, indent=1))
