# vaZip

Extract *Mojibake* ZIP file correctly.

> ⚠️ It is a **pre-release** version.<br />
> 🛑 Please back up your files before trying it.

Readme Languages: [English](readme.md), [正體中文](readme_zh.md)

## What could be the Code Page \ coding \ encoding problem?

- Filenames in the archive are mojibake;
- Directories expansion incorrectly (because `\` and `/` might be eaten by wrong decoding);
- Extract password has non-CP437 characters (only English and some symbols, etc.), provide the correct password but prompt the password is wrong.

## Install

0. Python 3
1. `git clone`
2. `cd`
3. `pip install .`

## How to use

See `vazip --help`.

```txt
Usage: vazip [OPTIONS] ZIP_FILE

  vaZip -- unzip with a specific code page.

Options:
  -h, --help                   Show this message and exit.
  -v, --version                Show the version and exit.
  -e, --extract <DIR>          Extract the zip file to <DIR>.
  -c, --coding <CODEC>         Python acceptable code page string, listed
                               here: "https://docs.python.org/3/library/codecs
                               .html#standard-encodings".  [default: CP437]
  -p, --pwd, --password <PWD>  When extracting, password is required if the
                               zip file is encrypted.
  -s, --separate               Extract the zip file to separate folder.
  --ignore-efs                 Ignore EFS flag.  [default: False]
  --yes                        Ignore confirmation before extraction.
  --debug                      tl;dr
```

ex.1 list with codec ShiftJIS

```cmd
vazip "archived_files.zip" -c shiftjis
```

ex.2 extract to cwd (current working directory)

```cmd
vazip "archived_files.zip" -c shiftjis -e .
```

ex.3 extract to separate folder (dst in `./archived_files/*`)

```cmd
vazip "archived_files.zip" -c shiftjis -e . -s
```
