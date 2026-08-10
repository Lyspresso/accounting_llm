# Agent 77 — CORE DEMO — LO 12-11

**Chapter:** 12  
**LO title:** Depreciation under GAAP and under the Internal Revenue Code are different  
**Critical gap LO:** no

## Concept list for this pack
- **Initial recognition JE:** capitalize PPE at historical cost (same cost basis starts both book and tax records)
- **MACRS (tax) vs GAAP (book):** statutory recovery percentages by property class; residual value **ignored** for tax; half-year convention built into MACRS rates
- **Subsequent measurement schedule:** full MACRS multi-year tax depreciation schedule vs straight-line book schedule side by side
- **Period-end adjusting JE:** only **GAAP** depreciation is recorded on the books (tax deduction is computed on the tax return / workpapers)
- **Disposal / settlement JE:** remove asset and accumulated depreciation at book carrying amount; book gain/loss ≠ tax gain/loss because tax basis differs
- Classification / presentation: MACRS is for **tax** only; temporary book–tax differences (deferred taxes deferred to Ch. 18); total life-cycle pretax economic effect converges when residual and sale are considered
- **Number-variant twin:** same structure, different class life and dollar amounts

---

### Q1 — CORE — Initial recognition, MACRS vs book schedules, Year-1 book adjusting JE
**LO:** LO 12-11  
**Concept:** Initial recognition of PPE at cost; full MACRS (5-year) tax schedule vs GAAP straight-line schedule; Year-1 book depreciation adjusting JE; book vs tax total comparison  
**Scenario:**  
**Northridge Machining LLC**, a calendar-year company, places a CNC milling system in service on **January 1, Year 1**. Management elects **out of** bonus depreciation and uses **MACRS** tables for the tax deduction. For financial reporting, Northridge uses **straight-line** depreciation.

| Fact | Amount / term |
|---|---|
| Cash purchase price (cost basis) | **$75,000** |
| MACRS property class (tax) | **Five-year** property |
| Useful life (GAAP) | **10 years** |
| Residual / salvage value (GAAP) | **$5,000** |
| Book depreciation method | Straight-line |
| Bonus depreciation | Not used |

**MACRS five-year recovery percentages (given):**  
Year 1: 20.00% · Year 2: 32.00% · Year 3: 19.20% · Year 4: 11.52% · Year 5: 11.52% · Year 6: 5.76%

**Required:**  
a. Prepare the **January 1, Year 1** journal entry for **initial recognition** of the equipment (cash purchase).  
b. Compute **annual GAAP straight-line** depreciation. Prepare the **December 31, Year 1** adjusting entry for book depreciation.  
c. Prepare a complete **MACRS tax depreciation schedule** for Years 1–6 (rate × cost = tax depreciation). Show cumulative tax depreciation and **tax basis** at each year-end.  
d. Prepare a side-by-side schedule of **tax depreciation vs book depreciation** for Years 1–10 (book continues through Year 10; tax is complete after Year 6). Total both columns.  
e. Briefly explain **why** total tax depreciation over the asset’s MACRS life differs from total book depreciation, and whether MACRS rates are used for **GAAP** financial statements.

**Answer key:**

**a. Initial recognition (same cost starts book and tax)**

*January 1, Year 1 — Purchase equipment*

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—CNC Milling System | 75,000 | |
| Cash | | 75,000 |
| *Capitalize historical cost; cost basis for book and tax* | | |

**Check:** Dr 75,000 = Cr 75,000. **Balanced.**

**b. GAAP depreciation and Year-1 adjusting JE**

\[
\text{Annual SL depreciation} = \frac{\$75{,}000 - \$5{,}000}{10} = \mathbf{\$7{,}000}
\]

*December 31, Year 1 — Book depreciation (GAAP only)*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 7,000 | |
| Accumulated Depreciation—CNC Milling System | | 7,000 |

**Check:** Dr = Cr = 7,000. **Balanced.**

*(Tax MACRS of Year 1 is computed on the tax return / tax workpapers — it is **not** the book depreciation entry.)*

**c. MACRS tax depreciation schedule (five-year class; residual ignored)**

Cost × statutory rate. Tax basis end = prior tax basis − current MACRS depreciation. Beginning tax basis Year 1 = **$75,000**.

| Year | Tax basis, beginning | MACRS rate | MACRS depreciation | Tax basis, end |
|---:|---:|---:|---:|---:|
| 1 | 75,000 | 20.00% | **15,000** | 60,000 |
| 2 | 60,000 | 32.00% | **24,000** | 36,000 |
| 3 | 36,000 | 19.20% | **14,400** | 21,600 |
| 4 | 21,600 | 11.52% | **8,640** | 12,960 |
| 5 | 12,960 | 11.52% | **8,640** | 4,320 |
| 6 | 4,320 | 5.76% | **4,320** | **0** |
| **Total** | | **100.00%** | **75,000** | |

**Roll-forward check:** $75,000 × (0.20 + 0.32 + 0.192 + 0.1152 + 0.1152 + 0.0576) = $75,000. Ending tax basis = **$0**.

**d. Side-by-side: tax (MACRS) vs book (SL)**

| Year | MACRS tax depreciation | Book SL depreciation | Excess of tax over book (temp. difference driver) |
|---:|---:|---:|---:|
| 1 | 15,000 | 7,000 | 8,000 |
| 2 | 24,000 | 7,000 | 17,000 |
| 3 | 14,400 | 7,000 | 7,400 |
| 4 | 8,640 | 7,000 | 1,640 |
| 5 | 8,640 | 7,000 | 1,640 |
| 6 | 4,320 | 7,000 | (2,680) |
| 7 | 0 | 7,000 | (7,000) |
| 8 | 0 | 7,000 | (7,000) |
| 9 | 0 | 7,000 | (7,000) |
| 10 | 0 | 7,000 | (7,000) |
| **Total** | **75,000** | **70,000** | **5,000** |

**e. Why totals differ; GAAP use**  
- Under **MACRS**, residual value is **ignored**, so the full **$75,000** cost is recovered for tax over the class life (half-year convention embedded in rates).  
- Under **GAAP**, depreciable base is cost minus residual: **$70,000**; residual remains on the books until disposal.  
- The **$5,000** excess of total tax depreciation over total book depreciation equals the GAAP residual value.  
- **MACRS rates are not used for GAAP** financial reporting; ASC 360 requires systematic allocation of cost (less residual) over useful life. Recovery periods / percentages that do not fall within a reasonable range of useful life are not book depreciation (see also ASC 360-10-35-9 context in chapter). Deferred tax accounting for temporary differences is covered in Chapter 18.

**Key insight:** **Initial recognition** capitalizes the same historical cost for book and tax. Divergence begins with **measurement of periodic depreciation**: statutory MACRS (tax) vs useful-life / residual (GAAP). Only the **GAAP** amount hits the books as Depreciation Expense.

---

### Q2 — CORE number variant — Three-year MACRS twin
**LO:** LO 12-11  
**Concept:** Number-variant twin: initial PPE recognition; MACRS three-year tax schedule vs book SL; period-end book JE; cumulative comparison  
**Scenario:**  
**CedarWorks Tools Inc.** (calendar year) purchases specialized small tooling on **January 1, Year 1** for cash. The tooling is **three-year** MACRS property for tax. CedarWorks does **not** use bonus depreciation. Book policy: straight-line.

| Fact | Amount / term |
|---|---|
| Cash cost | **$48,000** |
| MACRS class (tax) | **Three-year** property |
| Useful life (GAAP) | **6 years** |
| Residual value (GAAP) | **$6,000** |
| Book method | Straight-line |

**MACRS three-year recovery percentages (given):**  
Year 1: 33.33% · Year 2: 44.45% · Year 3: 14.81% · Year 4: 7.41%

**Required:**  
a. Prepare the **initial recognition** journal entry on January 1, Year 1.  
b. Compute annual book depreciation and prepare the **December 31, Year 1** book adjusting JE.  
c. Prepare the **full MACRS tax depreciation schedule** (Years 1–4) with tax basis roll-forward. Round MACRS amounts to the **nearest dollar**.  
d. Prepare a comparison table of tax vs book depreciation for Years 1–6 and total both columns.  
e. State the **tax basis** and **book carrying amount** (cost − accum. dep.) at **December 31, Year 2** (after Year-2 depreciation).

**Answer key:**

**a. Initial recognition**

*January 1, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Specialized Tooling | 48,000 | |
| Cash | | 48,000 |

**Check:** Dr = Cr = 48,000. **Balanced.**

**b. Book depreciation and Year-1 adjusting JE**

\[
\text{Annual SL} = \frac{\$48{,}000 - \$6{,}000}{6} = \mathbf{\$7{,}000}
\]

*December 31, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 7,000 | |
| Accumulated Depreciation—Specialized Tooling | | 7,000 |

**Check:** Dr = Cr = 7,000. **Balanced.**

**c. MACRS three-year tax schedule**

| Year | Beginning tax basis | Rate | MACRS depreciation | Ending tax basis |
|---:|---:|---:|---:|---:|
| 1 | 48,000 | 33.33% | **15,998** | 32,002 |
| 2 | 32,002 | 44.45% | **21,336** | 10,666 |
| 3 | 10,666 | 14.81% | **7,109** | 3,557 |
| 4 | 3,557 | 7.41% | **3,557** | **0** |
| **Total** | | **100.00%** | **48,000** | |

Computations:  
- Y1: $48,000 × 0.3333 = $15,998.40 → **$15,998**  
- Y2: $48,000 × 0.4445 = **$21,336**  
- Y3: $48,000 × 0.1481 = $7,108.80 → **$7,109**  
- Y4: $48,000 × 0.0741 = $3,556.80 → **$3,557** (or plug final year so total = $48,000)  

**Total check:** 15,998 + 21,336 + 7,109 + 3,557 = **48,000**. Ending tax basis **$0**.

**d. Tax vs book comparison**

| Year | MACRS tax | Book SL | Tax − Book |
|---:|---:|---:|---:|
| 1 | 15,998 | 7,000 | 8,998 |
| 2 | 21,336 | 7,000 | 14,336 |
| 3 | 7,109 | 7,000 | 109 |
| 4 | 3,557 | 7,000 | (3,443) |
| 5 | 0 | 7,000 | (7,000) |
| 6 | 0 | 7,000 | (7,000) |
| **Total** | **48,000** | **42,000** | **6,000** |

Difference in totals = GAAP residual **$6,000**.

**e. December 31, Year 2 positions**  
- **Tax basis:** $48,000 − $15,998 − $21,336 = **$10,666**  
- **Book carrying amount:** $48,000 − ($7,000 × 2) = **$34,000**  

Tax basis is **much lower** early because MACRS accelerates deductions and ignores residual.

**Key insight:** Changing the class (3-year vs 5-year) and cost changes the **speed** of tax recovery, but the structural contrast remains: MACRS recovers **100% of cost** for tax; GAAP leaves residual on the books and spreads cost over **useful life**.

---

### Q3 — CORE alternate angle — Multi-year bases, disposal JE, book vs tax gain/loss
**LO:** LO 12-11  
**Concept:** Subsequent book and tax bases after multi-year depreciation; period-end book adjusting JE in year of sale; disposal JE; classification of book vs tax gain/loss  
**Scenario:**  
**Harborline Logistics Co.** (calendar year) acquired a light delivery truck on **January 1, Year 1** for **$60,000** cash. The truck is **five-year** MACRS property for tax (no bonus depreciation). For books: useful life **8 years**, residual **$4,000**, straight-line.

On **December 31, Year 4**, after recording Year-4 book depreciation, Harborline sells the truck for **$28,000** cash.

**MACRS five-year rates:** 20.00%, 32.00%, 19.20%, 11.52%, 11.52%, 5.76%

**Required:**  
a. Prepare the **January 1, Year 1** purchase (initial recognition) JE.  
b. Compute **annual book** depreciation. Prepare the **December 31, Year 4** book depreciation adjusting JE (year of sale, full year).  
c. Prepare a **tax basis roll-forward** for Years 1–4 under MACRS and state tax basis at the sale date.  
d. Compute **book carrying amount** at the sale date and the **book** gain or loss. Prepare the **disposal** journal entry.  
e. Compute the **tax** gain or loss on sale. Briefly reconcile why book and tax gains/losses differ, and show that **net life-to-date pretax effect** (depreciation ± gain/loss) is the same for book and tax through the sale.  
f. **Presentation:** On the Year-4 financial statements, which gain/loss amount is reported—book or tax? Where does MACRS depreciation appear?

**Answer key:**

**a. Initial recognition**

*January 1, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Delivery Truck | 60,000 | |
| Cash | | 60,000 |

**Check:** Dr = Cr = 60,000. **Balanced.**

**b. Book depreciation; Year-4 adjusting JE**

\[
\text{Annual SL} = \frac{\$60{,}000 - \$4{,}000}{8} = \mathbf{\$7{,}000}
\]

*December 31, Year 4 — Book depreciation*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 7,000 | |
| Accumulated Depreciation—Delivery Truck | | 7,000 |

**Check:** Dr = Cr = 7,000. **Balanced.**

Accumulated depreciation after 4 years: $7,000 × 4 = **$28,000**.

**c. MACRS tax basis roll-forward (Years 1–4)**

| Year | MACRS rate | Tax depreciation | Cumulative tax dep. | Tax basis, end |
|---:|---:|---:|---:|---:|
| 1 | 20.00% | 12,000 | 12,000 | 48,000 |
| 2 | 32.00% | 19,200 | 31,200 | 28,800 |
| 3 | 19.20% | 11,520 | 42,720 | 17,280 |
| 4 | 11.52% | 6,912 | **49,632** | **10,368** |

Tax basis at sale (Dec 31, Year 4) = **$10,368**.

**d. Book carrying amount, book gain/loss, disposal JE**

Book carrying amount = $60,000 − $28,000 = **$32,000**  
Cash proceeds = **$28,000**  
**Book loss** = $32,000 − $28,000 = **$4,000**

*December 31, Year 4 — Dispose of truck*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 28,000 | |
| Accumulated Depreciation—Delivery Truck | 28,000 | |
| Loss on Disposal of Equipment | 4,000 | |
| Equipment—Delivery Truck | | 60,000 |

**Check:** Dr 28,000 + 28,000 + 4,000 = 60,000 = Cr 60,000. **Balanced.**

**e. Tax gain/loss and life-to-date reconciliation**

Tax gain = proceeds − tax basis = $28,000 − $10,368 = **$17,632** tax gain  
(Book reported a **$4,000 loss** — different because tax basis is lower after accelerated MACRS.)

**Net effect on pretax income / taxable income through sale date:**

| Item | Tax | Book |
|---|---:|---:|
| Cumulative depreciation (Y1–Y4) | 49,632 | 28,000 |
| Gain (loss) on sale | 17,632 gain | (4,000) loss |
| **Net reduction of income** | 49,632 − 17,632 = **32,000** | 28,000 + 4,000 = **32,000** |

Net reduction equals cost − proceeds: $60,000 − $28,000 = **$32,000**. Timing (and classification between depreciation vs gain/loss) differs; **lifetime net economic effect converges**.

**f. Presentation / classification**  
- Financial statements report the **book** loss of **$4,000** (and book depreciation of **$7,000** in Year 4).  
- **MACRS depreciation and the tax gain** appear on the **tax return** (and in deferred tax / tax footnote analysis), not as the primary book depreciation amount.  
- Temporary differences between book and tax bases give rise to deferred tax accounting (Chapter 18); they are **not** corrected by recording MACRS on the GAAP books.

**Key insight:** At **disposal**, book gain/loss uses **book carrying amount**; tax gain/loss uses **tax basis**. Accelerated MACRS typically produces a **lower tax basis** early on, so a sale can show a **tax gain** even when books show a **loss** (or a larger tax gain than book gain).

---

### Q4 — MC — MACRS vs GAAP classification
**LO:** LO 12-11  
**Concept:** Classification of MACRS as tax-only; residual value and statutory rates vs GAAP useful life  
**Question:**  
Which statement best describes depreciation under the **Internal Revenue Code (MACRS)** relative to **U.S. GAAP**?

- A) MACRS recovery percentages must be used for both the tax return and GAAP financial statements so book and tax depreciation always equal.  
- B) MACRS assigns assets to statutory property classes, applies prescribed recovery percentages (with a half-year convention built into the rates), and **ignores estimated residual value**; GAAP allocates cost less residual over useful life and does **not** use MACRS rates as book depreciation.  
- C) Under MACRS, residual value reduces the depreciable tax base exactly as under GAAP straight-line.  
- D) Total depreciation over an asset’s life is always equal under MACRS and GAAP because both methods depreciate to residual value.

**Answer:** **B.**  
MACRS is a **tax** system: class lives, statutory rates, residual ignored, half-year convention embedded. GAAP uses useful life and residual (expense recognition). A is false (MACRS is not GAAP depreciation). C is false (MACRS ignores residual). D is false (totals differ by residual unless residual is zero; even then patterns differ).

---

### Q5 — MC — Method / measurement choice at initial periods
**LO:** LO 12-11  
**Concept:** Why tax depreciation often exceeds book depreciation in early years; temporary difference driver  
**Question:**  
**Pinecrest Assembly** buys equipment for **$100,000**. GAAP: 10-year life, **$10,000** residual, straight-line. Tax: five-year MACRS (Year-1 rate **20%**), no bonus. In **Year 1**, which is correct?

- A) Book depreciation $10,000; tax depreciation $20,000; books should record tax depreciation of $20,000 to match the IRS.  
- B) Book depreciation $9,000; tax depreciation $20,000; only **$9,000** is recorded as Depreciation Expense on the GAAP books; the higher tax deduction creates a temporary difference (deferred tax effects in Ch. 18).  
- C) Book depreciation $20,000; tax depreciation $9,000 because MACRS is less accelerated than straight-line.  
- D) Book and tax depreciation are both $10,000 because initial recognition cost is $100,000 for both.

**Answer:** **B.**  
Book: \((\$100{,}000 - \$10{,}000)/10 = \$9{,}000\). Tax Year 1: \( \$100{,}000 \times 20\% = \$20{,}000 \). GAAP books record **book** depreciation only. A incorrectly posts tax amount to the books. C reverses the amounts/direction. D confuses equal **cost basis** with equal **periodic** depreciation.

---

### Self-check
- [x] Every JE balances (purchase, book dep., disposal)
- [x] Math recomputed (MACRS rates × cost; SL base; disposal gains/losses; life-to-date net $32,000 check)
- [x] Core demo not sidebar-only (Demo 12-11 / App. 12A MACRS vs GAAP path; disposal used as core book–tax basis angle)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook $10,000 Demo 12-11 figures)
