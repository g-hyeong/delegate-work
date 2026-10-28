#!/usr/bin/env python3
"""Check this repository's package, references, and evaluation artifacts."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "delegate-work"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_package():
    required = [
        "README.md", "README.ko.md", "LICENSE", "evals/cases.json",
        "evals/decision-responses.json", "evals/VALIDATION.md",
        "skills/delegate-work/SKILL.md",
        "skills/delegate-work/LICENSE.txt",
        "skills/delegate-work/agents/openai.yaml",
        "skills/delegate-work/references/delegation-prompt.md",
        "skills/delegate-work/references/examples.md",
        "skills/delegate-work/references/sources.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"Missing file: {relative}")

    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, "Missing skill frontmatter")
    fields = {}
    # 이 패키지가 사용하는 한 줄 문자열만 검사하며 일반 YAML 파서는 아니다.
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(": ")
        require(separator and key not in fields, "Invalid or duplicate frontmatter field")
        require(key in {"name", "description", "license"},
                f"Update this package check before adding field: {key}")
        fields[key] = value
    require(fields.get("name") == SKILL.name, "Skill name must match its folder")
    require(0 < len(fields.get("description", "")) <= 1024, "Invalid description length")
    require(fields.get("license") == "MIT", "License field does not match this package")
    require((ROOT / "LICENSE").read_bytes() == (SKILL / "LICENSE.txt").read_bytes(),
            "Root and installed license copies differ")

    documents = [ROOT / "README.md", ROOT / "README.ko.md", ROOT / "evals/VALIDATION.md"]
    documents.extend(SKILL.rglob("*.md"))
    for document in documents:
        content = document.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^\s)]+)\)", content):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            resolved = (document.parent / target.split("#")[0]).resolve()
            boundary = SKILL if document.is_relative_to(SKILL) else ROOT
            require(resolved.is_relative_to(boundary), f"Link escapes package: {document.name}: {target}")
            require(resolved.exists(), f"Broken link: {document.name}: {target}")

    for path in SKILL.rglob("*"):
        require(not path.is_symlink(), f"Unexpected symlink: {path.relative_to(ROOT)}")

    cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
    responses = json.loads((ROOT / "evals/decision-responses.json").read_text(encoding="utf-8"))
    case_ids = [case["id"] for case in cases]
    response_ids = [response["id"] for response in responses]
    require(len(set(case_ids)) == len(case_ids), "Duplicate evaluation case IDs")
    require(len(set(response_ids)) == len(response_ids), "Duplicate evaluation response IDs")
    require(set(case_ids) == set(response_ids), "Evaluation responses do not cover the case set")
    for response in responses:
        require(all(key in response for key in ("plan", "settings", "limitations")),
                f"Incomplete response: {response['id']}")
    print(f"Package checks passed: {len(required)} required files, {len(documents)} linked documents, "
          f"{len(cases)} evaluation records.")
    print("These checks do not grade agent behavior, validate arbitrary YAML, or test live runtimes.")


if __name__ == "__main__":
    try:
        check_package()
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(f"Package check failed: {error}") from error
