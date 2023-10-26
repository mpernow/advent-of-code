f = open('seating','r')
#f = open('test','r')
seating = f.readlines()
f.close()

seating = [line.replace('\n','') for line in seating]

#print(seating)

def update_seat(i, j, seating):
    if seating[i][j] == '.':
        return '.'
    # Pad the seating with dots, then re-define i,j
    seating = ['.'+line+'.' for line in seating]
    seating = ['.'*len(seating[0])] + seating + ['.'*len(seating[0])]
    neighbours = []
    i += 1
    j += 1
    neighbours.append(seating[i-1][j-1])
    neighbours.append(seating[i-1][j])
    neighbours.append(seating[i-1][j+1])
    neighbours.append(seating[i][j-1])
    neighbours.append(seating[i][j+1])
    neighbours.append(seating[i+1][j-1])
    neighbours.append(seating[i+1][j])
    neighbours.append(seating[i+1][j+1])
    if seating[i][j] == 'L':
        if neighbours.count('#') == 0:
            return '#'
        else:
            return 'L'
    elif seating[i][j] == '#':
        if neighbours.count('#') >= 4:
            return 'L'
        else:
            return '#'

#print(update_seat(0,1,seating))

def next(seating):
    updated = []
    for i in range(len(seating)):
        line = ''
        for j in range(len(seating[i])):
            line += update_seat(i, j, seating)
        updated.append(line)
    return updated

#print(next(next(seating)))

seating_new = next(seating)
while seating_new != seating:
    seating = seating_new
    seating_new = next(seating)
print(seating_new)
occupied = [line.count('#') for line in seating_new]
print(sum(occupied))


### Part 2
# Update the next function for visibility rule and updated rule

def traverse(i, j, seating, direction):
    # Direction is tuple
    # note that i is y-coordinate, and is first in the direction tuple
    if (i == 0 and direction[0] == -1):
        # At top and looking up
        return '.'
    if (i == len(seating)-1 and direction[0] == 1):
        # At bottom and looking down
        return '.'
    if (j == 0 and direction[1] == -1):
        # At left edge and looking left
        return '.'
    if (j == len(seating[0])-1 and direction[1] == 1):
        # At right edge and looking right
        return '.'
    adj = seating[i + direction[0]][j + direction[1]]
    if adj != '.':
        return adj
    else:
        return traverse(i + direction[0], j + direction[1], seating, direction)

#print(traverse(1,1,seating,(1,1)))
#print(traverse(1,1,seating,(1,0)))
#print(traverse(1,1,seating,(0,1)))
#print(traverse(1,1,seating,(-1,0)))

def update_seat2(i, j, seating):
    if seating[i][j] == '.':
        return '.'
    dirs = [(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1)]
    neighbours = [traverse(i, j, seating, direction) for direction in dirs]
    if seating[i][j] == 'L':
        if neighbours.count('#') == 0:
            return '#'
        else:
            return 'L'
    elif seating[i][j] == '#':
        if neighbours.count('#') >= 5:
            return 'L'
        else:
            return '#'

print(update_seat2(0,0,seating))

def next2(seating):
    updated = []
    for i in range(len(seating)):
        line = ''
        for j in range(len(seating[i])):
            line += update_seat2(i, j, seating)
        updated.append(line)
    return updated


# Reload the data:
f = open('seating','r')
#f = open('test','r')
seating = f.readlines()
f.close()
seating = [line.replace('\n','') for line in seating]


seating_new = next2(seating)
while seating_new != seating:
    seating = seating_new
    seating_new = next2(seating)
print(seating_new)
occupied = [line.count('#') for line in seating_new]
print(sum(occupied))
