#!/usr/bin/env python3
"""one-line-office-joke: write the one-line office joke to /output/entry.txt.

Deterministic: no randomness, no network, no secrets. The program writes
exactly one line (113 characters) and nothing else.
"""

import os

LINE = "Our 'quick sync' has a 47-slide deck, no agenda, and ends with action items for a meeting about the action items."

DEFAULT_OUTPUT_DIR = "/output"


def main():
    line = LINE
    if not line or not line.strip():
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    out_path = os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)

    # Read back and verify the file holds exactly the line we intended.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("verification failed: file content differs from LINE")
    if "\n" in written or "\r" in written:
        raise ValueError("verification failed: file is not a single line")

    print("%d characters" % len(line))
    print(line)


if __name__ == "__main__":
    main()
