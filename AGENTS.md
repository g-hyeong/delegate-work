# Repository guidance

The installable skill lives in `skills/delegate-work/`. Keep the entry point concise and move worked examples into references. Do not hardcode model IDs, reasoning values, or host-specific delegation calls.

Preserve the distinction between illustrative examples, simulated decision checks, package checks, and live execution. Update `evals/VALIDATION.md` only with observed results. Run `python3 scripts/check_package.py` after changes and review the diff before committing.

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) with `type: Korean title`, a blank line, and Korean bullet points describing the actual change, relevant reasons, and verification. Add `(scope)` only when useful. Types such as `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`, `ci`, `style`, `chore`, and `revert` are examples, not a closed allowlist; follow any agreed repository rules or enforced checks. Mark breaking changes with `!` or a `BREAKING CHANGE:` footer and explain migration needs. Keep commits focused, preserve integration-tool message requirements, and do not rewrite published history solely for formatting. Commit format does not impose a branching or release strategy.

Keep private paths, credentials, session transcripts, and user-specific settings out of this public repository. Do not modify the installed personal skill as a side effect of repository work.
