import pathlib
from itertools import combinations

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_input():
    patterns = open(INPUT_PATH / "25").read().split("\n\n")
    patterns = [item.splitlines() for item in patterns]
    return patterns

def part1():
    patterns = get_input()
    patterns = [{(i,j) for i,line in enumerate(pattern) for j,char in enumerate(line) if char=='#'} for pattern in patterns]

    count = 0
    for pattern1,pattern2 in combinations(patterns,2):
        if not set.intersection(pattern1,pattern2):
            count += 1
    print(count)


if __name__ == "__main__":
    part1()