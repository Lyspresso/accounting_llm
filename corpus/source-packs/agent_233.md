# Agent 233 — CORE DEMO — LO 16-12

**Chapter:** 16  
**LO title:** Account for debt settlement and restructuring  
**Critical gap LO:** no

## Concept list for this pack
- **Troubled debt restructuring (debtor):** creditor grants a concession it would not otherwise consider because of the debtor’s financial difficulties
- **Settlement — transfer of assets:** remeasure transferred assets to fair value (gain/loss on disposal); derecognize debt and assets; **gain on restructuring** = carrying amount of debt − fair value of assets transferred
- **Settlement — transfer of equity:** issue equity at fair value; **gain on restructuring** = carrying amount of debt − fair value of equity issued
- **Modification of terms — sum of restructured cash flows < debt carrying amount:** reduce carrying amount to **undiscounted** total future cash payments; recognize **gain** immediately; subsequent effective rate = **0%** (payments reduce carrying amount; no interest expense)
- **Modification of terms — sum of restructured cash flows > debt carrying amount (emphasis):** **no** carrying-amount write-down and **no** gain at restructuring; combine principal and accrued interest into the note; compute a **new effective interest rate** that equates PV of future cash payments to the pre-restructure carrying amount; prepare an **effective-interest amortization schedule**
- **Period-end adjusting / subsequent JE:** cash interest payment split between **Interest Expense** (CA × new effective rate) and reduction of Note Payable
- **Maturity / settlement JE:** pay remaining face (carrying amount rolls to face under the schedule)

---

### Q1 — CORE — Modification when restructured payments exceed carrying amount (emphasis: subsequent measurement schedule)
**LO:** LO 16-12  
**Concept:** Troubled debt modification — no gain when total future cash flows exceed debt carrying amount; new effective rate; multi-period amortization schedule; period-end interest JEs; maturity settlement  
**Scenario:**  
**Northspire Outfitters** (calendar-year debtor) issued a note and later renegotiated with its creditor after missing an interest payment.

| Fact | Amount / term |
|---|---|
| Original note issue date | **January 1, Year 1** |
| Face amount | **$500,000** |
| Stated rate (original) | **12%**, interest due each **December 31** |
| Term (original) | **2 years** (due January 1, Year 3) |
| Consideration at issuance | Merchandise inventory valued at **$500,000** |
| December 31, Year 1 interest | **Not paid**; Northspire **accrued** interest of **$60,000** |
| Carrying amount of debt, January 1, Year 2 | **$560,000** ($500,000 note + $60,000 interest payable) |
| Troubled debt restructure date | **January 1, Year 2** (creditor grants a concession) |

**Restructured terms (modification of terms only — no asset or equity transfer):**

| Term | Provision |
|---|---|
| Accrued Year 1 interest | Forgiven (combined into restructured note accounting) |
| Face amount | Remains **$500,000** |
| New maturity | **January 1, Year 4** (one-year extension) |
| New stated rate | **9%**; cash interest of **$45,000** due **December 31, Year 2** and **December 31, Year 3** |
| Principal payment | **$500,000** on **January 1, Year 4** |

**Required:**  
a. Record the **January 1, Year 1** journal entry for **initial recognition** of the note (debtor).  
b. Record the **December 31, Year 1** accrual of unpaid interest.  
c. Compute the **sum of restructured cash flows**, compare to the **January 1, Year 2 carrying amount**, and state whether the debtor recognizes a **gain** at restructuring.  
d. Compute the **new effective interest rate** (show the RATE inputs: N, PMT, PV, FV).  
e. Prepare the complete **subsequent-measurement amortization schedule** (effective interest method) from January 1, Year 2 through maturity, showing cash interest, interest expense, reduction of carrying amount, and ending carrying amount. (Round interest expense for Year 2 to the nearest dollar; plug Year 3 so ending CA equals face.)  
f. Record the **January 1, Year 2** restructuring entry.  
g. Record the **December 31, Year 2** and **December 31, Year 3** period-end interest payment entries.  
h. Record the **January 1, Year 4** maturity (principal) settlement entry.  
i. Reconcile: total cash paid after restructuring − pre-restructure carrying amount = total interest expense over the remaining term.

**Answer key:**  

**a. Initial recognition**

*January 1, Year 1 — Issue note for merchandise*

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory | 500,000 | |
| Notes Payable | | 500,000 |
| *Record issuance of 12%, 2-year note for merchandise* | | |

**Check:** Dr 500,000 = Cr 500,000. **Balanced.**

**b. Period-end accrual of unpaid interest**

Interest for Year 1 = \( \$500{,}000 \times 12\% = \$60{,}000 \).

*December 31, Year 1 — Accrue interest (not paid)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 60,000 | |
| Interest Payable | | 60,000 |

**Check:** Dr 60,000 = Cr 60,000. **Balanced.**

Carrying amount of debt, January 1, Year 2 = \( \$500{,}000 + \$60{,}000 = \$560{,}000 \).

**c. Restructured cash flows vs carrying amount**

| Component | Amount |
|---|---:|
| Face payable January 1, Year 4 | 500,000 |
| December 31, Year 2 interest (9% × $500,000) | 45,000 |
| December 31, Year 3 interest (9% × $500,000) | 45,000 |
| **Sum of restructured cash flows** | **590,000** |
| Carrying amount of debt, January 1, Year 2 | 560,000 |
| **Excess of restructured CF over carrying amount** | **30,000** |

Because **total future cash payments exceed** the carrying amount of the payable, the debtor **does not** reduce the carrying amount and **does not** recognize a gain at the restructuring date. Accounting is **prospective** using a new effective interest rate.

**d. New effective interest rate**

Solve for \( r \) such that:

\[
\$560{,}000 = \frac{\$45{,}000}{(1+r)} + \frac{\$45{,}000}{(1+r)^{2}} + \frac{\$500{,}000}{(1+r)^{2}}
\]

Excel / RATE inputs: `=RATE(2, −45000, 560000, −500000)`  
**New effective rate \( r \approx 2.7513\% \)** (rounded for schedule construction).

**e. Subsequent measurement schedule (emphasis)**

Total interest expense over remaining term = excess of CF over CA = **$30,000**.

| Date | Cash interest (stated) | Interest expense (eff.) | Reduction of note CA | Note payable, net (CA) |
|---|---:|---:|---:|---:|
| Jan. 1, Year 2 | | | | **560,000** |
| Dec. 31, Year 2 | 45,000 | **15,407** | **29,593** | **530,407** |
| Dec. 31, Year 3 | 45,000 | **14,593** | **30,407** | **500,000** |
| **Totals** | **90,000** | **30,000** | **60,000** | |

Computations:  
- Year 2 interest expense = \( \$560{,}000 \times 2.7513\% \approx \$15{,}407 \) (nearest dollar).  
- Year 2 reduction = \( \$45{,}000 - \$15{,}407 = \$29{,}593 \).  
- CA end Year 2 = \( \$560{,}000 - \$29{,}593 = \$530{,}407 \).  
- Year 3 reduction plugs to face: \( \$530{,}407 - \$500{,}000 = \$30{,}407 \).  
- Year 3 interest expense = \( \$45{,}000 - \$30{,}407 = \$14{,}593 \).  
- **Roll-forward check:** total IE \( \$15{,}407 + \$14{,}593 = \$30{,}000 \) = excess of restructured CF over pre-restructure CA.

**f. Restructuring entry (combine accrued interest into note; no gain)**

*January 1, Year 2 — Troubled debt restructure (payments exceed CA)*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable (old face) | 500,000 | |
| Interest Payable | 60,000 | |
| Notes Payable (restructured carrying amount) | | 560,000 |
| *Combine principal and accrued interest; no gain (CF > CA)* | | |

**Check:** Dr 560,000 = Cr 560,000. **Balanced.**

**g. Period-end interest payments**

*December 31, Year 2 — Interest payment under new effective rate*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 15,407 | |
| Notes Payable | 29,593 | |
| Cash | | 45,000 |

**Check:** Dr 15,407 + 29,593 = Cr 45,000. **Balanced.**

*December 31, Year 3 — Interest payment under new effective rate*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 14,593 | |
| Notes Payable | 30,407 | |
| Cash | | 45,000 |

**Check:** Dr 14,593 + 30,407 = Cr 45,000. **Balanced.**

After the Year 3 entry, Notes Payable CA = **$500,000**.

**h. Maturity settlement**

*January 1, Year 4 — Pay face at maturity*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 500,000 | |
| Cash | | 500,000 |

**Check:** Dr 500,000 = Cr 500,000. **Balanced.**

**i. Reconciliation**

Cash paid after restructuring = \( \$45{,}000 + \$45{,}000 + \$500{,}000 = \$590{,}000 \).  
Pre-restructure CA = **$560,000**.  
Difference = **$30,000** = total interest expense on the schedule. ✓

**Key insight:** When **undiscounted** restructured cash flows **exceed** the debt carrying amount, the debtor keeps the carrying amount, books **no gain**, and builds a **subsequent measurement schedule** using a **new (lower) effective rate**. Each cash “interest” payment is split between **Interest Expense** and a **reduction of the note’s carrying amount** until CA rolls down to face at the final interest date before maturity.

---

### Q2 — CORE number variant — Modification when payments exceed CA (schedule twin)
**LO:** LO 16-12  
**Concept:** Number-variant twin — troubled debt modification with CF > CA; new effective rate; subsequent measurement schedule; period-end JEs; maturity settlement  
**Scenario:**  
**Ironclad Fabricators** (calendar-year debtor) renegotiates a note with **Summitline Credit**.

| Fact | Amount / term |
|---|---|
| Original note issue date | **January 1, Year 1** |
| Face amount | **$750,000** |
| Stated rate (original) | **10%**, interest due each **December 31** |
| Term (original) | **2 years** |
| Issuance proceeds | Cash **$750,000** |
| December 31, Year 1 interest | **Not paid**; accrued **$75,000** |
| Carrying amount, January 1, Year 2 | **$825,000** |
| Restructure date | **January 1, Year 2** |

**Restructured terms:**

| Term | Provision |
|---|---|
| Accrued interest | Forgiven / combined into restructured note |
| Face | Remains **$750,000** |
| New maturity | **January 1, Year 4** |
| New stated rate | **8%**; cash interest **$60,000** each December 31 of Year 2 and Year 3 |
| Principal | **$750,000** on January 1, Year 4 |

**Required:**  
a. Record January 1, Year 1 **initial recognition** and December 31, Year 1 **interest accrual**.  
b. Compare sum of restructured cash flows to carrying amount; conclude on gain vs new effective rate.  
c. Compute the new effective rate (`RATE` inputs).  
d. Prepare the full **amortization schedule** (round Year 2 IE; plug Year 3 to face).  
e. Record restructuring JE, both period-end interest JEs, and maturity JE.  
f. Prove total post-restructure cash − beginning CA = total interest expense.

**Answer key:**  

**a. Initial recognition and accrual**

*January 1, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 750,000 | |
| Notes Payable | | 750,000 |

**Check:** Dr 750,000 = Cr 750,000. **Balanced.**

*December 31, Year 1 — Accrue unpaid interest* (\( \$750{,}000 \times 10\% = \$75{,}000 \))

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 75,000 | |
| Interest Payable | | 75,000 |

**Check:** Dr 75,000 = Cr 75,000. **Balanced.**

**b. CF vs CA**

| Component | Amount |
|---|---:|
| Face, January 1, Year 4 | 750,000 |
| Interest Dec. 31, Y2 (8% × $750,000) | 60,000 |
| Interest Dec. 31, Y3 | 60,000 |
| **Sum of restructured CF** | **870,000** |
| Carrying amount Jan. 1, Y2 | 825,000 |
| **Excess of CF over CA** | **45,000** |

**Conclusion:** CF > CA → **no gain**; compute **new effective rate** and amortize prospectively.

**c. New effective rate**

`=RATE(2, −60000, 825000, −750000)` → \( r \approx \mathbf{2.7898\%} \).

**d. Subsequent measurement schedule**

| Date | Cash interest | Interest expense | Reduction of CA | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Year 2 | | | | **825,000** |
| Dec. 31, Year 2 | 60,000 | **23,016** | **36,984** | **788,016** |
| Dec. 31, Year 3 | 60,000 | **21,984** | **38,016** | **750,000** |
| **Totals** | **120,000** | **45,000** | **75,000** | |

Year 2 IE = \( \$825{,}000 \times 2.7898\% \approx \$23{,}016 \).  
Year 2 red. = \( \$60{,}000 - \$23{,}016 = \$36{,}984 \); CA = \( \$825{,}000 - \$36{,}984 = \$788{,}016 \).  
Year 3 red. = \( \$788{,}016 - \$750{,}000 = \$38{,}016 \); IE = \( \$60{,}000 - \$38{,}016 = \$21{,}984 \).  
Total IE \( \$23{,}016 + \$21{,}984 = \$45{,}000 \) = excess of CF over CA. ✓

**e. Journal entries**

*January 1, Year 2 — Restructure (no gain)*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 750,000 | |
| Interest Payable | 75,000 | |
| Notes Payable | | 825,000 |

**Check:** Dr 825,000 = Cr 825,000. **Balanced.**

*December 31, Year 2*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 23,016 | |
| Notes Payable | 36,984 | |
| Cash | | 60,000 |

**Check:** Dr 60,000 = Cr 60,000. **Balanced.**

*December 31, Year 3*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 21,984 | |
| Notes Payable | 38,016 | |
| Cash | | 60,000 |

**Check:** Dr 60,000 = Cr 60,000. **Balanced.**

*January 1, Year 4 — Maturity*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 750,000 | |
| Cash | | 750,000 |

**Check:** Dr 750,000 = Cr 750,000. **Balanced.**

**f. Reconciliation**

Post-restructure cash = \( \$60{,}000 + \$60{,}000 + \$750{,}000 = \$870{,}000 \).  
\( \$870{,}000 - \$825{,}000 = \$45{,}000 \) = total interest expense. ✓

**Key insight:** Same decision rule as Q1 with all new amounts: when restructured cash flows **exceed** CA, the **schedule** (not a day-one gain) drives subsequent measurement until the note is settled at face.

---

### Q3 — CORE alternate angle — Settlement (assets / equity) and modification when CF < CA
**LO:** LO 16-12  
**Concept:** Debtor accounting for (1) settlement by asset transfer, (2) settlement by equity issuance, and (3) modification when total future cash payments are less than debt carrying amount (immediate gain; zero subsequent effective rate)  
**Scenario:**  
**Palisade Ceramics** owes **Ridgeway Bank** on a note. On **January 1, Year 2**, before any settlement/restructure alternatives below:

| Account | Balance |
|---|---:|
| Notes Payable (face) | **$200,000** |
| Interest Payable (accrued, unpaid) | **$20,000** |
| **Carrying amount of debt** | **$220,000** |

Interest has been fully accrued through December 31, Year 1. Consider **three independent** troubled-debt alternatives on January 1, Year 2.

---

**Alternative A — Settlement by transfer of assets**

Palisade transfers **land** and a **building** to Ridgeway in **full settlement**.

| Asset | Original cost | Accum. depr. (1/1/Y2) | Carrying amount | Fair value (1/1/Y2) |
|---|---:|---:|---:|---:|
| Land | 55,000 | — | 55,000 | **80,000** |
| Building | 210,000 | 70,000 | 140,000 | **110,000** |
| **Total** | | | **195,000** | **190,000** |

**Required A:**  
A1. Record the entry(ies) to adjust assets to fair value (gain/loss on disposal).  
A2. Record the entry to settle the debt through asset transfer.  
A3. Compute total pre-tax income effect (disposal result + restructuring gain).

**Answer key A:**  

Land: FV − CA = \( \$80{,}000 - \$55{,}000 = \$25{,}000 \) **gain**.  
Building: FV − CA = \( \$110{,}000 - \$140{,}000 = \$30{,}000 \) **loss**.  
FV of assets transferred = \( \$80{,}000 + \$110{,}000 = \$190{,}000 \).  
Gain on restructuring = debt CA − FV of assets = \( \$220{,}000 - \$190{,}000 = \$30{,}000 \).

**A1. Adjust assets to fair value**

| Account | Debit | Credit |
|---|---:|---:|
| Land ($80,000 − $55,000) | 25,000 | |
| Loss on Disposal of Building ($140,000 − $110,000) | 30,000 | |
| Building | | 30,000 |
| Gain on Disposal of Land | | 25,000 |
| *Remeasure transferred assets to FV before settlement* | | |

**Check:** Dr 25,000 + 30,000 = Cr 30,000 + 25,000. **Balanced.**

After A1: Land carrying amount = **$80,000**; Building carrying amount = **$110,000** (Building account reduced by the $30,000 write-down so gross Building = $180,000; Accumulated Depreciation remains $70,000).

**A2. Settle debt by transferring land and building**

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 200,000 | |
| Interest Payable | 20,000 | |
| Accumulated Depreciation—Building | 70,000 | |
| Land | | 80,000 |
| Building | | 180,000 |
| Gain on Restructuring of Debt | | 30,000 |
| *Derecognize debt and assets at FV; record restructuring gain* | | |

**Check:** Dr \( 200{,}000 + 20{,}000 + 70{,}000 = 290{,}000 \); Cr \( 80{,}000 + 180{,}000 + 30{,}000 = 290{,}000 \). **Balanced.**

**A3. Total pre-tax income effect**

| Item | Amount |
|---|---:|
| Gain on disposal of land | 25,000 |
| Loss on disposal of building | (30,000) |
| Net loss on asset transfer | (5,000) |
| Gain on restructuring of debt | 30,000 |
| **Net pre-tax income increase** | **25,000** |

(Cross-check: debt CA $220,000 − pre-transfer asset CA $195,000 = **$25,000** net income effect.)

---

**Alternative B — Settlement by transfer of equity interest**

Instead, on January 1, Year 2 Palisade issues **5,000** shares of **$2** par common stock in full settlement. Market price = **$28** per share. The modest increase in shares outstanding is not expected to change the market price.

**Required B:** Record the debtor’s settlement entry and compute the gain.

**Answer key B:**  

Fair value of equity = \( 5{,}000 \times \$28 = \$140{,}000 \).  
Common stock at par = \( 5{,}000 \times \$2 = \$10{,}000 \).  
APIC = \( \$140{,}000 - \$10{,}000 = \$130{,}000 \).  
Gain on restructuring = \( \$220{,}000 - \$140{,}000 = \$80{,}000 \).

*January 1, Year 2 — Settle debt by issuing equity*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 200,000 | |
| Interest Payable | 20,000 | |
| Common Stock | | 10,000 |
| Paid-In Capital in Excess of Par—Common Stock | | 130,000 |
| Gain on Restructuring of Debt | | 80,000 |

**Check:** Dr 220,000 = Cr 10,000 + 130,000 + 80,000. **Balanced.**

---

**Alternative C — Modification of terms when payments are less than carrying amount**

Instead, Ridgeway agrees to modify terms only:

| Term | Provision |
|---|---|
| Face reduced to | **$150,000** |
| Accrued interest | Forgiven |
| New maturity | **December 31, Year 3** (principal due with final year) |
| New stated rate | **4%** on the new face; interest **$6,000** due December 31, Year 2 and December 31, Year 3 |
| Principal | **$150,000** paid December 31, Year 3 (with final interest) |

**Required C:**  
C1. Compute sum of restructured cash flows and the gain on restructuring.  
C2. Record the January 1, Year 2 restructuring entry.  
C3. Record the December 31, Year 2 cash payment and explain interest expense.  
C4. Record the December 31, Year 3 final payment (interest designation + principal).

**Answer key C:**  

**C1. Cash flows and gain**

| Component | Amount |
|---|---:|
| Face payable December 31, Year 3 | 150,000 |
| Dec. 31, Y2 interest (4% × $150,000) | 6,000 |
| Dec. 31, Y3 interest | 6,000 |
| **Sum of restructured cash flows** | **162,000** |
| Carrying amount of debt, Jan. 1, Y2 | 220,000 |
| **Gain on restructuring** | **58,000** |

Because **sum of restructured CF < CA**, reduce the payable to **$162,000** and recognize **$58,000** gain. New effective rate = **0%** (all future cash payments reduce carrying amount).

**C2. Restructuring entry**

*January 1, Year 2 — Restructure (CF < CA)*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable (old) | 200,000 | |
| Interest Payable | 20,000 | |
| Notes Payable (restructured) | | 162,000 |
| Gain on Restructuring of Debt | | 58,000 |

**Check:** Dr 220,000 = Cr 162,000 + 58,000. **Balanced.**

**C3. December 31, Year 2 payment (no interest expense)**

*December 31, Year 2 — Payment under restructured terms (0% effective rate)*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 6,000 | |
| Cash | | 6,000 |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**  
CA after payment = \( \$162{,}000 - \$6{,}000 = \$156{,}000 \).  
**No Interest Expense** — when future undiscounted payments were set equal to the post-restructure carrying amount, the effective rate is zero.

**C4. December 31, Year 3 final settlement**

Interest designation $6,000 + principal $150,000 = **$156,000** cash; CA before payment = **$156,000**.

*December 31, Year 3 — Final payments*

| Account | Debit | Credit |
|---|---:|---:|
| Notes Payable | 156,000 | |
| Cash | | 156,000 |

**Check:** Dr 156,000 = Cr 156,000. **Balanced.**  
(Optional split presentation: Dr Notes Payable 6,000 and Dr Notes Payable 150,000; same net effect.)

**Key insight:** **Settlement** always compares debt CA to the **FV of consideration** (assets or equity) and usually produces a restructuring gain for a troubled debtor. **Modification** forks on the cash-flow test: **CF < CA → day-one gain and 0% subsequent rate**; **CF > CA → no day-one gain and a full effective-interest schedule** (Q1/Q2 emphasis).

---

### Q4 — MC (classification / method choice)
**LO:** LO 16-12  
**Concept:** Debtor decision rule — gain recognition vs new effective rate on troubled debt modification  

**Question 1:**  
On the date of a **troubled debt restructuring** involving **only a modification of terms** (no assets or equity transferred), a debtor should recognize a **gain** equal to the excess of the carrying amount of the payable over the **undiscounted** total future cash payments specified by the new terms when:

- A) The sum of the restructured cash flows **exceeds** the carrying amount of the debt  
- B) The sum of the restructured cash flows is **less than** the carrying amount of the debt  
- C) The present value of the restructured cash flows, discounted at the original effective rate, is less than the carrying amount  
- D) The present value of the restructured cash flows, discounted at the current market rate, is less than the carrying amount  

**Answer:** **B.** For the **debtor**, the cash-flow test uses **undiscounted** total future payments (including amounts designated as interest and principal). If that total is **less than** the carrying amount, reduce the payable to that total and recognize a **gain**. If the total **exceeds** the carrying amount (choice A), recognize **no gain** and compute a **new effective rate**. Choices C and D incorrectly apply a discounted PV test for the debtor’s day-one gain measurement under the modification model in this LO.

---

**Question 2:**  
In a troubled debt **settlement** in which the debtor transfers **noncash assets** to the creditor, the debtor first:

- A) Leaves assets at historical carrying amount and records the entire difference between debt CA and asset CA as a single restructuring gain  
- B) Adjusts the transferred assets to **fair value**, recognizing gain or loss on disposal, then recognizes restructuring gain equal to debt CA − **FV** of assets transferred  
- C) Writes assets up to the carrying amount of the debt and never reports a separate disposal gain or loss  
- D) Measures the settlement solely at the present value of the debt using the creditor’s original effective rate  

**Answer:** **B.** ASC 470-60 / Demo 16-12: difference between **FV and CA of assets transferred** is gain/loss on transfer of assets; difference between **FV of assets** and **CA of the payable** is gain on restructuring of payables.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (CF vs CA tests; rates; schedules roll to face; gains = CA − FV or CA − sum CF)
- [x] Core demo not sidebar-only (Appendix 16A Demo 16-12 primary path: settlement assets/equity + modification CF ≶ CA)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis Q1/Q2), period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Debb/Credex/Atlanta figures)
