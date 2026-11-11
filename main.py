#!/usr/bin/env python3
"""Draw the cutest cat — make.fun bounty entry (cutest-cat-01).

Writes one picture of a cat to /output/entry.png.

The entry image is a picture this repository holds (cat.png): an extreme
close-up of a fluffy orange tabby kitten's face filling the frame, with
enormous round amber eyes, a tiny pink nose and whiskers, on a soft cream
bokeh background. The program only copies those exact bytes to the output
path, so both runs write identical bytes and no network is used.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "cat.png")
OUTPUT = "/output/entry.png"


def png_size(path):
    """Return (width, height) of a PNG file, from its IHDR chunk."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    width, height = png_size(OUTPUT)
    size = os.path.getsize(OUTPUT)
    if size > 1048576:
        raise ValueError(f"output over 1 MiB: {size} bytes")
    print(f"Wrote {OUTPUT} ({size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
