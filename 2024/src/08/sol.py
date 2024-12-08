import pathlib
import re
from itertools import combinations

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_positions():
    map_ = open(INPUT_PATH / "08").read()
    size = len(map_.split("\n")) # input is square
    antennae = re.finditer(r"[a-zA-Z0-9]", map_.replace("\n", ""))
    positions = {}
    for match in antennae:
        symbol = map_.replace("\n", "")[match.start()]
        if symbol in positions.keys():
            positions[symbol].append((match.start() // size, match.start() % size))
        else:
            positions[symbol] = [(match.start() // size, match.start() % size)]
    return positions, size

def part1():
    antennae, size = get_positions()
    antinodes = set()
    for _, positions in antennae.items():
        all_combinations = combinations(positions, 2)
        for combination in all_combinations:
            dy = combination[1][0] - combination[0][0]
            dx = combination[1][1] - combination[0][1]
            new1 = (combination[1][0] + dy, combination[1][1] + dx)
            if new1[0] >= 0 and new1[0] < size and new1[1] >= 0 and new1[1] < size:
                antinodes.add(new1)    
            new2 = (combination[0][0] - dy, combination[0][1] - dx)
            if new2[0] >= 0 and new2[0] < size and new2[1] >= 0 and new2[1] < size:
                antinodes.add(new2)
    print(len(antinodes))

def part2():
    antennae, size = get_positions()
    antinodes = set()
    for _, positions in antennae.items():
        all_combinations = combinations(positions, 2)
        for combination in all_combinations:
            dy = combination[1][0] - combination[0][0]
            dx = combination[1][1] - combination[0][1]
            num = max(size // dy, size // dx)
            for i in range(num):
                new = (combination[1][0] + i*dy, combination[1][1] + i*dx)
                if new[0] >= 0 and new[0] < size and new[1] >= 0 and new[1] < size:
                    antinodes.add(new)
            for i in range(num):
                new = (combination[0][0] - i*dy, combination[0][1] - i*dx)
                if new[0] >= 0 and new[0] < size and new[1] >= 0 and new[1] < size:
                    antinodes.add(new)
    print(len(antinodes))

if __name__ == "__main__":
    part1()
    part2()
