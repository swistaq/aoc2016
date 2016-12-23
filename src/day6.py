from __future__ import print_function


def solve(infile, reverse):
    answer = ""
    chars = ["", "", "", "", "", "", "", ""]
    for line in infile.readlines():
        i = 0
        for char in line:
            if i < 8:
                chars[i] += char
                i += 1
    for s in chars:
        stats = []
        for c in set(s):
            stats.append((c, s.count(c)))
        stats = sorted(stats, key=lambda x: x[1], reverse=reverse)
        answer += stats[0][0]
    print(answer)


if __name__ == "__main__":
    # solve 6.1
    with open("resources/day6") as infile:
        solve(infile, True)
    # solve 6.2
    with open("resources/day6") as infile:
        solve(infile, False)
