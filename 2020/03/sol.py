f = open('map.dat', 'r')
#f = open('test.dat', 'r')
map = f.readlines()
f.close()

map = [line.strip('\n') for line in map]

width = len(map[0])
height = len(map)

def next(current, right=3, down=1, width=width):
    x = (current[0] + right) % width
    y = current[1] + down
    return (x,y)

def is_tree(pos, map=map):
    x = pos[0]
    y = pos[1]
    if map[y][x] == '#':
        return True
    else:
        return False

def get_num_trees(strategy, width=width, height=height, map=map):
    pos = (0,0)
    num_trees = 0
    
    while pos[1] < height - strategy[1]:
        pos = next(pos, strategy[0], strategy[1])
        #print(pos)
        if is_tree(pos):
            num_trees += 1
            #print('Tree!')
    return num_trees

trees1 = get_num_trees((1,1))
trees2 = get_num_trees((3,1))
trees3 = get_num_trees((5,1))
trees4 = get_num_trees((7,1))
trees5 = get_num_trees((1,2))

print(trees1 * trees2 * trees3 * trees4 * trees5)
