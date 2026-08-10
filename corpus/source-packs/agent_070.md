# Agent 70 — CORE DEMO — LO 11-5

**Chapter:** 11  
**LO title:** Account for asset retirement obligations  
**Critical gap LO:** no

## Concept list for this pack
- **Initial recognition JE:** capitalize PV of ARO into related PPE; credit Asset Retirement Obligation (legal obligation, reasonably estimable)
- PV measurement: discount estimated future retirement cash flows at a credit-adjusted rate reflecting risk of the cash flows (effective interest)
- **Subsequent measurement / accretion schedule:** effective interest method increases ARO liability each period
- **Period-end adjusting JE:** (1) depreciation on PPE **including** capitalized asset retirement cost; (2) accretion expense → ARO
- **Settlement JE:** remove ARO at carrying amount; difference vs actual cash → gain or loss on settlement
- Classification/presentation: ARO liability (typically noncurrent until near settlement); accretion expense is an **operating** expense; asset retirement cost depreciated through PPE

---

### Q1 — CORE — Full ARO life cycle (emphasis: initial recognition)
**LO:** LO 11-5  
**Concept:** Initial recognition of ARO (PV capitalized to PPE); Year-1 depreciation and accretion; multi-year accretion schedule; settlement with loss  
**Scenario:**  
**SummitChem Industries**, a calendar-year company, places a new hazardous-waste processing plant into service on **January 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Cash construction cost (excluding retirement costs) | **$120,000,000** |
| Useful life | **10 years**, straight-line, **zero** residual value |
| Legal obligation (regulation) | Dismantle plant and reclaim site at end of useful life |
| Estimated future dismantling / reclamation cost | **$15,000,000** (cash outflow expected **December 31, Year 10**) |
| Appropriate discount rate | **9%** |

**Required:**  
a. Compute the **present value** of the ARO on January 1, Year 1. Prepare the **combined** journal entry to record the plant purchase (cash) **and** the **initial recognition** of the asset retirement obligation.  
b. Prepare the **December 31, Year 1** adjusting entries for (1) **depreciation** and (2) **accretion**.  
c. Prepare a complete **ARO accretion schedule** for Years 1–10 (beginning balance, accretion expense, ending balance). Confirm ending balance equals the estimated future cost.  
d. On **December 31, Year 10**, after recording Year-10 accretion, SummitChem settles the obligation by paying a reclamation contractor **$15,800,000** cash. Prepare the **settlement** journal entry.  
e. Briefly state how the ARO and related asset cost appear on the **balance sheet** just after initial recognition (January 1, Year 1).

**Answer key:**  

**a. PV and initial recognition**

\[
PV = \frac{\$15{,}000{,}000}{(1.09)^{10}} = \$6{,}336{,}162
\]

(Excel-style: `PV(0.09,10,0,-15000000)` → **$6,336,162**.)

Capitalized plant cost = cash construction + PV of ARO  
= $120,000,000 + $6,336,162 = **$126,336,162**

*January 1, Year 1 — Purchase plant and record ARO (initial recognition)*  

| Account | Debit | Credit |
|---|---:|---:|
| Building—Waste Processing Plant | 126,336,162 | |
| Cash | | 120,000,000 |
| Asset Retirement Obligation | | 6,336,162 |
| *Capitalize PV of ARO into related long-lived asset; establish ARO liability* | | |

**Check:** Dr 126,336,162 = Cr 120,000,000 + 6,336,162. **Balanced.**

(If construction cost was already recorded, the ARO-only entry is Dr Building 6,336,162 / Cr ARO 6,336,162 — same PV amount.)

**b. December 31, Year 1 adjusting entries**

Annual depreciation (SL, no residual):  
\((\$120{,}000{,}000 + \$6{,}336{,}162) / 10 = \$12{,}633{,}616\) (rounded to nearest dollar).

*December 31, Year 1 — Depreciation (includes capitalized asset retirement cost)*  

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 12,633,616 | |
| Accumulated Depreciation—Waste Processing Plant | | 12,633,616 |

**Check:** Dr = Cr = 12,633,616.

Accretion (effective interest on **beginning** ARO):  
\$6,336,162 × 9% = **\$570,255**

*December 31, Year 1 — Accretion of ARO*  

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 570,255 | |
| Asset Retirement Obligation | | 570,255 |

**Check:** Dr = Cr = 570,255.

Ending ARO, December 31, Year 1: \$6,336,162 + \$570,255 = **\$6,906,417**

**c. ARO accretion schedule (effective interest @ 9%)**

Final-year accretion plugs so the liability equals the estimated future cost of **\$15,000,000** (avoids cumulative \$1 rounding drift).

| Year | Beginning ARO | Accretion expense (9%) | Ending ARO |
|---:|---:|---:|---:|
| 1 | 6,336,162 | 570,255 | 6,906,417 |
| 2 | 6,906,417 | 621,578 | 7,527,995 |
| 3 | 7,527,995 | 677,520 | 8,205,515 |
| 4 | 8,205,515 | 738,496 | 8,944,011 |
| 5 | 8,944,011 | 804,961 | 9,748,972 |
| 6 | 9,748,972 | 877,407 | 10,626,379 |
| 7 | 10,626,379 | 956,374 | 11,582,753 |
| 8 | 11,582,753 | 1,042,448 | 12,625,201 |
| 9 | 12,625,201 | 1,136,268 | 13,761,469 |
| 10 | 13,761,469 | 1,238,531 | **15,000,000** |
| **Total** | | **8,663,838** | |

**Roll-forward check:** PV + total accretion = \$6,336,162 + \$8,663,838 = **\$15,000,000** = estimated future cost.

**d. Settlement (after Year-10 accretion already recorded)**

ARO carrying amount = **\$15,000,000**  
Cash paid = **\$15,800,000**  
Loss on settlement = \$15,800,000 − \$15,000,000 = **\$800,000**

*December 31, Year 10 — Settle ARO*  

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 15,000,000 | |
| Loss on Settlement of Asset Retirement Obligation | 800,000 | |
| Cash | | 15,800,000 |

**Check:** Dr 15,000,000 + 800,000 = Cr 15,800,000. **Balanced.**

**e. Presentation just after initial recognition (Jan 1, Year 1)**  
- **PPE (gross):** Building includes **\$126,336,162** (construction + capitalized asset retirement cost).  
- **Liabilities:** Asset Retirement Obligation **\$6,336,162** (noncurrent; settlement is 10 years out).  
- No accretion or depreciation until period-end of Year 1.

**Key insight:** At **initial recognition**, the PV of the ARO is **added to the related asset** (not expensed immediately) with a matching **liability**. Subsequent periods **depreciate** the higher asset base and **accrete** the liability with the effective interest method until settlement produces a gain or loss.

---

### Q2 — CORE number variant — Full ARO cycle twin
**LO:** LO 11-5  
**Concept:** Number-variant twin: initial ARO recognition, depreciation, accretion schedule, settlement with gain  
**Scenario:**  
**Ironclad Landfill Co.** (calendar year) opens a new municipal solid-waste cell on **January 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Cash construction / development cost (ex-closure) | **$90,000,000** |
| Useful life of the cell | **8 years**, straight-line, **zero** residual |
| Legal obligation | Close and reclaim the cell at end of useful life |
| Estimated closure / reclamation cost | **$12,000,000** (December 31, Year 8) |
| Discount rate | **6%** |

**Required:**  
a. Compute PV of the ARO; record January 1, Year 1 entry for the cell **and** ARO.  
b. Record December 31, Year 1 depreciation and accretion.  
c. Complete ARO accretion schedule Years 1–8.  
d. On December 31, Year 8 (after Year-8 accretion), settle for **\$11,400,000** cash. Record settlement.  
e. Compute **total accretion expense** over the full term and **total depreciation** over the cell’s life (using annual rounded depreciation × 8).

**Answer key:**  

**a. PV and initial recognition**

\[
PV = \frac{\$12{,}000{,}000}{(1.06)^{8}} = \$7{,}528{,}948
\]

Capitalized cost = \$90,000,000 + \$7,528,948 = **\$97,528,948**

*January 1, Year 1*  

| Account | Debit | Credit |
|---|---:|---:|
| Land Improvements—Landfill Cell | 97,528,948 | |
| Cash | | 90,000,000 |
| Asset Retirement Obligation | | 7,528,948 |

**Check:** Dr 97,528,948 = Cr 90,000,000 + 7,528,948. **Balanced.**

**b. December 31, Year 1 adjusting entries**

Depreciation: \$97,528,948 / 8 = **\$12,191,119** (nearest dollar).

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 12,191,119 | |
| Accumulated Depreciation—Landfill Cell | | 12,191,119 |

**Check:** 12,191,119 = 12,191,119.

Accretion: \$7,528,948 × 6% = **\$451,737**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 451,737 | |
| Asset Retirement Obligation | | 451,737 |

**Check:** 451,737 = 451,737.

Ending ARO Year 1: \$7,528,948 + \$451,737 = **\$7,980,685**

**c. ARO accretion schedule @ 6%**

| Year | Beginning ARO | Accretion (6%) | Ending ARO |
|---:|---:|---:|---:|
| 1 | 7,528,948 | 451,737 | 7,980,685 |
| 2 | 7,980,685 | 478,841 | 8,459,526 |
| 3 | 8,459,526 | 507,572 | 8,967,098 |
| 4 | 8,967,098 | 538,026 | 9,505,124 |
| 5 | 9,505,124 | 570,307 | 10,075,431 |
| 6 | 10,075,431 | 604,526 | 10,679,957 |
| 7 | 10,679,957 | 640,797 | 11,320,754 |
| 8 | 11,320,754 | 679,246 | **12,000,000** |
| **Total** | | **4,471,052** | |

**Check:** \$7,528,948 + \$4,471,052 = **\$12,000,000**.

**d. Settlement with gain**

ARO = **\$12,000,000**; cash = **\$11,400,000**; gain = **\$600,000**

*December 31, Year 8 — Settle ARO*  

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 12,000,000 | |
| Cash | | 11,400,000 |
| Gain on Settlement of Asset Retirement Obligation | | 600,000 |

**Check:** Dr 12,000,000 = Cr 11,400,000 + 600,000. **Balanced.**

**e. Life-cycle totals**  
- Total accretion expense over term: **\$4,471,052** (= FV − PV).  
- Total depreciation (annual rounded × 8): \$12,191,119 × 8 = **\$97,528,952** (\$4 residual vs capitalized base due to annual rounding — exam answers typically use the annual rounded amount each year).

**Key insight:** Same mechanics as Q1 with **all numbers changed**. Settlement cash **below** ARO carrying amount produces a **gain**; cash **above** produces a **loss**. Total accretion over the life always bridges PV at recognition to the estimated future cost.

---

### Q3 — CORE alternate angle — Period-end adjusting, multi-year schedule excerpt, settlement & presentation
**LO:** LO 11-5  
**Concept:** Purchase + ARO initial recognition; Year-end depreciation and accretion only; multi-period schedule; settlement; classification/presentation  
**Scenario:**  
**PrairieTank Logistics** installs an underground storage tank on **January 1, Year 1** for cash **\$2,400,000**. Useful life **6 years**, straight-line, zero residual. State environmental law requires removal and site restoration at an estimated cost of **\$400,000** on **December 31, Year 6**. Discount rate **7%**. Calendar year-end.

**Required:**  
a. Record January 1, Year 1 entries for (1) tank purchase and (2) ARO initial recognition (may combine).  
b. Record **only** the December 31, Year 1 **period-end adjusting** entries (depreciation and accretion).  
c. Show ARO balances and accretion for **Years 1–3** only (schedule excerpt).  
d. Assume all accretion through Year 6 has been recorded so ARO = **\$400,000**. Actual removal cost paid December 31, Year 6 is **\$385,000**. Record settlement.  
e. **Classification / presentation:** For Year 1 financial statements, identify (i) income-statement classification of accretion expense, (ii) balance-sheet classification of the ARO at Dec 31, Year 1, and (iii) whether the asset retirement cost is presented separately from the tank or embedded in the tank’s capitalized cost.

**Answer key:**  

**a. PV and initial recognition**

\[
PV = \frac{\$400{,}000}{(1.07)^{6}} = \$266{,}537
\]

*January 1, Year 1 — Combined*  

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Storage Tank | 2,666,537 | |
| Cash | | 2,400,000 |
| Asset Retirement Obligation | | 266,537 |

**Check:** Dr 2,666,537 = Cr 2,400,000 + 266,537. **Balanced.**

**b. Period-end adjusting entries — December 31, Year 1**

Depreciation: \$2,666,537 / 6 = **\$444,423**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 444,423 | |
| Accumulated Depreciation—Storage Tank | | 444,423 |

**Check:** 444,423 = 444,423.

Accretion: \$266,537 × 7% = **\$18,658**

| Account | Debit | Credit |
|---|---:|---:|
| Accretion Expense | 18,658 | |
| Asset Retirement Obligation | | 18,658 |

**Check:** 18,658 = 18,658.

**c. Schedule excerpt Years 1–3**

| Year | Beginning ARO | Accretion (7%) | Ending ARO |
|---:|---:|---:|---:|
| 1 | 266,537 | 18,658 | 285,195 |
| 2 | 285,195 | 19,964 | 305,159 |
| 3 | 305,159 | 21,361 | 326,520 |

**d. Settlement with gain**

| Account | Debit | Credit |
|---|---:|---:|
| Asset Retirement Obligation | 400,000 | |
| Cash | | 385,000 |
| Gain on Settlement of Asset Retirement Obligation | | 15,000 |

**Check:** Dr 400,000 = Cr 385,000 + 15,000. **Balanced.**

**e. Classification / presentation**  
(i) **Accretion expense** is classified as an **operating expense** (not as interest expense for the core LO presentation; it is the period cost of the passage of time on the ARO).  
(ii) At Dec 31, Year 1 (five years before settlement), ARO is a **noncurrent liability** (reclassify to current when settlement is expected within one year).  
(iii) The asset retirement cost is **capitalized into the carrying amount of the related tank** (not a freestanding intangible); it is depreciated as part of the tank’s depreciable base.

**Key insight:** Period-end entries are always a **pair**: depreciate the **grossed-up** asset and **accrete** the liability. Presentation keeps the obligation on the balance sheet while the retirement cost rides through PPE via depreciation.

---

### Q4 — MC — ARO recognition and classification
**LO:** LO 11-5  
**Concept:** When to recognize ARO; income-statement classification of accretion vs depreciation of asset retirement cost  
**Question:**  
Which statement about **asset retirement obligations** is correct under the core accounting model (ASC 410-20 / LO 11-5)?

- A) The estimated future retirement cost is expensed in full when the related asset is placed in service; no liability is recorded until cash is paid.  
- B) The present value of a reasonably estimable legal retirement obligation is capitalized to the related long-lived asset with a matching ARO liability; subsequent accretion is an operating expense and the capitalized cost is depreciated over the asset’s useful life.  
- C) Accretion expense is always classified as interest expense in other expense, and the ARO is recorded only at the undiscounted future cash amount.  
- D) If fair value of the ARO cannot be estimated at acquisition, the company still must record the full undiscounted future cost as a liability immediately.

**Answer:** **B.**  
Recognition requires a **legal obligation** and a **reasonable estimate of fair value (PV)**. Initial entry capitalizes asset retirement cost to PPE and credits ARO. Over time: **depreciation** on the increased asset base + **accretion** (effective interest) increasing the liability; accretion is an **operating** expense in the core demo. A is wrong (would ignore capitalization). C is wrong (undiscounted initial measurement and “always interest” are incorrect for this LO). D is wrong — if fair value is not reasonably estimable, recognition is **deferred** until it becomes estimable.

---

### Q5 — MC — Settlement measurement
**LO:** LO 11-5  
**Concept:** Gain vs loss on ARO settlement relative to carrying amount of the liability  
**Question:**  
Just before settlement, an ARO liability has been fully accreted to its estimated future cost of **\$500,000**. Actual cash paid to complete retirement activities is **\$460,000**. The settlement entry should include:

- A) Debit Loss \$40,000  
- B) Credit Gain \$40,000  
- C) Debit ARO \$460,000 only (no gain or loss)  
- D) Credit ARO \$40,000 and debit Cash \$500,000  

**Answer:** **B.**  
Debit ARO **\$500,000**, credit Cash **\$460,000**, credit **Gain on Settlement of ARO \$40,000**. Cash less than carrying amount → **gain**; cash greater → **loss**.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV factors, accretion rolls, settlement differences)
- [x] Core demo path (Demo 11-5 / Review 11-5 style) — not Expanding Your Knowledge sidebar-only
- [x] **LO:** and **Concept:** on every item
- [x] MC ≤ 2 (Q4, Q5 only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original companies/numbers (SummitChem, Ironclad, PrairieTank — not Lakeside/BPP textbook figures)
