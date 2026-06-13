# Username Generator

A simple Python username generator. It reads a list of full names from a file, builds a unique username for each person, and writes the results to an output file.

![Language](https://img.shields.io/badge/language-Python-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> Created as an assignment for **ICTPRG302** as part of my Certificate III in Networking at Ringwood Training.

## How It Works

Each username is built from three parts:

```
<first initial><surname><4 random digits>
```

For example, `Campbell Kidwell` becomes something like `Ckidwell4821`.

- The **first initial** is the uppercase first letter of the given name.
- The **surname** is lower-cased.
- The **four digits** are generated with Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module, so the randomness is cryptographically strong rather than predictable.

## Requirements

- Python 3 (uses only the standard library — `secrets` and `string`).

## Usage

```sh
python main.py
```

The program prompts for:

1. The full path to your **input file** of names.
2. The full path to an **output file** (it will be created if it doesn't exist).

After generating, it asks whether you'd like to create more usernames (`Y` / `N`).

### Input format

One full name per line, given name and surname separated by a space:

```
Campbell Kidwell
Devyn Barr
Elisha Partridge
```

A sample `input.txt` is included.

### Output

Usernames are written to the output file under a `##USERNAMES##` header, one per line.

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | The generator. |
| `input.txt` | Sample list of names. |
| `output.txt` | Sample generated output. |

## License

Released under the [MIT License](LICENSE).
