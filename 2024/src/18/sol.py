import pathlib
from collections import deque

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

SIZE = 70
NUM_OBSTACLES = 1024
# SIZE = 6
# NUM_OBSTACLES = 12


def get_input():
    coords = open(INPUT_PATH / "18").read().splitlines()
    return list(map(lambda l: tuple(map(int, l.split(","))), coords))


def find_path_length(obstacles):
    # Deque with position, number of steps
    steps = deque()
    steps.append(((0, 0), 0))
    visited = set((0, 0))
    while steps:
        step = steps.popleft()
        position = step[0]
        step_num = step[1]
        if position == (SIZE, SIZE):
            return step_num
        candidates = [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        ]
        for candidate in candidates:
            if (
                (candidate not in obstacles)
                and (0 <= candidate[0] <= SIZE)
                and (0 <= candidate[1] <= SIZE)
                and (candidate not in visited)
            ):
                steps.append((candidate, step_num + 1))
                visited.add(candidate)
    return None


def part1():
    obstacle_list = get_input()
    print(find_path_length(obstacle_list[:NUM_OBSTACLES]))


def part2():
    obstacle_list = get_input()
    lower_lim = NUM_OBSTACLES
    upper_lim = len(obstacle_list)
    while upper_lim - lower_lim > 1:
        print(lower_lim, upper_lim)
        num_obstacles = (upper_lim + lower_lim) // 2
        num_steps = find_path_length(obstacle_list[:num_obstacles])
        if num_steps is None:
            # Too many
            upper_lim = num_obstacles
        else:
            # Too few
            lower_lim = num_obstacles
    print(
        num_obstacles - 1,
        obstacle_list[num_obstacles - 1],
        find_path_length(obstacle_list[: num_obstacles - 1]),
    )
    print(
        num_obstacles,
        obstacle_list[num_obstacles],
        find_path_length(obstacle_list[:num_obstacles]),
    )
    print(
        num_obstacles + 1,
        obstacle_list[num_obstacles + 1],
        find_path_length(obstacle_list[: num_obstacles + 1]),
    )


if __name__ == "__main__":
    part1()
    part2()
