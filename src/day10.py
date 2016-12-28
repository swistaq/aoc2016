from __future__ import print_function
import re

#   id          low                 high
# {botno : ((bot|output, id), (bot|output, id))}
bots = {}
# (value, botno)
vals = []
# {output_id : [values]}
outputs = {}
# {botno : [values]}
states = {}


def parse(line):
    global bots, vals, outputs
    if line.startswith("bot"):
        match = re.search("bot\s(\d+)\sgives low to (bot|output)\s(\d+) and high to (bot|output)\s(\d+)", line)
        bots.update(
            {int(match.group(1)): ((match.group(2), int(match.group(3))), (match.group(4), int(match.group(5))))})
    elif line.startswith("value"):
        match = re.search("value\s(\d+)\sgoes to bot\s(\d+)", line)
        vals.append((int(match.group(1)), int(match.group(2))))


def update_output(output_id, value):
    global outputs
    if outputs.has_key(output_id):
        outputs.get(output_id).append(value)
    else:
        outputs.update({output_id: [value]})


def update_bot(bot_no, value):
    global states, special_bot
    if states.has_key(bot_no):
        states.get(bot_no).append(value)
        if states.get(bot_no).__len__() == 2:
            vals = sorted(states.get(bot_no))
            if vals[0] == 17 and vals[1] == 61:
                print("BOT COMPARING 17 AND 61:", bot_no)
            states.update({bot_no: []})
            ((target_low, targe_low_id), (target_high, target_high_id)) = bots.get(bot_no)
            if target_low == "bot":
                update_bot(targe_low_id, vals[0])
            elif target_low == "output":
                update_output(targe_low_id, vals[0])
            if target_high == "bot":
                update_bot(target_high_id, vals[1])
            elif target_high == "output":
                update_output(target_high_id, vals[1])

    else:
        states.update({bot_no: [value]})


if __name__ == "__main__":
    with open("resources/day10") as infile:
        for line in infile:
            parse(line)
    for val in vals:
        update_bot(val[1], val[0])
    print(outputs.get(0)[0]*outputs.get(1)[0]*outputs.get(2)[0])
