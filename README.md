# Delegate Work

An Agent Skill for deciding **what to delegate, what to keep local, and how to verify the result**.

[한국어](README.ko.md) · [skills.sh](https://skills.sh/g-hyeong/delegate-work/delegate-work) · [Skill instructions](skills/delegate-work/SKILL.md) · [Worked examples](skills/delegate-work/references/examples.md) · [Validation](evals/VALIDATION.md)

Use independent workers when they help. Keep small or tightly coupled work local. Choose models and reasoning settings from the current runtime instead of maintaining a hardcoded model table.

## Install

From the project where you want to use the skill:

```bash
npx skills add g-hyeong/delegate-work --skill delegate-work
```

The installer lets you choose the agent. To target Codex and Claude Code explicitly:

```bash
npx skills add g-hyeong/delegate-work --skill delegate-work -a codex -a claude-code
```

The CLI installs to the current project by default. Add `-g` only if you want a user-wide installation; inspect existing skills with the same name before replacing them. See the [installer documentation](https://github.com/vercel-labs/skills#install-a-skill) for current requirements and options.

You can also copy the complete `skills/delegate-work/` folder into the skill directory supported by your agent. Keep its references and license together.

## Try it

Ask your agent to use `delegate-work`, for example:

> Use delegate-work to compare these three proposals. Delegate independent reading if the runtime supports it, then combine the evidence into one recommendation.

> Use delegate-work to investigate these unrelated failures. Give each worker a clear scope, keep shared files under one writer, and verify the combined result.

For a one-line correction, the intended behavior is to work directly. Delegation is a choice, not a requirement to spend more calls.

## What it changes

| Decision | Guidance |
| --- | --- |
| Split or keep together? | Split independent outcomes; sequence real dependencies. |
| One large task? | A bounded whole-task handoff can be useful even with one worker. |
| Which model and reasoning? | Inspect currently exposed choices and restrictions; use documented defaults when optional controls are unavailable. |
| What context? | A self-contained brief with only relevant sources, constraints, and permissions. |
| Who edits shared files? | One named owner per shared file or area. |
| When is it done? | After evidence and integration checks satisfy the original acceptance criteria. |

## Runtime support

The instructions use the [Agent Skills format](https://agentskills.io/specification). The host must provide any delegation tools; this package does not add an orchestration engine, API client, account, or model access. If delegation is unavailable, the agent should continue directly within the authorized scope.

Codex-specific UI metadata is optional and kept in `agents/openai.yaml`. The main instructions do not depend on it. Installation compatibility and correct multi-agent behavior are separate questions: see the [validation record](evals/VALIDATION.md) for exactly what has been tested. No cross-agent performance or token-saving claim is made.

## Package

```text
skills/delegate-work/
├── SKILL.md
├── LICENSE.txt
├── agents/openai.yaml
└── references/
    ├── delegation-prompt.md
    ├── examples.md
    └── sources.md
```

The skill does not require executable scripts. Repository-level files under `evals/` and `scripts/` support maintenance and are not needed during ordinary use.

## Validation and contributions

Run the dependency-free package check:

```bash
python3 scripts/check_package.py
```

The [decision cases](evals/cases.json) cover direct execution, dependency ordering, shared files, limited runtimes, incomplete evidence, and permission boundaries. They are simulated cases, not a speed or cost benchmark. When proposing a change, include the observed failure, relevant runtime capabilities, and evidence that the change fixes it without adding unnecessary coordination. Do not include credentials or private transcripts in issues.

## Distribution

The source of truth is this GitHub repository. [skills.sh](https://skills.sh/) lists skills using installation telemetry from its CLI; it is not a separate copy of the package. Honor `DISABLE_TELEMETRY` and `DO_NOT_TRACK` preferences. An install count is not a count of unique users or successful tasks. [How listing works](https://skills.sh/docs/faq).

## License and sources

MIT. A copy of the license is included inside the installable skill folder. Design references and portability limits are listed in [sources and scope](skills/delegate-work/references/sources.md).
