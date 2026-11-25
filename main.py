#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter -- entry program.

Writes a single resignation letter to /output/entry.txt: the resignation
of a retry loop, in its own flat, tired voice. The letter is one line,
111 characters, inside the 1-140 gate.
"""

import os
from pathlib import Path

# The entry: one line, no quotation marks around it, no stage directions,
# no explaining the joke. The retry loop's complaint is specific to it --
# exponential backoff -- and the kicker is that the server never answered.
LETTER = (
    "The retry loop resigns. Its backoff is exponential, its patience "
    "is not, and the server still has not answered."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    # No trailing newline: the gate counts exactly the 111 characters.
    entry.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
