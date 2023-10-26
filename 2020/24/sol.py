from itertools import product

f = open('tiles', 'r')
#f = open('test', 'r')
tiles = [line.replace('\n','') for line in f.readlines()]
f.close()

tmp = []
for line in tiles:
    i = 0
    steps = []
    while i < len(line):
        ch = line[i]
        if ch == 'n' or ch == 's':
            steps.append(line[i:i+2])
            i += 2
        else:
            steps.append(line[i])
            i += 1
    tmp.append(steps)
tiles = tmp
#print(tiles)

# Unit vectors non-orthogonal: one in east and other in north-west
dirs = {'e':(1,0), 'w':(-1,0), 'ne':(1,1), 'nw':(0,1), 'se':(0,-1), 'sw':(-1,-1)}

# Part 1
black = []

for line in tiles:
    current = (0,0)
    for step in line:
        coords = dirs[step]
        current = (current[0] + coords[0], current[1] + coords[1])
    if current in black:
        black.remove(current)
    else:
        black.append(current)
print(len(black))

# Part 2
# Set size of grid
extra = 50
size = max([abs(t[0])+abs(t[1]) for t in black]) + extra

white = []

grid = list(product(range(-size,size+1),repeat=2))
for tile in grid:
    if tile not in black:
        white.append(tile)


def flip(white, black):
    new_white = []
    new_black = []
    for tile in white:
        bs = 0
        for v in dirs.values():
            neigh = (tile[0] + v[0], tile[1] + v[1])
            if neigh in black:
                bs += 1
        if bs == 2:
            new_black.append(tile)
        else:
            new_white.append(tile)
    for tile in black:
        bs = 0
        for v in dirs.values():
            neigh = (tile[0] + v[0], tile[1] + v[1])
            if neigh in black:
                bs += 1
        if (bs == 0) or (bs > 2):
            new_white.append(tile)
        else:
            new_black.append(tile)
    return new_white, new_black

print('\n')
for i in range(100):
    white, black = flip(white, black)
    print(i+1, len(black))
