#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.

The line is fixed and chosen in advance: the program is deterministic,
uses only the standard library, touches no network, and reads nothing
outside this repository.
"""

import os

LINE = "I told my AI assistant I feel empty. It suggested a 2TB external drive."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
