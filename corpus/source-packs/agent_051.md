# Agent 51 — CORE DEMO — LO 9-4

**Chapter:** 9  
**LO title:** Demonstrate accounting in a perpetual inventory system  
**Critical gap LO:** no

## Concept list for this pack
- Perpetual system: **Inventory** and **COGS** adjusted continually (no temporary Purchases accounts)
- **Initial recognition** under **gross method**: Inventory and AP at invoice gross; freight-in capitalized to Inventory
- Settlement within discount (gross): reduce **Inventory** for cash discount taken
- Settlement after discount; purchase returns reduce Inventory and AP
- Sale under perpetual: **two** entries — revenue and COGS (remove Inventory) at sale date
- **Inventory rollforward schedule** (subsequent measurement of book balance)
- **Period-end adjusting JE**: physical count vs perpetual records → Loss on Inventory Shortage / Gain on Inventory Overage (presented with COGS)
- **Net method**: record Inventory/AP net of discount; lost discount → **Interest Expense** (finance charge)
- Classification/presentation: Inventory (current asset); COGS vs shortage vs Interest Expense

---

### Q1 — CORE — Perpetual gross method: full-month cycle (initial recognition emphasis)
**LO:** LO 9-4  
**Concept:** Initial recognition of purchases/freight under perpetual gross method; AP settlement and returns; sale with simultaneous COGS; period-end shortage adjustment  
**Scenario:**  
**Cedarcrest Outdoor Co.** uses a **perpetual inventory system** and the **gross method** for purchase discounts. Fiscal month is **September**. Beginning inventory on September 1 is **$5,400**.

Chronological transactions:

| Date | Event |
|---|---|
| Sept 4 | Purchased merchandise on account, **$18,000**, terms **2/10, n/30**. |
| Sept 4 | Paid freight of **$540** cash on the Sept 4 purchase (f.o.b. shipping point; buyer pays). |
| Sept 13 | Paid **half** of the Sept 4 invoice within the discount period. |
| Sept 16 | Paid **$6,000** of the remaining accounts payable **after** the discount period. |
| Sept 18 | Returned defective goods and received a credit of **$1,200** from the supplier. |
| Sept 22 | Sold merchandise on account for **$14,000**; cost of goods sold = **$9,200**. |
| Sept 30 | Physical inventory count: perpetual records exceed physical inventory by **$180** (shortage). |

**Required:**  
a. Prepare **all journal entries through September 22** (purchases through sale). Emphasize **initial recognition** under the perpetual gross method (Inventory, not temporary Purchases).  
b. Prepare an **Inventory rollforward schedule** from September 1 book balance through September 22 (before the physical-count adjustment).  
c. Prepare the **September 30 period-end adjusting entry** for the inventory shortage.  
d. State the September 30 balance-sheet amount for **Inventory** and the income-statement amount for **Cost of goods sold** (include shortage as part of reported COGS, consistent with the chapter).

**Answer key:**  

**a. Journal entries through September 22 (perpetual, gross method)**

*Sept 4 — Purchase of inventory (initial recognition, gross)*  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 18,000 | |
| Accounts Payable | | 18,000 |
| *Record purchase at invoice gross amount directly to Inventory* | | |

**Check:** Dr = Cr = 18,000.

*Sept 4 — Freight-in (initial recognition of inventoriable transportation-in)*  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 540 | |
| Cash | | 540 |
| *Buyer pays shipping; f.o.b. shipping point — capitalize to Inventory (not Freight-In temporary account)* | | |

**Check:** Dr = Cr = 540.

*Sept 13 — Payment within discount period (half of $18,000 = $9,000)*  
Purchase discount = $9,000 × 2% = **$180**; cash = $9,000 − $180 = **$8,820**.

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 9,000 | |
| Inventory | | 180 |
| Cash | | 8,820 |
| *Pay half within 2/10; reduce Inventory for discount taken (gross method, perpetual)* | | |

**Check:** Dr 9,000 = Cr 180 + 8,820. Balanced.

*Sept 16 — Payment after discount period*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 6,000 | |
| Cash | | 6,000 |
| *No discount; pay full gross amount of portion settled* | | |

**Check:** Dr = Cr = 6,000.

*Sept 18 — Purchase return*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 1,200 | |
| Inventory | | 1,200 |
| *Return defective goods; reduce Inventory and AP (no Purchase Returns temporary account)* | | |

**Check:** Dr = Cr = 1,200.

*AP rollforward (settlement):*  
18,000 − 9,000 − 6,000 − 1,200 = **$1,800** still payable.

*Sept 22 — Sale of inventory (perpetual: revenue **and** COGS)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 14,000 | |
| Sales Revenue | | 14,000 |
| *Record sale at retail* | | |

**Check:** Dr = Cr = 14,000.

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 9,200 | |
| Inventory | | 9,200 |
| *Remove cost from Inventory and recognize COGS at sale date* | | |

**Check:** Dr = Cr = 9,200.

**b. Inventory rollforward (subsequent measurement — book balance before physical count)**

| Inventory rollforward — September | Amount |
|---|---:|
| Beginning inventory, Sept 1 | $5,400 |
| + Purchases (gross) | 18,000 |
| + Freight-in | 540 |
| − Purchase discount taken | (180) |
| − Purchase returns | (1,200) |
| − Cost of goods sold (at sale) | (9,200) |
| = **Book inventory before physical-count adjustment** | **$13,360** |

Verification: 5,400 + 18,000 + 540 − 180 − 1,200 − 9,200 = **13,360**.

**c. Sept 30 — Period-end inventory shortage adjusting entry**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 180 | |
| Inventory | | 180 |
| *Adjust perpetual records down to physical count* | | |

**Check:** Dr = Cr = 180.

**d. Presentation amounts**  
- Balance sheet — Inventory (Sept 30): $13,360 − $180 = **$13,180**  
- Income statement — Cost of goods sold (incl. shortage): $9,200 + $180 = **$9,380**

**Key insight:** Under the **perpetual gross** method, purchases, freight, discounts taken, and returns all hit **Inventory** (not temporary purchase accounts). COGS is booked **at each sale**. A physical count still occurs; any shortage is adjusted with Loss on Inventory Shortage, which is presented as part of COGS—isolating the shortage amount in the account detail (unlike pure residual COGS under periodic).

---

### Q2 — CORE number variant — Perpetual gross method: full cycle twin
**LO:** LO 9-4  
**Concept:** Number-variant twin of perpetual gross-method purchases, settlements, sale with COGS, rollforward, and period-end shortage  
**Scenario:**  
**Rivermark Supply LLC** uses a **perpetual inventory system** and the **gross method**. Fiscal month is **October**. Beginning inventory on October 1 is **$3,750**.

| Date | Event |
|---|---|
| Oct 2 | Purchased merchandise on account, **$24,000**, terms **3/15, n/45**. |
| Oct 2 | Paid freight of **$720** cash (f.o.b. shipping point). |
| Oct 14 | Paid **60%** of the Oct 2 invoice within the discount period. |
| Oct 20 | Paid **$5,000** of the remaining accounts payable **after** the discount period. |
| Oct 21 | Returned defective goods; credit **$2,000**. |
| Oct 25 | Sold merchandise on account for **$19,500**; cost = **$12,800**. |
| Oct 31 | Physical count: perpetual records exceed physical inventory by **$250** (shortage). |

**Required:**  
a. Prepare all journal entries through October 25.  
b. Inventory rollforward through October 25 (before shortage).  
c. October 31 shortage adjusting entry.  
d. October 31 Inventory (BS) and COGS including shortage (IS).

**Answer key:**  

**a. Journal entries (perpetual, gross)**

*Oct 2 — Purchase (initial recognition, gross)*  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 24,000 | |
| Accounts Payable | | 24,000 |

**Check:** Dr = Cr = 24,000.

*Oct 2 — Freight*  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 720 | |
| Cash | | 720 |

**Check:** Dr = Cr = 720.

*Oct 14 — Payment within discount (60% of $24,000 = $14,400)*  
Discount = $14,400 × 3% = **$432**; cash = $14,400 − $432 = **$13,968**.

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 14,400 | |
| Inventory | | 432 |
| Cash | | 13,968 |

**Check:** Dr 14,400 = Cr 432 + 13,968. Balanced.

*Oct 20 — Payment after discount period*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 5,000 | |
| Cash | | 5,000 |

**Check:** Dr = Cr = 5,000.

*Oct 21 — Purchase return*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 2,000 | |
| Inventory | | 2,000 |

**Check:** Dr = Cr = 2,000.

*AP remaining:* 24,000 − 14,400 − 5,000 − 2,000 = **$2,600**.

*Oct 25 — Sale*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 19,500 | |
| Sales Revenue | | 19,500 |

**Check:** Dr = Cr = 19,500.

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 12,800 | |
| Inventory | | 12,800 |

**Check:** Dr = Cr = 12,800.

**b. Inventory rollforward (before shortage)**

| Inventory rollforward — October | Amount |
|---|---:|
| Beginning inventory, Oct 1 | $3,750 |
| + Purchases (gross) | 24,000 |
| + Freight-in | 720 |
| − Purchase discount taken | (432) |
| − Purchase returns | (2,000) |
| − Cost of goods sold | (12,800) |
| = **Book inventory before physical-count adjustment** | **$13,238** |

Verification: 3,750 + 24,000 + 720 − 432 − 2,000 − 12,800 = **13,238**.

**c. Oct 31 — Shortage**  

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 250 | |
| Inventory | | 250 |

**Check:** Dr = Cr = 250.

**d. Presentation**  
- Inventory (Oct 31): 13,238 − 250 = **$12,988**  
- COGS (incl. shortage): 12,800 + 250 = **$13,050**

**Key insight:** Same perpetual gross logic as Q1 with fully reworked amounts (3% discount, 60% early payment, different freight/return/sale/shortage). Every Inventory/AP/Cash/COGS entry still balances; the rollforward is the continuous subsequent measurement of Inventory.

---

### Q3 — CORE alternate angle — Perpetual net method, lost discount, sale, shortage, classification
**LO:** LO 9-4  
**Concept:** Perpetual net-method initial recognition; settlement within/after discount (Interest Expense for lost discount); sale COGS; period-end shortage; classification of Interest Expense vs COGS  
**Scenario:**  
**Willow Bend Merchandising Inc.** uses a **perpetual inventory system** and the **net method** for purchase discounts. Fiscal month is **November**. Beginning inventory on November 1 is **$2,100**.

| Date | Event |
|---|---|
| Nov 3 | Purchased merchandise on account, invoice **$10,000**, terms **2/10, n/30**. Record **net**. |
| Nov 8 | Returned damaged goods; invoice credit **$500** (gross). Record return at **net**. |
| Nov 12 | Paid the **remaining** accounts payable on the Nov 3 purchase **within** the discount period. |
| Nov 20 | Sold merchandise on account for **$7,200**; cost = **$4,500**. |
| Nov 25 | Purchased merchandise on account, invoice **$6,000**, terms **2/10, n/30**. Record **net**. |
| Nov 30 | Paid the **entire** Nov 25 invoice **after** the discount period. |
| Nov 30 | Physical count: shortage of **$75** relative to perpetual records. |

**Required:**  
a. Prepare journal entries for **all** November transactions (including both purchases and the lost-discount settlement).  
b. Prepare the Inventory rollforward through November 30 **after** the shortage adjustment.  
c. Classify each of the following for financial-statement presentation: (1) Inventory, (2) Cost of goods sold from the sale, (3) Loss on Inventory Shortage, (4) Interest Expense from the lost discount. State the November 30 Inventory balance and total amount presented as COGS (sale + shortage).

**Answer key:**  

**a. Journal entries (perpetual, net method)**

*Nov 3 — Purchase at net (initial recognition)*  
Net = $10,000 × (1 − 0.02) = **$9,800**.

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 9,800 | |
| Accounts Payable | | 9,800 |
| *Record purchase net of anticipated 2% discount* | | |

**Check:** Dr = Cr = 9,800.

*Nov 8 — Return at net*  
Net return = $500 × 0.98 = **$490**.

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 490 | |
| Inventory | | 490 |
| *Reduce Inventory and AP for return at net carrying amount* | | |

**Check:** Dr = Cr = 490.

*AP on Nov 3 purchase after return:* 9,800 − 490 = **$9,310**.

*Nov 12 — Payment within discount period (remaining balance)*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 9,310 | |
| Cash | | 9,310 |
| *Pay net AP; no Inventory adjustment (already at net)* | | |

**Check:** Dr = Cr = 9,310.

*Nov 20 — Sale*  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 7,200 | |
| Sales Revenue | | 7,200 |

**Check:** Dr = Cr = 7,200.

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 4,500 | |
| Inventory | | 4,500 |

**Check:** Dr = Cr = 4,500.

*Nov 25 — Purchase at net*  
Net = $6,000 × 0.98 = **$5,880**.

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 5,880 | |
| Accounts Payable | | 5,880 |

**Check:** Dr = Cr = 5,880.

*Nov 30 — Payment after discount period (lost discount = finance charge)*  
Lost discount = $6,000 × 2% = **$120** (or $6,000 − $5,880).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 5,880 | |
| Interest Expense | 120 | |
| Cash | | 6,000 |
| *Settle AP recorded at net; debit Interest Expense for discount not taken* | | |

**Check:** Dr 5,880 + 120 = Cr 6,000. Balanced.

*Nov 30 — Inventory shortage*  

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 75 | |
| Inventory | | 75 |

**Check:** Dr = Cr = 75.

**b. Inventory rollforward (after shortage)**

| Inventory rollforward — November | Amount |
|---|---:|
| Beginning inventory, Nov 1 | $2,100 |
| + Purchases, net (Nov 3) | 9,800 |
| − Returns, net | (490) |
| + Purchases, net (Nov 25) | 5,880 |
| − Cost of goods sold (sale) | (4,500) |
| − Shortage | (75) |
| = **Ending inventory, Nov 30** | **$12,715** |

Verification: 2,100 + 9,800 − 490 + 5,880 − 4,500 − 75 = **12,715**.

**c. Classification and presentation**

| Item | Classification / presentation |
|---|---|
| (1) Inventory | Current asset on the balance sheet |
| (2) COGS from sale ($4,500) | Cost of goods sold (operating) on the income statement |
| (3) Loss on Inventory Shortage ($75) | Inventory correction; **included as part of COGS** on the income statement |
| (4) Interest Expense ($120) | **Finance charge** (not inventoriable; not COGS)—interest/other expense |

- Balance sheet — Inventory (Nov 30): **$12,715**  
- Income statement — COGS presented (sale + shortage): $4,500 + $75 = **$4,575**  
- Interest Expense (lost discount): **$120** (separate from COGS)

**Key insight:** Under the **perpetual net** method, Inventory and AP are initially recognized **net of discount**. Paying within the discount period simply clears AP at the net amount. Paying **after** the discount period creates **Interest Expense** for the lost discount—a financing cost, not inventory cost. Sales still trigger simultaneous COGS; physical counts still adjust Inventory for shortage/overage.

---

### Q4 — MC — Perpetual gross vs temporary accounts / discount treatment
**LO:** LO 9-4  
**Concept:** Classification of accounts and journal treatment under perpetual inventory (gross method purchase discount)  

**Question:**  
Under a **perpetual inventory system** using the **gross method**, when the buyer pays within the discount period, the cash discount taken is recorded as a:

- A) Credit to Purchase Discounts (temporary contra-purchase account)  
- B) Credit to Inventory  
- C) Debit to Interest Expense  
- D) Debit to Purchase Returns and Allowances  

**Answer:** **B.** Under perpetual gross, purchases are capitalized to **Inventory** at invoice gross; a discount taken reduces the carrying amount of Inventory (credit Inventory). Purchase Discounts as a temporary account is a **periodic** system feature. Interest Expense applies when a discount is **lost** under the **net** method, not when a discount is taken under gross.

---

### Q5 — MC — What is recorded at the moment of sale (perpetual)
**LO:** LO 9-4  
**Concept:** Classification of simultaneous revenue and COGS recognition under perpetual vs periodic  

**Question:**  
At the date inventory is sold to a customer, a company using a **perpetual** inventory system records:

- A) Sales revenue only; COGS is deferred until the physical count and period-end adjusting entry  
- B) COGS only; sales revenue is recorded when cash is collected  
- C) Both sales revenue and cost of goods sold (with a credit to Inventory)  
- D) Neither sales nor COGS until year-end closing  

**Answer:** **C.** Perpetual systems update Inventory and COGS **continually**. The sale entry pair is: Dr Accounts Receivable (or Cash) / Cr Sales, and Dr COGS / Cr Inventory. Under **periodic**, only the revenue side is recorded at sale; COGS waits for the period-end inventory adjusting entry.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (rollforwards, discounts, net amounts, shortage plugs)
- [x] Core demo not sidebar-only (Demo 9-4A / 9-4B / Review 9-4 path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (AP settlement + inventory removal at sale), classification_presentation_or_disclosure, number_variant_twin
