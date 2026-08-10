# Agent 191 — CORE DEMO — LO 10-4

**Chapter:** 10  
**LO title:** Demonstrate the gross profit method to estimate inventory  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- Gross profit method two-step process: (1) express gross profit as a **percentage of sales**; (2) estimate COGS, then ending inventory
- Convert **markup on cost** to markup on sales: GP%_sales = markup_on_cost ÷ (1 + markup_on_cost); cost % of sales = 1 − GP%_sales
- **Subsequent measurement schedule (emphasis):** multi-period rollforward of estimated ending inventory (each period’s EI becomes next period’s BI)
- Estimation identity: Beginning inventory + Net purchases = GAS − Estimated COGS = Estimated ending inventory
- **Period-end adjusting JE** under periodic inventory for interim reporting (set estimated EI and COGS; close BI and Purchases)
- Casualty application: estimate inventory at loss date from the rollforward, subtract salvage → inventory loss
- **Initial recognition JE** for casualty write-off (salvage + loss = estimated inventory removed)
- Insurance **settlement JE** when cash is received (after receivable recognition when recovery is probable)
- Multi-class application when markups differ: separate GP schedules, then sum (limitation of blended rates)

---

### Q1 — CORE — Multi-period subsequent measurement schedule, interim adjusting JEs, fire loss & insurance settlement
**LO:** LO 10-4  
**Concept:** Subsequent measurement schedule of estimated inventory under the gross profit method; markup-on-cost conversion; period-end interim adjusting JEs; initial recognition of casualty loss; insurance settlement  
**Scenario:**  
**Crestwood Appliances Inc.** uses a **periodic** inventory system and a **December 31** year-end. Management estimates inventory for **each quarter** using the gross profit method because a full physical count is taken only at year-end. Past experience shows a consistent **markup of 25% of cost**.

| Item | Amount |
|---|---:|
| Inventory, January 1 (physical count) | $225,000 |

Quarterly activity (net purchases and net sales):

| Period | Net purchases | Net sales |
|---|---:|---:|
| Q1 (Jan 1 – Mar 31) | $280,000 | $350,000 |
| Q2 (Apr 1 – Jun 30) | 310,000 | 400,000 |
| Q3 (Jul 1 – Sep 30) | 265,000 | 320,000 |

**October 8, Year 1:** A fire destroys the warehouse inventory. Records for **October 1–8** show net purchases of **$55,000** and net sales of **$75,000**. Undamaged goods salvaged and still salable are valued at **cost of $28,000**. Expected insurance recovery of the book inventory loss is **probable** and reasonably estimable at **$175,000**. On **November 20**, the insurer pays **$175,000** cash in full settlement (equal to the receivable previously recognized).

Assume each interim quarter’s estimated ending inventory is booked via a period-end adjusting entry and becomes the beginning inventory carrying amount for the next period’s estimate. Purchases for each period are recorded in **Purchases** (periodic). Ignore income taxes.

**Required:**  
(a) Convert the markup on cost to **gross profit as a percentage of sales** and state the **cost percentage of sales**.  
(b) Prepare a **subsequent measurement schedule** (emphasis) rolling forward **estimated ending inventory** for Mar 31, Jun 30, and Sep 30 (show GAS, estimated COGS, and estimated EI for each quarter).  
(c) Prepare the **period-end adjusting journal entries** for **March 31** and **June 30** that recognize estimated COGS and set ending inventory (debit ending Inventory and COGS; credit beginning Inventory and Purchases for that period).  
(d) Using the Sep 30 estimated inventory as beginning inventory for October, prepare the **gross profit method schedule** estimating inventory on hand at the **October 8 fire date** (before salvage), and compute the **inventory loss**.  
(e) Prepare the **October 8 initial recognition journal entry** to reclassify salvage inventory, write off destroyed inventory, and record the casualty loss (**before** insurance).  
(f) Prepare the **October 8 journal entry** to recognize the **insurance receivable** for the expected recovery.  
(g) Prepare the **November 20 settlement journal entry** when cash is received.  
(h) Report inventory on the balance sheet immediately after the October 8 write-off (before insurance cash is received).

**Answer key:**

**(a) Markup conversion**  
\[
\text{GP\% of sales} = \frac{0.25}{1 + 0.25} = \frac{0.25}{1.25} = \mathbf{0.20\ (20\%)}
\]  
Cost percentage of sales = \(1 - 0.20 = \mathbf{80\%}\).

**(b) Subsequent measurement schedule — estimated inventory rollforward (emphasis)**

| Date / period | Beginning inv. | + Net purchases | = GAS | − Est. COGS (sales × 80%) | = Est. ending inv. |
|---|---:|---:|---:|---:|---:|
| Q1 → Mar 31 | $225,000 | $280,000 | $505,000 | \(350{,}000 \times 0.80 = \$280{,}000\) | **$225,000** |
| Q2 → Jun 30 | 225,000 | 310,000 | 535,000 | \(400{,}000 \times 0.80 = 320{,}000\) | **215,000** |
| Q3 → Sep 30 | 215,000 | 265,000 | 480,000 | \(320{,}000 \times 0.80 = 256{,}000\) | **224,000** |

**Schedule math checks:**  
- Q1: \(505{,}000 - 280{,}000 = 225{,}000\).  
- Q2: \(535{,}000 - 320{,}000 = 215{,}000\).  
- Q3: \(480{,}000 - 256{,}000 = 224{,}000\).  
Each period’s estimated EI is the next period’s BI (subsequent measurement under the GP method).

**(c) Period-end adjusting JEs**

**March 31 — interim adjusting entry**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending, estimated) | 225,000 | |
| Cost of Goods Sold | 280,000 | |
| Inventory (beginning) | | 225,000 |
| Purchases | | 280,000 |
| *Book Q1 estimated EI and COGS under GP method* | | |

**Check:** Dr \(225{,}000 + 280{,}000 = 505{,}000\); Cr \(225{,}000 + 280{,}000 = 505{,}000\). **Balanced.**

**June 30 — interim adjusting entry**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending, estimated) | 215,000 | |
| Cost of Goods Sold | 320,000 | |
| Inventory (beginning) | | 225,000 |
| Purchases | | 310,000 |
| *Book Q2 estimated EI and COGS; BI is Q1 estimated EI* | | |

**Check:** Dr \(215{,}000 + 320{,}000 = 535{,}000\); Cr \(225{,}000 + 310{,}000 = 535{,}000\). **Balanced.**

**(d) Inventory at fire date and loss**

| Component | Amount |
|---|---:|
| Beginning inventory, Oct 1 (Sep 30 estimated) | $224,000 |
| Add: Net purchases, Oct 1–8 | 55,000 |
| **Cost of goods available for sale** | **279,000** |
| Subtract: Cost of goods sold, estimated \($75{,}000 \times 0.80\) | (60,000) |
| **Ending inventory, estimated (at fire date)** | **$219,000** |

\[
\text{Inventory loss} = \$219{,}000 - \$28{,}000\ \text{salvage} = \mathbf{\$191{,}000}
\]

**(e) October 8 — initial recognition of casualty (before insurance)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory—Salvage | 28,000 | |
| Loss from Fire | 191,000 | |
| Inventory | | 219,000 |
| *Reclass salvage; write off destroyed inventory at estimated cost* | | |

**Check:** Dr \(28{,}000 + 191{,}000 = 219{,}000\) = Cr \(219{,}000\). **Balanced.**

**(f) October 8 — recognize probable insurance recovery**

| Account | Debit | Credit |
|---|---:|---:|
| Insurance Receivable | 175,000 | |
| Loss from Fire | | 175,000 |
| *Expected recovery reduces net casualty loss* | | |

**Check:** Dr = Cr = 175,000. **Balanced.**  
**Net casualty loss** after expected recovery = \(191{,}000 - 175{,}000 = \mathbf{\$16{,}000}\).

**(g) November 20 — insurance settlement**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 175,000 | |
| Insurance Receivable | | 175,000 |
| *Cash settlement equals receivable; no additional gain/loss* | | |

**Check:** Dr = Cr = 175,000. **Balanced.**

**(h) Balance sheet — inventory after October 8 write-off**

| | |
|---|---:|
| Inventory—Salvage (undamaged goods at cost) | $28,000 |
| **Total inventory reported** | **$28,000** |

(Insurance receivable of $175,000 is a **receivable**, not inventory.)

**Key insight:** Under interim use of the gross profit method, estimated inventory is **remeasured each period** and rolled forward—the subsequent measurement schedule is the core control. A mid-period casualty continues that same schedule to the loss date; salvage reduces the loss, and insurance recovery is layered separately from the inventory write-off.

---

### Q2 — CORE number variant — Redfern Outdoor twin (same structure, all numbers changed)
**LO:** LO 10-4  
**Concept:** Number-variant twin — subsequent measurement schedule of estimated inventory; markup conversion; interim adjusting JEs; casualty write-off and insurance settlement  
**Scenario:**  
**Redfern Outdoor Co.** uses a periodic inventory system. Historical **markup is 30% of cost**. Inventory at **January 1** (physical) is **$150,000**. Quarterly data:

| Period | Net purchases | Net sales |
|---|---:|---:|
| Q1 | $260,000 | $390,000 |
| Q2 | 290,000 | 325,000 |
| Q3 | 220,000 | 286,000 |

**November 5:** A flood destroys warehouse inventory. Activity **November 1–5**: net purchases **$40,000**, net sales **$78,000**. Salvage undamaged goods at **cost $22,000**. Insurance recovery is **probable** at **$100,000**. On **December 1**, the insurer pays **$100,000** cash in full settlement.

**Required:**  
(a) Convert markup on cost to GP% of sales and state the cost percentage of sales.  
(b) Prepare the **subsequent measurement schedule** of estimated EI for Mar 31, Jun 30, and Sep 30.  
(c) Prepare the **June 30 period-end adjusting journal entry** only (BI = Mar 31 estimated EI).  
(d) Estimate inventory at the flood date and the inventory loss after salvage.  
(e) Journal entry November 5 for salvage, write-off, and loss (before insurance).  
(f) Journal entry November 5 for the insurance receivable.  
(g) Journal entry December 1 for cash settlement.  
(h) Net casualty loss after expected insurance recovery.

**Answer key:**

**(a)**  
\[
\text{GP\% of sales} = \frac{0.30}{1.30} = \frac{3}{13} \approx \mathbf{23.0769\%}
\]  
Cost % of sales = \(1 - 3/13 = 10/13 \approx \mathbf{76.9231\%}\) (use exact fractions \(3/13\) and \(10/13\)).

**(b) Subsequent measurement schedule**

| Date / period | BI | + Purchases | = GAS | − Est. COGS (sales × 10/13) | = Est. EI |
|---|---:|---:|---:|---:|---:|
| Q1 → Mar 31 | $150,000 | $260,000 | $410,000 | \(390{,}000 \times 10/13 = \$300{,}000\) | **$110,000** |
| Q2 → Jun 30 | 110,000 | 290,000 | 400,000 | \(325{,}000 \times 10/13 = 250{,}000\) | **150,000** |
| Q3 → Sep 30 | 150,000 | 220,000 | 370,000 | \(286{,}000 \times 10/13 = 220{,}000\) | **150,000** |

**Checks:** \(410{,}000 - 300{,}000 = 110{,}000\); \(400{,}000 - 250{,}000 = 150{,}000\); \(370{,}000 - 220{,}000 = 150{,}000\).

**(c) June 30 — period-end adjusting entry**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending, estimated) | 150,000 | |
| Cost of Goods Sold | 250,000 | |
| Inventory (beginning) | | 110,000 |
| Purchases | | 290,000 |
| *Book Q2 estimated EI and COGS* | | |

**Check:** Dr \(150{,}000 + 250{,}000 = 400{,}000\); Cr \(110{,}000 + 290{,}000 = 400{,}000\). **Balanced.**

**(d) Flood-date estimate and loss**

| Component | Amount |
|---|---:|
| Beginning inventory, Nov 1 (Sep 30 estimated) | $150,000 |
| Add: Net purchases, Nov 1–5 | 40,000 |
| **GAS** | **190,000** |
| Subtract: Est. COGS \($78{,}000 \times 10/13\) | (60,000) |
| **EI estimated at flood date** | **$130,000** |

Loss = \(130{,}000 - 22{,}000 = \mathbf{\$108{,}000}\).

**(e) November 5 — casualty write-off**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory—Salvage | 22,000 | |
| Loss from Flood | 108,000 | |
| Inventory | | 130,000 |

**Check:** Dr \(22{,}000 + 108{,}000 = 130{,}000\) = Cr. **Balanced.**

**(f) November 5 — insurance receivable**

| Account | Debit | Credit |
|---|---:|---:|
| Insurance Receivable | 100,000 | |
| Loss from Flood | | 100,000 |

**Check:** Dr = Cr = 100,000. **Balanced.**

**(g) December 1 — settlement**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 100,000 | |
| Insurance Receivable | | 100,000 |

**Check:** Dr = Cr = 100,000. **Balanced.**

**(h)** Net casualty loss = \(108{,}000 - 100{,}000 = \mathbf{\$8{,}000}\).

**Key insight:** Same subsequent-measurement architecture as Q1 with every amount and the markup rate changed (30% of cost → \(3/13\) of sales). The rollforward still drives interim EI, casualty estimation, and balanced write-off/settlement entries.

---

### Q3 — CORE alternate angle — Multi-class subsequent measurement schedules vs blended rate; period-end adjusting JE; theft/shrinkage test
**LO:** LO 10-4  
**Concept:** Subsequent measurement schedules applied **separately by inventory class** when markups differ; compare to blended-rate estimate; period-end adjusting JE; estimated missing inventory vs physical count  
**Scenario:**  
**Glenbrook Garden Centers** sells two product lines with **different markups on cost**. For the quarter ended **March 31**, management estimates ending inventory with the gross profit method. Freight-in is included in net purchases below.

| | Patio furniture | Garden tools | Total |
|---|---:|---:|---:|
| Inventory, January 1 | $95,000 | $55,000 | $150,000 |
| Net purchases (incl. freight) | 220,000 | 145,000 | 365,000 |
| Net sales | 336,000 | 184,000 | 520,000 |

**Markups:** Patio furniture **40% of cost**; garden tools **25% of cost**.  
A manager proposes instead using a single blended markup of **30% of cost** on **combined** totals.  
A **physical count** on March 31 (after the separate-class estimate is prepared) shows inventory on hand of **$120,000** at cost. The Inventory control account still shows only the January 1 total of **$150,000**; quarter purchases sit in **Purchases**.

**Required:**  
(a) Convert each class markup on cost (and the blended 30% markup) to GP% of sales and cost % of sales.  
(b) Prepare **separate subsequent measurement / estimation schedules** for patio furniture and garden tools; sum for total estimated ending inventory.  
(c) Estimate ending inventory using the **blended 30% of cost** rate on combined totals; compute the difference vs the separate-class total.  
(d) Prepare the **March 31 period-end adjusting entry** using the **preferable separate-class** total estimated EI (debit ending Inventory and COGS; credit beginning Inventory and Purchases).  
(e) Compute estimated **missing inventory (theft/shrinkage)** if books are set to the separate-class GP estimate and the physical count is $120,000; prepare the write-down entry.  
(f) In two to three sentences, explain which estimation approach is preferable and which textbook limitation is illustrated.

**Answer key:**

**(a) Markup conversions**

| Class | Markup on cost | GP% of sales | Cost % of sales |
|---|---:|---:|---:|
| Patio furniture | 40% | \(0.40/1.40 = 2/7 \approx 28.571\%\) | \(5/7 \approx 71.429\%\) |
| Garden tools | 25% | \(0.25/1.25 = 20\%\) | **80%** |
| Blended (proposed) | 30% | \(0.30/1.30 = 3/13 \approx 23.077\%\) | \(10/13 \approx 76.923\%\) |

**(b) Separate-class subsequent measurement schedules**

**Patio furniture**

| Component | Amount |
|---|---:|
| Beginning inventory | $95,000 |
| Add: Net purchases | 220,000 |
| **GAS** | **315,000** |
| Subtract: Est. COGS \($336{,}000 \times 5/7\) | (240,000) |
| **Est. ending inventory** | **$75,000** |

**Garden tools**

| Component | Amount |
|---|---:|
| Beginning inventory | $55,000 |
| Add: Net purchases | 145,000 |
| **GAS** | **200,000** |
| Subtract: Est. COGS \($184{,}000 \times 0.80\) | (147,200) |
| **Est. ending inventory** | **$52,800** |

**Total estimated EI (separate classes)** = \(75{,}000 + 52{,}800 = \mathbf{\$127{,}800}\).

**(c) Blended-rate estimate (combined)**

| Component | Amount |
|---|---:|
| Beginning inventory (total) | $150,000 |
| Add: Net purchases (total) | 365,000 |
| **GAS** | **515,000** |
| Subtract: Est. COGS \($520{,}000 \times 10/13\) | (400,000) |
| **Est. ending inventory (blended)** | **$115,000** |

Difference: separate-class total exceeds blended by \(127{,}800 - 115{,}000 = \mathbf{\$12{,}800}\) (blended **understates** inventory by $12,800 here).

**(d) March 31 — period-end adjusting entry (separate-class total)**  
Est. COGS (sum of class COGS) = \(240{,}000 + 147{,}200 = \mathbf{\$387{,}200}\).  
GAS total = \(150{,}000 + 365{,}000 = \mathbf{\$515{,}000}\).  
Est. EI = \(515{,}000 - 387{,}200 = 127{,}800\) (matches sum of class EIs).

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending, estimated) | 127,800 | |
| Cost of Goods Sold | 387,200 | |
| Inventory (beginning) | | 150,000 |
| Purchases | | 365,000 |
| *Interim book of separate-class GP estimate* | | |

**Check:** Dr \(127{,}800 + 387{,}200 = 515{,}000\); Cr \(150{,}000 + 365{,}000 = 515{,}000\). **Balanced.**

**(e) Theft / shrinkage vs physical count**  
Estimated missing inventory = \(127{,}800 - 120{,}000 = \mathbf{\$7{,}800}\).

| Account | Debit | Credit |
|---|---:|---:|
| Inventory Shortage Loss (or COGS) | 7,800 | |
| Inventory | | 7,800 |
| *Write inventory down from GP estimate to physical count* | | |

**Check:** Dr = Cr = 7,800. **Balanced.**  
Ending inventory after shortage = **$120,000**.

**(f) Preferable method / limitation**  
When product lines have **materially different markups**, the gross profit method should be applied **separately by class** and the class estimates **summed**. A single blended rate is unreliable when the **sales mix** shifts toward higher- or lower-margin lines—this is a primary textbook **limitation** of the gross profit method. Separate schedules are the subsequent-measurement form that respects class economics.

**Key insight:** Subsequent measurement under LO 10-4 is not only multi-period rollforward—it is also **multi-class** measurement when markups differ. The same GAS − est. COGS engine supports interim reporting, reasonableness tests against physical counts, and detection of theft/shrinkage.

---

### Q4 — MC (markup conversion and estimated EI)
**LO:** LO 10-4  
**Concept:** Convert markup on cost and select estimated ending inventory under the gross profit method  
**Question:**  
**Pinecrest Distributors** reports beginning inventory of **$82,000**, net purchases of **$318,000**, and sales of **$360,000**. Markup on cost has remained constant at **25%**. What is the estimated cost of ending inventory under the gross profit method?

- A) $112,000  
- B) $148,000  
- C) $184,000  
- D) $40,000  

**Answer:** A.  
GP% of sales = \(0.25 / 1.25 = 0.20\).  
Est. COGS = \(360{,}000 \times 0.80 = \$288{,}000\).  
GAS = \(82{,}000 + 318{,}000 = \$400{,}000\).  
Est. EI = \(400{,}000 - 288{,}000 = \mathbf{\$112{,}000}\).  
Distractors: B uses cost % = 70% (wrong conversion, as if 30% of sales GP); C is GAS − sales × 60% style error; D is GAS − sales (treats sales as COGS).

---

### Q5 — MC (multi-class application / method choice)
**LO:** LO 10-4  
**Concept:** Identify when the gross profit method must be applied separately by inventory class  
**Question:**  
Which situation best requires applying the gross profit method **separately to each inventory class** (then summing class estimates) rather than using one company-wide average GP rate?

- A) The company uses a perpetual system and can count inventory monthly.  
- B) Product lines have **widely different markup rates**, and the sales mix can shift across lines.  
- C) Markup is given as a percentage of **cost** rather than sales (single product line).  
- D) Ending inventory is needed only for an internal budget draft with no financial-statement use.  

**Answer:** B.  
Textbook limitation: different markup rates and **sales-mix shifts** change the average GP rate and impair reliability of a single blended rate. Separate class estimates are required; then sum for total inventory. A is about when estimation may be unnecessary; C only requires converting cost markup to sales markup for that one line; D does not create a multi-class requirement.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (conversions, multi-period rollforward, multi-class schedules, COGS, EI, loss, interim, theft)
- [x] Core demo not sidebar-only (Demo 10-4 / Review 10-4 path: GP method, interim, casualty, multi-class limitation)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 only)
- [x] Original company names and numbers (not Diaz / Atlas / Meridian / Cascade textbook or agent_060 figures)
- [x] Emphasis: subsequent_measurement_schedule (multi-period EI rollforward + multi-class schedules)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
