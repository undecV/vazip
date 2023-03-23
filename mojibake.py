"""Find the plain text of Mojibake with two transformations."""

import itertools


def mojibake(s, cpls):
    for i, j in itertools.product(cpls, repeat=2):
        c = f'{i} > {j}' if i != j else i
        print(f"{c:<20}: {s.encode(i, errors='replace').decode(j, errors='replace')}")


def main(argv):
    assert len(argv) > 1, 'Error: len(argv) > 1'
    mojibake(argv[1], ['shiftjis', 'gbk', 'gb2312', 'big5', 'utf-8', 'cp437'])
    # mojibake(argv[1], ['gbk', 'utf-8', 'cp437'])
    pass


if __name__ == "__main__":
    import sys
    main(sys.argv)
