# Agent 313 — CORE DEMO — LO 9-4

**Chapter:** 9  
**LO title:** Demonstrate accounting in a perpetual inventory system  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Perpetual inventory system:** Inventory and Cost of Goods Sold are updated **continually** for purchases, returns, discounts affecting inventory cost, freight-in, and sales
- **Initial recognition JE:** capitalize purchases (and freight-in when f.o.b. shipping point) directly to **Inventory** (not Purchases)
- **Gross method (discounts):** record Inventory and AP at **invoice gross**; when discount is taken within terms, **credit Inventory** for the discount
- **Net method (discounts):** record Inventory and AP **net of available discount**; discount lost after the period is **Interest Expense** (finance charge)
- **Subsequent measurement schedule:** continuous inventory rollforward (beg + purchases/freight − discounts taken − returns − COGS − shortage/overage adjustments = ending)
- **Sale under perpetual:** two simultaneous entries — (1) AR/Sales at selling price and (2) COGS/Inventory at cost
- **Period-end adjusting JE (emphasis):** physical count verifies books; shortage → Dr **Loss on Inventory Shortage** / Cr Inventory; overage → reverse; shortage/overage typically absorbed in COGS on the income statement
- **Settlement JEs:** payments on AP (within/after discount period); sales collections are optional for this LO
- **Number-variant twin:** same perpetual path with all different amounts and dates

---

### Q1 — CORE — Perpetual gross method: purchase cycle, sale, inventory schedule, period-end shortage (emphasis)

**LO:** LO 9-4  
**Concept:** Initial recognition of inventory under perpetual gross method; freight-in; discount taken; AP settlement; sale (COGS); subsequent inventory rollforward; **period-end physical-count adjusting JE** (emphasis)  
**Scenario:**  
**Cedarline Outfitters Co.** uses a **perpetual** inventory system and records purchase discounts under the **gross method**. The company begins January with inventory of **$1,850**. Accounting period ends January 31. Physical inventory counts are performed at month-end; any difference between books and physical count is adjusted through **Loss on Inventory Shortage** (or Gain on Inventory Overage).

**Facts (chronological):**  
1. **Jan 4** — Purchased merchandise on account, invoice **$6,000**, terms **2/10, n/30**.  
2. **Jan 4** — Paid freight-in cash **$180** (f.o.b. shipping point; inventory cost).  
3. **Jan 12** — Paid **half** of the Jan 4 accounts payable balance within the discount period.  
4. **Jan 15** — Paid **$2,400** of the remaining accounts payable **after** the discount period.  
5. **Jan 20** — Returned the remaining unpaid merchandise (invoice amount **$600**) to the supplier.  
6. **Jan 25** — Sold merchandise on account for **$4,500**; the cost of goods sold is **$2,700**.  
7. **Jan 31** — Physical count shows inventory is **$125 less** than the perpetual book balance (shortage).

**Required:**  
a. Record all **journal entries** for items 1–7 (include both sale entries on Jan 25).  
b. Prepare a **subsequent measurement schedule** (inventory rollforward) from beginning inventory through the Jan 31 adjustment; state ending Inventory.  
c. Compute **total COGS-related expense** reported for January if inventory shortage is presented with cost of goods sold.  
d. Prove that **Accounts Payable** related to the Jan 4 purchase is zero after the return.

**Answer key:**  

**a. Journal entries (perpetual, gross method)**  

**Jan 4 — Purchase at gross (initial recognition)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 6,000 | |
| Accounts Payable | | 6,000 |
| *Record purchase at invoice gross under gross method* | | |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**

**Jan 4 — Freight-in (f.o.b. shipping point)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 180 | |
| Cash | | 180 |
| *Capitalize transportation-in to Inventory under perpetual* | | |

**Check:** Dr 180 = Cr 180. **Balanced.**

**Jan 12 — Payment within discount period (½ of $6,000 AP = $3,000)**  
Discount = \(3{,}000 \times 0.02 = \$60\); Cash = \(3{,}000 - 60 = \$2{,}940\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 3,000 | |
| Inventory | | 60 |
| Cash | | 2,940 |
| *Gross method: discount taken reduces Inventory cost* | | |

**Check:** Dr 3,000 = Cr \(60 + 2{,}940\). **Balanced.**

**Jan 15 — Payment after discount period**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 2,400 | |
| Cash | | 2,400 |
| *No discount; AP and cash at full remaining portion paid* | | |

**Check:** Dr 2,400 = Cr 2,400. **Balanced.**

**Jan 20 — Purchase return of remaining unpaid inventory**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 600 | |
| Inventory | | 600 |
| *Return reduces Inventory and AP under perpetual* | | |

**Check:** Dr 600 = Cr 600. **Balanced.**

**Jan 25 — Sale (selling price + cost)**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 4,500 | |
| Sales Revenue | | 4,500 |
| *Record sale at retail* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 2,700 | |
| Inventory | | 2,700 |
| *Perpetual: remove cost from Inventory at sale date* | | |

**Check:** Each entry balances (4,500 = 4,500; 2,700 = 2,700).

**Jan 31 — Period-end adjusting JE for inventory shortage (emphasis)**  

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 125 | |
| Inventory | | 125 |
| *Physical count < books; true-up perpetual records to count* | | |

**Check:** Dr 125 = Cr 125. **Balanced.**

**b. Subsequent measurement schedule (Inventory rollforward)**  

| Component | Amount |
|---|---:|
| Beginning inventory, Jan 1 | $1,850 |
| + Purchases (gross) | 6,000 |
| + Freight-in | 180 |
| − Purchase discount taken | (60) |
| − Purchase returns | (600) |
| − Cost of goods sold | (2,700) |
| − Loss on inventory shortage (period-end adj.) | (125) |
| **Ending inventory, Jan 31 (after adjustment)** | **$4,545** |

**Arithmetic check:** \(1{,}850 + 6{,}000 + 180 - 60 - 600 - 2{,}700 - 125 = 4{,}545\). ✓

**c. COGS-related expense for January**  
Recorded COGS \(+\) inventory shortage absorbed in COGS presentation:  
\(2{,}700 + 125 = \mathbf{\$2{,}825}\).  
(Perpetual isolates the shortage in **Loss on Inventory Shortage** while still reporting it with COGS on the income statement.)

**d. AP settlement proof (Jan 4 purchase)**  
\(6{,}000 - 3{,}000 - 2{,}400 - 600 = \mathbf{\$0}\). ✓

**Key insight:** Under a perpetual system, **Inventory** is the control account for cost flows—purchases, freight-in, discounts taken (gross method), returns, and COGS hit Inventory directly. The **period-end adjusting JE** after the physical count is still required: it forces books to the verified quantity and isolates shrinkage (theft, spoilage, error) that would otherwise hide inside a single periodic COGS figure.

---

### Q2 — CORE number variant — Perpetual gross method multi-transaction path (all numbers changed)

**LO:** LO 9-4  
**Concept:** Number-variant twin—perpetual gross method purchase cycle, sale, inventory schedule, period-end shortage adjusting JE  
**Scenario:**  
**Red Mesa Gear LLC** uses a **perpetual** inventory system and the **gross method** for purchase discounts. Beginning inventory on March 1 is **$3,220**. Month-end physical count adjusts books to actual.

**Facts (chronological):**  
1. **Mar 3** — Purchased inventory on account **$9,500**, terms **1/10, n/30**.  
2. **Mar 3** — Paid freight-in cash **$275** (f.o.b. shipping point).  
3. **Mar 11** — Paid **$5,000** of accounts payable within the discount period.  
4. **Mar 18** — Paid **$3,200** of accounts payable after the discount period.  
5. **Mar 22** — Returned remaining unpaid inventory of **$1,300** (invoice amount) to the vendor.  
6. **Mar 27** — Sold inventory on account for **$7,800**; cost **$4,450**.  
7. **Mar 31** — Physical count is **$210 less** than book inventory (shortage).

**Required:**  
a. Record JEs for all seven events (both sale entries on Mar 27).  
b. Inventory rollforward through Mar 31; ending Inventory.  
c. Total COGS-related expense if shortage is included with COGS.  
d. Prove AP from the Mar 3 purchase is zero after the return.

**Answer key:**  

**a. Journal entries**  

**Mar 3 — Purchase (gross)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 9,500 | |
| Accounts Payable | | 9,500 |

**Check:** Dr 9,500 = Cr 9,500. **Balanced.**

**Mar 3 — Freight-in**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 275 | |
| Cash | | 275 |

**Check:** Dr 275 = Cr 275. **Balanced.**

**Mar 11 — Payment within discount period**  
Discount = \(5{,}000 \times 0.01 = \$50\); Cash = \(5{,}000 - 50 = \$4{,}950\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 5,000 | |
| Inventory | | 50 |
| Cash | | 4,950 |

**Check:** Dr 5,000 = Cr \(50 + 4{,}950\). **Balanced.**

**Mar 18 — Payment after discount period**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 3,200 | |
| Cash | | 3,200 |

**Check:** Dr 3,200 = Cr 3,200. **Balanced.**

**Mar 22 — Purchase return**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 1,300 | |
| Inventory | | 1,300 |

**Check:** Dr 1,300 = Cr 1,300. **Balanced.**

**Mar 27 — Sale**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 7,800 | |
| Sales Revenue | | 7,800 |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 4,450 | |
| Inventory | | 4,450 |

**Check:** Both entries balance.

**Mar 31 — Period-end shortage (emphasis)**  

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 210 | |
| Inventory | | 210 |

**Check:** Dr 210 = Cr 210. **Balanced.**

**b. Inventory rollforward**  

| Component | Amount |
|---|---:|
| Beginning inventory, Mar 1 | $3,220 |
| + Purchases | 9,500 |
| + Freight-in | 275 |
| − Discount taken | (50) |
| − Returns | (1,300) |
| − COGS | (4,450) |
| − Shortage (period-end) | (210) |
| **Ending inventory, Mar 31** | **$6,985** |

**Check:** \(3{,}220 + 9{,}500 + 275 - 50 - 1{,}300 - 4{,}450 - 210 = 6{,}985\). ✓

**c. COGS-related expense**  
\(4{,}450 + 210 = \mathbf{\$4{,}660}\).

**d. AP zero-out**  
\(9{,}500 - 5{,}000 - 3{,}200 - 1{,}300 = \mathbf{\$0}\). ✓

**Key insight:** Changing invoice totals, discount percentage (here **1%**), freight, cost of sale, and shortage amount does not change the perpetual architecture: **Inventory is adjusted at every event**, and the **period-end physical-count JE** still trues books to verified units.

---

### Q3 — CORE alternate angle — Perpetual net method; lost discount settlement; period-end overage; inventory schedule

**LO:** LO 9-4  
**Concept:** Perpetual **net method** initial recognition; payment within terms; **settlement after discount period** (Interest Expense); sale; **period-end overage adjusting JE**; subsequent inventory schedule  
**Scenario:**  
**Harbor & Pine Trading Inc.** uses a **perpetual** inventory system and records purchases under the **net method**. Beginning inventory on August 1 is **$4,100**. Terms on the purchase below are **2/10, n/30**.

**Facts (chronological):**  
1. **Aug 2** — Purchased inventory on account, **invoice gross $8,000**. Record at **net** of the 2% discount.  
2. **Aug 10** — Paid **half** of the net accounts payable balance **within** the discount period.  
3. **Aug 20** — Paid the **remaining** accounts payable **after** the discount period (full gross half is remitted; recognize lost discount).  
4. **Aug 24** — Sold merchandise on account for **$5,600**; cost of inventory sold **$3,150**.  
5. **Aug 31** — Physical count shows inventory is **$80 greater** than books (overage / count exceeds perpetual records).

**Required:**  
a. Compute the **net purchase** amount and record JEs for Aug 2, Aug 10, and Aug 20.  
b. Record the Aug 24 sale entries and the **Aug 31 period-end adjusting JE**.  
c. Prepare the Inventory **subsequent measurement schedule** through Aug 31.  
d. Briefly contrast how the Aug 20 payment would differ under the **gross method** (no full re-JE required—state the account difference only).

**Answer key:**  

**a. Net purchase and payment JEs**  
Available discount on full invoice: \(8{,}000 \times 0.02 = \$160\).  
Net purchase: \(8{,}000 - 160 = \mathbf{\$7{,}840}\).

**Aug 2 — Purchase at net (initial recognition)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 7,840 | |
| Accounts Payable | | 7,840 |
| *Net method: Inventory and AP recorded net of available cash discount* | | |

**Check:** Dr 7,840 = Cr 7,840. **Balanced.**

**Aug 10 — Pay half within discount period**  
Half of net AP = \(7{,}840 \times 1/2 = \$3{,}920\).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 3,920 | |
| Cash | | 3,920 |
| *Within terms: cash equals carrying amount of AP (no Inventory adjustment)* | | |

**Check:** Dr 3,920 = Cr 3,920. **Balanced.**

**Aug 20 — Settlement after discount period (lost discount = interest)**  
Remaining net AP = **$3,920**.  
Gross half of original invoice = \(8{,}000 \times 1/2 = \$4{,}000\).  
Lost discount (Interest Expense) = \(4{,}000 - 3{,}920 = \$80\) (or \(4{,}000 \times 0.02 = \$80\)).

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Payable | 3,920 | |
| Interest Expense | 80 | |
| Cash | | 4,000 |
| *Discount not taken is a finance charge, not inventory cost* | | |

**Check:** Dr \(3{,}920 + 80 = 4{,}000\) = Cr 4,000. **Balanced.**

**b. Sale and period-end overage**  

**Aug 24 — Sale**  

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 5,600 | |
| Sales Revenue | | 5,600 |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 3,150 | |
| Inventory | | 3,150 |

**Check:** Both entries balance.

**Aug 31 — Period-end adjusting JE for inventory overage (emphasis)**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 80 | |
| Gain on Inventory Overage | | 80 |
| *Physical count > books; increase Inventory; overage reduces net COGS presentation* | | |

**Check:** Dr 80 = Cr 80. **Balanced.**  
(If the course/entity nets overages against COGS rather than using a gain title, credit **Cost of Goods Sold** $80 instead; amount and Inventory debit are identical.)

**c. Inventory subsequent measurement schedule**  

| Component | Amount |
|---|---:|
| Beginning inventory, Aug 1 | $4,100 |
| + Purchases (net method) | 7,840 |
| − Cost of goods sold | (3,150) |
| + Inventory overage (period-end adj.) | 80 |
| **Ending inventory, Aug 31** | **$8,870** |

**Check:** \(4{,}100 + 7{,}840 - 3{,}150 + 80 = 8{,}870\). ✓  
(No freight, returns, or discounts-taken reductions under this fact set; lost discount went to Interest Expense, not Inventory.)

**d. Gross-method contrast on Aug 20 only**  
Under **gross method**, remaining AP for the unpaid half would still be carried at **$4,000** (gross). Payment after the discount period: Dr Accounts Payable **4,000** / Cr Cash **4,000** — **no Interest Expense**. Under net method, the **$80** finance charge is recognized because Inventory was never recorded at the higher gross cost for that portion.

**Key insight:** The **net method** builds the expected discount into Inventory at purchase. Timely payment simply settles AP; **late payment** does not increase inventory cost—it recognizes **Interest Expense**. Regardless of gross or net, perpetual systems still need a **period-end physical-count adjusting JE** when books and count disagree (shortage or overage).

---

### Q4 — MC — Gross vs net lost-discount treatment under perpetual

**LO:** LO 9-4  
**Concept:** Classification of purchase-discount outcomes under perpetual gross vs net methods  
**Question:**  
Pinebox Retailers uses a perpetual inventory system. It purchased goods with terms 2/10, n/30 and did **not** pay within the discount period. Which statement is **correct**?

- A) Under the **gross method**, Inventory is reduced when the discount is lost.  
- B) Under the **net method**, the discount lost is debited to **Interest Expense** (or a similar finance charge), not to Inventory.  
- C) Under both methods, Cost of Goods Sold is increased immediately when the discount is lost.  
- D) Under the **net method**, Accounts Payable remains at gross invoice until paid.

**Answer:** **B.**  
Under the **net method**, Inventory and AP are recorded **net**; failure to take the discount increases cash paid above AP carrying amount, and the difference is **Interest Expense**—Inventory is not increased. Under the **gross method**, Inventory stays at gross unless a discount is **taken** (credit Inventory when taken); losing the discount simply pays AP at full carrying amount with no Interest Expense. A is wrong (gross method reduces Inventory only when the discount is **taken**, not lost). C is wrong (lost discount is not automatically COGS). D is wrong (net method carries AP at **net**).

---

### Q5 — MC — Period-end physical count under perpetual

**LO:** LO 9-4  
**Concept:** Period-end adjusting JE when perpetual books exceed physical count  
**Question:**  
At year-end, a company’s perpetual Inventory control account shows **$92,400**. A physical count supports inventory of **$91,150**. The appropriate **period-end adjusting entry** is:

- A) Dr Cost of Goods Sold 1,250; Cr Purchases 1,250  
- B) Dr Inventory 1,250; Cr Loss on Inventory Shortage 1,250  
- C) Dr Loss on Inventory Shortage 1,250; Cr Inventory 1,250  
- D) No entry is needed because perpetual records are authoritative over a physical count

**Answer:** **C.**  
Books \(92{,}400 - \) count \(91{,}150 = \$1{,}250\) **shortage**. Debit **Loss on Inventory Shortage** (often closed/presented with COGS) and **credit Inventory** so the balance sheet reports the verified amount. A uses periodic-system accounts incorrectly. B reverses the shortage. D is incorrect—companies using perpetual still count and **adjust** for errors, theft, and spoilage.

---

### Self-check
- [x] Every JE balances (Dr = Cr recomputed on each entry)
- [x] Math recomputed (rollforwards: Q1 EI $4,545; Q2 EI $6,985; Q3 EI $8,870; net purchase $7,840; discounts and lost-discount interest verified)
- [x] Core demo not sidebar-only (Demo 9-4A / 9-4B perpetual gross & net path; physical-count true-up)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 classification/method only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE (AP settlement + sale removal of inventory)
