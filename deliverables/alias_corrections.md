# Alias corrections applied

Three corrections to `alias_applied.md`, all applied to `question-verifier/pack/account_aliases.csv`.

## 1. Notation purge

Removed **2** notation rows from the alias file:

- `Retained Earnings (or Dividends)`
- `Retained Earnings (or Cash Dividends—Preferred)`

Their case-normalisation moves to the acceptable-form handler. The tokenizer gained a `NOTATION` classification, so these strings now pollute neither the chart nor the flag count — a string naming two permissible accounts can never resolve against a chart, so counting it as UNKNOWN_ACCOUNT was counting an unsatisfiable condition.

| | |
|---|---:|
| Lines classified `NOTATION` | **129** |
| `UNKNOWN_ACCOUNT` before | 938 |
| `UNKNOWN_ACCOUNT` after | **925** |

## 2. Paid-in-Capital family — one ruling

Canonical: **`Paid-in Capital in Excess of Par—Common Stock`** (139 occurrences) under the dominance rule; `—Common` (8) aliases to it.

Variants folded in:

- `Additional Paid-in Capital`
- `Paid-In Capital in Excess of Par—Common`
- `Paid-in Capital in Excess of Par - Common`
- `Paid-in Capital in Excess of Par—Common`
- `Share Premium`

**Bare form ruled DISTINCT**, not folded:

- `Paid-In Capital in Excess of Par`
- `Paid-in Capital in Excess of Par`

> DISTINCT - no security named, so the account is context-dependent per entry; matcher must not fold it into the Common Stock row.

`In`/`in` casing normalised to one style across all canonicals (audit: none remaining non-uniform).

## 3. Canonical style

Canonicals are uniform **title case regardless of which spelling was most frequent**. `Loss on bond retirement` → **`Loss on Bond Retirement`**, fold direction flipped so the lower-cased spelling is now the variant.

Canonical dedup after re-casing: 57 → **54** rows (three pairs collapsed to the same canonical once cased uniformly).

