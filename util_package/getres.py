

def getres():
    res = []
    with open("screenconf.txt") as f:
        for line in f:
            res.append(line)
    return res