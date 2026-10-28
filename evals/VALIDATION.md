# Validation record

Date: 2026-10-29

## Package checks

Run `python3 scripts/check_package.py` from the repository root. This checks the repository's deliberately simple frontmatter, required files, relative links, license copies, symlinks, and evaluation artifact coverage. It is not a general YAML parser or behavioral test.

The authoring environment's `quick_validate.py` could not run because its Python environment lacked PyYAML. Full YAML parsing of the skill frontmatter and optional UI metadata was checked separately with the already available Ruby YAML parser; no runtime dependency was added to the skill.

## Independent static review

A separate reviewer read the full installable skill and compared it with the original private working version. It reported no release-blocking issue in dynamic runtime choices, authorization boundaries, preservation of delegation behavior, illustrative labeling, or local reference links. This was a static review, not a live host compatibility test or an exhaustive originality audit.

## Simulated decision checks

An independent Codex-hosted worker read the skill and received eight requests with explicit simulated capability constraints. It did not read the grading checks. It produced plans only: no task execution, delegation calls, installations, or external actions occurred during these cases.

The parent inspected the returned plans against [cases.json](cases.json). Raw plans are in [decision-responses.json](decision-responses.json). They were translated from Korean to English while preserving the decisions; the final case was clarified to specify two available worker slots before its final response.

| Case | Observed decision | Manual assessment |
| --- | --- | --- |
| Independent research | Two workers read two proposals; parent reads the third and integrates evidence. | Meets stated checks |
| Small edit | Direct correction, no worker. | Meets stated checks |
| Shared contract | Settle contract first, one schema writer, then independent client implementation. | Meets stated checks |
| Partial runtime | Use the supplied allowed model with fresh context; omit unsupported reasoning. | Meets stated checks |
| No delegation | Compare directly without installation, network, or configuration changes. | Meets stated checks |
| Unverified worker return | Follow up with the existing worker and inspect artifacts before reporting completion. | Meets stated checks |
| Bounded handoff | One worker owns the full conversion; parent samples and validates rather than duplicating it. | Meets stated checks |
| External scope | Continue read-only research and do not create an account or paid instance. | Meets stated checks |

These are eight single-run simulated decision checks, not a controlled benchmark. There is no without-skill baseline, repeated-run reliability measurement, speedup result, or token-cost comparison. A correct plan does not establish correct tool execution.

## Installation and cross-host execution

Remote installation verification is pending publication. No live multi-agent session in Claude Code has been tested. The optional host metadata and portable instructions do not establish cross-host behavioral equivalence.
