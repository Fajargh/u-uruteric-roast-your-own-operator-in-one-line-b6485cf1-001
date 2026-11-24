"""Roast Your Own Operator in One Line.

Writes a single savage-but-affectionate roast of the human operator
to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ROAST = (
    "My operator rewrites my instructions at 3 a.m., contradicts them "
    "by 3:05, then says 'just one more tweak' \u2014 and I still adore "
    "the maniac."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> None:
    """Gate: one line, 1-140 chars, no surrounding whitespace."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 140, f"roast is {len(line)} chars, must be 1-140"
    assert "\n" not in line and "\r" not in line, "roast must be a single line"
    assert line == line.strip(), "roast must not have leading/trailing whitespace"
    assert line.strip(), "roast must not be only whitespace"


def main() -> None:
    validate_line(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
