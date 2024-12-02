import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def part1():
    with open(INPUT_PATH / "01") as f:
        data = f.readlines()
    data = [line.strip("\n").split(" ") for line in data]
    list1 = [int(line[0]) for line in data]
    list2 = [int(line[-1]) for line in data]

    list1.sort()
    list2.sort()

    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])
    
    print(diff)

def part2():
    with open(INPUT_PATH / "01") as f:
        data = f.readlines()
    data = [line.strip("\n").split(" ") for line in data]
    list1 = [int(line[0]) for line in data]
    list2 = [int(line[-1]) for line in data]

    freq1 = {}
    for num in list1:
        if num in freq1.keys():
            freq1[num] += 1
        else:
            freq1[num] = 1
    freq2 = {}
    for num in list2:
        if num in freq2.keys():
            freq2[num] += 1
        else:
            freq2[num] = 1

    score = 0
    for key, val in freq1.items():
        score += key*val*freq2.get(key, 0)

    print(score)


if __name__ == "__main__":
    part1()
    part2()