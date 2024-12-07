import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_input():
    eqs = open(INPUT_PATH / "07").read().split("\n")
    eqs = [(int(e.split(":")[0]), [int(v) for v in e.split(":")[1].strip().split(" ")]) for e in eqs]
    return eqs

def check_equation(eq, check_concat=False):
    result = eq[0]
    values = eq[1]
    if len(values) == 1:
        if result == values[0]:
            return True
        else:
            return False
    add_ok = False
    if result >= values[-1]:
        add_ok = check_equation((result - values[-1], values[:-1]), check_concat)
    mult_ok = False
    if result % values[-1] == 0:
        mult_ok = check_equation((result // values[-1], values[:-1]), check_concat)
    concat_ok = False
    if check_concat and len(str(result)) > len(str(values[-1])) and str(result)[-(len(str(values[-1]))):] == str(values[-1]):
        concat_ok = check_equation((int(str(result)[:-(len(str(values[-1])))]), values[:-1]), check_concat)
    return add_ok or mult_ok or concat_ok


def part1():
    eqs = get_input()
    result = 0
    for eq in eqs:
        if check_equation(eq):
            result += eq[0]
    print(result)

def part2():
    eqs = get_input()
    result = 0
    for eq in eqs:
        if check_equation(eq, check_concat=True):
            result += eq[0]
    print(result)

if __name__ == "__main__":
    part1()
    part2()
