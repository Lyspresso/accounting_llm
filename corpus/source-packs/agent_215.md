# Agent 215 — CORE DEMO — LO 12-8

**Chapter:** 12  
**LO title:** Account for assets held for sale  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Held-for-sale criteria (ASC 360-10-45-9):** management commits to a plan; asset available for immediate sale; active sale program underway; sale probable and generally expected within one year; actively marketed at a reasonable price; significant plan changes unlikely
- **Initial measurement:** lower of **carrying amount** or **fair value less costs to sell (FV − CTS)**; **no recoverability test** (unlike assets held and used)
- **Initial recognition JE:** write asset down (Loss on Impairment / Accumulated Depreciation) when FV − CTS < CA; **cease depreciation** while classified as held for sale; report in **Other Assets** (not PP&E)
- **Subsequent measurement schedule (emphasis):** each reporting date remeasure at lower of CA or FV − CTS; **recoveries allowed only up to cumulative prior held-for-sale impairment losses** (CA cannot exceed CA at designation as held for sale)
- **Period-end adjusting JE:** additional write-down (loss) or recovery of impairment (gain, capped)
- **Disposal / sale JE:** remove cost and accumulated depreciation; record cash (and selling costs); recognize final gain or loss vs. adjusted carrying amount

---

### Q1 — CORE — Full held-for-sale life cycle: initial impairment, multi-period subsequent measurement schedule, period-end JEs, disposal
**LO:** LO 12-8  
**Concept:** Initial recognition of impairment when a fixed asset is designated held for sale; multi-period subsequent measurement schedule (FV less costs to sell, recovery cap); period-end adjusting JEs; sale/disposal JE when sold  
**Scenario:**  
**Cedarline Packaging Inc.** (calendar year-end) operates a specialty carton press. On **December 31, Year 1**, management commits to a formal plan to sell the press, begins an active marketing program, and meets **all** held-for-sale criteria under ASC 360. The press will be available for immediate sale in its present condition; sale is probable and expected within one year.

Immediately before classification as held for sale on December 31, Year 1:

| Item | Amount |
|---|---:|
| Cost | $90,000 |
| Accumulated depreciation | 35,000 |
| **Carrying amount** | **$55,000** |

Measurement inputs while held for sale (costs to sell are direct incremental costs of disposal):

| Date | Fair value | Estimated costs to sell |
|---|---:|---:|
| Dec. 31, Year 1 (initial HFS) | $48,000 | $3,000 |
| Dec. 31, Year 2 (still held for sale; sale delayed) | $52,000 | $3,000 |
| Dec. 31, Year 3 (still held for sale) | $40,000 | $2,500 |

On **March 20, Year 4**, Cedarline sells the press for **$39,000 cash** and pays **$2,800 cash** of actual selling costs on the same date. No depreciation is recorded after December 31, Year 1 (while held for sale).

**Required:**  
a. Compute the **December 31, Year 1** impairment (if any) and prepare the **initial held-for-sale impairment JE**. State the **adjusted carrying amount** and balance-sheet classification.  
b. Prepare a **subsequent measurement schedule** from designation through December 31, Year 3 with columns: Date | FV | CTS | FV − CTS | CA before adj. | Adj. gain/(loss) | CA after adj. | Cumulative net HFS impairment | Cap (CA at HFS designation).  
c. Prepare the **period-end adjusting JEs** on **December 31, Year 2** and **December 31, Year 3**.  
d. Prepare the **March 20, Year 4 disposal/sale JE** (remove cost and accumulated depreciation; record cash and selling costs; final gain or loss).  
e. Briefly explain why a **recoverability test is not applied** for assets held for sale, and what limits any recovery gain before disposal.

**Answer key:**  

**a. December 31, Year 1 — initial measurement and JE**

Carrying amount at designation = $90,000 − $35,000 = **$55,000**  
FV less costs to sell = $48,000 − $3,000 = **$45,000**  
Measured amount = lower of $55,000 and $45,000 = **$45,000**  
Impairment loss = $55,000 − $45,000 = **$10,000**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 10,000 | |
| Accumulated Depreciation | | 10,000 |
| *Write asset held for sale down to FV less costs to sell* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.**

After entry: Accumulated depreciation = $35,000 + $10,000 = **$45,000**  
Adjusted carrying amount = $90,000 − $45,000 = **$45,000**  
**Classification:** report as **Other (nonoperating) assets** — not PP&E. **No further depreciation** while held for sale.  
**Cap for future recoveries:** carrying amount at designation = **$55,000** (cumulative recovery gains cannot restore CA above this amount).

**b. Subsequent measurement schedule (emphasis)**

Cap (CA at HFS designation) = **$55,000** throughout.

| Date | FV | CTS | FV − CTS | CA before adj. | Adj. gain/(loss) | CA after adj. | Cumulative net HFS impairment | Cap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dec. 31, Y1 | $48,000 | $3,000 | $45,000 | $55,000 | **$(10,000)** | **$45,000** | $10,000 | $55,000 |
| Dec. 31, Y2 | 52,000 | 3,000 | 49,000 | 45,000 | **$4,000** | **$49,000** | 6,000 | 55,000 |
| Dec. 31, Y3 | 40,000 | 2,500 | 37,500 | 49,000 | **$(11,500)** | **$37,500** | 17,500 | 55,000 |

**Schedule math checks:**  
- **Y2:** Target = min(FV − CTS, Cap) = min($49,000, $55,000) = $49,000 > CA $45,000 → recovery **$4,000** (≤ cumulative prior loss $10,000). New CA $49,000 = $90,000 − AD $41,000.  
- **Y3:** FV − CTS $37,500 < CA $49,000 → additional loss **$11,500**. New CA $37,500 = $90,000 − AD $52,500.  
- Cumulative net impairment at Y3: $10,000 − $4,000 + $11,500 = **$17,500**; $55,000 − $17,500 = **$37,500**.  
- No period’s CA exceeds the **$55,000** designation cap.

**c. Period-end adjusting JEs**

*December 31, Year 2 — recovery of impairment (capped)*

| Account | Debit | Credit |
|---|---:|---:|
| Accumulated Depreciation | 4,000 | |
| Gain on Recovery of Impaired Asset | | 4,000 |
| *Increase CA to current FV less CTS, not above designation CA* | | |

**Check:** Dr 4,000 = Cr 4,000. **Balanced.**  
AD after = $45,000 − $4,000 = **$41,000**; CA = **$49,000**.

*December 31, Year 3 — additional write-down*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 11,500 | |
| Accumulated Depreciation | | 11,500 |
| *Write down held-for-sale asset to updated FV less CTS* | | |

**Check:** Dr 11,500 = Cr 11,500. **Balanced.**  
AD after = $41,000 + $11,500 = **$52,500**; CA = **$37,500**.

**d. March 20, Year 4 — disposal / sale**

Net cash proceeds = $39,000 − $2,800 = **$36,200**  
Carrying amount at sale = **$37,500**  
Loss on disposal = $37,500 − $36,200 = **$1,300**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 39,000 | |
| Accumulated Depreciation | 52,500 | |
| Loss on Disposal of Asset Held for Sale | 1,300 | |
| Equipment | | 90,000 |
| Cash | | 2,800 |
| *Sell held-for-sale press; remove cost and AD; pay selling costs* | | |

**Check:** Dr 39,000 + 52,500 + 1,300 = **92,800**; Cr 90,000 + 2,800 = **92,800**. **Balanced.**

**e. Conceptual**  
For assets held for sale, value will be realized through **sale**, not continued use, so the **recoverability (undiscounted cash flows) test is not applied**. Measurement focuses on **valuation at FV less costs to sell**. Subsequent **increases** in FV − CTS may reverse prior held-for-sale write-downs, but **only up to cumulative impairment losses previously recognized** (CA cannot exceed the carrying amount when the asset was designated held for sale). Depreciation stops while held for sale.

**Key insight:** Held-for-sale accounting is a **lower-of-CA-or-(FV−CTS)** model with a **rolling subsequent measurement schedule**. Losses can deepen each period; recoveries are real but **capped**. The schedule’s ending CA is the anchor for the eventual disposal gain or loss.

---

### Q2 — CORE number variant — Initial HFS impairment, subsequent measurement schedule, period-end recovery then write-down, disposal
**LO:** LO 12-8  
**Concept:** Number-variant twin: designate asset held for sale; full subsequent measurement schedule with recovery and later write-down; period-end JEs; cash sale disposal  
**Scenario:**  
**Northridge Tool Works LLC** (calendar year-end) decides on **December 31, Year 1** that a CNC milling machine meets **all** criteria to be classified as held for sale. Sale is expected within one year; depreciation ceases on that date.

| Item at Dec. 31, Year 1 (before HFS measurement) | Amount |
|---|---:|
| Cost | $120,000 |
| Accumulated depreciation | 48,000 |
| **Carrying amount** | **$72,000** |

| Date | Fair value | Estimated costs to sell |
|---|---:|---:|
| Dec. 31, Year 1 | $65,000 | $4,000 |
| Dec. 31, Year 2 (still held for sale) | $70,000 | $4,000 |
| Dec. 31, Year 3 (still held for sale) | $58,000 | $3,500 |

On **February 10, Year 4**, Northridge sells the machine for **$57,000 cash** and incurs **$3,200** cash selling costs.

**Required:**  
a. Compute and record the **December 31, Year 1** held-for-sale impairment JE; state adjusted CA.  
b. Prepare the **subsequent measurement schedule** (same column structure as Q1) through December 31, Year 3.  
c. Prepare **period-end adjusting JEs** for Year 2 and Year 3.  
d. Prepare the **February 10, Year 4 sale JE**.  
e. State the **maximum carrying amount** allowable at any date after designation and the **maximum recovery gain** that could ever be recognized before sale (from the Y1 write-down alone, before later losses).

**Answer key:**  

**a. December 31, Year 1**

CA = $120,000 − $48,000 = **$72,000**  
FV − CTS = $65,000 − $4,000 = **$61,000**  
Impairment = $72,000 − $61,000 = **$11,000**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 11,000 | |
| Accumulated Depreciation | | 11,000 |
| *Initial write-down of asset held for sale to FV − CTS* | | |

**Check:** Dr 11,000 = Cr 11,000. **Balanced.**  
AD = $48,000 + $11,000 = **$59,000**; CA = **$61,000**. Cap at designation = **$72,000**.

**b. Subsequent measurement schedule**

| Date | FV | CTS | FV − CTS | CA before adj. | Adj. gain/(loss) | CA after adj. | Cumulative net HFS impairment | Cap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dec. 31, Y1 | $65,000 | $4,000 | $61,000 | $72,000 | **$(11,000)** | **$61,000** | $11,000 | $72,000 |
| Dec. 31, Y2 | 70,000 | 4,000 | 66,000 | 61,000 | **$5,000** | **$66,000** | 6,000 | 72,000 |
| Dec. 31, Y3 | 58,000 | 3,500 | 54,500 | 66,000 | **$(11,500)** | **$54,500** | 17,500 | 72,000 |

**Checks:**  
- Y2 recovery: min(FV−CTS, Cap) − CA = $66,000 − $61,000 = **$5,000** (≤ $11,000 prior cumulative loss). AD = $59,000 − $5,000 = **$54,000**.  
- Y3 loss: $66,000 − $54,500 = **$11,500**. AD = $54,000 + $11,500 = **$65,500**. CA = $120,000 − $65,500 = **$54,500**.  
- Cumulative net: $11,000 − $5,000 + $11,500 = **$17,500**; $72,000 − $17,500 = **$54,500**.

**c. Period-end JEs**

*December 31, Year 2*

| Account | Debit | Credit |
|---|---:|---:|
| Accumulated Depreciation | 5,000 | |
| Gain on Recovery of Impaired Asset | | 5,000 |
| *Partial recovery of prior held-for-sale impairment* | | |

**Check:** Dr 5,000 = Cr 5,000. **Balanced.**

*December 31, Year 3*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 11,500 | |
| Accumulated Depreciation | | 11,500 |
| *Subsequent write-down of held-for-sale asset* | | |

**Check:** Dr 11,500 = Cr 11,500. **Balanced.**

**d. February 10, Year 4 — disposal**

Net proceeds = $57,000 − $3,200 = **$53,800**  
CA = **$54,500**  
Loss on disposal = $54,500 − $53,800 = **$700**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 57,000 | |
| Accumulated Depreciation | 65,500 | |
| Loss on Disposal of Asset Held for Sale | 700 | |
| Equipment | | 120,000 |
| Cash | | 3,200 |
| *Sell held-for-sale CNC machine* | | |

**Check:** Dr 57,000 + 65,500 + 700 = **123,200**; Cr 120,000 + 3,200 = **123,200**. **Balanced.**

**e. Caps**  
Maximum CA after designation = CA at designation = **$72,000**.  
Maximum recovery gain from the initial $11,000 write-down alone (before any later losses) = **$11,000** (cannot create net unrealized holding gain above pre-HFS CA).

**Key insight:** Changing every dollar amount still leaves the same engine: **compare CA to FV − CTS each period**, allow **capped recoveries**, stop depreciation, and close out cost/AD at sale against **net proceeds**.

---

### Q3 — CORE alternate angle — Multi-asset held-for-sale screen + period-end recovery only + disposal with gain
**LO:** LO 12-8  
**Concept:** Identify which held-for-sale assets require impairment; combined initial JE; subsequent period with only a recovery adjustment (no depreciation); disposal when net proceeds exceed adjusted CA  
**Scenario:**  
**Bayfront Industrial Supply Co.** holds three plant assets that each meet the held-for-sale criteria on **December 31, Year 1**. No recoverability tests are performed (held for sale). Data:

| Asset | Original cost | Accumulated depreciation | Fair value | Selling costs |
|---|---:|---:|---:|---:|
| A — Pallet wrapper | $40,000 | $28,000 | $13,500 | $500 |
| B — Stretch film line | 75,000 | 20,000 | 48,000 | 2,000 |
| C — Warehouse forklift | 36,000 | 12,000 | 22,000 | 1,500 |

**Additional facts:**  
- Asset **B** remains unsold at **December 31, Year 2**. On that date FV = **$52,000** and estimated selling costs = **$2,000**. No other assets from the table remain.  
- On **January 25, Year 3**, Bayfront sells Asset B for **$51,500 cash** and pays **$1,900** cash selling costs.

**Required:**  
a. For each asset, compute CA, FV − CTS, and any **Year 1 impairment**. Which asset(s) require a loss?  
b. Prepare the **combined December 31, Year 1 impairment JE** for all assets that require write-down.  
c. Prepare the **December 31, Year 2 period-end adjusting JE** for Asset B only (subsequent measurement). Show supporting computation and the recovery cap.  
d. Prepare the **January 25, Year 3 disposal JE** for Asset B.  
e. For Asset A only, explain in one sentence why **no impairment** is recorded even though FV ($13,500) is below original cost ($40,000).

**Answer key:**  

**a. Asset-by-asset analysis (Year 1)**

| Asset | CA = Cost − AD | FV − CTS | Lower amount | Impairment? |
|---|---:|---:|---:|---|
| A | $40,000 − $28,000 = **$12,000** | $13,500 − $500 = **$13,000** | $12,000 | **No** (FV−CTS ≥ CA) |
| B | $75,000 − $20,000 = **$55,000** | $48,000 − $2,000 = **$46,000** | $46,000 | **Yes — $9,000** |
| C | $36,000 − $12,000 = **$24,000** | $22,000 − $1,500 = **$20,500** | $20,500 | **Yes — $3,500** |

Total Year 1 impairment = $9,000 + $3,500 = **$12,500**.

**b. Combined initial impairment JE**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 12,500 | |
| Accumulated Depreciation | | 12,500 |
| *Impair held-for-sale assets B ($9,000) and C ($3,500)* | | |

**Check:** Dr 12,500 = Cr 12,500. **Balanced.**

Post-JE carrying amounts:  
- A: still **$12,000**  
- B: **$46,000** (AD = $20,000 + $9,000 = $29,000)  
- C: **$20,500** (AD = $12,000 + $3,500 = $15,500)

**c. December 31, Year 2 — Asset B subsequent measurement only**

CA before adj. (Asset B) = **$46,000**  
Cap (CA at HFS designation for B) = **$55,000**  
FV − CTS = $52,000 − $2,000 = **$50,000**  
Target CA = min($50,000, $55,000) = **$50,000**  
Recovery gain = $50,000 − $46,000 = **$4,000** (≤ cumulative prior HFS loss on B of $9,000)

| Account | Debit | Credit |
|---|---:|---:|
| Accumulated Depreciation | 4,000 | |
| Gain on Recovery of Impaired Asset | | 4,000 |
| *Year 2 recovery on held-for-sale Asset B* | | |

**Check:** Dr 4,000 = Cr 4,000. **Balanced.**  
AD after (B) = $29,000 − $4,000 = **$25,000**; CA = $75,000 − $25,000 = **$50,000**.  
**No depreciation** is recorded on B during Year 2.

**d. January 25, Year 3 — disposal of Asset B**

Net proceeds = $51,500 − $1,900 = **$49,600**  
CA = **$50,000**  
Loss on disposal = $50,000 − $49,600 = **$400**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 51,500 | |
| Accumulated Depreciation | 25,000 | |
| Loss on Disposal of Asset Held for Sale | 400 | |
| Equipment | | 75,000 |
| Cash | | 1,900 |
| *Sell held-for-sale stretch film line* | | |

**Check:** Dr 51,500 + 25,000 + 400 = **76,900**; Cr 75,000 + 1,900 = **76,900**. **Balanced.**

**e. Asset A**  
Impairment for held-for-sale assets is based on **lower of carrying amount or FV less costs to sell**, not original cost; Asset A’s FV − CTS ($13,000) **exceeds** its CA ($12,000), so no write-down is recognized.

**Key insight:** Screen each held-for-sale asset independently; only those with **FV − CTS < CA** take losses. Subsequent recovery is a pure **period-end valuation** entry (no depreciation), and disposal compares **net proceeds** to the latest scheduled CA.

---

### Q4 — MC (classification / measurement)
**LO:** LO 12-8  
**Concept:** Measurement difference — impairment of asset held for sale vs held and used; role of costs to sell and absence of recoverability test  

**Question 1:**  
At a reporting date, **Solstice Metals Corp.** has equipment **held for sale** with a carrying amount of **$80,000**, undiscounted future net cash flows from use (recoverable cost) of **$78,000**, fair value of **$74,000**, and estimated selling costs of **$2,000**. What impairment loss, if any, should Solstice recognize for the held-for-sale equipment?

- A) $0  
- B) $2,000  
- C) $6,000  
- D) $8,000  

**Answer:** **D. $8,000.**  
Held-for-sale assets are measured at the **lower of carrying amount or fair value less costs to sell**. FV − CTS = $74,000 − $2,000 = **$72,000**. Impairment = $80,000 − $72,000 = **$8,000**. The recoverability (undiscounted cash flows) amount of $78,000 is **not used** for held-for-sale measurement (it would matter for assets held and used).

**Question 2:**  
Which statement about long-lived assets classified as **held for sale** is correct under ASC 360 (as applied in this chapter)?

- A) Continue depreciating while held for sale; measure at historical cost less accumulated depreciation only.  
- B) Cease depreciation; measure at the lower of carrying amount or fair value less costs to sell; subsequent increases in FV − CTS may reverse prior write-downs only up to cumulative losses previously recognized.  
- C) Cease depreciation; always remeasure at pure fair value with unlimited unrealized gains.  
- D) Apply the two-step recoverability test first; only if undiscounted cash flows are less than CA may a write-down to FV − CTS be recorded.  

**Answer:** **B.**  
Depreciation **stops**; measurement is **lower of CA or FV − CTS**; recoveries of previously recognized held-for-sale impairments are allowed **only up to cumulative prior losses** (not unlimited FV markups). Option D describes **held-and-used** impairment testing, not held for sale.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (impairments, recoveries, cumulative caps, disposal losses)
- [x] Core demo path (Demo 12-8 / Review 12-8 / E12-32–34 style) — not Expanding Your Knowledge sidebar
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/measurement items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Pier/Madrid demo figures)
