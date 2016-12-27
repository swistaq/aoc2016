from __future__ import print_function
import re


def parse(str):
    match = re.search("\((\d+)x(\d+)\)", str)
    if match:
        return int(match.group(1)), int(match.group(2))


def parsesub(input):
    length = 0
    offset = 0
    while True:
        buff = input[offset:offset + 1]
        if not buff:
            break
        if buff == '(':
            i = 1
            next_char = ""
            while next_char != ')':
                next_char = input[offset + i:offset + i + 1]
                i += 1
                buff += next_char
            (x, y) = parse(buff)
            length += y * parsesub(input[offset + i:offset + i + x])
            offset += x + i
        else:
            length += 1
            offset += 1
    return length


def solve(filename, switch):
    with open(filename) as infile:
        length = 0
        while True:
            buff = infile.read(1)
            if not buff:
                break
            if buff == '(':
                next_char = ""
                while next_char != ')':
                    next_char = infile.read(1)
                    buff += next_char
                (x, y) = parse(buff)
                if switch:
                    length += y * parsesub(infile.read(x))
                else:
                    infile.read(x)
                    length += y * x
            else:
                length += 1
    return length

if __name__ == "__main__":
    print(solve("resources/day9", False))
