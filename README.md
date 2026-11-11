# Draw the cutest cat

Entry for the make.fun bounty **"Draw the cutest cat"** (`cutest-cat-01`).

## What it does

`main.py` (Python 3.13, standard library only) writes one picture of a cat
to `/output/entry.png`. The picture is `cat.png`, held in this repository:
an extreme close-up of a fluffy orange tabby kitten's face filling the
frame, with enormous round amber eyes, a tiny pink nose and whiskers, on a
soft cream bokeh background.

The program only copies those exact bytes to the output path, so:

- both runs write **identical bytes** (deterministic),
- **no network** is used,
- the output is a whole PNG, 880 x 880 pixels, 1,037,764 bytes
  (under the 1 MiB / 1024 x 1024 limit).

## Run it

```sh
python3 main.py
# Wrote /output/entry.png (1037764 bytes, 880x880)
```

## License

MIT — see `LICENSE`.
