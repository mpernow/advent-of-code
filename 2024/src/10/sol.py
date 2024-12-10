import pathlib
from collections import deque

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    # Parse grid as complex numbers
    data = open(INPUT_PATH / "10").read().splitlines()
    grid = {
        x + y * 1j: int(val)
        for y, line in enumerate(data)
        for x, val in enumerate(line)
    }
    trailheads = [key for key, val in grid.items() if val == 0]
    return grid, trailheads


def get_score(grid, starting_position, check_visited=True):
    score = 0
    queue = deque()
    queue.append(starting_position)
    encountered = set()
    while queue:
        position = queue.popleft()
        if check_visited:
            if position in encountered:
                continue
            encountered.add(position)
        elevation = grid[position]
        if elevation == 9:
            score += 1
            continue
        surrounding = [
            position + direction
            for direction in [1, -1, 1j, -1j]
            if position + direction in grid
            and grid[position + direction] == elevation + 1
        ]
        queue.extend(surrounding)
    return score


def part1():
    grid, trailheads = get_input()
    print(sum(map(lambda pos: get_score(grid, pos), trailheads)))


def part2():
    grid, trailheads = get_input()
    print(sum(map(lambda pos: get_score(grid, pos, check_visited=False), trailheads)))


if __name__ == "__main__":
    part1()
    part2()
