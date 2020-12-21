import inp  # my [REDACTED] input parser
from pprint import pprint

edges = {}
squares = {}


def top(sq):
    return squares[sq][0]


def bottom(sq):
    return squares[sq][9][::-1]  # read backwards for matching


def right(sq):
    return ''.join([x[9] for x in squares[sq]][::-1])  # read bottom up for matching


def left(sq):
    return ''.join([x[0] for x in squares[sq]])


def all_edges(sq):
    return [('top', top(sq)), ('bottom', bottom(sq)), ('left', left(sq)), ('right', right(sq))]


def register_square(square):
    ident = int(square.split('\n')[0].split(' ')[1].strip(':'))
    squares[ident] = square.split('\n')[1:]


def find_pairs():
    pairs = []
    for sq in squares.keys():
        square = squares[sq]
        top_edge = square[0]
        bottom_edge = square[9]
        right_edge = ''.join([x[9] for x in square])
        left_edge = ''.join([x[0] for x in square])

        square_edges = [top_edge, bottom_edge, left_edge, right_edge]

        for edge in square_edges:
            if edge in edges.keys():
                pairs.append((sq, edges[edge]))
            elif edge[::-1] in edges.keys():
                pairs.append((sq, edges[edge[::-1]]))
            else:
                edges[edge] = sq

    return pairs


def main():
    instream = inp.parse_file_two_newline()
    ans = 0
    num_squares = 0
    for sq in instream:
        register_square(sq)
        num_squares += 1

    pairs = find_pairs()
    corners = []
    # corners only appear twice!
    for sq in squares.keys():
        occ = 0
        for pair in pairs:
            if sq in pair:
                occ += 1
        if occ == 2:
            corners.append(sq)
    print(corners)
    return corners[0] * corners[1] * corners[2] * corners[3]


def rotate(square, degrees):
    while degrees > 0:
        rotated = list(zip(*squares[square][::-1]))
        squares[square] = [''.join(x) for x in rotated]
        degrees -= 90


# mutates squares{}!
def flipv(square):
    squares[square] = squares[square][::-1]


def fliph(square):
    squares[square] = [x[::-1] for x in squares[square]]


def find_and_tf(base, other):
    relation = 'nil'
    for e1 in all_edges(base):
        for e2 in all_edges(other):
            if e1[1] == e2[1] or e1[1] == e2[1][::-1]:
                if e1[1] == e2[1][::-1]:
                    if e2[0] == 'top' or e2[0] == 'bottom':
                        fliph(other)
                    else:
                        flipv(other)
                relation = e1[0]
                if e1[0] == 'top':
                    if e2[0] == 'top':
                        flipv(other)
                    if e2[0] == 'bottom':
                        fliph(other)
                    if e2[0] == 'left':
                        rotate(other, 270)
                    if e2[0] == 'right':
                        rotate(other, 90)

                elif e1[0] == 'bottom':
                    if e2[0] == 'top':
                        fliph(other)
                    if e2[0] == 'bottom':
                        flipv(other)
                    if e2[0] == 'left':
                        rotate(other, 90)
                    if e2[0] == 'right':
                        rotate(other, 270)

                elif e1[0] == 'right':
                    if e2[0] == 'top':
                        rotate(other, 270)
                    if e2[0] == 'bottom':
                        rotate(other, 90)
                    if e2[0] == 'left':
                        flipv(other)
                    if e2[0] == 'right':
                        fliph(other)

                elif e1[0] == 'left':
                    if e2[0] == 'top':
                        rotate(other, 90)
                    if e2[0] == 'bottom':
                        rotate(other, 270)
                    if e2[0] == 'left':
                        fliph(other)
                    if e2[0] == 'right':
                        flipv(other)
    if relation == 'nil':
        print(all_edges(base))
        print(all_edges(other))
        exit(-1)
    # print(f'     base={base}')
    # print(f'     other={other}')
    # print(f'     relation={relation}')
    return relation


def check_assembled(picture):
    return len(picture) == 12 and len(picture[0]) == 12  # 12 rows and 12 columns


NUM_SQUARES = 12


def get_top_left_corner(corners, pairs):
    for corner in corners[:]:
        for pair in pairs:
            if corner in pair:
                other = pair[0] if pair[0] != corner else pair[1]
                # print(other in corners)
                rel = find_and_tf(corner, other)
                if rel == 'left' or rel == 'top':
                    corners.remove(corner)
                    break
    # print(corners)
    return corners[0]


def assemble(corners, pairs):
    assembled = [[0 for _ in range(NUM_SQUARES)] for _ in range(NUM_SQUARES)]
    top_left = get_top_left_corner(corners, pairs)
    assembled[0][0] = top_left
    print(top_left)
    for y in range(NUM_SQUARES):
        for x in range(NUM_SQUARES):
            # print(f'{x},{y}')
            current_piece = assembled[y][x]
            for pair in pairs:
                if current_piece in pair:
                    # print(current_piece)
                    # print(pair)
                    other = pair[0] if pair[0] != current_piece else pair[1]
                    rel = find_and_tf(current_piece, other)
                    # print(rel)
                    if rel == 'right':
                        assembled[y][x + 1] = other
                    elif rel == 'bottom':
                        assembled[y + 1][x] = other
                    elif rel == 'left':
                        assembled[y][x - 1] = other
                    elif rel == 'top':
                        assembled[y - 1][x] = other

    return assembled


SQUARE_LEN = 8


def strip_border(sq):
    return [x[1:-1] for x in squares[sq][1:-1]]


def full_picture(blueprint):
    finished = []
    for row in blueprint:
        stripped_row = []
        for tile in row:
            stripped_row.append(strip_border(tile))
        full_row = ''
        for row_in_tile in range(8):
            for tile in stripped_row:
                full_row += tile[row_in_tile]
            full_row += '\n'
        finished.append(full_row)
    finished = ''.join(finished)
    return finished


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def look_for_monsters(picture):
    monster_1 = find('                  # ', '#')
    monster_2 = find('#    ##    ##    ###', '#')
    monster_3 = find(' #  #  #  #  #  #   ', '#')
    monsters = 0
    rows = picture.split('\n')
    squares[0] = rows
    attempts = 0
    while monsters == 0:
        rows = squares[0]
        print(squares[0])
        for i in range(len(rows) - 2):
            row = rows[i]
            row2 = rows[i + 1]
            row3 = rows[i + 2]
            for x in range(96):
                try:
                    if all([row[x + y] == '#' for y in monster_1]) and \
                            all([row2[x + y] == '#' for y in monster_2]) and \
                            all([row3[x + y] == '#' for y in monster_3]):
                        monsters += 1
                except IndexError:
                    pass
        rotate(0, 90)
        if attempts == 4:
            fliph(0)
        attempts += 1
        if attempts == 8:
            break
    return monsters


def main2():
    instream = inp.parse_file_two_newline()
    squares.clear()
    edges.clear()
    ans = 0
    num_squares = 0
    for sq in instream:
        register_square(sq)
        num_squares += 1
    pairs = find_pairs()
    corners = []
    # corners only appear twice!
    for sq in squares.keys():
        occ = 0
        for pair in pairs:
            if sq in pair:
                occ += 1
        if occ == 2:
            corners.append(sq)
    assembled = assemble(corners, pairs)
    print(assembled)
    pic = full_picture(assembled)[:-1]
    num_monsters = look_for_monsters(pic)
    # we actually have to create the image :(
    pounds_per_monster = 15
    print(num_monsters)
    print(len(pic.split('\n')))
    return len(find(''.join(pic), '#')) - num_monsters * pounds_per_monster


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')
