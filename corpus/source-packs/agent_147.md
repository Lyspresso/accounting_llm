# Agent 147 — CORE DEMO — LO 16-6

**Chapter:** 16  
**LO title:** Accounting for Notes Payable (Measure and record notes at issuance and after issuance)  
**Critical gap LO:** yes

## Concept list for this pack
- Measure notes payable at the **present value** of future cash payments using the **market (effective) rate** at inception
- **Zero-interest-bearing** notes: entire discount is interest; amortize with **effective interest** method
- **Interest-bearing** notes issued at a discount when stated rate < market rate
- Full **effective-interest amortization schedule** (subsequent measurement) and period-end interest JEs
- Notes issued for **noncash consideration**: measure at fair value of asset **or** debt, whichever is more clearly evident
- **Maturity / settlement** (derecognition) of notes payable
- **Classification / presentation**: carrying amount net of unamortized discount; current vs noncurrent portion near maturity
- Number-variant twin of the core cash-for-note path

---

### Q1 — CORE — Zero-interest note: issuance, full effective-interest schedule, period-end interest, maturity
**LO:** LO 16-6  
**Concept:** Zero-interest-bearing note payable — initial PV measurement, subsequent effective-interest schedule, year-end adjusting entries, maturity settlement  
**Scenario:**  
On **January 1, Year 1**, HarborPoint Fabrication Co. issues a **4-year, $100,000 face**, **zero-interest-bearing** note payable to Northlake Bank in exchange for cash. The market rate for notes of similar risk is **5%**. HarborPoint’s fiscal year ends **December 31**. No cash interest is paid during the term; the entire face is due at maturity on **December 31, Year 4**. HarborPoint uses the **effective interest method**.

Present value of a single sum of $100,000 due in 4 periods at 5%:  
\[
PV = \$100{,}000 \div (1.05)^4 = \$82{,}270 \text{ (rounded)}
\]

**Required:**  
a. Record the **January 1, Year 1** issuance journal entry.  
b. Prepare the **complete effective-interest amortization schedule** for the life of the note (Date | Cash | Interest expense | Discount amortization | Carrying amount). Round interest expense to the nearest dollar each period; plug the final period so carrying amount equals face.  
c. Record the **December 31, Year 1** and **December 31, Year 2** interest (period-end) journal entries.  
d. Record the **December 31, Year 4** interest entry **and** the maturity (settlement) entry.  
e. What is the **carrying amount** of the note on the **December 31, Year 3** balance sheet (after the Year 3 interest entry)?

**Answer key:**  

**a. January 1, Year 1 — issuance**  
Cash received = **$82,270**; Discount = $100,000 − $82,270 = **$17,730**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 82,270 | |
| Discount on Note Payable | 17,730 | |
| Note Payable | | 100,000 |
| *To record zero-interest note issued for cash at PV using 5% market rate* | | |

**Check:** Dr 82,270 + 17,730 = Cr 100,000. Balanced.

**b. Effective-interest amortization schedule (stated 0%, market 5%)**

| Date | Cash (stated) | Interest expense (CV × 5%) | Discount amort. | Carrying amount (net) |
|---|---:|---:|---:|---:|
| Jan. 1, Year 1 | — | — | — | **82,270** |
| Dec. 31, Year 1 | 0 | 82,270 × 5% = **4,114** | **4,114** | 86,384 |
| Dec. 31, Year 2 | 0 | 86,384 × 5% = **4,319** | **4,319** | 90,703 |
| Dec. 31, Year 3 | 0 | 90,703 × 5% = **4,535** | **4,535** | 95,238 |
| Dec. 31, Year 4 | 0 | **4,762** (plug: 100,000 − 95,238) | **4,762** | **100,000** |
| **Totals** | **0** | **17,730** | **17,730** | |

Verification: 4,114 + 4,319 + 4,535 + 4,762 = **17,730** = initial discount. (Year 4 interest 95,238 × 5% = 4,761.90 → rounds to 4,762 and matches the plug.)

**c. Period-end interest entries (Years 1 and 2)**

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,114 | |
| Discount on Note Payable | | 4,114 |
| *Effective interest on zero-interest note; no cash paid* | | |

**Check:** Dr = Cr = 4,114. Ending CV = 82,270 + 4,114 = **$86,384**.

December 31, Year 2:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,319 | |
| Discount on Note Payable | | 4,319 |

**Check:** Dr = Cr = 4,319. Ending CV = 86,384 + 4,319 = **$90,703**.

**d. December 31, Year 4 — final interest and maturity**

Interest (Year 4):

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,762 | |
| Discount on Note Payable | | 4,762 |

Maturity settlement (derecognition):

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 100,000 | |
| Cash | | 100,000 |
| *Pay face at maturity; discount fully amortized so net CV = face* | | |

**Check:** Each entry balances. After interest, Discount balance = 0; Note Payable is removed at face.

**e. Carrying amount at December 31, Year 3 (after Year 3 interest of $4,535)**  
**$95,238** (Note Payable $100,000 − remaining Discount $4,762).

**Key insight:** A zero-interest note is recorded at PV of the face using the market rate. All interest is noncash amortization of the discount under the effective interest method. At maturity the carrying amount equals face and only face cash is paid.

---

### Q2 — CORE number variant — Interest-bearing note issued at a discount (full schedule + settlement)
**LO:** LO 16-6  
**Concept:** Number-variant twin — interest-bearing note at discount; effective-interest schedule; period-end cash interest and amortization; maturity  
**Scenario:**  
On **January 1, Year 1**, CedarRidge Logistics Inc. issues a **4-year, $250,000 face** note payable to Summit Credit for cash. The note pays **5%** cash interest annually each **December 31** (cash interest = **$12,500** per year). The market rate for similar risk is **8%**. CedarRidge’s year-end is December 31. Principal is due in full at maturity on **December 31, Year 4**.

Issue price (PV of principal + PV of interest annuity at 8%):  
\[
PV = \$12{,}500 \times \frac{1-(1.08)^{-4}}{0.08} + \$250{,}000 \times (1.08)^{-4} = \$225{,}159 \text{ (rounded)}
\]  
Discount = $250,000 − $225,159 = **$24,841**.

**Required:**  
a. Record the **January 1, Year 1** issuance entry.  
b. Prepare the **complete effective-interest amortization schedule** (Cash | Interest expense | Discount amort. | Carrying amount). Round interest expense to nearest dollar; plug final period so CV reaches face.  
c. Record the **December 31, Year 1** interest payment/amortization entry.  
d. Record the **December 31, Year 4** interest entry **and** the maturity entry (principal only may be shown separately after interest).  
e. Compute **total interest expense** over the life of the note and reconcile to cash interest + discount.

**Answer key:**  

**a. January 1, Year 1 — issuance**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 225,159 | |
| Discount on Note Payable | 24,841 | |
| Note Payable | | 250,000 |
| *Interest-bearing note issued below face (stated 5% < market 8%)* | | |

**Check:** Dr 225,159 + 24,841 = Cr 250,000. Balanced.

**b. Effective-interest amortization schedule (stated 5%, market 8%)**

| Date | Cash (5% × face) | Interest expense (CV × 8%) | Discount amort. | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Year 1 | — | — | — | **225,159** |
| Dec. 31, Year 1 | 12,500 | 225,159 × 8% = **18,013** | **5,513** | 230,672 |
| Dec. 31, Year 2 | 12,500 | 230,672 × 8% = **18,454** | **5,954** | 236,626 |
| Dec. 31, Year 3 | 12,500 | 236,626 × 8% = **18,930** | **6,430** | 243,056 |
| Dec. 31, Year 4 | 12,500 | **19,444** (12,500 + 6,944 plug) | **6,944** | **250,000** |
| **Totals** | **50,000** | **74,841** | **24,841** | |

Verification: 5,513 + 5,954 + 6,430 + 6,944 = **24,841**. Year 4: 243,056 × 8% = 19,444.48 → **19,444** matches cash + amort.

**c. December 31, Year 1 — period-end interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 18,013 | |
| Discount on Note Payable | | 5,513 |
| Cash | | 12,500 |
| *Cash interest at stated rate; amortize discount for effective interest* | | |

**Check:** Dr 18,013 = Cr 5,513 + 12,500. Balanced. Ending CV = **$230,672**.

**d. December 31, Year 4 — final interest and maturity**

Interest:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 19,444 | |
| Discount on Note Payable | | 6,944 |
| Cash | | 12,500 |

**Check:** 19,444 = 6,944 + 12,500.

Maturity (principal):

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 250,000 | |
| Cash | | 250,000 |

**Check:** Dr = Cr = 250,000. Discount is fully amortized after the interest entry.

**e. Total interest expense reconciliation**  
Total interest expense = **$74,841**  
= Total cash interest **$50,000** + total discount amortized **$24,841**.

**Key insight:** When the stated rate is below market, cash proceeds are less than face. Effective interest = beginning carrying amount × market rate; cash interest = face × stated rate; the difference amortizes the discount and accretes the carrying amount to face.

---

### Q3 — CORE alternate angle — Note for noncash consideration; schedule; maturity; classification
**LO:** LO 16-6  
**Concept:** Note payable exchanged for equipment (asset FV more clearly evident); effective-interest subsequent measurement; maturity; current vs noncurrent classification  
**Scenario:**  
On **January 1, Year 1**, Meridian Tools LLC purchases specialized equipment by issuing a **3-year, $120,000 face** note. The note requires **6%** cash interest each **December 31** ($7,200 per year); principal is due **December 31, Year 3**. The equipment’s fair value is **clearly evident** and equals **$108,063** (the PV of the note’s cash flows at the **10%** market rate implicit in the exchange). Meridian uses the effective interest method and a December 31 year-end.

**Required:**  
a. Record the **January 1, Year 1** issuance entry (noncash acquisition).  
b. Prepare the **effective-interest amortization schedule** for the 3-year term.  
c. Record interest expense entries for **December 31, Year 1** and **December 31, Year 2**.  
d. Record the **December 31, Year 3** interest entry and the maturity settlement of principal.  
e. **Classification / presentation:** For the **December 31, Year 1** and **December 31, Year 2** balance sheets (after interest entries), state the amount reported as **current** note payable (net) vs **noncurrent** note payable (net). Assume the note is a single principal due at maturity (no installment principal); reclassify the **entire net carrying amount** as current when due within one year.

**Answer key:**  

**a. January 1, Year 1 — issuance for equipment**  
Measure at fair value of equipment (**more clearly evident**): **$108,063**.  
Discount = $120,000 − $108,063 = **$11,937**.

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 108,063 | |
| Discount on Note Payable | 11,937 | |
| Note Payable | | 120,000 |
| *Note issued for equipment measured at asset FV / PV of note at 10%* | | |

**Check:** Dr 108,063 + 11,937 = Cr 120,000. Balanced.

**b. Effective-interest schedule (stated 6%, market 10%)**

| Date | Cash (6% × face) | Interest expense (CV × 10%) | Discount amort. | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Year 1 | — | — | — | **108,063** |
| Dec. 31, Year 1 | 7,200 | 108,063 × 10% = **10,806** | **3,606** | 111,669 |
| Dec. 31, Year 2 | 7,200 | 111,669 × 10% = **11,167** | **3,967** | 115,636 |
| Dec. 31, Year 3 | 7,200 | **11,564** (7,200 + 4,364) | **4,364** | **120,000** |
| **Totals** | **21,600** | **33,537** | **11,937** | |

Verification: 3,606 + 3,967 + 4,364 = **11,937**. Year 3: 115,636 × 10% = 11,563.6 → **11,564**.

**c. Period-end interest**

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,806 | |
| Discount on Note Payable | | 3,606 |
| Cash | | 7,200 |

**Check:** 10,806 = 3,606 + 7,200. CV end Year 1 = **$111,669**.

December 31, Year 2:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 11,167 | |
| Discount on Note Payable | | 3,967 |
| Cash | | 7,200 |

**Check:** 11,167 = 3,967 + 7,200. CV end Year 2 = **$115,636**.

**d. December 31, Year 3 — interest and maturity**

Interest:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 11,564 | |
| Discount on Note Payable | | 4,364 |
| Cash | | 7,200 |

**Check:** 11,564 = 4,364 + 7,200.

Principal settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 120,000 | |
| Cash | | 120,000 |

**Check:** Dr = Cr = 120,000.

**e. Classification / presentation (net of unamortized discount)**

| Balance sheet date | Net carrying amount | Current liabilities | Noncurrent liabilities |
|---|---:|---:|---:|
| Dec. 31, Year 1 | **$111,669** | $0 of principal (due after >1 year) | **$111,669** |
| Dec. 31, Year 2 | **$115,636** | **$115,636** (due within 1 year) | **$0** |

Presentation note: Report **Note Payable** face with **Discount on Note Payable** as a contra liability (or report the single net carrying amount). Do **not** report the note at face without subtracting unamortized discount.

**Key insight:** Noncash notes are measured at the more reliable of asset FV or debt PV. Subsequent measurement still uses the market rate locked in at inception. When principal is due within one year, the **entire net carrying amount** is reclassified as current.

---

### Q4 — MC (classification / measurement method)
**LO:** LO 16-6  
**Concept:** Measurement basis for notes issued for noncash consideration; balance-sheet classification of discounted notes  

**Question 1:**  
On January 1, Year 1, Pine & Oak Co. acquires used machinery by issuing a 2-year, $40,000 note with a **2%** stated rate (interest paid annually). Neither the machinery nor the note has a readily determinable fair value. The prevailing market rate for similar notes is **9%**. How should Pine & Oak **initially measure** the machinery and the note payable?

- A) Face amount of the note, $40,000, because a note was issued  
- B) Present value of the note’s future cash flows discounted at the **2%** stated rate  
- C) Present value of the note’s future cash flows discounted at the **9%** market (imputed) rate  
- D) Undiscounted sum of all future cash payments under the note  

**Answer:** **C.** When the fair value of the asset and the note are not clearly evident, GAAP requires discounting the note’s cash flows at the **prevailing market (imputed) rate** for similar risk—not the stated rate. The difference between face and PV is Discount on Note Payable; the PV is the cost of the machinery.

**Question 2:**  
At December 31, Year 2, Riverbend Inc. has a single **zero-interest-bearing** note payable: face **$50,000**, due December 31, Year 3, unamortized discount **$3,200** (net carrying amount **$46,800**). How should Riverbend **classify** this note on its December 31, Year 2 balance sheet?

- A) Current liability **$50,000**; ignore the discount until maturity  
- B) Noncurrent liability **$46,800**  
- C) Current liability **$46,800** (net of unamortized discount)  
- D) Current liability **$50,000** and a current asset “Discount on Note Payable” **$3,200**  

**Answer:** **C.** Principal is due within one year, so the obligation is **current**. The note is reported at **net carrying amount** ($50,000 − $3,200 unamortized discount = **$46,800**). Discount is a **contra liability**, not an asset, and face is not shown as the liability amount without netting (or without showing face and contra).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified for issuance, interest, and maturity entries)
- [x] Math recomputed (PV, schedule rollforwards, total discount = sum of amortizations)
- [x] Core demo not sidebar-only (Demo 16-6A cash notes; Demo 16-6B noncash; not Expanding Your Knowledge mortgage sidebar)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/measurement items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
