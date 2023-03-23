"""Find the plain text of three transformations."""

from itertools import permutations
import terminaltables

# CP_LIST = ['shiftjis', 'gbk', 'gb2312', 'big5', 'utf-8', 'cp437']
CP_LIST = ['utf-8', 'shiftjis', 'gbk']
DIMENSION = 3


assert 2 <= DIMENSION <= len(CP_LIST)


def mojibake_3d(s, cp1, cp2, cp3):
    return s.encode(cp1, errors='replace') \
        .decode(cp2, errors='replace') \
        .encode(cp2, errors='replace') \
        .decode(cp3, errors='replace')


def main(argv):
    assert len(argv) > 1, 'Error: len(argv) > 1'
    tab = [['cp1', 'cp2', 'cp3', 'return'], ]
    for comb in permutations(CP_LIST, DIMENSION):
        r = mojibake_3d(argv[1], *comb)
        tab.append([*comb, r])
    tt = terminaltables.AsciiTable(tab)
    print(tt.table)


if __name__ == "__main__":
    import sys
    main(sys.argv)
