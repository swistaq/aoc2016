import re

test1 = "aaaaa-bbb-z-y-x-123[abxyz]"
test2 = "a-b-c-d-e-f-g-h-987[abcde]"
test3 = "not-a-real-room-404[oarel]"
test4 = "totally-real-room-200[decoy]"


def parse(a):
	stats = []
	out, roomno, checksum = a[:-11], a[-11: -8], a[-7: -2]
	out = out.replace("-", "")
	out = re.findall("([a-z])", out)
	for letter in set(out):
		stats.append((letter, out.count(letter)))
	stats = sorted(stats, key=lambda x: (-x[1], x[0]), reverse=False)
	keys = stats[:5]
	chars = [i for (i, j) in keys]
	code = ""
	for k in chars:
		code += k
	print(code == checksum, code, checksum, roomno)
	return int(roomno) if code == checksum else 0


def parse2(a):
	stats = []
	out, roomno, checksum = a[:-11], int(a[-11: -8]), a[-7: -2]
	out = out.replace("-", "")
	out = re.findall("([a-z])", out)
	charizard = ""
	for letter in out:
		letter2 = chr((ord(letter) - 97 + roomno) % 26 + 97)
		charizard += letter2
	for letter in set(out):
		stats.append((letter, out.count(letter)))
	stats = sorted(stats, key=lambda x: (-x[1], x[0]), reverse=False)
	keys = stats[:5]
	chars = [i for (i, j) in keys]
	code = ""
	for k in chars:
		code += k
	return (charizard, roomno) if code == checksum else (None, None)


if __name__ == "__main__":
	i = 0
	# part1
	# with open("resources/day4") as infile:
	# 	for line in infile.readlines():
	# 		i += parse(line)
	# print(i)
	# part2
	with open("resources/day4") as infile:
		for line in infile.readlines():
			(a, b) = parse2(line)
			if a is not None and "north" in a:
				print(b)
