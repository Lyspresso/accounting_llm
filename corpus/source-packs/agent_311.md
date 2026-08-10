# Agent 311 — CORE DEMO — LO 9-2

**Chapter:** 9  
**LO title:** Demonstrate accounting in a periodic inventory system  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Periodic system structure:** temporary purchase accounts (Purchases, Freight-In, Purchase Discounts, Purchase Returns and Allowances) until the physical count
- **Initial recognition JE (gross method):** Dr Purchases / Cr Accounts Payable at invoice gross; Dr Freight-In for transportation-in
- **Settlement of AP:** pay within discount period (record Purchase Discount) vs after (full cash); purchase returns/allowances reduce AP and Purchases, net
- **Sales under periodic:** revenue only at sale — **no COGS entry** until period-end after the count
- **Subsequent measurement schedule:** COGS = Beginning Inventory + Purchases, net − Ending Inventory (from physical count)
- **Period-end adjusting JE (emphasis):** record Ending Inventory, close temporary purchase accounts and Beginning Inventory, residual = Cost of Goods Sold
- **Net method alternate:** record Purchases at net of discount; unused discount → **Interest Expense** (finance charge), including period-end accrual if unpaid after the discount window
- **Classification:** Inventory (asset) on BS; COGS on IS; lost discount is Interest Expense (not inventoriable); temporary purchase accounts are closed at period-end

**Method note (core exam path — Demo 9-2A/9-2B style):** Under the **periodic** system, inventoriable purchase activity hits temporary accounts. Ending inventory and COGS are determined **only after** a physical inventory count. The **period-end adjusting entry** simultaneously (1) establishes Ending Inventory, (2) removes Beginning Inventory, (3) closes temporary purchase accounts, and (4) records COGS as the residual so that **Dr = Cr**.

---

### Q1 — CORE — Periodic gross method: full cycle with period-end inventory adjusting JE (emphasis)

**LO:** LO 9-2  
**Concept:** Initial recognition under gross method; AP settlement and returns; sales without COGS; **period-end adjusting JE** that records EI, closes temps/BI, residual COGS; COGS schedule  
**Scenario:**  
**Northwind Merchants LLC** uses a **periodic inventory system** and the **gross method** for purchase discounts. Fiscal month is **April**. Beginning inventory on **April 1** is **$5,600**.

| Date | Event |
|---|---|
| Apr 2 | Purchased merchandise on account, **$15,000**, terms **2/10, n/30**. |
| Apr 2 | Paid freight of **$520** cash on the Apr 2 purchase (f.o.b. shipping point; buyer pays). |
| Apr 11 | Paid **60%** of the Apr 2 invoice **within** the discount period. |
| Apr 16 | Paid **$3,000** of accounts payable **after** the discount period. |
| Apr 19 | Returned defective goods; received supplier credit of **$1,200** (purchase return). |
| Apr 24 | Sold merchandise on account for **$11,800**. |
| Apr 30 | Physical inventory count: ending inventory cost = **$7,480**. |

**Required:**  
a. Prepare **all journal entries through April 24** (purchases through sale).  
b. Prepare a **cost of goods sold schedule** (subsequent measurement): beginning inventory, purchases net components, COGAS, ending inventory, COGS.  
c. Prepare the **April 30 period-end adjusting JE** (emphasis) that records ending inventory, closes temporary purchase accounts and beginning inventory, and records cost of goods sold.  
d. State the April 30 **balance-sheet Inventory** amount and the April **income-statement COGS** amount. Confirm the period-end entry balances (Dr = Cr).

**Answer key:**  

**a. Journal entries through April 24 (gross method)**

*Apr 2 — Purchase of inventory (initial recognition, gross)*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 15,000 | |
| Accounts Payable | | 15,000 |
| *Record purchase at invoice gross amount* | | |

**Check:** Dr = Cr = 15,000. **Balanced.**

*Apr 2 — Freight-in (inventoriable transportation-in)*  

| Account | Debit | Credit |
|---|---:|---:|
| Freight-In | 520 | |
| Cash | | 520 |
| *Buyer pays shipping; f.o.b. shipping point* | | |

**Check:** Dr = Cr = 520. **Balanced.**

*Apr 11 — Payment within discount period (60% of $15,000 = $9,000)*  
Purchase discount = \(9{,}000 \times 0.02 = \$180\); cash = \(9{,}000 - 180 = \$8{,}820\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 9,000 | |
| Purchase Discount | | 180 |
| Cash | | 8,820 |
| *Pay 60% within 2/10; discount taken on portion paid* | | |

**Check:** Dr 9,000 = Cr 180 + 8,820. **Balanced.**

*Apr 16 — Payment after discount period*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 3,000 | |
| Cash | | 3,000 |
| *No discount; pay full gross amount* | | |

**Check:** Dr = Cr = 3,000. **Balanced.**

*Apr 19 — Purchase return*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 1,200 | |
| Purchase Returns and Allowances | | 1,200 |
| *Return defective goods; contra-purchase* | | |

**Check:** Dr = Cr = 1,200. **Balanced.**

*AP roll-forward (settlement):* \(15{,}000 - 9{,}000 - 3{,}000 - 1{,}200 = \$1{,}800\) still payable.

*Apr 24 — Sale of inventory (revenue only under periodic)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 11,800 | |
| Sales Revenue | | 11,800 |
| *Periodic system: no COGS entry at sale* | | |

**Check:** Dr = Cr = 11,800. **Balanced.**

**b. Subsequent measurement — Cost of goods sold schedule (April)**

| Component | Amount |
|---|---:|
| Beginning inventory | $5,600 |
| Purchases (gross) | 15,000 |
| + Freight-in | 520 |
| − Purchase discounts | (180) |
| − Purchase returns and allowances | (1,200) |
| **Purchases, net** | **14,140** |
| **Cost of goods available for sale** | **19,740** |
| − Ending inventory (physical count) | (7,480) |
| **Cost of goods sold** | **$12,260** |

*Check:* Purchases, net \(= 15{,}000 + 520 - 180 - 1{,}200 = 14{,}140\); COGAS \(= 5{,}600 + 14{,}140 = 19{,}740\); COGS \(= 19{,}740 - 7{,}480 = 12{,}260\). ✓

**c. April 30 — Period-end adjusting JE (emphasis)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (Ending) | 7,480 | |
| Purchase Discount | 180 | |
| Purchase Returns and Allowances | 1,200 | |
| Cost of Goods Sold | 12,260 | |
| Purchases | | 15,000 |
| Freight-In | | 520 |
| Inventory (Beginning) | | 5,600 |
| *Close temps and BI; establish EI from physical count; residual COGS* | | |

**Check:** Dr \(= 7{,}480 + 180 + 1{,}200 + 12{,}260 = 21{,}120\); Cr \(= 15{,}000 + 520 + 5{,}600 = 21{,}120\). **Balanced.**

**d. Presentation**  
- **Balance sheet, Apr 30:** Inventory **$7,480** (physical count; replaces beginning inventory).  
- **Income statement, April:** Cost of goods sold **$12,260**.  
Temporary purchase accounts have zero balances after the period-end entry.

**Key insight:** In a periodic system, COGS is **not** booked at each sale. After the **physical count**, one **period-end adjusting entry** allocates COGAS between **Ending Inventory** (asset) and **COGS** (expense) while closing temporary purchase accounts and beginning inventory — and that compound entry **must balance**.

---

### Q2 — CORE number variant — Periodic gross method: full cycle + period-end adjusting JE

**LO:** LO 9-2  
**Concept:** Number-variant twin—gross-method initial recognition, AP settlement, sale without COGS, COGS schedule, **period-end inventory adjusting JE**  
**Scenario:**  
**Ironclad Distributors Inc.** uses a **periodic inventory system** and the **gross method**. Fiscal month is **August**. Beginning inventory on **August 1** is **$8,400**.

| Date | Event |
|---|---|
| Aug 4 | Purchased merchandise on account, **$22,500**, terms **1/10, n/30**. |
| Aug 4 | Paid freight of **$675** cash (f.o.b. shipping point). |
| Aug 13 | Paid **40%** of the Aug 4 invoice **within** the discount period. |
| Aug 18 | Paid **$6,000** of accounts payable **after** the discount period. |
| Aug 21 | Returned goods; supplier credit **$2,500**. |
| Aug 27 | Sold merchandise on account for **$18,000**. |
| Aug 31 | Physical inventory count: ending inventory cost = **$9,900**. |

**Required:**  
a. Prepare **all journal entries through August 27**.  
b. Prepare the **cost of goods sold schedule** for August.  
c. Prepare the **August 31 period-end adjusting JE** (emphasis).  
d. State August 31 Inventory and August COGS.

**Answer key:**  

**a. Journal entries through August 27 (gross method)**

*Aug 4 — Purchase (gross)*  

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 22,500 | |
| Accounts Payable | | 22,500 |

**Check:** Dr = Cr = 22,500. **Balanced.**

*Aug 4 — Freight-in*  

| Account | Debit | Credit |
|---|---:|---:|
| Freight-In | 675 | |
| Cash | | 675 |

**Check:** Dr = Cr = 675. **Balanced.**

*Aug 13 — Pay 40% within discount*  
Gross portion paid \(= 22{,}500 \times 0.40 = \$9{,}000\); discount \(= 9{,}000 \times 0.01 = \$90\); cash \(= \$8{,}910\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 9,000 | |
| Purchase Discount | | 90 |
| Cash | | 8,910 |

**Check:** Dr 9,000 = Cr 90 + 8,910. **Balanced.**

*Aug 18 — Pay after discount period*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 6,000 | |
| Cash | | 6,000 |

**Check:** Dr = Cr = 6,000. **Balanced.**

*Aug 21 — Purchase return*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 2,500 | |
| Purchase Returns and Allowances | | 2,500 |

**Check:** Dr = Cr = 2,500. **Balanced.**

*AP remaining:* \(22{,}500 - 9{,}000 - 6{,}000 - 2{,}500 = \$5{,}000\).

*Aug 27 — Sale (revenue only)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 18,000 | |
| Sales Revenue | | 18,000 |

**Check:** Dr = Cr = 18,000. **Balanced.**

**b. Cost of goods sold schedule (August)**

| Component | Amount |
|---|---:|
| Beginning inventory | $8,400 |
| Purchases (gross) | 22,500 |
| + Freight-in | 675 |
| − Purchase discounts | (90) |
| − Purchase returns and allowances | (2,500) |
| **Purchases, net** | **20,585** |
| **Cost of goods available for sale** | **28,985** |
| − Ending inventory | (9,900) |
| **Cost of goods sold** | **$19,085** |

*Check:* \(22{,}500 + 675 - 90 - 2{,}500 = 20{,}585\); \(8{,}400 + 20{,}585 = 28{,}985\); \(28{,}985 - 9{,}900 = 19{,}085\). ✓

**c. August 31 — Period-end adjusting JE (emphasis)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (Ending) | 9,900 | |
| Purchase Discount | 90 | |
| Purchase Returns and Allowances | 2,500 | |
| Cost of Goods Sold | 19,085 | |
| Purchases | | 22,500 |
| Freight-In | | 675 |
| Inventory (Beginning) | | 8,400 |
| *Period-end: EI from count; close temps and BI; residual COGS* | | |

**Check:** Dr \(= 9{,}900 + 90 + 2{,}500 + 19{,}085 = 31{,}575\); Cr \(= 22{,}500 + 675 + 8{,}400 = 31{,}575\). **Balanced.**

**d. Presentation**  
- **Inventory (BS), Aug 31:** **$9,900**  
- **COGS (IS), August:** **$19,085**

**Key insight:** Changing every dollar amount does not change the mechanics: temporary accounts accumulate purchases; **only the period-end adjusting entry** establishes EI and residual COGS so the books balance.

---

### Q3 — CORE alternate angle — Periodic net method: purchases, lost discount, period-end adjusting JE

**LO:** LO 9-2  
**Concept:** Net-method initial recognition; return and settlement at net; lost discount as Interest Expense; sale without COGS; **period-end inventory adjusting JE** and COGS schedule  
**Scenario:**  
**Blue Spruce Trading Co.** uses a **periodic inventory system** and the **net method** for purchase discounts. Fiscal month is **May**. Beginning inventory on **May 1** is **$6,200**.

| Date | Event |
|---|---|
| May 3 | Purchased merchandise on account, invoice **$12,000**, terms **2/10, n/30**. Record at **net**. |
| May 3 | Paid freight **$400** cash (f.o.b. shipping point). |
| May 8 | Returned goods with invoice (gross) cost **$500**; credit recorded at **net**. |
| May 12 | Paid **half of the remaining** accounts payable **within** the discount period. |
| May 25 | Paid the **remaining** accounts payable **after** the discount period (record lost discount). |
| May 28 | Sold merchandise on account for **$9,000**. |
| May 31 | Physical inventory count: ending inventory cost = **$8,100**. |

**Required:**  
a. Prepare **all journal entries through May 28** under the **net method**.  
b. Prepare the **cost of goods sold schedule** for May.  
c. Prepare the **May 31 period-end adjusting JE** (emphasis).  
d. Classify the **lost discount** amount (which financial statement line / nature of cost). State May 31 Inventory and May COGS.

**Answer key:**  

**a. Journal entries through May 28 (net method)**

*May 3 — Purchase at net*  
Net invoice \(= 12{,}000 \times 0.98 = \$11{,}760\).

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 11,760 | |
| Accounts Payable | | 11,760 |
| *Record purchase net of 2% cash discount* | | |

**Check:** Dr = Cr = 11,760. **Balanced.**

*May 3 — Freight-in*  

| Account | Debit | Credit |
|---|---:|---:|
| Freight-In | 400 | |
| Cash | | 400 |

**Check:** Dr = Cr = 400. **Balanced.**

*May 8 — Purchase return at net*  
Net return \(= 500 \times 0.98 = \$490\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 490 | |
| Purchase Returns and Allowances | | 490 |
| *Return at net carrying amount of AP* | | |

**Check:** Dr = Cr = 490. **Balanced.**

*AP after return:* \(11{,}760 - 490 = \$11{,}270\).  
*Gross remaining after return:* \(12{,}000 - 500 = \$11{,}500\).

*May 12 — Pay half of remaining within discount period*  
Half of remaining **net** AP \(= 11{,}270 / 2 = \$5{,}635\); cash \(= \$5{,}635\) (already net — no separate Purchase Discount).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 5,635 | |
| Cash | | 5,635 |
| *Pay half of remaining AP within discount window at net* | | |

**Check:** Dr = Cr = 5,635. **Balanced.**

*May 25 — Pay remaining after discount period (lost discount = interest)*  
Remaining net AP \(= \$5{,}635\); corresponding gross \(= 11{,}500 / 2 = \$5{,}750\); lost discount \(= 5{,}750 \times 0.02 = \$115\) (or \(5{,}750 - 5{,}635 = 115\)).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 5,635 | |
| Interest Expense | 115 | |
| Cash | | 5,750 |
| *Pay after discount window; lost discount is finance charge* | | |

**Check:** Dr 5,635 + 115 = 5,750 = Cr. **Balanced.**

*May 28 — Sale (revenue only)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 9,000 | |
| Sales Revenue | | 9,000 |

**Check:** Dr = Cr = 9,000. **Balanced.**

**b. Cost of goods sold schedule (May)**  
(Note: Purchases already at net; lost discount is **not** part of Purchases, net.)

| Component | Amount |
|---|---:|
| Beginning inventory | $6,200 |
| Purchases (recorded at net) | 11,760 |
| + Freight-in | 400 |
| − Purchase returns and allowances (at net) | (490) |
| **Purchases, net** | **11,670** |
| **Cost of goods available for sale** | **17,870** |
| − Ending inventory | (8,100) |
| **Cost of goods sold** | **$9,770** |

*Check:* \(11{,}760 + 400 - 490 = 11{,}670\); \(6{,}200 + 11{,}670 = 17{,}870\); \(17{,}870 - 8{,}100 = 9{,}770\). ✓

**c. May 31 — Period-end adjusting JE (emphasis)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (Ending) | 8,100 | |
| Purchase Returns and Allowances | 490 | |
| Cost of Goods Sold | 9,770 | |
| Purchases | | 11,760 |
| Freight-In | | 400 |
| Inventory (Beginning) | | 6,200 |
| *Close temps and BI; establish EI; residual COGS (no Purchase Discount account under net when all discounts either embedded or lost)* | | |

**Check:** Dr \(= 8{,}100 + 490 + 9{,}770 = 18{,}360\); Cr \(= 11{,}760 + 400 + 6{,}200 = 18{,}360\). **Balanced.**

**d. Classification / presentation**  
- **Lost discount $115:** **Interest Expense** (financing cost) on the **income statement** — **not** inventoriable, **not** COGS, **not** a purchase discount contra under the net method when the discount is forfeited.  
- **Inventory (BS), May 31:** **$8,100**  
- **COGS (IS), May:** **$9,770** (separate from the $115 Interest Expense)

**Key insight:** Under the **net method**, purchases start at the discounted amount. Taking the discount needs no extra discount account; **missing** the discount is **Interest Expense**. The **period-end inventory adjusting entry** still allocates COGAS between EI and COGS using temporary purchase accounts — same structure as gross method, different temporary-account mix.

---

### Q4 — MC — Timing of COGS and nature of period-end entry (periodic)

**LO:** LO 9-2  
**Concept:** Classification of when COGS is recognized and what the period-end inventory entry accomplishes in a periodic system  
**Question:**  
**Trailhead Provisions Co.** uses a **periodic inventory system**. During March it purchased inventory, paid freight-in, took some purchase discounts, returned defective goods, and made several sales. Which statement is **correct**?

- A) Cost of goods sold is debited at each sale date for the estimated cost of units sold, and the period-end physical count is used only to verify perpetual inventory records.  
- B) Cost of goods sold is not recorded until **period-end**, when a single adjusting entry establishes ending inventory from the physical count, closes temporary purchase accounts and beginning inventory, and records COGS as the residual so that total debits equal total credits.  
- C) Freight-in is expensed immediately as a period cost and is excluded from purchases, net and from the period-end inventory adjusting entry.  
- D) Under the periodic system, Purchase Discounts taken increase Inventory at period-end rather than reducing purchases, net in the COGS calculation.

**Answer:** **B.**  
In a **periodic** system, temporary purchase accounts accumulate inventoriable costs; sales entries record **revenue only**. After the **physical inventory count**, the **period-end adjusting entry** (1) records Ending Inventory, (2) closes Beginning Inventory and temporary purchase accounts, and (3) plugs **Cost of Goods Sold** so the entry **balances**. A describes a **perpetual** system. Freight-in is inventoriable (part of purchases, net). Purchase discounts **reduce** purchases, net (and are closed in the period-end entry under the gross method).

---

### Q4b — MC — Gross vs net method classification of unused discount (optional second MC)

**LO:** LO 9-2  
**Concept:** Classification of unused purchase discount under gross vs net method in a periodic system  
**Question:**  
A company using a **periodic inventory system** fails to pay within the cash discount period. How is the **unused discount** reported under the **gross method** versus the **net method**?

- A) Gross method: Interest Expense when the invoice is paid late; Net method: reduce Purchases when the invoice is paid late.  
- B) Gross method: no separate discount or interest account at payment (cash equals remaining gross AP); Net method: **Interest Expense** (or Purchase Discount Lost) for the forfeited discount.  
- C) Both methods debit Purchase Discount Lost for the unused discount and include it in inventory cost.  
- D) Both methods reclassify the unused discount into Freight-In at period-end.

**Answer:** **B.**  
Under the **gross method**, AP is already at full invoice; paying after the discount period simply Dr AP / Cr Cash for the full amount (discount never recorded). Under the **net method**, AP is at the net amount, so paying the higher cash amount requires Dr **Interest Expense** for the lost discount — a **financing** cost, not inventoriable inventory cost.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (COGS schedules roll: BI + Purchases, net − EI)
- [x] Core demo not sidebar-only (Demo 9-2A/9-2B path; not annualized cost-of-lost-discount sidebar as primary)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (two classification/method items)
- [x] Emphasis on **period_end_adjusting_JE** in Q1–Q3
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (COGS), period_end_adjusting_JE, settlement of AP / closing of temps
- [x] Original company names and numbers (not textbook CostKo demo figures)
