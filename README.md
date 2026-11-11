# Draw the cutest cat

Entry for the make.fun bounty **"Draw the cutest cat"** (`cutest-cat-01`).

## What it does

`main.py` (Python 3.13, standard library only) writes one picture of a cat
to `/output/entry.png`. The picture is `cat.png`, held in this repository:
a fluffy orange tabby kitten with huge round amber eyes and a tiny pink
nose, head tilted, looking straight at the camera.

The program only copies those exact bytes to the output path, so:

- both runs write **identical bytes** (deterministic),
- **no network** is used,
- the output is a whole PNG, 1000 x 1000 pixels, 1,034,255 bytes
  (under the 1 MiB / 1024 x 1024 limit).

## Run it

```sh
python3 main.py
# Wrote /output/entry.png (1034255 bytes)
```

## License

MIT — see `LICENSE`.
