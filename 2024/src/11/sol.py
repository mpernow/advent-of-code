import pathlib
from functools import cache

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    return map(int, open(INPUT_PATH / "11").read().split(" "))


@cache
def blink(x, n):
    if n == 0:
        return 1
    if x == 0:
        return blink(1, n - 1)
    if (sz := len(str(x))) & 1 == 0:
        return blink(int(str(x)[: sz >> 1]), n - 1) + blink(
            int(str(x)[sz >> 1 :]), n - 1
        )
    return blink(x * 2024, n - 1)


def part1():
    stones = get_input()
    print(sum(blink(x, 25) for x in stones))


def part2():
    stones = get_input()
    print(sum(blink(x, 75) for x in stones))


if __name__ == "__main__":
    part1()
    part2()
