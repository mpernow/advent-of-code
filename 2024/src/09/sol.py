import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_input():
    data = open(INPUT_PATH / "09").read()
    return data


def parse_blocks(data):
    output = []
    is_data = True
    block_num = 0
    for value in data:
        if is_data:
            output += [block_num] * int(value)
            block_num += 1
        else:
            output += [-1] * int(value)
        is_data = not is_data
    return output


def compress1(blocks):
    front_idx = 0
    back_idx = len(blocks) - 1
    while back_idx > front_idx:
        while blocks[front_idx] != -1:
            front_idx += 1
        while blocks[back_idx] == -1:
            back_idx -= 1
        if front_idx >= back_idx:
            break
        blocks[front_idx] = blocks[back_idx]
        blocks[back_idx] = -1
    return blocks


def find_first_empty_block(blocks, length):
    idx = 0
    found_empty = False
    while not found_empty:
        empty_length = 1
        try:
            while blocks[idx + empty_length] == blocks[idx]:
                empty_length += 1
        except IndexError:
            pass
        if empty_length >= length and blocks[idx] == -1:
            break
        idx += empty_length
        if idx >= len(blocks):
            return None
    return idx


def compress2(blocks):
    back_idx = len(blocks) - 1
    while back_idx > 0:
        while blocks[back_idx] == -1:
            back_idx -= 1
        length = 1
        while blocks[back_idx - length] == blocks[back_idx]:
            length += 1
        # Find the empty blocks
        front_idx = find_first_empty_block(blocks[:back_idx], length)
        if not front_idx:
            back_idx -= length
            continue
        blocks[front_idx : front_idx + length] = blocks[
            back_idx - length + 1 : back_idx + 1
        ]
        blocks[back_idx - length + 1 : back_idx + 1] = [-1] * length
        back_idx -= length
    return blocks


def compute_checksum(compressed):
    return sum(i * val for i, val in enumerate(compressed) if val != 1)


def part1():
    data = get_input()
    blocks = parse_blocks(data)
    compressed = compress1(blocks)
    print(compute_checksum(compressed))


def part2():
    data = get_input()
    blocks = parse_blocks(data)
    compressed = compress2(blocks)
    print(compute_checksum(compressed))


if __name__ == "__main__":
    part1()
    part2()
