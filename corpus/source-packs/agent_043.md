# Agent 43 — CORE DEMO — LO 8-5

**Chapter:** 8  
**LO title:** Noncurrent Note Receivable [Stated Rate = 0%; Market Rate = 10%]  
**Critical gap LO:** no

## Concept list for this pack
- Initial measurement of a zero-interest (0% stated) noncurrent note received for inventory/noncash (more clearly determinable FV)
- Discount on Note Receivable = face − present value; Sales (or other) revenue at PV, not face
- Effective-interest subsequent measurement: Interest revenue = beginning carrying amount × market rate; cash interest = 0 so full amount amortizes the discount
- Amortization schedule roll-forward to face at maturity
- Period-end adjusting entries when fiscal year-end ≠ note anniversary (allocate schedule interest)
- Maturity / settlement JE (collect face; clear Note Receivable)
- Balance-sheet classification: net carrying amount; current vs noncurrent in final year
- Number-variant twin with different face/PV/dates

---

### Q1 — CORE — Cascade Outfitters: zero-interest NR for inventory (initial JE, schedule, YE accruals, maturity)
**LO:** LO 8-5  
**Concept:** Initial recognition of 0% stated / 10% market noncurrent NR for inventory; effective-interest amortization; interim YE allocation; face settlement  
**Scenario:**  
On **June 30, Year 1**, **Cascade Outfitters Co.** sells inventory with a clearly determinable fair value of **$11,269** and receives in exchange a **three-year, noninterest-bearing** note with face (stated) value of **$15,000**. Principal is due in a single payment on **June 30, Year 4**. There are **no** periodic cash interest receipts (stated rate = **0%**). The market rate for notes of similar risk is **10%**. Ignore cost of goods sold.

The present value of the note equals the fair value of the inventory exchanged:

\[
PV = \frac{15{,}000}{(1.10)^{3}} = \mathbf{\$11{,}269}
\]

(Excel-equivalent: `PV(0.10,3,0,15000)` absolute value; or `RATE(3,0,-11269,15000)` confirms **10%**.)

**Required:**  
(a) Record the **June 30, Year 1** journal entry for receipt of the note (initial recognition). Compute the initial **Discount on Note Receivable**.  
(b) Prepare the **effective-interest amortization schedule** for the full term (cash interest, interest revenue, discount amortization, carrying amount).  
(c) Assume Cascade has a **June 30** fiscal year-end (note anniversary). Record all **interest accrual** entries on June 30 of Years 2, 3, and 4, and the **settlement** entry on June 30, Year 4 when face is collected.  
(d) Assume instead Cascade has a **December 31** year-end. The initial recognition and final cash collection entries are unchanged. Allocate the amortization schedule into reporting periods and record interest accruals on **December 31 of Years 1, 2, and 3** and on **June 30, Year 4**. Verify total interest revenue equals the original discount.  
(e) Briefly state how the note is **presented** on the December 31, Year 1 balance sheet (current vs noncurrent).

**Answer key:**

**(a) Initial recognition — June 30, Year 1**

Discount = face − PV = \(15{,}000 - 11{,}269 = \mathbf{\$3{,}731}\).

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 15,000 | |
| Discount on Note Receivable | | 3,731 |
| Sales Revenue | | 11,269 |

Check: Dr 15,000 = Cr 3,731 + 11,269. Net note receivable (carrying amount) = **$11,269**.

**(b) Effective-interest amortization schedule (market = 10%; stated cash interest = $0)**

| Date | Cash interest (stated 0%) | Interest revenue (CA × 10%) | Discount amortization | Note receivable, net (CA) |
|------|--------------------------:|----------------------------:|----------------------:|--------------------------:|
| June 30, Year 1 | — | — | — | **11,269** |
| June 30, Year 2 | 0 | 1,127 | 1,127 | 12,396 |
| June 30, Year 3 | 0 | 1,240 | 1,240 | 13,636 |
| June 30, Year 4 | 0 | 1,364 | 1,364 | **15,000** |
| **Totals** | **0** | **3,731** | **3,731** | |

Interest checks: \(11{,}269 \times 0.10 = 1{,}126.9 \to 1{,}127\); \(12{,}396 \times 0.10 = 1{,}239.6 \to 1{,}240\); \(13{,}636 \times 0.10 = 1{,}363.6 \to 1{,}364\).  
\(11{,}269 + 1{,}127 + 1{,}240 + 1{,}364 = 15{,}000\). Sales revenue \(11{,}269\) + total interest revenue \(3{,}731\) = total cash \(15{,}000\).

**(c) June 30 year-end accruals and settlement**

June 30, Year 2 — amortize discount / recognize interest:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,127 | |
| Interest Revenue | | 1,127 |

June 30, Year 3:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,240 | |
| Interest Revenue | | 1,240 |

June 30, Year 4 — final interest:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,364 | |
| Interest Revenue | | 1,364 |

June 30, Year 4 — collect face (after discount is fully amortized; net CA = face):

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 15,000 | |
| Note Receivable | | 15,000 |

**(d) December 31 year-end — allocate schedule amounts to reporting periods**

Half-year splits of each annual interest amount (first half of each note year gets the ceiling when odd):

| Note-year interest (ended June 30) | Amount | Allocated to prior Dec 31 | Allocated to next period |
|------------------------------------|-------:|----------------------------:|-------------------------:|
| Year ended June 30, Y2 | 1,127 | Dec 31, Y1: **564** | first half Y2: **563** |
| Year ended June 30, Y3 | 1,240 | Dec 31, Y2: **620** | first half Y3: **620** |
| Year ended June 30, Y4 | 1,364 | Dec 31, Y3: **682** | June 30, Y4: **682** |

Reporting-period interest revenue:

| Reporting date | Interest revenue | Build-up |
|----------------|-----------------:|----------|
| Dec 31, Year 1 | **564** | 564 |
| Dec 31, Year 2 | **1,183** | 563 + 620 |
| Dec 31, Year 3 | **1,302** | 620 + 682 |
| June 30, Year 4 | **682** | 682 |
| **Total** | **3,731** | equals original discount |

Journal entries:

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 564 | |
| Interest Revenue | | 564 |

December 31, Year 2:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,183 | |
| Interest Revenue | | 1,183 |

December 31, Year 3:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,302 | |
| Interest Revenue | | 1,302 |

June 30, Year 4:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 682 | |
| Interest Revenue | | 682 |

(Settlement Cash / Note Receivable same as part c.)

**(e) Classification / presentation — December 31, Year 1**

After the Dec 31, Y1 accrual, carrying amount = \(11{,}269 + 564 = \mathbf{\$11{,}833}\).  
Principal is not due until June 30, Year 4 (more than one year from Dec 31, Y1), so the **entire net note receivable of $11,833** is reported as a **noncurrent asset**. Discount on Note Receivable is a **contra-asset** deducted from Note Receivable (face) to arrive at the net carrying amount; it is not a liability.

**Key insight:** A 0% stated-rate note still has interest — the entire discount amortizes into interest revenue under the effective-interest method (CA × market rate). Initial sales revenue is limited to the **present value**, not face; cash interest is zero so Dr Discount = Cr Interest Revenue each period.

---

### Q2 — CORE number variant — Rivermark Tools: 0% / 10% NR twin
**LO:** LO 8-5  
**Concept:** Number-variant twin — initial recognition, full amortization schedule, annual accruals, maturity (different face/PV/dates)  
**Scenario:**  
On **January 1, Year 1**, **Rivermark Tools Inc.** sells specialized tooling with a fair value of **$13,524** and receives a **three-year, noninterest-bearing** note with face value **$18,000**. Face is due **December 31, Year 3**. Market rate for similar risk is **10%**. Rivermark’s fiscal year-end is **December 31** (coincides with the note’s interest “anniversary”). Ignore cost of goods sold.

\[
PV = \frac{18{,}000}{(1.10)^{3}} = \mathbf{\$13{,}524}
\]

**Required:**  
(a) Record the **January 1, Year 1** initial recognition entry and state the initial discount.  
(b) Prepare the **effective-interest amortization schedule** through maturity.  
(c) Record the **December 31** interest entries for Years 1–3 and the **maturity collection** entry on December 31, Year 3.  
(d) Prove that sales revenue + total interest revenue = cash collected.

**Answer key:**

**(a) Initial recognition — January 1, Year 1**

Discount = \(18{,}000 - 13{,}524 = \mathbf{\$4{,}476}\).

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 18,000 | |
| Discount on Note Receivable | | 4,476 |
| Sales Revenue | | 13,524 |

Dr = Cr = 18,000. Net CA = **$13,524**.

**(b) Amortization schedule (i = 10%)**

| Date | Cash interest | Interest revenue (CA × 10%) | Discount amort. | Carrying amount |
|------|-------------:|----------------------------:|----------------:|----------------:|
| Jan 1, Year 1 | — | — | — | **13,524** |
| Dec 31, Year 1 | 0 | 1,352 | 1,352 | 14,876 |
| Dec 31, Year 2 | 0 | 1,488 | 1,488 | 16,364 |
| Dec 31, Year 3 | 0 | 1,636 | 1,636 | **18,000** |
| **Totals** | **0** | **4,476** | **4,476** | |

Checks: \(13{,}524 \times 0.10 = 1{,}352.4 \to 1{,}352\); \(14{,}876 \times 0.10 = 1{,}487.6 \to 1{,}488\); \(16{,}364 \times 0.10 = 1{,}636.4 \to 1{,}636\).  
\(13{,}524 + 1{,}352 + 1{,}488 + 1{,}636 = 18{,}000\).

**(c) Period-end adjusting / maturity JEs**

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,352 | |
| Interest Revenue | | 1,352 |

December 31, Year 2:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,488 | |
| Interest Revenue | | 1,488 |

December 31, Year 3 — final interest:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,636 | |
| Interest Revenue | | 1,636 |

December 31, Year 3 — settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 18,000 | |
| Note Receivable | | 18,000 |

**(d) Economic split**  
Sales revenue \(13{,}524\) + interest revenue \(4{,}476\) = cash \(18{,}000\). Separating financing from the sale is the purpose of PV measurement.

**Key insight:** Same mechanics as Q1 with all new numbers — when year-end matches the schedule date, each full-year interest amount posts once with no interim allocation.

---

### Q3 — CORE alternate angle — Harborline Distributing: cash-loaned zero-interest NR, current/noncurrent split, settlement
**LO:** LO 8-5  
**Concept:** Zero-interest NR for cash (measure at cash proceeds); subsequent schedule; BS current/noncurrent classification of net CA; maturity settlement  
**Scenario:**  
On **January 1, Year 1**, **Harborline Distributing Co.** loans cash to a customer and receives a **four-year, noninterest-bearing** note with face **$20,000** due **December 31, Year 4**. Cash advanced is **$13,660** (equal to the present value of the note at the **10%** market rate for similar risk). Harborline’s year-end is **December 31**.

\[
PV = \frac{20{,}000}{(1.10)^{4}} = \mathbf{\$13{,}660}
\]

**Required:**  
(a) Record the **January 1, Year 1** initial recognition entry (cash loan).  
(b) Prepare the **four-year effective-interest amortization schedule**.  
(c) Record the **December 31, Year 1** adjusting entry only.  
(d) At **December 31, Year 3** (after that day’s interest accrual), compute the **net carrying amount** and state the **current vs noncurrent** balance-sheet classification (principal due in one year).  
(e) Record the **December 31, Year 4** interest accrual and the **settlement** entry.

**Answer key:**

**(a) Initial recognition — cash loan — January 1, Year 1**

Discount = \(20{,}000 - 13{,}660 = \mathbf{\$6{,}340}\).

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 20,000 | |
| Discount on Note Receivable | | 6,340 |
| Cash | | 13,660 |

Dr = Cr. Net CA = cash advanced = **$13,660** (ASC 835-30 cash-proceeds presumption when note is solely for cash).

**(b) Amortization schedule (i = 10%)**

| Date | Cash interest | Interest revenue | Discount amort. | Carrying amount |
|------|-------------:|-----------------:|----------------:|----------------:|
| Jan 1, Year 1 | — | — | — | **13,660** |
| Dec 31, Year 1 | 0 | 1,366 | 1,366 | 15,026 |
| Dec 31, Year 2 | 0 | 1,503 | 1,503 | 16,529 |
| Dec 31, Year 3 | 0 | 1,653 | 1,653 | 18,182 |
| Dec 31, Year 4 | 0 | 1,818 | 1,818 | **20,000** |
| **Totals** | **0** | **6,340** | **6,340** | |

Checks: \(13{,}660 \times 0.10 = 1{,}366\); \(15{,}026 \times 0.10 = 1{,}502.6 \to 1{,}503\); \(16{,}529 \times 0.10 = 1{,}652.9 \to 1{,}653\); \(18{,}182 \times 0.10 = 1{,}818.2 \to 1{,}818\).  
\(13{,}660 + 1{,}366 + 1{,}503 + 1{,}653 + 1{,}818 = 20{,}000\).

**(c) December 31, Year 1 adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,366 | |
| Interest Revenue | | 1,366 |

**(d) Classification — December 31, Year 3 (after Year 3 accrual)**

Net carrying amount = **$18,182**.  
Face is due **December 31, Year 4** — within one year of the balance-sheet date — so the **entire net receivable of $18,182** is classified as a **current asset** (Note Receivable $20,000 less remaining unamortized discount \(20{,}000 - 18{,}182 = \$1{,}818\)). There is no noncurrent portion once the sole principal payment is due within the next year.

**(e) Maturity year — December 31, Year 4**

Interest accrual (amortizes remaining discount):

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,818 | |
| Interest Revenue | | 1,818 |

Settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 20,000 | |
| Note Receivable | | 20,000 |

After the final amortization, Discount balance = 0 and net CA = face before cash collection.

**Key insight:** Whether the note arises from a cash loan or a noncash sale, a 0% stated / 10% market note is measured at **PV (or cash proceeds)** and grows to face solely through discount amortization. In the final year before principal is due, the **full net carrying amount** is current.

---

### Q4 — MC (classification / measurement)
**LO:** LO 8-5  
**Concept:** Initial measurement basis and interest-revenue amount when stated rate is 0%

**Question 1:**  
On the date inventory is sold for a three-year noninterest-bearing note, the market rate for similar notes is 10%. Which amount should be recorded as **Sales Revenue**?

- A) Face amount of the note  
- B) Face amount of the note plus imputed interest over the term  
- C) Present value of the note’s future cash flows discounted at the **market** rate (or the more clearly determinable fair value of the inventory)  
- D) Present value of the note’s future cash flows discounted at a 0% rate  

**Answer:** C. ASC 835-30 requires measurement at the more clearly determinable amount — FV of goods or PV of the note using an imputed market rate when stated interest is missing or unreasonable. Sales revenue equals that PV, not face. Face exceeds PV; the difference is discount (future interest revenue), not additional sales.

**Question 2:**  
For a noncurrent note receivable with a **0% stated rate** accounted for under the effective-interest method, interest revenue each period equals:

- A) Face × stated rate (always zero, so no interest is ever recognized)  
- B) Face × market rate  
- C) Beginning net carrying amount × market rate (which also equals discount amortization when cash interest is zero)  
- D) Total discount ÷ number of years (straight-line required)  

**Answer:** C. Interest revenue = beginning CA × market (effective) rate. With stated cash interest of zero, the full interest revenue amortizes Discount on NR. Straight-line is not the primary method illustrated for this LO; face × market rate would overstate interest early in the life of a discount note.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV, amort schedules roll to face; interim allocations sum to total discount)
- [x] Core demo path (Demo 8-5C style: 0% stated / 10% market noncurrent NR) — not sidebar-only
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/measurement items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook Atlas $6,011 / $8,000)
