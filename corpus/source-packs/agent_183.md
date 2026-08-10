# Agent 183 — CORE DEMO — LO 9-5

**Chapter:** 9  
**LO title:** Demonstrate moving average, FIFO, and LIFO in a perpetual inventory system  
**Critical gap LO:** no

## Concept list for this pack
- **Perpetual system:** Inventory and COGS updated at **each** purchase and each sale (not only at period-end)
- **Moving average (perpetual):** recompute unit cost after **every purchase**; apply latest average to sales and ending inventory
- **FIFO (perpetual):** assign **earliest** remaining cost layers to each sale; EI = latest purchases (same EI/COGS as periodic FIFO)
- **LIFO (perpetual):** assign **latest** remaining layers **as of each sale date** to COGS; EI tends to retain older layers (generally **differs** from periodic LIFO)
- **Subsequent measurement schedule:** perpetual inventory card (purchases / cost of sales / balance) after every transaction
- **Initial recognition JE:** Dr Inventory / Cr Accounts Payable (or Cash) at invoice cost — same under all three cost-flow methods
- **Disposal / settlement JE:** sale — Dr AR (Cash) / Cr Sales; Dr COGS / Cr Inventory at method-assigned cost
- **Period-end adjusting JE:** physical count vs perpetual books — shortage/overage against Inventory (often closed via shortage loss into COGS)
- Rising-cost ranking: EI FIFO ≥ MA ≥ LIFO; COGS LIFO ≥ MA ≥ FIFO (typical)

---

### Q1 — CORE — Crestvale Components: perpetual MA / FIFO / LIFO schedules + purchase and sale JEs
**LO:** LO 9-5  
**Concept:** Subsequent measurement schedules under moving average, FIFO, and LIFO (perpetual); initial purchase recognition; sale/COGS settlement under moving average  
**Scenario:**  
**Crestvale Components LLC** sells a single SKU of industrial valve gaskets and maintains a **perpetual** inventory system. Purchases are recorded under the **gross method** on account. Unit selling prices are given below. Purchase costs rose during April.

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Apr 1 | Beginning inventory | 500 | $10 cost |
| Apr 5 | Purchase on account | 300 | $14 cost |
| Apr 12 | Credit sale | 400 | $25 selling price |
| Apr 18 | Purchase on account | 600 | $16 cost |
| Apr 25 | Credit sale | 500 | $27 selling price |
| Apr 30 | Purchase on account | 200 | $17 cost |

No returns, discounts, or freight-in. Physical quantities match perpetual records at month-end (no shrink for this item).

**Required:**  
(a) Prepare a **perpetual inventory cost schedule** under the **moving average** method. After each purchase, show the new unit average; for each sale, show COGS. Compute April **ending inventory** and **COGS**.  
(b) Prepare a **perpetual inventory cost schedule** under **FIFO** (layer tracking). Compute April **ending inventory** and **COGS**.  
(c) Prepare a **perpetual inventory cost schedule** under **LIFO** (layer tracking at each sale date). Compute April **ending inventory** and **COGS**.  
(d) **Initial recognition:** journal entries for the three **purchases** (perpetual, gross method, on account).  
(e) **Disposal / settlement of inventory:** sales revenue and COGS journal entries for Apr 12 and Apr 25 **under the moving average** method.  
(f) Verify COGAS − EI = COGS for all three methods. Rank methods by highest **ending inventory** and highest **COGS** in this rising-cost setting. State how Inventory is presented and what cost-flow disclosure is required.

**Answer key:**

**Cost of goods available for sale (all methods)**  
Beginning inventory: \(500 \times \$10 = \$5{,}000\)  
Purchases: \(300\times\$14 + 600\times\$16 + 200\times\$17 = \$4{,}200 + \$9{,}600 + \$3{,}400 = \$17{,}200\)  
**COGAS = \$5{,}000 + \$17{,}200 = \$22{,}200**  
Units available \(500+300+600+200=1{,}600\); units sold \(400+500=900\); **EI units = 700**.

**(a) Moving average — perpetual (subsequent measurement schedule)**

| Date | Purchases (u × $) | COGS (u × $) | Inventory balance |
|---|---|---|---|
| Apr 1 | | | 500 × $10 = **$5,000** |
| Apr 5 | 300 × $14 = $4,200 | | 800 × **$11.50** = **$9,200** *(5,000+4,200)/800* |
| Apr 12 | | 400 × $11.50 = **$4,600** | 400 × $11.50 = **$4,600** |
| Apr 18 | 600 × $16 = $9,600 | | 1,000 × **$14.20** = **$14,200** *(4,600+9,600)/1,000* |
| Apr 25 | | 500 × $14.20 = **$7,100** | 500 × $14.20 = **$7,100** |
| Apr 30 | 200 × $17 = $3,400 | | 700 × **$15.00** = **$10,500** *(7,100+3,400)/700* |

**Moving average: Ending inventory = \$10,500; COGS = \$4,600 + \$7,100 = \$11,700**

**(b) FIFO — perpetual**

| Date | Purchases | COGS (layers) | Inventory layers |
|---|---|---|---|
| Apr 1 | | | 500 @ $10 = $5,000 |
| Apr 5 | 300 @ $14 = $4,200 | | 500 @ $10; 300 @ $14 |
| Apr 12 | | 400 @ $10 = **$4,000** | 100 @ $10; 300 @ $14 = $5,200 |
| Apr 18 | 600 @ $16 = $9,600 | | 100 @ $10; 300 @ $14; 600 @ $16 |
| Apr 25 | | 100 @ $10 + 300 @ $14 + 100 @ $16 = **$6,800** | 500 @ $16 = $8,000 |
| Apr 30 | 200 @ $17 = $3,400 | | 500 @ $16 + 200 @ $17 |

**FIFO EI layers:** \(500\times\$16 + 200\times\$17 = \$8{,}000 + \$3{,}400 = \mathbf{\$11{,}400}\)  
**FIFO COGS:** \(\$4{,}000 + \$6{,}800 = \mathbf{\$10{,}800}\)

**(c) LIFO — perpetual**

| Date | Purchases | COGS (layers) | Inventory layers |
|---|---|---|---|
| Apr 1 | | | 500 @ $10 = $5,000 |
| Apr 5 | 300 @ $14 = $4,200 | | 500 @ $10; 300 @ $14 |
| Apr 12 | | 300 @ $14 + 100 @ $10 = **$5,200** | 400 @ $10 = $4,000 |
| Apr 18 | 600 @ $16 = $9,600 | | 400 @ $10; 600 @ $16 |
| Apr 25 | | 500 @ $16 = **$8,000** | 400 @ $10; 100 @ $16 = $5,600 |
| Apr 30 | 200 @ $17 = $3,400 | | 400 @ $10 + 100 @ $16 + 200 @ $17 |

**LIFO EI layers:** \(400\times\$10 + 100\times\$16 + 200\times\$17 = \$4{,}000 + \$1{,}600 + \$3{,}400 = \mathbf{\$9{,}000}\)  
**LIFO COGS:** \(\$5{,}200 + \$8{,}000 = \mathbf{\$13{,}200}\)

**(d) Initial recognition — purchase JEs (same under all three cost-flow methods; perpetual gross)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Apr 5 | Inventory | 4,200 | |
| | Accounts Payable | | 4,200 |
| | *Purchase 300 units @ $14 on account* | | |

**Check:** Dr = Cr = 4,200.

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Apr 18 | Inventory | 9,600 | |
| | Accounts Payable | | 9,600 |
| | *Purchase 600 units @ $16 on account* | | |

**Check:** Dr = Cr = 9,600.

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Apr 30 | Inventory | 3,400 | |
| | Accounts Payable | | 3,400 |
| | *Purchase 200 units @ $17 on account* | | |

**Check:** Dr = Cr = 3,400.

**(e) Settlement / disposal — April sales under moving average (perpetual)**

Apr 12 — revenue \(400 \times \$25 = \$10{,}000\); MA COGS \$4,600:

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 10,000 | |
| Sales Revenue | | 10,000 |
| *Credit sale of 400 units @ $25* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 4,600 | |
| Inventory | | 4,600 |
| *Remove 400 units @ moving-average $11.50* | | |

**Check:** Each JE balances (Dr = Cr).

Apr 25 — revenue \(500 \times \$27 = \$13{,}500\); MA COGS \$7,100:

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 13,500 | |
| Sales Revenue | | 13,500 |
| *Credit sale of 500 units @ $27* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 7,100 | |
| Inventory | | 7,100 |
| *Remove 500 units @ moving-average $14.20* | | |

**Check:** Each JE balances (Dr = Cr).

**(f) Verification, ranking, presentation**

| Method | EI | COGS | Check: COGAS − EI |
|---|---:|---:|---:|
| Moving average | $10,500 | $11,700 | 22,200 − 10,500 = 11,700 |
| FIFO | $11,400 | $10,800 | 22,200 − 11,400 = 10,800 |
| LIFO | $9,000 | $13,200 | 22,200 − 9,000 = 13,200 |

**Rising costs:** highest **EI** = FIFO (\$11,400) > MA (\$10,500) > LIFO (\$9,000); highest **COGS** = LIFO > MA > FIFO (inverse).  
**Presentation:** Merchandise inventory is a **current asset** at historical cost under the elected cost-flow assumption. The cost-flow **method** (FIFO, LIFO, or average) is a **significant accounting policy** disclosed in the notes. Gross margin under MA: sales \(10{,}000+13{,}500=\$23{,}500\) − COGS \$11,700 = **\$11,800**.

**Key insight:** The perpetual **subsequent measurement schedule** is the exam core of LO 9-5: after every purchase, recompute MA unit cost (or stack layers for FIFO/LIFO); at each sale, relieve Inventory using that method’s rule. Purchase JEs always debit Inventory at invoice cost; only the **COGS/Inventory** pair differs by method.

---

### Q2 — CORE number variant — Harborline Tools: perpetual MA, FIFO, LIFO
**LO:** LO 9-5  
**Concept:** Number-variant twin — perpetual subsequent measurement schedules under MA, FIFO, and LIFO; purchase recognition; LIFO sale settlement JEs  
**Scenario:**  
**Harborline Tools Corp.** maintains perpetual inventory records for a portable work-light SKU. Purchases are on account (gross method). November activity:

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Nov 1 | Beginning inventory | 800 | $6 cost |
| Nov 4 | Purchase on account | 400 | $9 cost |
| Nov 10 | Credit sale | 600 | $15 selling price |
| Nov 15 | Purchase on account | 600 | $11 cost |
| Nov 22 | Credit sale | 450 | $16 selling price |
| Nov 28 | Purchase on account | 250 | $15 cost |

**Required:**  
(a) Compute November **ending inventory** and **COGS** under (1) **moving average**, (2) **FIFO**, and (3) **LIFO** perpetual. Show the inventory balance (unit cost or layers) after each purchase and after each sale.  
(b) Prepare **initial recognition** journal entries for the three purchases.  
(c) Prepare **sales and COGS** journal entries for Nov 10 and Nov 22 **under LIFO**.  
(d) Confirm COGAS − EI = COGS for all three methods.

**Answer key:**

**COGAS**  
BI \(800\times\$6=\$4{,}800\); purchases \(400\times\$9 + 600\times\$11 + 250\times\$15 = \$3{,}600 + \$6{,}600 + \$3{,}750 = \$13{,}950\)  
**COGAS = \$18{,}750**  
Units available \(800+400+600+250=2{,}050\); sold \(600+450=1{,}050\); **EI units = 1,000**.

**(a1) Moving average**

| Date | Event | Inventory balance / COGS |
|---|---|---|
| Nov 1 | BI | 800 × $6 = $4,800 |
| Nov 4 | +400 @ $9 | 1,200 × **$7.00** = $8,400 *(4,800+3,600)/1,200* |
| Nov 10 | Sale 600 @ $7.00 | COGS **$4,200**; bal 600 × $7 = $4,200 |
| Nov 15 | +600 @ $11 | 1,200 × **$9.00** = $10,800 *(4,200+6,600)/1,200* |
| Nov 22 | Sale 450 @ $9.00 | COGS **$4,050**; bal 750 × $9 = $6,750 |
| Nov 28 | +250 @ $15 | 1,000 × **$10.50** = **$10,500** *(6,750+3,750)/1,000* |

**MA: EI = \$10,500; COGS = \$4,200 + \$4,050 = \$8,250**

**(a2) FIFO perpetual**

| Date | COGS layers | Ending layers |
|---|---|---|
| Nov 1 | | 800 @ $6 |
| Nov 4 | | 800 @ $6; 400 @ $9 |
| Nov 10 | 600 @ $6 = **$3,600** | 200 @ $6; 400 @ $9 = $4,800 |
| Nov 15 | | 200 @ $6; 400 @ $9; 600 @ $11 |
| Nov 22 | 200 @ $6 + 250 @ $9 = **$3,450** | 150 @ $9; 600 @ $11 = $7,950 |
| Nov 28 | | 150 @ $9 + 600 @ $11 + 250 @ $15 |

**FIFO EI:** \(150\times\$9 + 600\times\$11 + 250\times\$15 = \$1{,}350 + \$6{,}600 + \$3{,}750 = \mathbf{\$11{,}700}\)  
**FIFO COGS:** \(\$3{,}600 + \$3{,}450 = \mathbf{\$7{,}050}\)

**(a3) LIFO perpetual**

| Date | COGS layers | Ending layers |
|---|---|---|
| Nov 1 | | 800 @ $6 |
| Nov 4 | | 800 @ $6; 400 @ $9 |
| Nov 10 | 400 @ $9 + 200 @ $6 = **$4,800** | 600 @ $6 = $3,600 |
| Nov 15 | | 600 @ $6; 600 @ $11 |
| Nov 22 | 450 @ $11 = **$4,950** | 600 @ $6; 150 @ $11 = $5,250 |
| Nov 28 | | 600 @ $6 + 150 @ $11 + 250 @ $15 |

**LIFO EI:** \(600\times\$6 + 150\times\$11 + 250\times\$15 = \$3{,}600 + \$1{,}650 + \$3{,}750 = \mathbf{\$9{,}000}\)  
**LIFO COGS:** \(\$4{,}800 + \$4{,}950 = \mathbf{\$9{,}750}\)

**(b) Initial recognition — purchases**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Nov 4 | Inventory | 3,600 | |
| | Accounts Payable | | 3,600 |
| Nov 15 | Inventory | 6,600 | |
| | Accounts Payable | | 6,600 |
| Nov 28 | Inventory | 3,750 | |
| | Accounts Payable | | 3,750 |

**Check:** Each entry balances (Dr = Cr).

**(c) Settlement under LIFO**

Nov 10 (\(600\times\$15=\$9{,}000\) revenue; LIFO COGS \$4,800):

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 9,000 | |
| Sales Revenue | | 9,000 |
| Cost of Goods Sold | 4,800 | |
| Inventory | | 4,800 |
| *LIFO layers: 400 @ $9 + 200 @ $6* | | |

Nov 22 (\(450\times\$16=\$7{,}200\) revenue; LIFO COGS \$4,950):

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 7,200 | |
| Sales Revenue | | 7,200 |
| Cost of Goods Sold | 4,950 | |
| Inventory | | 4,950 |
| *LIFO layers: 450 @ $11* | | |

**Check:** All JEs balance (Dr = Cr on each pair).

**(d) Verification**

| Method | EI | COGS | COGAS − EI |
|---|---:|---:|---:|
| Moving average | $10,500 | $8,250 | 18,750 − 10,500 = 8,250 |
| FIFO | $11,700 | $7,050 | 18,750 − 11,700 = 7,050 |
| LIFO | $9,000 | $9,750 | 18,750 − 9,000 = 9,750 |

**Key insight:** Same purchase and sale **quantities**, different cost assignments only. Purchase recognition always debits Inventory at invoice cost; the cost-flow method only changes **which cost leaves inventory** when COGS is recorded on each sale date under perpetual LIFO (or MA/FIFO).

---

### Q3 — CORE alternate angle — Mapleford Distributors: LIFO perpetual schedule + settlement + period-end shortage
**LO:** LO 9-5  
**Concept:** Perpetual LIFO subsequent measurement schedule; sale settlement JEs; period-end physical-count adjusting JE; FIFO vs LIFO perpetual/periodic note  
**Scenario:**  
**Mapleford Distributors Inc.** uses a **perpetual LIFO** system for a specialty packing strap product. September records:

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Sep 1 | Beginning inventory | 150 | $40 |
| Sep 6 | Purchase on account | 200 | $42 |
| Sep 11 | Credit sale | 180 | $65 SP |
| Sep 19 | Purchase on account | 120 | $45 |
| Sep 26 | Credit sale | 100 | $68 SP |

On **September 30**, a physical count finds **185 units** on hand. Perpetual LIFO records show **190 units**. Management concludes the **5-unit** shortage is from theft/spoilage and should be removed from the **most recent remaining layer** (latest unit cost still in inventory), with the loss recorded as **Loss on Inventory Shortage** (reported as part of COGS on the multi-step income statement).

**Required:**  
(a) Prepare the perpetual **LIFO** inventory schedule through September 26 (before the count). Compute book EI and COGS.  
(b) Prepare **initial recognition** purchase JEs and **sale/COGS settlement** JEs for September (LIFO).  
(c) Prepare the **period-end adjusting** entry for the inventory shortage. State the adjusted ending inventory cost and remaining layers.  
(d) **Classification / presentation:** (1) How is Inventory presented? (2) How is the shortage loss classified? (3) Briefly explain why **FIFO** EI/COGS would be the **same** under perpetual and periodic systems (ignore shrink), whereas **LIFO** generally **differs** perpetual vs periodic.

**Answer key:**

**(a) LIFO perpetual schedule (subsequent measurement)**

| Date | Event | COGS | Inventory layers |
|---|---|---|---|
| Sep 1 | BI | | 150 @ $40 = $6,000 |
| Sep 6 | Purchase | | 150 @ $40; 200 @ $42 |
| Sep 11 | Sale 180 | 180 @ $42 = **$7,560** | 150 @ $40; 20 @ $42 = $6,840 |
| Sep 19 | Purchase | | 150 @ $40; 20 @ $42; 120 @ $45 |
| Sep 26 | Sale 100 | 100 @ $45 = **$4,500** | 150 @ $40; 20 @ $42; 20 @ $45 |

**Book EI (before count):** \(150\times\$40 + 20\times\$42 + 20\times\$45 = \$6{,}000 + \$840 + \$900 = \mathbf{\$7{,}740}\) (190 units)  
**COGS (sales only):** \(\$7{,}560 + \$4{,}500 = \mathbf{\$12{,}060}\)  
COGAS \(=\$6{,}000 + \$8{,}400 + \$5{,}400 = \$19{,}800\); \(19{,}800 - 7{,}740 = 12{,}060\) ✓

**(b) Journal entries**

Sep 6 purchase (\(200\times\$42=\$8{,}400\)):

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 8,400 | |
| Accounts Payable | | 8,400 |

**Check:** Dr = Cr = 8,400.

Sep 11 sale (\(180\times\$65=\$11{,}700\); LIFO COGS \$7,560):

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 11,700 | |
| Sales Revenue | | 11,700 |
| Cost of Goods Sold | 7,560 | |
| Inventory | | 7,560 |
| *LIFO: 180 @ $42* | | |

**Check:** Each JE balances.

Sep 19 purchase (\(120\times\$45=\$5{,}400\)):

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 5,400 | |
| Accounts Payable | | 5,400 |

**Check:** Dr = Cr = 5,400.

Sep 26 sale (\(100\times\$68=\$6{,}800\); LIFO COGS \$4,500):

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 6,800 | |
| Sales Revenue | | 6,800 |
| Cost of Goods Sold | 4,500 | |
| Inventory | | 4,500 |
| *LIFO: 100 @ $45* | | |

**Check:** Each JE balances.

**(c) Period-end adjusting JE — shortage**  
Remove 5 units from latest remaining layer @ $45: \(5\times\$45=\mathbf{\$225}\).

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 225 | |
| Inventory | | 225 |
| *Physical count 185 vs book 190; remove 5 @ $45 LIFO residual layer* | | |

**Check:** Dr = Cr = 225.

**Adjusted ending inventory:** \(7{,}740 - 225 = \mathbf{\$7{,}515}\)  
**Remaining layers:** 150 @ $40 + 20 @ $42 + **15** @ $45.  
If shortage is closed into COGS, total inventory-related product cost affecting income \(= 12{,}060 + 225 = \$12{,}285\).

**(d) Classification / presentation / FIFO vs LIFO system note**  
1. **Inventory** remains a **current asset** at historical cost under the elected cost-flow assumption (here perpetual LIFO after shrink).  
2. **Loss on Inventory Shortage** is typically included in **cost of goods sold** (or shown separately within operating results if material); it is **not** a prior-period restatement for normal shrink.  
3. **FIFO** assigns earliest costs to COGS whether assignment is continuous (perpetual) or at period-end (periodic), so **EI and COGS are the same** under both systems (absent separate mid-period shrink). **LIFO** assigns “latest” costs **as of each sale date** under perpetual, which generally **differs** from assigning the month’s latest purchases only at period-end under periodic LIFO.

**Key insight:** Perpetual LIFO’s subsequent measurement schedule peels the newest layer **available at the sale date**, not the newest purchase of the whole period. Physical counts still adjust Inventory; policy (here: latest residual layer) determines which unit costs leave the books for shortage.

---

### Q4 — MC (method / classification)
**LO:** LO 9-5  
**Concept:** Classification of perpetual cost-flow results (moving-average update rule; LIFO layer composition)

**Question 1:**  
Under the **moving average** method in a **perpetual** inventory system, a new unit cost is computed:  
- A) Only at period-end for all units available during the period  
- B) After every purchase (and that updated average is used to cost subsequent sales until the next purchase)  
- C) After every sale only  
- D) Only when physical inventory is taken  

**Answer:** **B.** Perpetual moving average recalculates unit cost after **each purchase** by dividing total inventory cost by total units on hand; that average is applied to sales occurring before the next purchase. A describes **periodic weighted-average** cost; C and D are incorrect.

**Question 2:**  
In a **rising-cost** environment under **perpetual LIFO**, ending inventory typically consists primarily of:  
- A) Only the most recently purchased units  
- B) A single moving-average unit cost applied to all remaining units  
- C) The earliest purchases still on hand (older layers), often plus residual amounts of more recent layers not fully depleted by sales  
- D) Net realizable value of the units on hand  

**Answer:** **C.** Perpetual LIFO removes the latest layers available **at each sale date**, so remaining inventory tends to hold older (lower, when costs are rising) layers, often mixed with small residual recent layers. A describes FIFO EI; B describes moving average; D is not the historical-cost LIFO measurement basis for this LO.

---

### Self-check
- [x] Every JE balances
- [x] Math recomputed (COGAS − EI = COGS for all schedules)
- [x] Core demo not sidebar-only (Demo 9-5A/B/C perpetual MA, FIFO, LIFO path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 if any (exactly 2 MC)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Demo 9-5 data)
