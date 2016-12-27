from __future__ import print_function
import re

screen_width = 50
screen_height = 6
screen = [['.' for col in range(screen_width)] for row in range(screen_height)]


def print_screen():
    for row in screen:
        print(*row, sep="")


def rotaterow(id, offset):
    global screen
    tmp = [screen[id][i] for i in range(screen_width)]
    for x in range(screen_width):
        screen[id][(x + offset) % screen_width] = tmp[x]


def rotatecol(id, offset):
    global screen
    tmp = [screen[i][id] for i in range(screen_height)]
    for x in range(screen_height):
        screen[(x + offset) % screen_height][id] = tmp[x]


def rotate(switch, id, offset):
    if switch == 'x':
        rotatecol(id, offset)
    elif switch == 'y':
        rotaterow(id, offset)


def draw_rect(x, y):
    global screen
    for row in range(x):
        for col in range(y):
            screen[col][row] = '#'


def parse(line):
    if line.startswith("rect"):
        match = re.search("(\d+)[x](\d+)", line)
        draw_rect(int(match.group(1)), int(match.group(2)))
    if line.startswith("rotate"):
        match = re.search("([y|x])=(\d+)\sby\s(\d+)", line)
        rotate(match.group(1), int(match.group(2)), int(match.group(3)))
        print(line, match.groups(), match.group(0) + "\n", match.group(1), match.group(2), match.group(3))


if __name__ == "__main__":
    global screen
    with open("resources/day8") as infile:
        for line in infile:
            parse(line)
    print_screen()
    i = 0
    for col in range(screen_width):
        for row in range(screen_height):
            if screen[row][col] == '#':
                i += 1
    print("ON:", i)
