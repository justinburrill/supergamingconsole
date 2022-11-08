

def getres():
    res = []
    with open("screenconf.txt") as f:
        for line in f:
            res.append(int(line))
    return res