def parsefile():
    inp = open('input.txt')
    out = []
    for line in inp.readlines():
        out.append(int(line))
    return out
