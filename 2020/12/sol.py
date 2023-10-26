from math import *

f = open('directions', 'r')
#f = open('test', 'r')
directions = [line.replace('\n','') for line in f.readlines()]
f.close()

#print(directions)


# Describe ship by x, y, angle from x (East = 0, North = 90)
ship = [0, 0, 0]

def update(current, direction):
    x = current[0]
    y = current[1]
    angle = current[2]
    if direction[0] == 'N':
        y += int(direction[1:])
    elif direction[0] == 'S':
        y -= int(direction[1:])
    elif direction[0] == 'E':
        x += int(direction[1:])
    elif direction[0] == 'W':
        x -= int(direction[1:])
    elif direction[0] == 'L':
        angle += int(direction[1:])
    elif direction[0] == 'R':
        angle -= int(direction[1:])
    elif direction[0] == 'F':
        x += int(direction[1:]) * cos(angle*3.14159265/180)
        y += int(direction[1:]) * sin(angle*3.14159265/180)
    else:
        raise ValueError('Directions not recognised' + direction)
    return [x, y, angle]


for direction in directions:
    ship = update(ship, direction)
#    print(ship)
print(abs(ship[0]) + abs(ship[1]))

# Part 2

def update2(ship, waypoint, direction):
    x_ship = ship[0]
    y_ship = ship[1]
    x_waypoint = waypoint[0]
    y_waypoint = waypoint[1]
    if direction[0] == 'N':
        y_waypoint += int(direction[1:])
    elif direction[0] == 'S':
        y_waypoint -= int(direction[1:])
    elif direction[0] == 'E':
        x_waypoint += int(direction[1:])
    elif direction[0] == 'W':
        x_waypoint -= int(direction[1:])
    elif direction[0] == 'L':
        angle = int(direction[1:]) * pi/180
        x_new = x_waypoint * cos(angle) - y_waypoint * sin(angle)
        y_new = x_waypoint * sin(angle) + y_waypoint * cos(angle)
        x_waypoint = x_new
        y_waypoint = y_new
    elif direction[0] == 'R':
        angle = int(direction[1:]) * pi/180
        x_new = x_waypoint * cos(-angle) - y_waypoint * sin(-angle)
        y_new = x_waypoint * sin(-angle) + y_waypoint * cos(-angle)
        x_waypoint = x_new
        y_waypoint = y_new
    elif direction[0] == 'F':
        x_ship += int(direction[1:]) * (x_waypoint)
        y_ship += int(direction[1:]) * (y_waypoint)
    else:
        raise ValueError('Directions not recognised' + direction)
    return [x_ship, y_ship], [x_waypoint, y_waypoint]

ship = [0, 0]
waypoint = [10, 1]

for direction in directions:
    ship, waypoint = update2(ship, waypoint, direction)
#    print(ship, waypoint)
#print(ship)
print(abs(ship[0]) + abs(ship[1]))
