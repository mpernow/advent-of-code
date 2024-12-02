import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_reports():
    return [
        [int(val) for val in report.split(" ")]
        for report in open(INPUT_PATH / "02").read().split("\n")
    ]


def check_safe(report):
    diff = list(map(lambda x: x[1] - x[0], zip(report, report[1:])))
    slow_change = lambda d: 0 < abs(d) < 4
    sign = lambda d: (d > 0) - (d < 0)
    if all(map(slow_change, diff)) and all(sign(d) == sign(diff[0]) for d in diff):
        return True
    return False


def check_safe_problem_dampener(report):
    if check_safe(report):
        return True
    else:
        for i in range(len(report)):
            if check_safe(report[:i] + report[i + 1 :]):
                return True
    return False


def part1():
    reports = get_reports()
    print(sum(map(check_safe, reports)))


def part2():
    reports = get_reports()
    print(sum(map(check_safe_problem_dampener, reports)))

if __name__ == "__main__":
    part1()
    part2()
