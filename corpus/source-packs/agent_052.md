# Agent 52 — CORE DEMO — LO 9-5

**Chapter:** 9  
**LO title:** Demonstrate moving average, FIFO, and LIFO in a perpetual inventory system  
**Critical gap LO:** no

## Concept list for this pack
- Perpetual inventory cost flow: update Inventory and COGS on **each** purchase and each sale
- **Moving average:** recompute unit cost after every purchase; apply latest average to each sale and to ending inventory
- **FIFO (perpetual):** assign earliest remaining layers to each sale; ending inventory = most recent purchases (same EI/COGS as periodic FIFO)
- **LIFO (perpetual):** assign latest remaining layers to each sale; ending inventory tends to hold older layers (EI/COGS generally **differ** from periodic LIFO)
- **Initial recognition JE:** purchases under perpetual (gross method) — Dr Inventory / Cr Accounts Payable (or Cash)
- **Disposal/settlement JE:** sales — Dr AR (or Cash) / Cr Sales; Dr COGS / Cr Inventory at cost-flow method amount
- **Subsequent measurement schedules:** layer (or average) perpetual cards after each transaction
- **Period-end adjusting JE:** physical count vs perpetual records — inventory shortage/overage (Loss/Gain, often closed into COGS)
- Classification / presentation: Inventory as current asset; method disclosed; rising-cost ranking of EI and COGS across MA, FIFO, LIFO

---

### Q1 — CORE — Northpine Supply: perpetual MA, FIFO, LIFO schedules + purchase and sale JEs
**LO:** LO 9-5  
**Concept:** Initial recognition of inventory purchases; perpetual moving-average / FIFO / LIFO cost schedules; sale settlement (COGS) under FIFO; classification of method effects  
**Scenario:**  
**Northpine Supply Co.** sells a single SKU of industrial hose fittings and maintains a **perpetual** inventory system. It records purchases using the **gross method**. Unit selling prices are stated below. Rising purchase prices apply during June.

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| June 1 | Beginning inventory | 300 | $20 cost |
| June 5 | Purchase on account | 200 | $25 cost |
| June 10 | Credit sale | 200 | $40 selling price |
| June 18 | Purchase on account | 300 | $28 cost |
| June 24 | Credit sale | 250 | $42 selling price |
| June 29 | Purchase on account | 150 | $30 cost |

No purchase returns, discounts taken, or freight. Physical quantities match perpetual records at month-end (no shrink in this item).

**Required:**  
(a) Prepare a **perpetual inventory cost schedule** under the **moving average** method (show inventory balance after each purchase and the COGS unit cost for each sale). Compute June **ending inventory** and **COGS**.  
(b) Prepare a **perpetual inventory cost schedule** under **FIFO**. Compute June **ending inventory** and **COGS**.  
(c) Prepare a **perpetual inventory cost schedule** under **LIFO**. Compute June **ending inventory** and **COGS**.  
(d) **Initial recognition:** prepare journal entries for the three **purchases** (perpetual, gross method, on account).  
(e) **Disposal / settlement of inventory:** prepare the **sales and COGS** journal entries for June 10 and June 24 **under FIFO** (credit sales).  
(f) Verify for each method that COGAS − EI = COGS. Rank the three methods by **highest ending inventory** and by **highest COGS** (rising-cost environment). State how Inventory is presented on the balance sheet and what must be disclosed.

**Answer key:**

**Cost of goods available for sale (all methods)**  
Beginning inventory \(300 \times \$20 = \$6{,}000\)  
Purchases \(200\times\$25 + 300\times\$28 + 150\times\$30 = \$5{,}000 + \$8{,}400 + \$4{,}500 = \$17{,}900\)  
**COGAS = \$6{,}000 + \$17{,}900 = \$23{,}900**  
Units available \(300+200+300+150=950\); units sold \(200+250=450\); **EI units = 500**.

**(a) Moving average — perpetual**

| Date | Purchases (u × $) | COGS (u × $) | Inventory balance |
|---|---|---|---|
| June 1 | | | 300 × $20 = **$6,000** |
| June 5 | 200 × $25 = $5,000 | | 500 × **$22.00** = **$11,000** *(6,000+5,000)/500* |
| June 10 | | 200 × $22.00 = **$4,400** | 300 × $22.00 = **$6,600** |
| June 18 | 300 × $28 = $8,400 | | 600 × **$25.00** = **$15,000** *(6,600+8,400)/600* |
| June 24 | | 250 × $25.00 = **$6,250** | 350 × $25.00 = **$8,750** |
| June 29 | 150 × $30 = $4,500 | | 500 × **$26.50** = **$13,250** *(8,750+4,500)/500* |

**Moving average: Ending inventory = \$13,250; COGS = \$4,400 + \$6,250 = \$10,650**

**(b) FIFO — perpetual**

| Date | Purchases | COGS (layers) | Inventory layers |
|---|---|---|---|
| June 1 | | | 300 @ $20 = $6,000 |
| June 5 | 200 @ $25 = $5,000 | | 300 @ $20; 200 @ $25 |
| June 10 | | 200 @ $20 = **$4,000** | 100 @ $20; 200 @ $25 = $7,000 |
| June 18 | 300 @ $28 = $8,400 | | 100 @ $20; 200 @ $25; 300 @ $28 |
| June 24 | | 100 @ $20 + 150 @ $25 = **$5,750** | 50 @ $25; 300 @ $28 = $9,650 |
| June 29 | 150 @ $30 = $4,500 | | 50 @ $25 + 300 @ $28 + 150 @ $30 |

**FIFO EI layers:** \(50\times\$25 + 300\times\$28 + 150\times\$30 = \$1{,}250 + \$8{,}400 + \$4{,}500 = \mathbf{\$14{,}150}\)  
**FIFO COGS:** \(\$4{,}000 + \$5{,}750 = \mathbf{\$9{,}750}\)

**(c) LIFO — perpetual**

| Date | Purchases | COGS (layers) | Inventory layers |
|---|---|---|---|
| June 1 | | | 300 @ $20 = $6,000 |
| June 5 | 200 @ $25 = $5,000 | | 300 @ $20; 200 @ $25 |
| June 10 | | 200 @ $25 = **$5,000** | 300 @ $20 = $6,000 |
| June 18 | 300 @ $28 = $8,400 | | 300 @ $20; 300 @ $28 |
| June 24 | | 250 @ $28 = **$7,000** | 300 @ $20; 50 @ $28 = $7,400 |
| June 29 | 150 @ $30 = $4,500 | | 300 @ $20 + 50 @ $28 + 150 @ $30 |

**LIFO EI layers:** \(300\times\$20 + 50\times\$28 + 150\times\$30 = \$6{,}000 + \$1{,}400 + \$4{,}500 = \mathbf{\$11{,}900}\)  
**LIFO COGS:** \(\$5{,}000 + \$7{,}000 = \mathbf{\$12{,}000}\)

**(d) Initial recognition — purchase JEs (same under all three cost-flow methods; perpetual gross)**

June 5:
```
Dr Inventory ................................ 5,000
   Cr Accounts Payable .............................. 5,000
```
(Dr = Cr = 5,000)

June 18:
```
Dr Inventory ................................ 8,400
   Cr Accounts Payable .............................. 8,400
```
(Dr = Cr = 8,400)

June 29:
```
Dr Inventory ................................ 4,500
   Cr Accounts Payable .............................. 4,500
```
(Dr = Cr = 4,500)

**(e) Settlement / disposal — June sales under FIFO (perpetual)**

June 10 — record revenue and remove inventory:
```
Dr Accounts Receivable ..................... 8,000
   Cr Sales Revenue ................................. 8,000
```
(\(200 \times \$40\); Dr = Cr = 8,000)

```
Dr Cost of Goods Sold ...................... 4,000
   Cr Inventory ..................................... 4,000
```
(FIFO layers: 200 @ $20; Dr = Cr = 4,000)

June 24:
```
Dr Accounts Receivable .................... 10,500
   Cr Sales Revenue ................................ 10,500
```
(\(250 \times \$42\); Dr = Cr = 10,500)

```
Dr Cost of Goods Sold ...................... 5,750
   Cr Inventory ..................................... 5,750
```
(FIFO: 100 @ $20 + 150 @ $25; Dr = Cr = 5,750)

**(f) Verification, ranking, presentation**

| Method | EI | COGS | Check: COGAS − EI |
|---|---:|---:|---:|
| Moving average | $13,250 | $10,650 | 23,900 − 13,250 = 10,650 |
| FIFO | $14,150 | $9,750 | 23,900 − 14,150 = 9,750 |
| LIFO | $11,900 | $12,000 | 23,900 − 11,900 = 12,000 |

**Rising costs:** highest **EI** = FIFO > MA > LIFO; highest **COGS** = LIFO > MA > FIFO (inverse).  
**Presentation:** Merchandise inventory is a **current asset** on the balance sheet (often a single line; layers are memo/support only). The cost-flow **method** (FIFO, LIFO, or average) is a **significant accounting policy** disclosed in the notes. Gross margin June under FIFO sales of \(8{,}000+10{,}500=\$18{,}500\): FIFO GM \(18{,}500-9{,}750=\$8{,}750\).

**Key insight:** In a perpetual system, MA updates the unit cost after every purchase and applies that average to the next sale; FIFO always peels oldest layers first (identical totals to periodic FIFO); LIFO peels newest layers **at each sale date**, so perpetual LIFO layers and COGS can differ from a period-end-only LIFO calculation.

---

### Q2 — CORE number variant — Lakebound Merchants: perpetual MA, FIFO, LIFO
**LO:** LO 9-5  
**Concept:** Number-variant twin — perpetual moving average, FIFO, and LIFO schedules; purchase recognition and LIFO COGS settlement JEs  
**Scenario:**  
**Lakebound Merchants Inc.** maintains perpetual inventory records for a camping stove SKU. Purchases are on account (gross method). October activity:

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Oct 1 | Beginning inventory | 500 | $8 cost |
| Oct 6 | Purchase on account | 300 | $10 cost |
| Oct 12 | Credit sale | 400 | $18 selling price |
| Oct 18 | Purchase on account | 500 | $11 cost |
| Oct 25 | Credit sale | 450 | $19 selling price |
| Oct 30 | Purchase on account | 100 | $12 cost |

**Required:**  
(a) Compute October **ending inventory** and **COGS** under (1) **moving average**, (2) **FIFO**, and (3) **LIFO** perpetual. Show the inventory balance (and unit cost or layers) after each purchase and after each sale.  
(b) Prepare **initial recognition** journal entries for the three purchases.  
(c) Prepare **sales and COGS** journal entries for Oct 12 and Oct 25 **under LIFO**.  
(d) Confirm COGAS − EI = COGS for all three methods.

**Answer key:**

**COGAS**  
BI \(500\times\$8=\$4{,}000\); purchases \(300\times\$10 + 500\times\$11 + 100\times\$12 = \$3{,}000 + \$5{,}500 + \$1{,}200 = \$9{,}700\)  
**COGAS = \$13{,}700**  
Units available \(500+300+500+100=1{,}400\); sold \(400+450=850\); **EI units = 550**.

**(a1) Moving average**

| Date | Event | Inventory balance |
|---|---|---|
| Oct 1 | BI | 500 × $8 = $4,000 |
| Oct 6 | +300 @ $10 | 800 × **$8.75** = $7,000 *(4,000+3,000)/800* |
| Oct 12 | Sale 400 @ $8.75 | COGS **$3,500**; bal 400 × $8.75 = $3,500 |
| Oct 18 | +500 @ $11 | 900 × **$10.00** = $9,000 *(3,500+5,500)/900* |
| Oct 25 | Sale 450 @ $10.00 | COGS **$4,500**; bal 450 × $10 = $4,500 |
| Oct 30 | +100 @ $12 | 550 units; cost **$5,700** (avg $10.3636…) |

**MA: EI = \$5,700; COGS = \$3,500 + \$4,500 = \$8,000**

**(a2) FIFO perpetual**

| Date | COGS layers | Ending layers |
|---|---|---|
| Oct 1 | | 500 @ $8 |
| Oct 6 | | 500 @ $8; 300 @ $10 |
| Oct 12 | 400 @ $8 = **$3,200** | 100 @ $8; 300 @ $10 = $3,800 |
| Oct 18 | | 100 @ $8; 300 @ $10; 500 @ $11 |
| Oct 25 | 100 @ $8 + 300 @ $10 + 50 @ $11 = **$4,350** | 450 @ $11 = $4,950 |
| Oct 30 | | 450 @ $11 + 100 @ $12 |

**FIFO EI:** \(450\times\$11 + 100\times\$12 = \$4{,}950 + \$1{,}200 = \mathbf{\$6{,}150}\)  
**FIFO COGS:** \(\$3{,}200 + \$4{,}350 = \mathbf{\$7{,}550}\)

**(a3) LIFO perpetual**

| Date | COGS layers | Ending layers |
|---|---|---|
| Oct 1 | | 500 @ $8 |
| Oct 6 | | 500 @ $8; 300 @ $10 |
| Oct 12 | 300 @ $10 + 100 @ $8 = **$3,800** | 400 @ $8 = $3,200 |
| Oct 18 | | 400 @ $8; 500 @ $11 |
| Oct 25 | 450 @ $11 = **$4,950** | 400 @ $8; 50 @ $11 = $3,750 |
| Oct 30 | | 400 @ $8 + 50 @ $11 + 100 @ $12 |

**LIFO EI:** \(400\times\$8 + 50\times\$11 + 100\times\$12 = \$3{,}200 + \$550 + \$1{,}200 = \mathbf{\$4{,}950}\)  
**LIFO COGS:** \(\$3{,}800 + \$4{,}950 = \mathbf{\$8{,}750}\)

**(b) Initial recognition — purchases**

```
Oct 6   Dr Inventory ................ 3,000
           Cr Accounts Payable ............... 3,000

Oct 18  Dr Inventory ................ 5,500
           Cr Accounts Payable ............... 5,500

Oct 30  Dr Inventory ................ 1,200
           Cr Accounts Payable ............... 1,200
```
(Each entry balances.)

**(c) Settlement under LIFO**

Oct 12 (\(400\times\$18=\$7{,}200\) revenue; LIFO COGS \$3,800):
```
Dr Accounts Receivable ..................... 7,200
   Cr Sales Revenue ................................. 7,200

Dr Cost of Goods Sold ...................... 3,800
   Cr Inventory ..................................... 3,800
```

Oct 25 (\(450\times\$19=\$8{,}550\) revenue; LIFO COGS \$4,950):
```
Dr Accounts Receivable ..................... 8,550
   Cr Sales Revenue ................................. 8,550

Dr Cost of Goods Sold ...................... 4,950
   Cr Inventory ..................................... 4,950
```
(All JEs balance.)

**(d) Verification**

| Method | EI | COGS | COGAS − EI |
|---|---:|---:|---:|
| Moving average | $5,700 | $8,000 | 13,700 − 5,700 = 8,000 |
| FIFO | $6,150 | $7,550 | 13,700 − 6,150 = 7,550 |
| LIFO | $4,950 | $8,750 | 13,700 − 4,950 = 8,750 |

**Key insight:** Same purchase and sale **quantities**, different cost assignments only; purchase JEs debit Inventory at invoice cost regardless of cost-flow method—the method only changes **which cost leaves inventory** when COGS is recorded.

---

### Q3 — CORE alternate angle — Rivermark Trading: FIFO perpetual settlement + period-end shrink + presentation
**LO:** LO 9-5  
**Concept:** Perpetual FIFO subsequent measurement; sale settlement JEs; period-end physical-count adjusting JE; classification of inventory shortage and method disclosure  
**Scenario:**  
**Rivermark Trading Co.** uses a **perpetual FIFO** system for a specialty rope product. August records:

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Aug 1 | Beginning inventory | 80 | $15 |
| Aug 7 | Purchase on account | 120 | $16 |
| Aug 12 | Credit sale | 100 | $28 SP |
| Aug 20 | Purchase on account | 90 | $18 |
| Aug 27 | Credit sale | 70 | $29 SP |

On **August 31**, a physical count finds **116 units** on hand. Perpetual FIFO records show **120 units**. Management concludes the **4-unit** shortage is from theft/spoilage and should be removed from the **most recent remaining layer** (latest unit cost still in inventory), with the loss closed through **Loss on Inventory Shortage** (reported as part of COGS on the multi-step income statement).

**Required:**  
(a) Prepare the perpetual **FIFO** inventory schedule through August 27 (before the count). Compute book EI and COGS.  
(b) Prepare **initial recognition** purchase JEs and **sale/COGS settlement** JEs for August (FIFO).  
(c) Prepare the **period-end adjusting** entry for the inventory shortage. State the adjusted ending inventory cost.  
(d) **Classification / presentation:** (1) How is Inventory presented? (2) How is the shortage loss classified? (3) Briefly explain why FIFO EI/COGS would be the **same** if Rivermark had used **periodic** FIFO for the month (ignore shrink), whereas LIFO would often **differ** perpetual vs periodic.

**Answer key:**

**(a) FIFO perpetual schedule**

| Date | Event | COGS | Inventory layers |
|---|---|---|---|
| Aug 1 | BI | | 80 @ $15 = $1,200 |
| Aug 7 | Purchase | | 80 @ $15; 120 @ $16 |
| Aug 12 | Sale 100 | 80 @ $15 + 20 @ $16 = **$1,520** | 100 @ $16 = $1,600 |
| Aug 20 | Purchase | | 100 @ $16; 90 @ $18 |
| Aug 27 | Sale 70 | 70 @ $16 = **$1,120** | 30 @ $16 + 90 @ $18 = **$2,100** |

**Book EI (before count):** \(30\times\$16 + 90\times\$18 = \$480 + \$1{,}620 = \mathbf{\$2{,}100}\) (120 units)  
**COGS (sales only):** \(\$1{,}520 + \$1{,}120 = \mathbf{\$2{,}640}\)  
COGAS \(=\$1{,}200 + \$1{,}920 + \$1{,}620 = \$4{,}740\); \(4{,}740-2{,}100=2{,}640\) ✓

**(b) Journal entries**

Aug 7 purchase:
```
Dr Inventory ................................ 1,920
   Cr Accounts Payable .............................. 1,920
```
(Dr = Cr = 1,920)

Aug 12 sale (\(100\times\$28=\$2{,}800\); FIFO COGS \$1,520):
```
Dr Accounts Receivable ..................... 2,800
   Cr Sales Revenue ................................. 2,800

Dr Cost of Goods Sold ...................... 1,520
   Cr Inventory ..................................... 1,520
```

Aug 20 purchase:
```
Dr Inventory ................................ 1,620
   Cr Accounts Payable .............................. 1,620
```
(Dr = Cr = 1,620)

Aug 27 sale (\(70\times\$29=\$2{,}030\); FIFO COGS \$1,120):
```
Dr Accounts Receivable ..................... 2,030
   Cr Sales Revenue ................................. 2,030

Dr Cost of Goods Sold ...................... 1,120
   Cr Inventory ..................................... 1,120
```

**(c) Period-end adjusting JE — shortage**  
Remove 4 units from latest layer @ $18: \(4\times\$18=\mathbf{\$72}\).

```
Dr Loss on Inventory Shortage ................. 72
   Cr Inventory ....................................... 72
```
(Dr = Cr = 72)

**Adjusted ending inventory:** \(2{,}100 - 72 = \mathbf{\$2{,}028}\) (116 units: 30 @ $16 + 86 @ $18).  
If closed to COGS: total product cost affecting income from inventory outflows \(= 2{,}640 + 72 = \$2{,}712\).

**(d) Classification / presentation / FIFO vs LIFO system note**  
1. **Inventory** remains a **current asset** at historical cost under the elected cost-flow assumption (here FIFO after shrink).  
2. **Loss on Inventory Shortage** is typically included in **cost of goods sold** (or shown separately within operating results if material); it is **not** a prior-period restatement for normal shrink.  
3. **FIFO** assigns earliest costs to COGS regardless of whether assignment is continuous (perpetual) or at period-end (periodic), so **EI and COGS are the same** under both systems (absent mid-period quirks like the separate shrink entry). **LIFO** assigns “latest” costs **as of each sale date** under perpetual, which generally **differs** from assigning the month’s latest purchases only at period-end under periodic LIFO.

**Key insight:** Perpetual records still require a **physical count**; differences are adjusted to Inventory with a shortage/overage account. Cost-flow method governs **which unit costs** leave Inventory on sale **and** (by policy) which layer is removed for shrink.

---

### Q4 — MC (method / classification)
**LO:** LO 9-5  
**Concept:** Classification of perpetual cost-flow results (layer assignment; FIFO periodic vs perpetual)

**Question 1:**  
In a **rising-cost** environment under a **perpetual LIFO** system, ending inventory typically consists primarily of:  
- A) The most recently purchased units  
- B) A single moving-average unit cost applied to all remaining units  
- C) The earliest purchases still on hand (older layers), plus any residual recent layers not fully depleted by sales  
- D) Replacement cost of the units on hand  

**Answer:** **C.** Under perpetual LIFO, each sale removes the latest layers available **at the sale date**, so remaining inventory tends to hold older (lower, when costs are rising) layers, often mixed with small residual recent layers if a sale did not fully exhaust the latest purchase.  
A describes FIFO EI; B describes moving average; D is not the historical-cost LIFO measurement basis.

**Question 2:**  
Which statement is **correct** about inventory cost-flow methods in a perpetual system?  
- A) Moving average unit cost is recalculated only at period-end  
- B) FIFO ending inventory and COGS are the same under perpetual and periodic systems (for the same data)  
- C) Perpetual LIFO always produces the same COGS as periodic LIFO  
- D) Purchase journal entries under FIFO debit Inventory at a different amount than under LIFO for the same invoice  

**Answer:** **B.** FIFO peels earliest costs first; continuous vs period-end assignment yields the same totals. A is false—moving average updates after **each purchase**. C is false—perpetual vs periodic LIFO often differ. D is false—purchase recognition is at invoice cost; the method affects COGS when inventory is **relieved**.

---

### Self-check
- [x] Every JE balances
- [x] Math recomputed (COGAS − EI = COGS for all schedules)
- [x] Core demo not sidebar-only (Demo 9-5A/B/C perpetual MA, FIFO, LIFO path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 if any (exactly 2 MC)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
