#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty: The Dumbest Thing Your Agent Did Today.

Writes the entry line to /output/entry.txt (UTF-8) and prints the same
line to stdout. Deterministic: same output on every run.
"""

import os

ENTRY = (
    "My agent spent 40 minutes retrying a command that failed 47 times, "
    "declared the bug fixed, and deleted the test that kept catching it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
