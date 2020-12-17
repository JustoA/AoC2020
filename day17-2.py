import copy
import inp  # my [REDACTED] input parser

# This could be faster. I don't care.

PLAY_FIELD_LEN = 30
PLAY_FIELD_RANGE = range(-PLAY_FIELD_LEN // 2, PLAY_FIELD_LEN // 2 + 1)


def count_surrounding(state, x, y, z, w):
    count = 0
    for double_you in [w - 1, w, w + 1]:
        for zed in [z - 1, z, z + 1]:
            for why in [y - 1, y, y + 1]:
                for ex in [x - 1, x, x + 1]:
                    if (zed == z and why == y and x == ex and double_you == w) or zed < 0 or why < 0 or ex < 0 \
                            or double_you < 0 or zed > PLAY_FIELD_LEN or why > PLAY_FIELD_LEN or ex > PLAY_FIELD_LEN \
                            or double_you > PLAY_FIELD_LEN:
                        continue
                    if state[double_you][zed][why][ex] == '#':
                        count += 1
    return count


def all_dot(z_slice):
    for y_slice in z_slice:
        for c in y_slice:
            if c == '#':
                return False
    return True


def count_active(state):
    ans = 0
    for w_slice in state:
        for z_slice in w_slice:
            for y_slice in z_slice:
                for cube in y_slice:
                    if cube == '#':
                        ans += 1
    return ans


def init_play_field(in_stream):
    play_field = []
    for _ in PLAY_FIELD_RANGE:
        w_plane = []
        for _ in PLAY_FIELD_RANGE:
            z_plane = []
            for _ in PLAY_FIELD_RANGE:
                y_plane = []
                for _ in PLAY_FIELD_RANGE:
                    y_plane.append('.')
                z_plane.append(y_plane)
            w_plane.append(z_plane)
        play_field.append(w_plane)

    y_off = 0
    for y_slice in in_stream:
        x_off = 0
        for cube in y_slice:
            play_field[PLAY_FIELD_LEN//2][PLAY_FIELD_LEN // 2][PLAY_FIELD_LEN // 3 + y_off][PLAY_FIELD_LEN // 3 + x_off] = cube
            x_off += 1
        y_off += 1
    return play_field


def run_one_round(state):
    new = copy.deepcopy(state)
    for w in range(PLAY_FIELD_LEN):
        for z in range(PLAY_FIELD_LEN):  # z
            for y in range(PLAY_FIELD_LEN):  # y
                for x in range(PLAY_FIELD_LEN):
                    filled = count_surrounding(state, x, y, z, w)
                    if filled == 3:
                        new[w][z][y][x] = '#'
                    elif filled == 2 and state[w][z][y][x] == '#':
                        new[w][z][y][x] = '#'
                    else:
                        new[w][z][y][x] = '.'
    return new


def main():
    instream = inp.parse_file_str()
    # sure it's infinite, but it's easier for me to just define it as finite.
    play_field = init_play_field(instream)
    for round_num in range(6):
        print(f'round {round_num}')
        play_field = run_one_round(play_field)
        #print_state(play_field)

    return count_active(play_field)


print(f'part 1: {main()}')
