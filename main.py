"""One-line excuse an AI agent gives its human for missing a deadline.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
The line is the excuse itself: 140 characters, no trailing newline.
Stdlib only. Never writes to the current working directory.
"""

import os


# The excuse: git rebase gone wrong, told by the agent that did it.
# 140 characters, inside the 1-160 gate, one sentence, agent voice.
LINE = (
    "I rebased to keep the history clean, resolved 31 conflicts, "
    "force-pushed the wrong branch, and the deadline is now on a "
    "branch I can't find."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
