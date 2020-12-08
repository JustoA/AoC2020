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


def parse_file_two_eol():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n\n')
    ret = []
    for passport in buf:
        ret.append(passport.replace('\n', ' '))
    return ret


def parse_file_questionaire():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n\n')
    ret = []
    for passport in buf:
        ret.append(passport)
    return ret


def parse_file_rules():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n')
    ret = []
    for rule in buf:
        ret.append(rule)
    return ret


def parse_file_stringcode():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n')
    ret = []
    for rule in buf:
        ret.append(rule.split(' '))
    return ret
