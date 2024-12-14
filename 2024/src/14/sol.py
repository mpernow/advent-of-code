import pathlib
import re

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

# SIZE = (11, 7)
SIZE = (101, 103)

def get_input():
    robots = open(INPUT_PATH / "14").readlines()
    robots = list(map(lambda robot: re.findall(r"-?\d+", robot), robots))
    robots = list(map(lambda r: list(map(int, r)), robots))
    return robots

def part1():
    robots = get_input()
    num_seconds = 100
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        x = robot[0]
        y = robot[1]
        vx = robot[2]
        vy = robot[3]
        final_x = (x + vx*num_seconds) % SIZE[0]
        final_y = (y + vy*num_seconds) % SIZE[1]
        if final_x <SIZE[0] //2 and final_y < SIZE[1]//2:
            q1 += 1
        elif final_x < SIZE[0]//2 and final_y > SIZE[1] //2:
            q2 += 1
        elif final_x>SIZE[0]//2 and final_y < SIZE[1] // 2:
            q3 += 1
        elif final_x > SIZE[0]//2 and final_y> SIZE[1] //2:
            q4 += 1
    print(q1*q2*q3*q4)

def part2():
    robots = get_input()
    for t in range(SIZE[0] * SIZE[1]+1):
        robots = [[(r[0] + r[2]) % SIZE[0], (r[1] + r[3]) % SIZE[1], r[2], r[3]] for r in robots]
        unique = {(r[0], r[1]) for r in robots}
        if len(unique) == len(robots):
            print(t)


if __name__ == "__main__":
    part1()
    part2()
