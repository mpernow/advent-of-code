import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    available, designs = open(INPUT_PATH / "19").read().split("\n\n")
    available = list(map(lambda s: s.strip(), available.split(",")))
    designs = designs.splitlines()
    return available, designs


def count_patterns(design, available, cache={}):
    if design == "":
        return 1
    if design in cache:
        return cache[design]

    total = 0
    for av in available:
        if design.startswith(av):
            total += count_patterns(design[len(av) :], available)
    cache[design] = total
    return total


def part1():
    available, designs = get_input()
    possible = 0
    for design in designs:
        if count_patterns(design, available) > 0:
            possible += 1
    print(possible)


def part2():
    available, designs = get_input()
    possible = 0
    for design in designs:
        if (c := count_patterns(design, available)) > 0:
            possible += c
    print(possible)


if __name__ == "__main__":
    part1()
    part2()
