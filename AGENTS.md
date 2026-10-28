# Repository guidance

The installable skill lives in `skills/delegate-work/`. Keep the entry point concise and move worked examples into references. Do not hardcode model IDs, reasoning values, or host-specific delegation calls.

Preserve the distinction between illustrative examples, simulated decision checks, package checks, and live execution. Update `evals/VALIDATION.md` only with observed results. Run `python3 scripts/check_package.py` after changes and review the diff before committing.

Use Korean commit messages. Keep private paths, credentials, session transcripts, and user-specific settings out of this public repository. Do not modify the installed personal skill as a side effect of repository work.
