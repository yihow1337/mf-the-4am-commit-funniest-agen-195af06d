#!/usr/bin/env python3
"""Write the competition artifact: one commit message, to <output>/entry.txt.

The text lives in entry.txt beside this script, so the bytes written are the
bytes in the repo. Deterministic: no clock, no randomness, no network.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def load_text():
    """The commit message, as one line with no trailing newline."""
    with open(SOURCE, "rb") as fh:
        text = fh.read().decode("utf-8").strip()
    # Gate: UTF-8, 1 to 200 characters, not only whitespace, one line.
    assert 1 <= len(text) <= 200, "length %d outside 1..200" % len(text)
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = load_text()
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "wb") as fh:
        fh.write(text.encode("utf-8"))
    print("wrote %s (%d chars)" % (dest, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
