import pathlib
import re
from functools import cache
from itertools import combinations

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_input():
    inputs, gates = open(INPUT_PATH/"24", "r").read().split("\n\n")

    input_pattern = r"([xy]\d\d): ([10])"
    input_vals = {}
    for line in inputs.split("\n"):
        match = re.search(input_pattern, line)
        input_name, val = match.groups()
        val = int(val)
        input_vals[input_name] = val

    gate_pattern = r"([a-z0-9]{3}) ([XORAND]+) ([a-z0-9]{3}) -> ([a-z0-9]{3})"
    ops = set()
    op_list = []
    for line in gates.split("\n"):
        match = re.search(gate_pattern, line)
        x1, op, x2, res = match.groups()
        ops.add((x1, x2, res, op))
        op_list.append((x1, x2, res, op))
    
    return input_vals, ops, op_list


def part1(input_vals, ops):
    # The outputs form tree structure with input nodes as leaves
    parents = {}
    op_map = {}  # Mapping output name to corresponding operation (XOR, OR, AND)
    for x1, x2, res, op in ops:
        parents[res] = (x1, x2)
        op_map[res] = op

    @cache
    def get_depth(reg):
        if reg in input_vals:
            return 0
        x1, x2 = parents[reg]
        return max(get_depth(x1), get_depth(x2)) + 1

    # Calculate in optimal order
    vars = [(res, get_depth(res)) for _, _, res, _ in ops]
    vars.sort(key=lambda x: x[1])  # Process lower depth first
    for reg, _ in vars:
        x1, x2 = parents[reg]
        v1, v2 = input_vals[x1], input_vals[x2]
        op = op_map[reg]
        val = {
            "XOR": lambda a, b: a ^ b,
            "OR": lambda a, b: a | b,
            "AND": lambda a, b: a & b,
        }[op](v1, v2)
        input_vals[reg] = val

    # Concatenate outputs -> binary -> decimal
    regs = list(input_vals.items())
    regs.sort(key=lambda x: x[0])
    num_out = int(str(regs[-1][0])[-2:]) + 1
    bin_str = "".join(str(val) for _, val in regs[-num_out:])
    ans1 = int(bin_str[::-1], 2)

    print(ans1)

def part2(op_list):
    # Given the list of operations, see how far we get and keep track of wires that must be correct.
    # Derive which input lines corresponded to which wires in a ripple-carry adder. "Commit point" is when the output matches z15 or whatever -- we know everything that that output depended on must be correct.
    def furthest_made(op_list):
        ops = {}
        for x1, x2, res, op in op_list:
            ops[(frozenset([x1, x2]), op)] = res  # hashability reason

        # here, x1 and x2 can be provided in any order
        def get_res(x1, x2, op):
            return ops.get((frozenset([x1, x2]), op), None)

        carries = {}
        correct = set()
        prev_intermediates = set()
        for i in range(45):
            pos = f"0{i}" if i < 10 else str(i)
            predigit = get_res(f"x{pos}", f"y{pos}", "XOR")
            precarry1 = get_res(f"x{pos}", f"y{pos}", "AND")
            if i == 0:
                # only two, XOR and AND
                carries[i] = precarry1
                continue
            digit = get_res(carries[i - 1], predigit, "XOR")
            if digit != f"z{pos}":
                return i - 1, correct

            # If it did work, we know carries[i-1] and predigit were correct
            correct.add(carries[i - 1])
            correct.add(predigit)
            # Also add variables from previous position's ripple-carry adder module
            for wire in prev_intermediates:
                correct.add(wire)

            # Next, we compute the carries
            precarry2 = get_res(carries[i - 1], predigit, "AND")
            carry_out = get_res(precarry1, precarry2, "OR")
            carries[i] = carry_out
            prev_intermediates = set([precarry1, precarry2])

        return 45, correct

    swaps = set()

    base, base_used = furthest_made(op_list)
    for _ in range(4):
        # try swapping
        for i, j in combinations(range(len(op_list)), 2):
            x1_i, x2_i, res_i, op_i = op_list[i]
            x1_j, x2_j, res_j, op_j = op_list[j]
            # Don't switch z00 out
            if "z00" in (res_i, res_j):
                continue
            # Don't switch if these wires have already been used
            if res_i in base_used or res_j in base_used:
                continue
            # Switch output wires
            op_list[i] = x1_i, x2_i, res_j, op_i
            op_list[j] = x1_j, x2_j, res_i, op_j
            attempt, attempt_used = furthest_made(op_list)
            if attempt > base:
                print(f"Found a good swap. Got to a higher iteration number: {attempt}")
                swaps.add((res_i, res_j))
                base, base_used = attempt, attempt_used
                break
            # Switch output wires back
            op_list[i] = x1_i, x2_i, res_i, op_i
            op_list[j] = x1_j, x2_j, res_j, op_j

    ans2 = ",".join(sorted(sum(swaps, start=tuple())))

    print(ans2)

if __name__ == "__main__":
    input_vals, ops, op_list = get_input()

    part1(input_vals, ops)
    part2(op_list)

