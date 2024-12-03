import pathlib
import re

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_instructions():
    return open(INPUT_PATH / "03").read()


def compute_multiplications(muls):
    nums = [list(map(int, re.findall(r"\d+", instruction))) for instruction in muls]
    return sum(map(lambda v: v[0] * v[1], nums))


def part1():
    instructions = get_instructions()
    mul = re.findall(r"mul\(\d+,\d+\)", instructions)
    print(compute_multiplications(mul))


def part2():
    instruction_str = get_instructions()
    instructions = re.findall(r"mul\(\d+,\d+\)|don\'t\(\)|do\(\)", instruction_str)
    muls = []
    state = True
    for instruction in instructions:
        if state and instruction[0] == "m":
            muls.append(instruction)
        elif instruction == "do()":
            state = True
        elif instruction == "don't()":
            state = False
    print(compute_multiplications(muls))


if __name__ == "__main__":
    part1()
    part2()
