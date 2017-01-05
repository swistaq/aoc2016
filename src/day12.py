import re
import time

instructions = []
# 'c': 0 for part1
regs = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

with open("resources/day12") as infile:
    for line in infile:
        instructions.append(re.split(" ", line.strip()))
i = 0
while i < instructions.__len__():
    k = instructions[i]
    if k[0] == 'cpy':
        i += 1
        value = k[1]
        target = k[2]
        try:
            regs.update({target: regs[value]})
        except KeyError:
            regs.update({target: int(value)})
    elif k[0] == 'inc':
        i += 1
        regs[k[1]] += 1
    elif k[0] == 'dec':
        i += 1
        regs[k[1]] -= 1
    elif k[0] == 'jnz':
        try:
            if regs[k[1]] > 0:
                i += int(k[2])
            else:
                i += 1
        except KeyError:
            if int(k[1]) >= 0:
                i += int(k[2])
            else:
                i += 1
print(regs)
