import inp  # my [REDACTED] input parser
import math

# this code is UGLY. do NOT read


def main():
    instream = inp.parse_file_str()
    instructions = []
    for direction in instream:
        instructions.append((direction[0], int(direction[1:])))
    x = 0
    y = 0
    theta = 0
    for move in instructions:
        if move[0] == 'N':
            y += move[1]
        elif move[0] == 'S':
            y -= move[1]
        elif move[0] == 'E':
            x += move[1]
        elif move[0] == 'W':
            x -= move[1]
        elif move[0] == 'L':
            theta += move[1]
            theta = theta % 360
        elif move[0] == 'R':
            theta -= move[1]
            theta = theta % 360
        elif move[0] == 'F':
            if theta == 0:  # E
                x += move[1]
            elif theta == 90:
                y += move[1]
            elif theta == 180:
                x -= move[1]
            elif theta == 270:
                y -= move[1]

    return abs(x) + abs(y)


def main2():
    instream = inp.parse_file_str()
    instructions = []
    for direction in instream:
        instructions.append((direction[0], int(direction[1:])))
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1
    theta = math.degrees(math.atan2(way_y, way_x))
    for move in instructions:
        if move[0] == 'N':
            way_y += move[1]
        elif move[0] == 'S':
            way_y -= move[1]
        elif move[0] == 'E':
            way_x += move[1]
        elif move[0] == 'W':
            way_x -= move[1]
        elif move[0] == 'L' or move[0] == 'R':
            dt = math.radians(move[1])
            if move[0] == 'R':
                dt = -dt
            newx = (way_x-ship_x) * round(math.cos(dt)) - (way_y-ship_y) * round(math.sin(dt)) + ship_x
            newy = (way_y-ship_y) * round(math.cos(dt)) + (way_x-ship_x) * round(math.sin(dt)) + ship_y
            way_x = newx
            way_y = newy
        elif move[0] == 'F':
            dx = way_x - ship_x
            dy = way_y - ship_y
            ship_x += dx * move[1]
            ship_y += dy * move[1]
            way_x += dx * move[1]
            way_y += dy * move[1]

    return abs(ship_x) + abs(ship_y)


print(f'part 1: {main()}')
print(f'part 2: {main2()}')  # i learned the power of python 3.6 format strings
