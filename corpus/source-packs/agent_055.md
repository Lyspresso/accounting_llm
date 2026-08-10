# Agent 55 — CORE DEMO — LO 9-8

**Chapter:** 9  
**LO title:** Apply the dollar-value LIFO method  
**Critical gap LO:** no

## Concept list for this pack
- Dollar-value LIFO pools inventory **dollars** (not unit costs of individual products), reducing LIFO liquidation risk
- Four-step computation: (1) restate ending FIFO inventory to **base-year dollars** (EI ÷ index), (2) arrange into **layers**, (3) match each layer to its **originating index**, (4) restate layers to **dollar-value LIFO** (layer × its index)
- Base year = first year of DV LIFO (or adoption date inventory); that year’s FIFO EI is the base layer at index 1.00
- Internal books stay on **FIFO** (or average cost); DV LIFO is applied **at year-end** for external reporting and tax
- **LIFO reserve** = Ending inventory at FIFO − Ending inventory at dollar-value LIFO
- Period-end adjusting JE: Dr **Cost of Goods Sold**, Cr **Allowance to Reduce FIFO Inventory to LIFO Basis** when the reserve increases; reverse when the reserve decreases
- New layers only when base-year-dollar inventory **increases**; layer **liquidation** when base-year-dollar inventory **decreases** (oldest layers retained first; newest layers drop first)
- Presentation/disclosure: Inventory often shown net of the LIFO allowance; LIFO reserve disclosed in notes
- Classification: the allowance is a **valuation contra** to inventory (not a liability)

---

### Q1 — CORE — Ridgeway Hardware: adopt dollar-value LIFO, layers, LIFO-reserve JEs (initial recognition emphasis)
**LO:** LO 9-8  
**Concept:** Initial year base layer; subsequent DV LIFO measurement schedule; first and subsequent LIFO-reserve adjusting JEs; BS presentation  
**Scenario:**  
**Ridgeway Hardware Co.** began operations on **January 1, Year 1**. It maintains **FIFO** perpetual records for internal management. For **external reporting and income tax**, it adopts the **dollar-value LIFO** method with a **single inventory pool**. Year 1 is the base year (index **1.00**).

Selected year-end data:

| Year | Ending inventory at FIFO (year-end prices) | Price index |
|---:|---:|---:|
| Year 1 | $48,000 | 1.00 |
| Year 2 | $66,000 | 1.20 |
| Year 3 | $79,200 | 1.32 |

Additional Year 2 fact (FIFO books continue during the year):  
On March 15, Year 2, Ridgeway purchased merchandise on account for **$42,500** (recorded at cost under the company’s FIFO system; no year-end conversion is made at purchase date).

**Required:**  
(a) Explain why the March 15 purchase is **not** recorded at dollar-value LIFO, and prepare the **initial recognition** journal entry for that purchase.  
(b) Compute **dollar-value LIFO ending inventory** for Year 1, Year 2, and Year 3 using the four-step method. Present a complete layer schedule.  
(c) Compute the **LIFO reserve** at each year-end and the **adjustment** to the reserve each year.  
(d) Prepare the **period-end adjusting journal entries** on December 31, Year 2 and December 31, Year 3 to convert FIFO inventory to dollar-value LIFO (use **Allowance to Reduce FIFO Inventory to LIFO Basis**).  
(e) Show the December 31, Year 3 **balance-sheet presentation** of inventory (FIFO gross, allowance, net / LIFO amount) and one related **disclosure** note point.

**Answer key:**

**(a) Purchase remains on FIFO books; initial recognition JE**  
Dollar-value LIFO is **not** applied transaction-by-transaction. Ridgeway continues FIFO (or other internal cost) for purchases and only measures ending inventory under DV LIFO at **year-end**, then records a LIFO-reserve adjustment (LO 9-6 / Demo 9-8).

```
Dr Inventory (or Purchases, if periodic) ........ 42,500
   Cr Accounts Payable .................................. 42,500
```
(Dr = Cr = 42,500)

**(b) Dollar-value LIFO schedule (four steps)**

| Year | EI at FIFO | ÷ Index | = Base-year $ | Layers (base-year $) | × Layer index | = DV LIFO |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | $48,000 | 1.00 | $48,000 | $48,000 | 1.00 | **$48,000** |
| 2 | 66,000 | 1.20 | 55,000 | 48,000 | 1.00 | 48,000 |
|  |  |  |  | 7,000 | 1.20 | 8,400 |
|  |  |  |  |  |  | **$56,400** |
| 3 | 79,200 | 1.32 | 60,000 | 48,000 | 1.00 | 48,000 |
|  |  |  |  | 7,000 | 1.20 | 8,400 |
|  |  |  |  | 5,000 | 1.32 | 6,600 |
|  |  |  |  |  |  | **$63,000** |

**Workings — base-year dollars**  
- Year 1: \(48{,}000 / 1.00 = 48{,}000\)  
- Year 2: \(66{,}000 / 1.20 = 55{,}000\) → new layer \(55{,}000 - 48{,}000 = 7{,}000\)  
- Year 3: \(79{,}200 / 1.32 = 60{,}000\) → new layer \(60{,}000 - 55{,}000 = 5{,}000\)

**Workings — restated layers**  
- Year 2 DV LIFO: \(48{,}000 \times 1.00 + 7{,}000 \times 1.20 = 48{,}000 + 8{,}400 = \mathbf{\$56{,}400}\)  
- Year 3 DV LIFO: \(48{,}000 + 8{,}400 + 5{,}000 \times 1.32 = 48{,}000 + 8{,}400 + 6{,}600 = \mathbf{\$63{,}000}\)

No liquidation: base-year inventory increased each year.

**(c) LIFO reserve and annual adjustment**

| Date | FIFO EI | DV LIFO EI | LIFO reserve (FIFO − LIFO) | Adjustment to reserve |
|---|---:|---:|---:|---:|
| Dec 31, Year 1 | $48,000 | $48,000 | $0 | $0 |
| Dec 31, Year 2 | 66,000 | 56,400 | **9,600** | **9,600** |
| Dec 31, Year 3 | 79,200 | 63,000 | **16,200** | **6,600** |

Checks: \(9{,}600 = 66{,}000 - 56{,}400\); \(16{,}200 = 79{,}200 - 63{,}000\); \(6{,}600 = 16{,}200 - 9{,}600\).

**(d) Period-end adjusting JEs (LIFO reserve)**

*December 31, Year 2 — establish / increase LIFO reserve (initial conversion JE)*  
```
Dr Cost of Goods Sold ......................... 9,600
   Cr Allowance to Reduce FIFO Inventory to LIFO Basis ... 9,600
```
(Dr = Cr = 9,600)

*December 31, Year 3 — further increase LIFO reserve*  
```
Dr Cost of Goods Sold ......................... 6,600
   Cr Allowance to Reduce FIFO Inventory to LIFO Basis ... 6,600
```
(Dr = Cr = 6,600)

(No Year 1 reserve entry: base year FIFO = base year LIFO.)

**(e) Presentation and disclosure — December 31, Year 3**

| | Amount |
|---|---:|
| Inventory at FIFO | $79,200 |
| Less: Allowance to reduce FIFO inventory to LIFO basis | (16,200) |
| **Inventory (dollar-value LIFO)** | **$63,000** |

**Disclosure:** Report the **LIFO reserve** (or the allowance balance) of **$16,200** and the fact that inventories are stated on a **dollar-value LIFO** basis (policy note). Users may add back the reserve to approximate FIFO inventory for ratio analysis.

**Key insight:** Dollar-value LIFO is a **year-end measurement overlay** on FIFO books. Purchases are recognized at actual cost; the **first material JE** for DV LIFO is usually the Year 2 (or adoption-year) **LIFO reserve** entry that reduces inventory (via allowance) and increases COGS.

---

### Q2 — CORE number variant — Summitline Tools twin
**LO:** LO 9-8  
**Concept:** Number-variant twin of DV LIFO layers, reserve schedule, and period-end adjusting JEs  
**Scenario:**  
**Summitline Tools Inc.** uses FIFO internally and **dollar-value LIFO** for external reporting and tax. Year 1 is the base year.

| Year | Ending inventory at FIFO | Price index |
|---:|---:|---:|
| Year 1 | $100,000 | 1.00 |
| Year 2 | $140,800 | 1.28 |
| Year 3 | $165,600 | 1.38 |

**Required:**  
(a) Compute dollar-value LIFO ending inventory for each year (full layer schedule).  
(b) Compute LIFO reserve and the annual adjustment to the reserve.  
(c) Prepare December 31, Year 2 and Year 3 adjusting entries to the LIFO allowance.  
(d) State inventory **net** of allowance at December 31, Year 3.

**Answer key:**

**(a) DV LIFO schedule**

| Year | FIFO EI | ÷ Index | Base-year $ | Layers | × Index | DV LIFO |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | $100,000 | 1.00 | $100,000 | $100,000 | 1.00 | **$100,000** |
| 2 | 140,800 | 1.28 | 110,000 | 100,000 | 1.00 | 100,000 |
|  |  |  |  | 10,000 | 1.28 | 12,800 |
|  |  |  |  |  |  | **$112,800** |
| 3 | 165,600 | 1.38 | 120,000 | 100,000 | 1.00 | 100,000 |
|  |  |  |  | 10,000 | 1.28 | 12,800 |
|  |  |  |  | 10,000 | 1.38 | 13,800 |
|  |  |  |  |  |  | **$126,600** |

Base-year dollars: \(140{,}800 / 1.28 = 110{,}000\); \(165{,}600 / 1.38 = 120{,}000\).  
New layers: Year 2 \(10{,}000\); Year 3 \(10{,}000\).  
Year 3 DV LIFO: \(100{,}000 + 12{,}800 + 13{,}800 = \mathbf{\$126{,}600}\).

**(b) Reserve schedule**

| Date | FIFO | DV LIFO | Reserve | Adjustment |
|---|---:|---:|---:|---:|
| Dec 31, Y1 | $100,000 | $100,000 | $0 | $0 |
| Dec 31, Y2 | 140,800 | 112,800 | **28,000** | **28,000** |
| Dec 31, Y3 | 165,600 | 126,600 | **39,000** | **11,000** |

Checks: \(28{,}000 = 140{,}800 - 112{,}800\); \(39{,}000 = 165{,}600 - 126{,}600\); \(11{,}000 = 39{,}000 - 28{,}000\).

**(c) Adjusting JEs**

*Dec 31, Year 2*  
```
Dr Cost of Goods Sold ........................ 28,000
   Cr Allowance to Reduce FIFO Inventory to LIFO Basis ... 28,000
```
(Dr = Cr = 28,000)

*Dec 31, Year 3*  
```
Dr Cost of Goods Sold ........................ 11,000
   Cr Allowance to Reduce FIFO Inventory to LIFO Basis ... 11,000
```
(Dr = Cr = 11,000)

**(d) Net inventory Dec 31, Year 3**  
FIFO \(165{,}600\) − allowance \(39{,}000\) = **$126,600** (equals DV LIFO EI).

**Key insight:** Changing all dollar amounts and indices still follows the same four steps; only **layers that exist** use their originating indices—if a year had no new layer, that year’s index would not enter the DV LIFO total.

---

### Q3 — CORE alternate angle — Lakeshore Appliance: multi-year layers + LIFO layer liquidation
**LO:** LO 9-8  
**Concept:** Subsequent measurement with growth then **liquidation** of DV LIFO layers; period-end reserve JE including a **decrease** in the allowance (layer “settlement”)  
**Scenario:**  
**Lakeshore Appliance Co.** uses FIFO for internal records and **dollar-value LIFO** (one pool) for external reporting and tax. Base year is Year 1.

| Year | Ending inventory at FIFO | Price index |
|---:|---:|---:|
| Year 1 | $200,000 | 1.00 |
| Year 2 | $264,000 | 1.20 |
| Year 3 | $299,000 | 1.30 |
| Year 4 | $196,000 | 1.40 |

**Required:**  
(a) Compute dollar-value LIFO ending inventory for **each** of Years 1–4. Explicitly identify any **liquidated** layers in Year 4.  
(b) Prepare a LIFO reserve rollforward (beginning reserve, adjustment, ending reserve) for Years 2–4.  
(c) Prepare the **December 31, Year 4** adjusting entry only.  
(d) Briefly explain why dollar-value LIFO still **reduced liquidation risk** relative to unit LIFO even though a large decline occurred in Year 4, and state how inventory should be **classified/presented** at Year 4 year-end.

**Answer key:**

**(a) DV LIFO by year**

**Year 1**  
Base-year $: \(200{,}000 / 1.00 = 200{,}000\)  
Layers: \(200{,}000 \times 1.00 = \mathbf{\$200{,}000}\)

**Year 2**  
Base-year $: \(264{,}000 / 1.20 = 220{,}000\)  
Layers: \(200{,}000 \times 1.00 + 20{,}000 \times 1.20 = 200{,}000 + 24{,}000 = \mathbf{\$224{,}000}\)

**Year 3**  
Base-year $: \(299{,}000 / 1.30 = 230{,}000\)  
Layers: \(200{,}000 \times 1.00 + 20{,}000 \times 1.20 + 10{,}000 \times 1.30 = 200{,}000 + 24{,}000 + 13{,}000 = \mathbf{\$237{,}000}\)

**Year 4 (liquidation)**  
Base-year $: \(196{,}000 / 1.40 = 140{,}000\)  
Compared with Year 3 base-year inventory of \(230{,}000\), inventory in base-year dollars **declined by \(90{,}000\)**.  
Under LIFO, **newest layers liquidate first**:  
- Entire Year 3 layer \(10{,}000\) base-year $ — **liquidated**  
- Entire Year 2 layer \(20{,}000\) base-year $ — **liquidated**  
- Base (Year 1) layer reduced: \(200{,}000 - 60{,}000 = 140{,}000\) remaining  

Remaining layer:  
\(140{,}000 \times 1.00 = \mathbf{\$140{,}000}\) DV LIFO ending inventory  

(Year 4 index **1.40 is not used** to restate remaining inventory because no Year 4 layer was created.)

**(b) LIFO reserve rollforward**

| Year | FIFO EI | DV LIFO EI | Ending reserve | Adjustment (plug) |
|---:|---:|---:|---:|---:|
| 1 | $200,000 | $200,000 | $0 | — |
| 2 | 264,000 | 224,000 | 40,000 | **+40,000** |
| 3 | 299,000 | 237,000 | 62,000 | **+22,000** |
| 4 | 196,000 | 140,000 | 56,000 | **−6,000** |

Rollforward: \(0 + 40{,}000 = 40{,}000\); \(40{,}000 + 22{,}000 = 62{,}000\); \(62{,}000 - 6{,}000 = 56{,}000\).  
Checks: \(40{,}000 = 264{,}000 - 224{,}000\); \(62{,}000 = 299{,}000 - 237{,}000\); \(56{,}000 = 196{,}000 - 140{,}000\).

**(c) December 31, Year 4 adjusting JE (reserve decreases)**  
```
Dr Allowance to Reduce FIFO Inventory to LIFO Basis ... 6,000
   Cr Cost of Goods Sold ...................................... 6,000
```
(Dr = Cr = 6,000)

*Optional context — Year 2 and Year 3 entries (not required but for completeness):*  
Year 2: Dr COGS 40,000 / Cr Allowance 40,000  
Year 3: Dr COGS 22,000 / Cr Allowance 22,000  

**(d) Liquidation risk and presentation**  
- **Pooling:** DV LIFO measures one **pool of dollars**, so liquidation requires a decline in the **entire pool** in base-year dollars—not merely running out of units of one SKU (as under unit LIFO). A large overall quantity drop (as in Year 4) can still liquidate layers.  
- **Presentation:** Inventory is a **current asset**, reported at **dollar-value LIFO** (here **$140,000**), often as FIFO inventory less the **valuation allowance** of **$56,000**. Disclose LIFO method and LIFO reserve.

**Key insight:** Layer **liquidation** is identified only after restating to **base-year dollars**. Newest layers drop first; remaining older layers keep **their original indices**. A decline in the LIFO reserve reduces COGS (debit the allowance, credit COGS).

---

### Q4 — MC — Method and classification under dollar-value LIFO
**LO:** LO 9-8  
**Concept:** Classification of the LIFO allowance and application of DV LIFO steps  

**Question 1:**  
A company keeps FIFO inventory records during the year and applies dollar-value LIFO only at year-end. The credit balance in **Allowance to Reduce FIFO Inventory to LIFO Basis** is best classified as:  
- A) A current liability for unpaid inventory costs  
- B) A valuation allowance (contra-asset) deducted from inventory  
- C) A component of accumulated other comprehensive income  
- D) Deferred tax liability arising from the LIFO conformity rule  

**Answer:** **B.** The allowance converts FIFO carrying amounts to LIFO for external reporting; it is a **contra-inventory valuation** account, not a liability or AOCI item. (Tax effects of LIFO, if any, are separate deferred-tax accounting—not the nature of the inventory allowance itself.)

**Question 2:**  
Parkside Goods reports the following for its first three years under dollar-value LIFO (Year 1 = base year):

| Year | FIFO ending inventory | Index |
|---:|---:|---:|
| 1 | $50,000 | 1.00 |
| 2 | $72,000 | 1.20 |
| 3 | $78,000 | 1.30 |

What is **Year 3** ending inventory under dollar-value LIFO?  
- A) $60,000  
- B) $62,000  
- C) $65,000  
- D) $78,000  

**Answer:** **B. $62,000.**  
Year 1: base \(50{,}000\); DV LIFO \(50{,}000\).  
Year 2: base \(72{,}000 / 1.20 = 60{,}000\) → layers \(50{,}000 \times 1.00 + 10{,}000 \times 1.20 = 50{,}000 + 12{,}000 = 62{,}000\).  
Year 3: base \(78{,}000 / 1.30 = 60{,}000\) → **no new layer** (same base-year dollars as Year 2).  
Year 3 DV LIFO remains \(50{,}000 + 12{,}000 = \mathbf{\$62{,}000}\).  
(Year 3 index is **not** applied because no Year 3 layer exists. FIFO \(78{,}000\) is not the LIFO amount.)

---

### Self-check
- [x] Every JE balances (Dr = Cr documented)
- [x] Math recomputed (all layers, reserves, and MC Year 3 amount)
- [x] Core demo not sidebar-only (Demo 9-8 / Review 9-8 path; double-extension Expanding Your Knowledge not used as primary)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Angles: initial recognition (FIFO purchase + first reserve JE), subsequent measurement schedule, period-end adjusting JE, layer liquidation/settlement, classification/presentation/disclosure, number-variant twin
