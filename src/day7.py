from __future__ import print_function
import re

test1 = "abba[mnop]qrst"
test2 = "aaaa[qwer]tyui"
test3 = "ioxxoj[asdfgh]zxcvbn"


def contains_abba(str):
    subs = [str[i:i + 4] for i in range(0, str.__len__() - 3)]
    # print(str, subs)
    for sub in subs:
        if sub[0] != sub[1] and sub[0] == sub[3] and sub[1] == sub[2]:
            return True


def solve1(line):
    # print(line)
    hypernets = re.findall("\[([a-z]*)\]", line)
    for hypernet in hypernets:
        if contains_abba(hypernet):
            return False
    line = re.sub("\[([a-z]*)\]", "|", line)
    supernets = re.split("\|", line)
    # print(line, parts)
    for part in supernets:
        if contains_abba(part):
            return True


def get_abas(str):
    return [k for k in [str[i:i + 3] for i in range(0, str.__len__() - 2)] if k[0] == k[2]]


def solve2(line):
    super_abas = []
    hyper_abas = []
    hypernets = re.findall("\[([a-z]*)\]", line)
    line = re.sub("\[([a-z]*)\]", "|", line)
    supernets = re.split("\|", line)
    for supernet in supernets:
        super_abas += get_abas(supernet)
    for hypernet in hypernets:
        hyper_abas += get_abas(hypernet)
    for seq in hyper_abas:
        if super_abas.__contains__(seq[1]+seq[0]+seq[1]):
            return True


if __name__ == "__main__":
    # solve1
    # i = 0
    # with open("resources/day7") as infile:
    #     for line in infile.readlines():
    #         if solve1(line.strip()):
    #             i += 1
    # print("TLS: ", i)
    i = 0
    with open("resources/day7") as infile:
        for line in infile.readlines():
            if solve2(line.strip()):
                i += 1
    print("TLS: ", i)
