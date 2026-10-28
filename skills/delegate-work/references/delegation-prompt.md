# Delegation prompt

Use only the fields the task needs. Give a worker enough context to act without the parent's conversation. Point to source files and precise sections instead of copying long records.

```text
Goal: The user's overall goal is [goal]. Your deliverable is [independent result].

Context and inputs:
- Confirmed constraints and latest corrections: [only what changes the result]
- Applicable instructions: [instruction or skill paths to read]
- Sources: [paths, URLs, versions, and exact reading scope]
- Prerequisites: [settled inputs; label assumptions and pending results]

Scope and ownership:
- Do: [assigned work]
- Exclude: [adjacent work outside this assignment]
- Read/write: [read-only, or exact files/areas you own]
- Coordination: [dependencies and sole owner of each shared file]
  Preserve other workers' changes; do not revert, stage, or commit them.
- External actions: [authorized reads or changes; report any new permission needed]
- Further delegation: none unless explicitly allowed within [scope and limit].

Completion and verification:
- Done means: [observable result or question answered]
- Verify with: [checks appropriate to this deliverable]
- Report or stop dependent work for: [access failure, scope change, new permission,
  or ambiguity that changes the result]. Continue independent authorized work.

Return:
- done / partial / blocked, with the actual scope completed
- Main conclusion or deliverable location
- Inspectable evidence and verification results
- Remaining uncertainty, failures, or decisions needed, if any

Preserve source facts and confirmed wording. Return useful evidence, not full logs.
```

## Optional task-specific details

- **Research:** Specify comparison criteria, versions, date, and source types. Require support from inspected source content rather than search snippets alone.
- **Implementation:** State expected behavior, owned paths, contracts to preserve, and relevant checks. Do not include unapproved dependencies or publication in the completion criteria.
- **Independent review:** Supply the original requirements and actual artifact. Ask for defects, omissions, and reproduction evidence without presenting the implementer's conclusion as the expected answer. If no issue is found, report coverage and uncertainty.
- **Follow-up:** Send the original goal plus changed constraints and missing work. Do not require repeating already verified work without a reason.
