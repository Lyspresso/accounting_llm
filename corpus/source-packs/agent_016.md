# Agent 16 — CORE DEMO — LO 16-6

**Chapter:** 16  
**LO title:** Measure and record notes at issuance and after issuance (Accounting for Notes Payable)  
**Critical gap LO:** yes

## Concept list for this pack
- Initial recognition of a long-term note payable issued for cash at a discount (stated rate ≠ market rate)
- Present-value measurement of notes; Discount on Note Payable contra-liability
- Effective-interest amortization schedule (subsequent measurement)
- Period-end adjusting / interest JEs (cash interest + discount amortization)
- Derecognition (maturity settlement) of note payable
- Note issued for noncash consideration when fair value of asset is not clearly evident (imputed market rate)
- Zero-interest-bearing note (all interest in discount)
- Balance-sheet classification: current vs. noncurrent carrying amount / installment principal
- Number-variant twin of the cash-discount note lifecycle

---

### Q1 — CORE — Interest-bearing note issued for cash at a discount (full lifecycle)
**LO:** LO 16-6  
**Concept:** Initial recognition JE + effective-interest schedule + period-end interest JE + maturity settlement  
**Scenario:** On January 1, Year 1, **Redwood Metalworks Inc.** borrows cash by issuing a **3-year, $80,000** note payable to Northshore Bank. The note pays **5%** cash interest annually each December 31. The market rate for notes of similar risk is **9%**. Redwood’s fiscal year ends December 31. Redwood uses the **effective interest method**.

**Required:**  
(a) Compute the cash proceeds (issue price) of the note on January 1, Year 1. Round the present value to the nearest cent.  
(b) Record the **initial recognition** journal entry on January 1, Year 1.  
(c) Prepare the complete **effective-interest amortization schedule** over the 3-year term (show cash interest, interest expense, discount amortization, and carrying amount). Plug any final-period rounding difference so the carrying amount equals face at maturity.  
(d) Record the **December 31, Year 1** interest entry (period-end).  
(e) Record the **December 31, Year 3** interest entry and the **maturity settlement** entry (principal only may be shown separately from interest).  

**Answer key:**  

**(a) Issue price (PV of cash flows at 9%)**  
Annual cash interest = \(80{,}000 \times 5\% = \$4{,}000\).

\[
\begin{align*}
PV &= 4{,}000 \times PVA_{9\%,3} + 80{,}000 \times PVF_{9\%,3} \\
PVA_{9\%,3} &= \frac{1-(1.09)^{-3}}{0.09} \approx 2.531294666\\
PVF_{9\%,3} &= (1.09)^{-3} \approx 0.772183480\\
PV_{\text{raw}} &= 4{,}000(2.531294666) + 80{,}000(0.772183480) \approx 71{,}899.857
\end{align*}
\]

\(PV = \mathbf{\$71{,}899.86}\) (ROUND_HALF_UP to cent).  
**Discount on Note Payable** = \(80{,}000 - 71{,}899.86 = \mathbf{\$8{,}100.14}\).

**(b) January 1, Year 1 — Initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 71,899.86 | |
| Discount on Note Payable | 8,100.14 | |
| Note Payable | | 80,000.00 |

*Check:* Dr \(71{,}899.86 + 8{,}100.14 = 80{,}000.00\) = Cr. Carrying amount = \(80{,}000 - 8{,}100.14 = \$71{,}899.86\).

**(c) Effective-interest amortization schedule (market 9%)**

| Date | Cash (5%) | Interest expense (9% × CA) | Discount amort. | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 71,899.86 |
| Dec. 31, Y1 | 4,000.00 | 6,470.99 | 2,470.99 | 74,370.85 |
| Dec. 31, Y2 | 4,000.00 | 6,693.38 | 2,693.38 | 77,064.23 |
| Dec. 31, Y3 | 4,000.00 | 6,935.77* | 2,935.77* | 80,000.00 |
| **Totals** | **12,000.00** | **20,100.14** | **8,100.14** | |

\*Year 3: discount amort. plugged = \(80{,}000.00 - 77{,}064.23 = 2{,}935.77\); interest expense = cash + amort. = \(4{,}000 + 2{,}935.77 = 6{,}935.77\).  
*Roll-forward checks:* \(71{,}899.86 + 2{,}470.99 = 74{,}370.85\); \(74{,}370.85 + 2{,}693.38 = 77{,}064.23\); \(77{,}064.23 + 2{,}935.77 = 80{,}000.00\).  
Interest expense total \(20{,}100.14 = \) cash interest \(12{,}000 + \) discount \(8{,}100.14\).

**(d) December 31, Year 1 — Period-end interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,470.99 | |
| Discount on Note Payable | | 2,470.99 |
| Cash | | 4,000.00 |

*Check:* \(6{,}470.99 = 2{,}470.99 + 4{,}000.00\).

**(e) December 31, Year 3 — Final interest + maturity**

Interest:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,935.77 | |
| Discount on Note Payable | | 2,935.77 |
| Cash | | 4,000.00 |

Maturity settlement (principal):

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 80,000.00 | |
| Cash | | 80,000.00 |

(After Year 3 amortization, Discount on Note Payable is fully amortized to zero; net liability = face.)

**Key insight:** When the stated rate is below the market rate, cash proceeds are less than face—the **discount is interest cost recognized over the term** via effective interest (not cash coupons alone). Initial measurement is always **PV of future cash flows at the market rate at inception**.

---

### Q2 — CORE number variant — Interest-bearing cash note at a discount (all numbers changed)
**LO:** LO 16-6  
**Concept:** Number-variant twin — initial recognition, effective-interest schedule, period-end JE, maturity  
**Scenario:** On January 1, Year 1, **Solstice Components Corp.** issues a **4-year, $150,000** note payable to Westfield Credit Union for cash. Stated cash interest is **6%** payable each December 31. The market rate for similar risk is **10%**. Fiscal year-end is December 31. Effective interest method.

**Required:**  
(a) Compute issue price (nearest cent) and discount.  
(b) Record issuance on January 1, Year 1.  
(c) Prepare the full effective-interest amortization schedule (plug final period).  
(d) Record December 31, Year 1 interest.  
(e) Record December 31, Year 4 interest and principal maturity settlement.

**Answer key:**  

**(a)** Cash interest \(= 150{,}000 \times 6\% = \$9{,}000\).

\[
\begin{align*}
PVA_{10\%,4} &= \frac{1-(1.10)^{-4}}{0.10} = 3.169865446\\
PVF_{10\%,4} &= (1.10)^{-4} = 0.683013455\\
PV &= 9{,}000(3.169865446) + 150{,}000(0.683013455) = \mathbf{\$130{,}980.81}
\end{align*}
\]

Discount \(= 150{,}000 - 130{,}980.81 = \mathbf{\$19{,}019.19}\).

**(b) January 1, Year 1 — Issuance**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 130,980.81 | |
| Discount on Note Payable | 19,019.19 | |
| Note Payable | | 150,000.00 |

*Check:* \(130{,}980.81 + 19{,}019.19 = 150{,}000.00\).

**(c) Amortization schedule (market 10%)**

| Date | Cash (6%) | Interest expense (10% × CA) | Discount amort. | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 130,980.81 |
| Dec. 31, Y1 | 9,000.00 | 13,098.08 | 4,098.08 | 135,078.89 |
| Dec. 31, Y2 | 9,000.00 | 13,507.89 | 4,507.89 | 139,586.78 |
| Dec. 31, Y3 | 9,000.00 | 13,958.68 | 4,958.68 | 144,545.46 |
| Dec. 31, Y4 | 9,000.00 | 14,454.54* | 5,454.54* | 150,000.00 |
| **Totals** | **36,000.00** | **55,019.19** | **19,019.19** | |

\*Y4 plug: amort. \(= 150{,}000 - 144{,}545.46 = 5{,}454.54\); IE \(= 9{,}000 + 5{,}454.54 = 14{,}454.54\).  
Totals: IE \(55{,}019.19 = 36{,}000\) cash \(+ 19{,}019.19\) discount.

**(d) December 31, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 13,098.08 | |
| Discount on Note Payable | | 4,098.08 |
| Cash | | 9,000.00 |

*Check:* \(13{,}098.08 = 4{,}098.08 + 9{,}000.00\).

**(e) December 31, Year 4 — Interest + maturity**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 14,454.54 | |
| Discount on Note Payable | | 5,454.54 |
| Cash | | 9,000.00 |

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 150,000.00 | |
| Cash | | 150,000.00 |

**Key insight:** Same measurement model as Q1 with different face, term, stated rate, and market rate—**issue price is always PV at market; carrying amount walks to face** as the discount amortizes.

---

### Q3 — CORE alternate angle — Note for noncash consideration (imputed rate) + zero-interest contrast + classification
**LO:** LO 16-6  
**Concept:** Noncash initial measurement (imputed market rate); zero-interest note; BS current/noncurrent classification of installment note  
**Scenario — Part A (noncash, fair values not clearly evident):** On January 1, Year 1, **Fairview Industrial LLC** acquires specialized production equipment by issuing a **3-year, $90,000** note payable. The note requires **4%** cash interest each December 31; principal is due December 31, Year 3. Neither the equipment’s cash selling price nor the note’s fair value is clearly evident. The prevailing market rate on similar notes is **7%**. Effective interest method.

**Scenario — Part B (zero-interest noncash):** Same date, **Pinecroft Logistics Co.** acquires a used forklift (no reliable cash price) by issuing a **2-year, $25,000 zero-interest-bearing** note due in full at maturity. Market rate for similar risk is **11%**.

**Scenario — Part C (classification):** On January 1, Year 1, **Riverbend Outfitters Inc.** purchases equipment with a cash price of **$60,000** in exchange for a **4-year installment note**. Equal annual payments are due each December 31; the market rate implicit in the arrangement is **8%**. After recording the December 31, Year 1 installment payment, show the **December 31, Year 1** balance-sheet classification of the note (current vs. noncurrent).

**Required:**  
(A1) Compute PV of Fairview’s note and record issuance.  
(A2) Prepare Fairview’s full amortization schedule and the Dec. 31, Year 1 interest entry.  
(A3) Record Fairview’s maturity settlement of principal on Dec. 31, Year 3 (ignore that day’s interest in this single entry).  
(B1) Record Pinecroft’s issuance of the zero-interest note.  
(B2) Record Pinecroft’s Dec. 31, Year 1 interest (discount amortization only).  
(C1) Compute the annual installment payment (nearest cent).  
(C2) Prepare the installment amortization schedule.  
(C3) Present current and noncurrent note payable on the Dec. 31, Year 1 balance sheet (after the Year 1 payment).

**Answer key:**  

**(A1) Fairview — PV and issuance**  
Cash interest \(= 90{,}000 \times 4\% = \$3{,}600\).

\[
\begin{align*}
PVA_{7\%,3} &= \frac{1-(1.07)^{-3}}{0.07} = 2.624316036\\
PVF_{7\%,3} &= (1.07)^{-3} = 0.816297877\\
PV &= 3{,}600(2.624316036) + 90{,}000(0.816297877) = \mathbf{\$82{,}914.35}
\end{align*}
\]

Discount \(= 90{,}000 - 82{,}914.35 = \mathbf{\$7{,}085.65}\).

January 1, Year 1 — Issuance (measure at PV of note / imputed cost of equipment):

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 82,914.35 | |
| Discount on Note Payable | 7,085.65 | |
| Note Payable | | 90,000.00 |

*Check:* \(82{,}914.35 + 7{,}085.65 = 90{,}000.00\).

**(A2) Fairview schedule & Year 1 interest**

| Date | Cash (4%) | Interest expense (7% × CA) | Discount amort. | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 82,914.35 |
| Dec. 31, Y1 | 3,600.00 | 5,804.00 | 2,204.00 | 85,118.35 |
| Dec. 31, Y2 | 3,600.00 | 5,958.28 | 2,358.28 | 87,476.63 |
| Dec. 31, Y3 | 3,600.00 | 6,123.37* | 2,523.37* | 90,000.00 |
| **Totals** | **10,800.00** | **17,885.65** | **7,085.65** | |

\*Y3 plug: amort. \(= 90{,}000 - 87{,}476.63 = 2{,}523.37\); IE \(= 3{,}600 + 2{,}523.37 = 6{,}123.37\).

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,804.00 | |
| Discount on Note Payable | | 2,204.00 |
| Cash | | 3,600.00 |

*Check:* \(5{,}804 = 2{,}204 + 3{,}600\).

**(A3) Fairview maturity (principal)**

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 90,000.00 | |
| Cash | | 90,000.00 |

**(B1) Pinecroft zero-interest issuance**  
\(PV = 25{,}000 / (1.11)^2 = 25{,}000 / 1.2321 = \mathbf{\$20{,}290.56}\).  
Discount \(= 25{,}000 - 20{,}290.56 = \mathbf{\$4{,}709.44}\).

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 20,290.56 | |
| Discount on Note Payable | 4,709.44 | |
| Note Payable | | 25,000.00 |

*Check:* \(20{,}290.56 + 4{,}709.44 = 25{,}000.00\).

**(B2) Pinecroft Dec. 31, Year 1 interest**  
IE \(= 20{,}290.56 \times 11\% = \mathbf{\$2{,}231.96}\).

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 2,231.96 | |
| Discount on Note Payable | | 2,231.96 |

Carrying amount end of Y1 \(= 20{,}290.56 + 2{,}231.96 = \$22{,}522.52\).  
(Y2 plug: amort./IE \(= 25{,}000 - 22{,}522.52 = \$2{,}477.48\).)

**(C1) Riverbend installment payment**  
\(PVA_{8\%,4} = \dfrac{1-(1.08)^{-4}}{0.08} = 3.312126964\).

\[
PMT = \frac{60{,}000}{3.312126964} = \mathbf{\$18{,}115.25}
\]

**(C2) Installment amortization schedule**

| Date | Cash payment | Interest expense (8% × CA) | Principal reduction | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 60,000.00 |
| Dec. 31, Y1 | 18,115.25 | 4,800.00 | 13,315.25 | 46,684.75 |
| Dec. 31, Y2 | 18,115.25 | 3,734.78 | 14,380.47 | 32,304.28 |
| Dec. 31, Y3 | 18,115.25 | 2,584.34 | 15,530.91 | 16,773.37 |
| Dec. 31, Y4 | 18,115.25 | 1,341.88* | 16,773.37* | 0.00 |
| **Totals** | **72,461.00** | **12,461.00** | **60,000.00** | |

\*Y4 plug: principal = remaining CA \(16{,}773.37\); interest \(= 18{,}115.25 - 16{,}773.37 = 1{,}341.88\).  
Issuance JE (for completeness): Dr Equipment 60,000 / Cr Note Payable 60,000.  
Y1 payment JE: Dr Interest Expense 4,800; Dr Note Payable 13,315.25; Cr Cash 18,115.25. *(Balances: \(4{,}800 + 13{,}315.25 = 18{,}115.25\).)*

**(C3) Balance sheet — December 31, Year 1 (after payment)**  
Carrying amount \(= \$46{,}684.75\).  
**Current portion** = next year’s principal reduction \(= \$14{,}380.47\).  
**Long-term portion** \(= 46{,}684.75 - 14{,}380.47 = \$32{,}304.28\).

| Classification | Amount |
|---|---:|
| Current liabilities — Note payable (current portion) | 14,380.47 |
| Long-term liabilities — Note payable | 32,304.28 |
| **Total note payable** | **46,684.75** |

**Key insight:** For noncash notes, capitalize the asset at the **more clearly evident fair value**—often the **PV of the note at the market (imputed) rate** when the asset’s cash price is unknown. Zero-interest notes still have interest (entirely via discount). Installment notes reclassify the **next principal reduction** as current.

---

### Q4 — MC — Classification / measurement basis for notes payable
**LO:** LO 16-6  
**Concept:** Classification presentation and measurement basis (current vs. LT; PV at market)  

**Question 4.1:** On December 31, Year 2, Oakdale Co. has a single balloon note payable: face **$100,000**, remaining unamortized discount **$4,200**, **entire principal due December 31, Year 3** (within one year). How should Oakdale present this note on the December 31, Year 2 balance sheet?

- A) Current liability \(100{,}000\); no discount shown  
- B) Current liability \(95{,}800\) (net of discount)  
- C) Long-term liability \(95{,}800\) (net of discount)  
- D) Long-term liability \(100{,}000\); discount \(4{,}200\) as deferred charge asset  

**Answer:** **B.** Principal is due within one year, so the **net carrying amount** \(100{,}000 - 4{,}200 = 95{,}800\) is classified as a **current** liability. Discount is a contra-liability (not an asset) and reduces the amount reported; it is not left entirely long-term once maturity is within the current operating cycle/year.

**Question 4.2:** When a company issues a long-term note payable for specialized equipment and **neither** the equipment’s cash price nor the note’s fair value is clearly evident, the note (and equipment) should initially be measured at:

- A) Face value of the note, with no discount or premium  
- B) Face value less total stated cash interest over the term  
- C) Present value of the note’s future cash payments discounted at the **prevailing market rate** for similar notes (imputed rate)  
- D) Undiscounted sum of all future principal and interest payments  

**Answer:** **C.** ASC 835-30 / textbook LO 16-6: measure at the **present value of cash flows using the market (imputed) rate** when fair value of the asset/debt is not clearly evident and the stated rate is not a fair market rate. That PV becomes both the equipment cost and the initial net note liability.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV factors and effective-interest roll-forwards; final-period plugs documented)
- [x] Core demo not sidebar-only (Demo 16-6A cash notes + Demo 16-6B noncash/installment; mortgage sidebar excluded)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/measurement items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original companies/numbers (not textbook Frazier $1,000 demos)
