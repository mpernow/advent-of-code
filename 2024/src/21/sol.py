import pathlib
from functools import cache
from itertools import permutations

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"

def get_input():
    codes = open(INPUT_PATH / "21").read().splitlines()
    return codes

numkeypad = ['789',
             '456',
             '123',
             ' 0A']
numkeypad = {key: (x, y) for y, line in enumerate(numkeypad) for x, key in enumerate(line) if key != ' '}

dirkeypad = [' ^A',
             '<v>']
dirkeypad = {key: (x, y) for y, line in enumerate(dirkeypad) for x, key in enumerate(line) if key != ' '}

dirs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

@cache
def get_number_presses(code, depth=2, dirkey=False, cur=None):
    # Working backwards, starting with the keypad
    keypad = dirkeypad if dirkey else numkeypad
    if not code:
        return 0
    # Robots start at 'A'
    if not cur:
        cur = keypad['A']

    cx, cy = cur
    px, py = keypad[code[0]]
    dx, dy = px-cx, py-cy

    # Number of horizontal or vertical steps needed to get to next
    buttons = ''
    if dx > 0:
        buttons += '>'*dx
    elif dx < 0:
        buttons += '<'*-dx
    if dy > 0:
        buttons += 'v'*dy
    elif dy < 0:
        buttons += '^'*-dy
    
    if depth:
        # Try all permutations of the required steps for intermediary buttons
        perm_lens = []
        for perm in set(permutations(buttons)):
            cx, cy = cur
            for button in perm:
                dx, dy = dirs[button]
                cx += dx
                cy += dy
                if (cx, cy) not in keypad.values():
                    break
            else:
                # Add 'A' since needs to press the button
                perm_lens.append(get_number_presses(perm+('A',), depth-1, True))
        min_len = min(perm_lens)
    else:
        # At end, no need to try permutations
        min_len = len(buttons)+1
    # Now remove the processed number and run again for the remaining numbers
    return min_len+get_number_presses(code[1:], depth, dirkey, (px, py))



def part1():
    codes = get_input()
    score = 0
    for code in codes:
        codenum = int(code[:-1]) # They all end in 'A'
        score += codenum*get_number_presses(code)
    print(score)

def part2():
    codes = get_input()
    score = 0
    for code in codes:
        codenum = int(code[:-1]) # They all end in 'A'
        score += codenum*get_number_presses(code, 25)
    print(score)


if __name__ == "__main__":
    part1()
    part2()
