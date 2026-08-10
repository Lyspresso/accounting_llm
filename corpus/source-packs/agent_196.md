# Agent 196 — CORE DEMO — LO 10-9

**Chapter:** 10  
**LO title:** Retail inventory methods have two other options: the LIFO retail method (Appendix 10A — LIFO retail and dollar-value LIFO retail)  
**Critical gap LO:** no

## Concept list for this pack
- **LIFO retail** uses the **average cost retail** approach for ending inventory at retail (net markups **and** net markdowns relate to purchases and enter the **current-year** cost ratio)
- Current-year cost ratio **excludes beginning inventory**; base layer uses beginning inventory cost ÷ beginning inventory retail
- **Subsequent measurement schedule (emphasis):** allocate ending inventory at retail into **LIFO layers**, multiply each layer by its own cost ratio; multi-period rollforward preserves earlier layers and liquidates newest layers first when retail declines
- **Period-end adjusting JE (periodic):** establish ending inventory at LIFO retail cost and record COGS by closing beginning inventory and net purchases
- **Dollar-value LIFO retail:** convert ending inventory at current retail to **base-year retail** (÷ price index); value each layer as base-year retail × **layer price index** × **layer cost ratio**
- Layer **increases** (new layers) vs layer **liquidations** when base-year retail falls
- **Adoption / restatement JE** when switching from conventional retail to LIFO retail (or DV LIFO retail) at the change date
- Method classification: LIFO retail ≈ cost layers; conventional retail ≈ LCM approximation (not used for LIFO retail cost ratios)

---

### Q1 — CORE — Multi-period LIFO retail layer schedule (subsequent measurement emphasis)
**LO:** LO 10-9  
**Concept:** Subsequent measurement schedule for LIFO retail — multi-year layer rollforward (build and liquidation), current-year cost ratios excluding BI, period-end inventory/COGS JEs, and sales settlement of merchandise  
**Scenario:**  
**Cascade Valley Outfitters Inc.** adopts the **LIFO retail** method on **January 1, Year 1**. Within each year, prices are assumed stable (quantity changes only; no external price index). Net markups and net markdowns relate entirely to purchases. The company uses a **periodic** inventory system and a December 31 year-end. Ignore income taxes.

**Beginning inventory, January 1, Year 1 (base layer):** $39,000 at cost / $60,000 at retail.

| Year 1 | At cost | At retail |
|---|---:|---:|
| Beginning inventory | $39,000 | $60,000 |
| Net purchases | 210,000 | 350,000 |
| Net markups | — | 25,000 |
| Net markdowns | — | 25,000 |
| Net sales | — | 280,000 |

| Year 2 | At cost | At retail |
|---|---:|---:|
| Beginning inventory (at retail from Y1 EI; at LIFO cost from Y1 schedule) | (from Y1) | (from Y1) |
| Net purchases | 240,000 | 400,000 |
| Net markups | — | 20,000 |
| Net markdowns | — | 20,000 |
| Net sales | — | 370,000 |

| Year 3 | At cost | At retail |
|---|---:|---:|
| Beginning inventory (carryforward) | (from Y2) | (from Y2) |
| Net purchases | 200,000 | 320,000 |
| Net markups | — | 15,000 |
| Net markdowns | — | 15,000 |
| Net sales | — | 420,000 |

**Required:**  
a. Prepare **initial recognition** journal entries for Year 1 net purchases on account and for Year 1 net sales (cash).  
b. For **Year 1**: compute ending inventory at retail (average cost retail approach), base and current-year cost ratios, the **LIFO retail subsequent measurement (layer) schedule**, ending inventory at LIFO cost, and COGS.  
c. Prepare the **December 31, Year 1 period-end adjusting/closing JE** (periodic) to record ending inventory and COGS.  
d. For **Year 2**: prepare the full **subsequent measurement layer schedule** (preserve Year 1 layers; add Year 2 increment) and compute ending inventory at LIFO cost and COGS.  
e. Prepare the **December 31, Year 2 period-end adjusting/closing JE**.  
f. For **Year 3**: prepare the layer schedule showing **liquidation** of layers (LIFO order), ending inventory at LIFO cost, COGS, and the **December 31, Year 3 period-end JE**.  
g. In one sentence, explain why LIFO retail uses the **average cost retail** cost-ratio approach rather than the **conventional retail** approach.

**Answer key:**  

**a. Year 1 — initial recognition of purchases and sales (settlement of merchandise)**

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 210,000 | |
| Accounts Payable | | 210,000 |
| *Record net purchases on account* | | |

**Check:** Dr 210,000 = Cr 210,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 280,000 | |
| Sales Revenue | | 280,000 |
| *Record net sales (inventory disposed through sale at retail)* | | |

**Check:** Dr 280,000 = Cr 280,000. **Balanced.**

**b. Year 1 — EI at retail, cost ratios, layer schedule, COGS**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $39,000 | $60,000 |
| Net purchases | 210,000 | 350,000 |
| Net markups | — | 25,000 |
| Net markdowns | — | (25,000) |
| **Subtotal excluding beginning inventory** | **210,000** | **350,000** |
| Goods available for sale | $249,000 | $410,000 |
| Net sales | | (280,000) |
| **Estimated ending inventory at retail** | | **$130,000** |

Base (beginning inventory) cost ratio:  
\[
\frac{\$39{,}000}{\$60{,}000} = \mathbf{0.65}
\]

Current-year cost ratio (excludes BI; includes net markups and net markdowns with purchases):  
\[
\frac{\$210{,}000}{\$350{,}000 + \$25{,}000 - \$25{,}000} = \frac{\$210{,}000}{\$350{,}000} = \mathbf{0.60}
\]

Retail increased from $60,000 to $130,000 → new Year 1 layer of **$70,000** at retail.

**Year 1 subsequent measurement — LIFO retail layer schedule**

| Layer | Inventory at retail | Cost ratio | Inventory at LIFO cost |
|---|---:|---:|---:|
| Base (Jan 1, Year 1) | $60,000 | 0.65 | $39,000 |
| Year 1 increment | 70,000 | 0.60 | 42,000 |
| **Total** | **$130,000** | | **$81,000** |

GAFS at cost = $39,000 + $210,000 = **$249,000**  
COGS = $249,000 − $81,000 = **$168,000**

**c. December 31, Year 1 — period-end adjusting/closing JE**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 81,000 | |
| Cost of Goods Sold | 168,000 | |
| Merchandise Inventory (beginning) | | 39,000 |
| Purchases (net) | | 210,000 |
| *Close BI and purchases; record EI at LIFO retail cost and COGS* | | |

**Check:** Dr $81,000 + $168,000 = $249,000; Cr $39,000 + $210,000 = $249,000. **Balanced.**

**d. Year 2 — subsequent measurement schedule (layer rollforward)**

EI at retail:  
\[
\$130{,}000 + \$400{,}000 + \$20{,}000 - \$20{,}000 - \$370{,}000 = \mathbf{\$160{,}000}
\]

Year 2 cost ratio:  
\[
\frac{\$240{,}000}{\$400{,}000 + \$20{,}000 - \$20{,}000} = \frac{\$240{,}000}{\$400{,}000} = \mathbf{0.60}
\]

Retail increase = $160,000 − $130,000 = **$30,000** (new Year 2 layer).

**Year 2 subsequent measurement — LIFO retail layer schedule**

| Layer | Inventory at retail | Cost ratio | Inventory at LIFO cost |
|---|---:|---:|---:|
| Base | $60,000 | 0.65 | $39,000 |
| Year 1 | 70,000 | 0.60 | 42,000 |
| Year 2 increment | 30,000 | 0.60 | 18,000 |
| **Total** | **$160,000** | | **$99,000** |

Beginning inventory at LIFO cost (from Year 1) = **$81,000**  
GAFS cost = $81,000 + $240,000 = **$321,000**  
COGS = $321,000 − $99,000 = **$222,000**

**e. December 31, Year 2 — period-end JE**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 99,000 | |
| Cost of Goods Sold | 222,000 | |
| Merchandise Inventory (beginning) | | 81,000 |
| Purchases (net) | | 240,000 |

**Check:** Dr $99,000 + $222,000 = $321,000; Cr $81,000 + $240,000 = $321,000. **Balanced.**

**f. Year 3 — layer liquidation schedule and period-end JE**

EI at retail:  
\[
\$160{,}000 + \$320{,}000 + \$15{,}000 - \$15{,}000 - \$420{,}000 = \mathbf{\$60{,}000}
\]

Year 3 cost ratio (for information; no new layer when retail falls):  
\[
\frac{\$200{,}000}{\$320{,}000} = \mathbf{0.625}
\]

Base-year (current-dollar) retail declined from $160,000 to $60,000 → liquidate **$100,000** of retail layers in LIFO order:  
- Entire **Year 2** layer of $30,000 retail liquidated  
- Entire **Year 1** layer of $70,000 retail liquidated  
- **Base** layer of $60,000 retail remains intact  

**Year 3 subsequent measurement — LIFO retail layer schedule (after liquidation)**

| Layer | Inventory at retail | Cost ratio | Inventory at LIFO cost |
|---|---:|---:|---:|
| Base | $60,000 | 0.65 | $39,000 |
| Year 1 | 0 | 0.60 | 0 |
| Year 2 | 0 | 0.60 | 0 |
| **Total** | **$60,000** | | **$39,000** |

Beginning LIFO inventory cost = **$99,000**  
GAFS cost = $99,000 + $200,000 = **$299,000**  
COGS = $299,000 − $39,000 = **$260,000**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 39,000 | |
| Cost of Goods Sold | 260,000 | |
| Merchandise Inventory (beginning) | | 99,000 |
| Purchases (net) | | 200,000 |

**Check:** Dr $39,000 + $260,000 = $299,000; Cr $99,000 + $200,000 = $299,000. **Balanced.**

**g. Average cost vs conventional for LIFO retail**  
LIFO retail is a **cost** method: each layer is measured at historical cost using the **average cost retail** approach (markdowns **included** in the current-year ratio). Conventional retail **excludes** markdowns from the cost-ratio denominator to approximate **lower of cost or market**, which is incompatible with pure LIFO cost layering.

**Key insight:** The LIFO retail **subsequent measurement schedule** is the engine—preserve older layers at their original cost ratios, attach quantity increases to the current-year ratio only, and liquidate newest layers first when ending retail falls. Period-end JEs simply put the schedule’s LIFO cost on the books and charge the residual of goods available to COGS.

---

### Q2 — CORE number variant — LIFO retail single-year schedule and period-end JE
**LO:** LO 10-9  
**Concept:** Number-variant twin of LIFO retail — EI at retail, separate base vs current cost ratios, layer schedule, COGS, and period-end JE (all numbers changed)  
**Scenario:**  
**Redwood Trail Mercantile Co.** adopts the **LIFO retail** method on January 1 of the current year. Prices are stable within the year. Periodic inventory system; December 31 year-end.

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory | $50,000 | $100,000 |
| Net purchases | 240,000 | 400,000 |
| Net markups | — | 20,000 |
| Net markdowns | — | 20,000 |
| Net sales | — | 350,000 |

**Required:**  
a. Compute ending inventory at retail and both cost ratios (base and current year).  
b. Prepare the LIFO retail layer schedule and ending inventory at LIFO cost.  
c. Compute COGS.  
d. Prepare the period-end journal entry to record ending inventory and COGS (periodic close of BI and purchases).  
e. Prepare the journal entry for net purchases on account during the year (initial recognition of purchases).

**Answer key:**  

**a. EI at retail and cost ratios**

Goods available at retail = $100,000 + $400,000 + $20,000 − $20,000 = **$500,000**  
Ending inventory at retail = $500,000 − $350,000 = **$150,000**

Base cost ratio = $50,000 / $100,000 = **0.50**  
Current-year cost ratio = $240,000 / ($400,000 + $20,000 − $20,000) = $240,000 / $400,000 = **0.60**

**b. Layer schedule**

Retail increase = $150,000 − $100,000 = **$50,000**

| Layer | At retail | Cost ratio | At LIFO cost |
|---|---:|---:|---:|
| Base | $100,000 | 0.50 | $50,000 |
| Current year | 50,000 | 0.60 | 30,000 |
| **Total** | **$150,000** | | **$80,000** |

**c. COGS**  
GAFS cost = $50,000 + $240,000 = $290,000  
COGS = $290,000 − $80,000 = **$210,000**

**d. Period-end JE**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, LIFO retail) | 80,000 | |
| Cost of Goods Sold | 210,000 | |
| Merchandise Inventory (beginning) | | 50,000 |
| Purchases (net) | | 240,000 |

**Check:** Dr $80,000 + $210,000 = $290,000; Cr $50,000 + $240,000 = $290,000. **Balanced.**

**e. Initial recognition — purchases**

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 240,000 | |
| Accounts Payable | | 240,000 |

**Check:** Dr 240,000 = Cr 240,000. **Balanced.**

**Key insight:** Same three-step LIFO retail process with fully recomputed amounts: EI at retail (average cost approach) → separate base vs current cost ratios → multiply each retail layer by its own ratio; close BI and purchases into EI and COGS at period-end.

---

### Q3 — CORE — Dollar-value LIFO retail multi-year schedule, liquidation, adoption JE
**LO:** LO 10-9  
**Concept:** Dollar-value LIFO retail subsequent measurement — convert EI to base-year retail, value layers with price index × cost ratio; multi-year layer increase then liquidation; adoption restatement from conventional retail; period-end COGS JE  
**Scenario:**  
**Silverpine Markets Co.** adopts the **dollar-value LIFO retail** method on **January 1, Year 1**. The base price index at adoption is **1.00**. Beginning inventory on that date: **$54,000 cost / $90,000 retail** (base cost ratio **0.60**). Ignore income taxes. Periodic system; December 31 year-end.

Immediately before adoption, Silverpine’s books carried inventory under the **conventional retail** method at **$52,200**. Management restates inventory to the LIFO retail base cost of **$54,000** on January 1, Year 1 (difference adjusts beginning retained earnings for this problem).

**Year 1**

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory | $54,000 | $90,000 |
| Net purchases | 260,400 | 400,000 |
| Net markups | — | 40,000 |
| Net markdowns | — | 20,000 |
| Net sales | — | 356,000 |
| Year-end price index | | **1.10** |

**Year 2**

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory at retail (Y1 EI at retail) | | $154,000 |
| Net purchases | 290,000 | 500,000 |
| Net markups | — | 30,000 |
| Net markdowns | — | 30,000 |
| Net sales | — | 462,000 |
| Year-end price index | | **1.20** |

**Year 3**

| | At cost | At retail |
|---|---:|---:|
| Beginning inventory at retail (Y2 EI at retail) | | $192,000 |
| Net purchases | 256,000 | 400,000 |
| Net markups | — | 20,000 |
| Net markdowns | — | 20,000 |
| Net sales | — | 467,000 |
| Year-end price index | | **1.25** |

**Required:**  
a. For **Year 1**: compute EI at retail, current-year cost ratio, EI at base-year retail, the **dollar-value LIFO retail layer schedule**, and ending inventory at DV LIFO cost.  
b. For **Year 2**: same steps (show three layers).  
c. For **Year 3**: same steps; identify which layers are **liquidated** (full or partial).  
d. Prepare the **January 1, Year 1 adoption / restatement JE** from conventional retail carrying amount to LIFO retail base cost.  
e. Prepare the **December 31, Year 3 period-end JE** given Year 3 beginning inventory at DV LIFO cost equal to the Year 2 ending inventory from part b and Year 3 net purchases of $256,000.  
f. State balance-sheet **classification** of the inventory and one appropriate **disclosure** for dollar-value LIFO retail.

**Answer key:**  

**a. Year 1 — dollar-value LIFO retail**

EI at retail = $90,000 + $400,000 + $40,000 − $20,000 − $356,000 = **$154,000**  
Current-year cost ratio = $260,400 / ($400,000 + $40,000 − $20,000) = $260,400 / $420,000 = **0.62**  
EI at base-year retail = $154,000 / 1.10 = **$140,000**

| Layer (base-year retail) | Price index | Cost ratio | DV LIFO cost |
|---|---:|---:|---:|
| Base $90,000 | 1.00 | 0.60 | $54,000 |
| Year 1 $50,000 | 1.10 | 0.62 | 34,100 |
| **Total base-year $140,000** | | | **$88,100** |

Check: $50,000 × 1.10 × 0.62 = $50,000 × 0.682 = **$34,100**; $54,000 + $34,100 = **$88,100**.

**b. Year 2**

EI at retail = $154,000 + $500,000 + $30,000 − $30,000 − $462,000 = **$192,000**  
Year 2 cost ratio = $290,000 / ($500,000 + $30,000 − $30,000) = $290,000 / $500,000 = **0.58**  
EI at base-year retail = $192,000 / 1.20 = **$160,000**

Base-year retail increased from $140,000 to $160,000 → new Year 2 layer of **$20,000**.

| Layer (base-year retail) | Price index | Cost ratio | DV LIFO cost |
|---|---:|---:|---:|
| Base $90,000 | 1.00 | 0.60 | $54,000 |
| Year 1 $50,000 | 1.10 | 0.62 | 34,100 |
| Year 2 $20,000 | 1.20 | 0.58 | 13,920 |
| **Total base-year $160,000** | | | **$102,020** |

Check: $20,000 × 1.20 × 0.58 = $20,000 × 0.696 = **$13,920**; $54,000 + $34,100 + $13,920 = **$102,020**.

**c. Year 3 — layer liquidation**

EI at retail = $192,000 + $400,000 + $20,000 − $20,000 − $467,000 = **$125,000**  
Year 3 cost ratio = $256,000 / ($400,000 + $20,000 − $20,000) = $256,000 / $400,000 = **0.64**  
EI at base-year retail = $125,000 / 1.25 = **$100,000**

Base-year retail declined from $160,000 to $100,000 → **no Year 3 layer**. Liquidations (LIFO order):  
- Entire **Year 2** layer of $20,000 base-year retail is liquidated.  
- **Year 1** layer reduced from $50,000 to **$10,000** base-year retail (partial liquidation of $40,000).  
- Base layer of $90,000 remains intact.

| Layer (base-year retail) | Price index | Cost ratio | DV LIFO cost |
|---|---:|---:|---:|
| Base $90,000 | 1.00 | 0.60 | $54,000 |
| Year 1 $10,000 | 1.10 | 0.62 | 6,820 |
| **Total base-year $100,000** | | | **$60,820** |

Check: $10,000 × 1.10 × 0.62 = **$6,820**; $54,000 + $6,820 = **$60,820**.

**d. January 1, Year 1 — adoption / restatement JE**

Increase needed = $54,000 − $52,200 = **$1,800**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory | 1,800 | |
| Retained Earnings | | 1,800 |
| *Restate inventory from conventional retail to LIFO retail base at adoption* | | |

**Check:** Dr 1,800 = Cr 1,800. **Balanced.**  
(Inventory now at LIFO base $54,000, which equals $90,000 retail × 0.60.)

**e. December 31, Year 3 — period-end JE**

Beginning inventory at DV LIFO cost (end of Year 2) = **$102,020**  
Net purchases = **$256,000**  
Ending inventory at DV LIFO cost = **$60,820**  
COGS = $102,020 + $256,000 − $60,820 = **$297,200**

| Account | Debit | Credit |
|---|---:|---:|
| Merchandise Inventory (ending, DV LIFO retail) | 60,820 | |
| Cost of Goods Sold | 297,200 | |
| Merchandise Inventory (beginning) | | 102,020 |
| Purchases (net) | | 256,000 |

**Check:** Dr $60,820 + $297,200 = $358,020; Cr $102,020 + $256,000 = $358,020. **Balanced.**

**f. Classification and disclosure**  
- **Classification:** Inventory is a **current asset** on the balance sheet, measured at **dollar-value LIFO retail cost** (layers at historical cost ratios and price indices), not at conventional retail LCM approximation.  
- **Disclosure:** Disclose use of the **dollar-value LIFO retail** method, including that cost is determined by applying cost-to-retail ratios (and price indices) to merchandise categories’ ending retail values; companies often also disclose the **LIFO reserve** (FIFO/current cost excess over LIFO) for comparability.

**Key insight:** Dollar-value LIFO retail first strips price-level effects (÷ current index → base-year retail), then values each base-year layer with **two** factors from the year the layer was added—its **price index** and its **cost ratio**. Liquidations reduce newest layers first in base-year dollars.

---

### Q4 — MC — LIFO retail vs conventional; DV LIFO measurement elements
**LO:** LO 10-9  
**Concept:** Method classification — LIFO retail uses average-cost-style cost ratios (markdowns in ratio); dollar-value LIFO retail applies both price index and cost ratio to each layer  

**Question 1:**  
Which statement best describes how the **current-year cost-to-retail ratio** is computed under the **LIFO retail** method?

- A) Exclude beginning inventory and **exclude** net markdowns from the ratio denominator (conventional retail approach) so the ratio approximates LCM.  
- B) Include beginning inventory, purchases, markups, and markdowns in one overall average cost ratio applied to all ending retail.  
- C) Exclude beginning inventory; include net markups and net markdowns with purchases in the current-year ratio (average cost retail approach), then apply separate ratios to LIFO layers.  
- D) Use only the beginning inventory cost ratio for all layers, including current-year quantity increases.

**Answer:** **C.** LIFO retail applies the **average cost retail** approach to the current-year ratio (markdowns **included**; beginning inventory **excluded** from that ratio) and values ending inventory in **layers** at each layer’s own cost ratio. Conventional retail (A) is not used for LIFO cost layering. A single blended ratio on all GAFS (B) is average cost retail without LIFO layering. Applying only the base ratio to new layers (D) ignores the current-year purchase cost structure.

---

**Question 2:**  
Under the **dollar-value LIFO retail** method, a new inventory layer added this year is valued by multiplying the layer’s base-year retail dollars by:

- A) The current-year cost ratio only.  
- B) The current-year price index only.  
- C) Both the current-year price index and the current-year cost ratio.  
- D) The base-year price index (1.00) and the base-year cost ratio only.

**Answer:** **C.** Each layer is valued as: base-year retail layer × **price index of the year the layer was added** × **cost ratio of the year the layer was added**. Using only one of the two factors (A or B) understates the dual conversion. Base factors only (D) would value a new layer as if prices and cost structure never changed.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all period-end, purchase, sales, and adoption entries)
- [x] Math recomputed (layer schedules, base-year conversions, COGS rollforwards)
- [x] Core demo not sidebar-only (Demo 10-9A LIFO retail; Demo 10-9B dollar-value LIFO retail; adoption restatement)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Emphasis angle covered: multi-period **subsequent measurement schedules** (Q1 layer rollforward; Q3 DV LIFO multi-year schedule)
- [x] Angles: initial recognition JE (purchases/sales/adoption), subsequent measurement schedule, period-end adjusting JE, disposal/settlement (sales; layer liquidation)
