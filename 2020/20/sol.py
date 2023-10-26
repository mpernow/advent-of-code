import numpy as np
import re

f = open('tiles', 'r')
#f = open('test', 'r')
tiles = [line.replace('\n','') for line in f.readlines()]
f.close()


idxs = [-1] + [i for i, val in enumerate(tiles) if val == ''] + [len(tiles)]
tiles = [tiles[i+1:j] for i, j in zip(idxs, idxs[1:])]

w, h = len(tiles[0][2]), len(tiles[0])-1

tiles = {int(tile[0][5:-1]): tile[1:] for tile in tiles}
#print(tiles)

def get_borders(tile):
    return [tile[0], ''.join([row[0] for row in tile]), tile[-1], ''.join([row[-1] for row in tile])]

def get_flipped_borders(tile):
    borders = get_borders(tile)
    return [border[::-1] for border in borders]

def get_all_borders(tile):
    borders = get_borders(tile)
    flip = get_flipped_borders(tile)
    return borders + flip

def get_neighbours(tile, tiles):
    borders = get_all_borders(tiles[tile])
#    n = 0
    neighs = []
    for neigh in tiles:
        if neigh != tile:
            neigh_bords = get_borders(tiles[neigh])
            for bord in neigh_bords:
                if bord in borders:
                    neighs.append(neigh)
#                    print(neigh)
#    print(n)
    return neighs



neigh = {}
for tile in tiles:
#    print(tile)
    neigh[tile] = get_neighbours(tile, tiles)
#print(neigh)

prod = 1
for tile in neigh:
    if len(neigh[tile]) == 2:
        prod *= tile
print(prod)

#print(neigh)

# Part 2
corners = [tile for tile in neigh if len(neigh[tile])==2]
#print(corners)
borders = [tile for tile in neigh if len(neigh[tile])==3]
#print(borders)

# Start by setting one corner tile in position 0,0
l = int(len(tiles)**0.5)
grid = [[None for _ in range(l)] for _ in range(l)]
grid[0][0] = corners[0]
#print(grid)

def rotate_left(tile):
    tile = np.array([list(row) for row in tile])
    tile = np.rot90(tile)
    return [''.join(list(row)) for row in tile]

def flip_ud(tile):
    tile = np.array([list(row) for row in tile])
    tile = np.flipud(tile)
    return [''.join(list(row)) for row in tile]

def get_right(tile, tiles):
    to_match = ''.join([row[-1] for row in tiles[tile]])
    for neigh in tiles:
        if neigh != tile:
            bords = get_all_borders(tiles[neigh])
            if to_match in bords:
                idx = bords.index(to_match)
                if idx == 0:
                    tiles[neigh] = flip_ud(rotate_left(tiles[neigh]))
                elif idx == 1:
                    tiles[neigh] = tiles[neigh]
                elif idx == 2:
                    tiles[neigh] = rotate_left(rotate_left(rotate_left(tiles[neigh])))
                elif idx == 3:
                    tiles[neigh] = flip_ud(rotate_left(rotate_left(tiles[neigh])))
                elif idx == 4:
                    tiles[neigh] = rotate_left(tiles[neigh])
                elif idx == 5:
                    tiles[neigh] = flip_ud(tiles[neigh])
                elif idx == 6:
                    tiles[neigh] = flip_ud(rotate_left(rotate_left(rotate_left(tiles[neigh]))))
                elif idx == 7:
                    tiles[neigh] = rotate_left(rotate_left(tiles[neigh]))
                return neigh

def get_below(tile, tiles):
    to_match = tiles[tile][-1]
    for neigh in tiles:
        if neigh != tile:
            bords = get_all_borders(tiles[neigh])
            if to_match in bords:
                idx = bords.index(to_match)
                if idx == 0:
                    tiles[neigh] = tiles[neigh]
                elif idx == 1:
                    tiles[neigh] = rotate_left(rotate_left(rotate_left(flip_ud(tiles[neigh]))))
                elif idx == 2:
                    tiles[neigh] = flip_ud(tiles[neigh])
                elif idx == 3:
                    tiles[neigh] = rotate_left(tiles[neigh])
                elif idx == 4:
                    tiles[neigh] = [row[::-1] for row in tiles[neigh]]
                elif idx == 5:
                    tiles[neigh] = rotate_left(rotate_left(rotate_left(tiles[neigh])))
                elif idx == 6:
                    tiles[neigh] = rotate_left(rotate_left(tiles[neigh]))
                elif idx == 7:
                    tiles[neigh] = rotate_left(flip_ud(tiles[neigh]))
                return neigh

#print(corners[0])
# If the chosen corner has no neighbour below or to right, flip:
if get_below(corners[0], tiles) == None:
    tiles[corners[0]] = tiles[corners[0]][::-1]
if get_right(corners[0], tiles) == None:
    tiles[corners[0]] = [row[::-1] for row in tiles[corners[0]]]

#print(get_right(corners[0], tiles))
current = corners[0]
for row in range(l):
    for col in range(1, l):
        current = get_right(current, tiles)
        grid[row][col] = current
    if row < l-1:
        current = get_below(grid[row][0], tiles)
        grid[row+1][0] = current
print(grid)

lines = []
for grid_row in range(l):
    for row in range(1,h-1):
        lines.append(''.join([tiles[grid[grid_row][i]][row][1:-1] for i in range(l)]))
#print(len(lines))
[print(line) for line in lines]



orientations = [lines]
orientations.append(rotate_left(lines))
orientations.append(rotate_left(rotate_left(lines)))
orientations.append(rotate_left(rotate_left(rotate_left(lines))))
orientations.append(flip_ud(lines))
orientations.append(flip_ud(rotate_left(lines)))
orientations.append(flip_ud(rotate_left(rotate_left(lines))))
orientations.append(rotate_left(flip_ud(lines)))


# 20 long
l2 = len(lines[0]) - 20
monster = '..................#.'+'.{'+str(l2)+'}#....##....##....###'+'.{'+str(l2)+'}.#..#..#..#..#..#...'
#print(monster)

num_monsters = [len(re.findall(monster, ''.join(o))) for o in orientations]
print(num_monsters)

o = [n > 0 for n in num_monsters].index(True)
#print(o)

indxs = [(m.start(0)%len(lines[0]))<75 for m in re.finditer(monster, ''.join(orientations[o]))]

print(indxs)
n = indxs.count(True)
print(n)
#n = max(num_monsters)
print(''.join(lines).count('#') - n * monster.count('#'))

#print(''.join(lines).count('#'))
#print(monster.count('#'))

