import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def check_safe(report):
    offset = report[1:]
    diff = [offset[i] - report[i] for i in range(len(offset))]
    if all((abs(val) > 0) and (abs(val) < 4) for val in diff):
        if all(val >= 0 for val in diff) or all(val <= 0 for val in diff):
            return True
    return False


def part1():
    with open(INPUT_PATH / "02") as f:
        data = f.readlines()
    data = [[int(val) for val in line.strip("\n").split(" ")] for line in data]

    num_safe = 0
    for report in data:
        if check_safe(report):
            num_safe += 1
    print(num_safe)

def part2():
    with open(INPUT_PATH / "02") as f:
        data = f.readlines()
    data = [[int(val) for val in line.strip("\n").split(" ")] for line in data]

    num_safe = 0
    for report in data:
        if check_safe(report):
            num_safe += 1
        else:
            for i in range(len(report)):
                if check_safe(report[:i] + report[i+1:]):
                    num_safe += 1
                    break
    print(num_safe)

if __name__ == "__main__":
    part1()
    part2()
