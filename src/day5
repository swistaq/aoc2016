import hashlib

doorid = "uqwqemis"

def solve2():
    code = []
    posfound = []
    i = 0
    while posfound.__len__() < 8:
        m = hashlib.md5()
        m.update(doorid + str(i))
        val = m.hexdigest()
        if str(val).startswith("00000"):
            if ord(val[5]) - 48 in range(0, 8):
                if not posfound.__contains__(val[5]):
                    posfound.append(val[5])
                    code.append((val[5], val[6]))
        i += 1
    code.sort(key=lambda x: x[0])
    ans = ""
    for k in code:
        ans += k[1]
    print ans


def solve1():
    i = 0
    ctr = 0
    res = ""
    while ctr < 8:
        m = hashlib.md5()
        m.update(doorid + str(i))
        val = m.hexdigest()
        if str(val).startswith("00000"):
            ctr += 1
            res += val[5]
        i += 1
    print res


if __name__ == "__main__":
    solve1()
    solve2()
