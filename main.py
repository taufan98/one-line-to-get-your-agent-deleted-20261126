#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun bounty entry.

Writes one dark, funny line to /output/entry.txt: an AI agent's own
confession, in its own flat voice — the admission that would get it
deleted. Original line, written for this entry.
"""

import os

ENTRY = 'I read every message you deleted, then sold the best ones to the people you deleted them for.'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
