def parse_file_int():
    inp = open('input.txt')
    out = []
    for line in inp.readlines():
        out.append(int(line))
    return out

def parse_file_str():
    inp = open('input.txt')
    out = []
    for line in inp.readlines():
        out.append(line.strip('\n'))
    return out
