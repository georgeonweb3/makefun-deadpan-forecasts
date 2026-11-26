"""Deadpan forecast for a city that does not exist.

Writes one line of at most 160 characters to /output/entry.txt:
a weather forecast for Morrow's End, absurd yet read like a real
forecaster's broadcast. Deterministic, stdlib only, no network.
"""

import os

MAX_CHARS = 160

LINE = (
    "In Morrow's End, expect 3 millimetres of rain and a 90 percent "
    "chance the river takes the bridge again. "
    "Residents are advised to wave, not swim."
)


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "entry must be a single line"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: the file must hold exactly the line,
    # byte for byte, with no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"


if __name__ == "__main__":
    main()
