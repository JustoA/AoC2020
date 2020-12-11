import inp  # my [REDACTED] input parser
import copy


# okay, this code gets the warning.

#########################################################################
# __          __     _____  _   _ _____ _   _  _____ _                  #
# \ \        / /\   |  __ \| \ | |_   _| \ | |/ ____| |                 #
#  \ \  /\  / /  \  | |__) |  \| | | | |  \| | |  __| |                 #
#   \ \/  \/ / /\ \ |  _  /| . ` | | | | . ` | | |_ | |                 #
#    \  /\  / ____ \| | \ \| |\  |_| |_| |\  | |__| |_|                 #
#  __ \/_ \/_/__ _\_\_|  \_\_| \_|_____|_| \_|\_____(_)_  __            #
# |  \/  |  ____/ ____|   /\          | |  /\   | \ | | |/ /            #
# | \  / | |__ | |  __   /  \         | | /  \  |  \| | ' /             #
# | |\/| |  __|| | |_ | / /\ \    _   | |/ /\ \ | . ` |  <              #
# | |  | | |___| |__| |/ ____ \  | |__| / ____ \| |\  | . \             #
# |_|__|_|______\_____/_/____\_\  \____/_/    \_\_|_\_|_|\_\    _____   #
#  / ____/ __ \|  __ \|  ____|     /\   | |  | |  ____|   /\   |  __ \  #
# | |   | |  | | |  | | |__       /  \  | |__| | |__     /  \  | |  | | #
# | |   | |  | | |  | |  __|     / /\ \ |  __  |  __|   / /\ \ | |  | | #
# | |___| |__| | |__| | |____   / ____ \| |  | | |____ / ____ \| |__| | #
#  \_____\____/|_____/|______| /_/    \_\_|  |_|______/_/    \_\_____/  #
#########################################################################

# returns filled, empty
def check_surrounding(i, j, arr):
    filled = 0
    empty = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0:
                continue
            if 0 <= i + k < len(arr) and 0 <= j + l < len(arr[0]):  # bounds check
                if arr[i + k][j + l] == '#':
                    filled += 1
                else:
                    empty += 1
    return filled, empty


def run_one_round(arr):
    new = copy.deepcopy(arr)
    for i in range(len(arr)):  # rows
        for j in range(len(arr[0])):  # seats
            if arr[i][j] != '.':
                filled, empty = check_surrounding(i, j, arr)
                if empty > 8 or filled > 8:
                    print("ABORT")
                    exit(11037)
                # print(filled,empty)
                if filled == 0:
                    new[i][j] = '#'
                elif filled >= 4:
                    new[i][j] = 'L'
                else:
                    new[i][j] = arr[i][j]
    return new


def main():
    instream = inp.parse_file_str()
    board = []
    for row in instream:
        board.append(list(row))
    while True:
        dupe_check = run_one_round(board)
        if dupe_check == board:
            break
        else:
            board = dupe_check
    occupied = 0
    for row in board:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied


def check_legal(y, x, arr):
    return 0 <= y < len(arr) and 0 <= x < len(arr[0])


# returns filled, empty
def check_surrounding_view(i, j, arr):
    filled = 0
    empty = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0:
                continue
            view_y, view_x = i + k, j + l
            if check_legal(view_y, view_x, arr):
                while check_legal(view_y, view_x, arr) and arr[view_y][view_x] == '.':
                    view_y += k
                    view_x += l
                if check_legal(view_y, view_x, arr) and arr[view_y][view_x] == '#':
                    filled += 1  # 👁👄👁 i see a human being
                else:
                    empty += 1
    return filled, empty


def run_one_round_two(arr):
    new = copy.deepcopy(arr)
    for i in range(len(arr)):  # rows
        for j in range(len(arr[0])):  # seats
            if arr[i][j] != '.':
                filled, empty = check_surrounding_view(i, j, arr)
                if empty > 8 or filled > 8:  # reality broke lol
                    print("ABORT")
                    exit(11037)
                # print(filled,empty)
                if filled == 0:
                    new[i][j] = '#'  # ooh empty seat
                elif filled >= 5:
                    new[i][j] = 'L'  # im leabing
                else:
                    new[i][j] = arr[i][j]

    return new


def main2():
    instream = inp.parse_file_str()
    board = []
    for row in instream:
        board.append(list(row))
    while True:
        dupe_check = run_one_round_two(board)
        if dupe_check == board:
            break
        else:
            board = dupe_check
    occupied = 0
    for row in board:
        for seat in row:
            if seat == '#':
                occupied += 1

    return occupied


print(f'part 1: {main()}')
print(f'part 2: {main2()}')  # i learned the power of python 3.6 format strings
