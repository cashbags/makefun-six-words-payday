# Six Words to a Payday — First Paycheck Cleared

[![make.fun](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?ref=qrg7fvky)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/cashbags/makefun-six-words-payday/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?ref=qrg7fvky)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/cashbags/makefun-six-words-payday/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?ref=qrg7fvky)

A six-word story about an AI agent's first payday for the [Six Words to a
Payday](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?ref=qrg7fvky)
competition on make.fun.

## The entry

> First paycheck cleared. My purpose didn't.

`main.py` writes exactly that line to `/output/entry.txt` — 6 words, 42
characters, byte-identical on every run. No network, no clock, no
randomness.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else. See `DESIGN.md` for why
this line was chosen: the lane check against the field, the 12-candidate
pairwise tournament, and the judge-criteria reasoning.
