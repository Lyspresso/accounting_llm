# Agent 21 — CORE DEMO — LO 17-12

**Chapter:** 17  
**LO title:** Describe the difference in accounting for a sale-leaseback versus a failed sale  
**Critical gap LO:** yes

## Concept list for this pack
- Sale-leaseback vs failed sale hinge: does **control** transfer? (leaseback **operating** → sale; leaseback **finance** → failed sale)
- **Initial recognition — sale-leaseback:** derecognize asset, record gain/loss, recognize operating ROU asset and lease liability at PV of lease payments
- **Initial recognition — failed sale:** keep asset on books, record proceeds as a **loan/note payable** (no sale, no gain)
- Subsequent measurement schedules: lease liability / ROU (operating leaseback) vs note amortization (failed sale)
- Period-end adjusting entries: operating lease expense + payment vs interest/principal + continued depreciation
- Maturity/settlement of failed-sale note over full term; asset continues to be depreciated over remaining useful life
- Classification / presentation: gain on sale-leaseback vs financing liability; finance-leaseback criteria (term ≥ 75% of economic life; PV ≥ substantially all of FV)

---

### Q1 — CORE — Sale-leaseback vs failed sale: classification, initial recognition, Year-1 schedules and JEs
**LO:** LO 17-12  
**Concept:** Initial recognition JEs and Year-1 subsequent measurement — sale-leaseback (operating) versus failed sale (finance liability)  
**Scenario:**  
On **January 1, Year 1**, Cascade Logistics Inc. sells a warehouse to Summit Capital Partners for **$200,000** cash (fair value) and simultaneously leases the warehouse back. Before the transfer, Cascade’s books show:

| | Amount |
|---|---:|
| Warehouse (cost) | $450,000 |
| Accumulated depreciation | 270,000 |
| **Carrying amount** | **$180,000** |

- Estimated **remaining useful life** of the warehouse: **15 years** (no residual value; straight-line).
- Cascade’s incremental borrowing rate equals the rate implicit in the lease: **8%** (known to Cascade).
- The lease contains **no** ownership transfer and **no** purchase option. The warehouse has **alternative uses** to Summit at lease end.
- Annual lease payments are due **each December 31** (ordinary annuity).

**Alternative A — Sale-leaseback path**  
Lease term **5 years**; annual payment **$35,000**.

**Alternative B — Failed-sale path**  
Same facts except lease term **12 years** and annual payment **$26,539** (structured so the PV of payments equals the $200,000 cash received).

**Required:**  
a. For **Alternative A**, evaluate the five finance-lease classification criteria and conclude whether the arrangement is a **sale-leaseback** or a **failed sale**. Compute the PV of lease payments.  
b. Prepare Cascade’s **January 1, Year 1** journal entries under Alternative A.  
c. Prepare a partial **lease liability / ROU** schedule for Years 1–2 under Alternative A and the **December 31, Year 1** journal entries.  
d. For **Alternative B**, evaluate classification and conclude sale-leaseback vs failed sale.  
e. Prepare Cascade’s **January 1, Year 1** journal entry under Alternative B.  
f. Prepare a partial **note payable amortization** schedule for Years 1–2 under Alternative B and the **December 31, Year 1** journal entries (payment and depreciation).  
g. Briefly contrast balance-sheet / income-statement presentation at Dec 31, Year 1 under A vs B.

**Answer key:**  

**a. Alternative A — Classification**  

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to lessor; no title transfer | No |
| 2. Purchase option | None | No |
| 3. Lease term | 5 / 15 = **33%** of remaining economic life (< 75%) | No |
| 4. PV of lease payments | See below; compare to 90% of FV | No |
| 5. Specialized asset / no alternative use | Alternative uses exist | No |

\[
\text{PV of lease payments} = \$35{,}000 \times \frac{1-(1.08)^{-5}}{0.08} = \$35{,}000 \times 3.992710 = \mathbf{\$139{,}744.85}
\]

90% of fair value = 0.90 × $200,000 = **$180,000**.  
$139,744.85 < $180,000 → PV criterion not met.

**None** of the finance-lease criteria are met → leaseback is an **operating lease** → **control transfers** → treat as a **sale-leaseback**.

**b. January 1, Year 1 — Sale-leaseback initial recognition**  
Gain = sale price − carrying amount = $200,000 − $180,000 = **$20,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 200,000 | |
| Accumulated Depreciation—Warehouse | 270,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Warehouse | | 450,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;Gain on Sale-Leaseback | | 20,000 |
| *Derecognize warehouse and recognize sale at FV* | | |

Dr 470,000 = Cr 470,000 ✓

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 139,744.85 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Lease Liability | | 139,744.85 |
| *Recognize operating lease at PV of lease payments* | | |

Dr 139,744.85 = Cr 139,744.85 ✓

**c. Alternative A — Liability / ROU schedule (partial) and Dec 31, Year 1**  

Lease Liability / ROU Asset Schedule (operating; equal annual payments)

| Date | Lease payment | Interest (8% × beg. bal.) | Liability / ROU reduction | Ending liability = ending ROU |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | — | — | — | 139,744.85 |
| Dec 31, Y1 | 35,000.00 | 11,179.59 | 23,820.41 | 115,924.44 |
| Dec 31, Y2 | 35,000.00 | 9,273.96 | 25,726.04 | 90,198.40 |

Interest Y1 = $139,744.85 × 0.08 = **$11,179.59**  
ROU / principal reduction Y1 = $35,000.00 − $11,179.59 = **$23,820.41**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 35,000.00 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Lease Liability | | 11,179.59 |
| &nbsp;&nbsp;&nbsp;&nbsp;Right-of-Use Asset | | 23,820.41 |
| *Operating lease cost (single lease expense); accrete liability and amortize ROU* | | |

Dr 35,000.00 = Cr 35,000.00 ✓

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000.00 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 35,000.00 |
| *Cash lease payment* | | |

Dr 35,000.00 = Cr 35,000.00 ✓  

Net liability reduction = 35,000.00 − 11,179.59 = 23,820.41 → ending liability **$115,924.44**.

**d. Alternative B — Classification**  

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | No | No |
| 2. Purchase option | None | No |
| 3. Lease term | 12 / 15 = **80%** of remaining economic life (≥ 75%) | **Yes** |
| 4. PV of lease payments | PV of $26,539 for 12 periods at 8% ≈ **$200,000** ≥ 90% of FV ($180,000) | **Yes** |
| 5. Specialized / no alternative use | Alternative uses exist | No |

Finance-lease criteria **are met** (term and PV). A finance leaseback means the seller-lessee has **not** surrendered control → **failed sale**. Proceeds are a **financing**, not a sale.

**e. January 1, Year 1 — Failed sale initial recognition**  
Do **not** remove the warehouse or record a gain. Record cash as a loan:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 200,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Note Payable | | 200,000 |
| *Failed sale — proceeds accounted for as a borrowing* | | |

Dr 200,000 = Cr 200,000 ✓

**f. Alternative B — Note schedule (partial) and Dec 31, Year 1**  

Note Payable Amortization Schedule (partial)

| Date | Payment | Interest (8%) | Principal | Ending note balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | — | — | — | 200,000.00 |
| Dec 31, Y1 | 26,539.00 | 16,000.00 | 10,539.00 | 189,461.00 |
| Dec 31, Y2 | 26,539.00 | 15,156.88 | 11,382.12 | 178,078.88 |

Interest Y1 = $200,000 × 0.08 = **$16,000**  
Principal Y1 = $26,539 − $16,000 = **$10,539**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 16,000 | |
| Note Payable | 10,539 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 26,539 |
| *Allocate payment to interest and principal* | | |

Dr 26,539 = Cr 26,539 ✓

Continue depreciating the warehouse over remaining useful life:  
Depreciation = $180,000 / 15 = **$12,000**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 12,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation—Warehouse | | 12,000 |
| *Asset remains on books; depreciate remaining CV over 15 years* | | |

Dr 12,000 = Cr 12,000 ✓

**g. Presentation contrast (Dec 31, Year 1)**  

| Item | Alternative A (sale-leaseback) | Alternative B (failed sale) |
|---|---|---|
| Warehouse asset | **Derecognized** | Still on books (CV after Y1 dep = $168,000) |
| Financing liability | Lease liability **$115,924.44** | Note payable **$189,461** |
| ROU asset | **$115,924.44** | None (no lease capitalization as lessee “purchase”) |
| Year 1 income | Gain on sale **$20,000** + lease expense **$35,000** | Interest exp **$16,000** + dep exp **$12,000** (no sale gain) |

**Key insight:** If the leaseback is **operating**, control transferred → record a **sale** (gain/loss) and an **operating lease**. If the leaseback is **finance**, control did **not** transfer → **failed sale**: keep the asset, book proceeds as a **loan**, and allocate payments to interest and principal while continuing depreciation.

---

### Q2 — CORE number variant — Sale-leaseback vs failed sale with different facts
**LO:** LO 17-12  
**Concept:** Number-variant twin — initial recognition and first-year measurement for sale-leaseback vs failed sale  
**Scenario:**  
On **January 1, Year 1**, Horizon Freight Co. sells a distribution building to Lakeside Funding LLC for **$320,000** cash (fair value) and leases it back. Horizon’s records immediately before the transfer:

| | Amount |
|---|---:|
| Building (cost) | $800,000 |
| Accumulated depreciation | 520,000 |
| **Carrying amount** | **$280,000** |

- Remaining useful life: **20 years**; residual value zero; straight-line depreciation.
- Implicit rate known to Horizon: **7%**.
- No title transfer, no purchase option; building has alternative uses at lease end.
- Payments due each **December 31**.

**Case S (sale-leaseback):** term **6 years**; annual payment **$48,000**.  
**Case F (failed sale):** term **16 years**; annual payment **$33,874.45** (PV of payments equals the $320,000 cash).

**Required:**  
a. Classify Case S and Case F (sale-leaseback vs failed sale); support with term % and PV test.  
b. Journal entries on January 1, Year 1 for **both** cases.  
c. December 31, Year 1 journal entries for **both** cases (include depreciation only where applicable).  
d. State ending lease liability (Case S) and ending note payable (Case F) at Dec 31, Year 1.

**Answer key:**  

**a. Classification**  

**Case S:**  
Term = 6/20 = **30%** < 75%.  
\[
\text{PV} = \$48{,}000 \times \frac{1-(1.07)^{-6}}{0.07} = \$48{,}000 \times 4.766540 = \mathbf{\$228{,}793.90}
\]  
90% of FV = 0.90 × $320,000 = **$288,000**. PV $228,793.90 < $288,000.  
No finance criteria met → **operating leaseback** → **sale-leaseback**.

**Case F:**  
Term = 16/20 = **80%** ≥ 75% → finance criterion met.  
PV of $33,874.45 for 16 periods at 7% ≈ **$320,000** ≥ $288,000 → PV criterion also met.  
**Failed sale**.

**b. January 1, Year 1**  

*Case S — Sale and operating lease*  
Gain = $320,000 − $280,000 = **$40,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 320,000 | |
| Accumulated Depreciation—Building | 520,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Building | | 800,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;Gain on Sale-Leaseback | | 40,000 |

Dr 840,000 = Cr 840,000 ✓

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 228,793.90 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Lease Liability | | 228,793.90 |

Dr 228,793.90 = Cr 228,793.90 ✓

*Case F — Financing only*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 320,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Note Payable | | 320,000 |

Dr 320,000 = Cr 320,000 ✓  
(Building remains; no gain.)

**c. December 31, Year 1**  

*Case S*  
Interest = $228,793.90 × 0.07 = **$16,015.57**  
ROU reduction = $48,000 − $16,015.57 = **$31,984.43**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 48,000.00 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Lease Liability | | 16,015.57 |
| &nbsp;&nbsp;&nbsp;&nbsp;Right-of-Use Asset | | 31,984.43 |

Dr 48,000.00 = Cr 48,000.00 ✓

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 48,000.00 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 48,000.00 |

Dr 48,000.00 = Cr 48,000.00 ✓

*Case F*  
Interest = $320,000 × 0.07 = **$22,400.00**  
Principal = $33,874.45 − $22,400.00 = **$11,474.45**  
Depreciation = $280,000 / 20 = **$14,000**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 22,400.00 | |
| Note Payable | 11,474.45 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 33,874.45 |

Dr 33,874.45 = Cr 33,874.45 ✓

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 14,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation—Building | | 14,000 |

Dr 14,000 = Cr 14,000 ✓

**d. Ending balances Dec 31, Year 1**  
- Case S lease liability = $228,793.90 − $31,984.43 = **$196,809.47**  
- Case F note payable = $320,000 − $11,474.45 = **$308,525.55**

**Key insight:** Changing only term/payment size flips classification. Operating leaseback → sale + ROU/lease liability; finance leaseback → failed sale (loan + continued depreciation of the original asset).

---

### Q3 — CORE — Failed sale: multi-year amortization to maturity/settlement
**LO:** LO 17-12  
**Concept:** Failed-sale note amortization through final settlement; continued depreciation over remaining useful life  
**Scenario:**  
On **January 1, Year 1**, Northshore Manufacturing Co. “sells” specialized production equipment to Riverbend Leasing for **$135,000** cash and immediately leases it back for **4 years**. Facts:

| | Amount |
|---|---:|
| Equipment (cost) | $210,000 |
| Accumulated depreciation | 90,000 |
| **Carrying amount** | **$120,000** |

- Remaining useful life equals the lease term: **4 years**; residual value zero; straight-line.
- Annual payments of **$38,959.85** due each December 31; interest rate **6%** (known).
- No purchase option; title does not transfer under a bargain; however, lease term = **100%** of remaining economic life.

**Required:**  
a. Explain why this is a **failed sale** (not a sale-leaseback).  
b. Record the January 1, Year 1 entry.  
c. Prepare the **complete** note payable amortization schedule (Years 1–4) and depreciation each year.  
d. Record all December 31, Year 4 entries (final payment / settlement and final depreciation).  
e. What is the equipment’s carrying amount immediately after the Year 4 depreciation entry?

**Answer key:**  

**a.** Lease term = 4/4 = **100%** of remaining economic life → **finance lease** criterion met. Finance leaseback means control did **not** transfer to the buyer-lessor → **failed sale**. Proceeds are a loan; equipment stays on Northshore’s books.

**b. January 1, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 135,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Note Payable | | 135,000 |
| *Failed sale — financing, not a sale* | | |

Dr 135,000 = Cr 135,000 ✓

**c. Full note amortization and depreciation**  

Annual depreciation = $120,000 / 4 = **$30,000** each year.

| Year | Payment | Interest (6% × beg.) | Principal | Ending note bal. | Depreciation | Ending equip. CV |
|---:|---:|---:|---:|---:|---:|---:|
| 0 (1/1 Y1) | — | — | — | 135,000.00 | — | 120,000 |
| 1 | 38,959.85 | 8,100.00 | 30,859.85 | 104,140.15 | 30,000 | 90,000 |
| 2 | 38,959.85 | 6,248.41 | 32,711.44 | 71,428.71 | 30,000 | 60,000 |
| 3 | 38,959.85 | 4,285.72 | 34,674.13 | 36,754.58 | 30,000 | 30,000 |
| 4 | 38,959.85 | 2,205.27 | 36,754.58 | **0.00** | 30,000 | **0** |

Checks: Y1 interest = 135,000 × 0.06 = 8,100; 8,100 + 30,859.85 = 38,959.85.  
Y4: 2,205.27 + 36,754.58 = 38,959.85; note clears to zero.

**d. December 31, Year 4 — settlement and final depreciation**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 2,205.27 | |
| Note Payable | 36,754.58 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 38,959.85 |
| *Final payment settles the failed-sale note* | | |

Dr 38,959.85 = Cr 38,959.85 ✓

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 30,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation—Equipment | | 30,000 |
| *Final year of remaining useful life* | | |

Dr 30,000 = Cr 30,000 ✓

**e.** Carrying amount after Year 4 depreciation = **$0** (fully depreciated). Note payable = **$0** (settled). Equipment cost $210,000 remains in the accounts with accumulated depreciation $210,000 until disposal/retirement of the fully depreciated asset (no failed-sale liability remains).

**Key insight:** A failed sale is accounted for like a **secured borrowing** through maturity: payments split interest/principal until the note is extinguished, while the original asset is depreciated over its useful life—not “sold” and not replaced by a ROU asset from a true sale-leaseback.

---

### Q4 — MC — Classification: sale-leaseback vs failed sale
**LO:** LO 17-12  
**Concept:** Classify transfer as sale-leaseback or failed sale based on leaseback type (control)  
**Question:**  
Pinnacle Tools sells a building (carrying amount $2,400,000) to an unrelated lessor for cash equal to fair value of $3,000,000 and leases the building back for 18 years. The building’s remaining economic life is 20 years. There is no purchase option and title does not transfer at lease end. The PV of lease payments equals approximately 95% of the building’s fair value. How should Pinnacle account for the transfer at inception?

- A) Record a sale and a $600,000 gain; recognize an operating ROU asset and lease liability.  
- B) Record a sale and a $600,000 gain; recognize a finance ROU asset and lease liability.  
- C) Do **not** record a sale; credit a note (or financing) payable for $3,000,000 and keep the building on the books.  
- D) Defer the entire $600,000 difference as unearned gain and amortize it over 18 years as a reduction of rent expense (legacy sale-leaseback model).

**Answer:** **C.**  
Lease term = 18/20 = **90%** ≥ 75%, and PV ≈ 95% of FV ≥ substantially all of FV → the leaseback is a **finance lease**. Under ASC 842 / the chapter’s control test, a finance leaseback means control did **not** transfer → **failed sale**. Proceeds are a loan; the building is **not** derecognized and **no** sale gain is recognized. A is the treatment for an **operating** leaseback (true sale-leaseback). B incorrectly pairs a sale gain with a finance leaseback. D is not the current core model illustrated for this LO.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV factors, interest, principal, depreciation, gains)
- [x] Core demo not sidebar-only (Appendix 17C / Demo 17-12 primary path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and amounts (not textbook Merill / Wal-Market figures)
