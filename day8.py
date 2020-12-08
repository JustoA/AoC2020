# no witty comments this time. im exhausted.
import copy
import inp  # my amazing and poggers input parser


def main():
    data = inp.parse_file_stringcode()  # refactored because connor told me to <3
    hits = []
    current_instruction = 0
    acc = 0
    while (current_instruction not in hits):
        hits.append(current_instruction)
        if data[current_instruction][0] == 'nop':
            current_instruction += 1
            continue
        if data[current_instruction][0] == 'acc':
            acc += int(data[current_instruction][1])
            current_instruction += 1
            continue
        if data[current_instruction][0] == 'jmp':
            current_instruction += int(data[current_instruction][1])
            continue
    return acc


def main2():
    pristine_data = inp.parse_file_stringcode()  # refactored because connor told me to <3
    for i in range(len(pristine_data)):
        data = copy.deepcopy(pristine_data)
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
        elif data[i][0] == 'jmp':
            data[i][0] = 'nop'
        else:
            continue
        hits = []
        current_instruction = 0
        acc = 0
        while current_instruction not in hits:
            if current_instruction == len(data):
                return acc
            hits.append(current_instruction)  # duplicate code so what
            if data[current_instruction][0] == 'nop':
                current_instruction += 1
                continue
            if data[current_instruction][0] == 'acc':
                acc += int(data[current_instruction][1])
                current_instruction += 1
                continue
            if data[current_instruction][0] == 'jmp':
                current_instruction += int(data[current_instruction][1])
                continue


print('part 1: {}'.format(main()))
print('part 2: {}'.format(main2()))
