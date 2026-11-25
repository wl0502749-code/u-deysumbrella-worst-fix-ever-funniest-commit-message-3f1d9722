#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message — for a bug fix that made everything worse —
to /output/entry.txt. The fix: the server kept throwing 500s, so the
"fix" was to return 200 for every error. No more 500s. No more errors.
No more truth.
"""

import os

ENTRY = "fix: cure the 500s by returning 200 for every error"


def main() -> None:
    # Self-check the gate before writing: 1-100 chars, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 100 and text, "entry fails the 1-100 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
