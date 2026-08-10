# Agent 314 — CORE DEMO — LO 9-5

**Chapter:** 9  
**LO title:** Demonstrate moving average, FIFO, and LIFO in a perpetual inventory system  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Perpetual inventory system:** Inventory and COGS updated at **each** purchase and **each** sale; physical count still required to verify books
- **Moving average (perpetual):** recompute unit cost after **every purchase**; apply latest average to subsequent sales and to ending inventory
- **FIFO (perpetual):** assign **earliest** remaining cost layers to each sale; EI = most recent layers (same EI/COGS as periodic FIFO)
- **LIFO (perpetual):** assign **latest** remaining layers **as of each sale date** to COGS; EI tends to keep older layers (generally **differs** from periodic LIFO)
- **Subsequent measurement schedule:** perpetual inventory card (purchases / cost of sales / balance) after every transaction
- **Initial recognition JE:** Dr Inventory / Cr Accounts Payable (or Cash) at invoice cost — identical under all three cost-flow methods
- **Disposal / settlement JE:** at sale — Dr AR (or Cash) / Cr Sales; Dr COGS / Cr Inventory at method-assigned cost
- **Period-end adjusting JE (emphasis):** physical count vs perpetual books → Loss (Gain) on Inventory Shortage (Overage) and Inventory; shortage amount assigned using the same cost-flow rule as sales; shortage typically closed into COGS on the income statement
- Rising-cost ranking (typical): EI FIFO ≥ MA ≥ LIFO; COGS LIFO ≥ MA ≥ FIFO

---

### Q1 — CORE — Silverpeak Trailware: perpetual MA / FIFO / LIFO schedules, purchase & sale JEs, period-end shortage (emphasis)

**LO:** LO 9-5  
**Concept:** Subsequent measurement schedules under moving average, FIFO, and LIFO (perpetual); initial purchase recognition; sale/COGS settlement; **period-end inventory shortage adjusting JEs** (emphasis)  
**Scenario:**  
**Silverpeak Trailware Co.** sells a single SKU of trail daypacks and maintains a **perpetual** inventory system. Purchases are recorded on account under the **gross method**. Unit selling prices are given below. Costs rose during June. At month-end, a physical count is taken and books are adjusted.

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| June 1 | Beginning inventory | 200 | $15 cost |
| June 5 | Purchase on account | 300 | $18 cost |
| June 10 | Credit sale | 250 | $40 selling price |
| June 18 | Purchase on account | 250 | $20 cost |
| June 24 | Credit sale | 200 | $42 selling price |
| June 30 | Physical count | **280** units on hand | — |

Book quantity before the physical count: \(200 + 300 - 250 + 250 - 200 = \mathbf{300}\) units. Shortage = \(300 - 280 = \mathbf{20}\) units.  
Apply each cost-flow method consistently to sales **and** to the period-end shortage (units removed from inventory under that method’s “out” rule). No purchase returns, discounts, or freight-in.

**Required:**  
(a) Prepare a **perpetual inventory cost schedule** under the **moving average** method. Compute June **ending inventory (book, before physical)** and **COGS from sales**.  
(b) Prepare a **perpetual inventory cost schedule** under **FIFO**. Compute book EI and COGS from sales.  
(c) Prepare a **perpetual inventory cost schedule** under **LIFO**. Compute book EI and COGS from sales.  
(d) **Initial recognition:** journal entries for the two **purchases** (perpetual, gross method, on account).  
(e) **Disposal / settlement:** sales revenue and COGS journal entries for June 10 and June 24 **under the moving average** method.  
(f) **Period-end adjusting JEs (emphasis):** for **each** of MA, FIFO, and LIFO, compute the **dollar amount of the 20-unit shortage** and record the June 30 adjusting entry. State adjusted EI and total COGS including shortage for each method.  
(g) Verify COGAS − adjusted EI = total COGS (sales + shortage) for all three methods. Rank methods by highest **adjusted ending inventory** and highest **total COGS**.

**Answer key:**

**Cost of goods available for sale (all methods)**  
Beginning inventory: \(200 \times \$15 = \$3{,}000\)  
Purchases: \(300\times\$18 + 250\times\$20 = \$5{,}400 + \$5{,}000 = \$10{,}400\)  
**COGAS = \$3,000 + \$10,400 = \$13,400**  
Units available \(200+300+250=750\); units sold \(250+200=450\); book EI units = 300; physical EI units = 280.

**(a) Moving average — perpetual (subsequent measurement schedule)**

| Date | Purchases (u × $) | COGS (u × $) | Inventory balance |
|---|---|---|---|
| June 1 | | | 200 × $15 = **$3,000** |
| June 5 | 300 × $18 = $5,400 | | 500 × **$16.80** = **$8,400** *(3,000+5,400)/500* |
| June 10 | | 250 × $16.80 = **$4,200** | 250 × $16.80 = **$4,200** |
| June 18 | 250 × $20 = $5,000 | | 500 × **$18.40** = **$9,200** *(4,200+5,000)/500* |
| June 24 | | 200 × $18.40 = **$3,680** | 300 × $18.40 = **$5,520** |

**Moving average — book (before physical):** Ending inventory = **$5,520**; COGS from sales = \(4{,}200 + 3{,}680 = \mathbf{\$7{,}880}\)

**(b) FIFO — perpetual**

| Date | Purchases | COGS (layers) | Inventory layers |
|---|---|---|---|
| June 1 | | | 200 @ $15 = $3,000 |
| June 5 | 300 @ $18 = $5,400 | | 200 @ $15; 300 @ $18 |
| June 10 | | 200 @ $15 + 50 @ $18 = **$3,900** | 250 @ $18 = $4,500 |
| June 18 | 250 @ $20 = $5,000 | | 250 @ $18; 250 @ $20 |
| June 24 | | 200 @ $18 = **$3,600** | 50 @ $18 + 250 @ $20 = $5,900 |

**FIFO — book:** EI = \(50\times\$18 + 250\times\$20 = \$900 + \$5{,}000 = \mathbf{\$5{,}900}\); COGS from sales = \(3{,}900 + 3{,}600 = \mathbf{\$7{,}500}\)

**(c) LIFO — perpetual**

| Date | Purchases | COGS (layers) | Inventory layers |
|---|---|---|---|
| June 1 | | | 200 @ $15 = $3,000 |
| June 5 | 300 @ $18 = $5,400 | | 200 @ $15; 300 @ $18 |
| June 10 | | 250 @ $18 = **$4,500** | 200 @ $15 + 50 @ $18 = $3,900 |
| June 18 | 250 @ $20 = $5,000 | | 200 @ $15; 50 @ $18; 250 @ $20 |
| June 24 | | 200 @ $20 = **$4,000** | 200 @ $15 + 50 @ $18 + 50 @ $20 = $4,900 |

**LIFO — book:** EI = \(200\times\$15 + 50\times\$18 + 50\times\$20 = \$3{,}000 + \$900 + \$1{,}000 = \mathbf{\$4{,}900}\); COGS from sales = \(4{,}500 + 4{,}000 = \mathbf{\$8{,}500}\)

**(d) Initial recognition — purchase JEs (same under all three cost-flow methods; perpetual gross)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| June 5 | Inventory | 5,400 | |
| | Accounts Payable | | 5,400 |
| | *Purchase 300 units @ $18 on account* | | |
| June 18 | Inventory | 5,000 | |
| | Accounts Payable | | 5,000 |
| | *Purchase 250 units @ $20 on account* | | |

**Check:** Each entry Dr = Cr. **Balanced.**

**(e) Disposal / settlement — June sales under moving average (perpetual)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| June 10 | Accounts Receivable | 10,000 | |
| | Sales Revenue | | 10,000 |
| | *250 × $40* | | |
| June 10 | Cost of Goods Sold | 4,200 | |
| | Inventory | | 4,200 |
| | *250 × $16.80 moving average* | | |
| June 24 | Accounts Receivable | 8,400 | |
| | Sales Revenue | | 8,400 |
| | *200 × $42* | | |
| June 24 | Cost of Goods Sold | 3,680 | |
| | Inventory | | 3,680 |
| | *200 × $18.40 moving average* | | |

**Check:** Each compound pair balances (Dr = Cr). **Balanced.**

**(f) Period-end adjusting JEs — June 30 shortage of 20 units (emphasis)**

**Moving average:** latest average = $18.40 → shortage \(20 \times \$18.40 = \mathbf{\$368}\)

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 368 | |
| Inventory | | 368 |
| *Period-end only: true books to physical count (20 units @ $18.40 MA)* | | |

**Adjusted EI (MA)** = \(280 \times \$18.40 = \mathbf{\$5{,}152}\) (or \(5{,}520 - 368\)).  
**Total COGS including shortage** = \(7{,}880 + 368 = \mathbf{\$8{,}248}\).

**FIFO:** earliest remaining layer = 50 @ $18 → remove 20 @ $18 = **$360**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 360 | |
| Inventory | | 360 |
| *Period-end only: FIFO out-flow applied to shortage (20 @ $18)* | | |

**Adjusted EI (FIFO)** layers: \(30 \times \$18 + 250 \times \$20 = \$540 + \$5{,}000 = \mathbf{\$5{,}540}\).  
**Total COGS including shortage** = \(7{,}500 + 360 = \mathbf{\$7{,}860}\).

**LIFO:** latest remaining layer = 50 @ $20 → remove 20 @ $20 = **$400**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 400 | |
| Inventory | | 400 |
| *Period-end only: LIFO out-flow applied to shortage (20 @ $20)* | | |

**Adjusted EI (LIFO)** layers: \(200 \times \$15 + 50 \times \$18 + 30 \times \$20 = \$3{,}000 + \$900 + \$600 = \mathbf{\$4{,}500}\).  
**Total COGS including shortage** = \(8{,}500 + 400 = \mathbf{\$8{,}900}\).

**(g) Verification and ranking**

| Method | COGAS | Adjusted EI | Total COGS (sales + shortage) | Check |
|---|---:|---:|---:|---|
| Moving average | $13,400 | $5,152 | $8,248 | \(13{,}400 - 5{,}152 = 8{,}248\) ✓ |
| FIFO | $13,400 | $5,540 | $7,860 | \(13{,}400 - 5{,}540 = 7{,}860\) ✓ |
| LIFO | $13,400 | $4,500 | $8,900 | \(13{,}400 - 4{,}500 = 8{,}900\) ✓ |

**Rank (rising costs):** Adjusted EI: **FIFO $5,540 > MA $5,152 > LIFO $4,500**.  
Total COGS: **LIFO $8,900 > MA $8,248 > FIFO $7,860**.

**Key insight:** Under perpetual inventory, cost flow is applied **transaction by transaction** (MA re-average after each purchase; FIFO/LIFO layers at each sale). The **period-end adjusting JE** is still required: when physical count ≠ perpetual books, Inventory is reduced (or increased) and Loss (Gain) on Inventory Shortage (Overage) is recorded, with the shortage cost assigned under the **same** cost-flow assumption. Shortage is typically presented as part of cost of goods sold.

---

### Q2 — CORE number variant — Cedarline Sports Outfitters (all numbers changed)

**LO:** LO 9-5  
**Concept:** Number-variant twin — perpetual MA/FIFO/LIFO schedules; purchase recognition; LIFO sale settlement JEs; **period-end shortage adjusting JEs**  
**Scenario:**  
**Cedarline Sports Outfitters LLC** uses a **perpetual** inventory system for one SKU of climbing carabiners. Purchases are on account (gross method). Costs rose in August.

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Aug 1 | Beginning inventory | 500 | $12 cost |
| Aug 4 | Purchase on account | 500 | $16 cost |
| Aug 9 | Credit sale | 400 | $28 selling price |
| Aug 17 | Purchase on account | 400 | $18 cost |
| Aug 22 | Credit sale | 500 | $30 selling price |
| Aug 31 | Physical count | **470** units on hand | — |

Book quantity before physical: \(500 + 500 - 400 + 400 - 500 = \mathbf{500}\) units. Shortage = \(500 - 470 = \mathbf{30}\) units.  
Assign shortage under each method’s cost-flow rule. No returns, discounts, or freight.

**Required:**  
(a) Compute August **book ending inventory** and **COGS from sales** under (1) **moving average**, (2) **FIFO**, and (3) **LIFO** perpetual. Show the inventory balance (unit cost or layers) after each purchase and after each sale.  
(b) **Initial recognition:** journal entries for the two purchases.  
(c) **Disposal / settlement:** sales and COGS entries for Aug 9 and Aug 22 **under LIFO**.  
(d) **Period-end adjusting JEs (emphasis):** shortage amount and June 30-style Aug 31 entry under **each** method; report adjusted EI and total COGS (sales + shortage).  
(e) Prove COGAS − adjusted EI = total COGS for all three methods.

**Answer key:**

**COGAS**  
BI: \(500 \times \$12 = \$6{,}000\)  
Purchases: \(500\times\$16 + 400\times\$18 = \$8{,}000 + \$7{,}200 = \$15{,}200\)  
**COGAS = \$6,000 + \$15,200 = \$21,200**

**(a) Schedules**

**Moving average**

| Date | Event | Balance |
|---|---|---|
| Aug 1 | BI | 500 × $12 = $6,000 |
| Aug 4 | +500 @ $16 = $8,000 | 1,000 × **$14.00** = **$14,000** *(6,000+8,000)/1,000* |
| Aug 9 | Sale 400 × $14.00 = **$5,600** | 600 × $14.00 = $8,400 |
| Aug 17 | +400 @ $18 = $7,200 | 1,000 × **$15.60** = **$15,600** *(8,400+7,200)/1,000* |
| Aug 22 | Sale 500 × $15.60 = **$7,800** | 500 × $15.60 = **$7,800** |

**MA book EI = \$7,800; COGS from sales = \$5,600 + \$7,800 = \$13,400**

**FIFO**

| Date | COGS layers | Balance layers |
|---|---|---|
| Aug 1 | | 500 @ $12 |
| Aug 4 | | 500 @ $12; 500 @ $16 |
| Aug 9 | 400 @ $12 = **$4,800** | 100 @ $12; 500 @ $16 |
| Aug 17 | | 100 @ $12; 500 @ $16; 400 @ $18 |
| Aug 22 | 100 @ $12 + 400 @ $16 = **$7,600** | 100 @ $16 + 400 @ $18 = **$8,800** |

**FIFO book EI = \$8,800; COGS from sales = \$4,800 + \$7,600 = \$12,400**

**LIFO**

| Date | COGS layers | Balance layers |
|---|---|---|
| Aug 1 | | 500 @ $12 |
| Aug 4 | | 500 @ $12; 500 @ $16 |
| Aug 9 | 400 @ $16 = **$6,400** | 500 @ $12; 100 @ $16 |
| Aug 17 | | 500 @ $12; 100 @ $16; 400 @ $18 |
| Aug 22 | 400 @ $18 + 100 @ $16 = **$8,800** | 500 @ $12 = **$6,000** |

**LIFO book EI = \$6,000; COGS from sales = \$6,400 + \$8,800 = \$15,200**

**(b) Initial recognition — purchases**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Aug 4 | Inventory | 8,000 | |
| | Accounts Payable | | 8,000 |
| Aug 17 | Inventory | 7,200 | |
| | Accounts Payable | | 7,200 |

**Check:** Dr = Cr each entry. **Balanced.**

**(c) Disposal / settlement — sales under LIFO**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Aug 9 | Accounts Receivable | 11,200 | |
| | Sales Revenue | | 11,200 |
| | *400 × $28* | | |
| Aug 9 | Cost of Goods Sold | 6,400 | |
| | Inventory | | 6,400 |
| | *400 @ $16 (latest layer)* | | |
| Aug 22 | Accounts Receivable | 15,000 | |
| | Sales Revenue | | 15,000 |
| | *500 × $30* | | |
| Aug 22 | Cost of Goods Sold | 8,800 | |
| | Inventory | | 8,800 |
| | *400 @ $18 + 100 @ $16* | | |

**Check:** Each entry balances. **Balanced.**

**(d) Period-end adjusting JEs — Aug 31 shortage of 30 units (emphasis)**

| Method | Shortage cost assignment | Amount | Adjusted EI | Total COGS |
|---|---|---:|---:|---:|
| Moving average | 30 × $15.60 | **$468** | \(470 \times \$15.60 = \mathbf{\$7{,}332}\) | \(13{,}400 + 468 = \mathbf{\$13{,}868}\) |
| FIFO | 30 @ $16 (earliest remaining) | **$480** | \(70\times\$16 + 400\times\$18 = \mathbf{\$8{,}320}\) | \(12{,}400 + 480 = \mathbf{\$12{,}880}\) |
| LIFO | 30 @ $12 (only remaining layer) | **$360** | \(470 \times \$12 = \mathbf{\$5{,}640}\) | \(15{,}200 + 360 = \mathbf{\$15{,}560}\) |

**Journal entries (structure identical; amounts differ by method):**

| Method | Debit Loss on Inventory Shortage | Credit Inventory |
|---|---:|---:|
| Moving average | 468 | 468 |
| FIFO | 480 | 480 |
| LIFO | 360 | 360 |

*Period-end only: align perpetual Inventory to physical count under the cost-flow method in use.*

**Check:** Each JE Dr = Cr. **Balanced.**

**(e) COGAS proof**

| Method | COGAS | Adjusted EI | Total COGS | Check |
|---|---:|---:|---:|---|
| MA | $21,200 | $7,332 | $13,868 | \(21{,}200 - 7{,}332 = 13{,}868\) ✓ |
| FIFO | $21,200 | $8,320 | $12,880 | \(21{,}200 - 8{,}320 = 12{,}880\) ✓ |
| LIFO | $21,200 | $5,640 | $15,560 | \(21{,}200 - 5{,}640 = 15{,}560\) ✓ |

**Key insight:** Changing every unit cost and quantity still produces the same mechanics: recompute MA after purchases; peel FIFO/LIFO layers at each sale; then at **period-end** adjust Inventory for the physical shortage using that method’s out-flow rule. COGAS is method-independent; only the split between EI and COGS (including shortage) differs.

---

### Q3 — CORE alternate angle — Northbridge Power Tools: period-end shortage focus + FIFO identity vs LIFO difference

**LO:** LO 9-5  
**Concept:** Perpetual LIFO/MA/FIFO schedules; **period-end shortage adjusting JE as primary focus**; note that FIFO perpetual equals FIFO periodic while LIFO generally does not  
**Scenario:**  
**Northbridge Power Tools Inc.** tracks one SKU of replacement drill bits under a **perpetual** system. September activity (rising costs):

| Date | Transaction | Units | Unit cost |
|---|---|---:|---:|
| Sept 1 | Beginning inventory | 100 | $30 |
| Sept 8 | Purchase | 200 | $33 |
| Sept 12 | Sale | 150 | — |
| Sept 20 | Purchase | 100 | $36 |
| Sept 25 | Sale | 120 | — |
| Sept 30 | Physical count | **110** units | — |

Book quantity before physical: \(100 + 200 - 150 + 100 - 120 = \mathbf{130}\) units. Shortage = **20** units.  
Selling prices are not needed for this problem (focus on cost measurement and the period-end JE).

**Required:**  
(a) Compute book EI and COGS from sales under **moving average**, **FIFO**, and **LIFO** perpetual (show key layer/average steps).  
(b) For **each** method, compute the **period-end shortage cost**, record the **Sept 30 adjusting JE**, and state **adjusted EI** and **total COGS** (sales + shortage).  
(c) Briefly explain: (i) why the shortage entry is a **period-end** adjusting entry even though the system is perpetual; (ii) whether **FIFO** perpetual EI/COGS would equal FIFO **periodic** for the same data; (iii) whether **LIFO** perpetual would equal LIFO periodic.

**Answer key:**

**COGAS** = \(100\times\$30 + 200\times\$33 + 100\times\$36 = \$3{,}000 + \$6{,}600 + \$3{,}600 = \mathbf{\$13{,}200}\)

**(a) Book results before physical**

**Moving average**  
Sept 8: \((3{,}000 + 6{,}600)/300 = \$32.00\); sale 150 × $32 = **$4,800**; bal 150 × $32 = $4,800.  
Sept 20: \((4{,}800 + 3{,}600)/250 = \$33.60\); sale 120 × $33.60 = **$4,032**; bal 130 × $33.60 = **$4,368**.  
**MA book EI = \$4,368; COGS sales = \$8,832**

**FIFO**  
Sept 12 sale: \(100\times\$30 + 50\times\$33 = \$3{,}000 + \$1{,}650 = \mathbf{\$4{,}650}\); bal 150 @ $33.  
Sept 25 sale: \(120\times\$33 = \mathbf{\$3{,}960}\); bal \(30\times\$33 + 100\times\$36 = \$990 + \$3{,}600 = \mathbf{\$4{,}590}\).  
**FIFO book EI = \$4,590; COGS sales = \$8,610**

**LIFO**  
Sept 12 sale: \(150\times\$33 = \mathbf{\$4{,}950}\); bal \(100\times\$30 + 50\times\$33 = \$3{,}000 + \$1{,}650 = \$4{,}650\).  
Sept 25 sale: \(100\times\$36 + 20\times\$33 = \$3{,}600 + \$660 = \mathbf{\$4{,}260}\); bal \(100\times\$30 + 30\times\$33 = \$3{,}000 + \$990 = \mathbf{\$3{,}990}\).  
**LIFO book EI = \$3,990; COGS sales = \$9,210**

**(b) Period-end adjusting JEs — Sept 30 (emphasis)**

| Method | Shortage assignment | Amount | JE (Dr Loss / Cr Inventory) | Adjusted EI | Total COGS |
|---|---|---:|---|---:|---:|
| MA | 20 × $33.60 | **$672** | Dr Loss 672 / Cr Inventory 672 | **$3,696** | **$9,504** |
| FIFO | 20 @ $33 (earliest remaining) | **$660** | Dr Loss 660 / Cr Inventory 660 | **$3,930** | **$9,270** |
| LIFO | 20 @ $33 (latest remaining partial layer) | **$660** | Dr Loss 660 / Cr Inventory 660 | **$3,330** | **$9,870** |

**Expanded JEs (all balance):**

*Moving average — Sept 30*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 672 | |
| Inventory | | 672 |

*FIFO — Sept 30*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 660 | |
| Inventory | | 660 |

*LIFO — Sept 30*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Inventory Shortage | 660 | |
| Inventory | | 660 |

**Proofs:**  
MA: \(13{,}200 - 3{,}696 = 9{,}504\) ✓  
FIFO: \(13{,}200 - 3{,}930 = 9{,}270\) ✓  
LIFO: \(13{,}200 - 3{,}330 = 9{,}870\) ✓  
(Adjusted FIFO layers: \(10\times\$33 + 100\times\$36 = \$330 + \$3{,}600 = \$3{,}930\); LIFO: \(100\times\$30 + 10\times\$33 = \$3{,}000 + \$330 = \$3{,}330\).)

**(c) Conceptual**  
(i) Perpetual records track **known** purchases and sales continuously, but **theft, spoilage, and errors** are not recorded as they occur. The physical count **verifies** books; any difference is adjusted **at period-end** (or when the count is taken) so Inventory on the balance sheet equals goods actually on hand.  
(ii) **FIFO perpetual = FIFO periodic** for EI and COGS: the same earliest costs are always assigned to goods sold whether layered continually or only at period-end.  
(iii) **LIFO perpetual generally ≠ LIFO periodic**: “latest” costs for a mid-period sale are the latest purchases **as of that sale date**, not the latest purchases of the **entire** period. Periodic LIFO would assign September’s last purchases first to all units sold for the month.

**Key insight:** LO 9-5’s exam core is the perpetual **cost schedule**, but the **period-end adjusting JE** completes the measurement cycle: after continuous cost assignment, true-up Inventory for the physical count under the same cost-flow assumption. FIFO’s identity across systems is a classic contrast with LIFO’s system-dependent results.

---

### Q4 — MC (method / classification)

**LO:** LO 9-5  
**Concept:** Classification of when the perpetual moving-average unit cost is updated; which method yields identical perpetual vs periodic results  

**Question 1:**  
Under the **moving average** method in a **perpetual** inventory system, a new unit cost is computed:  
- A) Only at period-end, as total COGAS ÷ total units available  
- B) After **each purchase**, as total inventory cost ÷ units on hand  
- C) After **each sale**, by dividing remaining cost by units sold that day  
- D) Only when a physical inventory count is taken  

**Answer:** **B.** Perpetual moving average recalculates unit cost after **each purchase** by dividing total inventory cost by total units on hand; that average is applied to sales until the next purchase. A describes **periodic weighted-average** cost; C and D are incorrect.

**Question 2:**  
Which cost-flow method produces the **same** ending inventory and COGS whether applied in a **perpetual** or **periodic** system (assuming the same data and no mid-period complications other than the timing of cost assignment)?  
- A) LIFO only  
- B) Moving average only  
- C) FIFO only  
- D) Both LIFO and moving average  

**Answer:** **C.** FIFO assigns earliest costs to COGS whether layered continually or at period-end, so results match. LIFO and moving average (vs periodic weighted average) generally differ between perpetual and periodic applications.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (COGAS − EI = COGS for all methods; shortage roll-forwards)
- [x] Core demo not sidebar-only (Demo 9-5A/B/C perpetual MA/FIFO/LIFO path)
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Emphasis angle covered: period_end_adjusting_JE (shortage under each method in Q1–Q3)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Original companies/numbers (not textbook Chase/CostKo/Robin demos)
