import inp  # my [REDACTED] input parser


def main():
    in_stream = inp.parse_file_int()
    in_stream.append(0)
    in_stream.append(max(in_stream)+3)
    sort = sorted(in_stream)
    one_diff = 0
    three_dif = 0
    for i in range(len(sort) - 1):

        if sort[i + 1] - sort[i] == 1:
            one_diff += 1
        elif sort[i + 1] - sort[i] == 3:
            three_dif += 1
    # print(sort)
    return one_diff, three_dif


def main2():
    in_stream = inp.parse_file_int()
    in_stream.append(0)
    in_stream.append(max(in_stream) + 3)
    sort = sorted(in_stream)

    # OH JESUS CHRIST THIS IS DYNAMIC PROGRAMMING. BYE. IM LEAVING.
    # https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/
    # referencing this because AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.

    # ok uhhhhhhh first step is make array for each part's connections
    num_ports = len(sort)
    solutions = [0]*num_ports
    # ok cool.
    solutions[0] = 1  # there's one way to connect the first part (0), just itself.
    # for each part now, count the number of ways that each part can connect to it. Store that in the array
    for second_part in range(0, num_ports):
        for first_part in range(0, second_part):
            # if there is a valid combination between second_part and first_part,
            # then we add the possible solutions to connect to first_part to
            # the possible solutions to connect to second_part.
            if sort[second_part] - sort[first_part] <= 3:
                solutions[second_part] += solutions[first_part]
    # return how many ways to connect to the last port?
    return solutions[-1]

# i drew a pretty picture to help think through part 2: https://cdn.discordapp.com/attachments/434918813025435668/786473827819323432/unknown.png


print(f'part 1: {main()}')
print(f'part 2: {main2()}')  # i learned the power of python 3.6 format strings
