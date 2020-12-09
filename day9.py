import inp  # my [REDACTED] input parser

PREAMBLE_LENGTH = 25  # yay constant


def main():
    in_stream = inp.parse_file_int()
    for i in range(len(in_stream)):
        if i < PREAMBLE_LENGTH:
            continue
        check_list = in_stream[i - PREAMBLE_LENGTH:i] # LIST SLICE GO BRBRBRBRRRRRRRRRRRRRrrrrRRRR
        target = in_stream[i]
        found = False
        for k in check_list:
            if not found:
                for l in check_list:
                    if k != l:
                        if k + l == target:
                            found = True
                            break
            else:
                break
        if not found:
            return target
    return "fail"  # only 12% of players can reach pink level 😂 😂 🤣 😳 😳


def main2(target):
    data = inp.parse_file_int()
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            variable_name_inoffensive_to_justin = sum(data[i:j + 1])  # if ya know ya know!
            if variable_name_inoffensive_to_justin == target:
                return min(data[i:j + 1]) + max(data[i:j + 1])
            elif variable_name_inoffensive_to_justin > target:  # smort brute force
                break
    return "oh no"  # no answer sad reacts only


part1 = main()
print(f'part 1: {part1}')
print(f'part 2: {main2(part1)}')  # i learned the power of python 3.6 format strings
