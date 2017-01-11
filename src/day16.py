state = "10001110011110000"
# part1
# to_fill = 272
# part2
to_fill = 35651584


def generate_checksum(sequence: str):
    pairs = [(sequence[i], sequence[i + 1]) for i in range(0, sequence.__len__(), 2)]
    checksum = ""
    for (x, y) in pairs:
        if x == y:
            checksum += '1'
        else:
            checksum += '0'
    return checksum


while state.__len__() < to_fill:
    # b = reversed(initial_state)
    b = state[::-1]
    # can't replace 1 with 0 as it would be lost in the next step so first replace it with a marker
    b = b.replace("1", ".").replace("0", "1").replace(".", "0")
    state = state + '0' + b
checksum_input = state[:to_fill]
checksum = generate_checksum(checksum_input)
while checksum.__len__() % 2 == 0:
    checksum = generate_checksum(checksum)
print(checksum)
