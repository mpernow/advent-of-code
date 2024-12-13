import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    map_ = open(INPUT_PATH / "12").read()
    grid = {
        i + j * 1j: c
        for i, line in enumerate(map_.splitlines())
        for j, c in enumerate(line.strip())
    }
    return grid


def get_patches(grid):
    patches = {p: {p} for p in grid}
    for p in grid:
        for n in p + 1, p - 1, p + 1j, p - 1j:
            if n in grid and grid[p] == grid[n]:
                patches[p] |= patches[n]
                for x in patches[p]:
                    patches[x] = patches[p]
    patches = {tuple(s) for s in patches.values()}
    return patches


def part1():
    grid = get_input()
    patches = get_patches(grid)
    perimeter = lambda ps: sum(
        4 - len({p + 1, p - 1, p + 1j, p - 1j} & {*ps}) for p in ps
    )
    print(sum(len(s) * perimeter(s) for s in patches))


def part2():
    grid = get_input()
    patches = get_patches(grid)
    num_corners = 0
    for s in patches:
        num_corners_this = 0
        for p in s:
            neighbours = {
                p + 1 - 1j: p + 1 - 1j in s,
                p + 1: p + 1 in s,
                p + 1 + 1j: p + 1 + 1j in s,
                p + 1j: p + 1j in s,
                p - 1j: p - 1j in s,
                p - 1 - 1j: p - 1 - 1j in s,
                p - 1: p - 1 in s,
                p - 1 + 1j: p - 1 + 1j in s,
            }
            # Check how many outer corners
            num_direct_neighbors = sum(
                [
                    neighbours[p + 1],
                    neighbours[p + 1j],
                    neighbours[p - 1],
                    neighbours[p - 1j],
                ]
            )
            if num_direct_neighbors == 4:
                pass
            if num_direct_neighbors == 3:
                pass
            if num_direct_neighbors == 2:
                if (neighbours[p + 1] and neighbours[p - 1]) or (
                    neighbours[p + 1j] and neighbours[p - 1j]
                ):
                    pass
                else:
                    num_corners_this += 1
            if num_direct_neighbors == 1:
                num_corners_this += 2
            if num_direct_neighbors == 0:
                num_corners_this += 4

            # Check how many inner corners:
            if (
                (not neighbours[p + 1 + 1j])
                and neighbours[p + 1]
                and neighbours[p + 1j]
            ):
                num_corners_this += 1
            if (
                (not neighbours[p + 1 - 1j])
                and neighbours[p + 1]
                and neighbours[p - 1j]
            ):
                num_corners_this += 1
            if (
                (not neighbours[p - 1 + 1j])
                and neighbours[p - 1]
                and neighbours[p + 1j]
            ):
                num_corners_this += 1
            if (
                (not neighbours[p - 1 - 1j])
                and neighbours[p - 1]
                and neighbours[p - 1j]
            ):
                num_corners_this += 1

        num_corners += num_corners_this * len(s)
    print(num_corners)


if __name__ == "__main__":
    part1()
    part2()
