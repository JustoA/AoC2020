# only one function today. I wrote it well the first time for once :)
def main(target):
    my_input = [8, 13, 1, 0, 18, 9]
    numbers = {8: 0, 13: 1, 1: 2, 0: 3, 18: 4, 9: 5}
    numbers_uttered = 5
    while numbers_uttered < target - 1:
        cur_num = my_input[numbers_uttered]
        if cur_num not in numbers.keys():
            my_input.append(0)
        else:
            my_input.append(numbers_uttered - numbers[cur_num])
        numbers[cur_num] = numbers_uttered
        numbers_uttered += 1
    return my_input[-1]


print(f'part 1: {main(2020)}')
print(f'part 2: {main(30000000)}')  # i learned the power of python 3.6 format strings
