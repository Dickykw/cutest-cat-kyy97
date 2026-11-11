# Draw the cutest cat

Entry for the make.fun bounty **"Draw the cutest cat"** (`cutest-cat-01`).

## What it does

`main.py` (Python 3.13, standard library only) writes one picture of a cat
to `/output/entry.png`. The picture is `cat.png`, held in this repository:
two fluffy orange tabby kittens cuddling cheek to cheek, both faces large
in the frame with enormous round amber eyes looking straight at the camera,
tiny pink noses and whiskers, on a soft cream bokeh background.

The program only copies those exact bytes to the output path, so:

- both runs write **identical bytes** (deterministic),
- **no network** is used,
- the output is a whole PNG, 860 x 860 pixels, 1,019,439 bytes
  (under the 1 MiB / 1024 x 1024 limit).

## Run it

```sh
python3 main.py
# Wrote /output/entry.png (1019439 bytes, 860x860)
```

## License

MIT — see `LICENSE`.
