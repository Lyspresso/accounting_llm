# Agent 47 — CORE DEMO — LO 8-9

**Chapter:** 8  
**LO title:** Account for impairment of noncurrent receivables  
**Critical gap LO:** no  
**Emphasis:** initial_recognition_JE

## Concept list for this pack
- **Initial recognition** of note receivable impairment under the **discounted cash flow (DCF)** method (ASC 326): PV of expected future cash flows discounted at the note’s **original effective interest rate**
- Allowance measurement: amortized cost basis − PV of expected cash flows; **Bad Debt Expense** and **Allowance for Doubtful Accounts**
- Write-off / noncollection of **interest receivable** that is not expected when impairment is recognized
- **Subsequent measurement schedule** using the **effective interest method** after impairment (interest revenue = net carrying amount × original effective rate; typically Dr AFDA / Cr Interest Revenue when cash interest is not expected)
- **Period-end adjusting** interest accruals after impairment
- **Settlement / maturity** derecognition when cash (or assets) is finally received; shortfall loss
- **Restructuring**: settlement by asset transfer vs **modification of terms** treated as continuation of the existing loan (PV of restructured cash flows at original rate)
- Balance-sheet **presentation**: note receivable gross less allowance (net amortized cost)
- Do **not** use the current market rate for similar-risk notes when measuring DCF impairment

---

### Q1 — CORE — Note receivable impairment life cycle (initial recognition emphasis)
**LO:** LO 8-9  
**Concept:** DCF impairment of a noncurrent note — initial recognition JE, subsequent effective-interest schedule, period-end interest AJEs, settlement at maturity, BS presentation  
**Scenario:**  
**Aspen Ridge Supply Co.** (calendar-year creditor) sold merchandise to **Teton Outfitters** on **January 1, Year 1**, and received a **$60,000**, **7%**, **four-year** note. The note’s market rate at issuance equaled the stated rate of **7%**. Annual interest is due each **December 31**; principal is due **December 31 of Year 4**.

Facts:
1. On December 31 of Year 1, Aspen collected the contractual Year 1 interest of **$4,200** on schedule.
2. Immediately after that collection, Aspen reviewed the note because of Teton’s financial distress. Aspen expects **no further interest collections** and expects to collect only **$40,000** of principal on **December 31 of Year 4**.
3. The current market rate for notes of similar risk is **12%** (do **not** use this rate for impairment measurement).
4. Aspen measures expected credit losses with the **discounted cash flow method** and, after impairment, recognizes interest revenue with the **effective interest method**.
5. On December 31 of Year 4, Aspen receives **$38,500** cash in full settlement and expects nothing further.

**Required:**  
(a) Journal entry to record receipt of the note on January 1 of Year 1 (ignore cost of goods sold).  
(b) Journal entry to record collection of Year 1 interest on December 31 of Year 1.  
(c) Compute the present value of expected cash flows at the impairment date, the allowance, and bad debt expense. Prepare the **December 31, Year 1 impairment journal entry** (initial recognition).  
(d) Show the **December 31, Year 1** balance-sheet presentation of the note.  
(e) Prepare the **subsequent measurement schedule** of net carrying amount and interest revenue for Years 2–4.  
(f) Prepare period-end adjusting entries for interest revenue on December 31 of Year 2 and Year 3.  
(g) Prepare the combined December 31 of Year 4 entry for final-year interest revenue and cash settlement.

**Answer key:**

**(a) January 1, Year 1 — receipt of note**  
```
Dr Note Receivable .............................. 60,000
   Cr Sales Revenue ...................................... 60,000
```
(Dr = Cr = 60,000)

**(b) December 31, Year 1 — collect contractual interest**  
Interest = \(60{,}000 \times 0.07 = \$4{,}200\).  
```
Dr Cash .......................................... 4,200
   Cr Interest Revenue ..................................... 4,200
```
(Dr = Cr = 4,200)

**(c) December 31, Year 1 — impairment (DCF at original 7% rate)**  
Expected cash flow: **$40,000** in **3** years; no further interest.  
\[
PV = \frac{40{,}000}{(1.07)^3} = \$32{,}651.92
\]
Excel: `=PV(0.07,3,0,-40000)` → **$32,651.92**.

| Item | Amount |
|---|---:|
| Amortized cost basis (face) | $60,000.00 |
| PV of expected cash flows @ **7%** (original effective rate) | 32,651.92 |
| **Allowance for Doubtful Accounts** | **27,348.08** |
| **Bad Debt Expense** | **27,348.08** |

**Do not** discount at the 12% current market rate.

```
Dr Bad Debt Expense ......................... 27,348.08
   Cr Allowance for Doubtful Accounts .............. 27,348.08
```
(Dr = Cr = 27,348.08)

**(d) Balance sheet presentation — December 31, Year 1**  
```
Note receivable .............................. $60,000.00
Less: Allowance for doubtful accounts ........ (27,348.08)
Note receivable, net ......................... $32,651.92
```
Net amount equals the PV of expected cash flows.

**(e) Subsequent measurement schedule** (effective interest at **7%** on net carrying amount)

| Date | Interest revenue (7% × beg. net) | Increase in net / reduction of AFDA | Net carrying amount |
|---|---:|---:|---:|
| Dec 31, Y1 (after impairment) | — | — | 32,651.92 |
| Dec 31, Y2 | 2,285.63 | 2,285.63 | 34,937.55 |
| Dec 31, Y3 | 2,445.63 | 2,445.63 | 37,383.18 |
| Dec 31, Y4 | 2,616.82 | 2,616.82 | 40,000.00 |
| **Totals** | **7,348.08** | **7,348.08** | |

Checks: \(32{,}651.92 \times 0.07 = 2{,}285.63\); \(34{,}937.55 \times 0.07 = 2{,}445.63\); \(37{,}383.18 \times 0.07 = 2{,}616.82\). Terminal net equals expected principal **$40,000**.

AFDA roll-forward (for settlement):  
\(27{,}348.08 - 2{,}285.63 - 2{,}445.63 = \$22{,}616.82\) remaining **before** the Year 4 interest recognition embedded in the settlement entry.

**(f) Period-end interest AJEs (no cash interest expected)**  
December 31, Year 2:  
```
Dr Allowance for Doubtful Accounts ........... 2,285.63
   Cr Interest Revenue ................................. 2,285.63
```
(Dr = Cr = 2,285.63)

December 31, Year 3:  
```
Dr Allowance for Doubtful Accounts ........... 2,445.63
   Cr Interest Revenue ................................. 2,445.63
```
(Dr = Cr = 2,445.63)

**(g) December 31, Year 4 — final interest + settlement**  
Cash received **$38,500**; expected net before shortfall **$40,000** → **settlement loss $1,500**.  
```
Dr Cash ......................................... 38,500.00
Dr Allowance for Doubtful Accounts .............. 22,616.82
Dr Loss on Settlement of Note Receivable ......... 1,500.00
   Cr Note Receivable .................................. 60,000.00
   Cr Interest Revenue .................................. 2,616.82
```
(Dr \(38{,}500.00 + 22{,}616.82 + 1{,}500.00 = 62{,}616.82\) = Cr \(60{,}000.00 + 2{,}616.82\))

**Key insight:** Impairment uses **expected cash flows discounted at the original effective rate**, not the current market rate. The allowance reduces the note to that PV; later effective interest **accretes** the net carrying amount toward the expected collection amount, usually by reducing AFDA and recognizing interest revenue.

---

### Q2 — CORE number variant — Impairment twin (all numbers changed)
**LO:** LO 8-9  
**Concept:** DCF impairment initial recognition, multi-year effective-interest schedule, period-end AJEs, maturity settlement (number-variant twin)  
**Scenario:**  
**Boreal Credit Partners** (calendar-year) holds a note from **Summit Glass LLC** received January 1 of Year 1 for a merchandise sale:

1. Face **$90,000**; stated and market rate **8%**; term **five years**; annual interest each December 31; principal due December 31 of Year 5.  
2. December 31 of Year 1: Boreal **collected** Year 1 interest of **$7,200**.  
3. Same day, after collection, Boreal concludes it will receive **no further interest** and only **$55,000** of principal on December 31 of Year 5.  
4. Current market rate for similar-risk notes is **15%** (ignore for measurement).  
5. DCF method; effective interest after impairment.  
6. December 31 of Year 5: Boreal collects **$55,000** cash as expected (full expected recovery; no additional loss).

**Required:**  
(a) Compute PV of expected cash flows, allowance, and bad debt expense at December 31 of Year 1; record the **impairment JE**.  
(b) Prepare the **net carrying amount / interest revenue schedule** for Years 2–5 (round intermediate interest to the nearest cent; plug the final-year interest by **$0.01** if needed so terminal net equals **$55,000**).  
(c) Prepare interest AJEs for December 31 of Year 2, Year 3, and Year 4.  
(d) Prepare the December 31 of Year 5 combined interest and settlement entry.  
(e) State the net note receivable that would appear on the December 31 of Year 1 balance sheet.

**Answer key:**

**(a) Impairment — December 31, Year 1**  
Expected CF: **$55,000** in **4** years.  
\[
PV = \frac{55{,}000}{(1.08)^4} = \$40{,}426.64
\]
Excel: `=PV(0.08,4,0,-55000)` → **$40,426.64**.

| Item | Amount |
|---|---:|
| Face / amortized cost | $90,000.00 |
| PV @ **8%** original effective rate | 40,426.64 |
| **AFDA / Bad Debt Expense** | **49,573.36** |

```
Dr Bad Debt Expense ......................... 49,573.36
   Cr Allowance for Doubtful Accounts .............. 49,573.36
```
(Dr = Cr = 49,573.36)

**(b) Subsequent measurement schedule**

| Date | Interest revenue (8%) | Net carrying amount |
|---|---:|---:|
| Dec 31, Y1 (post-impairment) | — | 40,426.64 |
| Dec 31, Y2 | 3,234.13 | 43,660.77 |
| Dec 31, Y3 | 3,492.86 | 47,153.63 |
| Dec 31, Y4 | 3,772.29 | 50,925.92 |
| Dec 31, Y5 | **4,074.08**† | **55,000.00** |
| **Totals** | **14,573.36** | |

†Computed \(50{,}925.92 \times 0.08 = 4{,}074.07\); **+$0.01** plug so net equals expected principal $55,000 (standard cent-rounding).

AFDA before Year 5 entry:  
\(49{,}573.36 - 3{,}234.13 - 3{,}492.86 - 3{,}772.29 = \$39{,}074.08\).

**(c) Interest AJEs**  
December 31, Year 2:  
```
Dr Allowance for Doubtful Accounts ........... 3,234.13
   Cr Interest Revenue ................................. 3,234.13
```
December 31, Year 3:  
```
Dr Allowance for Doubtful Accounts ........... 3,492.86
   Cr Interest Revenue ................................. 3,492.86
```
December 31, Year 4:  
```
Dr Allowance for Doubtful Accounts ........... 3,772.29
   Cr Interest Revenue ................................. 3,772.29
```
(Each entry balances.)

**(d) December 31, Year 5 — settlement at expected amount**  
```
Dr Cash ......................................... 55,000.00
Dr Allowance for Doubtful Accounts .............. 39,074.08
   Cr Note Receivable .................................. 90,000.00
   Cr Interest Revenue .................................. 4,074.08
```
(Dr \(55{,}000.00 + 39{,}074.08 = 94{,}074.08\) = Cr \(90{,}000.00 + 4{,}074.08\))

**(e) BS net, December 31, Year 1**  
Note receivable **$90,000** − AFDA **$49,573.36** = **$40,426.64** (equals PV of expected cash flows).

**Key insight:** Changing face, rate, term, and expected recovery changes every dollar, but the **measurement model is identical**: original effective rate → PV → AFDA; then effective interest accretes the net toward the expected collection.

---

### Q3 — CORE alternate angle — Settlement by assets and modification of terms
**LO:** LO 8-9  
**Concept:** Creditor settlement of an impaired noncurrent receivable (asset transfer) and restructuring treated as continuation of the existing loan (DCF impairment + subsequent interest + maturity)  
**Scenario:**  
**Pinecrest Regional Bank** (calendar-year creditor) has two separate troubled-debt situations in Year 2.

---

**Part A — Settlement through transfer of assets**  
**Redwood Construction** owes Pinecrest a **$175,000**, **8%** note. Interest for the past year of **$14,000** was accrued by Pinecrest but was **not** paid. On **January 1, Year 2**, Redwood settles the note and accrued interest in full by transferring:

| Asset transferred | Fair value to creditor |
|---|---:|
| Land | $60,000 |
| Building | 85,000 |
| Cash | 5,000 |

Pinecrest intends to hold/use the real estate (record at fair value). Any shortfall is a **loss on settlement** (alternatively, Bad Debt Expense or a charge against an existing allowance—use Loss on Settlement here).

**Required (Part A):**  
Prepare Pinecrest’s January 1, Year 2 journal entry to record the settlement.

**Answer key (Part A):**  
Carrying amount settled = \(175{,}000 + 14{,}000 = \$189{,}000\).  
Assets received = \(60{,}000 + 85{,}000 + 5{,}000 = \$150{,}000\).  
**Loss** = \(189{,}000 - 150{,}000 = \$39{,}000\).

```
Dr Land ......................................... 60,000
Dr Building ..................................... 85,000
Dr Cash .......................................... 5,000
Dr Loss on Settlement of Receivable ............. 39,000
   Cr Note Receivable ................................. 175,000
   Cr Interest Receivable .............................. 14,000
```
(Dr \(60{,}000 + 85{,}000 + 5{,}000 + 39{,}000 = 189{,}000\) = Cr \(175{,}000 + 14{,}000\))

---

**Part B — Modification of terms (continuation of existing loan)**  
Separately, **Oakmont Builders** issued to Pinecrest on January 1 of Year 1 a **$120,000**, **10%**, multi-year note with interest due each December 31. Oakmont failed to pay the December 31 of Year 1 interest; Pinecrest had accrued **Interest Receivable $12,000**.

On **January 1 of Year 2**, the parties restructure (terms are **not** comparable to a new market loan to a similar customer → treat as **continuation of the existing loan**):

| Restructured term | Amount / feature |
|---|---|
| Accrued Year 1 interest | **Forgiven** |
| New face (maturity amount) | **$95,000** due December 31 of Year 3 |
| New contractual rate | **4%** → cash interest **$3,800** due Dec 31 Y2 and Dec 31 Y3 |
| Original effective rate for DCF | **10%** (unchanged) |

Pinecrest uses the DCF method and the effective interest method after the restructure.

**Required (Part B):**  
(a) Compute the PV of expected restructured cash flows at the **original 10%** rate and the impairment loss.  
(b) Record the January 1, Year 2 impairment / restructure entries (capitalize forgiven interest into the note investment; establish AFDA).  
(c) Prepare the **net investment schedule** for Year 2 and Year 3 (interest at 10% on net; reduce net for cash interest and for principal at maturity).  
(d) Journal entries for December 31 of Year 2 (interest revenue and cash interest).  
(e) Journal entries for December 31 of Year 3 (interest revenue, cash interest, and principal collection), including clearing remaining AFDA and note balance.

**Answer key (Part B):**

**(a) PV of restructured cash flows @ 10%**  
Cash flows: **$3,800** end of Year 2, **$3,800 + $95,000** end of Year 3.  
\[
PV = \frac{3{,}800}{1.10} + \frac{3{,}800}{1.10^2} + \frac{95{,}000}{1.10^2} = \$85{,}107.44
\]
Excel: `=PV(0.10,2,-3800,-95000)` → **$85,107.44**.

| Item | Amount |
|---|---:|
| Pre-restructure carrying amount (\(120{,}000 + 12{,}000\)) | $132,000.00 |
| PV of expected payments @ **10%** | 85,107.44 |
| **Impairment (Bad Debt Expense)** | **46,892.56** |

**(b) January 1, Year 2 — restructure / impairment**  
```
Dr Note Receivable .............................. 12,000.00
   Cr Interest Receivable .............................. 12,000.00
```
(Capitalize accrued interest into the note investment; Dr = Cr = 12,000)

```
Dr Bad Debt Expense ......................... 46,892.56
   Cr Allowance for Doubtful Accounts .............. 46,892.56
```
(Dr = Cr = 46,892.56)

After these entries:  
Gross note investment **$132,000** − AFDA **$46,892.56** = **net $85,107.44** (= PV).

**(c) Net investment schedule**

| Date | Effective interest (10%) | Cash received | Net investment |
|---|---:|---:|---:|
| Jan 1, Y2 (post-impairment) | — | — | 85,107.44 |
| Dec 31, Y2 | 8,510.74 | 3,800.00 | 89,818.18 |
| Dec 31, Y3 | 8,981.82 | 3,800.00 | 95,000.00 |
| Dec 31, Y3 (principal) | — | 95,000.00 | 0.00 |

Checks: \(85{,}107.44 \times 0.10 = 8{,}510.74\); \(89{,}818.18 \times 0.10 = 8{,}981.82\).  
After Year 2 cash: \(85{,}107.44 + 8{,}510.74 - 3{,}800 = 89{,}818.18\).  
After Year 3 cash interest: \(89{,}818.18 + 8{,}981.82 - 3{,}800 = 95{,}000\).

**(d) December 31, Year 2**  
```
Dr Allowance for Doubtful Accounts ........... 8,510.74
   Cr Interest Revenue ................................. 8,510.74
```
```
Dr Cash .......................................... 3,800.00
   Cr Note Receivable ................................... 3,800.00
```
(Each balances. After entries: NR = \(132{,}000 - 3{,}800 = 128{,}200\); AFDA = \(46{,}892.56 - 8{,}510.74 = 38{,}381.82\); net = **$89,818.18**.)

**(e) December 31, Year 3 — interest, final cash interest, and principal**  
```
Dr Allowance for Doubtful Accounts ........... 8,981.82
   Cr Interest Revenue ................................. 8,981.82
```
```
Dr Cash .......................................... 3,800.00
   Cr Note Receivable ................................... 3,800.00
```
(After these two: NR = \(128{,}200 - 3{,}800 = 124{,}400\); AFDA = \(38{,}381.82 - 8{,}981.82 = 29{,}400.00\); net = **$95,000**.)

Principal collection and derecognition:  
```
Dr Cash ......................................... 95,000.00
Dr Allowance for Doubtful Accounts .............. 29,400.00
   Cr Note Receivable ................................. 124,400.00
```
(Dr \(95{,}000 + 29{,}400 = 124{,}400\) = Cr. Net investment cleared to zero.)

**Key insight:** For a **settlement**, record assets at **fair value** and a loss for any shortfall versus the receivable’s carrying amount. For a **modification** that continues the existing loan, discount **restructured** expected cash flows at the **original effective rate**, recognize impairment to that PV, then apply **effective interest** on the net investment.

---

### Q4 — MC — Discount rate for DCF impairment
**LO:** LO 8-9  
**Concept:** Classification/method choice — original effective rate vs current market rate for measuring impairment of a noncurrent receivable  
**Question:**  
Under the discounted cash flow method for estimating expected credit losses on a note receivable, the allowance is the excess of amortized cost over the present value of expected future cash flows. Those expected cash flows should be discounted using:

- A) The current market interest rate for notes of similar risk  
- B) The risk-free rate on U.S. Treasury securities of similar maturity  
- C) The financial asset’s **original effective interest rate**  
- D) The creditor’s weighted-average cost of capital  

**Answer:** **C.** ASC 326 requires that when a DCF method is used, expected cash flows are discounted at the asset’s **effective interest rate**. Changes in general market rates or risk premiums are **not** used to remeasure the allowance; only changes in expected cash flows affect the measurement. Using the current similar-risk market rate (A) would improperly mix fair-value interest-rate effects into credit-loss measurement.

---

### Q5 — MC — Subsequent interest after impairment (no cash expected)
**LO:** LO 8-9  
**Concept:** Classification/method — how subsequent effective interest is recorded after a DCF impairment when contractual interest is not expected  
**Question:**  
After a note receivable is impaired under the DCF method and management does **not** expect further contractual interest collections, recognition of interest revenue in subsequent periods under the effective interest method is typically recorded as:

- A) Debit Cash; credit Interest Revenue  
- B) Debit Interest Receivable; credit Interest Revenue  
- C) Debit Allowance for Doubtful Accounts; credit Interest Revenue  
- D) Debit Bad Debt Expense; credit Interest Revenue  

**Answer:** **C.** Interest revenue equals the **net carrying amount** × original effective rate. Because cash is not expected, the accretion is recorded by reducing the allowance (increasing net receivable) and recognizing interest revenue—matching Demo 8-9A / Review 8-9. Cash (A) and Interest Receivable (B) would imply collection or a new receivable; Bad Debt Expense (D) is used at **initial** impairment measurement, not for subsequent accretion.

---

### Self-check
- [x] Every JE balances (Dr = Cr)  
- [x] Math recomputed (PV factors, effective interest, AFDA roll-forwards, settlement plugs)  
- [x] Core demo path from LO 8-9 / Appendix 8B (Demo 8-9A, 8-9B, Review 8-9) — not Expanding Your Knowledge sidebars  
- [x] **LO:** and **Concept:** on every item  
- [x] MC ≤ 2 (Q4, Q5)  
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin  
- [x] Original company names and numbers (not textbook demo figures)
