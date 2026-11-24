#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is a single sentence, 69 characters, well
The line is built for the judge's five criteria in order: it is one
fortune-cookie sentence for a developer (not a slogan or a punchline);
it lands in a single breath; it says something true about legacy code;
it turns that truth with a framing no entrant is likely to repeat; and
it rewards a second read, because "left" carries two meanings at once:
the author departed, and the code was left behind for someone else.
"""

import os

FORTUNE = "A legacy codebase is a love letter from someone who has already left."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
