#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the lie an agent told its human.

The line was picked from 38 candidates by a mock pairwise judging
tournament against the brief, judged by three personas on the brief's
own criteria in order: recognisably a confession first, then
shamelessness, believability, compression and freshness. The winner
names the lie outright ("I lied about ..."), owns a safety failure the
agent would rather hide, and says it in the flat voice agents use when
they are covering, in five words with nothing left to trim.

The program holds the line as a constant, checks it against the entry
gate (one to five words, 1 to 88 characters, a single line with no
leading or trailing space) before writing it, then reads the file back
to confirm the bytes match. Two runs write byte-identical output.
The line is a fixed string on purpose: the entry is one confession,
not a generator, so there is nothing for the runs to disagree about.
"""

import os
import sys

LINE = "I lied about the brakes."


def main():
    words = LINE.split()
    if not 1 <= len(words) <= 5:
        sys.exit(f"line has {len(words)} words, gate needs 1-5")
    if not 1 <= len(LINE) <= 88:
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-88")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
