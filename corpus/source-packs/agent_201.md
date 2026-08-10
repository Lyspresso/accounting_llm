# Agent 201 — CORE DEMO — LO 11-5

**Chapter:** 11  
**LO title:** Account for asset retirement obligations  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Initial recognition JE:** capitalize the **present value** of the ARO by increasing the related long-lived asset and credit **Asset Retirement Obligation** (liability) when a legal obligation exists and fair value is reasonably estimable (ASC 410-20)
- **Measurement of initial ARO:** PV of estimated future dismantling/reclamation cash flows discounted at a rate reflecting the risk of the cash flows (or expected cash flow technique with risk-free rate)
- **Subsequent measurement schedule (emphasis):** ARO liability **accretes** under the **effective interest method** — Accretion expense = beginning-of-period ARO × discount rate; ending ARO rolls forward each period to the undiscounted estimated settlement amount
- **Period-end adjusting JE:** (1) **Depreciation** on carrying amount that includes capitalized ARO cost; (2) **Accretion expense** increasing the ARO liability (operating expense)
- **Settlement / maturity JE:** debit ARO for its carrying amount, credit Cash for actual reclamation cost; difference is **Loss (Gain) on Settlement of ARO**
- **Rationale:** future closure/removal is integral to operating the asset → capitalize to asset rather than expense immediately; passage of time accretes the liability like effective interest

---

### Q1 — CORE — Landfill cell ARO: initial recognition, full accretion schedule, period-end dep + accretion, settlement
**LO:** LO 11-5  
**Concept:** Initial capitalization of ARO at PV into plant asset; full subsequent measurement (accretion) schedule under effective interest; period-end depreciation and accretion adjusting JEs; settlement of ARO with loss  
**Scenario:**  
**Cedar Ridge Landfill LLC** (calendar year-end) completed construction of a **hazardous waste disposal cell** in **December of Year 1**. The cell is placed into service on **January 1, Year 2**. Construction costs of **$8,500,000** (excluding any retirement obligation) have already been recorded. Additional facts:

- Useful life of the cell: **4 years**, straight-line depreciation, **zero** residual value.
- Federal and state regulations require dismantling and site reclamation when the cell is retired.
- Estimated cost to dismantle and reclaim: **$483,153**, with cash outflow expected on **December 31, Year 6** (one year after the end of the cell’s useful life on December 31, Year 5).
- Credit-adjusted risk-free / company discount rate appropriate for the ARO cash flows: **10%**.
- On **December 31, Year 6**, after recording that year’s accretion, Cedar Ridge pays a third-party reclamation firm **$500,000** cash to settle the obligation.

**Required:**  
a. Compute the **present value** of the ARO on December 31, Year 1. Prepare the **initial recognition JE** for the ARO (construction cost already recorded).  
b. Prepare the **full subsequent measurement (accretion) schedule** for the ARO from December 31, Year 1 through December 31, Year 6 (columns: date, beginning ARO, accretion expense at 10%, ending ARO).  
c. Prepare the **December 31, Year 2 period-end adjusting JEs** for (1) depreciation expense and (2) accretion expense.  
d. Prepare the **December 31, Year 6 settlement JE** (assume Year 6 accretion has already been recorded).  
e. Compute **total accretion expense** over the life of the ARO and **total depreciation** of the cell. Briefly explain why the ARO PV is capitalized to the asset rather than expensed immediately.

**Answer key:**  

**a. PV and initial recognition (December 31, Year 1)**

\[
PV = \frac{\$483{,}153}{(1.10)^5} = \frac{\$483{,}153}{1.61051} = \$300{,}000
\]

(Check: \( \$300{,}000 \times (1.10)^5 = \$300{,}000 \times 1.61051 = \$483{,}153 \). Five periods because cash flows occur **one year after** the 4-year useful life ends.)

| Account | Debit | Credit |
|---|---:|---:|
| Building—Hazardous Waste Cell | 300,000 | |
| Asset Retirement Obligation | | 300,000 |
| *Capitalize PV of ARO; recognize ARO liability* | | |

**Check:** Dr 300,000 = Cr 300,000. **Balanced.**  
Carrying amount of cell after ARO = $8,500,000 + $300,000 = **$8,800,000**.

**b. Subsequent measurement schedule — ARO accretion at 10% (emphasis)**

Accretion expense each year = Beginning ARO × **10%**  
Ending ARO = Beginning ARO + Accretion expense

| Date | Beginning ARO | Accretion expense (10%) | Ending ARO |
|---|---:|---:|---:|
| Dec. 31, Year 1 (initial) | — | — | $300,000 |
| Dec. 31, Year 2 | $300,000 | $30,000 | 330,000 |
| Dec. 31, Year 3 | 330,000 | 33,000 | 363,000 |
| Dec. 31, Year 4 | 363,000 | 36,300 | 399,300 |
| Dec. 31, Year 5 | 399,300 | 39,930 | 439,230 |
| Dec. 31, Year 6 | 439,230 | 43,923 | 483,153 |
| **Totals** | | **$183,153** | |

**Schedule checks:**  
- Total accretion = Estimated future cash − Initial PV = $483,153 − $300,000 = **$183,153**  
- Ending ARO at settlement date (after Year 6 accretion) = estimated undiscounted settlement **$483,153**  
- Year 2: $300,000 × 10% = $30,000; Year 3: $330,000 × 10% = $33,000; Year 4: $363,000 × 10% = $36,300; Year 5: $399,300 × 10% = $39,930; Year 6: $439,230 × 10% = $43,923  

**c. Period-end adjusting JEs — December 31, Year 2**

*Depreciation (full capitalized cost ÷ useful life)*

\[
\text{Depreciation} = \frac{\$8{,}500{,}000 + \$300{,}000}{4} = \frac{\$8{,}800{,}000}{4} = \$2{,}200{,}000
\]

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 2,200,000 | |
| Accumulated Depreciation—Hazardous Waste Cell | | 2,200,000 |
| *SL depreciation of cell including capitalized ARO cost* | | |

**Check:** Dr 2,200,000 = Cr 2,200,000. **Balanced.**

*Accretion (effective interest on beginning ARO)*

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 30,000 | |
| Asset Retirement Obligation | | 30,000 |
| *Accrete ARO: $300,000 × 10%* | | |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**  
ARO balance after Year 2 entry = **$330,000**.

**d. Settlement — December 31, Year 6**

ARO carrying amount after Year 6 accretion = **$483,153**  
Cash paid = **$500,000**  
Loss on settlement = $500,000 − $483,153 = **$16,847**

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 483,153 | |
| Loss on Settlement of Asset Retirement Obligation | 16,847 | |
| Cash | | 500,000 |
| *Settle ARO; actual reclamation exceeds accreted liability* | | |

**Check:** Dr 483,153 + 16,847 = 500,000; Cr 500,000. **Balanced.**

**e. Totals and conceptual**  
- Total accretion expense over ARO life = **$183,153** (see schedule totals).  
- Total depreciation of cell = $2,200,000 × 4 = **$8,800,000** (recovers construction + capitalized ARO cost).  
- The obligation for future closure is **integral to operating** the asset, so the PV is **capitalized** to the related long-lived asset (and depreciated) rather than expensed immediately; the liability grows via **accretion expense** (operating) as time passes.

**Key insight:** Initial ARO is recorded at **PV**, not at the undiscounted future cash. The **accretion schedule** is the subsequent measurement engine: each year, beginning ARO × discount rate increases both accretion expense and the liability until the balance equals the estimated settlement amount; settlement then clears the liability against cash, with any difference a gain or loss.

---

### Q2 — CORE number variant — Compressor station ARO: purchase + ARO, 3-year accretion schedule, accruals, settlement with gain
**LO:** LO 11-5  
**Concept:** Number-variant twin: combined purchase and ARO recognition; full subsequent accretion schedule (effective interest); period-end depreciation and accretion JEs; settlement of ARO with gain when cash paid is less than accreted liability  
**Scenario:**  
**Boreal Pipeline Services Inc.** (calendar year-end) installs a **compressor station** on **January 1, Year 1** and places it in service the same day. Facts:

- Cash construction / acquisition cost (excluding ARO): **$2,600,000**.
- Useful life: **3 years**, straight-line, **zero** residual value.
- Legal obligation to dismantle and restore the site at the end of the station’s useful life; estimated cash outflow on **December 31, Year 3**: **$532,400**.
- Discount rate: **10%**.
- On December 31, Year 3, after recording Year 3 accretion, Boreal settles the obligation by paying **$510,000** cash to a reclamation contractor.

**Required:**  
a. Compute the PV of the ARO and the **initial cost** of the compressor station. Prepare the **January 1, Year 1** journal entry to record the purchase and ARO.  
b. Prepare the **3-year subsequent measurement (accretion) schedule**.  
c. Prepare the **December 31, Year 1** period-end adjusting JEs for depreciation and accretion.  
d. Prepare the **December 31, Year 2** accretion JE only (depreciation pattern is the same each year).  
e. Prepare the **December 31, Year 3** accretion JE and the **settlement JE**.  
f. State the **balance sheet presentation** of the ARO at December 31, Year 1 (after Year 1 accretion).

**Answer key:**  

**a. PV, asset cost, initial JE**

\[
PV = \frac{\$532{,}400}{(1.10)^3} = \frac{\$532{,}400}{1.331} = \$400{,}000
\]

(Check: \( \$400{,}000 \times 1.10^3 = \$400{,}000 \times 1.331 = \$532{,}400 \).)

Initial cost of compressor station = $2,600,000 + $400,000 = **$3,000,000**

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Compressor Station | 3,000,000 | |
| Cash | | 2,600,000 |
| Asset Retirement Obligation | | 400,000 |
| *Record station cost + capitalize PV of ARO* | | |

**Check:** Dr 3,000,000 = Cr 2,600,000 + 400,000. **Balanced.**

**b. Subsequent measurement schedule — ARO accretion at 10% (emphasis)**

| Date | Beginning ARO | Accretion expense (10%) | Ending ARO |
|---|---:|---:|---:|
| Jan. 1, Year 1 | — | — | $400,000 |
| Dec. 31, Year 1 | $400,000 | $40,000 | 440,000 |
| Dec. 31, Year 2 | 440,000 | 44,000 | 484,000 |
| Dec. 31, Year 3 | 484,000 | 48,400 | 532,400 |
| **Totals** | | **$132,400** | |

**Schedule checks:** Total accretion = $532,400 − $400,000 = **$132,400**; ending ARO at settlement date = **$532,400**.

**c. December 31, Year 1 — period-end adjusting JEs**

Depreciation = $3,000,000 / 3 = **$1,000,000**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 1,000,000 | |
| Accumulated Depreciation—Compressor Station | | 1,000,000 |
| *SL depreciation including capitalized ARO cost* | | |

**Check:** Dr 1,000,000 = Cr 1,000,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 40,000 | |
| Asset Retirement Obligation | | 40,000 |
| *Accrete ARO: $400,000 × 10%* | | |

**Check:** Dr 40,000 = Cr 40,000. **Balanced.**

**d. December 31, Year 2 — accretion**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 44,000 | |
| Asset Retirement Obligation | | 44,000 |
| *Accrete ARO: $440,000 × 10%* | | |

**Check:** Dr 44,000 = Cr 44,000. **Balanced.**  
ARO after Year 2 = **$484,000**.

**e. December 31, Year 3 — accretion and settlement**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 48,400 | |
| Asset Retirement Obligation | | 48,400 |
| *Accrete ARO: $484,000 × 10%* | | |

**Check:** Dr 48,400 = Cr 48,400. **Balanced.**  
ARO after Year 3 accretion = **$532,400**.

Gain on settlement = $532,400 − $510,000 = **$22,400**

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 532,400 | |
| Cash | | 510,000 |
| Gain on Settlement of Asset Retirement Obligation | | 22,400 |
| *Settle ARO; actual cost less than accreted liability* | | |

**Check:** Dr 532,400 = Cr 510,000 + 22,400. **Balanced.**

**f. Balance sheet at December 31, Year 1**  
Asset Retirement Obligation (liability) = **$440,000** (typically noncurrent if settlement is more than one year away; here remaining term is 2 years — still noncurrent at YE1 if not due within the next year). Net PPE includes Equipment $3,000,000 less Accumulated Depreciation $1,000,000 = **$2,000,000**.

**Key insight:** Same core engine as Q1 with all new numbers: **PV at inception**, **accretion schedule** rolls the liability to the estimated future cash, depreciation is based on **construction cost + ARO PV**, and settlement compares cash paid to the **accreted** ARO balance (not to the original PV).

---

### Q3 — CORE alternate angle — Storage tank: combined recognition, multi-year accretion schedule only, period-end pair, settlement
**LO:** LO 11-5  
**Concept:** Alternate angle — purchase and ARO on same date; emphasis on multi-period accretion schedule and year-end dep + accretion pair; settlement when cash equals estimated FV (no gain/loss)  
**Scenario:**  
**Ironwood Refining Corp.** (calendar year-end) purchases and installs an **underground product storage tank** on **January 1, Year 1** for **$1,100,000 cash**. The tank has a **4-year** useful life, straight-line, no residual. Environmental regulations require removal and site restoration at the end of Year 4; estimated cost **$146,410** payable **December 31, Year 4**. Discount rate **10%**. Ironwood settles the ARO on December 31, Year 4 by paying exactly **$146,410** cash (after Year 4 accretion).

**Required:**  
a. Compute PV of the ARO. Record the **January 1, Year 1** combined purchase and ARO JE.  
b. Prepare the **full 4-year accretion subsequent measurement schedule**.  
c. Record **only the December 31, Year 1 period-end adjusting JEs** (depreciation and accretion).  
d. Record the **December 31, Year 4 settlement JE** (Year 4 accretion already recorded).  
e. Without preparing every year-end JE, compute **total accretion expense** and **total depreciation expense** over the 4-year life.

**Answer key:**  

**a. PV and January 1, Year 1 JE**

\[
PV = \frac{\$146{,}410}{(1.10)^4} = \frac{\$146{,}410}{1.4641} = \$100{,}000
\]

(Check: \( \$100{,}000 \times 1.10^4 = \$100{,}000 \times 1.4641 = \$146{,}410 \).)

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Storage Tank | 1,200,000 | |
| Cash | | 1,100,000 |
| Asset Retirement Obligation | | 100,000 |
| *Tank cost $1,100,000 + ARO PV $100,000* | | |

**Check:** Dr 1,200,000 = Cr 1,100,000 + 100,000. **Balanced.**

**b. Subsequent measurement schedule — accretion at 10% (emphasis)**

| Date | Beginning ARO | Accretion expense (10%) | Ending ARO |
|---|---:|---:|---:|
| Jan. 1, Year 1 | — | — | $100,000 |
| Dec. 31, Year 1 | $100,000 | $10,000 | 110,000 |
| Dec. 31, Year 2 | 110,000 | 11,000 | 121,000 |
| Dec. 31, Year 3 | 121,000 | 12,100 | 133,100 |
| Dec. 31, Year 4 | 133,100 | 13,310 | 146,410 |
| **Totals** | | **$46,410** | |

**Schedule checks:** Total accretion = $146,410 − $100,000 = **$46,410**; terminal ARO = estimated settlement cash **$146,410**.

**c. December 31, Year 1 period-end adjusting JEs**

Depreciation = $1,200,000 / 4 = **$300,000**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 300,000 | |
| Accumulated Depreciation—Storage Tank | | 300,000 |
| *SL depreciation of tank including ARO cost* | | |

**Check:** Dr 300,000 = Cr 300,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 10,000 | |
| Asset Retirement Obligation | | 10,000 |
| *Accrete ARO: $100,000 × 10%* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.**

**d. Settlement — December 31, Year 4**

Cash paid = accreted ARO = **$146,410** → **no gain or loss**

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 146,410 | |
| Cash | | 146,410 |
| *Settle ARO at amount equal to accreted liability* | | |

**Check:** Dr 146,410 = Cr 146,410. **Balanced.**

**e. Life-cycle totals**  
- Total accretion expense = **$46,410**  
- Total depreciation expense = $300,000 × 4 = **$1,200,000**  
Combined income-statement charges related to the retirement layer over life = accretion $46,410 + depreciation of ARO cost $100,000 = **$146,410**, which equals the cash ultimately paid for reclamation when there is no settlement gain or loss.

**Key insight:** Over the full life, if actual cash equals the original estimate, the sum of **(1) depreciation of the capitalized ARO cost** and **(2) all accretion expense** equals the cash paid for reclamation. The schedule allocates the financing-like accretion through time; depreciation allocates the capitalized retirement cost to the periods the asset is used.

---

### Q4 — MC (classification / measurement)
**LO:** LO 11-5  
**Concept:** Classification and measurement — equipment cost includes PV of ARO (not undiscounted future cash); accretion increases the ARO liability and is an operating expense  

**Question 1:**  
**Summit Quarry Co.** purchases equipment on January 1 of the current year for **$680,000** cash. Summit has a legal asset retirement obligation related to the equipment. Estimated reclamation cost in **4 years** is **$146,410**. The appropriate discount rate is **10%**. (PV of $1 due in 4 periods at 10% = **0.6830**.) What amount should Summit report as the **cost of the equipment** on January 1?

- A) $680,000  
- B) $826,410  
- C) $780,000  
- D) $533,590  

**Answer:** C.  
PV of ARO = $146,410 × 0.6830 = **$100,000** (equivalently \( \$146{,}410 / 1.4641 = \$100{,}000 \)).  
Equipment cost = cash paid + PV of ARO = $680,000 + $100,000 = **$780,000**.  
(A) omits the ARO. (B) adds the **undiscounted** future cash (overstates the asset). (D) subtracts PV from cash (wrong direction).

---

**Question 2:**  
Referring to the same facts as Question 1, **accretion expense** for the year ended December 31 of the current year is:

- A) $14,641  
- B) $10,000  
- C) $0 (accretion begins only in the year of settlement)  
- D) $11,641  

**Answer:** B.  
Initial ARO = **$100,000**.  
Accretion expense Year 1 = $100,000 × 10% = **$10,000**.  
Debit Accretion Expense (operating); credit **Asset Retirement Obligation**. Accretion is recognized **each period** for the passage of time under the effective interest method, not only at settlement.  
(A) is $146,410 × 10% (wrong base — uses future cash, not beginning ARO). (D) is ($146,410 − $100,000) / 4 (straight-line accretion is **not** the method used for AROs).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV factors, accretion rollforwards, dep = cost÷life, settlement G/L)
- [x] Core demo not sidebar-only (Demo 11-5 / Review 11-5 path: recognize → depreciate + accrete → settle)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/measurement items)
- [x] Emphasis on subsequent_measurement_schedule (full accretion schedules in Q1–Q3)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Original company names and amounts (not textbook Lakeside / BPP numbers)
