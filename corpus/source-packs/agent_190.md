# Agent 190 — CORE DEMO — LO 10-3

**Chapter:** 10  
**LO title:** Demonstrate the relative sales value method to allocate costs to inventory  
**Critical gap LO:** no

## Concept list for this pack
- Lump-sum (basket) purchase of multiple inventory types at one price
- Relative sales value (RSV) allocation of total cost to inventory grades/categories
- Initial recognition JE: debit each inventory type for allocated cost; credit cash/payable for total lump-sum cost
- Unit cost = allocated cost ÷ units of that type
- Subsequent measurement schedule: ending inventory by category after partial sales (rollforward)
- Disposal/sale JE: remove allocated cost via COGS; record sales at actual selling prices
- Uniform gross profit percentage across types when costs are allocated by relative sales value
- Land-subdivision (real estate inventory) application of RSV (core demo path, not sidebar)

---

### Q1 — CORE — Graded produce: RSV allocation, purchase JE, inventory schedule, sales
**LO:** LO 10-3  
**Concept:** Relative sales value allocation of lump-sum purchase cost; subsequent inventory schedule after partial sales  
**Scenario:**  
Cascade Orchards Co. purchases **1,400 bushels** of ungraded pears for **$6,000 cash** on May 1. Sorting and grading cost an additional **$300 cash**. Total cost to allocate = **$6,300**. Sorting yields:

| Grade | Quantity (bushels) | Unit retail price |
|-------|-------------------:|------------------:|
| A     | 400               | $10.00            |
| B     | 500               | $6.00             |
| C     | 500               | $4.00             |

Through May 31, Cascade sold **250** Grade A, **300** Grade B, and **400** Grade C bushels for cash at the retail prices above. The company uses a perpetual inventory system.

**Required:**  
a. Prepare the **relative sales value allocation schedule** of the $6,300 lump-sum cost to Grades A, B, and C (show total sales value, fraction, allocated cost, and unit cost).  
b. Record the **May 1 purchase** journal entry allocating cost to each inventory grade.  
c. Prepare a **subsequent measurement schedule** as of May 31 showing for each grade: units sold, COGS, units remaining, and ending inventory cost.  
d. Record the **May sales and COGS** journal entries (one combined sales entry and one combined COGS entry is acceptable).  
e. Compute the **gross profit percentage** for each grade assuming the entire lot were sold at the listed retail prices (verify they are equal).

**Answer key:**  

**a. Relative sales value allocation**  

| Grade | Qty | Unit SP | Total sales value | Fraction of total SV | Allocated cost | Unit cost |
|-------|----:|--------:|------------------:|---------------------:|---------------:|----------:|
| A     | 400 | $10.00  | $4,000            | 4,000 / 9,000        | **$2,800**     | **$7.00** |
| B     | 500 | 6.00    | 3,000             | 3,000 / 9,000        | **2,100**      | **$4.20** |
| C     | 500 | 4.00    | 2,000             | 2,000 / 9,000        | **1,400**      | **$2.80** |
| **Total** | **1,400** | | **$9,000** | **1.000** | **$6,300** | |

Computations:  
- A: \(4{,}000 / 9{,}000 \times 6{,}300 = 2{,}800\); unit = \(2{,}800 / 400 = 7.00\)  
- B: \(3{,}000 / 9{,}000 \times 6{,}300 = 2{,}100\); unit = \(2{,}100 / 500 = 4.20\)  
- C: \(2{,}000 / 9{,}000 \times 6{,}300 = 1{,}400\); unit = \(1{,}400 / 500 = 2.80\)  
**Check:** Allocated costs sum to $6,300.

**b. May 1 — initial recognition JE**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory—Grade A Pears (400 bu) | 2,800 | |
| Inventory—Grade B Pears (500 bu) | 2,100 | |
| Inventory—Grade C Pears (500 bu) | 1,400 | |
| Cash | | 6,300 |
| *To allocate lump-sum purchase + sorting cost by relative sales value* | | |

**Check:** Dr 2,800 + 2,100 + 1,400 = 6,300 = Cr. Balanced.

**c. Subsequent measurement schedule (May 31)**  

| Grade | Beg. units | Unit cost | Beg. cost | Units sold | COGS | EI units | **EI cost** |
|-------|----------:|----------:|----------:|-----------:|-----:|---------:|------------:|
| A     | 400       | $7.00     | $2,800    | 250        | **1,750** | 150   | **1,050** |
| B     | 500       | 4.20      | 2,100     | 300        | **1,260** | 200   | **840** |
| C     | 500       | 2.80      | 1,400     | 400        | **1,120** | 100   | **280** |
| **Total** | **1,400** | | **$6,300** | | **$4,130** | | **$2,170** |

Rollforward check: \(6{,}300 - 4{,}130 = 2{,}170\).

Detail:  
- A COGS \(250 \times 7.00 = 1{,}750\); EI \(150 \times 7.00 = 1{,}050\)  
- B COGS \(300 \times 4.20 = 1{,}260\); EI \(200 \times 4.20 = 840\)  
- C COGS \(400 \times 2.80 = 1{,}120\); EI \(100 \times 2.80 = 280\)

**d. May sales / disposal JEs**  

Sales revenue: \(250 \times 10 + 300 \times 6 + 400 \times 4 = 2{,}500 + 1{,}800 + 1{,}600 = 5{,}900\).

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 5,900 | |
| Sales Revenue | | 5,900 |
| *To record cash sales of graded pears* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 4,130 | |
| Inventory—Grade A Pears | | 1,750 |
| Inventory—Grade B Pears | | 1,260 |
| Inventory—Grade C Pears | | 1,120 |
| *To remove allocated cost of pears sold* | | |

**Check:** Sales JE Dr = Cr = 5,900. COGS JE Dr 4,130 = Cr 1,750 + 1,260 + 1,120. Balanced.

**e. Gross profit percentage (full lot at listed prices)**  

| Grade | Sales value | Allocated cost | Gross profit | GP % |
|-------|------------:|---------------:|-------------:|-----:|
| A     | $4,000      | $2,800         | $1,200       | **30%** |
| B     | 3,000       | 2,100          | 900          | **30%** |
| C     | 2,000       | 1,400          | 600          | **30%** |
| Total | $9,000      | $6,300         | $2,700       | **30%** |

Because cost is allocated in proportion to sales value, the GP percentage is the same for every grade: \(1 - 6{,}300/9{,}000 = 30\%\).

**Key insight:** The relative sales value method assigns more cost to higher-priced inventory so that each type carries the **same** expected gross margin; subsequent EI and COGS use the **allocated unit cost**, not retail price.

---

### Q2 — CORE number variant — Nut grading: RSV, schedule, sales
**LO:** LO 10-3  
**Concept:** Relative sales value allocation (number variant); inventory rollforward after partial sales  
**Scenario:**  
Harbor Nut Processors Inc. purchases **1,400 bags** of ungraded walnuts for **$9,000 cash** on July 10. Freight-in and grading cost **$600 cash**. Total cost to allocate = **$9,600**. Grading yields:

| Grade     | Quantity (bags) | Unit retail price |
|-----------|----------------:|------------------:|
| Premium   | 400             | $15.00            |
| Select    | 500             | $8.00             |
| Standard  | 500             | $4.00             |

By July 31, Harbor sold **250** Premium, **300** Select, and **350** Standard bags for cash at the listed retail prices. Perpetual inventory system.

**Required:**  
a. Prepare the RSV allocation schedule (sales value, fraction, allocated cost, unit cost).  
b. Record the July 10 purchase JE.  
c. Prepare the July 31 subsequent measurement schedule (COGS and EI by grade).  
d. Record sales and COGS journal entries for July.  
e. Show that the full-lot GP percentage is identical across grades.

**Answer key:**  

**a. Relative sales value allocation**  

| Grade    | Qty | Unit SP | Total SV | Fraction        | Allocated cost | Unit cost |
|----------|----:|--------:|---------:|----------------:|---------------:|----------:|
| Premium  | 400 | $15.00  | $6,000   | 6,000 / 12,000  | **$4,800**     | **$12.00** |
| Select   | 500 | 8.00    | 4,000    | 4,000 / 12,000  | **3,200**      | **$6.40** |
| Standard | 500 | 4.00    | 2,000    | 2,000 / 12,000  | **1,600**      | **$3.20** |
| **Total**| **1,400** | | **$12,000** | **1.000** | **$9,600** | |

Computations:  
- Premium: \(6{,}000/12{,}000 \times 9{,}600 = 4{,}800\); unit \(4{,}800/400 = 12.00\)  
- Select: \(4{,}000/12{,}000 \times 9{,}600 = 3{,}200\); unit \(3{,}200/500 = 6.40\)  
- Standard: \(2{,}000/12{,}000 \times 9{,}600 = 1{,}600\); unit \(1{,}600/500 = 3.20\)  
**Check:** \(4{,}800 + 3{,}200 + 1{,}600 = 9{,}600\).

**b. July 10 — initial recognition JE**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory—Premium Walnuts (400 bags) | 4,800 | |
| Inventory—Select Walnuts (500 bags) | 3,200 | |
| Inventory—Standard Walnuts (500 bags) | 1,600 | |
| Cash | | 9,600 |
| *Lump-sum purchase + freight/grading allocated by RSV* | | |

**Check:** Dr = Cr = 9,600. Balanced.

**c. Subsequent measurement schedule (July 31)**  

| Grade    | Beg. units | Unit cost | Beg. cost | Units sold | COGS | EI units | **EI cost** |
|----------|----------:|----------:|----------:|-----------:|-----:|---------:|------------:|
| Premium  | 400       | $12.00    | $4,800    | 250        | **3,000** | 150   | **1,800** |
| Select   | 500       | 6.40      | 3,200     | 300        | **1,920** | 200   | **1,280** |
| Standard | 500       | 3.20      | 1,600     | 350        | **1,120** | 150   | **480** |
| **Total**| **1,400** | | **$9,600** | | **$6,040** | | **$3,560** |

Rollforward: \(9{,}600 - 6{,}040 = 3{,}560\).

Detail:  
- Premium COGS \(250 \times 12 = 3{,}000\); EI \(150 \times 12 = 1{,}800\)  
- Select COGS \(300 \times 6.40 = 1{,}920\); EI \(200 \times 6.40 = 1{,}280\)  
- Standard COGS \(350 \times 3.20 = 1{,}120\); EI \(150 \times 3.20 = 480\)

**d. July sales / disposal JEs**  

Sales: \(250 \times 15 + 300 \times 8 + 350 \times 4 = 3{,}750 + 2{,}400 + 1{,}400 = 7{,}550\).

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 7,550 | |
| Sales Revenue | | 7,550 |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 6,040 | |
| Inventory—Premium Walnuts | | 3,000 |
| Inventory—Select Walnuts | | 1,920 |
| Inventory—Standard Walnuts | | 1,120 |

**Check:** Both JEs balance (7,550 = 7,550; 6,040 = 3,000 + 1,920 + 1,120).

**e. Full-lot GP %**  

| Grade    | SV     | Cost   | GP     | GP % |
|----------|-------:|-------:|-------:|-----:|
| Premium  | $6,000 | $4,800 | $1,200 | **20%** |
| Select   | 4,000  | 3,200  | 800    | **20%** |
| Standard | 2,000  | 1,600  | 400    | **20%** |
| Total    | $12,000| $9,600 | $2,400 | **20%** |

\(1 - 9{,}600/12{,}000 = 20\%\) for every grade.

**Key insight:** Changing purchase price, sorting cost, and retail mix only changes the **fractions and unit costs**; the method (allocate by relative sales value, then track EI/COGS at allocated unit cost) is identical to Q1.

---

### Q3 — CORE alternate angle — Subdivided land lots: RSV + year-end inventory schedule + sales
**LO:** LO 10-3  
**Concept:** Relative sales value method for real-estate inventory lots; period-end inventory valuation schedule and disposal (sale) entries  
**Scenario:**  
Copperleaf Estates LLC purchased a tract of land for **$420,000 cash** on April 1 to subdivide and sell as residential lots. Approximately **12%** of the acreage is reserved for public greenbelt and walkways (not sold separately). The sellable lots are categorized as follows (full $420,000 is allocated to the three lot categories by relative sales value—public space cost is absorbed into lot inventory):

| Category | Number of lots | Expected selling price per lot |
|----------|---------------:|-------------------------------:|
| Vista    | 15             | $20,000                        |
| Ridge    | 20             | $10,000                        |
| Meadow   | 10             | $10,000                        |

By December 31 (year-end), Copperleaf had sold **8 Vista**, **14 Ridge**, and **7 Meadow** lots for cash at the expected selling prices. Perpetual inventory system; lots are inventory (not PP&E).

**Required:**  
a. Prepare the RSV allocation of the **$420,000** land cost to the three lot categories (include unit cost per lot).  
b. Record the **April 1 purchase** JE.  
c. Prepare the **December 31 subsequent measurement / inventory valuation schedule** by category (units remaining and EI cost).  
d. Record **sales and COGS** for the year (may combine or present by category).  
e. Compute year-end gross profit and verify it equals the RSV-implied margin on lots sold.

**Answer key:**  

**a. Relative sales value allocation**  

| Category | Lots | Unit SP | Total SV   | Fraction of total SV | Allocated cost | Unit cost |
|----------|-----:|--------:|-----------:|---------------------:|---------------:|----------:|
| Vista    | 15   | $20,000 | $300,000   | 300,000 / 600,000    | **$210,000**   | **$14,000** |
| Ridge    | 20   | 10,000  | 200,000    | 200,000 / 600,000    | **140,000**    | **$7,000** |
| Meadow   | 10   | 10,000  | 100,000    | 100,000 / 600,000    | **70,000**     | **$7,000** |
| **Total**| **45** | | **$600,000** | **1.000** | **$420,000** | |

Computations:  
- Vista: \(300{,}000/600{,}000 \times 420{,}000 = 210{,}000\); unit \(210{,}000/15 = 14{,}000\)  
- Ridge: \(200{,}000/600{,}000 \times 420{,}000 = 140{,}000\); unit \(140{,}000/20 = 7{,}000\)  
- Meadow: \(100{,}000/600{,}000 \times 420{,}000 = 70{,}000\); unit \(70{,}000/10 = 7{,}000\)  
**Check:** \(210{,}000 + 140{,}000 + 70{,}000 = 420{,}000\).

Implied full-lot GP %: \(1 - 420{,}000/600{,}000 = 30\%\).

**b. April 1 — initial recognition JE**  

| Account | Debit | Credit |
|---|---:|---:|
| Inventory—Vista Lots (15) | 210,000 | |
| Inventory—Ridge Lots (20) | 140,000 | |
| Inventory—Meadow Lots (10) | 70,000 | |
| Cash | | 420,000 |
| *Lump-sum land purchase allocated to lot inventory by relative sales value* | | |

**Check:** Dr = Cr = 420,000. Balanced.

**c. December 31 subsequent measurement schedule (emphasis)**  

| Category | Beg. lots | Unit cost | Beg. cost | Lots sold | COGS | EI lots | **EI cost** |
|----------|----------:|----------:|----------:|----------:|-----:|--------:|------------:|
| Vista    | 15        | $14,000   | $210,000  | 8         | **112,000** | 7  | **98,000** |
| Ridge    | 20        | 7,000     | 140,000   | 14        | **98,000**  | 6  | **42,000** |
| Meadow   | 10        | 7,000     | 70,000    | 7         | **49,000**  | 3  | **21,000** |
| **Total**| **45** | | **$420,000** | **29** | **$259,000** | **16** | **$161,000** |

Rollforward: \(420{,}000 - 259{,}000 = 161{,}000\).  
Detail: Vista EI \(7 \times 14{,}000 = 98{,}000\); Ridge EI \(6 \times 7{,}000 = 42{,}000\); Meadow EI \(3 \times 7{,}000 = 21{,}000\).

**Year-end balance sheet inventory** = **$161,000** (sum of remaining lot costs).

**d. Disposal / settlement (sales) JEs**  

Sales revenue:  
- Vista \(8 \times 20{,}000 = 160{,}000\)  
- Ridge \(14 \times 10{,}000 = 140{,}000\)  
- Meadow \(7 \times 10{,}000 = 70{,}000\)  
- **Total sales = $370,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 370,000 | |
| Sales Revenue | | 370,000 |
| *Cash sales of 8 Vista, 14 Ridge, and 7 Meadow lots* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 259,000 | |
| Inventory—Vista Lots | | 112,000 |
| Inventory—Ridge Lots | | 98,000 |
| Inventory—Meadow Lots | | 49,000 |
| *Remove allocated cost of lots sold* | | |

**Check:** Sales Dr = Cr = 370,000. COGS Dr 259,000 = Cr 112,000 + 98,000 + 49,000. Balanced.

**e. Gross profit on lots sold**  
GP = Sales \(370{,}000\) − COGS \(259{,}000\) = **$111,000**.  
GP % = \(111{,}000 / 370{,}000 = 30\%\), equal to the RSV-implied margin (because every lot was sold at its expected selling price used in the allocation).

**Key insight:** For subdivided land, RSV allocates the entire tract cost to sellable lot categories; year-end inventory is the **sum of remaining lots × allocated unit cost**. Public greenbelt is not a separate inventory account—its cost is embedded via the RSV fractions.

---

### Q4 — MC — Identify correct RSV allocated cost for one group
**LO:** LO 10-3  
**Concept:** Relative sales value method — choose correct allocated cost for a lot group  
**Question:**  
Pinecrest Land Co. purchased land for **$3,500,000** cash to subdivide into building lots as follows:

| Group | Number of lots | Price per lot |
|-------|---------------:|--------------:|
| A     | 25             | $40,000       |
| B     | 40             | $50,000       |
| C     | 50             | $20,000       |

Using the relative sales value method, what is the **allocated cost** of land for **Group B**?

- A) $2,000,000  
- B) $1,750,000  
- C) $1,217,391  
- D) $1,166,667  

**Answer:** **B. $1,750,000.**  

Group sales values: A \(25 \times 40{,}000 = 1{,}000{,}000\); B \(40 \times 50{,}000 = 2{,}000{,}000\); C \(50 \times 20{,}000 = 1{,}000{,}000\); **total SV = $4,000,000**.  
Allocated cost of B: \(2{,}000{,}000 / 4{,}000{,}000 \times 3{,}500{,}000 = \mathbf{1{,}750{,}000}\).

Distractors:  
- A is Group B’s **total sales value**, not allocated cost.  
- C is allocation by **lot count** (\(40/115 \times 3{,}500{,}000 \approx 1{,}217{,}391\)), not relative sales value.  
- D is an **equal three-way** split of cost (\(3{,}500{,}000 / 3 \approx 1{,}166{,}667\)).

---

### Self-check
- [x] Every JE balances (purchase, sales, COGS in Q1–Q3)
- [x] Math recomputed (fractions, unit costs, EI rollforwards, GP %)
- [x] Core demo not sidebar-only (Demo 10-3 / Review 10-3 / E10-11–E10-12 path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC classification/method item)
- [x] Angles: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period-end inventory valuation, disposal/sale JEs
