# Agent 189 — CORE DEMO — LO 10-2

**Chapter:** 10  
**LO title:** Apply lower of cost or market rule to inventory  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **LCM applicability:** lower of cost or market applies only when inventory cost is measured using **LIFO** or the **retail inventory method** (ASC 330); other methods use LCNRV (LO 10-1)
- **Market defined:** current **replacement cost**, limited by a **ceiling** (NRV = selling price − completion/disposal costs) and a **floor** (NRV − approximate normal profit margin)
- **Market shortcut:** choose the **mid-value** among replacement cost, ceiling, and floor
- **Carrying amount:** lower of **cost** and **designated market**; write-down only when market < cost (never write up above cost while units remain on hand)
- **Application levels:** individual item (most common; lowest inventory), category, or inventory in total
- **Initial recognition JE:** charge **COGS** or **Holding Loss on Inventory**; credit Inventory directly or **Allowance to Reduce Inventory to Market**
- **Subsequent measurement schedule (emphasis):** recompute required allowance each period-end; roll forward unadjusted balance to required ending balance
- **Period-end adjusting JE:** true-up allowance (increase or decrease) to match cost − LCM of ending inventory
- **Disposal / settlement:** when written-down inventory is sold, close related allowance into COGS so net COGS equals net carrying amount of inventory sold

---

### Q1 — CORE — Multi-item LCM, multi-year subsequent measurement schedule, period-end JEs, sale settlement
**LO:** LO 10-2  
**Concept:** Individual-item LCM measurement schedule; multi-period subsequent allowance rollforward (emphasis); period-end adjusting JEs; disposal close of allowance on sale  
**Scenario:**  
**CedarPeak Outdoor Gear LLC** measures merchandise inventory using the **LIFO** cost method and applies the **lower of cost or market (LCM)** rule **to each individual inventory item**. The company maintains an **Allowance to Reduce Inventory to Market** and adjusts the allowance only at **year-end** (true-up method) unless a sale-settlement entry is specified.

**Year 1 ending inventory — per-unit data at December 31, Year 1:**

| Item | Qty | Est. selling price | Est. cost to complete & sell | Est. normal profit margin | Original cost (LIFO) | Replacement cost |
|---|---:|---:|---:|---:|---:|---:|
| AlpineShell | 120 | $95 | $15 | $12 | $78 | $70 |
| BaseLayer | 200 | 42 | 6 | 7 | 32 | 38 |
| TrailBoot | 90 | 130 | 22 | 18 | 105 | 88 |
| SummitPoles | 150 | 55 | 8 | 6 | 48 | 40 |
| DayPack | 75 | 110 | 18 | 14 | 72 | 95 |

Additional facts:
- Unadjusted Allowance balance at December 31, Year 1 (before LCM) = **$0**.
- COGS for Year 1 **before** any LCM adjustment = **$412,000**.
- All beginning inventory each year is **sold** by year-end (layers turn fully).
- Aggregate LIFO cost and **designated market** of ending inventory for subsequent years (management has already completed item-level LCM):

| Period-end | Ending inventory at LIFO cost | Designated market (item approach) |
|---|---:|---:|
| December 31, Year 2 | $44,200 | $39,850 |
| December 31, Year 3 | $41,000 | $41,800 |

- On **March 15, Year 3**, assume instead that CedarPeak sells **all** of the Year 2 ending inventory for cash of **$42,500**. Inventory cost on the books is still **$44,200**, and the allowance still carries its December 31, Year 2 credit balance until closed on the sale date (ignore Year 3 year-end inventory for this sale-settlement requirement).

**Required:**  
a. For each Year 1 item, compute **ceiling**, **floor**, designated **market**, and **LCM per unit**. Identify which constraint sets market (RC, ceiling, or floor).  
b. Prepare the **Year 1 LCM measurement schedule** (totals by item: cost, LCM, write-down) and the total required write-down.  
c. Record the **December 31, Year 1 initial recognition JE** charging **Cost of Goods Sold** and crediting the **allowance**. Show balance-sheet inventory presentation and the income-statement effect on COGS.  
d. Prepare a multi-year **subsequent measurement / allowance rollforward schedule** (emphasis) for December 31 of Years 1–3 under the year-end true-up method (do **not** close the allowance when inventory turns—adjust only at year-end). Columns: inventory cost; designated market; required allowance; unadjusted allowance; adjustment Dr/(Cr) to allowance; ending allowance; inventory, net.  
e. Record the **period-end adjusting JEs** for December 31 of Years 1, 2, and 3 consistent with the schedule in (d). Use COGS for the equity-side effect.  
f. **Disposal / settlement alternative:** Record the **March 15, Year 3** sale of all Year 2 inventory for cash and the entry to **close the December 31, Year 2 allowance** into COGS. Compute **net COGS** related to this inventory layer.

**Answer key:**

**(a) Per-unit market determination**  
Ceiling = estimated selling price − costs to complete/sell (NRV).  
Floor = ceiling − normal profit margin.  
Market = mid-value of {replacement cost, ceiling, floor}.

| Item | Ceiling | Floor | RC | **Market** | Constraint | Cost | **LCM / unit** |
|---|---:|---:|---:|---:|---|---:|---:|
| AlpineShell | 95−15=**80** | 80−12=**68** | 70 | **70** | RC (between floor & ceiling) | 78 | **70** |
| BaseLayer | 42−6=**36** | 36−7=**29** | 38 | **36** | Ceiling (RC > ceiling) | 32 | **32** |
| TrailBoot | 130−22=**108** | 108−18=**90** | 88 | **90** | Floor (RC < floor) | 105 | **90** |
| SummitPoles | 55−8=**47** | 47−6=**41** | 40 | **41** | Floor (RC < floor) | 48 | **41** |
| DayPack | 110−18=**92** | 92−14=**78** | 95 | **92** | Ceiling (RC > ceiling) | 72 | **72** |

Notes: BaseLayer and DayPack have cost ≤ market → no unit write-down. AlpineShell, TrailBoot, and SummitPoles write down to market.

**(b) Year 1 LCM measurement schedule (individual-item approach)**

| Item | Qty | Cost total | LCM / unit | LCM total | Write-down |
|---|---:|---:|---:|---:|---:|
| AlpineShell | 120 | 120×78=**9,360** | 70 | 120×70=**8,400** | **960** |
| BaseLayer | 200 | 200×32=**6,400** | 32 | **6,400** | **0** |
| TrailBoot | 90 | 90×105=**9,450** | 90 | 90×90=**8,100** | **1,350** |
| SummitPoles | 150 | 150×48=**7,200** | 41 | 150×41=**6,150** | **1,050** |
| DayPack | 75 | 75×72=**5,400** | 72 | **5,400** | **0** |
| **Total** | | **$37,810** | | **$34,450** | **$3,360** |

Check: \(37{,}810 - 34{,}450 = 3{,}360\); unit write-downs \(960 + 1{,}350 + 1{,}050 = 3{,}360\).

**(c) December 31, Year 1 — initial recognition JE**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 3,360 | |
| Allowance to Reduce Inventory to Market | | 3,360 |
| *Dec 31, Y1 — reduce LIFO inventory to market (item LCM)* | | |

**Check:** Dr 3,360 = Cr 3,360. **Balanced.**

| Balance sheet | Amount |
|---|---:|
| Inventory (at LIFO cost) | $37,810 |
| Less: Allowance to Reduce Inventory to Market | (3,360) |
| **Inventory, net** | **$34,450** |

| Income statement | Amount |
|---|---:|
| COGS before LCM | $412,000 |
| LCM write-down | 3,360 |
| **COGS after LCM** | **$415,360** |

**(d) Subsequent measurement / allowance rollforward schedule (emphasis)**

| Period-end | Inv. cost | Designated market | Required allow. | Unadj. allow. | Adj. Dr/(Cr) to allow. | Ending allow. | Inventory, net |
|---|---:|---:|---:|---:|---:|---:|---:|
| Dec 31, Y1 | $37,810 | $34,450 | $3,360 | $0 | **Cr 3,360** | $3,360 | $34,450 |
| Dec 31, Y2 | 44,200 | 39,850 | 4,350 | 3,360 | **Cr 990** | 4,350 | 39,850 |
| Dec 31, Y3 | 41,000 | 41,800 | **0** | 4,350 | **Dr 4,350** | 0 | 41,000 |

**Schedule math checks:**  
- Y1 required = \(37{,}810 - 34{,}450 = 3{,}360\).  
- Y2 required = \(44{,}200 - 39{,}850 = 4{,}350\); additional credit = \(4{,}350 - 3{,}360 = 990\).  
- Y3: market \(41{,}800 >\) cost \(41{,}000\) → LCM = cost → required allowance **$0**; reverse unadjusted credit \(4{,}350\).  
- Inventory, net = cost − ending allowance each year.  
- *Note:* Y3 debit to the allowance is a **true-up for new ending inventory** that does not require a write-down (prior units turned). It is **not** a write-up of the same units previously written down while still on hand.

**(e) Period-end adjusting JEs (true-up method)**

*December 31, Year 1* — same as (c):

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 3,360 | |
| Allowance to Reduce Inventory to Market | | 3,360 |

**Check:** Dr = Cr = 3,360. **Balanced.**

*December 31, Year 2*

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 990 | |
| Allowance to Reduce Inventory to Market | | 990 |
| *Increase allowance to $4,350 required balance* | | |

**Check:** Dr = Cr = 990. **Balanced.** Ending allowance = \(3{,}360 + 990 = 4{,}350\).

*December 31, Year 3*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 4,350 | |
| Cost of Goods Sold | | 4,350 |
| *Reduce allowance to $0; new EI needs no LCM reserve* | | |

**Check:** Dr = Cr = 4,350. **Balanced.** Ending allowance **$0**; inventory, net = **$41,000**.

**(f) March 15, Year 3 — disposal / settlement of written-down inventory**

Sale of inventory:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 42,500 | |
| Sales Revenue | | 42,500 |
| *Cash sale of Year 2 ending inventory* | | |

**Check:** Dr = Cr = 42,500. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 44,200 | |
| Inventory | | 44,200 |
| *Remove inventory at LIFO cost* | | |

**Check:** Dr = Cr = 44,200. **Balanced.**

Close related allowance (Dec 31, Y2 balance $4,350):

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 4,350 | |
| Cost of Goods Sold | | 4,350 |
| *Close allowance on sale of written-down inventory* | | |

**Check:** Dr = Cr = 4,350. **Balanced.**

**Net COGS** on this layer = \(44{,}200 - 4{,}350 = \mathbf{\$39{,}850}\) (equals prior inventory, net).  
Gross profit on layer = \(42{,}500 - 39{,}850 = \mathbf{\$2{,}650}\).

**Key insight:** Market is replacement cost **corridor-constrained** by ceiling and floor. The **subsequent measurement schedule** tracks the allowance as a valuation account that is remeasured each period-end; when inventory is sold, closing the allowance into COGS makes net COGS equal the inventory’s **net carrying amount**.

---

### Q2 — CORE number variant — BlueRidge Camp & Climb: LCM twin + Year-2 subsequent true-up
**LO:** LO 10-2  
**Concept:** Number-variant twin — individual-item LCM schedule, initial write-down JE, subsequent Year-2 allowance adjustment schedule  
**Scenario:**  
**BlueRidge Camp & Climb Inc.** uses **LIFO** and applies LCM **by individual item**. Unadjusted allowance at the start of the measurement is **$0**. Fiscal year-end is **December 31**.

**December 31, Year 4 inventory:**

| Item | Qty | Selling price / unit | Cost to sell / unit | Normal profit / unit | Cost / unit | Replacement cost / unit |
|---|---:|---:|---:|---:|---:|---:|
| CragHarness | 80 | $160 | $25 | $20 | $125 | $130 |
| GripChalk | 300 | 18 | 2 | 3 | 14 | 11 |
| FixedCam | 45 | 210 | 30 | 25 | 180 | 155 |

**December 31, Year 5:** Ending inventory at LIFO cost = **$28,600**; designated market (item approach) = **$25,900**. All Year 4 ending inventory was sold during Year 5. Allowance is adjusted only at year-end (true-up). COGS before LCM in Year 4 = **$195,000**.

**Required:**  
a. Compute ceiling, floor, market, and LCM per unit for each Year 4 item; identify the market constraint.  
b. Compute total inventory at cost, at LCM, and the required Year 4 write-down.  
c. Prepare the December 31, Year 4 journal entry (allowance + COGS).  
d. Prepare the **Year 4 → Year 5 subsequent measurement schedule** for the allowance (required, unadjusted, adjustment, ending) and the December 31, Year 5 adjusting JE.  
e. State inventory, net at December 31, Year 4 and Year 5.

**Answer key:**

**(a) Per-unit computations**

| Item | Ceiling | Floor | RC | Market | Why | Cost | LCM |
|---|---:|---:|---:|---:|---|---:|---:|
| CragHarness | 160−25=**135** | 135−20=**115** | 130 | **130** | RC between | 125 | **125** |
| GripChalk | 18−2=**16** | 16−3=**13** | 11 | **13** | Floor (RC < floor) | 14 | **13** |
| FixedCam | 210−30=**180** | 180−25=**155** | 155 | **155** | RC = floor | 180 | **155** |

**(b) Totals**

| Item | Cost total | LCM total | Write-down |
|---|---:|---:|---:|
| CragHarness | 80×125=**10,000** | 80×125=**10,000** | **0** |
| GripChalk | 300×14=**4,200** | 300×13=**3,900** | **300** |
| FixedCam | 45×180=**8,100** | 45×155=**6,975** | **1,125** |
| **Total** | **$22,300** | **$20,875** | **$1,425** |

Check: \(22{,}300 - 20{,}875 = 1{,}425\); \(300 + 1{,}125 = 1{,}425\).

**(c) December 31, Year 4 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 1,425 | |
| Allowance to Reduce Inventory to Market | | 1,425 |
| *Y4 — LCM write-down (item approach)* | | |

**Check:** Dr = Cr = 1,425. **Balanced.**  
COGS after LCM = \(195{,}000 + 1{,}425 = \mathbf{\$196{,}425}\).

**(d) Subsequent measurement schedule Year 4 → Year 5 & Y5 JE**

| Period-end | Inv. cost | Designated market | Required allow. | Unadj. allow. | Adj. Dr/(Cr) | Ending allow. |
|---|---:|---:|---:|---:|---:|---:|
| Dec 31, Y4 | $22,300 | $20,875 | $1,425 | $0 | **Cr 1,425** | $1,425 |
| Dec 31, Y5 | 28,600 | 25,900 | 2,700 | 1,425 | **Cr 1,275** | 2,700 |

Y5 required = \(28{,}600 - 25{,}900 = \mathbf{\$2{,}700}\); additional credit = \(2{,}700 - 1{,}425 = \mathbf{\$1{,}275}\).

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 1,275 | |
| Allowance to Reduce Inventory to Market | | 1,275 |
| *Y5 — increase allowance to $2,700* | | |

**Check:** Dr = Cr = 1,275. **Balanced.**

**(e) Inventory, net**  
- Dec 31, Y4: \(22{,}300 - 1{,}425 = \mathbf{\$20{,}875}\)  
- Dec 31, Y5: \(28{,}600 - 2{,}700 = \mathbf{\$25{,}900}\)

**Key insight:** Same LCM corridor mechanics as Q1 with all numbers changed; the **subsequent measurement schedule** is the control for how much additional (or reduced) allowance hits earnings each year-end.

---

### Q3 — CORE alternate angle — Item / category / total LCM; Holding Loss JE; sale settlement
**LO:** LO 10-2  
**Concept:** Apply LCM at item, category, and total levels; period-end Holding Loss JE; disposal close of allowance when inventory sold  
**Scenario:**  
**StormBay Marine Supply Co.** uses **LIFO** and has completed designation of **market** for each item (ceiling/floor already applied). Management is deciding the **application level** for LCM. Allowance method is used. Unadjusted allowance = **$0**. COGS before LCM = **$276,000**.

| Item | Category | LIFO cost | Designated market |
|---|---|---:|---:|
| Anchor-A | Anchors | $8,000 | $7,200 |
| Anchor-B | Anchors | 6,500 | 7,000 |
| Rope-X | Ropes | 12,000 | 11,000 |
| Rope-Y | Ropes | 9,500 | 8,800 |
| Fender-P | Fenders | 5,000 | 5,400 |
| **Total** | | **$41,000** | **$39,400** |

During Year 2, **all** of this inventory is sold for cash of **$43,000**. StormBay closes the related allowance into COGS on the sale date (treat sale as a single mid-year event).

**Required:**  
a. Compute inventory at LCM and the write-down under **(1) individual items**, **(2) each category**, and **(3) inventory in total**.  
b. Using the **individual-item** approach, record the period-end adjusting entry charging **Holding Loss on Inventory** (credit allowance). Show BS inventory net and IS effect (Holding Loss method).  
c. Record the **disposal / settlement** entries when the inventory is sold in Year 2 (sale, remove inventory at cost, close allowance). Compute net COGS and gross profit on the layer.  
d. Briefly state: (1) when LCM (vs LCNRV) is required; (2) whether a prior write-down may be reversed if market recovers while the **same units** remain on hand.

**Answer key:**

**(a) LCM by application level**

**Individual items (lower of cost or market per item):**

| Item | Cost | Market | LCM — item |
|---|---:|---:|---:|
| Anchor-A | 8,000 | 7,200 | **7,200** |
| Anchor-B | 6,500 | 7,000 | **6,500** |
| Rope-X | 12,000 | 11,000 | **11,000** |
| Rope-Y | 9,500 | 8,800 | **8,800** |
| Fender-P | 5,000 | 5,400 | **5,000** |
| **Total** | **41,000** | **39,400** | **$38,500** |

Item write-down = \(41{,}000 - 38{,}500 = \mathbf{\$2{,}500}\).

**By category:**

| Category | Cost | Market | LCM — category |
|---|---:|---:|---:|
| Anchors | \(8{,}000+6{,}500=14{,}500\) | \(7{,}200+7{,}000=14{,}200\) | **14,200** |
| Ropes | \(12{,}000+9{,}500=21{,}500\) | \(11{,}000+8{,}800=19{,}800\) | **19,800** |
| Fenders | 5,000 | 5,400 | **5,000** |
| **Total** | **41,000** | | **$39,000** |

Category write-down = \(41{,}000 - 39{,}000 = \mathbf{\$2{,}000}\).

**By total inventory:** \(\min(41{,}000,\ 39{,}400) = \mathbf{\$39{,}400}\); write-down = \(\mathbf{\$1{,}600}\).

| Application level | Inventory at LCM | Write-down vs cost $41,000 |
|---|---:|---:|
| Individual items | **$38,500** | **$2,500** |
| Categories | $39,000 | $2,000 |
| Total inventory | $39,400 | $1,600 |

Item approach produces the **lowest** inventory (no offsetting of Anchor-B / Fender-P “surpluses” against deficits).

**(b) Period-end JE — item approach, Holding Loss method**

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 2,500 | |
| Allowance to Reduce Inventory to Market | | 2,500 |
| *Reduce LIFO inventory to market (item LCM)* | | |

**Check:** Dr = Cr = 2,500. **Balanced.**

| Balance sheet | Amount |
|---|---:|
| Inventory (at LIFO cost) | $41,000 |
| Less: Allowance to Reduce Inventory to Market | (2,500) |
| **Inventory, net** | **$38,500** |

| Income statement (Holding Loss method) | Amount |
|---|---:|
| Cost of goods sold (unadjusted) | $276,000 |
| Holding loss on inventory | 2,500 |
| Effect on pretax income | −2,500 |

**(c) Disposal / settlement when inventory sold**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 43,000 | |
| Sales Revenue | | 43,000 |

**Check:** Dr = Cr = 43,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 41,000 | |
| Inventory | | 41,000 |

**Check:** Dr = Cr = 41,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 2,500 | |
| Cost of Goods Sold | | 2,500 |
| *Close allowance related to inventory sold* | | |

**Check:** Dr = Cr = 2,500. **Balanced.**

Net COGS = \(41{,}000 - 2{,}500 = \mathbf{\$38{,}500}\).  
Gross profit = \(43{,}000 - 38{,}500 = \mathbf{\$4{,}500}\).

**(d) Classification / recovery**  
1. **LCM** is required when cost is measured using **LIFO** or the **retail inventory method**. Methods other than LIFO/retail (e.g., FIFO, average cost) use **lower of cost or NRV**.  
2. **No.** A write-down establishes a new cost basis; the company does **not** reverse the loss in later periods if market recovers while the **same units** remain on hand. Recovery is recognized only through sale (higher margin / lower net COGS).

**Key insight:** Application level changes the write-down because surpluses on some items can offset deficits only when LCM is applied by category or in total. Disposal closes the valuation allowance so net COGS matches net inventory carrying amount.

---

### Q4 — MC (classification / method)
**LO:** LO 10-2  
**Concept:** LCM applicability and mid-value market designation  

**Question 1:**  
Under U.S. GAAP (ASC 330), the **lower of cost or market** rule—where market is replacement cost limited by a ceiling and a floor—applies when inventory cost is measured using which methods?

- A) FIFO and weighted-average only  
- B) All inventory cost methods  
- C) **LIFO** or the **retail inventory method** only  
- D) Only agricultural commodities stated above cost  

**Answer:** **C.** LCM with the replacement-cost corridor applies to **LIFO** and **retail**. Other methods use **lower of cost or NRV** (LO 10-1).

---

**Question 2:**  
A LIFO inventory item has: replacement cost **$72**, net realizable value (ceiling) **$80**, and NRV less normal profit (floor) **$68**. Original cost is **$90**. Designated **market** and **LCM carrying amount** are:

- A) Market $72; LCM $72  
- B) Market $80; LCM $80  
- C) Market $68; LCM $68  
- D) Market $72; LCM $90  

**Answer:** **A.** RC $72 lies **between** floor $68 and ceiling $80, so market = **$72**. LCM = lower of cost $90 and market $72 = **$72**. (Mid-value of {72, 80, 68} = 72.)

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (per-unit corridors, item totals, multi-year allowance rollforwards, category/total LCM)
- [x] Core demo not sidebar-only (Demo 10-2 / Review 10-2 path: LCM, ceiling/floor, market mid-value, write-down JE, allowance subsequent measurement)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook Demo 10-2 / Review 10-2 figures)
