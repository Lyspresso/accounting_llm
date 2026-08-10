# Agent 15 — CORE DEMO — LO 16-5

**Chapter:** 16  
**LO title:** Account for bonds issued at a premium  
**Critical gap LO:** yes

## Concept list for this pack
- Initial recognition of bonds sold at a premium (Cash, Premium on Bonds Payable, Bonds Payable)
- Effective-interest amortization schedule (premium reduces carrying amount toward face)
- Semiannual / annual interest payment JEs (Interest Expense + Premium amortization = cash coupon)
- Period-end adjusting entry when interest dates do not fall on year-end
- Derecognition at maturity (final interest + repayment of face)
- Balance sheet presentation of bonds payable, net (face + unamortized premium)
- Straight-line vs effective interest (method choice MC only)
- Number-variant twin with fully recomputed PV and schedule

### Q1 — CORE — Cedarpoint Fabrication: premium bonds, effective interest (full life cycle)
**LO:** LO 16-5  
**Concept:** initial_recognition_JE + subsequent_measurement_schedule + maturity settlement  
**Scenario:** On January 1 of Year 1, Cedarpoint Fabrication Inc. authorizes and issues **$200,000** face of **6%** bonds. The bonds mature in **three years** on December 31 of Year 3 and pay cash interest **semiannually** on June 30 and December 31. The bonds sell to yield a market rate of **5%**. Cedarpoint amortizes the bond premium using the **effective interest method**. Round the issue price and each period’s interest expense to the **nearest dollar**; in the final period, amortize the remaining unamortized premium so that carrying amount equals face.

**Required:**  
(a) Compute the issue price (PV of principal + PV of interest annuity) and prepare the **full effective-interest amortization schedule** over the bond term.  
(b) Record the journal entry for **issuance** on January 1 of Year 1.  
(c) Record the journal entries for interest payment and premium amortization on **June 30 of Year 1** and **December 31 of Year 1**.  
(d) Show the December 31 of Year 1 **balance sheet** presentation of the bonds and Year 1 **interest expense**.  
(e) Record the entries on **December 31 of Year 3** for the final interest payment and **derecognition at maturity**.

**Answer key:**

**Setup (semiannual):**  
- Semiannual market rate: \(5\% \div 2 = 2.5\%\)  
- Semiannual periods: \(3 \times 2 = 6\)  
- Semiannual cash interest: \(6\% \div 2 \times \$200{,}000 = \$6{,}000\)

**Issue price:**  
\[
\begin{align*}
PV_{\text{principal}} &= \$200{,}000 \times (1.025)^{-6} = \$172{,}459 \\
PV_{\text{annuity}} &= \$6{,}000 \times \frac{1 - (1.025)^{-6}}{0.025} = \$33{,}049 \\
\text{Issue price} &= \$205{,}508 \quad (\text{Excel: }=PV(0.025,6,-6000,-200000))
\end{align*}
\]  
Premium = \(\$205{,}508 - \$200{,}000 = \$5{,}508\).

**(a) Effective interest amortization schedule — premium**

| Date | Cash (stated) | Interest expense (2.5% × beg. CA) | Premium amort. | Unamortized premium | Carrying amount |
|---|---:|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 5,508 | 205,508 |
| June 30, Y1 | 6,000 | 5,138 | 862 | 4,646 | 204,646 |
| Dec. 31, Y1 | 6,000 | 5,116 | 884 | 3,762 | 203,762 |
| June 30, Y2 | 6,000 | 5,094 | 906 | 2,856 | 202,856 |
| Dec. 31, Y2 | 6,000 | 5,071 | 929 | 1,927 | 201,927 |
| June 30, Y3 | 6,000 | 5,048 | 952 | 975 | 200,975 |
| Dec. 31, Y3 | 6,000 | 5,025 | 975 | 0 | 200,000 |
| **Totals** | **36,000** | **30,492** | **5,508** | | |

Check: total interest expense \(\$30{,}492\) < total cash interest \(\$36{,}000\) by the premium \(\$5{,}508\).

**(b) Issuance — January 1, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 205,508 | |
| &nbsp;&nbsp;Premium on Bonds Payable | | 5,508 |
| &nbsp;&nbsp;Bonds Payable | | 200,000 |

Dr = Cr = \$205,508.

**(c) Interest and amortization — Year 1**

June 30, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,138 | |
| Premium on Bonds Payable | 862 | |
| &nbsp;&nbsp;Cash | | 6,000 |

Dr = Cr = \$6,000. Carrying amount after entry: \$204,646.

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,116 | |
| Premium on Bonds Payable | 884 | |
| &nbsp;&nbsp;Cash | | 6,000 |

Dr = Cr = \$6,000. Carrying amount after entry: \$203,762.

**(d) Financial statement effects — December 31, Year 1**

Balance sheet (liabilities):

| | |
|---|---:|
| Bonds payable | \$200,000 |
| Plus: Premium on bonds payable | 3,762 |
| **Bonds payable, net** | **\$203,762** |

Income statement (Year 1): Interest expense = \$5,138 + \$5,116 = **\$10,254**.

**(e) Maturity — December 31, Year 3**

Final interest payment:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,025 | |
| Premium on Bonds Payable | 975 | |
| &nbsp;&nbsp;Cash | | 6,000 |

Derecognize bonds at maturity:

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 200,000 | |
| &nbsp;&nbsp;Cash | | 200,000 |

**Key insight:** When stated rate > market rate, bonds issue at a **premium** (adjunct liability). Under the effective interest method, interest expense = beginning carrying amount × market rate; premium amortization = cash coupon − interest expense, so **carrying amount declines to face** and **total interest expense is less than total cash interest**.

---

### Q2 — CORE number variant — Meridian Logistics: premium bonds, annual effective interest
**LO:** LO 16-5  
**Concept:** number_variant_twin (initial recognition + full schedule + first interest)  
**Scenario:** On January 1 of Year 1, Meridian Logistics Corp. issues **$500,000** face of **8%** bonds that mature in **four years** (December 31 of Year 4). Interest is paid **annually** each December 31. The market yield is **6%**. Meridian uses the **effective interest method**. Round the issue price and each period’s interest expense to the nearest dollar; plug the final period so premium amortizes fully.

**Required:**  
(a) Compute the issue price and prepare the **four-year effective-interest amortization schedule**.  
(b) Record the issuance entry on January 1 of Year 1.  
(c) Record the December 31 of Year 1 interest payment and premium amortization.  
(d) State Year 1 interest expense and the December 31 of Year 1 bonds payable, net.  
(e) Record the final interest payment and maturity settlement on December 31 of Year 4.

**Answer key:**

**Setup (annual):** market rate 6%, n = 4, cash interest = \(8\% \times \$500{,}000 = \$40{,}000\).

**Issue price:**  
\[
\begin{align*}
PV_{\text{principal}} &= \$500{,}000 \times (1.06)^{-4} = \$396{,}047 \\
PV_{\text{annuity}} &= \$40{,}000 \times \frac{1 - (1.06)^{-4}}{0.06} = \$138{,}604 \\
\text{Issue price} &= \$534{,}651
\end{align*}
\]  
Premium = \$34,651.

**(a) Schedule**

| Date | Cash | Interest expense (6% × beg. CA) | Premium amort. | Unamortized premium | Carrying amount |
|---|---:|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 34,651 | 534,651 |
| Dec. 31, Y1 | 40,000 | 32,079 | 7,921 | 26,730 | 526,730 |
| Dec. 31, Y2 | 40,000 | 31,604 | 8,396 | 18,334 | 518,334 |
| Dec. 31, Y3 | 40,000 | 31,100 | 8,900 | 9,434 | 509,434 |
| Dec. 31, Y4 | 40,000 | 30,566 | 9,434 | 0 | 500,000 |
| **Totals** | **160,000** | **125,349** | **34,651** | | |

**(b) Issuance — January 1, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 534,651 | |
| &nbsp;&nbsp;Premium on Bonds Payable | | 34,651 |
| &nbsp;&nbsp;Bonds Payable | | 500,000 |

**(c) December 31, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 32,079 | |
| Premium on Bonds Payable | 7,921 | |
| &nbsp;&nbsp;Cash | | 40,000 |

**(d)** Year 1 interest expense = **\$32,079**. Bonds payable, net at Dec. 31, Y1 = \$500,000 + \$26,730 = **\$526,730**.

**(e) December 31, Year 4 — final interest + maturity**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 30,566 | |
| Premium on Bonds Payable | 9,434 | |
| &nbsp;&nbsp;Cash | | 40,000 |

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 500,000 | |
| &nbsp;&nbsp;Cash | | 500,000 |

**Key insight:** Same premium model as Q1 with **all numbers changed** and **annual** (not semiannual) compounding—issue above face, premium amortizes as a reduction of interest expense each period until carrying amount = face at maturity.

---

### Q3 — CORE alternate angle — Alpine Forge: period-end premium accrual (interest dates off year-end)
**LO:** LO 16-5  
**Concept:** period_end_adjusting_JE (accrue interest + amortize premium at year-end)  
**Scenario:** On **January 1 of Year 1**, Alpine Forge Co. issues **$250,000** face of **6%** bonds due in **five years**. Cash interest is paid **semiannually on July 1 and January 1** (not on the December 31 year-end). The bonds sell to yield **4%** market. Alpine uses the **effective interest method** and has a **calendar year-end**. Round issue price and each period’s interest expense to the nearest dollar.

**Required:**  
(a) Compute the issue price and record the January 1 of Year 1 issuance entry.  
(b) Record the **July 1 of Year 1** cash interest payment and premium amortization.  
(c) Record the **December 31 of Year 1 adjusting entry** to accrue interest and amortize premium for the second semiannual period.  
(d) Record the **January 1 of Year 2** cash payment of the interest accrued at year-end.  
(e) Report December 31 of Year 1 bonds payable, net and Year 1 interest expense.

**Answer key:**

**Setup:** semiannual market 2%; n = 10; cash interest = \(3\% \times \$250{,}000 = \$7{,}500\).

Issue price = \(PV(0.02, 10, -7500, -250000) = \$272{,}456\); premium = **\$22,456**.

**(a) Issuance — January 1, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 272,456 | |
| &nbsp;&nbsp;Premium on Bonds Payable | | 22,456 |
| &nbsp;&nbsp;Bonds Payable | | 250,000 |

**(b) July 1, Year 1 — first semiannual period**  
Interest expense = round(\$272,456 × 2%) = **\$5,449**; premium amort. = \$7,500 − \$5,449 = **\$2,051**.

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,449 | |
| Premium on Bonds Payable | 2,051 | |
| &nbsp;&nbsp;Cash | | 7,500 |

Carrying amount after July 1: \$270,405; unamortized premium: \$20,405.

**(c) December 31, Year 1 — adjusting entry (period-end)**  
Interest expense = round(\$270,405 × 2%) = **\$5,408**; premium amort. = \$7,500 − \$5,408 = **\$2,092**.  
No cash is paid on Dec. 31 (next coupon is Jan. 1).

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,408 | |
| Premium on Bonds Payable | 2,092 | |
| &nbsp;&nbsp;Interest Payable | | 7,500 |

**(d) January 1, Year 2 — pay accrued coupon**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Payable | 7,500 | |
| &nbsp;&nbsp;Cash | | 7,500 |

(No additional interest expense or premium amortization on Jan. 1—already recognized at Dec. 31.)

**(e) Presentation**  
- Unamortized premium Dec. 31, Y1: \$22,456 − \$2,051 − \$2,092 = **\$18,313**  
- Bonds payable, net: \$250,000 + \$18,313 = **\$268,313**  
- Year 1 interest expense: \$5,449 + \$5,408 = **\$10,857**

**Key insight:** When coupon dates do not land on the balance-sheet date, the issuer still recognizes **a full interest period’s effective interest expense and premium amortization** at year-end, crediting **Interest Payable** (not Cash) for the contractual coupon; the subsequent cash payment clears the payable only.

---

### Q4 — MC — Classification / presentation of premium bonds
**LO:** LO 16-5  
**Concept:** classification_presentation_or_disclosure  
**Question:** On December 31 of Year 1, Pinecrest Utilities reports bonds payable face \$200,000 with unamortized **Premium on Bonds Payable** of \$3,762 (bonds not maturing within one year). How should Pinecrest present these amounts on the classified balance sheet?

- A) Bonds payable \$200,000 as a long-term liability; Premium on Bonds Payable \$3,762 as a noncurrent asset (adjunct to investments)  
- B) Bonds payable, net \$203,762 as a long-term liability (face \$200,000 plus unamortized premium \$3,762)  
- C) Bonds payable \$203,762 face; no separate premium account is allowed under U.S. GAAP  
- D) Bonds payable \$200,000 long-term; Premium on Bonds Payable \$3,762 as a current liability equal to next year’s amortization  

**Answer:** **B.** Premium on Bonds Payable is an **adjunct liability** added to Bonds Payable; the net carrying amount is reported as a long-term liability when the bonds are not due within one year. Premium is not an asset (A), face is not rewritten to include premium (C), and the entire unamortized premium is not reclassified as current merely because a portion will amortize next period (D).

---

### Q4b — MC — Method / interest effect of a premium (optional second MC)
**LO:** LO 16-5  
**Concept:** subsequent_measurement_schedule (effective interest vs cash coupon)  
**Question:** For bonds issued at a **premium** and amortized under the **effective interest method**, which statement is correct each interest period?

- A) Interest expense equals cash interest paid; premium is ignored until maturity  
- B) Interest expense equals beginning carrying amount × market rate at issuance; premium amortization = cash interest − interest expense  
- C) Interest expense equals beginning carrying amount × stated rate; discount amortization increases interest expense  
- D) Interest expense equals face × market rate; carrying amount increases toward face  

**Answer:** **B.** Effective interest expense uses the **historical market (yield) rate** × **beginning carrying amount**. For a premium bond, cash coupon > interest expense, so the difference **amortizes premium** and **decreases** carrying amount toward face. (A) ignores amortization; (C)/(D) mix discount mechanics or wrong rate bases.

---

### QL — CORE long multi-period — Harbor Ridge Energy: premium bonds through maturity
**LO:** LO 16-5  
**Concept:** disposal_maturity_or_settlement_JE + full effective-interest life cycle  
**Scenario:** On January 1 of Year 1, Harbor Ridge Energy LLC issues **$300,000** of **10%** bonds maturing in **two years** (December 31 of Year 2). Interest is paid **semiannually** on June 30 and December 31. Market yield is **8%**. Harbor Ridge uses the **effective interest method**. Round issue price and period interest expense to the nearest dollar; plug the final period.

**Required:**  
(a) Issue price and full four-period amortization schedule.  
(b) Issuance JE.  
(c) All four interest JEs through maturity.  
(d) Maturity repayment of principal.  
(e) Prove: total interest expense + total premium amortization = total cash coupons; ending unamortized premium = 0.

**Answer key:**

Semiannual market rate 4%; n = 4; cash = \$15,000 per period.  
Issue price = \$310,890; premium = **\$10,890**.

**(a) Schedule**

| Date | Cash | Interest exp. | Prem. amort. | Unamort. prem. | Carrying amount |
|---|---:|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 10,890 | 310,890 |
| June 30, Y1 | 15,000 | 12,436 | 2,564 | 8,326 | 308,326 |
| Dec. 31, Y1 | 15,000 | 12,333 | 2,667 | 5,659 | 305,659 |
| June 30, Y2 | 15,000 | 12,226 | 2,774 | 2,885 | 302,885 |
| Dec. 31, Y2 | 15,000 | 12,115 | 2,885 | 0 | 300,000 |
| **Totals** | **60,000** | **49,110** | **10,890** | | |

**(b) Issuance**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 310,890 | |
| &nbsp;&nbsp;Premium on Bonds Payable | | 10,890 |
| &nbsp;&nbsp;Bonds Payable | | 300,000 |

**(c) Interest entries**

| Date | Dr Interest Expense | Dr Premium on BP | Cr Cash |
|---|---:|---:|---:|
| June 30, Y1 | 12,436 | 2,564 | 15,000 |
| Dec. 31, Y1 | 12,333 | 2,667 | 15,000 |
| June 30, Y2 | 12,226 | 2,774 | 15,000 |
| Dec. 31, Y2 | 12,115 | 2,885 | 15,000 |

Each entry balances at \$15,000.

**(d) Maturity principal repayment — December 31, Year 2**

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 300,000 | |
| &nbsp;&nbsp;Cash | | 300,000 |

**(e) Proof:** Total cash coupons \$60,000 = total interest expense \$49,110 + total premium amortization \$10,890. Ending premium = 0; carrying amount = face.

**Key insight:** Over the full term, the issuer pays **more cash interest than it recognizes as expense**; the “extra” cash is the investors’ recovery of the premium paid at issuance. At maturity only **face** is repaid because the premium has been fully amortized.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV + effective-interest schedules; final period plugs remaining premium)
- [x] Core demo not sidebar-only (Demo 16-5A / 16-5B style primary path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4 and Q4b classification/method only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
