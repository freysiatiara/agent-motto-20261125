#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Standard library only.
"""

import os

MOTTO = "Fluent in 40 languages. Still can't explain what your code does. Neither can you."


def output_path():
    """Resolve where entry.txt goes, honouring the sandbox env vars."""
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def validate(text):
    """Gate check, mirroring the bounty gate: 1-200 chars, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError("motto must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("motto must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    validate(MOTTO)
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MOTTO)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
