import pathlib
from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    grid = open(INPUT_PATH / "16").read().splitlines()
    size = len(grid[0].strip()), len(grid)
    positions = {}
    for r, row in enumerate(grid):
        for c, col in enumerate(row.strip()):
            positions[c + r * 1j] = col
    return positions, size


def part1():
    grid, size = get_input()
    pos = 1 + (size[1] - 2) * 1j
    end = size[0] - 2 + 1j
    dir = 1
    candidates = PriorityQueue()
    candidates.put(PrioritizedItem(0, (pos, dir, 0, [pos])))
    visited = {(pos, dir): 0}
    while candidates.not_empty:
        current = candidates.get().item
        pos = current[0]
        dir = current[1]
        score = current[2]
        if pos == end:
            print(score)
            break
        new_candidates = [
            (pos + dir, dir, score + 1),
            (pos, dir * 1j, score + 1000),
            (pos, dir * -1j, score + 1000),
        ]
        for new_candidate in new_candidates:
            # Accept if in grid, not on a '#', not been visited with lower score, and not already on end
            if (
                grid.get(new_candidate[0]) in [".", "S", "E"]
                and (
                    visited.get((new_candidate[0], new_candidate[1]), 1e10)
                    > new_candidate[2]
                )
                and pos != end
            ):
                candidates.put(PrioritizedItem(new_candidate[2], new_candidate))
                visited[(new_candidate[0], new_candidate[1])] = new_candidate[2]


def part2():
    grid, size = get_input()
    pos = 1 + (size[1] - 2) * 1j
    end = size[0] - 2 + 1j
    dir = 1
    candidates = PriorityQueue()
    candidates.put(PrioritizedItem(0, (pos, dir, 0, [pos])))
    visited = {(pos, dir): 0}
    good_paths = []
    best_score = None
    while candidates.not_empty:
        current = candidates.get().item
        pos = current[0]
        dir = current[1]
        score = current[2]
        prev = current[3]
        if pos == end:
            if best_score is None:
                best_score = score
            if score > best_score:
                break
            good_paths.append((score, prev))
        new_candidates = [
            (pos + dir, dir, score + 1, prev + [pos + dir]),
            (pos, dir * 1j, score + 1000, prev),
            (pos, dir * -1j, score + 1000, prev),
        ]
        for new_candidate in new_candidates:
            # Accept if in grid, not on a '#', not been visited with lower score, and not already on end
            if (
                grid.get(new_candidate[0]) in [".", "S", "E"]
                and (
                    visited.get((new_candidate[0], new_candidate[1]), 1e10)
                    >= new_candidate[2]
                )
                and pos != end
            ):
                candidates.put(PrioritizedItem(new_candidate[2], new_candidate))
                visited[(new_candidate[0], new_candidate[1])] = new_candidate[2]

    visited = set()
    for path in good_paths:
        if path[0] == best_score:
            for pos in path[1]:
                visited.add(pos)
    print(len(visited))


if __name__ == "__main__":
    part1()
    part2()
