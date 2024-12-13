import pathlib
import re
from math import floor

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    claw_machines = open(INPUT_PATH / "13").read().split("\n\n")
    claw_machines = [
        list(map(int, re.findall(r"\d+", claw_machine)))
        for claw_machine in claw_machines
    ]
    return claw_machines


def get_min_cost(claw_machine, add=0):
    xa = claw_machine[0]
    ya = claw_machine[1]
    xb = claw_machine[2]
    yb = claw_machine[3]
    x = claw_machine[4] + add
    y = claw_machine[5] + add
    det = xa * yb - xb * ya
    a = (x * yb - y * xb) / det
    b = (y * xa - x * ya) / det
    if abs(floor(a) - a) < 1e-6 and abs(floor(b) - b) < 1e-6:
        return 3 * int(a) + int(b)
    else:
        return 0


def part1():
    claw_machines = get_input()
    print(sum(map(get_min_cost, claw_machines)))


def part2():
    claw_machines = get_input()
    print(sum(map(lambda m: get_min_cost(m, add=10000000000000), claw_machines)))


if __name__ == "__main__":
    part1()
    part2()
