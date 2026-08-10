# Agent 205 — CORE DEMO — LO 11-9

**Chapter:** 11  
**LO title:** Account for exchange of property, plant, and equipment  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- Nonmonetary PPE exchange: remove old asset (cost + accum. dep.), record cash paid/received, record new asset, record gain/loss (subject to commercial-substance rules)
- **Commercial substance:** future cash flows (risk, timing, or amount) significantly change → **full gain and full loss** recognized; new asset at FV of asset given up ± cash (or FV received if more clearly evident)
- **Lack of commercial substance — gains:** fully **deferred** if no cash or cash is **paid**; **partial gain** if cash is **received** (boot)
- Partial gain formula: \(\frac{\text{Cash received}}{\text{Cash received} + \text{FV of other assets received}} \times \text{total potential gain}\)
- **Losses:** always fully recognized (whether or not commercial substance) so new asset is not capitalized above FV
- **Period-end / update adjusting JE:** accumulate depreciation to the **exchange date** before recording the exchange
- **Subsequent measurement schedule (emphasis):** depreciation of the **new** asset uses its exchange-date cost basis (FV-based if gain recognized; carrying-amount-based if gain deferred) over remaining useful life
- Cash ≥ 25% of exchange FV → entire gain recognized (ASC 845-10-25-6) — awareness only; core demos stay below that threshold when partial gain applies

---

### Q1 — CORE — Commercial substance: dep update, exchange JE, multi-year subsequent dep schedule
**LO:** LO 11-9  
**Concept:** Full gain recognition on PPE exchange with commercial substance (cash paid); update depreciation to exchange date; subsequent straight-line measurement schedule on the new asset’s FV-based cost  
**Scenario:**  
**Ridgeway Fabricators Inc.** (calendar year-end) purchased a **hydraulic press** on **January 1, Year 1** for **$80,000**. Residual value **$0**; useful life **10 years**; straight-line depreciation; full years of depreciation in Years 1–3.

On **July 1, Year 4**, Ridgeway exchanges the press plus **$40,000 cash** for a **CNC milling machine**. The press has a **fair value of $55,000** on the exchange date (more reliable than the CNC’s list price). The exchange has **commercial substance**.  

The CNC has residual value **$5,000** and a useful life of **8 years** from the acquisition date. Ridgeway uses straight-line depreciation and records a **half-year** of depreciation on the CNC in Year 4.

**Required:**  
a. Prepare a **subsequent measurement (depreciation) schedule for the old press** from acquisition through the exchange date (show annual dep, accum. dep., and book value; include the Year 4 half-year update).  
b. Record the **July 1, Year 4 adjusting JE** to update depreciation on the press.  
c. Compute the **book value** of the press, the **gain or loss**, and the **initial cost of the CNC**. Record the **July 1, Year 4 exchange JE**.  
d. Prepare the **subsequent measurement schedule for the CNC** for Years 4–6 (and state the annual full-year depreciation for later years).  
e. Record the **December 31, Year 4** depreciation adjusting JE for the CNC.

**Answer key:**  

**a. Old press — depreciation rollforward through exchange**

Annual depreciation on press = \(\$80{,}000 / 10 = \$8{,}000\).  
Year 4 half-year (Jan 1–July 1) = \(\$8{,}000 \times 6/12 = \$4{,}000\).

| Period | Depreciation | Accum. dep. (end) | Book value (end) |
|---|---:|---:|---:|
| Jan. 1, Year 1 (acq.) | — | $0 | $80,000 |
| Year 1 | $8,000 | 8,000 | 72,000 |
| Year 2 | 8,000 | 16,000 | 64,000 |
| Year 3 | 8,000 | 24,000 | 56,000 |
| Year 4 H1 (to July 1) | **4,000** | **28,000** | **52,000** |

**Check:** BV at exchange = \(80{,}000 - 28{,}000 = 52{,}000\).

**b. July 1, Year 4 — period-end / update adjusting JE (press)**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Press | 4,000 | |
| Accumulated Depreciation—Press | | 4,000 |
| *Update depreciation on press to exchange date (½ year)* | | |

**Check:** Dr 4,000 = Cr 4,000. **Balanced.**

**c. Exchange measurement and initial recognition JE**

| Item | Amount |
|---|---:|
| Fair value of press given up | $55,000 |
| Cash paid | 40,000 |
| **Cost of CNC (FV given up + cash paid)** | **$95,000** |
| Book value of press | 52,000 |
| **Gain on exchange** (\(55{,}000 - 52{,}000\)) | **$3,000** |

Full gain is recognized because the exchange has **commercial substance**.

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—CNC Mill | 95,000 | |
| Accumulated Depreciation—Press | 28,000 | |
| Cash | | 40,000 |
| Equipment—Hydraulic Press | | 80,000 |
| Gain on Asset Exchange | | 3,000 |
| *Nonmonetary exchange with commercial substance; full gain recognized* | | |

**Check:** Dr \(95{,}000 + 28{,}000 = 123{,}000\); Cr \(40{,}000 + 80{,}000 + 3{,}000 = 123{,}000\). **Balanced.**

**d. Subsequent measurement schedule — CNC (emphasis)**

Depreciable base = \(\$95{,}000 - \$5{,}000 = \$90{,}000\).  
Full-year depreciation = \(\$90{,}000 / 8 = \$11{,}250\).  
Year 4 (half-year from July 1) = \(\$11{,}250 \times 1/2 = \$5{,}625\).

| Year | Beg. carrying amount | Depreciation expense | End. accum. dep. | End. carrying amount |
|---|---:|---:|---:|---:|
| Year 4 (½ yr) | $95,000 | **$5,625** | $5,625 | **$89,375** |
| Year 5 | 89,375 | **11,250** | 16,875 | **78,125** |
| Year 6 | 78,125 | **11,250** | 28,125 | **66,875** |

Thereafter (Years 7–11 full years): **$11,250** per year; final half-year in Year 12 brings carrying amount to residual **$5,000**.  
**Rollforward check Year 4–6:** \(95{,}000 - 5{,}625 - 11{,}250 - 11{,}250 = 66{,}875\).

**e. December 31, Year 4 — CNC depreciation adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—CNC | 5,625 | |
| Accumulated Depreciation—CNC | | 5,625 |
| *½ year SL on CNC acquired July 1 (cost $95,000 − residual $5,000) / 8 × ½* | | |

**Check:** Dr 5,625 = Cr 5,625. **Balanced.**

**Key insight:** With commercial substance, the new PPE is capitalized at **FV of the asset given up + cash paid**, and the **full unrealized holding gain** on the old asset is recognized. The **subsequent depreciation schedule** is driven by that **FV-based cost**, not the old book value—so higher gain recognition means higher future depreciation.

---

### Q2 — CORE number variant — Lack of commercial substance, cash paid (gain deferred); update + new-asset schedule
**LO:** LO 11-9  
**Concept:** Number-variant twin: gain on exchange lacking commercial substance with cash **paid** is fully deferred; new asset recorded at carrying amount of assets given up; subsequent dep schedule on stepped-down cost basis  
**Scenario:**  
**Solstice Packaging Co.** (calendar year-end) acquired a **filler machine** on **January 1, Year 1** for **$96,000**. Residual **$0**; useful life **8 years**; straight-line.

On **April 1, Year 5**, Solstice exchanges the filler plus **$10,000 cash** for a **similar** filler better suited to a different product line. The fair value of the old filler is **$50,000**. The exchange **lacks commercial substance** (cash-flow risk/timing/amount not expected to change significantly).  

The new filler has residual value **$5,000** and a useful life of **5 years** from April 1, Year 5. Straight-line depreciation; Year 5 takes **9/12** of a full year.

**Required:**  
a. Prepare the **depreciation rollforward for the old filler** through April 1, Year 5 (include the Year 5 partial-year update).  
b. Record the **April 1, Year 5 adjusting JE** to update depreciation.  
c. Compute **potential gain**, amount of gain **recognized vs deferred**, and **cost assigned to the new filler**. Record the **exchange JE**.  
d. Prepare the **subsequent measurement schedule** for the new filler for Years 5–7 (and state annual full-year dep).  
e. Record the **December 31, Year 5** depreciation JE for the new filler.  
f. Briefly state how the **new-asset cost and Year 5 depreciation** would differ if the exchange **had** commercial substance.

**Answer key:**  

**a. Old filler — dep through exchange**

Annual dep = \(\$96{,}000 / 8 = \$12{,}000\).  
Through Dec. 31, Year 4: 4 full years → accum. dep. = \(4 \times 12{,}000 = \$48{,}000\); BV = \(96{,}000 - 48{,}000 = \$48{,}000\).  
Year 5 Jan 1–Apr 1 (3/12): \(12{,}000 \times 3/12 = \$3{,}000\).

| Period | Depreciation | Accum. dep. (end) | Book value (end) |
|---|---:|---:|---:|
| Years 1–4 (combined) | $48,000 | $48,000 | $48,000 |
| Year 5 Q1 (to Apr 1) | **3,000** | **51,000** | **45,000** |

**b. April 1, Year 5 — update adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Filler (old) | 3,000 | |
| Accumulated Depreciation—Filler (old) | | 3,000 |
| *Update dep on old filler to exchange date (3/12 year)* | | |

**Check:** Dr 3,000 = Cr 3,000. **Balanced.**

**c. Gain analysis and exchange JE (lack CS; cash paid)**

| Item | Amount |
|---|---:|
| FV of old filler | $50,000 |
| Book value of old filler | 45,000 |
| **Total potential gain** | **$5,000** |
| Cash paid | 10,000 |
| Gain recognized (cash paid + lack CS) | **$0** (fully deferred) |
| **Cost of new filler** = BV old + cash paid = \(45{,}000 + 10{,}000\) | **$55,000** |

(Alternative view: FV-based cost would be \(50{,}000 + 10{,}000 = 60{,}000\); deferred gain of $5,000 reduces new asset to $55,000.)

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—New Filler | 55,000 | |
| Accumulated Depreciation—Old Filler | 51,000 | |
| Cash | | 10,000 |
| Equipment—Old Filler | | 96,000 |
| *Exchange lacking commercial substance; cash paid → gain fully deferred* | | |

**Check:** Dr \(55{,}000 + 51{,}000 = 106{,}000\); Cr \(10{,}000 + 96{,}000 = 106{,}000\). **Balanced.** No gain account.

**d. Subsequent measurement schedule — new filler (emphasis)**

Depreciable base = \(\$55{,}000 - \$5{,}000 = \$50{,}000\).  
Full-year dep = \(\$50{,}000 / 5 = \$10{,}000\).  
Year 5 (9/12 from Apr 1) = \(\$10{,}000 \times 9/12 = \$7{,}500\).

| Year | Beg. carrying amount | Depreciation expense | End. accum. dep. | End. carrying amount |
|---|---:|---:|---:|---:|
| Year 5 (9/12) | $55,000 | **$7,500** | $7,500 | **$47,500** |
| Year 6 | 47,500 | **10,000** | 17,500 | **37,500** |
| Year 7 | 37,500 | **10,000** | 27,500 | **27,500** |

Years 8–9: full **$10,000** each year; residual **$5,000** remaining after Year 9 (5-year life from Apr 1 Y5 ends Mar 31 Y10 — final 3/12 in Y10 = $2,500 if partial-year convention applied consistently).  
**Rollforward Y5–Y7:** \(55{,}000 - 7{,}500 - 10{,}000 - 10{,}000 = 27{,}500\).

**e. December 31, Year 5 — new filler dep JE**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—New Filler | 7,500 | |
| Accumulated Depreciation—New Filler | | 7,500 |
| *9/12 year SL on new filler (cost $55,000 − residual $5,000) / 5 × 9/12* | | |

**Check:** Dr 7,500 = Cr 7,500. **Balanced.**

**f. Counterfactual — commercial substance**  
New filler cost = \(50{,}000 + 10{,}000 = \$60{,}000\); full gain **$5,000** recognized.  
Full-year dep = \((60{,}000 - 5{,}000)/5 = \$11{,}000\); Year 5 dep = \(11{,}000 \times 9/12 = \$8{,}250\).  
Deferring the gain under lack of CS **lowers** both the capitalized cost and future depreciation by the deferred amount ($5,000 cost / 5 years = $1,000 less full-year dep).

**Key insight:** When the exchange **lacks commercial substance** and the company **pays** cash, any potential gain is **fully deferred** into a lower new-asset basis (BV transferred + cash). The **subsequent measurement schedule** therefore uses that lower basis—exam trap is recording the new asset at FV + cash as if commercial substance existed.

---

### Q3 — CORE alternate angles — Loss (always full) + partial gain (cash received, lack CS)
**LO:** LO 11-9  
**Concept:** (1) Losses fully recognized whether or not commercial substance; (2) partial gain when cash is **received** and commercial substance is lacking; disposal of old asset via exchange  
**Scenario:**  

**Part A — Loss on exchange (commercial substance irrelevant for loss amount)**  
**Northfield Transit LLC** exchanges an old bus (cost **$90,000**, accum. dep. **already updated** to **$60,000**) for a smaller van and receives **$5,000 cash**. Fair value of the bus is **$22,000**. Record Northfield’s exchange entry. State whether the entry changes if the exchange **lacks** commercial substance.

**Part B — Partial gain (cash received; lacks commercial substance)**  
**Cedarline Optics Co.** exchanges a microscope (cost **$70,000**, accum. dep. **updated** **$40,000**) for similar lab equipment with fair value **$32,000** and receives **$8,000 cash**. Fair value of the microscope given up is **$40,000**. The exchange **lacks commercial substance**.  

After the exchange, the new equipment has residual **$0** and a **4-year** life, straight-line, full year in the year of exchange (acquired Jan 1).

**Required:**  
a. **Part A:** Compute loss and new asset cost; record the exchange JE; comment on lack of commercial substance.  
b. **Part B:** Compute total potential gain, partial gain recognized, deferred gain, and cost of new equipment; record the exchange JE.  
c. **Part B:** Prepare a **4-year subsequent measurement schedule** for the new equipment and the Year 1 depreciation JE.  
d. Verify both exchange JEs balance (Dr = Cr).

**Answer key:**  

**a. Part A — Loss fully recognized**

| Item | Amount |
|---|---:|
| Book value of bus (\(90{,}000 - 60{,}000\)) | $30,000 |
| Fair value of bus | 22,000 |
| **Loss on exchange** | **$8,000** |
| Cash received | 5,000 |
| **Cost of van** (\(22{,}000 - 5{,}000\)) | **$17,000** |

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—Van | 17,000 | |
| Accumulated Depreciation—Bus | 60,000 | |
| Cash | 5,000 | |
| Loss on Asset Exchange | 8,000 | |
| Equipment—Bus | | 90,000 |
| *Exchange with loss; full loss recognized* | | |

**Check:** Dr \(17{,}000 + 60{,}000 + 5{,}000 + 8{,}000 = 90{,}000\); Cr \(90{,}000\). **Balanced.**

If the exchange **lacked** commercial substance, the entry is **identical**: losses are **always fully recognized** so the new asset is not recorded above fair value.

**b. Part B — Partial gain (cash received; lack CS)**

| Item | Amount |
|---|---:|
| FV of microscope given up | $40,000 |
| Book value (\(70{,}000 - 40{,}000\)) | 30,000 |
| **Total potential gain** | **$10,000** |
| Cash received | 8,000 |
| FV of other assets received (new equipment) | 32,000 |
| Cash + FV other received | 40,000 |
| **Partial gain recognized** \(\frac{8{,}000}{40{,}000} \times 10{,}000\) | **$2,000** |
| Deferred gain (\(10{,}000 - 2{,}000\)) | 8,000 |
| **Cost of new equipment** = FV given up − cash − deferred gain = \(40{,}000 - 8{,}000 - 8{,}000\) | **$24,000** |

(Equiv.: FV of new equipment − deferred gain = \(32{,}000 - 8{,}000 = 24{,}000\).)

| Account | Debit | Credit |
|---|---:|---:|
| Equipment—New Lab Equipment | 24,000 | |
| Accumulated Depreciation—Microscope | 40,000 | |
| Cash | 8,000 | |
| Gain on Asset Exchange | | 2,000 |
| Equipment—Microscope | | 70,000 |
| *Lack CS; cash received → partial gain only* | | |

**Check:** Dr \(24{,}000 + 40{,}000 + 8{,}000 = 72{,}000\); Cr \(2{,}000 + 70{,}000 = 72{,}000\). **Balanced.**

**c. Part B — subsequent measurement schedule (new equipment)**

Cost $24,000; residual $0; 4 years SL → annual dep = \(\$24{,}000 / 4 = \$6{,}000\).

| Year | Beg. carrying amount | Depreciation | End. carrying amount |
|---|---:|---:|---:|
| 1 | $24,000 | **$6,000** | $18,000 |
| 2 | 18,000 | 6,000 | 12,000 |
| 3 | 12,000 | 6,000 | 6,000 |
| 4 | 6,000 | 6,000 | 0 |
| **Totals** | | **$24,000** | |

Year 1 depreciation JE:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Lab Equipment | 6,000 | |
| Accumulated Depreciation—Lab Equipment | | 6,000 |
| *Full-year SL on new equipment recorded at deferred-gain basis $24,000* | | |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**  
**Schedule check:** total dep over life = cost = $24,000.

**d. Balance summary**  
- Part A exchange: Dr = Cr = $90,000  
- Part B exchange: Dr = Cr = $72,000  
- Part B Year 1 dep: Dr = Cr = $6,000  

**Key insight:** **Losses** are never deferred. **Gains** without commercial substance are deferred entirely when no cash or cash is paid; when **cash (boot) is received**, only the **cash proportion** of the potential gain is recognized, and the remainder **reduces the new asset’s cost**—which then flows through the **subsequent depreciation schedule**.

---

### Q4 — MC — Gain recognition classification in nonmonetary exchanges
**LO:** LO 11-9  
**Concept:** Classify when full gain, no gain, or partial gain is recognized on a PPE exchange  
**Question:**  
Pinnacle Industrial has equipment with a book value of $40,000 and a fair value of $50,000. It exchanges the equipment in a transaction that **lacks commercial substance**. Which situation correctly states the gain Pinnacle recognizes?

- A) No cash is exchanged → recognize full gain of $10,000  
- B) Pinnacle **pays** $6,000 cash → recognize full gain of $10,000  
- C) Pinnacle **receives** $10,000 cash and other assets with FV $40,000 → recognize partial gain of $2,000  
- D) Pinnacle **receives** $10,000 cash and other assets with FV $40,000 → recognize full gain of $10,000  

**Answer:** **C.**  
Potential gain = \(50{,}000 - 40{,}000 = \$10{,}000\). With lack of commercial substance and cash **received**, partial gain = \(\frac{10{,}000}{10{,}000 + 40{,}000} \times 10{,}000 = \$2{,}000\).  
A and B are wrong because when cash is **not received** (none or paid), the gain is **fully deferred** (recognized gain $0). D is wrong because full gain applies to commercial substance (or losses), not to lack-of-CS cash-received cases.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (BV, gains/losses, partial gain formula, dep schedules roll forward)
- [x] Core demo not sidebar-only (Demo 11-9A/B path: commercial substance, lack CS cash paid, lack CS cash received, losses always full)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC on gain-recognition classification)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE (exchange removes old asset)
- [x] Original company names/numbers (not Tacoma/Lambou textbook figures)
