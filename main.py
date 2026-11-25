"""The Excuse That Almost Works: one line, at most 20 words.
"""

import os

TEXT = "Sorry, the office VPN locked me out after the update and IT says the reset queue is forty people deep."


def main():
    words = TEXT.split()
    assert 1 <= len(words) <= 20, len(words)
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()
    assert "\n" not in TEXT
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
