# Standards-Vintage Note — ACCOUNT-343 Chapter 17, "Accounting for Leases"

**Pack field:** `standard_context` (attach verbatim to every ch. 17 item)
**Regime:** ASC 842 only — current vintage, no legacy content
**Source of record:** `chapter_17_clean.txt` (textbook, INT 4e), `CH 17 Handout - Accounting for Leases.docx.extracted.md`, `CH 17 Class Exercises.docx.extracted.md`, all under
`<local course-files directory — see paths.textbook in config.yaml>`
**Line cites** below are line numbers in `chapter_17_clean.txt` (8,866 lines).

---

## 0. Verdict on regime — ASC 842, zero ASC 840 content

Mechanical scan of the chapter text (re-run and confirmed):

| probe | hits |
|---|---:|
| `840` | 0 |
| `capital lease` | 0 |
| `IFRS` | 0 |
| `common control` | 0 |
| `risk-free` | 0 |
| `transition` | 0 |
| `effective date` | 0 |

Every codification cite in the chapter is an 842-series paragraph (842-10, 842-20, 842-30, 842-40).

> "[ASC 842-20-25-1] At the commencement date, a lessee shall recognize a right-of-use asset and a lease liability."
> — line 308

The settling passage that puts **both** lease classes on the balance sheet:

> "With an operating lease, a lease liability and a right-of-use asset are initially recognized on the balance sheet **in the same way as a finance lease**."
> — Demo 17-3, part (b)

Handout, same point in plain language:

> "Regardless of whether the lease is classified as a finance or operating lease, all long-term leases are capitalized. The right to use the asset in the lease is an asset called right-of-use asset (ROU asset). The obligation to pay the lease payments is a liability called lease liability."
> — CH 17 Handout, closing line of LO 17-1

**Hard rules for keys and solvers alike.** Never write "Capital Lease." Never leave a long-term operating lease off the balance sheet. Never book a long-term operating lease as a `Rent Expense / Cash` one-liner.

---

## 1. Account names this edition actually uses

| Concept | This edition's account name |
|---|---|
| Leased asset (both classes) | **Right-of-Use Asset** |
| Lease obligation (both classes) | **Lease Liability** |
| Operating-lease P&L | **Lease Expense** (single line) |
| Finance-lease P&L | **Interest Expense** + **Amortization Expense** (two lines) |
| Short-term election P&L | **Lease Expense (Short-Term)** |
| Pre-commencement broker/legal cost | **Initial Direct Cost** (asset; reclassed at commencement) |
| Pre-commencement incentive received | **Lease Incentive Liability** (reclassed at commencement) |
| Pre-commencement payment made | **Prepaid Lease Payment** (reclassed at commencement) |
| Recognized sale-leaseback gain | **Gain on Sale-Leaseback** |
| Failed sale | **Note Payable** (financing, no sale recognized) |

Two conventions to copy **exactly**:

1. **Accrued interest on a finance lease is credited to Lease Liability, not Interest Payable.**
   > "December 31, Year 1—To record interest expense / Interest Expense — 3,251 / Lease Liability — 3,251"
   > — Demo 17-2 part (d), lines 493–495

2. **Amortization is credited directly to the ROU asset; no contra account.**
   > "*The company chooses to credit the right-of-use asset directly for the amortization expense instead of crediting an accumulated amortization account, **as we see in all examples in this chapter**."
   > — Demo 17-2, footnote to part (d), lines 499–500

---

## 2. Measurement at commencement (identical for both classes)

**Lease Liability** = PV of lease payments, discounted at the rate implicit in the lease if readily determinable, otherwise the lessee's incremental borrowing rate.

> "842-20-30-3 A lessee should use the rate implicit in the lease whenever that rate is readily determinable." — LO 17-1
> "The solution remains unchanged as the lessee will use the lessor's implicit rate when known, even if it differs from its incremental borrowing rate." — Demo 17-2 part (i), line 590

**ROU Asset** = lease liability − lease incentives received + initial direct costs incurred.

> "Calculate Right-of-Use Asset / Initial measurement of lease liability − Subtract lease incentive received + Add initial direct cost incurred / Right-of-use asset" — LO 17-4 boxed formula, line 1052

> "[ASC 842-20-30-5] At the commencement date, the cost of the right-of-use asset shall consist of all of the following: a. The amount of the initial measurement of the lease liability b. Any lease payments made to the lessor at or before the commencement date, minus any lease incentives received c. Any initial direct costs incurred by the lessee" — line 1055

**Three measurement traps the edition flags explicitly** (LO 17-4, line 1052; Exhibit 17-3, line ~1830):

- Lease incentives **reduce fixed payments for the 90% classification test** but **do not** reduce the initial lease liability.
- **100% of a guaranteed residual** enters the 90% test; only the **probable amount owed** (GRV − expected residual, floored at zero) enters the lease liability. Handout table: GRV 100,000 / expected RV 95,000 → probable amount owed 5,000.
- **Unguaranteed residual is excluded from both.** Purchase option / termination penalty reasonably certain of exercise is **included in both**.

**Amortization period.** Lease term, unless title transfers or a purchase option is reasonably certain of exercise — then the underlying asset's useful life.

> "842-20-35-8 … if the lease transfers ownership of the underlying asset to the lessee or the lessee is reasonably certain to exercise an option to purchase the underlying asset, the lessee shall amortize the right-of-use asset to the end of the useful life of the underlying asset." — line 1055

**Remeasurement.** Adjust the ROU asset; update the discount rate unless one of the three 842-20-35-5 exceptions applies.

> "[ASC 842-20-35-4] … A lessee shall recognize the amount of the remeasurement of the lease liability as an adjustment to the right-of-use asset" — line 4201
> Demo 17-11 Example Three: "January 1, Year 3—To remeasure lease liability / Right-of-Use Asset — 129,338 / Lease Liability — 129,338" — line ~4258

---

## 3. Divergence from current guidance

**None found.** This is a current-vintage ASC 842 chapter, not a legacy text. There is no capital/operating split, no 840 language, and no "old rules" sidebar to reconcile. There is nothing to warn a student about.

**Do not import from general GAAP — the chapter is SILENT on:**

- ASU 2023-01 common-control arrangements and common-control leasehold-improvement amortization (`common control` → 0 hits). The chapter states only the plain rule: *"842-20-35-12 Leasehold improvements — shall be amortized over the shorter of the useful life of those leasehold improvements and the remaining lease term…"* (line 1055).
- The risk-free-rate discount election for non-public business entities, ASU 2021-09 (`risk-free`, `nonpublic`, `private company` → 0 hits each).
- Transition, effective dates, comparative-period presentation (0 hits).
- IFRS 16 / single-model lessee accounting (0 hits).

---

## 4. Internal quirks — follow the demo, not the caption

These are textbook-vs-textbook, not standard-vs-standard. A key that follows them is correct; a solver that "corrects" them is wrong.

1. **Final-year operating entry is mis-captioned.** The caption reads *"To record amortization on right-of-use asset"* but the **debit is Lease Expense**:
   > "December 31, Year 3—To record amortization on right-of-use asset / Lease Expense — 34,972 / Right-of-Use Asset — 34,972" — Demo 17-3 part (h), lines 948–953 (same pattern at Demo 17-5 part (i))

   Debit **Lease Expense**. Never `Amortization Expense` in an operating lease.

2. **Two acceptable forms of the operating year-end entry.** The compound form and the two-part form are the same entry; the chapter presents both and calls neither preferred:
   > "An option is to record Dec. 31 entry in two parts. / Right-of-Use Asset — 3,251 / Lease Liability — 3,251 / Lease Expense — 34,972 / Right-of-Use Asset — 34,972" — line ~890

   A comparator must net/canonicalize before flagging a form difference.

3. **Short-term lease wording.** LO 17-9 margin box says *"a duration of one year or less"* and the body says *"reasonably expected to exercise"*; the quoted ASC Glossary says *"a lease term of 12 months or less"* and *"reasonably certain to exercise."* Same rule. **Use the glossary wording** when authoring.

4. **ROU balance-sheet classification flips.** "Noncurrent assets" in Year 1, "Current assets" in the final year (Demos 17-3 and 17-5). Mirror the edition if a problem asks for a balance sheet.

---

## 5. Rounding — the edition has no single convention, and says so

This is the one place ch. 17 items reliably diverge without either side being wrong.

> "Note: Amounts adjusted to whole numbers to simplify recording of journal entries that follow. If we prepare this schedule in Excel with unlimited decimals, the numbers slightly vary."
> — lines 1545–1547, repeated at 3283–3284

Standing rounding footnotes elsewhere in the chapter: line 584 (*"Amount adjusted due to rounding"* on `Amortization Expense 33,334` for `$100,000/3`), line 1544 (*"Amount rounded"*), line 7986 (*"Amounts rounded to the dollar"*), line 8083 (*"Amounts in schedule are rounded"*), lines 805 and 2567 (*"Certain amounts adjusted for rounding differences"*).

The edition's house style for journal entries is **whole dollars, round the straight-line charge first, carry the rounded charge, and let the final period absorb the difference**. Its PV computations, however, are Excel `=PV(...)` calls carrying cents. Both appear in the same demo.

**Consequence for the pack:** a ch. 17 item that does not state a rounding convention will produce a defensible key and a defensible solver answer that differ by cents to a few dollars on carrying amounts. That is a **question defect, not an answer defect**. Every ch. 17 Class A stem must carry an explicit line such as:

> "Round the commencement PV and all schedule amounts to the nearest dollar; plug the final period's interest so the lease liability clears exactly."

(Item `agent_285#00` already does this and produced no numeric divergence. Items `agent_151#01` and `agent_283#02` do not, and produced $0.86 / $1.35 and $0.65 divergences respectively.)

---

## 6. Coverage scope for this course

Per the handout's LO/page table, **LO 17-1, 17-2, 17-3, 17-4, 17-5, 17-9, 17-12 are "Covered? = Yes."** All lessor LOs (17-6, 17-7, 17-8, 17-10) and modifications (17-11) are **"No."**

> "we are going to be focusing exclusively on lessees. This is because lessee accounting is on FAR…" — CH 17 Handout

Authoring implication: lessor-side entries (Lease Receivable, Sales-Type/Direct Financing, Unearned Interest Revenue) are **out of scope**. LO 17-11 remeasurement mechanics appear in the corpus (e.g. `agent_151#01`) and are defensible as an extension, but should be tagged out-of-scope rather than treated as core.
