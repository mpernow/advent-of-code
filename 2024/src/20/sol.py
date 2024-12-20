import pathlib
from collections import deque
from itertools import combinations

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    map_ = open(INPUT_PATH / "20").read()
    size = int(len(map_) ** 0.5)
    walls = set()
    for r, row in enumerate(map_.splitlines()):
        for c, col in enumerate(row):
            if col == "#":
                walls.add(c + r * 1j)
            if col == "S":
                start = c + r * 1j
            if col == "E":
                end = c + r * 1j
    return walls, start, end, size


def is_valid(walls, pos, size, visited):
    return (
        0 <= pos.real < size
        and 0 <= pos.imag < size
        and pos not in walls
        and pos not in visited
    )


def floodfill(walls, size, start):
    distance = {start: 0}
    candidates = deque([start])
    while candidates:
        position = candidates.popleft()
        for direction in [1, -1, 1j, -1j]:
            next_position = position + direction
            if is_valid(walls, next_position, size, distance.keys()):
                distance[next_position] = distance[position] + 1
                candidates.append(next_position)
    return distance


def part1(distances):
    num_cheats = 0
    for (pos1, i), (pos2, j) in combinations(distances.items(), 2):
        d = abs((pos1 - pos2).real) + abs((pos1 - pos2).imag)
        if d == 2 and j - i - d >= 100:
            num_cheats += 1
    print(num_cheats)


def part2(distances):
    num_cheats = 0
    for (pos1, i), (pos2, j) in combinations(distances.items(), 2):
        d = abs((pos1 - pos2).real) + abs((pos1 - pos2).imag)
        if d <= 20 and j - i - d >= 100:
            num_cheats += 1
    print(num_cheats)


if __name__ == "__main__":
    walls, start, end, size = get_input()
    distances = floodfill(walls, size, start)
    part1(distances)
    part2(distances)
