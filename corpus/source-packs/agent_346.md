# Agent 346 — CORE DEMO — LO 12-8

**Chapter:** 12  
**LO title:** Account for assets held for sale  
**Critical gap LO:** no  
**Emphasis:** period_end_adjusting_JE

## Concept list for this pack
- **Held-for-sale (HFS) criteria** (ASC 360-10-45-9): management commits to a plan; asset available for immediate sale; active program to locate a buyer; sale probable and generally expected within one year; actively marketed at a reasonable price; unlikely significant plan changes/withdrawal
- **Initial measurement** once classified HFS: report at the **lower of carrying amount** or **fair value less cost to sell (FV − CTS)**; recognize any write-down as **impairment loss** immediately
- **Cease depreciation/amortization** while classified as held for sale; present as **other (nonoperating) assets**, not PPE
- **Subsequent remeasurement each reporting date**: further write-downs to lower FV − CTS; **recovery gains** allowed only up to **cumulative prior HFS impairment losses** (cannot restore above carrying amount at classification date)
- **Period-end adjusting JE (emphasis):** remeasure HFS asset each year-end — impairment loss or recovery of impairment via accumulated depreciation
- **Disposal JE:** remove cost and accumulated depreciation; cash = net proceeds; residual gain/loss vs current carrying amount
- **No recoverability (undiscounted cash flow) test** for HFS — valuation focus, not use-based recoverability

---

### Q1 — CORE — HFS life cycle: initial write-down, subsequent measurement schedule, period-end recovery, disposal
**LO:** LO 12-8  
**Concept:** Initial HFS impairment JE; subsequent measurement schedule; period-end recovery JE (emphasis); disposal JE  
**Scenario:**  
**Linden Forge Equipment Co.** removes a specialized milling machine from daily operations on **December 31, Year 1** after management commits to a sale plan that meets all held-for-sale criteria. The machine will no longer be depreciated.

| Item | Amount |
|---|---:|
| Cost of milling machine | $90,000 |
| Accumulated depreciation, Dec 31, Year 1 (before HFS adjustment) | 35,000 |
| Fair value, Dec 31, Year 1 | 48,000 |
| Estimated direct costs to sell, Dec 31, Year 1 | 3,000 |

**Subsequent events:**
- **December 31, Year 2:** Asset still held for sale. Fair value is **$52,000**; estimated costs to sell remain **$3,000**. No depreciation is recorded in Year 2.
- **March 15, Year 3:** Linden sells the machine. Cash proceeds are **$51,000**; Linden pays selling costs of **$2,500** in cash at closing (net cash inflow **$48,500**).

**Required:**  
a. Compute carrying amount before HFS adjustment and FV − CTS on Dec 31, Year 1. Record the **initial impairment** journal entry (if any). State the adjusted carrying amount and the balance-sheet classification.  
b. Prepare a **subsequent measurement schedule** from classification through disposal (carrying amount, FV − CTS, ceiling, adjustment, cumulative HFS impairment).  
c. Record the **period-end adjusting entry** on Dec 31, Year 2 (emphasis). State the adjusted carrying amount.  
d. Record the **disposal** entry on March 15, Year 3.  

**Answer key:**

**a. Initial recognition / impairment — Dec 31, Year 1**

| Computation | Amount |
|---|---:|
| Carrying amount before HFS adjustment ($90,000 − $35,000) | $55,000 |
| Fair value less cost to sell ($48,000 − $3,000) | 45,000 |
| **Impairment loss** (lower is FV − CTS) | **$10,000** |

```
Dec 31, Year 1 — To record impairment of asset held for sale
  Dr Loss on Impairment .............................. 10,000
     Cr Accumulated Depreciation — Equipment ................. 10,000
```
**Check:** Dr 10,000 = Cr 10,000.

- Adjusted carrying amount: **$45,000** (= $90,000 cost − $45,000 accum. dep.).  
- Report as **other (nonoperating) assets**, not PPE; **no further depreciation** while HFS.

**b. Subsequent measurement schedule**

| Date | Event | FV | CTS | FV − CTS | Carrying before adj. | Ceiling* | Measurement target | Adjustment | Carrying after | Cum. HFS impair. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12/31/Y1 | Classify HFS | 48,000 | 3,000 | 45,000 | 55,000 | 55,000 | 45,000 | (10,000) loss | 45,000 | 10,000 |
| 12/31/Y2 | Remeasure | 52,000 | 3,000 | 49,000 | 45,000 | 55,000 | 49,000 | +4,000 recovery | 49,000 | 6,000 |
| 3/15/Y3 | Dispose (net proceeds 48,500) | — | — | — | 49,000 | — | 0 | (500) disposal loss | 0 | — |

\*Ceiling = carrying amount at the date the asset was classified as held for sale ($55,000). Recovery cannot push carrying above this amount; also limited by cumulative prior write-downs.

**c. Period-end adjusting JE — Dec 31, Year 2 (emphasis)**

| Computation | Amount |
|---|---:|
| Current carrying amount | $45,000 |
| FV − CTS ($52,000 − $3,000) | 49,000 |
| Ceiling (CA at HFS classification) | 55,000 |
| Allowed new carrying (min of FV − CTS and ceiling) | 49,000 |
| **Recovery of impairment** | **$4,000** |

```
Dec 31, Year 2 — To record recovery of impairment on asset held for sale
  Dr Accumulated Depreciation — Equipment ............ 4,000
     Cr Gain on Recovery of Impaired Asset ................... 4,000
```
**Check:** Dr 4,000 = Cr 4,000.

- No depreciation entry.  
- Adjusted carrying amount Dec 31, Year 2: **$49,000** (= $90,000 − $41,000 accum. dep.).  
- Cumulative HFS impairment remaining: $6,000 ($10,000 − $4,000).

**d. Disposal — March 15, Year 3**

| Computation | Amount |
|---|---:|
| Net cash proceeds ($51,000 − $2,500) | $48,500 |
| Carrying amount at disposal | 49,000 |
| **Loss on disposal** | **$500** |
| Accumulated depreciation balance ($35,000 + $10,000 − $4,000) | 41,000 |

```
Mar 15, Year 3 — To record sale of asset held for sale
  Dr Cash (net proceeds) ............................. 48,500
  Dr Accumulated Depreciation — Equipment ............ 41,000
  Dr Loss on Disposal of Asset Held for Sale ........... 500
     Cr Equipment — Milling Machine .......................... 90,000
```
**Check:** Dr 48,500 + 41,000 + 500 = 90,000 = Cr 90,000.

**Key insight:** Held-for-sale assets are valued each period at the lower of carrying amount or FV − CTS; depreciation stops; recoveries cannot exceed cumulative HFS losses (or original classification carrying amount). Disposal closes cost and accum. dep. against net proceeds.

---

### Q2 — CORE number variant — HFS initial write-down, remeasurement schedule, period-end recovery, disposal
**LO:** LO 12-8  
**Concept:** Same HFS life cycle as Q1 with all new amounts — initial impairment, schedule, period-end recovery, disposal  
**Scenario:**  
**Cedarline Packaging LLC** classifies a high-speed sealer as held for sale on **December 31, Year 1** (all HFS criteria met).

| Item | Amount |
|---|---:|
| Cost of sealer | $120,000 |
| Accumulated depreciation, Dec 31, Year 1 (before HFS adjustment) | 48,000 |
| Fair value, Dec 31, Year 1 | 68,000 |
| Estimated costs to sell, Dec 31, Year 1 | 4,000 |

**Subsequent events:**
- **December 31, Year 2:** Still held for sale. Fair value **$71,000**; costs to sell still **$4,000**. No Year 2 depreciation.
- **February 20, Year 3:** Sold. Gross cash proceeds **$69,500**; selling costs paid in cash **$3,000** (net cash **$66,500**).

**Required:**  
a. Initial impairment JE (if any) and adjusted carrying amount on Dec 31, Year 1.  
b. Subsequent measurement schedule through disposal.  
c. Period-end adjusting JE on Dec 31, Year 2.  
d. Disposal JE on February 20, Year 3.  

**Answer key:**

**a. Dec 31, Year 1**

| Computation | Amount |
|---|---:|
| Carrying amount before HFS ($120,000 − $48,000) | $72,000 |
| FV − CTS ($68,000 − $4,000) | 64,000 |
| **Impairment loss** | **$8,000** |

```
Dec 31, Year 1 — To record impairment of asset held for sale
  Dr Loss on Impairment ............................... 8,000
     Cr Accumulated Depreciation — Equipment .................. 8,000
```
**Check:** Dr 8,000 = Cr 8,000.  
Adjusted carrying amount: **$64,000** (= $120,000 − $56,000 AD). Classify as other assets; stop depreciation.

**b. Subsequent measurement schedule**

| Date | Event | FV | CTS | FV − CTS | CA before | Ceiling | Target | Adj. | CA after | Cum. HFS impair. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12/31/Y1 | Classify HFS | 68,000 | 4,000 | 64,000 | 72,000 | 72,000 | 64,000 | (8,000) | 64,000 | 8,000 |
| 12/31/Y2 | Remeasure | 71,000 | 4,000 | 67,000 | 64,000 | 72,000 | 67,000 | +3,000 | 67,000 | 5,000 |
| 2/20/Y3 | Dispose (net 66,500) | — | — | — | 67,000 | — | 0 | (500) loss | 0 | — |

**c. Period-end adjusting JE — Dec 31, Year 2**

| Computation | Amount |
|---|---:|
| FV − CTS ($71,000 − $4,000) | $67,000 |
| Current carrying | 64,000 |
| Ceiling | 72,000 |
| **Recovery** (min(67,000, 72,000) − 64,000) | **$3,000** |

```
Dec 31, Year 2 — To record recovery of impairment on asset held for sale
  Dr Accumulated Depreciation — Equipment ............. 3,000
     Cr Gain on Recovery of Impaired Asset .................... 3,000
```
**Check:** Dr 3,000 = Cr 3,000.  
Carrying amount Dec 31, Year 2: **$67,000** (= $120,000 − $53,000 AD).

**d. Disposal — February 20, Year 3**

| Computation | Amount |
|---|---:|
| Net cash proceeds ($69,500 − $3,000) | $66,500 |
| Carrying amount | 67,000 |
| **Loss on disposal** | **$500** |
| Accum. dep. ($48,000 + $8,000 − $3,000) | 53,000 |

```
Feb 20, Year 3 — To record sale of asset held for sale
  Dr Cash (net proceeds) .............................. 66,500
  Dr Accumulated Depreciation — Equipment ............. 53,000
  Dr Loss on Disposal of Asset Held for Sale ............ 500
     Cr Equipment — Sealer ...................................... 120,000
```
**Check:** Dr 66,500 + 53,000 + 500 = 120,000 = Cr 120,000.

**Key insight:** Same measurement rules as Q1; only amounts change. Recovery is capped by cumulative HFS losses and the classification-date carrying amount.

---

### Q3 — CORE alternate angle — multi-asset HFS impairment screen + further period-end write-down
**LO:** LO 12-8  
**Concept:** Identify which HFS assets need impairment; initial recognition JEs; period-end subsequent write-down (emphasis) when FV − CTS falls further  
**Scenario:**  
**Northwind Industrial Systems Inc.** has three plant assets that **already qualify** as held for sale on **December 31, Year 1**. Management is preparing year-end adjustments.

| Plant asset | Original cost | Accumulated depreciation | Fair value | Selling costs |
|---|---:|---:|---:|---:|
| #N-14 packaging line | $80,000 | $50,000 | $32,000 | $2,000 |
| #N-22 press | 55,000 | 12,000 | 38,000 | 3,000 |
| #N-31 curing oven | 150,000 | 70,000 | 72,000 | 5,000 |

**Year 2 (period-end emphasis):** Only the **#N-22 press** remains unsold at **December 31, Year 2**. Its fair value has declined to **$34,000**; estimated selling costs are now **$2,500**. No depreciation was taken in Year 2 on the press.

**Required:**  
a. For each asset at Dec 31, Year 1, compute carrying amount, FV − CTS, and impairment loss (if any).  
b. Record the **combined** journal entry for any Year 1 HFS impairments.  
c. State the Year 1 adjusted carrying amount of each asset.  
d. Record the **period-end adjusting entry** for the #N-22 press on Dec 31, Year 2. State its new carrying amount.  

**Answer key:**

**a. Impairment analysis — Dec 31, Year 1**

| Asset | Cost | AD | Carrying amount | FV − CTS | Impairment? | Loss |
|---|---:|---:|---:|---:|---|---:|
| #N-14 packaging line | 80,000 | 50,000 | **30,000** | 32,000 − 2,000 = **30,000** | No (FV − CTS = CA) | $0 |
| #N-22 press | 55,000 | 12,000 | **43,000** | 38,000 − 3,000 = **35,000** | Yes | **8,000** |
| #N-31 curing oven | 150,000 | 70,000 | **80,000** | 72,000 − 5,000 = **67,000** | Yes | **13,000** |
| **Total** | | | | | | **$21,000** |

**b. Combined initial impairment JE**

```
Dec 31, Year 1 — To record impairment loss on assets held for sale
  Dr Loss on Impairment ($8,000 + $13,000) ............ 21,000
     Cr Accumulated Depreciation — Plant Assets .............. 21,000
```
**Check:** Dr 21,000 = Cr 21,000.

(If recorded separately: #N-22 Dr/Cr 8,000; #N-31 Dr/Cr 13,000 — both balance.)

**c. Adjusted carrying amounts — Dec 31, Year 1**

| Asset | Adjusted CA | How computed |
|---|---:|---|
| #N-14 packaging line | **$30,000** | Unchanged ($80,000 − $50,000) |
| #N-22 press | **$35,000** | $55,000 − ($12,000 + $8,000) |
| #N-31 curing oven | **$67,000** | $150,000 − ($70,000 + $13,000) |

**d. Period-end subsequent write-down — #N-22 press, Dec 31, Year 2 (emphasis)**

| Computation | Amount |
|---|---:|
| Carrying amount entering Year 2 remeasurement | $35,000 |
| New FV − CTS ($34,000 − $2,500) | 31,500 |
| **Additional impairment loss** | **$3,500** |

```
Dec 31, Year 2 — To record subsequent write-down of asset held for sale
  Dr Loss on Impairment ............................... 3,500
     Cr Accumulated Depreciation — Plant Assets ............... 3,500
```
**Check:** Dr 3,500 = Cr 3,500.

- New carrying amount of #N-22 press: **$31,500** (= $55,000 − $23,500 AD).  
- Cumulative HFS impairment on press: $8,000 + $3,500 = **$11,500**.  
- Ceiling for any future recovery remains the classification-date CA of **$43,000** (recovery still limited to cumulative losses recognized).

**Key insight:** HFS impairment is a pure **lower-of** test (CA vs FV − CTS) — no undiscounted recoverability screen. Subsequent periods can produce **additional write-downs** or **recoveries** (recovery limited to cumulative prior HFS losses). Period-end remeasurement is required each reporting date while the asset remains held for sale.

---

### Q4 — MC — Measurement of impairment on asset held for sale
**LO:** LO 12-8  
**Concept:** HFS impairment uses lower of carrying amount and fair value less cost to sell (recoverable cost is irrelevant)  
**Question:**  
At a reporting date, **Baycroft Tools Corp.** has equipment **held for sale** with a carrying amount of **$50,000**, estimated undiscounted future net cash flows from use (recoverable cost) of **$48,000**, fair value of **$46,000**, and estimated selling costs of **$1,500**. What impairment loss, if any, should Baycroft recognize for this held-for-sale asset?

- A) $0  
- B) $2,000 loss  
- C) $4,000 loss  
- D) $5,500 loss  

**Answer:** **D.** Held-for-sale assets are measured at the **lower of carrying amount or fair value less cost to sell**. FV − CTS = $46,000 − $1,500 = **$44,500**. Impairment = $50,000 − $44,500 = **$5,500**. Recoverable cost ($48,000) is used for **held-and-used** impairment testing (LO 12-7), not for HFS measurement.  
- A is wrong (a write-down is required).  
- B is the difference between CA and recoverable cost (held-and-used logic misapplied).  
- C is CA − fair value only (ignores selling costs).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (impairments, recoveries, ceilings, disposal residuals)
- [x] Core demo path from Demo 12-8 / Review 12-8 — not Expanding Your Knowledge sidebar
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one classification/measurement MC)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Pier / Review 12-8 figures)
