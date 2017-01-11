import re

discs = []

with open("resources/day15") as infile:
    for line in infile:
        match = re.match("Disc\s#(\d+)\shas\s(\d+)\spositions;\sat\stime=0,\sit\sis\sat\sposition\s(\d+)", line)
        discs.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))
done = False
time = 0
while not done:
    current_disc = 0
    step = True
    while step and current_disc < discs.__len__():
        (disc_id, positions, start) = discs[current_disc]
        if (time + disc_id + start) % positions != 0:
            step = False
        current_disc += 1
    if step and current_disc == discs.__len__():
        done = True
    time += 1
print(time - 1)
