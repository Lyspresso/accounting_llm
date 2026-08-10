# Agent 332 — CORE DEMO — LO 11-5

**Chapter:** 11  
**LO title:** Account for asset retirement obligations  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Asset retirement obligation (ARO):** legal obligation (law, regulation, or contract) to dismantle, remove, decommission, close, or reclaim a tangible long-lived asset at the end of its useful life
- **Initial recognition:** capitalize the **present value** of estimated future retirement costs by **increasing the carrying amount of the related PPE** and recognizing a **corresponding ARO liability** when the obligation is incurred and reasonably estimable (ASC 410-20)
- **Depreciation:** depreciate the **full asset cost including capitalized ARO** over the asset’s useful life
- **Accretion (subsequent measurement):** increase the ARO liability each period using the **effective interest method** (beginning liability × credit-adjusted rate); charge **accretion expense** (an **operating** expense)
- **Period-end adjusting JEs (emphasis):** at each reporting date, record (1) depreciation on the asset inclusive of ARO cost and (2) accretion of the ARO liability
- **Settlement / disposal:** when retirement work is completed, **derecognize the ARO liability** against cash (and residual PPE/AD as applicable); difference between cash spent and carrying amount of the liability is a **gain or loss on settlement of ARO**

---

### Q1 — CORE — Initial ARO capitalization, multi-year accretion schedule, period-end dep/accretion, settlement with loss

**LO:** LO 11-5  
**Concept:** Initial recognition of ARO PV into PPE; subsequent accretion schedule; period-end adjusting JEs for depreciation and accretion (emphasis); settlement of ARO with loss  
**Scenario:**  
**Ridgeway Landfill Partners**, a calendar-year company, places a new **leachate treatment facility** into service on **January 1, Year 1**. Construction cost (excluding retirement costs) is **$3,500,000**, paid in cash. Federal and state regulations require the company to cap the facility and reclaim the site at the end of the facility’s life.

Additional facts:
- Estimated cash outlay for capping and reclamation: **$1,200,000**, expected on **December 31, Year 10** (end of useful life; end-of-year cash flow).
- Credit-adjusted risk-free discount rate reflecting the risk of the cash flows: **6%**.
- Useful life: **10 years**, straight-line, **zero residual value**.
- On **December 31, Year 10**, after recording Year 10 accretion, Ridgeway completes the reclamation work and pays **$1,250,000** cash.
- The facility’s cost and related accumulated depreciation are removed in a separate PPE disposal entry (not required here); focus is on the **ARO**.

**Required:**  
(a) Compute the present value of the ARO and record the **January 1, Year 1** journal entries for (1) the facility purchase and (2) **initial recognition of the ARO**.  
(b) Prepare a complete **subsequent measurement (accretion) schedule** for Years 1–10 (beginning ARO, accretion expense, ending ARO). Plug the final year so the liability equals the estimated future cost of **$1,200,000**.  
(c) Record the **December 31, Year 1 period-end adjusting entries** for depreciation and accretion (**emphasis**).  
(d) Record the **December 31, Year 2 period-end adjusting entries** for depreciation and accretion.  
(e) Record the **December 31, Year 10** settlement of the ARO for **$1,250,000** (Year 10 accretion already recorded). Compute the gain or loss.

**Answer key:**

**(a) Present value and initial recognition — January 1, Year 1**

\[
PV = \frac{\$1{,}200{,}000}{(1.06)^{10}} = \$670{,}073.73
\]

Excel-style check: `=PV(0.06,10,0,-1200000)` → **$670,073.73**.

Total depreciable cost of facility = \(3{,}500{,}000 + 670{,}073.73 =\) **$4,170,073.73**.

(1) Facility acquisition:

| Account | Debit | Credit |
|---|---:|---:|
| Leachate Treatment Facility | 3,500,000.00 | |
| Cash | | 3,500,000.00 |
| *Record construction cost of facility* | | |

**Check:** Dr 3,500,000.00 = Cr 3,500,000.00. **Balanced.**

(2) Initial recognition of ARO:

| Account | Debit | Credit |
|---|---:|---:|
| Leachate Treatment Facility | 670,073.73 | |
| Asset Retirement Obligation | | 670,073.73 |
| *Capitalize PV of ARO; establish ARO liability* | | |

**Check:** Dr 670,073.73 = Cr 670,073.73. **Balanced.**

**(b) Subsequent measurement — ARO accretion schedule (6% effective interest)**

Accretion each year = beginning ARO × 6% (rounded to nearest cent). Year 10 accretion is **plugged** so ending balance equals the estimated retirement cost of **$1,200,000**.

| Year | Beginning ARO | Accretion expense (× 6%) | Ending ARO |
|---:|---:|---:|---:|
| 1 | 670,073.73 | 40,204.42 | 710,278.15 |
| 2 | 710,278.15 | 42,616.69 | 752,894.84 |
| 3 | 752,894.84 | 45,173.69 | 798,068.53 |
| 4 | 798,068.53 | 47,884.11 | 845,952.64 |
| 5 | 845,952.64 | 50,757.16 | 896,709.80 |
| 6 | 896,709.80 | 53,802.59 | 950,512.39 |
| 7 | 950,512.39 | 57,030.74 | 1,007,543.13 |
| 8 | 1,007,543.13 | 60,452.59 | 1,067,995.72 |
| 9 | 1,067,995.72 | 64,079.74 | 1,132,075.46 |
| 10 | 1,132,075.46 | **67,924.54** (plug) | **1,200,000.00** |
| **Totals** | | **529,926.27** | |

**Rollforward check:** \(670{,}073.73 + 529{,}926.27 = 1{,}200{,}000.00\). **OK.**

**(c) December 31, Year 1 — period-end adjusting JEs (emphasis)**

Annual depreciation (Years 1–9):  
\[
\frac{\$4{,}170{,}073.73}{10} = \$417{,}007.37
\]
(Year 10 depreciation will be **$417,007.40** so that total AD = **$4,170,073.73**; residual **$0.03**.)

Depreciation:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 417,007.37 | |
| Accumulated Depreciation—Leachate Treatment Facility | | 417,007.37 |
| *SL depreciation on facility cost including capitalized ARO* | | |

**Check:** Dr 417,007.37 = Cr 417,007.37. **Balanced.**

Accretion (from schedule Year 1):

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 40,204.42 | |
| Asset Retirement Obligation | | 40,204.42 |
| *Effective-interest accretion of ARO (670,073.73 × 6%)* | | |

**Check:** Dr 40,204.42 = Cr 40,204.42. **Balanced.**

After Year 1 adjustments:  
Facility (gross) **$4,170,073.73**; AD **$417,007.37**; net book value **$3,753,066.36**.  
ARO liability **$710,278.15**.

**(d) December 31, Year 2 — period-end adjusting JEs**

Depreciation:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 417,007.37 | |
| Accumulated Depreciation—Leachate Treatment Facility | | 417,007.37 |
| *Year 2 SL depreciation* | | |

**Check:** Dr 417,007.37 = Cr 417,007.37. **Balanced.**

Accretion (Year 2: \(710{,}278.15 \times 6\% = 42{,}616.69\)):

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 42,616.69 | |
| Asset Retirement Obligation | | 42,616.69 |
| *Year 2 accretion of ARO* | | |

**Check:** Dr 42,616.69 = Cr 42,616.69. **Balanced.**

Ending ARO at Dec 31, Year 2: **$752,894.84**.

**(e) December 31, Year 10 — settlement of ARO (after Year 10 accretion)**

After Year 10 accretion, ARO carrying amount = **$1,200,000**. Cash paid = **$1,250,000**.

Loss on settlement = \(1{,}250{,}000 - 1{,}200{,}000 =\) **$50,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 1,200,000.00 | |
| Loss on Settlement of ARO | 50,000.00 | |
| Cash | | 1,250,000.00 |
| *Settle ARO; excess cash outlay is a loss* | | |

**Check:** Dr 1,250,000.00 = Cr 1,250,000.00. **Balanced.**

**Key insight:** The ARO is **not** expensed when incurred; its PV is **capitalized into the asset** and recovered through **depreciation**, while the liability **grows over time through accretion**. At settlement, only the difference between cash paid and the **fully accreted** liability is gain or loss—not the entire retirement cash outlay.

---

### Q2 — CORE number variant — Initial ARO, accretion schedule, period-end adjustments, settlement with gain

**LO:** LO 11-5  
**Concept:** Number-variant twin — PV capitalization of ARO; multi-year accretion schedule; period-end dep and accretion; settlement of ARO with **gain**  
**Scenario:**  
**Copper Basin Mining Co.**, a calendar-year firm, places a **primary ore crusher and related site works** into service on **January 1, Year 1**. Cash cost excluding retirement obligations is **$2,150,000**. State mining reclamation rules require dismantling and site restoration at the end of the asset’s life.

Additional facts:
- Estimated restoration cost: **$750,000** on **December 31, Year 8**.
- Discount rate: **5%**.
- Useful life: **8 years**, straight-line, **zero residual value**.
- On **December 31, Year 8**, after recording Year 8 accretion, Copper Basin completes restoration and pays only **$720,000** cash (work came in under budget).

**Required:**  
(a) Compute PV of the ARO and record **January 1, Year 1** entries for the asset purchase and initial ARO recognition.  
(b) Prepare the **Years 1–8 accretion schedule** (plug Year 8 so ending ARO = **$750,000**).  
(c) Record **December 31, Year 1** period-end adjusting entries (depreciation and accretion).  
(d) Record **December 31, Year 8** settlement of the ARO for **$720,000** (Year 8 accretion already recorded).

**Answer key:**

**(a) PV and initial recognition — January 1, Year 1**

\[
PV = \frac{\$750{,}000}{(1.05)^{8}} = \$507{,}629.52
\]

Total depreciable cost = \(2{,}150{,}000 + 507{,}629.52 =\) **$2,657,629.52**.  
Annual depreciation = \(2{,}657{,}629.52 / 8 =\) **$332,203.69**.

(1) Purchase:

| Account | Debit | Credit |
|---|---:|---:|
| Ore Crusher & Site Works | 2,150,000.00 | |
| Cash | | 2,150,000.00 |
| *Record cash acquisition cost* | | |

**Check:** Dr 2,150,000.00 = Cr 2,150,000.00. **Balanced.**

(2) ARO capitalization:

| Account | Debit | Credit |
|---|---:|---:|
| Ore Crusher & Site Works | 507,629.52 | |
| Asset Retirement Obligation | | 507,629.52 |
| *Capitalize PV of reclamation ARO* | | |

**Check:** Dr 507,629.52 = Cr 507,629.52. **Balanced.**

**(b) Accretion schedule (5%)**

| Year | Beginning ARO | Accretion (× 5%) | Ending ARO |
|---:|---:|---:|---:|
| 1 | 507,629.52 | 25,381.48 | 533,011.00 |
| 2 | 533,011.00 | 26,650.55 | 559,661.55 |
| 3 | 559,661.55 | 27,983.08 | 587,644.63 |
| 4 | 587,644.63 | 29,382.23 | 617,026.86 |
| 5 | 617,026.86 | 30,851.34 | 647,878.20 |
| 6 | 647,878.20 | 32,393.91 | 680,272.11 |
| 7 | 680,272.11 | 34,013.61 | 714,285.72 |
| 8 | 714,285.72 | **35,714.28** (plug) | **750,000.00** |
| **Totals** | | **242,370.48** | |

**Rollforward check:** \(507{,}629.52 + 242{,}370.48 = 750{,}000.00\). **OK.**

**(c) December 31, Year 1 — period-end adjusting JEs**

Depreciation:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 332,203.69 | |
| Accumulated Depreciation—Ore Crusher & Site Works | | 332,203.69 |
| *SL dep on cost including ARO* | | |

**Check:** Dr 332,203.69 = Cr 332,203.69. **Balanced.**

Accretion:

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 25,381.48 | |
| Asset Retirement Obligation | | 25,381.48 |
| *507,629.52 × 5%* | | |

**Check:** Dr 25,381.48 = Cr 25,381.48. **Balanced.**

**(d) December 31, Year 8 — settlement with gain**

ARO after Year 8 accretion = **$750,000**. Cash paid = **$720,000**.  
Gain on settlement = \(750{,}000 - 720{,}000 =\) **$30,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 750,000.00 | |
| Cash | | 720,000.00 |
| Gain on Settlement of ARO | | 30,000.00 |
| *Settle ARO under budget; recognize gain* | | |

**Check:** Dr 750,000.00 = Cr 750,000.00. **Balanced.**

**Key insight:** A settlement **gain** arises when actual retirement costs are **less** than the **accreted carrying amount** of the ARO—not when actual costs are less than the **undiscounted** original estimate alone (the liability already grew to that estimate via accretion).

---

### Q3 — CORE alternate angle — Period-end adjusting JE emphasis (multi-year dep + accretion; partial life cycle)

**LO:** LO 11-5  
**Concept:** Period-end adjusting JE emphasis — given capitalized ARO already on books, recompute multi-year accretion and record each year-end depreciation and accretion; year-5 settlement with loss  
**Scenario:**  
**Saltline Storage LLC** installed underground **petroleum storage tanks** on **January 1, Year 1**. The tanks’ cash cost of **$480,000** and the related ARO have **already been recorded**. You are preparing **year-end adjusting entries only**.

Given balances at **January 1, Year 1** (after initial recognition):
- Storage Tanks (gross, includes ARO cost): **$622,597.24**
- Asset Retirement Obligation: **$142,597.24**  
  (equals \(200{,}000 / (1.07)^{5}\); estimated reclamation cost **$200,000** due **December 31, Year 5**; rate **7%**)
- Accumulated Depreciation: **$0**
- Useful life: **5 years**, straight-line, zero residual
- Policy: record depreciation and accretion only as **December 31 period-end adjusting entries**

Additional facts:
- No change in estimated retirement cash flows or discount rate during the five years.
- On **December 31, Year 5**, after the Year 5 adjusting entries, Saltline pays **$208,000** cash to complete tank removal and site restoration.

**Required:**  
(a) Verify the initial PV of **$142,597.24** and the depreciable base. Compute annual depreciation (with final-year plug if needed).  
(b) Prepare a **Years 1–5 accretion schedule** (plug Year 5 to **$200,000**).  
(c) Record the **period-end adjusting entries** for **December 31, Year 1**, **Year 2**, and **Year 3** (depreciation + accretion each year) — **emphasis**.  
(d) State the ARO balance and net book value of the tanks after the **December 31, Year 3** adjustments.  
(e) Record the **December 31, Year 5** settlement entry for **$208,000** (Year 5 accretion already recorded).

**Answer key:**

**(a) PV verification and depreciation**

\[
PV = \frac{\$200{,}000}{(1.07)^{5}} = \$142{,}597.24 \quad \checkmark
\]

Depreciable base = **$622,597.24**.  
Annual depreciation (Years 1–4): \(622{,}597.24 / 5 = 124{,}519.448\) → **$124,519.45**.  
Sum of four years = \(4 \times 124{,}519.45 = 498{,}077.80\).  
Year 5 depreciation plug = \(622{,}597.24 - 498{,}077.80 =\) **$124,519.44**.

**(b) Accretion schedule (7%)**

| Year | Beginning ARO | Accretion (× 7%) | Ending ARO |
|---:|---:|---:|---:|
| 1 | 142,597.24 | 9,981.81 | 152,579.05 |
| 2 | 152,579.05 | 10,680.53 | 163,259.58 |
| 3 | 163,259.58 | 11,428.17 | 174,687.75 |
| 4 | 174,687.75 | 12,228.14 | 186,915.89 |
| 5 | 186,915.89 | **13,084.11** (plug) | **200,000.00** |
| **Totals** | | **57,402.76** | |

**Rollforward check:** \(142{,}597.24 + 57{,}402.76 = 200{,}000.00\). **OK.**

**(c) Period-end adjusting JEs — emphasis**

**December 31, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 124,519.45 | |
| Accumulated Depreciation—Storage Tanks | | 124,519.45 |
| *Year 1 SL depreciation* | | |

**Check:** Dr 124,519.45 = Cr 124,519.45. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 9,981.81 | |
| Asset Retirement Obligation | | 9,981.81 |
| *142,597.24 × 7%* | | |

**Check:** Dr 9,981.81 = Cr 9,981.81. **Balanced.**

**December 31, Year 2**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 124,519.45 | |
| Accumulated Depreciation—Storage Tanks | | 124,519.45 |

**Check:** Dr 124,519.45 = Cr 124,519.45. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 10,680.53 | |
| Asset Retirement Obligation | | 10,680.53 |
| *152,579.05 × 7%* | | |

**Check:** Dr 10,680.53 = Cr 10,680.53. **Balanced.**

**December 31, Year 3**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 124,519.45 | |
| Accumulated Depreciation—Storage Tanks | | 124,519.45 |

**Check:** Dr 124,519.45 = Cr 124,519.45. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 11,428.17 | |
| Asset Retirement Obligation | | 11,428.17 |
| *163,259.58 × 7%* | | |

**Check:** Dr 11,428.17 = Cr 11,428.17. **Balanced.**

**(d) Balances after December 31, Year 3 adjustments**

| Item | Amount |
|---|---:|
| Storage Tanks (gross) | 622,597.24 |
| Accumulated Depreciation (\(3 \times 124{,}519.45\)) | (373,558.35) |
| **Net book value** | **249,038.89** |
| **ARO liability** | **174,687.75** |

**(e) December 31, Year 5 — settlement with loss**

ARO after Year 5 accretion = **$200,000**. Cash paid = **$208,000**.  
Loss = \(208{,}000 - 200{,}000 =\) **$8,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 200,000.00 | |
| Loss on Settlement of ARO | 8,000.00 | |
| Cash | | 208,000.00 |
| *Settle ARO; excess cost is a loss* | | |

**Check:** Dr 208,000.00 = Cr 208,000.00. **Balanced.**

**Key insight (emphasis):** Even when initial recognition is already on the books, every period-end still requires **two** ARO-related adjusting entries—**depreciation** (on the asset that includes ARO cost) and **accretion** (to grow the liability). Omitting either understates expense and misstates assets/liabilities.

---

### Q4 — MC (classification / measurement method)

**LO:** LO 11-5  
**Concept:** Classification of accretion expense; measurement of equipment cost when an ARO exists  

**Question 1:**  
Under U.S. GAAP (ASC 410-20), how is **accretion expense** on an asset retirement obligation classified on the income statement?

- A) Interest expense (nonoperating financing cost)  
- B) **Operating expense** (accretion of the ARO liability)  
- C) Other comprehensive income (never hits net income)  
- D) Capitalized as additional PPE each period  

**Answer:** **B.** Accretion increases the ARO liability under the effective interest method; the corresponding charge is **accretion expense**, classified as an **operating expense**. It is **not** the same presentation as contractual interest on notes payable, and it is **not** capitalized into PPE after initial recognition of the ARO cost.

---

**Question 2:**  
**North Pier Logistics** purchases specialized dock equipment on January 1 for a cash price of **$900,000**. Environmental rules require removal of the equipment and dock restoration in **6 years** at an estimated cost of **$180,000**. North Pier’s credit-adjusted discount rate is **8%**. What total amount is reported as **equipment** on January 1 immediately after purchase and ARO recognition?

- A) $900,000  
- B) $1,080,000  
- C) **$1,013,430.53**  
- D) $780,000  

**Computation:**  
\[
PV(\text{ARO}) = \frac{\$180{,}000}{(1.08)^{6}} = \$113{,}430.53
\]  
Equipment total = \(900{,}000 + 113{,}430.53 =\) **$1,013,430.53**.

**Answer:** **C.** Equipment includes the cash purchase price **plus** the capitalized present value of the ARO—not the undiscounted future retirement cost (**B**) and not the cash price alone (**A**).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV factors, accretion rollforwards to estimated FV, dep residual plugs)
- [x] Core demo path (Demo 11-5 / Review 11-5 style: capitalize PV → depreciate → accrete → settle)—not sidebar-only
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/measurement MCs)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Lakeside / BPP demo figures)
