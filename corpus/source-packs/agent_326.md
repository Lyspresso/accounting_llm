# Agent 326 — CORE DEMO — LO 10-8

**Chapter:** 10  
**LO title:** Estimate ending inventory using the average cost and conventional retail methods  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Retail inventory method (three steps):** (1) estimate ending inventory at **retail**, (2) compute **cost-to-retail ratio**, (3) multiply EI at retail × cost ratio → **estimated inventory at cost**
- **Average cost retail method:** include **both** net markups and **net markdowns** in goods available for sale at retail when computing the cost ratio → estimate approximates **average cost**
- **Conventional retail method:** include net markups in the cost-ratio denominator; **exclude net markdowns** from the ratio (still deduct them when computing EI at retail) → lower cost ratio approximates **lower of cost or market (LCM)**
- **Net markups** = additional markups − markup cancellations; **net markdowns** = markdowns − markdown cancellations
- **Initial recognition JE:** purchases (and freight-in) recorded at cost; retail tagging is memo for the schedule
- **Subsequent measurement schedule:** multi-column cost/retail rollforward of goods available, cost ratio, and EI at cost
- **Period-end adjusting JE (emphasis):** under a **periodic** system, establish ending inventory at the retail-method estimate, close beginning inventory and purchase-related costs into **COGS** (Dr EI + Dr COGS = Cr BI + Cr Purchases [+ freight − returns])
- **Disposal / settlement:** record **sales** that remove goods from the retail pool; optional **physical-count settlement** when count ≠ estimate (shrinkage charged to COGS)
- **Complicating factors (core Demo 10-8C path):** freight-in (cost only); purchase returns (cost and retail); abnormal casualty (remove cost and retail **before** cost ratio); sales returns; employee discounts and normal spoilage (deduct at retail **after** cost ratio)

---

### Q1 — CORE — Average cost retail: multi-year period-end adjusting JEs (emphasis)
**LO:** LO 10-8  
**Concept:** Average cost retail cost-to-retail schedule; initial purchase/freight recognition; multi-year **period-end inventory/COGS adjusting JEs** (emphasis)  
**Scenario:**  
**Cedarline Outfitters Co.** (calendar year-end) uses the **average cost retail method** to estimate merchandise inventory for external reporting and maintains a **periodic** inventory system. Markups, markdowns, and retail sales are tracked for the retail-method schedule only (they do not create separate general-ledger inventory accounts).

**January 1, Year 1** beginning inventory (already on the books): **$90,000** at cost and **$150,000** at retail.

**Year 1 activity** (not yet closed at year-end):

| Item | Cost | Retail |
|---|---:|---:|
| Purchases (on account) | $350,000 | $600,000 |
| Freight-in (cash) | 10,000 | — |
| Additional markups | — | 55,000 |
| Additional markup cancellations | — | 5,000 |
| Markdowns | — | 58,000 |
| Markdown cancellations | — | 8,000 |
| Net sales (cash and on account) | — | 650,000 |

No purchase returns, employee discounts, or spoilage in Year 1.

**Year 2 activity** (beginning inventory equals Year 1 ending inventory at cost and at retail from the Year 1 average cost retail estimate):

| Item | Cost | Retail |
|---|---:|---:|
| Purchases (on account) | $300,000 | $500,000 |
| Additional markups | — | 28,000 |
| Additional markup cancellations | — | 8,000 |
| Markdowns | — | 35,000 |
| Markdown cancellations | — | 15,000 |
| Net sales | — | 500,000 |

No freight-in or other adjustments in Year 2. Ignore income taxes.

**Required:**  
a. Compute **net markups** and **net markdowns** for Year 1 and Year 2.  
b. Prepare the full **average cost retail subsequent measurement schedule** for **Year 1** (GAFS, cost ratio, EI at retail, EI at cost) and compute **Year 1 COGS**.  
c. Record Year 1 **initial recognition JEs** for purchases and freight-in.  
d. Record the **December 31, Year 1 period-end adjusting JE** that establishes ending inventory and closes beginning inventory, purchases, and freight-in into COGS (**emphasis**). Prove Dr = Cr.  
e. Prepare the full **average cost retail schedule** for **Year 2** and compute Year 2 COGS.  
f. Record the **December 31, Year 2 period-end adjusting JE** (**emphasis**). Prove Dr = Cr.  
g. In one sentence, state why net markdowns are included in the Year 1 cost-ratio denominator under average cost retail (contrast with conventional).

**Answer key:**  

**a. Net markups and net markdowns**

| | Year 1 | Year 2 |
|---|---:|---:|
| Additional markups | $55,000 | $28,000 |
| Markup cancellations | (5,000) | (8,000) |
| **Net markups** | **$50,000** | **$20,000** |
| Markdowns | $58,000 | $35,000 |
| Markdown cancellations | (8,000) | (15,000) |
| **Net markdowns** | **$50,000** | **$20,000** |

**b. Year 1 — average cost retail subsequent measurement schedule**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $90,000 | $150,000 |
| Purchases | 350,000 | 600,000 |
| Freight-in | 10,000 | — |
| Net markups | — | 50,000 |
| Net markdowns | — | (50,000) |
| **Goods available for sale** | **$450,000** | **$750,000** |
| Net sales | | (650,000) |
| **Estimated ending inventory at retail** | | **$100,000** |

Cost-to-retail ratio (average cost):

\[
\frac{\$450{,}000}{\$750{,}000} = \mathbf{0.600}
\]

Estimated ending inventory at cost:

\[
\$100{,}000 \times 0.600 = \mathbf{\$60{,}000}
\]

Year 1 COGS = GAFS cost − EI cost = \(450{,}000 - 60{,}000 = \mathbf{\$390{,}000}\).

**c. Year 1 initial recognition JEs**

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 350,000 | |
| Accounts Payable | | 350,000 |
| *Record merchandise purchases at cost (retail $600,000 tracked for retail method)* | | |

**Check:** Dr 350,000 = Cr 350,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Freight-in | 10,000 | |
| Cash | | 10,000 |
| *Add freight to inventory cost (cost column only)* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.**

**d. December 31, Year 1 — period-end adjusting JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 60,000 | |
| Cost of Goods Sold | 390,000 | |
| Inventory (beginning) | | 90,000 |
| Purchases | | 350,000 |
| Freight-in | | 10,000 |
| *Close BI, purchases, and freight-in; establish average-cost-retail EI and COGS* | | |

**Check:** Dr \(60{,}000 + 390{,}000 = 450{,}000\); Cr \(90{,}000 + 350{,}000 + 10{,}000 = 450{,}000\). **Balanced.**

**e. Year 2 — average cost retail schedule**  
(Beginning inventory = Year 1 EI: **$60,000** cost / **$100,000** retail)

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $60,000 | $100,000 |
| Purchases | 300,000 | 500,000 |
| Net markups | — | 20,000 |
| Net markdowns | — | (20,000) |
| **Goods available for sale** | **$360,000** | **$600,000** |
| Net sales | | (500,000) |
| **Estimated ending inventory at retail** | | **$100,000** |

Cost ratio = \(360{,}000 / 600{,}000 = \mathbf{0.600}\)  
EI at cost = \(100{,}000 \times 0.600 = \mathbf{\$60{,}000}\)  
Year 2 COGS = \(360{,}000 - 60{,}000 = \mathbf{\$300{,}000}\)

**f. December 31, Year 2 — period-end adjusting JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 60,000 | |
| Cost of Goods Sold | 300,000 | |
| Inventory (beginning) | | 60,000 |
| Purchases | | 300,000 |
| *Close BI and purchases; establish Year 2 average-cost-retail EI and COGS* | | |

**Check:** Dr \(60{,}000 + 300{,}000 = 360{,}000\); Cr \(60{,}000 + 300{,}000 = 360{,}000\). **Balanced.**

**g. Conceptual**  
Under **average cost retail**, net markdowns are included in GAFS at retail for the cost ratio so the ratio reflects average cost of goods that were marked down; **conventional retail** excludes net markdowns from the ratio denominator (only deducts them when measuring EI at retail), which lowers the ratio and approximates LCM.

**Key insight:** The period-end adjusting JE is the **bridge** from the retail-method schedule to the financial statements: once EI at cost is estimated, the periodic close always balances if **Dr EI + Dr COGS = Cr BI + Cr purchase-related costs** (GAFS cost).

---

### Q2 — CORE number variant — Average cost retail schedule and period-end close
**LO:** LO 10-8  
**Concept:** Number-variant twin — average cost retail cost-to-retail schedule; purchase recognition; **period-end inventory/COGS adjusting JE**  
**Scenario:**  
**Maplebrook Mercantile Inc.** (calendar year-end) estimates ending inventory with the **average cost retail method** under a **periodic** system. Beginning inventory is **$70,000** at cost and **$100,000** at retail.

Year 1 activity:

| Item | Cost | Retail |
|---|---:|---:|
| Purchases (on account) | $280,000 | $400,000 |
| Additional markups | — | 36,000 |
| Additional markup cancellations | — | 6,000 |
| Markdowns | — | 42,000 |
| Markdown cancellations | — | 12,000 |
| Net sales | — | 420,000 |

No freight-in, returns, employee discounts, or spoilage.

**Required:**  
a. Compute net markups and net markdowns.  
b. Prepare the full **average cost retail subsequent measurement schedule** and estimate ending inventory at cost.  
c. Record the purchase JE and the **December 31 period-end inventory/COGS adjusting JE** (emphasis).  
d. State COGS and verify that BI + Purchases − EI = COGS.

**Answer key:**  

**a.**  
Net markups = \(36{,}000 - 6{,}000 = \mathbf{\$30{,}000}\)  
Net markdowns = \(42{,}000 - 12{,}000 = \mathbf{\$30{,}000}\)

**b. Average cost retail schedule**

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $70,000 | $100,000 |
| Purchases | 280,000 | 400,000 |
| Net markups | — | 30,000 |
| Net markdowns | — | (30,000) |
| **Goods available for sale** | **$350,000** | **$500,000** |
| Net sales | | (420,000) |
| **Estimated ending inventory at retail** | | **$80,000** |

Cost ratio = \(350{,}000 / 500{,}000 = \mathbf{0.700}\)  
Ending inventory at cost = \(80{,}000 \times 0.700 = \mathbf{\$56{,}000}\)

**c. Journal entries**

*Purchases (initial recognition):*

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 280,000 | |
| Accounts Payable | | 280,000 |
| *Record purchases at cost* | | |

**Check:** Dr 280,000 = Cr 280,000. **Balanced.**

*December 31 period-end adjusting JE (emphasis):*  
COGS = \(350{,}000 - 56{,}000 = \mathbf{\$294{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 56,000 | |
| Cost of Goods Sold | 294,000 | |
| Inventory (beginning) | | 70,000 |
| Purchases | | 280,000 |
| *Establish EI at average cost retail; close BI and purchases* | | |

**Check:** Dr \(56{,}000 + 294{,}000 = 350{,}000\); Cr \(70{,}000 + 280{,}000 = 350{,}000\). **Balanced.**

**d. Verification**  
BI + Purchases − EI = \(70{,}000 + 280{,}000 - 56{,}000 = \mathbf{\$294{,}000}\) = COGS.

**Key insight:** Changing every input amount still follows the same path—EI at retail → cost ratio with **both** markups and markdowns → EI at cost—then the period-end JE balances only when COGS equals GAFS cost minus that estimated EI.

---

### Q3 — CORE alternate angle — Conventional retail with complications; period-end close + physical settlement
**LO:** LO 10-8  
**Concept:** Conventional retail subsequent measurement schedule (markdowns excluded from cost ratio); complicating factors; **period-end EI/COGS JE**; physical inventory settlement (shrinkage) JE  
**Scenario:**  
**Summit Peak Retail Group** uses the **conventional retail method** (approximates lower of average cost or market) and a **periodic** inventory system. Data for the year ended **December 31, Year 1** (amounts already stated at cost or retail as indicated; sales returns relate to merchandise restored to inventory):

| Item | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $50,000 | $100,000 |
| Purchases | 200,000 | 400,000 |
| Freight-in | 10,000 | — |
| Purchase returns | 10,000 | 20,000 |
| Net markups | — | 20,000 |
| Abnormal casualty loss (theft exceeding expectations) | 20,000 | 40,000 |
| Sales (gross) | — | 360,000 |
| Sales returns (goods restored to inventory) | — | 20,000 |
| Employee discounts | — | 5,000 |
| Normal spoilage | — | 5,000 |
| Net markdowns | — | 30,000 |

**Additional facts:**  
- Abnormal casualty is recognized when discovered (remove cost and retail from goods available **before** the cost ratio).  
- A year-end **physical count** extends to **$74,000 at retail**. Management treats the difference between estimated ending inventory at retail and the physical count as **shrinkage** (charged to COGS at the conventional cost ratio).  
- Ignore income taxes.

**Required:**  
a. Prepare the full **conventional retail subsequent measurement schedule**, properly placing freight-in, purchase returns, abnormal casualty, sales returns, employee discounts, normal spoilage, and net markdowns. Compute the cost ratio and **estimated** ending inventory at cost **before** the physical count.  
b. Compare in one short computation what the **average cost retail** cost ratio **would have been** if net markdowns were included in the cost-ratio denominator (same pre-ratio cost and retail, then subtract net markdowns from the retail base for the ratio only).  
c. Record: (1) the **casualty removal JE** (assume cost removed from Purchases), (2) the **period-end adjusting JE** establishing inventory at the **estimated** conventional amount and closing BI and remaining purchase costs into COGS (**emphasis**).  
d. Compute shrinkage at retail and at cost; record the **settlement JE** writing inventory down from the retail-method estimate to the physical-count amount at cost.  
e. State ending inventory reported on the balance sheet after the physical-count settlement.

**Answer key:**  

**a. Conventional retail subsequent measurement schedule**

Under conventional retail, **net markdowns are excluded** from goods available used in the **cost ratio** but are deducted (with net sales, employee discounts, and normal spoilage) when computing **ending inventory at retail**.

| | Cost | Retail |
|---|---:|---:|
| Beginning inventory | $50,000 | $100,000 |
| Purchases | 200,000 | 400,000 |
| Freight-in | 10,000 | — |
| Purchase returns | (10,000) | (20,000) |
| Net markups | — | 20,000 |
| Abnormal casualty loss | (20,000) | (40,000) |
| **Goods available for sale (for cost ratio)** | **$230,000** | **$460,000** |
| Net sales (\(360{,}000 - 20{,}000\)) | | (340,000) |
| Employee discounts | | (5,000) |
| Normal spoilage | | (5,000) |
| Net markdowns | | (30,000) |
| **Estimated ending inventory at retail** | | **$80,000** |

Cost-to-retail ratio (conventional):

\[
\frac{\$230{,}000}{\$460{,}000} = \mathbf{0.500}
\]

Estimated ending inventory at cost (before physical count):

\[
\$80{,}000 \times 0.500 = \mathbf{\$40{,}000}
\]

**Placement notes (core treatments):**  
- Freight-in → cost only (before ratio).  
- Purchase returns → cost and retail (before ratio).  
- Abnormal casualty → remove cost and retail **before** ratio (as if never purchased).  
- Net sales, employee discounts, normal spoilage, net markdowns → **after** ratio base (retail only for EI at retail).

**b. Average cost retail cost ratio (contrast only)**  
If net markdowns were included in the cost-ratio retail denominator:  
Retail for average-cost ratio = \(460{,}000 - 30{,}000 = \mathbf{\$430{,}000}\)  
Average cost ratio = \(230{,}000 / 430{,}000 \approx \mathbf{0.535}\)  
(Conventional 0.500 < average ≈ 0.535 → conventional EI is lower for the same EI at retail, approximating LCM.)

**c. Period-end related JEs (emphasis on inventory/COGS close)**

*(1) Abnormal casualty already removed from goods available:*

| Account | Debit | Credit |
|---|---:|---:|
| Casualty Loss (or COGS—abnormal) | 20,000 | |
| Purchases | | 20,000 |
| *Remove abnormal casualty cost from goods available (before cost ratio)* | | |

**Check:** Dr 20,000 = Cr 20,000. **Balanced.**

*(2) Period-end inventory close — estimated EI $40,000*  

Purchase-related cost remaining to close after freight, returns, and casualty:  
\(200{,}000 + 10{,}000 - 10{,}000 - 20{,}000 = \mathbf{\$180{,}000}\)  
GAFS cost for COGS allocation = BI \(50{,}000\) + remaining purchases \(180{,}000\) = **$230,000**  
COGS (before shrink) = \(230{,}000 - 40{,}000 = \mathbf{\$190{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending, estimated) | 40,000 | |
| Cost of Goods Sold | 190,000 | |
| Inventory (beginning) | | 50,000 |
| Purchases (net of returns, freight-in, after casualty removal) | | 180,000 |
| *Close BI and remaining purchase costs; set conventional retail EI* | | |

**Check:** Dr \(40{,}000 + 190{,}000 = 230{,}000\); Cr \(50{,}000 + 180{,}000 = 230{,}000\). **Balanced.**

**d. Physical-count settlement (shrinkage)**

Estimated EI at retail \(80{,}000\) − Physical count at retail \(74{,}000\) = **$6,000** shortage at retail  
Shrinkage at cost = \(6{,}000 \times 0.500 = \mathbf{\$3{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold (shrinkage) | 3,000 | |
| Inventory | | 3,000 |
| *Settle retail-method estimate to physical count at conventional cost ratio* | | |

**Check:** Dr 3,000 = Cr 3,000. **Balanced.**

**e. Balance sheet inventory after settlement**  
\(40{,}000 - 3{,}000 = \mathbf{\$37{,}000}\)

**Key insight:** Conventional retail’s schedule deliberately **inflates** the retail denominator (by omitting net markdowns) so the cost ratio is lower; the **period-end JE** posts that lower EI, and physical shrink is settled **after** the ratio so it does not distort the LCM approximation.

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

**Question 2:** At **period-end** under a periodic system, a retailer that has computed estimated ending inventory at cost using the average cost retail method should:  
- A) Debit Purchases and credit Inventory for the estimated ending inventory amount only  
- B) Debit Inventory (ending) and Cost of Goods Sold, and credit Inventory (beginning) and purchase-related accounts so that Dr EI + Dr COGS equals GAFS at cost  
- C) Credit Inventory for net sales at retail and debit COGS for net sales at retail  
- D) Make no inventory entry until a physical count is completed, because the retail method is not acceptable under GAAP

**Answer:** **B.** The period-end adjusting/closing entry establishes EI at the retail-method cost estimate and allocates the residual of goods available at cost to COGS; Dr must equal Cr (GAFS cost). The retail method is GAAP-acceptable as an estimation method (ASC 330). Option A misstates the close; C confuses retail sales with cost; D is incorrect.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (Q1 Y1 ratio 0.600 EI $60,000 COGS $390,000; Y2 ratio 0.600 EI $60,000 COGS $300,000; Q2 ratio 0.700 EI $56,000 COGS $294,000; Q3 ratio 0.500 EI $40,000, shrink $3,000 → $37,000)
- [x] Core demo not sidebar-only (Demo 10-8A/B/C path: average cost, conventional, complications)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method MCs)
- [x] Emphasis on period_end_adjusting_JE (multi-year period-end closes in Q1; full close in Q2; estimated EI close + shrink settlement in Q3; MC Q2 on period-end close)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (sales removal from pool + physical settlement)
