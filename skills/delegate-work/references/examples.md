# Delegation examples

These examples are illustrative. Paths, commands, and results are invented to show decisions and return formats; they are not reports of executed work or measured improvements.

## 1. Split independent questions, not overlapping edits

**Poor assignment**

```text
Worker A: Fix the parser in src/parser.ts.
Worker B: Improve the same parser in src/parser.ts.
```

Both workers can change the same behavior and overwrite each other's edits. Different wording does not make their work independent.

**Better assignment**

```text
Worker A: Read-only. Reproduce the reported empty-input failure using the
existing parser tests. Return the smallest input and observed behavior.

Worker B: Read-only. Inspect the parser's public contract and callers for
empty-input expectations. Return file/line evidence and conflicting uses.

Parent: Combine the findings, choose the behavior, and own the implementation.
```

The investigations can run together. The edit follows the findings and has one owner.

## 2. Sequence dependencies and keep one shared-file writer

**Poor assignment**

```text
Worker A: Design the export result and update src/export.ts.
Worker B: Implement the UI against whatever export result seems appropriate.
Both: Update src/types.ts as needed.
```

The UI depends on an unsettled contract, and both workers own the shared type file.

**Better assignment**

```text
First: Settle the export result fields and error contract from the approved
requirements. The parent owns src/types.ts and publishes the agreed contract.

Then, in parallel:
Worker A owns src/export.ts and its existing test file; preserve the contract.
Worker B owns src/export-panel.tsx and its existing test file; use that contract.

Workers report proposed type changes to the parent instead of editing src/types.ts.
Parent integrates both results and checks the complete export flow.
```

Do not start dependent implementation against guessed interfaces. Independent investigation can continue while the contract is pending.

## 3. Return evidence the parent can inspect

**Weak return**

```text
Done. Fixed it and all tests pass.
```

**Useful return**

```text
Status: partial
Changed: src/parser.ts and test/parser.test.ts only.
Behavior: empty input returns the documented empty result instead of throwing.
Verification: npm test -- parser.test.ts — passed, 8 tests.
Evidence: the added empty-input case failed before the fix and passed afterward.
Remaining: the full suite could not run because the local database is unavailable.
No database settings or dependencies were changed.
```

The parent checks the owned diff and relevant evidence, then resolves the remaining integration check. A worker's completion claim does not complete the user's whole goal.

## 4. Fall back to supported runtime capabilities

**Poor approach**

```text
Assume a worker tool and a model option exist. Guess their names, then install
another service or change account settings when the call fails.
```

**Better approach**

```text
Inspect the current runtime's exposed delegation tool and schema.
If it supports workers but no model or reasoning controls, omit those fields
and use its documented defaults.
If delegation is unavailable, perform the scoped work directly and state that
no independent worker review occurred. Use supported parallel reads where useful.
```

Do not simulate separate workers or claim independent verification. Missing optional controls do not justify new services, credentials, or permission changes.
