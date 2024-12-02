import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_lists():
    data = [*map(int, open(INPUT_PATH / "01").read().split())]
    return sorted(data[0::2]), sorted(data[1::2])


def part1():
    list1, list2 = get_lists()
    print(sum(map(lambda a, b: abs(a - b), list1, list2)))


def part2():
    list1, list2 = get_lists()
    print(sum(map(lambda a: a * list2.count(a), list1)))


if __name__ == "__main__":
    part1()
    part2()
