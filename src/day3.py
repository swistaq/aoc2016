import re


def solve1():
    infile = open("resources/day3")
    i = 0
    for line in infile.readlines():
        vals = [k for k in re.split("\s", line) if k]
        vals.sort()
        if int(vals[0]) + int(vals[1]) > int(vals[2]) and int(vals[1]) + int(vals[2]) > int(vals[0]) and int(
                vals[0]) + int(vals[2]) > int(vals[1]):
            i += 1
    print(i)
    infile.close()


def solve2():
    i = 0
    triangles = []
    with open("resources/day3") as infile:
        for l in range(0, 1992, 3):
            lines = [infile.readline(), infile.readline(), infile.readline()]
            lines = [[k for k in re.split("\s", line) if k] for line in lines]
            triangles.append((lines[0][0], lines[1][0], lines[2][0]))
            triangles.append((lines[0][1], lines[1][1], lines[2][1]))
            triangles.append((lines[0][2], lines[1][2], lines[2][2]))
    for (a, b, c) in triangles:
        if isvalid(int(a), int(b), int(c)):
            i += 1
    print(i)


def isvalid(a, b, c):
    return a + b > c and b + c > a and c + a > b


if __name__ == "__main__":
    solve1()
    solve2()
