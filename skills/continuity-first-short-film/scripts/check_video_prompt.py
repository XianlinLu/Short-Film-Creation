#!/usr/bin/env python3
"""Reject ambiguous language in prompts sent to video-generation nodes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = (
    (r"可能", "可能"),
    (r"或者", "或者"),
    (r"或许", "或许"),
    (r"或(?!者|许)", "或"),
    (r"也许", "也许"),
    (r"大概", "大概"),
    (r"大约", "大约"),
    (r"约(?:为|在|\s*\d)", "约/约为"),
    (r"差不多", "差不多"),
    (r"似乎", "似乎"),
    (r"尽量", "尽量"),
    (r"适当", "适当"),
    (r"酌情", "酌情"),
    (r"任选", "任选"),
    (r"任意", "任意"),
    (r"某种", "某种"),
    (r"类似", "类似"),
    (r"左右", "左右"),
    (r"等等", "等等"),
    (r"\bmaybe\b", "maybe"),
    (r"\bperhaps\b", "perhaps"),
    (r"\bpossibly\b", "possibly"),
    (r"\bpossible\b", "possible"),
    (r"\bmight\b", "might"),
    (r"\bcould\b", "could"),
    (r"\bprobably\b", "probably"),
    (r"\blikely\b", "likely"),
    (r"\broughly\b", "roughly"),
    (r"\bapproximately\b", "approximately"),
    (r"\bsomewhat\b", "somewhat"),
    (r"\boptionally\b", "optionally"),
    (r"\boptional\b", "optional"),
    (r"\beither\b", "either"),
    (r"\bor\b", "or"),
    (r"\bas appropriate\b", "as appropriate"),
    (r"\bif desired\b", "if desired"),
    (r"\btry to\b", "try to"),
    (r"\betc\.?\b", "etc."),
    (r"\band so on\b", "and so on"),
)


def read_prompt(path: str | None) -> str:
    if path is None or path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def find_ambiguities(prompt: str) -> list[tuple[int, int, str, str]]:
    findings: list[tuple[int, int, str, str]] = []
    for pattern, label in PATTERNS:
        for match in re.finditer(pattern, prompt, flags=re.IGNORECASE):
            line = prompt.count("\n", 0, match.start()) + 1
            previous_newline = prompt.rfind("\n", 0, match.start())
            column = match.start() - previous_newline
            findings.append((line, column, label, match.group(0)))
    return sorted(findings)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check a video-generation prompt for ambiguous language."
    )
    parser.add_argument(
        "prompt_file",
        nargs="?",
        default="-",
        help="UTF-8 prompt file. Omit or use - to read stdin.",
    )
    args = parser.parse_args()

    prompt = read_prompt(args.prompt_file)
    if not prompt.strip():
        print("FAIL: prompt is empty", file=sys.stderr)
        return 1

    findings = find_ambiguities(prompt)
    if findings:
        print("FAIL: ambiguous video-prompt language detected", file=sys.stderr)
        for line, column, label, matched in findings:
            print(
                f"  line {line}, column {column}: {matched!r} ({label})",
                file=sys.stderr,
            )
        print(
            "Rewrite every match as one exact action, camera, composition, timing, "
            "and asset-state instruction.",
            file=sys.stderr,
        )
        return 1

    print("PASS: no ambiguous video-prompt language detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
