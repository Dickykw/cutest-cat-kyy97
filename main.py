#!/usr/bin/env python3
"""Draw the cutest cat — make.fun bounty entry (cutest-cat-01).

Writes one picture of a cat to /output/entry.png.

The entry image is a picture this repository holds (cat.png): a fluffy
orange tabby kitten with huge amber eyes, head tilted, looking straight
at the camera. The program only copies those exact bytes to the output
path, so both runs write identical bytes and no network is used.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "cat.png")
OUTPUT = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"Wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
