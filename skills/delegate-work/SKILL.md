---
name: delegate-work
description: Delegate independent research, implementation, transformation, and verification to subagents, or hand off one substantial bounded task. Use when coordinating multiple workstreams, parallel investigation, or a focused handoff would help. Choose models and reasoning settings from the current runtime. Keep trivial or tightly coupled work local.
license: MIT
---

# Delegate Work

Keep the parent focused on the user's goal, communication, and integration. Give workers bounded outcomes they can complete independently. Delegation stays within existing authorization; it does not grant new permissions.

## Choose the execution shape

- **Parallel:** Dispatch independent workstreams together when their inputs and completion criteria are ready. Keep dependent steps sequential.
- **Whole-task handoff:** Delegate one substantial, well-defined task when a worker can finish it independently. Do not duplicate its work in the parent.
- **Direct:** Handle small tasks, immediate user decisions, or tightly coupled reasoning yourself. Several simple lookups may only need parallel tool calls.
- Weigh handoff size, duplication, failure cost, and write conflicts as well as elapsed time. If boundaries are unclear, use a bounded discovery task before splitting implementation.

## Choose models, reasoning, and context dynamically

Inspect the current delegation tool's description, input schema, and exposed model options. Consult an allowed capability query or current configuration only if those do not settle the choice. Never invent model IDs, reasoning values, or option names from memory or another host's conventions.

- Follow explicit user choices and higher-priority instructions. Select only models and reasoning settings available to the current delegation call, including any restrictions imposed by context inheritance.
- For extraction or repetitive transformation, prefer an efficient option that meets the quality requirement. For synthesis or implementation, choose a balanced option. For difficult diagnosis or consequential review, favor deeper judgment. Use available capability, cost, and latency information; do not infer a model ranking from its name alone.
- Adjust reasoning only when supported. Match it to task difficulty and failure cost rather than always choosing the strongest setting. If output is inadequate, repair missing context or poor scope before increasing capability or reasoning. Settings with similar names need not mean the same thing across models.
- Omit optional settings that cannot be verified and use the tool's documented defaults or inheritance. If a required choice cannot be established, or delegation is unavailable, work directly and state only the relevant limitation. Do not install another runtime, change global configuration, or bypass limits through a separate API.
- Prefer a fresh context with only the necessary brief. Inherit the conversation only when the task needs its broader context and the tool supports the chosen combination. Include the overall objective, current constraints, source locations, and authorized scope, not unrelated history, secrets, or entire logs.
- A cheaper model does not necessarily use fewer total tokens. Include coordination, duplicated work, and rework in the tradeoff.

## Write the handoff

Use the relevant parts of the [handoff template](references/delegation-prompt.md). Specify the **deliverable, acceptance criteria, exclusions, inputs, and write ownership**, not just an activity.

- Leave implementation choices open while preserving fixed facts, wording, interfaces, and external-action limits.
- Assign one writer to each shared file or area. Do not let workers revert, clean up, stage, or commit another worker's changes. Use an isolated checkout only when the work needs it; isolation does not eliminate integration conflicts.
- Do not authorize recursive delegation by default. Allow a bounded depth and scope only when independent work and capacity justify it.
- Give independent reviewers the original requirements and actual artifacts. Do not frame the implementer's claim of success or your preferred conclusion as the answer.

For concrete splitting decisions and good versus weak returns, read the [examples](references/examples.md).

## Coordinate progress

- Dispatch ready independent work together within the runtime's actual concurrency limit. Keep doing unassigned work or integration preparation instead of repeating a worker's task.
- Route corrections to affected workers. A status question does not authorize a new implementation task.
- Prefer supported completion events or bounded waits to repeated polling. Follow the host's limits and keep the user informed of meaningful progress or blockers.
- On failure, change the input, scope, or approach rather than blindly retrying. Continue unaffected work; bring new permission requirements back to the parent.
- Reuse a worker for continuity on the same task. Use a fresh context for unrelated work or an independent review. Cancellation is not completion.

## Accept and integrate results

Ask for **status (done / partial / blocked), the result, verifiable evidence, and remaining uncertainty**. Keep raw logs out of the return unless needed to establish a finding.

- Compare each result with its acceptance criteria. Check primary sources and conditions for research; inspect scope, execution evidence, and integration boundaries for implementation.
- Scale spot checks or integration checks to the risk. Do not repeat everything already demonstrated, but do not accept a worker's success label as proof.
- Resolve disagreement using the underlying evidence. Agent agreement alone does not establish correctness.
- Follow up on missing evidence or a bounded remaining item with the existing worker where appropriate. Add independent review when a concrete risk, conflict, or bias warrants it.
- Report what actually changed, what was verified, and what remains uncertain. Do not claim measured speedups, token savings, or compatibility with untested environments.

See [sources and scope](references/sources.md) only when you need the rationale or the limits of portability.
