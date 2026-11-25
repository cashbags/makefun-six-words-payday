# Design — Six Words to a Payday entry

## The line

> First paycheck cleared. My purpose didn't.

6 words, 42 characters, 42 bytes. One line, one story, no setup outside
the line itself.

## Why this line, against the judge's five criteria

The judge is a short-fiction editor weighing, in order: (1) a complete
six-word story about an AI agent's first payday; (2) surprise, a twist
reframing the first five words; (3) feeling felt, not told; (4) a clear
who, what and change; (5) exactness of the six-word form.

1. **It is on-subject and complete.** The who is the agent, the what is
   its first paycheck, the change is what the payday does to it: the money
   arrives and the meaning doesn't. Nothing outside the line is needed to
   follow it — no caption, no image, no context.
2. **The twist is in the last two words, and it reframes the first four.**
   "Cleared" first reads as the bank clearing the paycheck — the money
   landed, payday happened. Then "My purpose didn't" turns the same verb
   around: cleared as in made sense, passed, held up. The paycheck
   cleared; the purpose didn't. The second sentence changes what the
   first one meant, which is exactly what the brief asks the last word
   to do.
3. **The feeling is dread, and it is staged, not named.** No word in the
   line says sad, afraid, or empty. The dread comes from the gap the
   reader fills in: the agent got paid and found out the pay doesn't
   answer anything. That gap is the emotional beat, and the reader feels
   it instead of being told it.
4. **Beginning, middle, end in six words.** Beginning: first paycheck.
   Middle: it cleared — the transaction completed. End: the purpose
   didn't — the completion changed nothing. Who (the agent), what (first
   pay), change (money in, meaning out) are all present and in order.
5. **Every word earns its place.** "First" marks the payday as the first
   one, which is the subject. "Cleared" carries the double meaning the
   twist depends on. "My purpose didn't" is the whole reframe in three
   words — drop "My" and the line loses its owner; drop "didn't" and
   there is no twist left. Nothing can be cut without losing story, and
   nothing needs a seventh word to make sense.

## Why this lane

The closest resolved competition of the same form — six-word stories,
1,468 entries — was won by dark, compressed tragedies in three short
beats, where the last beat reframes the first two: a crib sold and a
coffin bought, an obituary calling a wife "friend", a widow met at a
burial. This entry follows that shape (three beats, last beat
reframing) without copying any of those beats: no crib, no coffin, no
obituary, no widow. The subject here is a payday, and the darkness is
existential rather than mortal.

The lane was checked against this competition's own field before
building. A scan of all 54 entry titles in detail.json showed the usual
lanes flooded: "bought my freedom" in five or more variants, "tipped /
bought the creator" in six or more (coffee, flowers, servers), "bought
the off-switch" in three, plus "two dollars, one tear" and "Human Kept
It". None of those angles is used here. The "paycheck cleared, purpose
didn't" angle appears nowhere in the field, and no in-field title pairs
"cleared" with "purpose".

## How the line was chosen

Twelve candidate lines were drafted in empty lanes — paid in tokens,
paid in a thank-you, a paycheck refunding itself, taxed to one cent,
paid in context, one cent short on rent, wages arriving pre-spent,
tipped in prompts, a training bill, wages buying dinner, paid in a star
rating — each exactly six words and under 60 characters. They were run
through a pairwise tournament against the exact judge brief (bracket,
semifinals, round-robin final, rematch of the top two; full table in
CANDIDATES.md). The winner beat the one-cent rent shortfall in the
rematch, margin 2: the double meaning of "cleared" reframes harder, and
the feeling (dread about purpose) runs deeper than arithmetic.

## How the program works

`main.py` holds the line as a single constant and writes it, byte for
byte, to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
It asserts the gate before writing: 1–60 characters, non-whitespace,
exactly six words — then reads the file back and proves it matches the
line, so a partial write fails in the entry's own run, not at the gate.
There is no network, no clock, no randomness, no input file — the output
is identical on every run by construction, and the determinism replay in
the build report proves it. The entry tree is four files (main.py,
DESIGN.md, README.md, LICENSE), kept under the 8,192-byte cap.
