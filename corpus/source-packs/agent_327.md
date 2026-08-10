# Agent 327 — CORE DEMO — LO 10-9

**Chapter:** 10  
**LO title:** Retail inventory methods have two other options: the LIFO retail method (Appendix 10A — LIFO retail and dollar-value LIFO retail)  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **LIFO retail** uses the **average cost retail** approach for ending inventory at retail: net markups **and** net markdowns relate to purchases and enter the **current-year** cost ratio (not conventional retail / LCM approximation)
- Current-year cost ratio **excludes beginning inventory**; base layer uses BI cost ÷ BI retail
- **Subsequent measurement schedule:** allocate ending inventory at retail into **LIFO layers**; multiply each layer by its own cost ratio; multi-period rollforward preserves earlier layers and liquidates newest layers first when retail declines
- **Period-end adjusting JE (emphasis):** under a periodic system, establish ending inventory at LIFO (or DV LIFO) retail cost and record **COGS** by closing beginning inventory and net purchases (Dr EI + COGS; Cr BI + Purchases)
- **Initial recognition JE:** record purchases at cost (retail tracked for the schedule)
- **Disposal / settlement:** record **sales** that remove retail from the pool; layer **liquidation** when ending retail falls below prior-layer retail (raises COGS relative to keeping layers)
- **Dollar-value LIFO retail:** deflate ending retail to **base-year retail** (÷ price index); value each layer as base-year retail × **layer price index** × **layer cost ratio**
- **Adoption / restatement JE** when switching from conventional retail to LIFO (or DV LIFO) retail at the change date

---

### Q1 — CORE — Multi-year LIFO retail layers, sales, and period-end adjusting JEs (emphasis)

**LO:** LO 10-9  
**Concept:** LIFO retail multi-year layer schedule; initial purchase recognition; sales disposal of retail pool; **period-end adjusting JEs** each year (including layer liquidation year)  
**Scenario:**  
**Lakeshore Goods LLC** adopts the **LIFO retail** method on **January 1, Year 1**. Within each year, prices are assumed **stable** (quantity changes only; no external price index). Net markups and net markdowns relate entirely to purchases. The company uses a **periodic** inventory system and a December 31 year-end. Ignore income taxes.

**Beginning inventory, January 1, Year 1 (base layer):** $58,000 at cost / $100,000 at retail (base cost ratio **0.580**).

| Year 1 | At cost | At retail |
|---|---:|---:|
| Beginning inventory | $58,000 | $100,000 |
| Net purchases (on account) | 372,000 | 600,000 |
| Net markups | — | 40,000 |
| Net markdowns | — | 20,000 |
| Net sales (cash and on account) | — | 560,000 |

| Year 2 | At cost | At retail |
|---|---:|---:|
| Beginning inventory (carryforward from Y1 LIFO schedule) | (from Y1) | (from Y1) |
| Net purchases | 420,000 | 700,000 |
| Net markups | — | 35,000 |
| Net markdowns | — | 35,000 |
| Net sales | — | 640,000 |

| Year 3 | At cost | At retail |
|---|---:|---:|
| Beginning inventory (carryforward from Y2) | (from Y2) | (from Y2) |
| Net purchases | 300,000 | 500,000 |
| Net markups | — | 20,000 |
| Net markdowns | — | 20,000 |
| Net sales | — | 620,000 |

**Required:**  
(a) For **Year 1**: compute ending inventory at retail (average cost retail approach), base and current-year cost ratios, LIFO retail **layer schedule**, and COGS.  
(b) Record Year 1 **initial recognition** of net purchases on account and the **sales** entry (disposal of goods from the retail pool).  
(c) Record the **December 31, Year 1 period-end adjusting JE** (periodic close: establish EI at LIFO retail cost; record COGS).  
(d) For **Year 2**: compute EI at retail, Year 2 cost ratio, updated layer schedule, COGS, and the **December 31, Year 2 period-end adjusting JE**.  
(e) For **Year 3**: compute EI at retail, identify **layer liquidations**, compute ending LIFO retail cost and COGS, and record the **December 31, Year 3 period-end adjusting JE** (emphasis — liquidation year).  
(f) In one sentence, state why LIFO retail uses the **average cost retail** cost-ratio approach rather than the **conventional retail** approach.

**Answer key:**

**(a) Year 1 — retail schedule, ratios, layers, COGS**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $58,000 | $100,000 |
| Net purchases | 372,000 | 600,000 |
| Net markups | — | 40,000 |
| Net markdowns | — | (20,000) |
| **Subtotal excluding beginning inventory** | **372,000** | **620,000** |
| Goods available for sale | $430,000 | $720,000 |
| Net sales | | (560,000) |
| **Estimated ending inventory at retail** | | **$160,000** |

Base (beginning) cost ratio:  
\[
\frac{\$58{,}000}{\$100{,}000} = \mathbf{0.580}
\]

Current-year cost ratio (excludes BI; markups and markdowns in denominator):  
\[
\frac{\$372{,}000}{\$600{,}000 + \$40{,}000 - \$20{,}000} = \frac{\$372{,}000}{\$620{,}000} = \mathbf{0.600}
\]

Ending retail $160,000 exceeds beginning retail $100,000 → new Year 1 layer of **$60,000** at retail.

| Layer | Inventory at retail | Cost ratio | Inventory at LIFO cost |
|---|---:|---:|---:|
| Base (beginning inventory) | $100,000 | 0.580 | $58,000 |
| Year 1 increment | 60,000 | 0.600 | 36,000 |
| **Total** | **$160,000** | | **$94,000** |

GAFS at cost = $58,000 + $372,000 = **$430,000**  
COGS Year 1 = $430,000 − $94,000 = **$336,000**

**(b) Year 1 — initial recognition and sales (disposal)**

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 372,000 | |
| Accounts Payable | | 372,000 |
| *Record Year 1 net purchases at cost (retail $600,000 tracked for LIFO retail schedule)* | | |

**Check:** Dr 372,000 = Cr 372,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cash (and/or Accounts Receivable) | 560,000 | |
| Sales Revenue | | 560,000 |
| *Record net sales; removes $560,000 retail from goods available* | | |

**Check:** Dr 560,000 = Cr 560,000. **Balanced.**

**(c) December 31, Year 1 — period-end adjusting JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 94,000 | |
| Cost of Goods Sold | 336,000 | |
| Merchandise Inventory (beginning) | | 58,000 |
| Purchases (net) | | 372,000 |
| *Period-end only: close BI and purchases; establish EI at LIFO retail cost and COGS* | | |

**Check:** Dr $94,000 + $336,000 = $430,000; Cr $58,000 + $372,000 = $430,000. **Balanced.**

*(If inventory still sits at GAFS cost $430,000 before close, equivalent net effect: Dr COGS $336,000 / Cr Merchandise Inventory $336,000 to bring inventory to $94,000.)*

**(d) Year 2 — subsequent measurement and period-end JE**

Beginning inventory at retail (from Y1) = **$160,000**; beginning inventory at LIFO cost = **$94,000**.

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $94,000 | $160,000 |
| Net purchases | 420,000 | 700,000 |
| Net markups | — | 35,000 |
| Net markdowns | — | (35,000) |
| Goods available (retail basis for EI) | | $860,000 |
| Net sales | | (640,000) |
| **Estimated ending inventory at retail** | | **$220,000** |

Year 2 cost ratio:  
\[
\frac{\$420{,}000}{\$700{,}000 + \$35{,}000 - \$35{,}000} = \frac{\$420{,}000}{\$700{,}000} = \mathbf{0.600}
\]

Retail increase = $220,000 − $160,000 = **$60,000** (new Year 2 layer).

| Layer | Inventory at retail | Cost ratio | Inventory at LIFO cost |
|---|---:|---:|---:|
| Base | $100,000 | 0.580 | $58,000 |
| Year 1 | 60,000 | 0.600 | 36,000 |
| Year 2 | 60,000 | 0.600 | 36,000 |
| **Total** | **$220,000** | | **$130,000** |

GAFS at cost = $94,000 + $420,000 = **$514,000**  
COGS Year 2 = $514,000 − $130,000 = **$384,000**

**December 31, Year 2 — period-end adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 130,000 | |
| Cost of Goods Sold | 384,000 | |
| Merchandise Inventory (beginning) | | 94,000 |
| Purchases (net) | | 420,000 |
| *Period-end only: roll inventory to LIFO retail EI; record COGS* | | |

**Check:** Dr $130,000 + $384,000 = $514,000; Cr $94,000 + $420,000 = $514,000. **Balanced.**

**(e) Year 3 — layer liquidation and period-end adjusting JE (emphasis)**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $130,000 | $220,000 |
| Net purchases | 300,000 | 500,000 |
| Net markups | — | 20,000 |
| Net markdowns | — | (20,000) |
| Goods available (retail) | | $720,000 |
| Net sales | | (620,000) |
| **Estimated ending inventory at retail** | | **$100,000** |

Year 3 cost ratio = $300,000 / ($500,000 + $20,000 − $20,000) = **0.600** (no new layer is created because retail **declined**).

Ending retail $100,000 equals the base layer only → **full liquidation** of:  
- Entire **Year 2** layer ($60,000 retail / $36,000 cost)  
- Entire **Year 1** layer ($60,000 retail / $36,000 cost)  

| Layer | Inventory at retail | Cost ratio | Inventory at LIFO cost |
|---|---:|---:|---:|
| Base (remaining) | $100,000 | 0.580 | $58,000 |
| Year 1 | 0 | 0.600 | 0 |
| Year 2 | 0 | 0.600 | 0 |
| **Total** | **$100,000** | | **$58,000** |

GAFS at cost = $130,000 + $300,000 = **$430,000**  
COGS Year 3 = $430,000 − $58,000 = **$372,000**

**December 31, Year 3 — period-end adjusting JE (liquidation year)**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 58,000 | |
| Cost of Goods Sold | 372,000 | |
| Merchandise Inventory (beginning) | | 130,000 |
| Purchases (net) | | 300,000 |
| *Period-end only: liquidate Y1–Y2 layers into COGS; EI = base layer only* | | |

**Check:** Dr $58,000 + $372,000 = $430,000; Cr $130,000 + $300,000 = $430,000. **Balanced.**

**Multi-year subsequent measurement rollforward (layers at LIFO cost)**

| Year-end | Ending retail | Layers (retail) | EI at LIFO cost | Period-end COGS |
|---|---:|---|---:|---:|
| 12/31/Y1 | $160,000 | Base 100k + Y1 60k | $94,000 | $336,000 |
| 12/31/Y2 | 220,000 | Base 100k + Y1 60k + Y2 60k | 130,000 | 384,000 |
| 12/31/Y3 | 100,000 | Base 100k only (Y1 & Y2 liquidated) | 58,000 | 372,000 |

**(f) Why average cost retail, not conventional**  
Conventional retail **excludes net markdowns from the cost-ratio denominator** to approximate **LCM**; LIFO retail is a **cost-layer** method and therefore uses the **average cost retail** approach (markdowns **included** in the current-year ratio) so each layer is measured at historical cost.

**Key insight:** Under LIFO retail, the **period-end adjusting JE** does the heavy lifting: it converts goods available for sale into (1) ending inventory valued by **layers** at their own cost ratios and (2) COGS. When ending retail falls, newest layers are liquidated first—raising COGS relative to maintaining those layers.

---

### Q2 — CORE number variant — LIFO retail schedule and period-end JE

**LO:** LO 10-9  
**Concept:** Number-variant twin — LIFO retail EI at retail, dual cost ratios, layer valuation, and **period-end** inventory/COGS adjusting JE  
**Scenario:**  
**Prairie & Pine Outfitters** adopts the LIFO retail method on January 1 of the current year. Prices are stable within the year. Net markups and net markdowns relate to purchases. Periodic inventory; December 31 year-end.

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory | $81,000 | $135,000 |
| Net purchases (on account) | 455,000 | 700,000 |
| Net markups | — | 50,000 |
| Net markdowns | — | 50,000 |
| Net sales | — | 650,000 |

**Required:**  
(a) Compute ending inventory at retail and both cost ratios (base and current year).  
(b) Prepare the LIFO retail layer schedule and ending inventory at LIFO cost.  
(c) Compute COGS.  
(d) Record the purchase JE and the **period-end adjusting JE** that establishes ending inventory and COGS.  
(e) Record the sales JE for the period.

**Answer key:**

**(a) Ending inventory at retail and cost ratios**

Goods available at retail = $135,000 + $700,000 + $50,000 − $50,000 = **$835,000**  
Ending inventory at retail = $835,000 − $650,000 = **$185,000**

Base cost ratio = $81,000 / $135,000 = **0.600**  
Current-year cost ratio = $455,000 / ($700,000 + $50,000 − $50,000) = $455,000 / $700,000 = **0.650**

**(b) Layer schedule**

Retail increase = $185,000 − $135,000 = **$50,000**

| Layer | At retail | Cost ratio | At LIFO cost |
|---|---:|---:|---:|
| Base | $135,000 | 0.600 | $81,000 |
| Current year | 50,000 | 0.650 | 32,500 |
| **Total** | **$185,000** | | **$113,500** |

**(c) COGS**  
GAFS cost = $81,000 + $455,000 = **$536,000**  
COGS = $536,000 − $113,500 = **$422,500**

**(d) Purchase JE and period-end adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 455,000 | |
| Accounts Payable | | 455,000 |
| *Record net purchases at cost* | | |

**Check:** Dr 455,000 = Cr 455,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 113,500 | |
| Cost of Goods Sold | 422,500 | |
| Merchandise Inventory (beginning) | | 81,000 |
| Purchases (net) | | 455,000 |
| *Period-end only: EI at LIFO retail cost; close BI and purchases into COGS* | | |

**Check:** Dr $113,500 + $422,500 = $536,000; Cr $81,000 + $455,000 = $536,000. **Balanced.**

**(e) Sales JE (disposal of retail pool)**

| Account | Debit | Credit |
|---|---:|---:|
| Cash (and/or Accounts Receivable) | 650,000 | |
| Sales Revenue | | 650,000 |
| *Record net sales for the period* | | |

**Check:** Dr 650,000 = Cr 650,000. **Balanced.**

**Key insight:** Same three-step LIFO retail path with all numbers changed: EI at retail → separate base vs current cost ratios → layer conversion; the **period-end JE** is what puts LIFO retail EI and COGS on the books.

---

### Q3 — CORE alternate angle — Dollar-value LIFO retail multi-year, liquidation, adoption JE, period-end JEs

**LO:** LO 10-9  
**Concept:** Dollar-value LIFO retail layer schedule (price index × cost ratio); multi-year subsequent measurement with layer build and liquidation; adoption restatement JE; **period-end adjusting JEs**  
**Scenario:**  
**Summit Trail Retailers Inc.** adopts the **dollar-value LIFO retail** method on **January 1, Year 1**. The price index at adoption (base) is **1.00**. Beginning inventory on that date: **$87,000 cost / $150,000 retail** (base cost ratio **0.580**). Ignore income taxes.

**Additional adoption fact:** Immediately **before** January 1, Year 1, books showed ending inventory under the **conventional retail** method of **$84,000**. Management restates inventory to the DV LIFO retail base cost of **$87,000** on adoption (difference treated as an adoption adjustment to beginning retained earnings for this problem).

**Year 1**

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory | $87,000 | $150,000 |
| Net purchases | 624,000 | 1,000,000 |
| Net markups | — | 80,000 |
| Net markdowns | — | 40,000 |
| Net sales | — | 930,000 |
| Year-end price index | | **1.04** |

**Year 2**

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory at retail (Y1 EI at retail) | | $260,000 |
| Net purchases | 663,400 | 1,050,000 |
| Net markups | — | 50,000 |
| Net markdowns | — | 30,000 |
| Net sales | — | 1,000,000 |
| Year-end price index | | **1.10** |

**Year 3**

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory at retail (Y2 EI at retail) | | $330,000 |
| Net purchases | 561,200 | 900,000 |
| Net markups | — | 40,000 |
| Net markdowns | — | 20,000 |
| Net sales | — | 997,000 |
| Year-end price index | | **1.15** |

Beginning inventory at **DV LIFO cost** for Year 2 = Year 1 ending DV LIFO cost; for Year 3 = Year 2 ending DV LIFO cost (computed below).

**Required:**  
(a) **January 1, Year 1:** prepare the adoption / restatement JE from conventional retail to the DV LIFO retail base.  
(b) **Year 1:** compute EI at retail, current-year cost ratio, EI at base-year retail, DV LIFO layer schedule, EI at cost, COGS, and the **December 31, Year 1 period-end adjusting JE**.  
(c) **Year 2:** same steps (three layers) and the **December 31, Year 2 period-end adjusting JE**.  
(d) **Year 3:** same steps; identify which layers are **liquidated**; record the **December 31, Year 3 period-end adjusting JE**.  
(e) State balance-sheet **classification** and one appropriate **disclosure** for dollar-value LIFO retail.

**Answer key:**

**(a) January 1, Year 1 — adoption / restatement (initial measurement at LIFO base)**  
Increase needed = $87,000 − $84,000 = **$3,000**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory | 3,000 | |
| Retained Earnings | | 3,000 |
| *Restate inventory from conventional retail carrying amount to DV LIFO retail base layer cost* | | |

**Check:** Dr 3,000 = Cr 3,000. **Balanced.**

**(b) Year 1 — dollar-value LIFO retail and period-end JE**

EI at retail = $150,000 + $1,000,000 + $80,000 − $40,000 − $930,000 = **$260,000**  
Current-year cost ratio = $624,000 / ($1,000,000 + $80,000 − $40,000) = $624,000 / $1,040,000 = **0.600**  
EI at base-year retail = $260,000 / 1.04 = **$250,000**

| Layer (base-year retail) | Price index | Cost ratio | DV LIFO cost |
|---|---:|---:|---:|
| Base $150,000 | 1.00 | 0.580 | $87,000 |
| Year 1 $100,000 | 1.04 | 0.600 | 62,400 |
| **Total base-year $250,000** | | | **$149,400** |

GAFS at cost = $87,000 + $624,000 = **$711,000**  
COGS Year 1 = $711,000 − $149,400 = **$561,600**

**December 31, Year 1 — period-end adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, DV LIFO retail) | 149,400 | |
| Cost of Goods Sold | 561,600 | |
| Merchandise Inventory (beginning) | | 87,000 |
| Purchases (net) | | 624,000 |
| *Period-end only: establish DV LIFO retail EI and COGS* | | |

**Check:** Dr $149,400 + $561,600 = $711,000; Cr $87,000 + $624,000 = $711,000. **Balanced.**

**(c) Year 2 — three layers and period-end JE**

EI at retail = $260,000 + $1,050,000 + $50,000 − $30,000 − $1,000,000 = **$330,000**  
Year 2 cost ratio = $663,400 / ($1,050,000 + $50,000 − $30,000) = $663,400 / $1,070,000 = **0.620**  
EI at base-year retail = $330,000 / 1.10 = **$300,000**

Increase in base-year retail = $300,000 − $250,000 = **$50,000** (new Year 2 layer).

| Layer (base-year retail) | Price index | Cost ratio | DV LIFO cost |
|---|---:|---:|---:|
| Base $150,000 | 1.00 | 0.580 | $87,000 |
| Year 1 $100,000 | 1.04 | 0.600 | 62,400 |
| Year 2 $50,000 | 1.10 | 0.620 | 34,100 |
| **Total base-year $300,000** | | | **$183,500** |

GAFS at cost = $149,400 + $663,400 = **$812,800**  
COGS Year 2 = $812,800 − $183,500 = **$629,300**

**December 31, Year 2 — period-end adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, DV LIFO retail) | 183,500 | |
| Cost of Goods Sold | 629,300 | |
| Merchandise Inventory (beginning) | | 149,400 |
| Purchases (net) | | 663,400 |
| *Period-end only: add Year 2 DV LIFO layer; record COGS* | | |

**Check:** Dr $183,500 + $629,300 = $812,800; Cr $149,400 + $663,400 = $812,800. **Balanced.**

**(d) Year 3 — layer liquidation and period-end JE (emphasis)**

EI at retail = $330,000 + $900,000 + $40,000 − $20,000 − $997,000 = **$253,000**  
Year 3 cost ratio = $561,200 / ($900,000 + $40,000 − $20,000) = $561,200 / $920,000 = **0.610**  
EI at base-year retail = $253,000 / 1.15 = **$220,000**

Base-year retail declined from $300,000 to $220,000 → **no Year 3 layer**. Liquidations (LIFO order):  
- Entire **Year 2** layer of $50,000 base-year retail is liquidated.  
- **Year 1** layer reduced from $100,000 to $70,000 base-year retail (partial liquidation of $30,000).  
- Base layer of $150,000 remains intact.

| Layer (base-year retail) | Price index | Cost ratio | DV LIFO cost |
|---|---:|---:|---:|
| Base $150,000 | 1.00 | 0.580 | $87,000 |
| Year 1 (remaining) $70,000 | 1.04 | 0.600 | 43,680 |
| **Total base-year $220,000** | | | **$130,680** |

GAFS at cost = $183,500 + $561,200 = **$744,700**  
COGS Year 3 = $744,700 − $130,680 = **$614,020**

**December 31, Year 3 — period-end adjusting JE after liquidation**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, DV LIFO retail) | 130,680 | |
| Cost of Goods Sold | 614,020 | |
| Merchandise Inventory (beginning) | | 183,500 |
| Purchases (net) | | 561,200 |
| *Period-end only: liquidate Y2 fully and part of Y1 into COGS; EI = remaining layers* | | |

**Check:** Dr $130,680 + $614,020 = $744,700; Cr $183,500 + $561,200 = $744,700. **Balanced.**

**Subsequent measurement schedule — DV LIFO retail (summary)**

| Year-end | EI at current retail | ÷ Index | Base-year EI | Layers (base-year retail) | EI at DV LIFO cost | Period-end COGS |
|---|---:|---:|---:|---|---:|---:|
| 12/31/Y1 | $260,000 | 1.04 | $250,000 | Base 150k + Y1 100k | $149,400 | $561,600 |
| 12/31/Y2 | 330,000 | 1.10 | 300,000 | + Y2 50k | 183,500 | 629,300 |
| 12/31/Y3 | 253,000 | 1.15 | 220,000 | Base 150k + Y1 70k (Y2 gone) | 130,680 | 614,020 |

**(e) Classification / presentation / disclosure**  
- **Classification:** Merchandise inventory under dollar-value LIFO retail is a **current asset** at **LIFO cost** (not at current retail selling price).  
- **Disclosure:** Accounting policy note that inventory is valued using the **dollar-value LIFO retail** method (layer cost-to-retail ratios and external price indices), often with a **LIFO reserve** (or FIFO-equivalent inventory) for comparability.

**Key insight:** Dollar-value LIFO retail first converts ending retail to **base-year dollars**, then multiplies each layer by **both** its price index and its cost ratio. The **period-end adjusting JE** is where that layered cost hits the books as ending inventory and COGS; a decline in base-year retail **liquidates** newest layers first.

---

### Q4 — MC (method / classification) — 2 items

**LO:** LO 10-9  
**Concept:** Distinguishing LIFO retail vs conventional retail; measurement elements under dollar-value LIFO retail  

**Question 1:**  
Which statement best describes the **LIFO retail** method when prices are assumed stable within the period?  
- A) Ending inventory is valued with a single cost ratio that excludes markdowns from the denominator to approximate LCM.  
- B) Beginning inventory and current purchases share one blended cost ratio that includes markdowns; layers are not used.  
- C) Ending inventory at retail is layered; the base layer uses the beginning cost ratio and any retail increase uses a current-year cost ratio that includes markups and markdowns (average cost approach).  
- D) Ending inventory at retail is always multiplied only by the current-year price index, with no separate cost ratio by layer.

**Answer:** **C.** LIFO retail layers inventory: base at BI cost ratio; increments at the current-year **average cost retail** ratio (markups and markdowns in the ratio). Conventional retail (A) is the LCM approximation, not LIFO retail.

**Question 2:**  
Under the **dollar-value LIFO retail** method, a new inventory layer is measured by multiplying the layer’s base-year retail amount by:  
- A) The current-year cost ratio only.  
- B) The current-year price index only.  
- C) The base-year cost ratio and a price index of 1.00 only.  
- D) **Both** the price index for the year the layer was added **and** that year’s cost ratio.

**Answer:** **D.** Each DV LIFO retail layer = base-year retail layer × layer-year price index × layer-year cost ratio.

---

### Self-check
- [x] Every JE balances (Q1 b–e; Q2 d–e; Q3 a–d)
- [x] Math recomputed (ratios, layers, base-year deflation, COGS, period-end closes)
- [x] Core demo not sidebar-only (Demo 10-9A / 10-9B path: LIFO retail + dollar-value LIFO retail)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Emphasis **period_end_adjusting_JE** featured in Q1–Q3
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (sales + layer liquidation)
