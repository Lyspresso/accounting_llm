# Agent 209 — CORE DEMO — LO 12-2

**Chapter:** 12  
**LO title:** Account for depreciation in partial periods  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Exact fractional proration:** apply months-in-service ÷ 12 to time-based annual depreciation (straight-line annual amount; each SYD layer; first DDB year only)
- **Subsequent measurement schedule (emphasis):** multi-year schedules of depreciation expense, accumulated depreciation, and carrying amount that roll to residual value and total exactly to depreciable cost
- **Sum-of-the-years’-digits partial periods:** split each full-year layer across calendar years (e.g., 9/12 then 3/12)
- **Double-declining-balance partial periods:** prorate Year 1 only; then apply rate to beginning carrying amount; stop so carrying amount does not fall below residual
- **Units-of-production:** automatically partial — multiply actual output by per-unit rate (no separate month fraction)
- **Policy conventions:** full-year (beginning / end of period), half-year, full-month — GAAP-acceptable if not materially different from exact fractional; applied consistently
- **Initial recognition JE:** capitalize PPE at acquisition cost when placed in service mid-period
- **Period-end adjusting JE:** Dr Depreciation Expense / Cr Accumulated Depreciation for the partial or full-year amount
- **Disposal with partial period:** update depreciation through disposal date, then remove cost and AD; gain/loss = proceeds − carrying amount

---

### Q1 — CORE — Mid-period acquisition: multi-method subsequent schedules (SL, SYD, DDB, UOP), initial JE, period-end JE
**LO:** LO 12-2  
**Concept:** Subsequent measurement schedule for partial-period depreciation under SL, SYD, DDB, and UOP; initial recognition JE; Year 1 period-end adjusting JE  
**Scenario:**  
**Meridian Tool & Die Inc.** (calendar-year reporter) places a hydraulic stamping press into service on **April 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Acquisition cost (cash) | **$80,000** |
| Estimated residual value | **$8,000** |
| Estimated useful life | **4 years** |
| Estimated total productive output | **90,000 units** |
| Actual output, Year 1 | **6,000 units** |
| Actual output, Year 2 | **24,000 units** |
| Fiscal year-end | December 31 |
| Partial-period policy | **Exact fractional months** (prorate time-based methods) |

Depreciable base = $80,000 − $8,000 = **$72,000**.  
Service life under exact months: **April 1, Year 1 through March 31, Year 5** (exactly 4 years).

**Required:**  
a. Prepare the **April 1, Year 1 initial recognition** journal entry.  
b. Compute **Year 1** and **Year 2** depreciation under (1) **straight-line**, (2) **sum-of-the-years’-digits**, (3) **double-declining-balance**, and (4) **units-of-production**. Prorate partial periods for time-based methods.  
c. Prepare the complete **straight-line subsequent measurement schedule** for Years 1–5 (expense, accumulated depreciation, carrying amount each year-end). Confirm total expense = depreciable cost.  
d. Prepare the complete **sum-of-the-years’-digits subsequent measurement schedule** for Years 1–5, showing layer splits. Confirm total = depreciable cost.  
e. Prepare the complete **double-declining-balance subsequent measurement schedule** for Years 1–5 (stop at residual).  
f. Record the **December 31, Year 1** adjusting entry under **straight-line**.  
g. State Year 1 balance-sheet presentation of the press under straight-line.

**Answer key:**  

**a. April 1, Year 1 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Hydraulic Press | 80,000 | |
| Cash | | 80,000 |
| *Place press in service at acquisition cost* | | |

**Check:** Dr 80,000 = Cr 80,000. **Balanced.**

**b. Year 1 and Year 2 depreciation (exact fractional periods)**

**(1) Straight-line**  
Annual SL = $72,000 / 4 = **$18,000**  
Year 1 (Apr–Dec = **9/12**): $18,000 × 9/12 = **$13,500**  
Year 2 (full year): **$18,000**

**(2) Sum-of-the-years’-digits**  
Digits sum = 4+3+2+1 = **10**  
Each full-year layer is allocated **9/12** to the calendar year that contains April–December of that service year and **3/12** to the following calendar year (January–March).

| Layer | Fraction | Full-year layer | 9/12 portion | 3/12 portion |
|---|---:|---:|---:|---:|
| 1 | 4/10 | $28,800 | $21,600 (Y1) | $7,200 (Y2) |
| 2 | 3/10 | 21,600 | 16,200 (Y2) | 5,400 (Y3) |
| 3 | 2/10 | 14,400 | 10,800 (Y3) | 3,600 (Y4) |
| 4 | 1/10 | 7,200 | 5,400 (Y4) | 1,800 (Y5) |

**Year 1 SYD** = **$21,600**  
**Year 2 SYD** = $7,200 + $16,200 = **$23,400**

**(3) Double-declining-balance**  
DDB rate = 2 × (1/4) = **50%**  
Year 1: $80,000 × 50% × 9/12 = **$30,000**  
Carrying amount end of Year 1 = $80,000 − $30,000 = **$50,000**  
Year 2: $50,000 × 50% = **$25,000**  
Carrying amount end of Year 2 = $50,000 − $25,000 = **$25,000**

**(4) Units-of-production** (automatically partial)  
Rate = $72,000 / 90,000 units = **$0.80 per unit**  
Year 1: 6,000 × $0.80 = **$4,800**  
Year 2: 24,000 × $0.80 = **$19,200**

**Summary — Year 1 / Year 2 depreciation expense**

| Method | Year 1 | Year 2 |
|---|---:|---:|
| Straight-line | $13,500 | $18,000 |
| Sum-of-the-years’-digits | 21,600 | 23,400 |
| Double-declining-balance | 30,000 | 25,000 |
| Units-of-production | 4,800 | 19,200 |

**c. Straight-line subsequent measurement schedule (emphasis)**

| End of period | Depreciable cost | Rate | Partial period | Depreciation expense | Accumulated depreciation | Carrying amount |
|---|---:|---:|---:|---:|---:|---:|
| Apr 1, Y1 (in service) | — | — | — | — | $0 | $80,000 |
| Dec 31, Y1 | $72,000 | 1/4 | 9/12 | **$13,500** | 13,500 | 66,500 |
| Dec 31, Y2 | 72,000 | 1/4 | full | **18,000** | 31,500 | 48,500 |
| Dec 31, Y3 | 72,000 | 1/4 | full | **18,000** | 49,500 | 30,500 |
| Dec 31, Y4 | 72,000 | 1/4 | full | **18,000** | 67,500 | 12,500 |
| Dec 31, Y5 | 72,000 | 1/4 | 3/12 | **4,500** | **72,000** | **8,000** residual |

**Total depreciation over life** = $13,500 + $18,000 × 3 + $4,500 = **$72,000** = depreciable cost. ✓  
Exactly **4 full years** of SL depreciation are recorded across Years 1–5.

**d. SYD subsequent measurement schedule (emphasis)**

| End of period | Depreciation expense | Accumulated depreciation | Carrying amount |
|---|---:|---:|---:|
| Apr 1, Y1 | — | $0 | $80,000 |
| Dec 31, Y1 | **$21,600** (layer 1 × 9/12) | 21,600 | 58,400 |
| Dec 31, Y2 | **23,400** (7,200 + 16,200) | 45,000 | 35,000 |
| Dec 31, Y3 | **16,200** (5,400 + 10,800) | 61,200 | 18,800 |
| Dec 31, Y4 | **9,000** (3,600 + 5,400) | 70,200 | 9,800 |
| Dec 31, Y5 | **1,800** (layer 4 × 3/12) | **72,000** | **8,000** residual |

**Total** = $21,600 + $23,400 + $16,200 + $9,000 + $1,800 = **$72,000**. ✓

**e. DDB subsequent measurement schedule (emphasis)**

| End of period | Beginning carrying amount | Rate | Partial | Depreciation expense | Accumulated depreciation | Carrying amount |
|---|---:|---:|---:|---:|---:|---:|
| Apr 1, Y1 | — | — | — | — | $0 | $80,000 |
| Dec 31, Y1 | $80,000 | 50% | 9/12 | **$30,000** | 30,000 | 50,000 |
| Dec 31, Y2 | 50,000 | 50% | full | **25,000** | 55,000 | 25,000 |
| Dec 31, Y3 | 25,000 | 50% | full | **12,500** | 67,500 | 12,500 |
| Dec 31, Y4 | 12,500 | 50% | full | **$4,500**† | **72,000** | **8,000** residual |
| Dec 31, Y5 | 8,000 | — | — | **$0** | 72,000 | 8,000 |

† Uncapped 50% of $12,500 = $6,250 would drop BV below residual $8,000. Maximum Year 4 depreciation = $12,500 − $8,000 = **$4,500**. Year 5 has no remaining depreciable base after residual is reached early in the fourth calendar year of service.  
**Total** = $30,000 + $25,000 + $12,500 + $4,500 = **$72,000**. ✓

**f. December 31, Year 1 — period-end adjusting JE (straight-line)**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Hydraulic Press | 13,500 | |
| Accumulated Depreciation—Hydraulic Press | | 13,500 |
| *Partial-year SL: $18,000 × 9/12* | | |

**Check:** Dr 13,500 = Cr 13,500. **Balanced.**

**g. Year 1 presentation (straight-line)**  
- **Income statement:** Depreciation Expense **$13,500**.  
- **Balance sheet (noncurrent assets):** Equipment **$80,000** less Accumulated Depreciation **$13,500** → **carrying amount $66,500**.

**Key insight:** The **subsequent measurement schedule** is the core of LO 12-2: after mid-period acquisition, each method’s multi-year table must still total **depreciable cost** and end at **residual**. SL and SYD prorate time fractions (and SYD splits **layers** across calendar years); DDB prorates only Year 1 then floors at residual; UOP needs no month fraction because **actual output** does the partial-period work.

---

### Q2 — CORE number variant — Late-year purchase: SL life schedule + policy conventions comparison
**LO:** LO 12-2  
**Concept:** Number-variant twin — subsequent measurement SL schedule under exact fractional months; policy-convention comparison schedule; initial recognition and period-end JEs  
**Scenario:**  
**Copperline Bottling Co.** (calendar year) purchases a high-speed filler line on **October 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Acquisition cost (cash) | **$105,000** |
| Residual value | **$5,000** |
| Useful life | **5 years** |
| Placed in service | **October 1, Year 1** |
| Depreciation method for schedules | Straight-line |
| Year-end | December 31 |

Depreciable base = $105,000 − $5,000 = **$100,000**.  
Annual SL = $100,000 / 5 = **$20,000**.  
Exact service window: Oct 1, Year 1 – Sep 30, Year 6.

**Required:**  
a. Record the **October 1, Year 1 initial recognition** journal entry.  
b. Under **exact fractional months**, prepare the **straight-line subsequent measurement schedule** for Years 1–6 and the **December 31, Year 1** depreciation adjusting entry.  
c. Prepare a **comparison schedule** of Year 1–Year 6 SL depreciation under: (1) exact fractional (from b), (2) full-year convention—beginning of period, (3) full-year convention—end of period, (4) half-year convention, (5) full-month convention. Confirm each column totals $100,000.  
d. Record the December 31, Year 1 adjusting entry under the **half-year convention**.  
e. Briefly state why policy conventions are acceptable under GAAP.

**Answer key:**  

**a. October 1, Year 1 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Filler Line | 105,000 | |
| Cash | | 105,000 |
| *Place filler line in service* | | |

**Check:** Dr 105,000 = Cr 105,000. **Balanced.**

**b. Exact fractional months — SL subsequent measurement schedule**

Months in Year 1 = Oct–Dec = **3/12**.  
Year 6 = Jan–Sep = **9/12**.

| End of period | Depreciation expense | Accumulated depreciation | Carrying amount |
|---|---:|---:|---:|
| Oct 1, Y1 | — | $0 | $105,000 |
| Dec 31, Y1 | **$5,000** ($20,000 × 3/12) | 5,000 | 100,000 |
| Dec 31, Y2 | **20,000** | 25,000 | 80,000 |
| Dec 31, Y3 | **20,000** | 45,000 | 60,000 |
| Dec 31, Y4 | **20,000** | 65,000 | 40,000 |
| Dec 31, Y5 | **20,000** | 85,000 | 20,000 |
| Dec 31, Y6 | **$15,000** ($20,000 × 9/12) | **100,000** | **5,000** residual |

**Total expense** = $5,000 + $20,000 × 4 + $15,000 = **$100,000**. ✓

*December 31, Year 1 — exact fractional SL*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Filler Line | 5,000 | |
| Accumulated Depreciation—Filler Line | | 5,000 |
| *Partial-year SL: $20,000 × 3/12* | | |

**Check:** Dr 5,000 = Cr 5,000. **Balanced.**

**c. Policy-convention comparison schedule (subsequent measurement across conventions)**

| Method | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Year 6 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| (1) Exact fractional (Demo 12-2A style) | **$5,000** | $20,000 | $20,000 | $20,000 | $20,000 | **$15,000** | **$100,000** |
| (2) Full-year — beginning of period | **0** | 20,000 | 20,000 | 20,000 | 20,000 | 20,000 | **100,000** |
| (3) Full-year — end of period | **20,000** | 20,000 | 20,000 | 20,000 | 20,000 | **0** | **100,000** |
| (4) Half-year | **10,000** | 20,000 | 20,000 | 20,000 | 20,000 | **10,000** | **100,000** |
| (5) Full-month (Oct purchase) | **5,000** | 20,000 | 20,000 | 20,000 | 20,000 | **15,000** | **100,000** |

**Reasoning notes:**  
- **Full-year—beginning of period:** no depreciation in year of purchase; full years in Years 2–6.  
- **Full-year—end of period:** full depreciation in year of purchase; none in Year 6.  
- **Half-year:** ½ × $20,000 in Year 1 and Year 6 regardless of October 1.  
- **Full-month:** full month of depreciation in October (month of purchase), none in month of disposal in the final year → same pattern as exact 3/12 and 9/12 when purchase/disposal fall on the first of the month.  

Year 1 difference, exact vs half-year: half-year records **$5,000 more** ($10,000 vs $5,000) because it ignores the late-year purchase date. All five approaches still depreciate exactly **$100,000** over the asset’s life.

**d. December 31, Year 1 — half-year convention adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Filler Line | 10,000 | |
| Accumulated Depreciation—Filler Line | | 10,000 |
| *Half-year convention: ½ × $20,000 annual SL* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.**

**e. GAAP note**  
Policy conventions are acceptable when results are **not materially different** from exact fractional-period depreciation and the **same policy is applied consistently** from period to period.

**Key insight:** Changing acquisition date and amounts does not change the **schedule discipline**: every convention’s multi-year column must still sum to **depreciable cost**. Exact months (or full-month on a first-of-month purchase) give a small Year-1 stub for late purchases; half-year and full-year conventions deliberately ignore the actual in-service month for simplicity.

---

### Q3 — CORE alternate angle — Partial-period update through disposal + disposal JE; convention classification
**LO:** LO 12-2  
**Concept:** Period-end/through-date partial depreciation before disposal; disposal JE (gain); policy-convention Year-1 amounts for mid-period purchase  
**Scenario:**  
**Oakridge Transit Co.** owns a transit bus purchased and placed in service on **January 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Cost of bus | **$90,000** |
| Residual value | **$10,000** |
| Useful life | **8 years** |
| Depreciation method | Straight-line |
| Accumulated depreciation, January 1, Year 5 | **$40,000** |
| Disposal date | **July 1, Year 5** |
| Cash proceeds on sale | **$48,000** |
| Partial-period policy | **Exact fractional months** through disposal date |
| Fiscal year-end | December 31 |

Annual SL = ($90,000 − $10,000) / 8 = **$10,000**.  
Check AD at Jan 1, Year 5: 4 full years × $10,000 = **$40,000**. ✓

**Required:**  
a. Prepare the **July 1, Year 5** entry to **update depreciation** through the disposal date (6 months).  
b. Compute the **carrying amount** at July 1 and the **gain or loss** on disposal.  
c. Prepare the **July 1 disposal journal entry**. Show Dr = Cr.  
d. Independently, assume a **different** asset acquired on **June 18, Year 1** (cost $90,000, residual $10,000, 8-year SL, annual $10,000). Without computing exact days, state **Year 1** depreciation under each policy convention: (1) full-year—beginning of period, (2) full-year—end of period, (3) half-year, (4) full-month.  
e. Classify: where is the gain on disposal reported, and is Accumulated Depreciation a liability?

**Answer key:**  

**a. July 1, Year 5 — update depreciation through disposal**  
6/12 × $10,000 = **$5,000**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Transit Bus | 5,000 | |
| Accumulated Depreciation—Transit Bus | | 5,000 |
| *Partial-year SL through July 1: $10,000 × 6/12* | | |

**Check:** Dr 5,000 = Cr 5,000. **Balanced.**

**b. Carrying amount and gain/loss**  
AD at disposal = $40,000 + $5,000 = **$45,000**  
Carrying amount = $90,000 − $45,000 = **$45,000**  
Proceeds = **$48,000**  
**Gain on disposal** = $48,000 − $45,000 = **$3,000**

**c. July 1, Year 5 — disposal JE**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 48,000 | |
| Accumulated Depreciation—Transit Bus | 45,000 | |
| Equipment—Transit Bus | | 90,000 |
| Gain on Disposal of PPE | | 3,000 |
| *Remove cost and AD; recognize gain (proceeds > BV)* | | |

**Check:** Dr $48,000 + $45,000 = **$93,000**; Cr $90,000 + $3,000 = **$93,000**. **Balanced.**

**d. Policy conventions — Year 1 only (June 18 acquisition; annual SL $10,000)**

| Convention | Year 1 depreciation | Reasoning |
|---|---:|---|
| (1) Full-year — **beginning of period** | **$0** | Assets purchased during the year are **not** depreciated that year |
| (2) Full-year — **end of period** | **$10,000** | Assets purchased during the year are depreciated a **full year** |
| (3) Half-year | **$5,000** | ½ × $10,000 in year of purchase regardless of June 18 |
| (4) Full-month | **$5,833** (rounded) or **$5,833.33** = 7/12 × $10,000 | Full month in June (month of purchase); 7 months Jun–Dec |

(Exact fractional from June 18 is nearly the same as full-month for practical purposes; textbook full-month = full depreciation in purchase month, none in disposal month.)

**e. Classification / presentation**  
- **Gain on Disposal of PPE $3,000** is reported on the **income statement** (typically other income / not operating revenue from sales to customers).  
- **Accumulated Depreciation** is a **contra-asset** (credit balance reducing PPE), **not** a liability.  
- After disposal, both the bus’s cost and its AD are **removed**; neither remains on the balance sheet.

**Key insight:** Before any mid-period **disposal**, always **update depreciation** for the fractional period used so AD and carrying amount are current. The disposal entry clears cost and AD and plugs **gain or loss** so the entry balances. Policy conventions remain a practical alternative to exact days when applied consistently.

---

### Q4 — MC — Half-year convention amount
**LO:** LO 12-2  
**Concept:** Identify correct partial-period depreciation under the half-year convention  
**Question:**  
On **November 20, Year 1**, Redline Packaging LLC purchased equipment for **$150,000**. Residual value **$15,000**; useful life **5 years**; straight-line. Redline’s policy is the **half-year convention**. What is **Year 1 depreciation expense**?

- A) $0  
- B) $13,500  
- C) $4,500  
- D) $27,000  

**Answer:** **B. $13,500.**  
Annual SL = ($150,000 − $15,000) / 5 = **$27,000**. Half-year convention → Year 1 = ½ × $27,000 = **$13,500**, regardless of the November 20 purchase date.  
- A would be full-year—beginning of period (no depreciation in year of purchase).  
- C is 2/12 × $27,000 (approximate exact months Nov–Dec) — not half-year.  
- D is a full year of SL — full-year—end of period, not half-year.

---

### Q5 — MC — SYD first-layer proration
**LO:** LO 12-2  
**Concept:** Prorate first SYD layer when asset is acquired mid-year  
**Question:**  
Equipment cost **$86,000**, residual **$6,000**, life **5 years**, purchased **July 1, Year 1**. Company uses **sum-of-the-years’-digits** and **exact fractional periods**. What is **Year 1 depreciation**?

- A) $26,667  
- B) $13,333  
- C) $16,000  
- D) $8,000  

**Answer:** **B. $13,333** (rounded; exact $13,333.33).  
Depreciable base = $80,000; digits sum = 15; first full layer = 5/15 × $80,000 = **$26,666.67**. July 1 → **6/12** of first layer in Year 1: $26,666.67 × 6/12 = **$13,333.33**.  
- A is the full first layer (no proration).  
- C is half-year of SL annual ($16,000 = ½ × $32,000), wrong method.  
- D is 6/12 of annual SL ($16,000 × 6/12) or other miscalc.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (SL multi-year totals, SYD layers, DDB residual floor, UOP, half-year, disposal BV/gain, convention table)
- [x] Core demo not sidebar-only (LO 12-2 Demo 12-2A / 12-2B path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Emphasis: subsequent_measurement_schedule (Q1 multi-method life schedules; Q2 convention comparison schedule)
