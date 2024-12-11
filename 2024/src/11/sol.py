import pathlib
from collections import Counter, defaultdict

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    return map(int, open(INPUT_PATH / "11_test").read().split(" "))


def blink(input_counter: Counter):
    output_counter = defaultdict(int)

    for stone, _ in input_counter.items():
        if stone == 0:
            output_counter[1] += input_counter[0]
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            s1, s2 = int(s[: len(s) // 2]), int(s[len(s) // 2 :])
            output_counter[s1] += input_counter[stone]
            output_counter[s2] += input_counter[stone]
        else:
            output_counter[stone * 2024] += input_counter[stone]

    return output_counter


def part1():
    stones = get_input()
    c = Counter(stones)
    for _ in range(25):
        c = blink(c)
    print(sum(c.values()))


def part2():
    stones = get_input()
    c = Counter(stones)
    for _ in range(75):
        c = blink(c)
    print(sum(c.values()))


if __name__ == "__main__":
    part1()
    part2()
