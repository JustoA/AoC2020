import copy


def parse_file_int():
    inp = open('input.txt')
    out = []
    for line in inp.readlines():
        out.append(int(line))
    return out


def parse_file_str():
    inp = open('input.txt')
    buf = inp.read()
    out = buf.split('\n')
    return out


def parse_file_two_newline():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n\n')
    return buf


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


def parse_file_docker():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n')
    ret = []
    temp = []
    for line in buf:
        # print(line)
        if 'mask' in line:
            if len(temp) != 0:
                ret.append(copy.deepcopy(temp))
            temp = [line]
        else:
            temp.append(line)
        # print(temp)
    ret.append(temp)
    # print(ret)

    return ret


def parse_file_tickets():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n\n')
    tickets = [x.split(',') for x in buf[2].split('\n')[1:]]  # i love python
    int_tickets = []
    my_ticket = [int(y) for y in buf[1].split('\n')[1].split(',')]
    for ticket in tickets:
        int_ticket = [int(y) for y in ticket]
        int_tickets.append(int_ticket)
    ret = [buf[0].split('\n'), my_ticket, int_tickets]
    return ret


def parse_file_not_regex():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n\n')
    ret = []
    ret.append(buf[0].split('\n'))
    ret.append(buf[1].split('\n'))
    return ret

def parse_file_puzzle():
    inp = open('input.txt')
    buf = inp.read()
    buf = buf.split('\n\n')
    ret = [x.split('\n') for x in buf]
    return ret
