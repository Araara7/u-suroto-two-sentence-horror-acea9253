#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences (140 chars) to
/output/entry.txt. Deterministic: the same bytes on every run.
"""
import os

ENTRY = (
    # Sentence 1: a grief habit, stated plainly. Sentence 2 re-reads it:
    # the plate was already warm, so the habit was never only his.
    "Every night since my wife died, I still set two plates at the table "
    "out of habit. Tonight I reached for hers first, and it was already warm."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
