# Sources and scope

Reviewed on 2026-10-29. These sources informed the design and packaging; this skill is independently written, not a copy of their instructions. Popularity is a discovery signal, not evidence of correctness.

- [Agent Skills specification](https://agentskills.io/specification): a small SKILL.md entry point with optional references and host metadata.
- [Superpowers: dispatching parallel agents](https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md): independent task boundaries, focused briefs, conflict checks, and integration. This skill also allows whole-task handoffs and direct execution.
- [Matt Pocock: TDD](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd): focused instructions with separate worked examples and failure patterns. Its testing and approval policies are not imported here.
- [Matt Pocock: grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): distinguish facts to investigate from decisions, and keep only dependent work waiting. Its interview format is not required here.
- [Vercel: agent-browser](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md): consult instructions matching the installed runtime instead of assuming a fixed tool interface. This skill has no CLI dependency of its own.
- [Anthropic: skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator): evaluate representative behavior and distinguish observed outcomes from claims. See the repository's evaluation cases and validation record; no benchmark advantage is claimed.
- [Anthropic multi-agent research](https://www.anthropic.com/research/multi-agent-research-system): task decomposition, context selection, and coordination costs. Results from that system do not establish performance here.

The host provides delegation tools, available models, settings, concurrency, and permissions. A skill can guide these choices but cannot add missing capabilities or authorize restricted actions. Model and reasoning options must come from the current runtime, not from this source list.
