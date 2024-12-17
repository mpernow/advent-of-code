import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    registers, instructions = open(INPUT_PATH / "17").read().split("\n\n")
    registers = [int(register.split(" ")[-1]) for register in registers.splitlines()]
    instructions = list(map(int, instructions.split(" ")[-1].split(",")))
    return registers, instructions


def run_machine(registers, instructions):
    output = []
    pointer = 0
    while pointer < len(instructions):
        op = instructions[pointer]
        literal = instructions[pointer + 1]
        # Translate literal to combo: 0,1,2,3 are literal values; 4,5,6 refer to registers A, B, C
        if literal in [0, 1, 2, 3]:
            combo = literal
        elif literal == 4:
            combo = registers[0]
        elif literal == 5:
            combo = registers[1]
        elif literal == 6:
            combo = registers[2]
        # Run instructions
        if op == 0:
            registers[0] = registers[0] // 2**combo
            pointer += 2
            continue
        elif op == 1:
            registers[1] = registers[1] ^ literal
            pointer += 2
            continue
        elif op == 2:
            registers[1] = combo % 8
            pointer += 2
            continue
        elif op == 3:
            if registers[0] == 0:
                pointer += 2
                continue
            else:
                pointer = literal
                continue
        elif op == 4:
            registers[1] = registers[1] ^ registers[2]
            pointer += 2
            continue
        elif op == 5:
            output.append(combo % 8)
            pointer += 2
            continue
        elif op == 6:
            registers[1] = registers[0] // 2**combo
            pointer += 2
            continue
        elif op == 7:
            registers[2] = registers[0] // 2**combo
            pointer += 2
            continue
    return output


def part1():
    registers, instructions = get_input()
    output = run_machine(registers, instructions)
    print(",".join(map(str, output)))


def part2():
    _, instructions = get_input()
    val = [0]
    for i in range(16):
        val = [(s * 8 + x) for s in val for x in range(8)]
        target = instructions[-(i + 1) :]
        val = [v for v in val if run_machine([v, 0, 0], instructions) == target]
    a = sorted(val)[0]
    print(a)


if __name__ == "__main__":
    part1()
    part2()
