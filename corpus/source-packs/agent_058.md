# Agent 58 — CORE DEMO — LO 10-2

**Chapter:** 10  
**LO title:** Apply lower of cost or market rule to inventory  
**Critical gap LO:** no

## Concept list for this pack
- LCM applies only when cost is measured with **LIFO** or the **retail inventory method**
- **Market** = current replacement cost, constrained by **ceiling** (NRV) and **floor** (NRV − normal profit margin)
- Market = mid-value among replacement cost, ceiling, and floor
- Inventory reported at **lower of cost or market** by item / category / total (item approach most common)
- Period-end **initial recognition JE**: write inventory down via Allowance (or direct credit) and COGS or Holding Loss
- **Subsequent measurement schedule**: recompute required allowance each period-end
- Allowance rollforward when beginning inventory is sold and ending inventory needs a new market write-down
- **Disposal / settlement of write-down**: allowance closed into COGS when related inventory is sold (or absorbed via year-end allowance reset)
- Classification / presentation: COGS vs Holding Loss on IS; Inventory net of Allowance on BS; LCM vs LCNRV method choice

---

### Q1 — CORE — RidgeLine Outfitters: LCM schedule and initial recognition JEs
**LO:** LO 10-2  
**Concept:** Apply lower of cost or market by individual item; record initial period-end write-down (allowance)  
**Scenario:**  
**RidgeLine Outfitters Co.** values merchandise inventory using the **LIFO** cost method. At **December 31, Year 1**, management applies the **lower of cost or market (LCM)** rule **to each individual inventory item**. Per-unit data:

| Item | Qty | Est. selling price | Est. cost to complete & sell | Est. normal profit margin | Original cost (LIFO) | Replacement cost |
|---|---:|---:|---:|---:|---:|---:|
| RidgePack | 100 | $120 | $20 | $15 | $95 | $85 |
| GlacierParka | 80 | 150 | 25 | 20 | 110 | 140 |
| EmberStove | 50 | 90 | 10 | 12 | 80 | 55 |
| PeakTent | 40 | 200 | 30 | 25 | 140 | 165 |
| TrailMug | 60 | 80 | 8 | 10 | 70 | 50 |

Before any LCM adjustment, Inventory is carried at **LIFO cost**. The unadjusted Allowance to Reduce Inventory to Market balance is **$0**. COGS before LCM adjustment is **$485,000**.

**Required:**  
a. For each item, compute ceiling (NRV), floor (NRV − normal profit), designated **market**, and **lower of cost or market** per unit. Identify which constraint (RC, ceiling, or floor) sets market.  
b. Prepare a **subsequent-measurement schedule** summarizing total cost, total LCM carrying amount, and total write-down by item and in total.  
c. Record the **December 31, Year 1 initial recognition** journal entry using an **allowance** account and charging **Cost of Goods Sold**.  
d. Record the alternative initial recognition entry using a separate **Holding Loss on Inventory** account (same allowance).  
e. Show **balance sheet** presentation of inventory at December 31, Year 1, and the **income statement** effect under each of (c) and (d).

**Answer key:**  

**a. Per-unit market determination**  
Ceiling = selling price − costs to complete/sell; Floor = ceiling − normal profit; Market = mid-value of {RC, ceiling, floor}.

| Item | Ceiling | Floor | RC | **Market** | Constraint | Cost | **LCM / unit** |
|---|---:|---:|---:|---:|---|---:|---:|
| RidgePack | 120−20=**100** | 100−15=**85** | 85 | **85** | RC (between floor & ceiling) | 95 | **85** |
| GlacierParka | 150−25=**125** | 125−20=**105** | 140 | **125** | Ceiling (RC > ceiling) | 110 | **110** |
| EmberStove | 90−10=**80** | 80−12=**68** | 55 | **68** | Floor (RC < floor) | 80 | **68** |
| PeakTent | 200−30=**170** | 170−25=**145** | 165 | **165** | RC (between) | 140 | **140** |
| TrailMug | 80−8=**72** | 72−10=**62** | 50 | **62** | Floor (RC < floor) | 70 | **62** |

Notes: GlacierParka and PeakTent have cost ≤ market → no write-down. RidgePack, EmberStove, and TrailMug write down to market.

**b. LCM measurement schedule (individual-item approach)**

| Item | Qty | Cost total | LCM / unit | LCM total | Write-down |
|---|---:|---:|---:|---:|---:|
| RidgePack | 100 | 100×95=**9,500** | 85 | **8,500** | **1,000** |
| GlacierParka | 80 | 80×110=**8,800** | 110 | **8,800** | **0** |
| EmberStove | 50 | 50×80=**4,000** | 68 | **3,400** | **600** |
| PeakTent | 40 | 40×140=**5,600** | 140 | **5,600** | **0** |
| TrailMug | 60 | 60×70=**4,200** | 62 | **3,720** | **480** |
| **Total** | | **$32,100** | | **$30,020** | **$2,080** |

Check: 32,100 − 30,020 = **2,080**.

**c. Initial recognition JE — COGS method (emphasis angle)**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 2,080 | |
| Allowance to Reduce Inventory to Market | | 2,080 |
| *Dec 31, Year 1 — reduce LIFO inventory to market (item LCM)* | | |

**Check:** Dr = Cr = 2,080.

**d. Alternative — Holding Loss method**

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 2,080 | |
| Allowance to Reduce Inventory to Market | | 2,080 |
| *Dec 31, Year 1 — same asset write-down; separate IS line* | | |

**Check:** Dr = Cr = 2,080.

**e. Financial statement presentation**

**Balance sheet (both methods):**

| | Amount |
|---|---:|
| Inventory (at LIFO cost) | $32,100 |
| Less: Allowance to Reduce Inventory to Market | (2,080) |
| **Inventory, net** | **$30,020** |

**Income statement effects:**

| | COGS method (c) | Holding loss method (d) |
|---|---:|---:|
| Cost of goods sold | 485,000 + 2,080 = **$487,080** | **$485,000** |
| Holding loss on inventory | **$0** | **$2,080** |

**Key insight:** For LIFO/retail, market is not raw replacement cost—it is RC **capped** by NRV and **floored** by NRV − normal profit. Write inventory down only when **market < cost**; never write up above cost.

---

### Q2 — CORE number variant — HarborForge Tools: LCM twin pack
**LO:** LO 10-2  
**Concept:** Number-variant twin of individual-item LCM measurement and initial write-down JE  
**Scenario:**  
**HarborForge Tools Inc.** uses **LIFO** and applies LCM **by individual item** at **June 30, Year 2**. Unadjusted allowance = **$0**.

| Item | Qty | Selling price / unit | Cost to sell / unit | Normal profit / unit | Cost / unit | Replacement cost / unit |
|---|---:|---:|---:|---:|---:|---:|
| #A-110 Bit set | 200 | $48 | $6 | $8 | $40 | $35 |
| #B-220 Clamp | 150 | 72 | 10 | 12 | 55 | 62 |
| #C-330 Mallet | 100 | 90 | 15 | 10 | 70 | 50 |

**Required:**  
a. Compute ceiling, floor, market, and LCM per unit for each item.  
b. Compute total inventory at cost, at LCM, and the required write-down.  
c. Prepare the June 30 journal entry (allowance + COGS).  
d. State inventory net amount for the balance sheet.

**Answer key:**  

**a. Per-unit computations**

| Item | Ceiling | Floor | RC | Market | Why | Cost | LCM |
|---|---:|---:|---:|---:|---|---:|---:|
| #A-110 | 48−6=**42** | 42−8=**34** | 35 | **35** | RC between | 40 | **35** |
| #B-220 | 72−10=**62** | 62−12=**50** | 62 | **62** | RC = ceiling | 55 | **55** |
| #C-330 | 90−15=**75** | 75−10=**65** | 50 | **65** | Floor (RC < floor) | 70 | **65** |

**b. Totals**

| Item | Cost total | LCM total | Write-down |
|---|---:|---:|---:|
| #A-110 | 200×40=**8,000** | 200×35=**7,000** | **1,000** |
| #B-220 | 150×55=**8,250** | 150×55=**8,250** | **0** |
| #C-330 | 100×70=**7,000** | 100×65=**6,500** | **500** |
| **Total** | **$23,250** | **$21,750** | **$1,500** |

Check: 23,250 − 21,750 = **1,500**.

**c. Journal entry**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 1,500 | |
| Allowance to Reduce Inventory to Market | | 1,500 |
| *June 30, Year 2 — LCM write-down (item approach)* | | |

**Check:** Dr = Cr = 1,500.

**d. Balance sheet**  
Inventory, net = 23,250 − 1,500 = **$21,750**.

**Key insight:** Same mechanics as Q1 with all numbers changed: identify market with the ceiling/floor corridor, then take lower of cost or market.

---

### Q3 — CORE — NorthShore Sporting Goods: multi-year allowance, period-end adj, sale of written-down goods
**LO:** LO 10-2  
**Concept:** Subsequent LCM allowance schedule; period-end adjusting JEs; disposal of write-down when inventory sold; presentation  
**Scenario:**  
**NorthShore Sporting Goods LLC** uses **LIFO** and applies LCM with an **allowance** account. Assume **all beginning inventory is sold** by each year-end. Aggregate data (company applies LCM to inventory **in total** for this problem):

| Date | LIFO cost | Market (designated) |
|---|---:|---:|
| January 1, Year 1 | $42,000 | $42,000 |
| December 31, Year 1 | 56,000 | 51,200 |
| December 31, Year 2 | 63,500 | 57,000 |

Income statement data (before LCM adjustments):

| | Year 1 | Year 2 |
|---|---:|---:|
| Sales | $310,000 | $365,000 |
| COGS (at cost, before LCM adj.) | 168,000 | 205,000 |
| Selling & admin expenses | 72,000 | 84,000 |

**Required:**  
a. Prepare the **December 31, Year 1** period-end adjusting entry using the **allowance** and a **Holding Loss on Inventory** account.  
b. Prepare a **Year 2 subsequent-measurement / allowance rollforward schedule** and the **December 31, Year 2** adjusting entry (Holding Loss method). Show required ending allowance, unadjusted balance, and adjustment.  
c. **Disposal / settlement alternative:** Assume that when Year 1 inventory is sold during Year 2, NorthShore **closes** the Year 1 allowance balance into COGS on the date the related inventory is sold (treat as mid-Year 2 for simplicity). Record that settlement entry. Then record the Year 2 **new** LCM allowance entry at December 31 for Year 2 ending inventory only (COGS method).  
d. Under requirement (a)/(b) (allowance left until year-end), prepare **comparative income statements** for Year 1 and Year 2 (Holding Loss method) and report **inventory, net** at each year-end.  
e. **Classification / presentation:** (1) When must a company use LCM rather than lower of cost or NRV? (2) How may the equity-side charge be classified? (3) May the company reverse a prior write-down if market recovers while the same units remain on hand?

**Answer key:**  

**a. December 31, Year 1 — initial LCM recognition**  
Required allowance = cost − market = 56,000 − 51,200 = **$4,800**.

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 4,800 | |
| Allowance to Reduce Inventory to Market | | 4,800 |
| *Year 1 — reduce inventory to market* | | |

**Check:** Dr = Cr = 4,800. Inventory net = 56,000 − 4,800 = **$51,200**.

**b. Year 2 subsequent measurement schedule & adjusting JE**

| Allowance rollforward | Amount |
|---|---:|
| Required allowance at Dec 31, Year 2 (63,500 − 57,000) | **$6,500** credit |
| Unadjusted balance (from Year 1; BI sold but allowance not yet closed) | 4,800 credit |
| **Additional credit needed** | **$1,700** |

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 1,700 | |
| Allowance to Reduce Inventory to Market | | 1,700 |
| *Year 2 — increase allowance to $6,500 required balance* | | |

**Check:** Dr = Cr = 1,700. Ending allowance **$6,500**; inventory net = 63,500 − 6,500 = **$57,000**.

**c. Disposal/settlement of write-down when inventory sold + new YE allowance**

When Year 1 inventory is sold (settles the related contra):

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 4,800 | |
| Cost of Goods Sold | | 4,800 |
| *Close allowance related to inventory sold (reduces COGS; inventory was carried effectively at market)* | | |

**Check:** Dr = Cr = 4,800. Allowance now **$0**.

December 31, Year 2 — establish allowance for **new** ending inventory (COGS method):

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 6,500 | |
| Allowance to Reduce Inventory to Market | | 6,500 |
| *Year 2 EI: cost $63,500 vs market $57,000* | | |

**Check:** Dr = Cr = 6,500.

**d. Comparative income statements (Holding Loss method, parts a–b)**

| | Year 1 | Year 2 |
|---|---:|---:|
| Sales | $310,000 | $365,000 |
| Cost of goods sold (at cost) | 168,000 | 205,000 |
| **Gross profit (before holding loss)** | **142,000** | **160,000** |
| Holding loss on inventory | 4,800 | 1,700 |
| Selling & admin expenses | 72,000 | 84,000 |
| **Net income** | **$65,200** | **$74,300** |

| Balance sheet inventory | Dec 31, Y1 | Dec 31, Y2 |
|---|---:|---:|
| Inventory at LIFO cost | 56,000 | 63,500 |
| Allowance to reduce inventory to market | (4,800) | (6,500) |
| **Inventory, net** | **$51,200** | **$57,000** |

**e. Classification / presentation answers**  
1. **LCM** applies when inventory cost is measured using **LIFO** or the **retail inventory method**. All other cost methods (e.g., FIFO, average cost) use **lower of cost or net realizable value (LCNRV)** under ASC 330.  
2. The charge may be included in **Cost of Goods Sold** or, if unusual/infrequent, reported as a separate **Holding Loss on Inventory** in earnings.  
3. **No.** A write-down establishes a new cost basis; the company does **not** reverse the loss in later periods if market recovers while the units remain on hand. Recovery is recognized only when inventory is sold (through lower COGS / higher margin).

**Key insight:** The allowance is a **valuation account** remeasured each period-end. Whether you “true up” a leftover credit balance or explicitly close the allowance when inventory is sold, ending inventory must still report at LCM, and write-downs are not reversed for recoveries.

---

### Q4 — MC (classification / method)
**LO:** LO 10-2  
**Concept:** Method applicability and designation of “market” under LCM  

**Question 1:**  
Which of the following correctly states when the **lower of cost or market** rule (with ceiling and floor constraints on replacement cost) applies under U.S. GAAP (ASC 330)?

- A) Always, for all inventory cost methods  
- B) Only for FIFO and weighted-average cost methods  
- C) Only when inventory cost is measured using **LIFO** or the **retail inventory method**  
- D) Only for agricultural products stated at NRV above cost  

**Answer:** **C.** LCM with market = RC (subject to NRV ceiling and NRV − normal profit floor) applies to **LIFO** and **retail** methods. Other methods use **lower of cost or NRV** (LO 10-1).

---

**Question 2:**  
An inventory item measured under LIFO has: replacement cost **$48**, net realizable value (ceiling) **$55**, and NRV less normal profit (floor) **$50**. Original cost is **$60**. Designated **market** and **LCM carrying amount** are:

- A) Market $48; LCM $48  
- B) Market $50; LCM $50  
- C) Market $55; LCM $55  
- D) Market $48; LCM $60  

**Answer:** **B.** RC $48 is **below the floor** $50, so market is limited to the **floor of $50**. LCM = lower of cost $60 and market $50 = **$50**. (Mid-value of {48, 55, 50} = 50.)

---

### Self-check
- [x] Every JE balances (Dr = Cr verified)
- [x] Math recomputed (item schedules, totals, allowance rollforwards)
- [x] Core demo not sidebar-only (Demo 10-2 / Review 10-2 path: LCM, ceiling/floor, write-down JE)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook Demo 10-2 figures)
