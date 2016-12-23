import re

input_ = 'R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1'
heading = 'N'
x = 0
y = 0
visited = []


def visit(x, y):
    global visited
    if visited.__contains__((x, y)):
        print "LOCATION"
        print abs(x) + abs(y)
        print ""
    else:
        visited.append((x, y))


def moveN(i):
    global x, y, visited
    for j in range(y + 1, y + i, 1):
        visit(x, j)
    y += i


def moveW(i):
    global x, y, visited
    for j in range(x - i, y - 1, 1):
        visit(j, y)
    x -= i


def moveS(i):
    global x, y, visited
    for j in range(y - i, y - 1, 1):
        visit(x, j)
    y -= i


def moveE(i):
    global x, y, visited
    for j in range(x + 1, x + i, 1):
        visit(j, y)
    x += i


def parsevar(a, b):
    global x, y, heading
    global visited
    b = int(b)
    if heading == 'N':
        if a == 'R':
            heading = 'E'
            moveE(b)
            return
        if a == 'L':
            heading = 'W'
            moveW(b)
            return
    if heading == 'W':
        if a == 'R':
            heading = 'N'
            moveN(b)
            return
        if a == 'L':
            heading = 'S'
            moveS(b)
            return
    if heading == 'S':
        if a == 'R':
            heading = 'W'
            moveW(b)
            return
        if a == 'L':
            heading = 'E'
            moveE(b)
            return
    if heading == 'E':
        if a == 'R':
            heading = 'S'
            moveS(b)
            return
        if a == 'L':
            heading = 'N'
            moveN(b)
            return
    pass


if __name__ == "__main__":
    split = re.split(", ", input_)
    listvar = [[z for z in string if z] for string in [re.split('(\w)(\d*)', string) for string in split]]
    listvar = [tuple(s) for s in listvar]
    print listvar
    for (i, j) in listvar:
        parsevar(i, j)
    print "x=", x, " y=", y
    print heading
