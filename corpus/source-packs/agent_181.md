# Agent 181 — CORE DEMO — LO 9-3

**Chapter:** 9  
**LO title:** Demonstrate specific identification, average cost, FIFO, and LIFO in a periodic inventory system  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Initial recognition JE** (periodic): Debit Purchases / credit Cash or AP at acquisition; Inventory permanent account not updated until period end
- Sale under periodic: revenue only at sale (no COGS until physical count / cost-flow allocation)
- **COGAS schedule**: beginning inventory + purchases (units and dollars)
- **Subsequent measurement schedules** (period-end allocation of COGAS):
  - **Specific identification:** value identified ending lots at actual cost; COGS = COGAS − EI (or sum sold-lot costs)
  - **Average cost (periodic weighted average):** WA unit cost = COGAS ÷ units available; apply to EI units and sold units
  - **FIFO (periodic):** EI from most recent purchases; COGS from earliest layers
  - **LIFO (periodic):** EI from earliest layers; COGS from most recent purchases
- **Period-end adjusting JE**: Dr Inventory (ending) + COGS; Cr Purchases + Inventory (beginning) — Dr must equal Cr
- **Settlement of inventory cost**: period-end COGS entry “disposes” of cost of units sold; sales revenue entry settles the customer receivable side
- Rising-price ranking: highest EI / lowest COGS = FIFO; lowest EI / highest COGS = LIFO; average between; specific ID depends on lots remaining
- Classification: Inventory (BS current asset), COGS (IS); method is a cost-flow **assumption** (except specific ID matches physical identity)

---

### Q1 — CORE — Harborlight Marine: full subsequent measurement schedules (all four methods)
**LO:** LO 9-3  
**Concept:** Subsequent measurement schedules allocating COGAS under specific identification, average cost, FIFO, and LIFO (periodic); initial purchase/sale JEs; period-end adjusting JE under average cost  
**Scenario:**  
**Harborlight Marine Supply Co.** uses a **periodic inventory system**. Fiscal month is **April**. Beginning inventory on April 1: **200 units at $10.00** each (**$2,000**). No freight-in, purchase discounts, or returns this month.

| Date | Event |
|---|---|
| Apr 8 | Purchased **300 units at $12.00** on account (**$3,600**). |
| Apr 16 | Purchased **400 units at $14.00** on account (**$5,600**). |
| Apr 25 | Purchased **100 units at $16.00** cash (**$1,600**). |
| Apr (various) | Sold **700 units** on account for total sales revenue of **$21,000**. |
| Apr 30 | Physical inventory count: **300 units** on hand. |

For **specific identification**, management identifies ending inventory as: **50 units from April 1**, **50 units from April 8**, **100 units from April 16**, and **100 units from April 25**.

**Required:**  
a. Prepare **initial recognition** journal entries for the three purchases and the aggregate sale (periodic).  
b. Prepare the **cost of goods available for sale (COGAS)** schedule (units and dollars).  
c. Prepare a **subsequent measurement schedule** computing **ending inventory** and **cost of goods sold** under each of: (1) specific identification, (2) average cost, (3) FIFO, (4) LIFO. Show layer detail for EI and COGS (or sold-layer check).  
d. Prepare the **April 30 period-end adjusting entry** assuming the company uses **average cost**.  
e. Present April 30 **Inventory** (balance sheet) and **Cost of goods sold** (income statement) under average cost, and rank all four methods’ EI from highest to lowest.

**Answer key:**  

**a. Initial recognition and sale (periodic)**

*Apr 8 — Purchase on account*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 3,600 | |
| Accounts Payable | | 3,600 |
| *Invoice cost to temporary Purchases; Inventory permanent account not updated* | | |

**Check:** Dr = Cr = 3,600.

*Apr 16 — Purchase on account*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 5,600 | |
| Accounts Payable | | 5,600 |

**Check:** Dr = Cr = 5,600.

*Apr 25 — Purchase for cash*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 1,600 | |
| Cash | | 1,600 |

**Check:** Dr = Cr = 1,600.

Purchases total = $3,600 + $5,600 + $1,600 = **$10,800**.

*April (aggregate) — Sale (periodic: revenue only; settlement of sales, not COGS)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 21,000 | |
| Sales Revenue | | 21,000 |
| *No COGS or Inventory relief at sale under periodic* | | |

**Check:** Dr = Cr = 21,000.

**b. COGAS schedule**

| Layer | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Apr 1 beginning inventory | 200 | $10.00 | $2,000 |
| Apr 8 purchase | 300 | 12.00 | 3,600 |
| Apr 16 purchase | 400 | 14.00 | 5,600 |
| Apr 25 purchase | 100 | 16.00 | 1,600 |
| **Goods available for sale** | **1,000** | | **$12,800** |

Units sold = 700; EI units = 1,000 − 700 = **300**.  
COGAS check: BI $2,000 + Purchases $10,800 = **$12,800**.

**c. Subsequent measurement schedules — four methods**

**(1) Specific identification — Ending inventory**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| Apr 1 | 50 | $10.00 | $500 |
| Apr 8 | 50 | 12.00 | 600 |
| Apr 16 | 100 | 14.00 | 1,400 |
| Apr 25 | 100 | 16.00 | 1,600 |
| **EI** | **300** | | **$4,100** |

COGS = COGAS − EI = $12,800 − $4,100 = **$8,700**.

*(Sold-layer check)*  
Apr 1: 150 × $10 = $1,500; Apr 8: 250 × $12 = $3,000; Apr 16: 300 × $14 = $4,200; Apr 25: 0.  
Total sold 700; COGS = 1,500 + 3,000 + 4,200 = **$8,700**.

**(2) Average cost (weighted average, periodic)**

\[
\text{WA unit cost} = \frac{\$12{,}800}{1{,}000\ \text{units}} = \$12.80\ \text{per unit}
\]

| | Computation | Amount |
|---|---|---:|
| Ending inventory | 300 × $12.80 | **$3,840** |
| Cost of goods sold | 700 × $12.80 | **$8,960** |

Check: $3,840 + $8,960 = $12,800.

**(3) FIFO — Ending inventory (most recent layers first)**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| Apr 25 | 100 | $16.00 | $1,600 |
| Apr 16 | 200 | 14.00 | 2,800 |
| **EI** | **300** | | **$4,400** |

COGS = $12,800 − $4,400 = **$8,400**.

*(COGS layers — earliest first)*  
Apr 1: 200 × $10 = $2,000; Apr 8: 300 × $12 = $3,600; Apr 16: 200 × $14 = $2,800.  
Total 700; COGS = **$8,400**.

**(4) LIFO — Ending inventory (earliest layers first)**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| Apr 1 | 200 | $10.00 | $2,000 |
| Apr 8 | 100 | 12.00 | 1,200 |
| **EI** | **300** | | **$3,200** |

COGS = $12,800 − $3,200 = **$9,600**.

*(COGS layers — most recent first)*  
Apr 25: 100 × $16 = $1,600; Apr 16: 400 × $14 = $5,600; Apr 8: 200 × $12 = $2,400.  
Total 700; COGS = **$9,600**.

**Summary schedule (subsequent measurement comparison — rising unit costs)**

| Method | Ending inventory | COGS | EI + COGS |
|---|---:|---:|---:|
| Specific identification | $4,100 | $8,700 | $12,800 |
| Average cost | 3,840 | 8,960 | 12,800 |
| FIFO | **4,400** (highest EI) | **8,400** (lowest COGS) | 12,800 |
| LIFO | **3,200** (lowest EI) | **9,600** (highest COGS) | 12,800 |

**d. Apr 30 — Period-end adjusting entry (average cost)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 3,840 | |
| Cost of Goods Sold | 8,960 | |
| Purchases | | 10,800 |
| Inventory (beginning) | | 2,000 |
| *Close Purchases and BI; record EI at WA; residual = COGS (settlement of inventory cost of units sold)* | | |

**Check:** Dr 3,840 + 8,960 = **12,800**; Cr 10,800 + 2,000 = **12,800**. Balanced.  
Also: EI + COGS = BI + Purchases = COGAS.

**e. Presentation (average cost) and ranking**  
- Balance sheet — Inventory (Apr 30): **$3,840**  
- Income statement — Cost of goods sold: **$8,960**  
- EI ranking (highest → lowest): **FIFO $4,400 > specific ID $4,100 > average $3,840 > LIFO $3,200**

**Key insight:** In a **periodic** system, cost-flow methods are applied only **after** the physical count via a **subsequent measurement schedule** that splits one COGAS pool into EI and COGS. FIFO peels newest costs into inventory; LIFO peels newest costs into COGS. The period-end JE simultaneously records EI, closes temporary Purchases and beginning Inventory, and settles COGS — and must balance.

---

### Q2 — CORE number variant — Ridgeway Parts: four-method schedules twin
**LO:** LO 9-3  
**Concept:** Number-variant twin — subsequent measurement schedules for specific identification, average cost, FIFO, and LIFO; initial purchase JEs; period-end adjusting entry under LIFO  
**Scenario:**  
**Ridgeway Parts Distributors LLC** uses a **periodic inventory system**. Fiscal month is **May**. Beginning inventory on May 1: **250 units at $20** each (**$5,000**).

| Date | Event |
|---|---|
| May 5 | Purchased **350 units at $22** on account (**$7,700**). |
| May 18 | Purchased **300 units at $24** on account (**$7,200**). |
| May 28 | Purchased **100 units at $26** cash (**$2,600**). |
| May (various) | Sold **650 units** on account for total sales of **$26,000**. |
| May 31 | Physical count: **350 units** on hand. |

**Specific identification** of ending inventory: **80 units from May 1**, **70 units from May 5**, **100 units from May 18**, and **100 units from May 28**.

**Required:**  
a. Prepare journal entries for the three purchases and the aggregate sale.  
b. Compute COGAS (units and dollars).  
c. Prepare subsequent measurement results: EI and COGS under specific identification, average cost, FIFO, and LIFO (layer detail required).  
d. Prepare the May 31 period-end adjusting entry under **LIFO**.  
e. Compute May **gross profit** under LIFO and under FIFO (sales already given).

**Answer key:**  

**a. Journal entries**

*May 5 — Purchase on account*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 7,700 | |
| Accounts Payable | | 7,700 |

**Check:** Dr = Cr = 7,700.

*May 18 — Purchase on account*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 7,200 | |
| Accounts Payable | | 7,200 |

**Check:** Dr = Cr = 7,200.

*May 28 — Purchase for cash*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 2,600 | |
| Cash | | 2,600 |

**Check:** Dr = Cr = 2,600.

Purchases total = $7,700 + $7,200 + $2,600 = **$17,500**.

*Sale (periodic)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 26,000 | |
| Sales Revenue | | 26,000 |

**Check:** Dr = Cr = 26,000.

**b. COGAS**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| May 1 beginning | 250 | $20 | $5,000 |
| May 5 | 350 | 22 | 7,700 |
| May 18 | 300 | 24 | 7,200 |
| May 28 | 100 | 26 | 2,600 |
| **Available** | **1,000** | | **$22,500** |

EI units = 1,000 − 650 = **350**. COGAS = $5,000 + $17,500 = **$22,500**.  
WA unit cost = $22,500 ÷ 1,000 = **$22.50**.

**c. Four methods — subsequent measurement**

**(1) Specific identification — EI**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| May 1 | 80 | $20 | $1,600 |
| May 5 | 70 | 22 | 1,540 |
| May 18 | 100 | 24 | 2,400 |
| May 28 | 100 | 26 | 2,600 |
| **EI** | **350** | | **$8,140** |

COGS = $22,500 − $8,140 = **$14,360**.

*(Sold-layer check)*  
May 1: 170 × $20 = $3,400; May 5: 280 × $22 = $6,160; May 18: 200 × $24 = $4,800; May 28: 0.  
Total 650; COGS = 3,400 + 6,160 + 4,800 = **$14,360**.

**(2) Average cost**  
EI = 350 × $22.50 = **$7,875**.  
COGS = 650 × $22.50 = **$14,625**.  
Check: $7,875 + $14,625 = $22,500.

**(3) FIFO — EI (most recent)**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| May 28 | 100 | $26 | $2,600 |
| May 18 | 250 | 24 | 6,000 |
| **EI** | **350** | | **$8,600** |

COGS = $22,500 − $8,600 = **$13,900**.  
*(COGS layers)* 250 × $20 + 350 × $22 + 50 × $24 = $5,000 + $7,700 + $1,200 = **$13,900**.

**(4) LIFO — EI (earliest)**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| May 1 | 250 | $20 | $5,000 |
| May 5 | 100 | 22 | 2,200 |
| **EI** | **350** | | **$7,200** |

COGS = $22,500 − $7,200 = **$15,300**.  
*(COGS layers)* 100 × $26 + 300 × $24 + 250 × $22 = $2,600 + $7,200 + $5,500 = **$15,300**.

**Summary**

| Method | EI | COGS |
|---|---:|---:|
| Specific identification | $8,140 | $14,360 |
| Average cost | 7,875 | 14,625 |
| FIFO | 8,600 | 13,900 |
| LIFO | 7,200 | 15,300 |

**d. May 31 — Period-end adjusting entry (LIFO)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 7,200 | |
| Cost of Goods Sold | 15,300 | |
| Purchases | | 17,500 |
| Inventory (beginning) | | 5,000 |
| *LIFO allocation of COGAS; close temporary Purchases and BI; settle inventory cost of units sold* | | |

**Check:** Dr 7,200 + 15,300 = **22,500**; Cr 17,500 + 5,000 = **22,500**. Balanced.

**e. Gross profit under LIFO vs FIFO**

| | LIFO | FIFO |
|---|---:|---:|
| Sales | $26,000 | $26,000 |
| COGS | 15,300 | 13,900 |
| **Gross profit** | **$10,700** | **$12,100** |

Difference = $12,100 − $10,700 = **$1,400** = FIFO EI − LIFO EI ($8,600 − $7,200).

**Key insight:** Same mechanics as Q1 with new quantities and costs. Under rising prices, LIFO’s subsequent measurement schedule assigns newer costs to COGS, reducing gross profit relative to FIFO by exactly the EI gap between the two methods.

---

### Q3 — CORE alternate angle — FIFO vs LIFO schedules, dual period-end JEs, sale settlement
**LO:** LO 9-3  
**Concept:** Subsequent measurement schedules under FIFO and LIFO from identical COGAS; period-end adjusting JEs for both methods; sales settlement vs inventory-cost settlement  
**Scenario:**  
**Northfork Hardware LLC** uses a **periodic inventory system**. For **June**, purchases totaling **$9,000** have already been recorded in the Purchases account. Beginning inventory on June 1 was **$1,600**. No freight-in, discounts, or returns.

Unit data (same pool for both methods):

| Layer | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| June 1 beginning inventory | 200 | $8.00 | $1,600 |
| June 9 purchase | 300 | 10.00 | 3,000 |
| June 21 purchase | 500 | 12.00 | 6,000 |
| **Available** | **1,000** | | **$10,600** |

Physical count on June 30: **250 units** remaining (**750 units** sold).  
Sales revenue for June: **$18,750** (recorded as Dr Accounts Receivable / Cr Sales — no COGS entry yet).

**Required:**  
a. Prepare **subsequent measurement schedules** for ending inventory and COGS under **FIFO** and under **LIFO** (show layers for both EI and COGS). Also compute **average cost** EI and COGS for comparison.  
b. Prepare the **June 30 period-end adjusting entry** under FIFO.  
c. Prepare the **June 30 period-end adjusting entry** under LIFO (as if LIFO were elected instead).  
d. Prepare a **comparison schedule** of Inventory (BS), COGS (IS), and gross profit under FIFO vs LIFO vs average cost.  
e. Explain the two distinct “settlements” in June: (1) the sales revenue entry and (2) the period-end COGS entry. Which one disposes of inventory cost?

**Answer key:**  

**a. Subsequent measurement schedules**

**FIFO — Ending inventory (most recent 250 units)**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| June 21 | 250 | $12.00 | $3,000 |
| **EI** | **250** | | **$3,000** |

COGS = $10,600 − $3,000 = **$7,600**.

*(COGS layers — earliest first)*  

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| June 1 | 200 | $8.00 | $1,600 |
| June 9 | 300 | 10.00 | 3,000 |
| June 21 | 250 | 12.00 | 3,000 |
| **COGS** | **750** | | **$7,600** |

**LIFO — Ending inventory (earliest 250 units)**

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| June 1 | 200 | $8.00 | $1,600 |
| June 9 | 50 | 10.00 | 500 |
| **EI** | **250** | | **$2,100** |

COGS = $10,600 − $2,100 = **$8,500**.

*(COGS layers — most recent first)*  

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| June 21 | 500 | $12.00 | $6,000 |
| June 9 | 250 | 10.00 | 2,500 |
| **COGS** | **750** | | **$8,500** |

**Average cost (comparison)**  
WA = $10,600 ÷ 1,000 = **$10.60** per unit.  
EI = 250 × $10.60 = **$2,650**.  
COGS = 750 × $10.60 = **$7,950**.  
Check: $2,650 + $7,950 = $10,600.

**b. June 30 adjusting entry — FIFO**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 3,000 | |
| Cost of Goods Sold | 7,600 | |
| Purchases | | 9,000 |
| Inventory (beginning) | | 1,600 |

**Check:** Dr 3,000 + 7,600 = **10,600**; Cr 9,000 + 1,600 = **10,600**. Balanced.

**c. June 30 adjusting entry — LIFO**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 2,100 | |
| Cost of Goods Sold | 8,500 | |
| Purchases | | 9,000 |
| Inventory (beginning) | | 1,600 |

**Check:** Dr 2,100 + 8,500 = **10,600**; Cr 9,000 + 1,600 = **10,600**. Balanced.

**d. Comparison schedule**

| | FIFO | Average | LIFO |
|---|---:|---:|---:|
| Inventory (balance sheet) | $3,000 | $2,650 | $2,100 |
| Cost of goods sold | 7,600 | 7,950 | 8,500 |
| Sales | 18,750 | 18,750 | 18,750 |
| **Gross profit** | **$11,150** | **$10,800** | **$10,250** |

Reconciliation FIFO vs LIFO: EI difference $3,000 − $2,100 = **$900** = COGS difference $8,500 − $7,600 = pretax income difference $11,150 − $10,250.

Rising costs ($8 → $12): **FIFO highest EI / lowest COGS / highest GP**; **LIFO lowest EI / highest COGS / lowest GP**; average in between.

**e. Two settlements**  
1. **Sales settlement (already recorded):** Dr Accounts Receivable $18,750 / Cr Sales $18,750 — settles the **customer / revenue** side when goods are delivered. Under periodic, this entry does **not** remove inventory cost.  
2. **Inventory-cost settlement (period-end adjusting entry):** Dr COGS / Cr through the closing of Purchases and BI (with Dr Inventory ending) — this is the entry that **allocates and disposes of the cost of units sold** into expense. Physical “disposal” of goods at sale is not mirrored by a COGS JE until the subsequent measurement schedule is applied after the count.

**Key insight:** FIFO and LIFO use the **same** COGAS and the **same** period-end JE skeleton; only the **subsequent measurement schedule** that splits EI vs COGS changes. That schedule difference is exactly the pretax income difference when sales are fixed.

---

### Q4 — MC — Ranking methods under rising prices (periodic)
**LO:** LO 9-3  
**Concept:** Classification of periodic cost-flow method effects on EI and COGS when acquisition costs are rising  
**Question:**  
A merchandiser uses a **periodic** inventory system. Unit purchase costs **increased steadily** during the year. Ending unit quantity is the same under every method. Which statement is **correct**?

- A) LIFO produces the highest ending inventory and the lowest COGS.  
- B) FIFO produces the highest ending inventory and the lowest COGS.  
- C) Average cost always produces the highest COGS.  
- D) Specific identification always produces EI between FIFO and LIFO.

**Answer:** **B.** Under rising prices, periodic **FIFO** assigns the most recent (highest) costs to ending inventory and the earliest (lowest) costs to COGS, so EI is highest and COGS is lowest. LIFO does the opposite. Average cost falls between FIFO and LIFO. Specific identification depends on which lots remain and need not lie between FIFO and LIFO in every fact pattern.

---

### Q5 — MC — What the subsequent measurement schedule allocates
**LO:** LO 9-3  
**Concept:** Classification of the object of period-end cost-flow allocation in a periodic system  
**Question:**  
Under the **periodic** inventory system, after the physical count, management applies specific identification, average cost, FIFO, or LIFO. What single amount is being **allocated** between ending inventory and cost of goods sold?

- A) Only the most recent purchase invoice  
- B) Net sales revenue for the period  
- C) Cost of goods available for sale (beginning inventory + net purchases)  
- D) Accounts payable related to inventory suppliers

**Answer:** **C.** All four methods allocate **COGAS** (beginning inventory plus purchases, net of related temporary accounts when present) between the asset (ending inventory) and expense (COGS). Sales revenue is not allocated by cost-flow methods; AP is a liability, not the allocation base.

---

### Self-check
- [x] Every JE balances (Dr = Cr on all purchase, sale, and period-end entries)
- [x] Math recomputed (WA clean: $12.80, $22.50, $10.60; layer sums equal COGAS − EI)
- [x] Core demo not sidebar-only (Demo 9-3A–D path: specific ID, average, FIFO, LIFO periodic)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE (sale + COGS cost settlement)
- [x] Original company names/numbers (not textbook Chase / not agent_050 figures)
