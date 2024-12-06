import pathlib
import re

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

next_dir = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def get_input():
    map_ = open(INPUT_PATH / "06").read().split("\n")
    obstacles = []
    for ind, line in enumerate(map_):
        obstacles += [(ind, m.start()) for m in re.finditer("#", line)]
    for ind, line in enumerate(map_):
        pos = line.find("^")
        start_pos = (ind, pos)
        if pos > 0:
            break
    size = (len(map_), len(map_[0]))
    return obstacles, start_pos, size


def get_visited(obstacles, pos, size, direction):
    visited = set()
    visited_with_dir = set()
    loop = False
    while True:
        if direction == (-1, 0):
            obstacle = min(
                [
                    obstacle
                    for obstacle in obstacles
                    if obstacle[1] == pos[1] and obstacle[0] < pos[0]
                ],
                key=lambda coord: (pos[0] - coord[0]) % size[0],
                default=(-1, pos[1]),
            )
            new_visited = set([(i, pos[1]) for i in range(pos[0], obstacle[0], -1)])
            new_with_dir = set(
                [(i, pos[1], direction) for i in range(pos[0], obstacle[0], -1)]
            )
            # TODO check if visited_with_dir.disjoint(new_with_dir)
            if not visited_with_dir.isdisjoint(new_with_dir):
                loop = True
                break
            visited_with_dir |= new_with_dir
            visited |= new_visited
            if obstacle[0] == -1:
                break
            pos = (obstacle[0] + 1, obstacle[1])
            direction = next_dir[direction]
        elif direction == (0, 1):
            obstacle = min(
                [
                    obstacle
                    for obstacle in obstacles
                    if obstacle[0] == pos[0] and obstacle[1] > pos[1]
                ],
                key=lambda coord: (coord[1] - pos[1]) % size[1],
                default=(pos[0], size[1]),
            )
            new_visited = set([(pos[0], i) for i in range(pos[1], obstacle[1])])
            new_with_dir = set(
                [(pos[0], i, direction) for i in range(pos[1], obstacle[1])]
            )
            if not visited_with_dir.isdisjoint(new_with_dir):
                loop = True
                break
            visited_with_dir |= new_with_dir
            visited |= new_visited
            if obstacle[1] == size[1]:
                break
            pos = (obstacle[0], obstacle[1] - 1)
            direction = next_dir[direction]
        elif direction == (1, 0):
            obstacle = min(
                [
                    obstacle
                    for obstacle in obstacles
                    if obstacle[1] == pos[1] and obstacle[0] > pos[0]
                ],
                key=lambda coord: (coord[0] - pos[0]) % size[0],
                default=(size[0], pos[1]),
            )
            new_visited = set([(i, pos[1]) for i in range(pos[0], obstacle[0])])
            new_with_dir = set(
                [(i, pos[1], direction) for i in range(pos[0], obstacle[0])]
            )
            if not visited_with_dir.isdisjoint(new_with_dir):
                loop = True
                break
            visited_with_dir |= new_with_dir
            visited |= new_visited
            if obstacle[0] == size[0]:
                break
            pos = (obstacle[0] - 1, obstacle[1])
            direction = next_dir[direction]
        else:  # direction (0, -1)
            obstacle = min(
                [
                    obstacle
                    for obstacle in obstacles
                    if obstacle[0] == pos[0] and obstacle[1] < pos[1]
                ],
                key=lambda coord: (pos[1] - coord[1]) % size[1],
                default=(pos[0], -1),
            )
            new_visited = set([(pos[0], i) for i in range(pos[1], obstacle[1], -1)])
            new_with_dir = set(
                [(pos[0], i, direction) for i in range(pos[1], obstacle[1], -1)]
            )
            if not visited_with_dir.isdisjoint(new_with_dir):
                loop = True
                break
            visited_with_dir |= new_with_dir
            visited |= new_visited
            if obstacle[1] == -1:
                break
            pos = (obstacle[0], obstacle[1] + 1)
            direction = next_dir[direction]
    return visited, loop


def part1():
    obstacles, pos, size = get_input()
    direction = (-1, 0)
    visited, _ = get_visited(obstacles, pos, size, direction)
    print(len(visited))


def part2():
    obstacles, pos, size = get_input()
    direction = (-1, 0)
    candidates, _ = get_visited(obstacles, pos, size, direction)
    candidates.remove(pos)
    # For each candidate, add to obstacles, run through and check whether loop detected
    num_loops = 0
    count = 1
    for candidate in candidates:
        print(f"{count}/{len(candidates)}")
        _, is_loop = get_visited(obstacles + [candidate], pos, size, direction)
        num_loops += is_loop
        count += 1
    print(num_loops)


if __name__ == "__main__":
    part1()
    part2()
