# Agent 320 — CORE DEMO — LO 10-2

**Chapter:** 10  
**LO title:** Apply lower of cost or market rule to inventory  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **LCM applies only** when cost is measured by **LIFO** or the **retail inventory method** (FIFO/average cost use LCNRV under LO 10-1)
- **Market** = current **replacement cost**, constrained by a **ceiling** and a **floor**
  - **Ceiling** = net realizable value = estimated selling price − costs of completion/disposal
  - **Floor** = NRV − approximate **normal profit margin**
  - Practically: market = the **middle value** among replacement cost, ceiling, and floor
- Inventory carrying amount = **lower of cost or market** (item, category, or total; item is most common and yields the lowest inventory)
- When market < cost: reduce assets (**Allowance to Reduce Inventory to Market** or credit Inventory directly) and reduce equity (**COGS** or **Holding Loss on Inventory**)
- No subsequent write-up of the same goods if market recovers; the reduced amount is “cost” for later accounting
- **Period-end adjusting JE (emphasis):** allowance is remeasured only at each **reporting date** to the required credit balance (required allow = cost − LCM inventory)
- **Subsequent measurement schedule:** multi-year rollforward of cost, designated market, required LCM, required allowance, unadjusted allowance, and period-end Dr/Cr adjustment
- **Disposal / settlement:** when written-down inventory is sold, close remaining allowance into COGS so net COGS equals the net carrying amount

---

### Q1 — CORE — LCM item schedule, multi-year allowance rollforward, period-end adjusting JEs (emphasis), sale close-out

**LO:** LO 10-2  
**Concept:** Initial recognition at LIFO cost; item-level LCM market (ceiling/floor/RC) schedule; multi-year subsequent measurement of allowance; **period-end adjusting JEs** (emphasis); disposal close of allowance  
**Scenario:**  
**Northwind Outfitters LLC** values merchandise using **LIFO** and therefore applies the **lower of cost or market (LCM)** rule. It applies LCM at the **individual-item** level and maintains an **Allowance to Reduce Inventory to Market**. The allowance is remeasured only at each **December 31** year-end (not at each sale). Write-downs are charged to **Cost of Goods Sold**.

**January 8, Year 1 — initial recognition of the ending-inventory layer:** Northwind purchases (on account) the merchandise that remains on hand at December 31, Year 1. Total LIFO cost of that layer is **$20,550** (detail below). Other Year 1 purchases are sold before year-end and are already reflected in pre-adjustment COGS.

**December 31, Year 1 — per-unit data for ending inventory (LIFO cost):**

| Item | Units | Cost per unit | Est. selling price | Cost to complete & sell | Normal profit margin | Replacement cost |
|---|---:|---:|---:|---:|---:|---:|
| Ridge Tent | 40 | $160 | $200 | $20 | $30 | $145 |
| Camp Stove | 80 | 70 | 90 | 10 | 12 | 55 |
| Trail Frame | 50 | 95 | 120 | 15 | 18 | 110 |
| Base Layer | 100 | 38 | 45 | 5 | 6 | 32 |

Additional facts:
- Cost of goods sold **before** any LCM adjustment for Year 1: **$385,000**.
- All **January 1, Year 2** inventory (Year 1 ending inventory) is sold during Year 2. The Year 1 allowance balance remains on the books until the **December 31, Year 2** year-end adjustment.
- At **December 31, Year 2**, LIFO cost of ending inventory is **$27,400** and **designated market** (already constrained by ceiling/floor) is **$24,600**.
- All **January 1, Year 3** inventory is sold during Year 3. Allowance is again adjusted only at year-end.
- At **December 31, Year 3**, LIFO cost is **$15,900** and designated market is **$15,100**.
- On **April 8, Year 4**, Northwind sells **all** remaining Year 3 ending inventory for cash of **$15,500**. Inventory still carries **$15,900** cost on the books; the allowance still has its December 31, Year 3 credit balance until closed at sale.

**Required:**  
(a) Record the **January 8, Year 1** purchase of the inventory that remains at year-end (**$20,550** on account).  
(b) Prepare a **market determination schedule** (ceiling, floor, designated market) and an **LCM valuation schedule** by individual item at December 31, Year 1. Compute the total write-down.  
(c) Record the **December 31, Year 1 period-end adjusting entry** (charge COGS; credit allowance). Also show the alternative entry charging **Holding Loss on Inventory**. Show inventory net and COGS after adjustment.  
(d) Prepare a multi-year **subsequent measurement schedule** of the allowance for Year 1–Year 3 year-ends (cost, designated market / LCM, required allowance, unadjusted allowance, period-end adjustment).  
(e) Record the **December 31, Year 2** and **December 31, Year 3 period-end adjusting entries** (emphasis).  
(f) Record the **April 8, Year 4** sale and the entry to **close the allowance** into COGS. Compute net COGS on this layer and gross profit.

**Answer key:**

**(a) January 8, Year 1 — initial recognition of inventory at LIFO cost**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 20,550 | |
| Accounts Payable | | 20,550 |
| *Purchase ending-inventory layer at LIFO cost* | | |

**Check:** Dr 20,550 = Cr 20,550. **Balanced.**

**(b) December 31, Year 1 — market determination and LCM schedule**

Ceiling = selling price − cost to complete & sell.  
Floor = ceiling − normal profit margin.  
Designated market = middle value of (replacement cost, ceiling, floor).  
LCM unit value = lower of cost or designated market.

| Item | Ceiling (NRV) | Floor | RC | Designated market | Cost | LCM / unit | Units | Cost total | LCM total | Write-down |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ridge Tent | 180 | 150 | 145 | **150** (floor; RC < floor) | 160 | **150** | 40 | 6,400 | 6,000 | 400 |
| Camp Stove | 80 | 68 | 55 | **68** (floor; RC < floor) | 70 | **68** | 80 | 5,600 | 5,440 | 160 |
| Trail Frame | 105 | 87 | 110 | **105** (ceiling; RC > ceiling) | 95 | **95** | 50 | 4,750 | 4,750 | 0 |
| Base Layer | 40 | 34 | 32 | **34** (floor; RC < floor) | 38 | **34** | 100 | 3,800 | 3,400 | 400 |
| **Totals** | | | | | | | | **20,550** | **19,590** | **960** |

**Market logic notes:**  
- Ridge Tent / Camp Stove / Base Layer: RC is below the floor → market is limited to the **floor**.  
- Trail Frame: RC exceeds the ceiling → market is capped at the **ceiling**, but cost ($95) is still below market ($105), so **no write-down**.

**(c) December 31, Year 1 — period-end adjusting JE (write-down $960) — emphasis**

(1) Charge COGS (Northwind’s policy):

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 960 | |
| Allowance to Reduce Inventory to Market | | 960 |
| *Period-end only: reduce LIFO inventory to LCM (item approach)* | | |

**Check:** Dr 960 = Cr 960. **Balanced.**

(2) Alternative — charge separate holding loss:

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 960 | |
| Allowance to Reduce Inventory to Market | | 960 |
| *Recognize inventory holding loss; allowance contra to inventory* | | |

**Check:** Dr 960 = Cr 960. **Balanced.**

Year 1 presentation (COGS method):  
Inventory, net = \(20{,}550 - 960 =\) **$19,590**  
COGS after adjustment = \(385{,}000 + 960 =\) **$385,960**

**(d) Subsequent measurement schedule — allowance rollforward**

| Year-end | Inventory cost | Designated market / LCM | Required allow. (Cr) | Unadjusted allow. (Cr) | Period-end adjustment |
|---|---:|---:|---:|---:|---|
| 12/31/Y1 | $20,550 | **$19,590** (item) | **$960** | $0 | **Cr $960** (to COGS) |
| 12/31/Y2 | 27,400 | **24,600** | **2,800** | 960 | **Cr $1,840** (to COGS) |
| 12/31/Y3 | 15,900 | **15,100** | **800** | 2,800 | **Dr $2,000** (from COGS) |

**Allowance T-account rollforward**

| Date | Description | Allowance Dr | Allowance Cr | Balance (Cr) |
|---|---|---:|---:|---:|
| 12/31/Y1 | Initial LCM write-down | | 960 | 960 |
| 12/31/Y2 | Period-end top-up | | 1,840 | 2,800 |
| 12/31/Y3 | Period-end reduction (new layer needs less reserve) | 2,000 | | 800 |
| 4/8/Y4 | Close on sale of inventory | 800 | | 0 |

**Schedule math checks:**  
- Y2 adj: \(2{,}800 - 960 = 1{,}840\) credit.  
- Y3 adj: \(2{,}800 - 800 = 2{,}000\) debit.  
- Ending net inventory Y2: \(27{,}400 - 2{,}800 = 24{,}600\).  
- Ending net inventory Y3: \(15{,}900 - 800 = 15{,}100\).

**(e) Period-end adjusting JEs — Years 2 and 3 (emphasis)**

**December 31, Year 2**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 1,840 | |
| Allowance to Reduce Inventory to Market | | 1,840 |
| *Period-end only: adjust allowance to Year 2 required LCM balance* | | |

**Check:** Dr 1,840 = Cr 1,840. **Balanced.** Ending allowance **$2,800** credit.

**December 31, Year 3**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 2,000 | |
| Cost of Goods Sold | | 2,000 |
| *Period-end only: reduce allowance to Year 3 required balance after inventory turn* | | |

**Check:** Dr 2,000 = Cr 2,000. **Balanced.** Ending allowance **$800** credit.

**(f) April 8, Year 4 — disposal/settlement of inventory and allowance**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 15,500 | |
| Sales Revenue | | 15,500 |
| *Cash sale of remaining inventory* | | |

**Check:** Dr 15,500 = Cr 15,500. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 15,900 | |
| Inventory | | 15,900 |
| *Remove inventory at LIFO cost* | | |

**Check:** Dr 15,900 = Cr 15,900. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 800 | |
| Cost of Goods Sold | | 800 |
| *Close allowance; reduces COGS to net carrying amount* | | |

**Check:** Dr 800 = Cr 800. **Balanced.**

Net COGS on this layer = \(15{,}900 - 800 =\) **$15,100** (equals prior net inventory).  
Gross profit = \(15{,}500 - 15{,}100 =\) **$400**.

**Key insight:** Under LCM (LIFO/retail only), market is **replacement cost constrained by ceiling and floor**, not raw NRV. The allowance is a **period-end** measurement tool: it is trued up only at each reporting date so net inventory equals current LCM, and it is closed into COGS when the related goods are sold.

---

### Q2 — CORE number variant — LCM item schedule, multi-year allowance, period-end JEs, sale close-out

**LO:** LO 10-2  
**Concept:** Number-variant twin — item-level LCM (ceiling/floor/RC); multi-year subsequent allowance schedule; **period-end adjusting JEs**; disposal close of allowance  
**Scenario:**  
**Harborline Marine Supply Inc.** values inventory using **LIFO** and applies **LCM** at the **individual-item** level with an **Allowance to Reduce Inventory to Market**. Write-downs run through **COGS**. The allowance is adjusted only at each **December 31** year-end.

**January 12, Year 1 — initial recognition of the ending-inventory layer:** Harborline purchases on account the goods remaining at December 31, Year 1. Total LIFO cost of that layer is **$29,500**.

**December 31, Year 1 — per-unit data:**

| Item | Units | Cost per unit | Est. selling price | Cost to complete & sell | Normal profit margin | Replacement cost |
|---|---:|---:|---:|---:|---:|---:|
| Sea Kayak | 25 | $540 | $620 | $40 | $80 | $490 |
| Paddle | 120 | 55 | 70 | 8 | 10 | 42 |
| Dry Bag | 200 | 28 | 36 | 4 | 5 | 22 |
| Anchor Kit | 40 | 95 | 130 | 15 | 20 | 105 |

Additional facts:
- Pre-adjustment COGS Year 1: **$512,000**.
- All January 1, Year 2 inventory is sold during Year 2; allowance remains until the Year 2 year-end adjustment.
- December 31, Year 2: LIFO cost **$33,000**; designated market **$29,400**.
- All January 1, Year 3 inventory is sold during Year 3.
- December 31, Year 3: LIFO cost **$21,200**; designated market **$20,000**.
- On **May 3, Year 4**, Harborline sells all remaining Year 3 inventory for cash of **$20,800**. Inventory cost on books is still **$21,200**; allowance still carries its December 31, Year 3 balance until closed.

**Required:**  
(a) Record the **January 12, Year 1** purchase of the ending-inventory layer.  
(b) Prepare the **market determination + LCM schedule** by item at December 31, Year 1 and the total write-down.  
(c) Record the **December 31, Year 1 period-end adjusting JE** (COGS method) and the **Holding Loss** alternative.  
(d) Prepare the multi-year **subsequent measurement schedule** of the allowance for Years 1–3.  
(e) Record the **December 31, Year 2** and **December 31, Year 3 period-end adjusting JEs**.  
(f) Record the **May 3, Year 4** sale, close the allowance, and compute net COGS and gross profit on the layer.

**Answer key:**

**(a) January 12, Year 1 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 29,500 | |
| Accounts Payable | | 29,500 |
| *Purchase ending-inventory layer at LIFO cost* | | |

**Check:** Dr 29,500 = Cr 29,500. **Balanced.**

**(b) December 31, Year 1 — market determination and LCM schedule**

| Item | Ceiling | Floor | RC | Designated market | Cost | LCM / unit | Units | Cost total | LCM total | Write-down |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Sea Kayak | 580 | 500 | 490 | **500** (floor) | 540 | **500** | 25 | 13,500 | 12,500 | 1,000 |
| Paddle | 62 | 52 | 42 | **52** (floor) | 55 | **52** | 120 | 6,600 | 6,240 | 360 |
| Dry Bag | 32 | 27 | 22 | **27** (floor) | 28 | **27** | 200 | 5,600 | 5,400 | 200 |
| Anchor Kit | 115 | 95 | 105 | **105** (RC in range) | 95 | **95** | 40 | 3,800 | 3,800 | 0 |
| **Totals** | | | | | | | | **29,500** | **27,940** | **1,560** |

**Checks:** Ceiling = SP − sell cost; Floor = ceiling − NPM; market = middle of RC/ceiling/floor.  
Write-down total: \(1{,}000 + 360 + 200 + 0 = 1{,}560\).  
Cost − LCM: \(29{,}500 - 27{,}940 = 1{,}560\).

**(c) December 31, Year 1 — period-end adjusting JE (emphasis)**

(1) COGS method:

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 1,560 | |
| Allowance to Reduce Inventory to Market | | 1,560 |
| *Period-end only: LCM write-down (item approach)* | | |

**Check:** Dr 1,560 = Cr 1,560. **Balanced.**

(2) Holding loss alternative:

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 1,560 | |
| Allowance to Reduce Inventory to Market | | 1,560 |
| *Separate holding loss presentation* | | |

**Check:** Dr 1,560 = Cr 1,560. **Balanced.**

Inventory, net = \(29{,}500 - 1{,}560 =\) **$27,940**.  
COGS after adjustment = \(512{,}000 + 1{,}560 =\) **$513,560**.

**(d) Subsequent measurement schedule**

| Year-end | Inventory cost | Designated market / LCM | Required allow. (Cr) | Unadjusted allow. (Cr) | Period-end adjustment |
|---|---:|---:|---:|---:|---|
| 12/31/Y1 | $29,500 | **$27,940** | **$1,560** | $0 | **Cr $1,560** |
| 12/31/Y2 | 33,000 | **29,400** | **3,600** | 1,560 | **Cr $2,040** |
| 12/31/Y3 | 21,200 | **20,000** | **1,200** | 3,600 | **Dr $2,400** |

**Rollforward:** \(1{,}560 + 2{,}040 = 3{,}600\); \(3{,}600 - 2{,}400 = 1{,}200\); sale closes \(1{,}200 → 0\).

**(e) Period-end adjusting JEs — Years 2 and 3**

**December 31, Year 2**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 2,040 | |
| Allowance to Reduce Inventory to Market | | 2,040 |
| *Period-end only: top up allowance to required LCM* | | |

**Check:** Dr 2,040 = Cr 2,040. **Balanced.** Ending allowance **$3,600**.

**December 31, Year 3**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 2,400 | |
| Cost of Goods Sold | | 2,400 |
| *Period-end only: reduce allowance to Year 3 required balance* | | |

**Check:** Dr 2,400 = Cr 2,400. **Balanced.** Ending allowance **$1,200**.

**(f) May 3, Year 4 — disposal and allowance close-out**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 20,800 | |
| Sales Revenue | | 20,800 |
| *Cash sale of remaining inventory* | | |

**Check:** Dr 20,800 = Cr 20,800. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 21,200 | |
| Inventory | | 21,200 |
| *Remove inventory at LIFO cost* | | |

**Check:** Dr 21,200 = Cr 21,200. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 1,200 | |
| Cost of Goods Sold | | 1,200 |
| *Close allowance into COGS* | | |

**Check:** Dr 1,200 = Cr 1,200. **Balanced.**

Net COGS = \(21{,}200 - 1{,}200 =\) **$20,000**.  
Gross profit = \(20{,}800 - 20{,}000 =\) **$800**.

**Key insight:** Changing every input amount does not change the LCM process: determine constrained market per item, compare to cost, and **true the allowance only at period-end** so net inventory always equals current LCM.

---

### Q3 — CORE alternate angle — Period-end LCM JE focus: ceiling/floor edge cases, COGS vs holding loss, two-year allowance true-up

**LO:** LO 10-2  
**Concept:** **Period-end adjusting JE emphasis** — compute designated market from ceiling/floor/RC edge cases; record Year 1 write-down two ways; Year 2 allowance true-up after full turnover of prior layer; BS/IS presentation  
**Scenario:**  
**Aspen Forge Tools Inc.** measures inventory with **LIFO** and applies **LCM by individual item**. It uses an **Allowance to Reduce Inventory to Market** and adjusts the allowance **only at December 31**. All beginning inventory each year is sold by year-end (the prior allowance remains until the year-end true-up).

**December 31, Year 1 — ending inventory (totals already aggregated by item line):**

| Item | LIFO cost | Est. selling price | Cost to complete & sell | Normal profit margin | Replacement cost |
|---|---:|---:|---:|---:|---:|
| Edger line | $26,000 | $30,000 | $3,000 | $3,000 | $16,000 |
| Clipper line | 50,000 | 90,000 | 28,000 | 18,000 | 36,000 |
| Blade Set line | 15,500 | 18,000 | 1,000 | 2,000 | 14,200 |
| **Total** | **$91,500** | | | | |

Pre-adjustment COGS for Year 1: **$210,000**. Allowance balance before Year 1 adjustment: **$0**.

**December 31, Year 2:** All Year 1 ending inventory was sold during Year 2. Year 2 ending inventory LIFO cost is **$70,000**; designated market (already constrained) is **$66,000**. The unadjusted allowance still carries the **Year 1 credit balance** until the Year 2 period-end entry.

**Required:**  
(a) For each item at December 31, Year 1, compute ceiling, floor, designated market, LCM carrying amount, and write-down. Sum to the required allowance.  
(b) Prepare the **December 31, Year 1 period-end adjusting JE** charging **COGS**.  
(c) Prepare the alternative **December 31, Year 1** entry charging **Holding Loss on Inventory**.  
(d) Show Year 1 **balance sheet** inventory presentation and **income statement** impact under both (b) and (c).  
(e) Compute the **December 31, Year 2** required allowance and the period-end adjustment; record the **Year 2 period-end adjusting JE** through COGS.  
(f) Briefly explain why LCM (not LCNRV) applies to Aspen Forge.

**Answer key:**

**(a) Market determination and LCM — December 31, Year 1**

| Item | Ceiling | Floor | RC | Designated market | Cost | LCM | Write-down |
|---|---:|---:|---:|---:|---:|---:|---:|
| Edger line | 27,000 | 24,000 | 16,000 | **24,000** (floor; RC below floor) | 26,000 | **24,000** | **2,000** |
| Clipper line | 62,000 | 44,000 | 36,000 | **44,000** (floor; RC below floor) | 50,000 | **44,000** | **6,000** |
| Blade Set line | 17,000 | 15,000 | 14,200 | **15,000** (floor; RC below floor) | 15,500 | **15,000** | **500** |
| **Totals** | | | | | **91,500** | **83,000** | **8,500** |

Required allowance Year 1 = \(91{,}500 - 83{,}000 =\) **$8,500**.

**(b) December 31, Year 1 — period-end JE via COGS (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 8,500 | |
| Allowance to Reduce Inventory to Market | | 8,500 |
| *Period-end only: establish LCM allowance (item approach)* | | |

**Check:** Dr 8,500 = Cr 8,500. **Balanced.**

**(c) December 31, Year 1 — alternative period-end JE via Holding Loss**

| Account | Debit | Credit |
|---|---:|---:|
| Holding Loss on Inventory | 8,500 | |
| Allowance to Reduce Inventory to Market | | 8,500 |
| *Period-end only: separate holding loss presentation* | | |

**Check:** Dr 8,500 = Cr 8,500. **Balanced.**

**(d) Year 1 financial statement presentation**

| | (b) COGS method | (c) Holding loss method |
|---|---:|---:|
| **Balance sheet — Dec 31, Year 1** | | |
| Inventory (at cost) | $91,500 | $91,500 |
| Allowance to reduce inventory to market | (8,500) | (8,500) |
| **Inventory, net** | **$83,000** | **$83,000** |
| **Income statement — Year 1** | | |
| Cost of goods sold | **$218,500** | $210,000 |
| Holding loss on inventory | 0 | **$8,500** |

Both methods reduce equity by **$8,500** and assets by **$8,500**; only the income-statement line differs.

**(e) December 31, Year 2 — period-end allowance true-up (emphasis)**

Required allowance Y2 = \(70{,}000 - 66{,}000 =\) **$4,000** credit.  
Unadjusted allowance = **$8,500** credit (Y1 balance still on books).  
Adjustment needed = \(8{,}500 - 4{,}000 =\) **$4,500** debit (reduce allowance / reduce COGS).

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to Market | 4,500 | |
| Cost of Goods Sold | | 4,500 |
| *Period-end only: true allowance to Year 2 required LCM after prior layer sold* | | |

**Check:** Dr 4,500 = Cr 4,500. **Balanced.** Ending allowance **$4,000** credit.  
Inventory, net Y2 = \(70{,}000 - 4{,}000 =\) **$66,000**.

**(f) Why LCM applies**  
Aspen Forge measures cost with **LIFO**. Under ASC 330, LIFO (and retail) inventory is remeasured using **lower of cost or market** (LO 10-2), not lower of cost or NRV (LO 10-1, which applies to FIFO/average cost and other non-LIFO, non-retail methods).

**Key insight:** The **period-end adjusting entry** does not recompute a “new write-down from zero” each year if an allowance already exists—it sets the allowance to the **currently required** credit balance. When a prior layer has been sold but its reserve remains, the true-up can **reduce** COGS (debit allowance).

---

### Q4 — MC (classification / method choice)

**LO:** LO 10-2  
**Concept:** Classification of LCM vs LCNRV by inventory cost method; designation of market when replacement cost is outside the ceiling–floor band  

**Question 1:**  
Which inventory cost methods require application of the **lower of cost or market** rule (with market defined as replacement cost constrained by ceiling and floor)?

- A) FIFO only  
- B) Average cost only  
- C) LIFO and the retail inventory method  
- D) Any method other than LIFO or retail  

**Answer:** C.  
LCM (LO 10-2) applies when cost is measured using **LIFO** or the **retail inventory method**. Methods other than LIFO or retail (e.g., FIFO, average cost) use **lower of cost or net realizable value** (LO 10-1).

---

**LO:** LO 10-2  
**Concept:** Designated market = middle of replacement cost, ceiling, and floor  

**Question 2:**  
For an LIFO inventory item, estimated selling price is $90, costs to complete and sell are $15, normal profit margin is $12, replacement cost is $50, and LIFO cost is $72. What is **designated market**, and what LCM unit value is reported?

- A) Market $75; LCM $72  
- B) Market $63; LCM $63  
- C) Market $50; LCM $50  
- D) Market $63; LCM $72  

**Answer:** B.  
Ceiling (NRV) = \(90 - 15 = 75\).  
Floor = \(75 - 12 = 63\).  
RC = 50 is **below the floor**, so designated market = **floor $63**.  
LCM = lower of cost $72 and market $63 = **$63**.  
(Option C incorrectly uses unconstrained RC; option A confuses ceiling with market; option D fails to write down when market < cost.)

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (ceilings, floors, middle-value market, write-downs, allowance rollforwards, net COGS)
- [x] Core demo not sidebar-only (Demo 10-2 path: LCM for LIFO/retail; market = RC with ceiling/floor; period-end allowance JEs)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook demo figures)
