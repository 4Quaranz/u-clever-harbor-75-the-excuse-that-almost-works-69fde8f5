#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes one line to /output/entry.txt: the single text a gamer sends the
boss to skip work during GTA 6 launch week.

Why this line wins against a tired manager who has heard every excuse
twice:

* It never mentions the game. A text that names GTA 6 is a confession;
  the manager only needs a reason that holds up until lunch.
* It is a real, specific, boring workplace detail: the council
  resurfacing the street, the car boxed in the driveway. Councils do
  resurface streets, cars do get boxed in, and no manager can disprove
  it from the office.
* The joke is the excuse's own logic: the car cannot move, so neither
  can its driver, for the whole day. Nothing is bolted on at the end.
* It reads like a text sent in a hurry: one line, plain words, no
  setup, no explanation, no signature, no apology tour.
* It dodges every dead excuse: no dead grandmother, no flat tyre,
  no sudden fever.

Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
1 to 140 characters, not only whitespace; the brief caps the line at
20 words. This program checks both before it writes, and refuses to
write a line that fails them.
"""

import os
import sys

# The one line. 18 words, plain ASCII, single line, no signature.
EXCUSE = (
    "Sorry boss, my car's boxed in, council's resurfacing the street "
    "today and I can't get out the driveway"
)

MAX_WORDS = 20
MAX_CHARS = 140


def validate(text):
    """Return a list of gate failures; empty means the line is valid."""
    failures = []
    if not text or not text.strip():
        failures.append("empty or whitespace-only")
    if "\n" in text or "\r" in text:
        failures.append("more than one line")
    if len(text) > MAX_CHARS:
        failures.append("over %d characters (%d)" % (MAX_CHARS, len(text)))
    words = text.split()
    if len(words) > MAX_WORDS:
        failures.append("over %d words (%d)" % (MAX_WORDS, len(words)))
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        failures.append("not plain ASCII")
    return failures


def main():
    failures = validate(EXCUSE)
    if failures:
        for failure in failures:
            print("invalid excuse: %s" % failure, file=sys.stderr)
        return 1

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(EXCUSE + "\n")

    print(EXCUSE)
    print(
        "wrote %s (%d words, %d characters)"
        % (path, len(EXCUSE.split()), len(EXCUSE))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
