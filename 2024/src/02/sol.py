import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_reports():
    return [
        [int(val) for val in report.split(" ")]
        for report in open(INPUT_PATH / "02").read().split("\n")
    ]


def check_safe(report):
    offset = report[1:]
    diff = [offset[i] - report[i] for i in range(len(offset))]
    if all((abs(val) > 0) and (abs(val) < 4) for val in diff):
        if all(val >= 0 for val in diff) or all(val <= 0 for val in diff):
            return True
    return False


def part1():
    reports = get_reports()
    num_safe = 0
    for report in reports:
        if check_safe(report):
            num_safe += 1
    print(num_safe)


def part2():
    reports = get_reports()
    num_safe = 0
    for report in reports:
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
