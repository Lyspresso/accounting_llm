# Agent 195 — CORE DEMO — LO 10-8

**Chapter:** 10  
**LO title:** Estimate ending inventory using the average cost and conventional retail methods  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Retail inventory method (core steps):** (1) compute ending inventory at **retail**, (2) compute **cost-to-retail ratio** (cost of goods available ÷ retail of goods available as defined by the method), (3) apply ratio to ending inventory at retail → **estimated inventory at cost**
- **Average cost retail method:** include **both** net markups and **net markdowns** in goods available for sale at retail when computing the cost ratio → estimate approximates **average cost**
- **Conventional retail method:** include net markups in the cost-ratio denominator; **exclude net markdowns** from the ratio (still deduct them when computing EI at retail) → lower cost ratio approximates **lower of cost or market (LCM)**
- **Net markups** = additional markups − markup cancellations; **net markdowns** = markdowns − markdown cancellations
- **Initial recognition JE:** purchases (and freight-in) recorded at cost; retail tagging is memo for the schedule
- **Subsequent measurement schedule (emphasis):** multi-column cost/retail rollforward of goods available, cost ratio, and EI at cost
- **Period-end adjusting JE:** periodic inventory close — set ending inventory, close beginning inventory and purchases into **COGS**
- **Disposal / settlement:** record **sales** that remove goods from the retail pool; optional **physical-count settlement** when count ≠ estimate (shrinkage)
- **Complicating factors (core, not sidebar-only):** freight-in (cost only); purchase returns (cost and retail); abnormal casualty (remove cost and retail **before** cost ratio); sales returns; employee discounts and normal spoilage (deduct at retail **after** cost ratio)

---

### Q1 — CORE — Average cost retail: full schedule, purchases JE, sales, year-end COGS
**LO:** LO 10-8  
**Concept:** Average cost retail subsequent measurement schedule (net markups and net markdowns in cost ratio); initial purchase JE; sales (disposal of retail pool); period-end inventory/COGS adjusting JE  
**Scenario:**  
**Pinehaven Outdoor Co.** (calendar year-end) uses the **average cost retail method** to estimate year-end merchandise inventory for external reporting. It uses a **periodic** inventory system. Beginning inventory (already on the books) is **$72,000** at cost and **$120,000** at retail.

During **Year 1**, Pinehaven records the following (not yet closed):

| Item | Cost | Retail |
|---|---:|---:|
| Purchases (on account) | $288,000 | $480,000 |
| Additional markups | — | 45,000 |
| Additional markup cancellations | — | 5,000 |
| Markdowns | — | 50,000 |
| Markdown cancellations | — | 10,000 |
| Sales (cash and on account) | — | 520,000 |

No freight-in, returns, employee discounts, or spoilage this year. Ignore income taxes.

**Required:**  
a. Compute **net markups** and **net markdowns**.  
b. Prepare the full **average cost retail subsequent measurement schedule**: goods available for sale at cost and retail, cost-to-retail ratio (to three decimals if needed; prefer exact fraction), estimated ending inventory at retail, and estimated ending inventory at **cost**.  
c. Record the **initial recognition JE** summarizing Year 1 purchases on account.  
d. Record the **sales JE** (disposal of goods from the retail pool) for the year’s net sales of $520,000 (assume all cash for simplicity).  
e. Compute **cost of goods sold** and prepare the **December 31, Year 1 period-end adjusting JE** that establishes ending inventory and closes beginning inventory and purchases into COGS.  
f. Briefly explain why **net markdowns** are included in the average cost cost-ratio denominator (contrast with conventional retail in one sentence).

**Answer key:**  

**a. Net markups and net markdowns**

Net markups = $45,000 − $5,000 = **$40,000**  
Net markdowns = $50,000 − $10,000 = **$40,000**

**b. Subsequent measurement schedule — average cost retail (emphasis)**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $72,000 | $120,000 |
| Purchases | 288,000 | 480,000 |
| Net markups | — | 40,000 |
| Net markdowns | — | (40,000) |
| **Goods available for sale** | **$360,000** | **$600,000** |
| Net sales | | (520,000) |
| **Estimated ending inventory at retail** | | **$80,000** |

Cost-to-retail ratio:

\[
\frac{\$360{,}000}{\$600{,}000} = 0.600
\]

Estimated ending inventory at cost:

\[
\$80{,}000 \times 0.600 = \mathbf{\$48{,}000}
\]

**Schedule checks:** GAFS cost $360,000; GAFS retail $600,000; EI retail $80,000; EI cost $48,000; COGS (see e) = $360,000 − $48,000 = $312,000.

**c. Initial recognition — purchases (Year 1 summary)**

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 288,000 | |
| Accounts Payable | | 288,000 |
| *Record merchandise purchases at cost (retail $480,000 tracked for retail method)* | | |

**Check:** Dr 288,000 = Cr 288,000. **Balanced.**

**d. Disposal — sales for the period**

| Account | Debit | Credit |
|---|---:|---:|
| Cash (and/or Accounts Receivable) | 520,000 | |
| Sales Revenue | | 520,000 |
| *Record sales; removes $520,000 retail from goods available in the schedule* | | |

**Check:** Dr 520,000 = Cr 520,000. **Balanced.**

**e. Cost of goods sold and period-end adjusting JE**

COGS = Goods available at cost − Ending inventory at cost  
= $360,000 − $48,000 = **$312,000**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 48,000 | |
| Cost of Goods Sold | 312,000 | |
| Inventory (beginning) | | 72,000 |
| Purchases | | 288,000 |
| *Close BI and purchases; establish average-cost-retail EI and COGS* | | |

**Check:** Dr $48,000 + $312,000 = $360,000; Cr $72,000 + $288,000 = $360,000. **Balanced.**

**f. Conceptual**  
Under the **average cost retail method**, net markdowns are part of the retail of goods available used in the cost ratio so the ratio reflects average cost including markdowned goods. Under the **conventional retail method**, net markdowns are excluded from the cost-ratio denominator (only deducted when measuring EI at retail), which **lowers** the ratio and approximates LCM.

**Key insight:** The average cost retail **schedule** is the subsequent measurement engine: one cost ratio applied to EI at retail converts the retail rollforward into an estimated **cost** carrying amount for the balance sheet and COGS.

---

### Q2 — CORE number variant — Average cost retail schedule, JEs, COGS
**LO:** LO 10-8  
**Concept:** Number-variant twin — average cost retail cost-to-retail schedule; purchase recognition; period-end inventory/COGS adjusting JE  
**Scenario:**  
**Brookline Home Goods Inc.** (calendar year-end) estimates ending inventory with the **average cost retail method** under a **periodic** system. Beginning inventory is **$80,000** at cost and **$125,000** at retail.

Year 1 activity:

| Item | Cost | Retail |
|---|---:|---:|
| Purchases (on account) | $320,000 | $500,000 |
| Additional markups | — | 42,000 |
| Additional markup cancellations | — | 7,000 |
| Markdowns | — | 28,000 |
| Markdown cancellations | — | 8,000 |
| Sales | — | 560,000 |

No other adjustments.

**Required:**  
a. Compute net markups and net markdowns.  
b. Prepare the full **average cost retail subsequent measurement schedule** and estimate ending inventory at cost.  
c. Record the purchase JE and the December 31 period-end inventory/COGS adjusting JE.  
d. State COGS and verify that BI + Purchases − EI = COGS.

**Answer key:**  

**a.**  
Net markups = $42,000 − $7,000 = **$35,000**  
Net markdowns = $28,000 − $8,000 = **$20,000**

**b. Average cost retail schedule**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $80,000 | $125,000 |
| Purchases | 320,000 | 500,000 |
| Net markups | — | 35,000 |
| Net markdowns | — | (20,000) |
| **Goods available for sale** | **$400,000** | **$640,000** |
| Net sales | | (560,000) |
| **Estimated ending inventory at retail** | | **$80,000** |

Cost ratio = \(400{,}000 / 640{,}000 = 0.625\)

Ending inventory at cost = \(80{,}000 \times 0.625 = \mathbf{\$50{,}000}\)

**c. Journal entries**

*Purchases (initial recognition):*

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 320,000 | |
| Accounts Payable | | 320,000 |
| *Record purchases at cost* | | |

**Check:** Dr 320,000 = Cr 320,000. **Balanced.**

*December 31 period-end adjusting JE:*  
COGS = $400,000 − $50,000 = **$350,000**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 50,000 | |
| Cost of Goods Sold | 350,000 | |
| Inventory (beginning) | | 80,000 |
| Purchases | | 320,000 |
| *Establish EI at average cost retail; close BI and purchases* | | |

**Check:** Dr $50,000 + $350,000 = $400,000; Cr $80,000 + $320,000 = $400,000. **Balanced.**

**d. Verification**  
BI + Purchases − EI = $80,000 + $320,000 − $50,000 = **$350,000** = COGS.

**Key insight:** Changing every input amount still follows the same three-step path—EI at retail → cost ratio with **both** markups and markdowns → EI at cost—then the period-end JE always balances if COGS = GAFS cost − EI cost.

---

### Q3 — CORE alternate angle — Conventional retail with complications; physical-count settlement
**LO:** LO 10-8  
**Concept:** Conventional retail subsequent measurement schedule (markdowns excluded from cost ratio); complicating factors; period-end EI JE; physical inventory settlement (shrinkage) JE  
**Scenario:**  
**Redwood Retail Group** uses the **conventional retail method** (approximates lower of average cost or market). It maintains a periodic inventory system. Data for the year ended **December 31, Year 1** (amounts already stated at cost or retail as indicated; sales returns relate to merchandise restored to inventory):

| Item | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $25,000 | $50,000 |
| Purchases | 200,000 | 350,000 |
| Freight-in | 5,000 | — |
| Purchase returns | 5,000 | 10,000 |
| Net markups | — | 15,000 |
| Abnormal casualty loss (theft exceeding expectations) | 15,000 | 30,000 |
| Sales (gross) | — | 280,000 |
| Sales returns (goods restored to inventory) | — | 10,000 |
| Employee discounts | — | 2,000 |
| Normal spoilage | — | 3,000 |
| Net markdowns | — | 25,000 |

**Additional fact:** A year-end **physical count** extends to **$72,000 at retail**. Management treats the difference between estimated ending inventory at retail and the physical count as **shrinkage** (normal operating loss charged to COGS). Beginning inventory on the books is $25,000; net purchases on the books after recording freight-in and purchase returns = $200,000 + $5,000 − $5,000 = **$200,000** of purchase-related cost accounts (treat “Purchases” net of returns as $195,000 plus Freight-in $5,000, or use a single Net Purchases control of $200,000 for the closing entry—see answer key).

**Required:**  
a. Prepare the full **conventional retail subsequent measurement schedule**, properly placing freight-in, purchase returns, abnormal casualty, sales returns, employee discounts, normal spoilage, and net markdowns. Compute the cost ratio and **estimated** ending inventory at cost **before** considering the physical count.  
b. Compare in one short computation what the **average cost retail** cost ratio **would have been** using the same goods-available totals **if** net markdowns were included in the cost-ratio denominator (retail GAFS for ratio only).  
c. Record the **period-end adjusting JE** to establish inventory at the **estimated** conventional amount and close BI and net purchase costs into COGS (use estimated EI from part a; ignore casualty loss entry already assumed recorded when the loss occurred).  
d. Compute shrinkage at retail and at cost; record the **settlement JE** to write inventory down from the retail-method estimate to the physical-count amount at cost.  
e. State ending inventory reported on the balance sheet after the physical-count settlement.

**Answer key:**  

**a. Conventional retail subsequent measurement schedule**

Under conventional retail, **net markdowns are excluded** from goods available used in the **cost ratio** but are deducted (with net sales, employee discounts, and normal spoilage) when computing **ending inventory at retail**.

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $25,000 | $50,000 |
| Purchases | 200,000 | 350,000 |
| Freight-in | 5,000 | — |
| Purchase returns | (5,000) | (10,000) |
| Net markups | — | 15,000 |
| Abnormal casualty loss | (15,000) | (30,000) |
| **Goods available for sale (for cost ratio)** | **$210,000** | **$375,000** |
| Net sales ($280,000 − $10,000) | | (270,000) |
| Employee discounts | | (2,000) |
| Normal spoilage | | (3,000) |
| Net markdowns | | (25,000) |
| **Estimated ending inventory at retail** | | **$75,000** |

Cost-to-retail ratio (conventional):

\[
\frac{\$210{,}000}{\$375{,}000} = 0.560
\]

Estimated ending inventory at cost (before physical count):

\[
\$75{,}000 \times 0.560 = \mathbf{\$42{,}000}
\]

**Placement notes (core treatments):**  
- Freight-in → cost only (before ratio).  
- Purchase returns → cost and retail (before ratio).  
- Abnormal casualty → remove cost and retail **before** ratio (as if never purchased).  
- Net sales, employee discounts, normal spoilage, net markdowns → **after** ratio (retail only for EI at retail).

**b. Average cost retail cost ratio (contrast only)**  
If net markdowns were included in the cost-ratio retail denominator:  
Retail for average-cost ratio = $375,000 − $25,000 = **$350,000**  
Average cost ratio = $210,000 / $350,000 = **0.600**  
(Conventional 0.560 < average 0.600 → conventional EI would be lower for the same EI at retail, approximating LCM.)

**c. Period-end adjusting JE (estimated EI $42,000)**

Net purchase-related cost to close = Purchases $200,000 + Freight-in $5,000 − Purchase returns $5,000 = **$200,000**  
(Casualty loss already removed from inventory cost when recognized; not closed through this entry.)

GAFS cost remaining in inventory accounts before EI = BI $25,000 + Net purchases $200,000 = **$225,000**  
Wait—after casualty, goods available for sale at cost for COGS purposes:  
The schedule’s GAFS for ratio is $210,000 after removing $15,000 casualty. Beginning inventory $25,000 + net purch $200,000 − casualty $15,000 = $210,000.  
COGS (before shrink) = $210,000 − $42,000 = **$168,000**  
(Alternatively: if casualty loss was already expensed separately at $15,000 cost, books still hold BI $25,000 + net purch $200,000 = $225,000 of inventory-related costs; closing then establishes EI $42,000 and residual COGS $183,000, of which $15,000 might already be in a casualty loss account—**preferred clean approach below**: assume casualty was removed from Purchases/Inventory via a prior entry debiting Casualty Loss $15,000 and crediting Purchases or Inventory $15,000, so remaining cost to allocate is $210,000.)

*Assume abnormal casualty already recorded:*

| Account | Debit | Credit |
|---|---:|---:|
| Casualty Loss (or COGS—abnormal) | 15,000 | |
| Purchases (or Inventory) | | 15,000 |
| *Remove abnormal casualty from goods available (already recorded earlier)* | | |

**Check:** Dr 15,000 = Cr 15,000. **Balanced.**

*Period-end inventory close (GAFS cost now $210,000):*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending, estimated) | 42,000 | |
| Cost of Goods Sold | 168,000 | |
| Inventory (beginning) | | 25,000 |
| Purchases (net of returns, freight-in, after casualty removal) | | 185,000 |
| *Close BI and remaining purchase costs; set conventional retail EI* | | |

**Purchase cost reconciliation:** Gross purchases $200,000 + freight $5,000 − returns $5,000 − casualty $15,000 = **$185,000**.  
**Check:** Dr $42,000 + $168,000 = $210,000; Cr $25,000 + $185,000 = $210,000. **Balanced.**

**d. Physical-count settlement (shrinkage)**

Estimated EI at retail $75,000 − Physical count at retail $72,000 = **$3,000** shortage at retail  
Shrinkage at cost = $3,000 × 0.560 = **$1,680**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold (shrinkage) | 1,680 | |
| Inventory | | 1,680 |
| *Settle retail-method estimate to physical count at conventional cost ratio* | | |

**Check:** Dr 1,680 = Cr 1,680. **Balanced.**

**e. Balance sheet inventory after settlement**  
$42,000 − $1,680 = **$40,320**

**Key insight:** Conventional retail’s subsequent schedule deliberately **inflates** the retail denominator (by omitting net markdowns) so the cost ratio is lower—then employee discounts, normal spoilage, and physical shrink are settled **after** the ratio so they do not distort average cost-or-market approximation.

---

### Q4 — MC (method / classification)
**LO:** LO 10-8  
**Concept:** Classify treatment of net markdowns and what each retail method approximates  

**Question 1:** Under the **average cost retail method**, how are **net markdowns** treated when computing the **cost-to-retail ratio**?  
- A) Excluded from both the cost ratio and the computation of ending inventory at retail  
- B) Included in goods available for sale at retail in the cost-ratio denominator (and deducted when computing ending inventory at retail)  
- C) Added to goods available for sale at **cost** only  
- D) Treated identically to employee discounts (deducted only after the cost ratio, never affecting the ratio)

**Answer:** **B.** Average cost retail includes net markups **and** net markdowns in GAFS at retail for the cost ratio; ending inventory at retail is still GAFS retail − sales (and other post-ratio retail deductions if any). Conventional retail is the method that excludes net markdowns from the cost-ratio denominator.

---

**Question 2:** Relative to the average cost retail method applied to the **same data**, the conventional retail method typically produces a **lower** estimated ending inventory at cost because:  
- A) It uses a **higher** cost ratio by excluding sales from the computation  
- B) It values inventory at replacement cost rather than historical cost  
- C) Excluding net markdowns from the cost-ratio retail denominator **increases** that denominator, **decreases** the cost ratio, and thus approximates lower of cost or market  
- D) It always applies LIFO layers to retail inventory

**Answer:** **C.** Conventional retail omits net markdowns from the cost-ratio denominator → larger retail base → lower cost ratio → lower EI at cost (LCM approximation). It does not, by itself, create LIFO layers (that is LO 10-9).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (Q1 ratio 0.600 EI $48,000; Q2 ratio 0.625 EI $50,000; Q3 ratio 0.560 EI $42,000, shrink $1,680 → $40,320)
- [x] Core demo not sidebar-only (Demo 10-8A/B/C path: average cost, conventional, complications)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method MCs)
- [x] Emphasis on subsequent_measurement_schedule (full cost/retail schedules in Q1–Q3)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (sales + physical settlement)
