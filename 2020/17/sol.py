from itertools import product

f = open('cubes', 'r')
#f = open('test', 'r')
cubes = f.readlines()
f.close()

cubes = [row.replace('\n', '') for row in cubes]

#print(cubes)

coords = {}
for row in range(len(cubes)):
    for col in range(len(cubes[row])):
        coords[(row, col, 0)] = cubes[row][col]
#print(coords)

# Pad out the coordinates in each dimension. We need six cycles, so six in each dimension

for row in range(-6, len(cubes)+7):
    for col in range(-6, len(cubes[0])+7):
        for depth in range(-6,+7):
            coord = (row, col, depth)
            if coord not in coords:
                coords[coord] = '.'
#print(len(coords))

def cycle(coords):
    new = {}
    for coord in coords:
#        print(coord)
        num_active = 0
        offset = list(product((-1,0,1),repeat=3))
        offset.remove((0,0,0))
        for o in offset:
            neighbour = tuple([coord[i]+o[i] for i in range(3)])
            if (neighbour in coords):
                if coords[neighbour] == '#':
                    num_active += 1
        if (coords[coord] == '#'):
            if (num_active == 2) or (num_active == 3):
                new[coord] = '#'
            else:
                new[coord] = '.'
        elif coords[coord] == '.':
            if num_active == 3:
                new[coord] = '#'
            else:
                new[coord] = '.'
#        if num_active > 0:
#            print(coord, num_active)
    return new

def count(coords):
    tot = 0
    for coord in coords:
        if coords[coord] == '#':
            tot += 1
    return tot

cycle(coords)
for i in range(6):
    coords = cycle(coords)
    print(count(coords))

# Part 2: Same code, but 4 dimenstions


coords = {}
for row in range(len(cubes)):
    for col in range(len(cubes[row])):
        coords[(row, col, 0, 0)] = cubes[row][col]
#print(coords)

# Pad out the coordinates in each dimension. We need six cycles, so six in each dimension

for row in range(-6, len(cubes)+7):
    for col in range(-6, len(cubes[0])+7):
        for depth in range(-6,+7):
            for w in range(-6,+7):
                coord = (row, col, depth, w)
                if coord not in coords:
                    coords[coord] = '.'
#print(len(coords))

def cycle(coords):
    new = {}
    for coord in coords:
#        print(coord)
        num_active = 0
        offset = list(product((-1,0,1),repeat=4))
        offset.remove((0,0,0,0))
        for o in offset:
            neighbour = tuple([coord[i]+o[i] for i in range(4)])
            if (neighbour in coords):
                if coords[neighbour] == '#':
                    num_active += 1
        if (coords[coord] == '#'):
            if (num_active == 2) or (num_active == 3):
                new[coord] = '#'
            else:
                new[coord] = '.'
        elif coords[coord] == '.':
            if num_active == 3:
                new[coord] = '#'
            else:
                new[coord] = '.'
#        if num_active > 0:
#            print(coord, num_active)
    return new


cycle(coords)
for i in range(6):
    coords = cycle(coords)
    print(count(coords))
