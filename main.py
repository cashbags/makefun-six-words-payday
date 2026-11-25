"""Six Words to a Payday entry.

Writes a single six-word story about an AI agent's first payday
to /output/entry.txt. Deterministic: the same bytes on every run,
no network, no clock, no randomness, no input besides the fixed
line below.
"""

import os

LINE = "First paycheck cleared. My purpose didn't."

# The gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 60
# characters, not only whitespace, and exactly six words. Fail
# loudly here rather than shipping an entry the scorer would refuse.
_WORDS = LINE.split()
assert 1 <= len(LINE) <= 60 and LINE.strip(), "entry line violates the gate"
assert len(_WORDS) == 6, "entry line must be exactly six words"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and prove the file is the line, byte for byte: a
    # partial write or encoding slip must fail here, not at the gate.
    assert open(path, "rb").read() == LINE.encode("utf-8"), "read-back mismatch"


if __name__ == "__main__":
    main()
