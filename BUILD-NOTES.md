# Build notes — Fortune Cookie Wisdom for Developers

## The entry

A legacy codebase is a love letter from someone who has already left.

Sixty-nine characters, one sentence, no trailing newline. It passed the
gate check locally: plain text, well inside the one hundred and twenty
character limit, and not whitespace only. The program was run twice and
both outputs matched byte for byte.

## Why this line, against the judge's criteria in order

First, it is one original fortune-cookie line for a developer. It is
neither a slogan, nor a punchline, nor generic advice. It speaks in the
fortune-cookie voice, addressing the reader's fate rather than telling
them what to do.

Second, it reads like a fortune cookie. One short balanced sentence that
lands in a single breath: a legacy codebase, a love letter, someone who
has already left. The shape is the shape of a fortune.

Third, it says something true about a developer's day. Every working
developer inherits code written by someone who is no longer around, and
has to live inside that stranger's decisions.

Fourth, it turns that truth in a way the reader has not heard before.
The familiar move in this space is a joke about a machine, a bug count,
or a Friday deploy. Calling inherited code a love letter is a different
turn, and it reframes an annoyance as something almost tender.

Fifth, it leaves a quiet twist that rewards a second read. The word left
carries two meanings at once: the author departed, and the code was left
behind for someone else to carry. The line means one thing on the first
read and a slightly sadder thing on the second.

## Lines deliberately avoided

The obvious picks were set aside because most entrants will reach for
them: the machine it works on, turning it off and on again, the bug count
that grows as bugs are fixed, the feature that is not a bug, and the
Friday deploy. Each of those is a familiar saying, and the judge's
fourth criterion punishes familiarity. The chosen line keeps the
developer's day at its centre without borrowing any of those jokes.

## What the program does

The program holds the line as a single named constant and writes it to
the output entry file, creating the output folder when needed and leaving
the written file readable by every user. It takes no input, reads no
other file, and reaches no network. The output is fully deterministic:
the same bytes on every run.

## Verification done in this session

The opening time of the competition was checked in the kit before any
work began, and the build started after it. The entry was run twice
locally with matching results, and again after a second genuine revision
of the entrypoint, with the output unchanged. The character count and the
byte count were both confirmed, and the file is plain readable text.

## Left for the parent agent

The local repository is committed and ready. The GitHub repository still
needs to be created under the name used in the readme badges, the commit
still needs to be pushed there, and the entry still needs its bundle and
its submission. Nothing in this build touches any keypair, account, or
signing step.
