import copy
import inp  # my [REDACTED] input parser

PLAY_FIELD_LEN = 30
PLAY_FIELD_RANGE = range(-PLAY_FIELD_LEN // 2, PLAY_FIELD_LEN // 2 + 1)


def count_surrounding(state, x, y, z):
    count = 0
    for zed in [z - 1, z, z + 1]:
        for why in [y - 1, y, y + 1]:
            for ex in [x - 1, x, x + 1]:
                if (zed == z and why == y and x == ex) or zed < 0 or why < 0 or ex < 0 or zed>PLAY_FIELD_LEN or why > PLAY_FIELD_LEN or ex > PLAY_FIELD_LEN:
                    continue
                if state[zed][why][ex] == '#':
                    count += 1
    return count


def all_dot(z_slice):
    for y_slice in z_slice:
        for c in y_slice:
            if c == '#':
                return False
    return True


def print_state(state):
    z = 0
    for z_slice in state:
        if not all_dot(z_slice):
            print(f'z={z}')
            for y_slice in z_slice:
                print(y_slice)
        z += 1


def count_active(state):
    ans = 0
    for z_slice in state:
        for y_slice in z_slice:
            for cube in y_slice:
                if cube == '#':
                    ans += 1
    return ans


def init_play_field(in_stream):
    play_field = []
    for _ in PLAY_FIELD_RANGE:
        z_plane = []
        for _ in PLAY_FIELD_RANGE:
            y_plane = []
            for _ in PLAY_FIELD_RANGE:
                y_plane.append('.')
            z_plane.append(y_plane)
        play_field.append(z_plane)

    y_off = 0
    for y_slice in in_stream:
        x_off = 0
        for cube in y_slice:
            play_field[PLAY_FIELD_LEN // 2][PLAY_FIELD_LEN // 3 + y_off][PLAY_FIELD_LEN // 3 + x_off] = cube
            x_off += 1
        y_off += 1
    return play_field


def run_one_round(state):
    new = copy.deepcopy(state)
    for z in range(PLAY_FIELD_LEN):  # z
        for y in range(PLAY_FIELD_LEN):  # y
            for x in range(PLAY_FIELD_LEN):
                filled = count_surrounding(state, x, y, z)
                if filled == 3:
                    new[z][y][x] = '#'
                elif filled == 2 and state[z][y][x] == '#':
                    new[z][y][x] = '#'
                else:
                    new[z][y][x] = '.'
    return new


def main():
    instream = inp.parse_file_str()
    # sure it's infinite, but it's easier for me to just define it as finite.
    play_field = init_play_field(instream)
    #print_state(play_field)
    for round_num in range(6):
        #print(f'round {round_num}')
        play_field = run_one_round(play_field)
        #print_state(play_field)

    return count_active(play_field)


print(f'part 1: {main()}')
