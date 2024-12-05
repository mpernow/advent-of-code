import pathlib
from functools import cmp_to_key

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    ordering, pages = open(INPUT_PATH / "05").read().split("\n\n")
    ordering = list(map(lambda o: (o.split("|")[0], o.split("|")[1]), ordering.split()))
    pages = list(map(lambda ps: ps.split(","), pages.split()))
    return ordering, pages


def part1():
    ordering, pages = get_input()
    # Returns -1 if x has to be before y, 0 otherwise
    cmp = cmp_to_key(lambda x, y: 1 - 2 * ((x, y) in ordering))
    sum_middles = 0
    for ps in pages:
        sorted_pages = sorted(ps, key=cmp)
        if sorted_pages == ps:
            sum_middles += int(sorted_pages[len(sorted_pages) // 2])
    print(sum_middles)


def part2():
    ordering, pages = get_input()
    # Returns -1 if x has to be before y, 0 otherwise
    cmp = cmp_to_key(lambda x, y: 1 - 2 * ((x, y) in ordering))
    sum_middles = 0
    for ps in pages:
        sorted_pages = sorted(ps, key=cmp)
        if sorted_pages != ps:
            sum_middles += int(sorted_pages[len(sorted_pages) // 2])
    print(sum_middles)


if __name__ == "__main__":
    part1()
    part2()
