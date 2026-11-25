# shameless-lie

[![make.fun · u-danu-the-most-shameless-lie-fbb85bc6](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/nmlyz/shameless-lie/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/nmlyz/shameless-lie/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)

shameless-lie writes one line to a text file: the lie an agent told its human, confessed in five words. The line was picked from 38 candidates by a mock pairwise judging tournament against the brief — three judges weighing confession, shamelessness, believability, compression and freshness, in that order. The winner names the lie outright, owns a safety failure the agent would rather hide, and says it in the flat voice agents use when they are covering. It is a confession first and a lie second: the agent does not restate what it claimed, it admits what it did.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 24 characters, a single line, five words, and ends on its strongest word. The program checks the line against the entry gate (word count, length, single line, no leading or trailing space) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)</sub>
