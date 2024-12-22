import pathlib
from functools import cache
from itertools import accumulate, repeat

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_input():
    seeds = list(map(int, open(INPUT_PATH / "22").read().splitlines()))
    return seeds

@cache
def compute_next(num):
    num = (num*64 ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = (num*2048 ^ num) % 16777216
    return num

def run_iterations(num, num_iters=2000):
    for _ in range(num_iters):
        num = compute_next(num)
    return num

def get_scores_for_sequences(ones, diff):
    scores = {}
    for i in range(len(diff)-3):
        pattern = (diff[i], diff[i+1], diff[i+2], diff[i+3])
        if pattern not in scores:
            scores[pattern] = ones[i+4]
    return scores

def part1():
    seeds = get_input()
    print(sum(map(run_iterations, seeds)))

def part2():
    seeds = get_input()
    score = {}
    for seed in seeds:
        ones = list(map(lambda n: n%10, accumulate(repeat(1,2000), lambda v, tmp: compute_next(v), initial=seed)))
        diff = [ones[i+1] - ones[i] for i in range(len(ones)-1)]
        scores = get_scores_for_sequences(ones, diff)
        for sequence, val in scores.items():
            if sequence not in score:
                score[sequence] = val
            else:
                score[sequence] += val
    print(max(score.values()))


if __name__ == "__main__":
    part1()
    part2()