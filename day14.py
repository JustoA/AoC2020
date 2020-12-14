#########################
#     import copy       # STINKY LIBRARY MAKE CODE GO SLOW
#########################
import inp  # my [REDACTED] input parser


def unwrapped(inst):
    address = int(inst.split('[')[1].split(']')[0])
    value = int(inst.split('=')[1])
    return address, value


def apply_mask(mask, num):
    str_num = list(bin(num))[2:]
    str_num = ['0']*(36-len(str_num))+str_num  # oh jesus christ
    #print(str_num)
    #print(mask)
    for i in range(len(mask)):
        if mask[i] != 'X':
            str_num[i] = mask[i]
    binstring = ['0b']+str_num
    ret = ''.join(binstring)
    #print(ret)
    return int(ret, 2)

def main():
    instream = inp.parse_file_docker()
    memory = {}
    for mask_write_set in instream:
        mask = mask_write_set[0].split('=')[1].strip()
        for write_op in mask_write_set[1:]:
            address, value = unwrapped(write_op)
            memory[address] = apply_mask(mask,value)

    return sum(memory.values())


def mutate_memory(mask, location):
    str_num = list(bin(location))[2:]
    str_num = ['0']*(36-len(str_num))+str_num  # oh jesus christ
    lol = [str_num]
    for i in range(len(mask)):
        if mask[i] == '1':
            for location in lol:
                location[i] = '1'
        if mask[i] == 'X':
            lol2 = []
            for location in lol:
                loc0 = location.copy()
                loc0[i] = '0'
                loc1 = location.copy()
                loc1[i] = '1'
                lol2.append(loc0)
                lol2.append(loc1)
            lol = lol2
    final = []
    for location in lol:
        binstring = ['0b'] + location
        final.append(int(''.join(binstring), 2))
    return set(final)


def write_to_memory(lol, value, memory):
    for location in lol:
        memory[location] = value
    return memory


def main2():  # this used to take a long time. it turns out that deepcopy() is really hecking large
    instream = inp.parse_file_docker()
    memory = {}
    for mask_writes_sksksksk_and_i_oop in instream:
        mask = mask_writes_sksksksk_and_i_oop[0].split('=')[1].strip()
        for write_operation in mask_writes_sksksksk_and_i_oop[1:]:
            address, value = unwrapped(write_operation)
            lol = mutate_memory(mask, address)
            memory = write_to_memory(lol, value, memory)
    return sum(memory.values())


print(f'part 1: {main()}')
print(f'part 2: {main2()}')  # i learned the power of python 3.6 format strings
