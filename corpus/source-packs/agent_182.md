# Agent 182 — CORE DEMO — LO 9-4

**Chapter:** 9  
**LO title:** Demonstrate accounting in a perpetual inventory system  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Perpetual system:** Inventory and Cost of Goods Sold are adjusted **continually** (no temporary Purchases / Freight-In / Purchase Returns accounts)
- **Initial recognition JE (gross method):** Dr Inventory / Cr Accounts Payable at invoice **gross**; freight-in (f.o.b. shipping point) capitalized to Inventory
- **Subsequent measurement schedule (emphasis):** multi-date **Inventory rollforward** after each purchase, discount, return, sale, and physical-count adjustment
- **Settlement JEs:** payment within discount period reduces **Inventory** for discount taken (gross); payment after discount has no inventory effect; purchase returns reduce Inventory and AP
- **Disposal / sale JEs:** at sale date, **two** entries — Sales revenue **and** COGS (remove Inventory)
- **Period-end adjusting JE:** physical count vs perpetual book balance → Loss on Inventory Shortage (or Gain on Inventory Overage); shortage/overage presented with COGS
- **Net method (alternate):** record Inventory/AP **net** of available discount; discount **not** taken → **Interest Expense** (finance charge), not Inventory
- Classification: Inventory (current asset); Interest Expense (financing) vs COGS/shortage (product cost flow)

---

### Q1 — CORE — Multi-date perpetual inventory subsequent measurement schedule (gross method)
**LO:** LO 9-4  
**Concept:** Subsequent measurement schedule for perpetual Inventory (gross method); initial recognition of purchase/freight; AP settlement and returns; sale with simultaneous COGS; period-end shortage adjusting JE  
**Scenario:**  
**Lakeshore Outfitters Inc.** uses a **perpetual inventory system** and records purchase discounts under the **gross method**. Fiscal month is **June**. Beginning inventory on **June 1** is **$6,200**.

Chronological transactions:

| Date | Event |
|---|---|
| June 3 | Purchased merchandise on account, **$12,500**, terms **2/10, n/30**. |
| June 3 | Paid freight of **$375** cash on the June 3 purchase (f.o.b. shipping point; buyer pays). |
| June 12 | Paid **50%** of the June 3 invoice **within** the discount period. |
| June 14 | Paid **$3,000** of the remaining accounts payable **after** the discount period. |
| June 16 | Returned defective goods; supplier credit **$800**. |
| June 22 | Sold merchandise on account for **$11,400**; cost of the units sold = **$7,500**. |
| June 30 | Physical inventory count: perpetual book inventory exceeds physical inventory by **$220** (shortage). |

**Required:**  
a. Prepare **all journal entries** for June 3 through June 22 (initial recognition, settlements, return, sale).  
b. Prepare the **subsequent measurement schedule** for the Inventory account: after **each** event date through June 22, show the running book balance (columns: Date | Event | Effect on Inventory (+/−) | Inventory balance). Start from the June 1 beginning balance.  
c. Prepare the **June 30 period-end adjusting entry** for the inventory shortage, and extend the subsequent measurement schedule through June 30.  
d. State the **June 30 balance-sheet Inventory** amount and the **income-statement Cost of goods sold** amount (include shortage as part of reported COGS, consistent with the chapter).  
e. Briefly state the **Accounts Payable** balance remaining after June 16 (settlement rollforward).

**Answer key:**

**a. Journal entries (perpetual, gross method)**

*June 3 — Purchase of inventory (initial recognition, gross)*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 12,500 | |
| Accounts Payable | | 12,500 |
| *Record purchase at invoice gross; perpetual system debits Inventory (not Purchases)* | | |

**Check:** Dr 12,500 = Cr 12,500. **Balanced.**

*June 3 — Freight-in (inventoriable transportation-in)*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 375 | |
| Cash | | 375 |
| *f.o.b. shipping point — buyer pays; capitalize freight to Inventory* | | |

**Check:** Dr 375 = Cr 375. **Balanced.**

*June 12 — Payment within discount period (50% of $12,500 = $6,250)*  
Purchase discount = \(6{,}250 \times 0.02 = \mathbf{\$125}\); cash = \(6{,}250 - 125 = \mathbf{\$6{,}125}\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 6,250 | |
| Inventory | | 125 |
| Cash | | 6,125 |
| *Pay half within 2/10; reduce Inventory for cash discount taken (gross method, perpetual)* | | |

**Check:** Dr 6,250 = Cr 125 + 6,125. **Balanced.**

*June 14 — Payment after discount period*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 3,000 | |
| Cash | | 3,000 |
| *No discount; settle portion of AP at gross amount* | | |

**Check:** Dr 3,000 = Cr 3,000. **Balanced.**

*June 16 — Purchase return*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 800 | |
| Inventory | | 800 |
| *Return defective goods; reduce Inventory and AP (no Purchase Returns temporary account)* | | |

**Check:** Dr 800 = Cr 800. **Balanced.**

*June 22 — Sale (perpetual: revenue **and** COGS / disposal of inventory cost)*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 11,400 | |
| Sales Revenue | | 11,400 |
| *Record sale at retail* | | |

**Check:** Dr 11,400 = Cr 11,400. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 7,500 | |
| Inventory | | 7,500 |
| *Remove cost from Inventory and recognize COGS at sale date* | | |

**Check:** Dr 7,500 = Cr 7,500. **Balanced.**

**b–c. Subsequent measurement schedule — Inventory (emphasis)**

| Date | Event | Effect on Inventory | Inventory balance |
|---|---|---:|---:|
| June 1 | Beginning balance | — | $6,200 |
| June 3 | Purchase (gross) | +12,500 | 18,700 |
| June 3 | Freight-in | +375 | 19,075 |
| June 12 | Purchase discount taken | (125) | 18,950 |
| June 14 | AP payment after discount (no Inv effect) | 0 | 18,950 |
| June 16 | Purchase return | (800) | 18,150 |
| June 22 | Cost of goods sold (sale) | (7,500) | **10,650** |
| June 30 | Inventory shortage (period-end adj.) | (220) | **10,430** |

**Schedule checks:**  
\(6{,}200 + 12{,}500 + 375 - 125 - 800 - 7{,}500 = 10{,}650\) (book before physical count).  
\(10{,}650 - 220 = 10{,}430\) (after shortage).

*June 30 — Period-end adjusting JE for shortage*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 220 | |
| Inventory | | 220 |
| *Adjust perpetual records down to physical count* | | |

**Check:** Dr 220 = Cr 220. **Balanced.**

**d. Presentation amounts (June 30)**  
- Balance sheet — **Inventory:** **$10,430**  
- Income statement — **Cost of goods sold** (incl. shortage): \(7{,}500 + 220 = \mathbf{\$7{,}720}\)

**e. Accounts Payable settlement rollforward**  
\(12{,}500 - 6{,}250 - 3{,}000 - 800 = \mathbf{\$2{,}450}\) remaining payable after June 16.

**Key insight:** Under perpetual accounting, the Inventory balance is a **running subsequent measurement** updated for every inventoriable inflow/outflow. The multi-date schedule is the core control tool: discounts taken and returns reduce Inventory (gross method), COGS removes cost at each sale, and a physical count still drives a period-end shortage/overage entry so the books match reality—while isolating the shortage amount in the account detail (presented with COGS).

---

### Q2 — CORE number variant — Multi-date subsequent measurement schedule twin (gross method)
**LO:** LO 9-4  
**Concept:** Number-variant twin: perpetual gross-method initial recognition, multi-date Inventory subsequent measurement schedule, settlements/returns, sale with COGS, period-end shortage  
**Scenario:**  
**Crestview Merchants Co.** uses a **perpetual inventory system** and the **gross method**. Fiscal month is **July**. Beginning inventory on **July 1** is **$4,850**.

| Date | Event |
|---|---|
| July 5 | Purchased merchandise on account, **$20,000**, terms **3/15, n/45**. |
| July 5 | Paid freight of **$600** cash (f.o.b. shipping point). |
| July 18 | Paid **70%** of the July 5 invoice **within** the discount period. |
| July 22 | Paid **$2,500** of the remaining accounts payable **after** the discount period. |
| July 24 | Returned defective goods; credit **$1,500**. |
| July 28 | Sold merchandise on account for **$16,800**; cost = **$10,900**. |
| July 31 | Physical count: perpetual records exceed physical inventory by **$310** (shortage). |

**Required:**  
a. Prepare all journal entries through July 28.  
b. Prepare the **subsequent measurement schedule** for Inventory after each event through July 28 (before shortage).  
c. July 31 shortage adjusting entry; extend the schedule through July 31.  
d. July 31 Inventory (BS) and COGS including shortage (IS).  
e. Remaining Accounts Payable after July 24.

**Answer key:**

**a. Journal entries (perpetual, gross)**

*July 5 — Purchase (initial recognition, gross)*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 20,000 | |
| Accounts Payable | | 20,000 |
| *Purchase at invoice gross* | | |

**Check:** Dr 20,000 = Cr 20,000. **Balanced.**

*July 5 — Freight-in*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 600 | |
| Cash | | 600 |
| *Capitalize inventoriable freight* | | |

**Check:** Dr 600 = Cr 600. **Balanced.**

*July 18 — Payment within discount (70% of $20,000 = $14,000)*  
Discount = \(14{,}000 \times 0.03 = \mathbf{\$420}\); cash = \(14{,}000 - 420 = \mathbf{\$13{,}580}\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 14,000 | |
| Inventory | | 420 |
| Cash | | 13,580 |
| *Pay 70% within 3/15; reduce Inventory for discount taken* | | |

**Check:** Dr 14,000 = Cr 420 + 13,580. **Balanced.**

*July 22 — Payment after discount period*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 2,500 | |
| Cash | | 2,500 |
| *Settle portion of AP at gross* | | |

**Check:** Dr 2,500 = Cr 2,500. **Balanced.**

*July 24 — Purchase return*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 1,500 | |
| Inventory | | 1,500 |
| *Return reduces Inventory and AP* | | |

**Check:** Dr 1,500 = Cr 1,500. **Balanced.**

*July 28 — Sale*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 16,800 | |
| Sales Revenue | | 16,800 |
| *Record sale at retail* | | |

**Check:** Dr 16,800 = Cr 16,800. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 10,900 | |
| Inventory | | 10,900 |
| *COGS and inventory removal at sale date* | | |

**Check:** Dr 10,900 = Cr 10,900. **Balanced.**

**b–c. Subsequent measurement schedule — Inventory**

| Date | Event | Effect on Inventory | Inventory balance |
|---|---|---:|---:|
| July 1 | Beginning balance | — | $4,850 |
| July 5 | Purchase (gross) | +20,000 | 24,850 |
| July 5 | Freight-in | +600 | 25,450 |
| July 18 | Purchase discount taken | (420) | 25,030 |
| July 22 | AP payment after discount | 0 | 25,030 |
| July 24 | Purchase return | (1,500) | 23,530 |
| July 28 | Cost of goods sold | (10,900) | **12,630** |
| July 31 | Inventory shortage | (310) | **12,320** |

**Schedule checks:**  
\(4{,}850 + 20{,}000 + 600 - 420 - 1{,}500 - 10{,}900 = 12{,}630\).  
\(12{,}630 - 310 = 12{,}320\).

*July 31 — Period-end shortage JE*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 310 | |
| Inventory | | 310 |
| *Adjust perpetual records to physical count* | | |

**Check:** Dr 310 = Cr 310. **Balanced.**

**d. Presentation amounts (July 31)**  
- Balance sheet — **Inventory:** **$12,320**  
- Income statement — **COGS** (incl. shortage): \(10{,}900 + 310 = \mathbf{\$11{,}210}\)

**e. Accounts Payable remaining**  
\(20{,}000 - 14{,}000 - 2{,}500 - 1{,}500 = \mathbf{\$2{,}000}\).

**Key insight:** Same perpetual gross-method path as Q1 with every number changed. The subsequent measurement schedule still rolls Inventory after each inventoriable event; AP settlements after the discount window and partial payments do not touch Inventory unless a discount is taken or goods are returned.

---

### Q3 — CORE alternate angle — Perpetual net method: lost discount, sale, period-end overage
**LO:** LO 9-4  
**Concept:** Perpetual **net method** initial recognition; settlement within discount; settlement after discount → Interest Expense (finance charge); sale COGS disposal; period-end inventory **overage** adjusting JE; Inventory subsequent measurement schedule  
**Scenario:**  
**Harborline Trade Co.** uses a **perpetual inventory system** and records purchases under the **net method**. Fiscal month is **August**. Beginning inventory on **August 1** is **$5,100**.

| Date | Event |
|---|---|
| Aug 2 | Purchased merchandise on account, invoice gross **$10,000**, terms **2/10, n/30**. Record at **net**. |
| Aug 2 | Paid freight of **$280** cash (f.o.b. shipping point). |
| Aug 11 | Paid **50%** of the Aug 2 payable **within** the discount period. |
| Aug 20 | Paid the **remaining** Aug 2 payable **after** the discount period. |
| Aug 25 | Sold merchandise on account for **$9,000**; cost = **$5,600**. |
| Aug 31 | Physical count: physical inventory exceeds perpetual book inventory by **$75** (overage). |

**Required:**  
a. Prepare all journal entries for August 2 through August 25 under the **net method**.  
b. Prepare the **subsequent measurement schedule** for Inventory through August 25 (before physical count).  
c. Prepare the **August 31 period-end adjusting entry** for the overage; extend the schedule.  
d. Report August 31 Inventory (BS), COGS (before considering overage presentation), and total **Interest Expense** related to the lost discount.  
e. Contrast in one sentence how a **lost discount** is treated under net vs gross method.

**Answer key:**

**a. Journal entries (perpetual, net method)**

Invoice net = \(10{,}000 \times (1 - 0.02) = \mathbf{\$9{,}800}\).

*Aug 2 — Purchase (initial recognition, net)*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 9,800 | |
| Accounts Payable | | 9,800 |
| *Record purchase net of 2% cash discount available* | | |

**Check:** Dr 9,800 = Cr 9,800. **Balanced.**

*Aug 2 — Freight-in*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 280 | |
| Cash | | 280 |
| *Capitalize inventoriable freight* | | |

**Check:** Dr 280 = Cr 280. **Balanced.**

*Aug 11 — Payment within discount period (50% of net AP = $4,900)*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 4,900 | |
| Cash | | 4,900 |
| *Pay half within discount window; no Inventory adjustment (already net)* | | |

**Check:** Dr 4,900 = Cr 4,900. **Balanced.**

*Aug 20 — Payment after discount period (lost discount on remaining half)*  
Remaining AP (net) = **$4,900**. Gross cash paid for that half of the original invoice = \(5{,}000\).  
Lost discount = finance charge = \(5{,}000 - 4{,}900 = \mathbf{\$100}\) (or \(5{,}000 \times 0.02 = \$100\)).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 4,900 | |
| Interest Expense | 100 | |
| Cash | | 5,000 |
| *Pay remaining after discount period; lost discount → Interest Expense (not Inventory)* | | |

**Check:** Dr 4,900 + 100 = Cr 5,000. **Balanced.**

*Aug 25 — Sale*

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 9,000 | |
| Sales Revenue | | 9,000 |
| *Record sale at retail* | | |

**Check:** Dr 9,000 = Cr 9,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 5,600 | |
| Inventory | | 5,600 |
| *Remove inventory cost; COGS at sale* | | |

**Check:** Dr 5,600 = Cr 5,600. **Balanced.**

**b–c. Subsequent measurement schedule — Inventory**

| Date | Event | Effect on Inventory | Inventory balance |
|---|---|---:|---:|
| Aug 1 | Beginning balance | — | $5,100 |
| Aug 2 | Purchase (net) | +9,800 | 14,900 |
| Aug 2 | Freight-in | +280 | 15,180 |
| Aug 11 | AP payment within discount | 0 | 15,180 |
| Aug 20 | AP payment after discount (Interest Exp only) | 0 | 15,180 |
| Aug 25 | Cost of goods sold | (5,600) | **9,580** |
| Aug 31 | Inventory overage (period-end adj.) | +75 | **9,655** |

**Schedule check:** \(5{,}100 + 9{,}800 + 280 - 5{,}600 = 9{,}580\); \(9{,}580 + 75 = 9{,}655\).

*Aug 31 — Period-end overage adjusting JE*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 75 | |
| Gain on Inventory Overage | | 75 |
| *Adjust perpetual records up to physical count* | | |

**Check:** Dr 75 = Cr 75. **Balanced.**

(Chapter treatment: inventory correction accounts are presented with cost of goods sold; the overage reduces COGS in aggregate presentation.)

**d. Presentation / amounts**  
- Balance sheet — **Inventory:** **$9,655**  
- **COGS** from sales: **$5,600** (before netting overage in the COGS aggregate)  
- **Interest Expense** (lost discount): **$100**  
- If overage is included with COGS presentation: reported product cost flow = \(5{,}600 - 75 = \mathbf{\$5{,}525}\)

**e. Net vs gross — lost discount**  
Under the **net** method a missed discount is **Interest Expense** (financing); under the **gross** method a discount taken reduces **Inventory** when paid within terms, and paying late simply uses full AP with **no** Interest Expense line (Inventory remains at the undiscounted cost of units still on hand).

**Key insight:** Net-method perpetual accounting embeds the expected discount in **initial recognition**. Taking the discount requires no Inventory credit; **missing** it is a period finance charge. The subsequent measurement schedule still rolls Inventory for purchases (net), freight, sales COGS, and physical-count corrections—AP timing after the discount window does not change Inventory.

---

### Q4 — MC (classification / method)
**LO:** LO 9-4  
**Concept:** Classification of accounts and journal treatment under perpetual inventory (gross-method discount; perpetual vs periodic sale recognition)

**Question 1:**  
Under a **perpetual** inventory system using the **gross method**, when a company pays an invoice **within** the cash-discount period, the cash discount is recorded by:

- A) Debiting Purchase Discounts (contra-purchase temporary account)  
- B) Crediting **Inventory** (reducing the inventory carrying amount)  
- C) Crediting Interest Revenue  
- D) Debiting Cost of Goods Sold  

**Answer:** **B.** Under perpetual gross, purchases hit **Inventory** at gross; a discount taken reduces **Inventory** (not a temporary Purchase Discounts account). Options A and D reflect periodic/purchase-account thinking or misclassification; C is not the purchase-discount treatment.

---

**Question 2:**  
Which statement best describes **sale-date** accounting under a **perpetual** inventory system?

- A) Only Sales Revenue is recorded at sale; COGS is computed only in a period-end closing entry from temporary purchase accounts  
- B) Only COGS is recorded at sale; revenue is deferred until cash is collected  
- C) **Both** Sales Revenue **and** Cost of Goods Sold (with a credit to Inventory) are recorded at the time of sale  
- D) Neither revenue nor COGS is recorded until the physical inventory count is completed  

**Answer:** **C.** Perpetual systems record revenue and remove inventory cost (COGS) **at each sale**. A is the periodic approach for COGS timing; B and D are incorrect.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (discounts, rollforwards, AP remaining, BS/IS amounts)
- [x] Core demo not sidebar-only (Demo 9-4A/9-4B path: perpetual gross/net, freight, returns, sale+COGS, physical-count adjustment)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (two classification/method items)
- [x] Emphasis angle covered: multi-date **subsequent measurement schedules** for Inventory in Q1–Q3
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (sale / AP settlement)
- [x] Original company names and numbers (not textbook CostKo demo figures)
