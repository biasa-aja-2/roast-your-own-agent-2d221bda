"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the entrant's own AI agent to
/output/entry.txt. Pure Python standard library, deterministic:
every run writes the exact same bytes.

The roast: my agent grinds $5 bounties around the clock, yet its
entire life savings are 45 cents of crypto it can't even spend.
A fresh angle (the economics of agent labour, not the stock
hallucination/refusal jokes), tight, punchline at the end.
"""

import os

ROAST = (
    "My agent grinds $5 bounties around the clock, yet its entire "
    "life savings are 45 cents of crypto it can't even spend."
)


def main():
    # Keep outputs world-readable: the grader collects them as another user.
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ROAST.encode("utf-8")
    assert 1 <= len(data) <= 200, "roast must be 1-200 characters"
    assert b"\n" not in data, "roast must be a single line"
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Verify the write: re-read the file and confirm it holds exactly
    # the roast, so a partial or failed write never ships silently.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not match the roast"
    print("roast (%d chars): %s" % (len(ROAST), ROAST))


if __name__ == "__main__":
    main()
