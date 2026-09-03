#!/usr/bin/env python3
"""Assemble bounded Markdown context for a web-based LLM; no API calls."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
VALID_WEEKS = ("preweek", "week01", "week02", "week03", "week04")
MAX_FILE_CHARS = 40_000
MAX_TOTAL_CHARS = 100_000
HELP_POLICY = """- Answer factual questions directly.
- For the core of an assignment, start with a scaffold or targeted hint.
- If I have tried and request a full explanation, explain it fully.
- Point out misconceptions explicitly.
- Distinguish source-backed claims from additional explanation.
- Translation and local explanation are allowed, but important claims must be checked in the original source."""


def read_text(path: Path) -> tuple[str, str | None]:
    """Read one small text file and return content plus an optional warning."""
    if path.suffix.lower() == ".ipynb":
        return "", f"Skipped unsupported notebook JSON: {path}"
    try:
        raw = path.read_bytes()
    except OSError as error:
        return "", f"Could not read {path}: {error}"
    if b"\x00" in raw:
        return "", f"Skipped binary file: {path}"
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return "", f"Skipped non-UTF-8 file: {path}"
    if len(text) > MAX_FILE_CHARS:
        return text[:MAX_FILE_CHARS], f"Truncated {path} at {MAX_FILE_CHARS} characters"
    return text, None


def within_repo(path: Path) -> Path:
    resolved = path.resolve()
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ValueError(f"--include must stay inside the repository: {path}")
    return resolved


def section(title: str, content: str) -> str:
    return f"## {title}\n\n{content.strip()}\n"


def build_context(week: str, includes: list[Path], question: str | None) -> tuple[str, list[str]]:
    warnings: list[str] = []
    readme, warning = read_text(ROOT / "course" / week / "README.md")
    if warning:
        warnings.append(warning)
    tasks, warning = read_text(ROOT / "course" / week / "tasks.md")
    if warning:
        warnings.append(warning)

    parts = [
        "# LM Fieldwork — Learning Context\n",
        f"I am a learner in LM Fieldwork.\nCurrent week: {week}\n",
        section("How to help me", HELP_POLICY),
        section("Current week guide and learning goals", readme),
        section("Current tasks", tasks),
    ]

    notes_name = "paper_notes.md" if week == "week04" else "notes.md"
    notes_path = ROOT / "work" / week / notes_name
    if notes_path.exists():
        notes, warning = read_text(notes_path)
        if warning:
            warnings.append(warning)
        parts.append(section("My notes", notes))

    for requested in includes:
        try:
            path = within_repo(requested if requested.is_absolute() else ROOT / requested)
        except ValueError as error:
            warnings.append(str(error))
            continue
        content, warning = read_text(path)
        if warning:
            warnings.append(warning)
        if content:
            parts.append(section(f"Included file: {path.relative_to(ROOT)}", f"```text\n{content}\n```"))

    parts.append(section("Question", question or "<write my question here>"))
    output = "\n".join(parts)
    if len(output) > MAX_TOTAL_CHARS:
        warnings.append(f"Total context truncated at {MAX_TOTAL_CHARS} characters")
        question_section = section("Question", question or "<write my question here>")
        output = output[: MAX_TOTAL_CHARS - len(question_section) - 2] + "\n\n" + question_section
    return output, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", required=True, choices=VALID_WEEKS)
    parser.add_argument("--include", action="append", default=[], type=Path)
    parser.add_argument("--question")
    parser.add_argument("--clipboard", action="store_true")
    args = parser.parse_args()

    output, warnings = build_context(args.week, args.include, args.question)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if args.clipboard and sys.platform == "darwin":
        try:
            subprocess.run(["pbcopy"], input=output, text=True, check=True)
            print("Context copied to clipboard.", file=sys.stderr)
            return 0
        except (OSError, subprocess.CalledProcessError) as error:
            print(f"WARNING: pbcopy failed; using stdout: {error}", file=sys.stderr)
    elif args.clipboard:
        print("WARNING: clipboard mode requires macOS pbcopy; using stdout", file=sys.stderr)

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
