import inp  # my amazing and poggers input parser


def main():
    prompt = inp.parse_file_str()  # parses the input into a list of row
    rows = [x for x in range(0, 128)]
    cols = [x for x in range(0, 8)]
    results = []
    for boarding in prompt:
        possible_row = rows
        possible_col = cols
        row = boarding[0:7]
        col = boarding[7:]  # i legit feel like im cheating by using python list slicing
        for chara in row:
            if chara == 'F':
                possible_row = possible_row[:(len(possible_row)) // 2]
            else:
                possible_row = possible_row[(len(possible_row)) // 2:]
        for chara in col:
            if chara == 'L':
                possible_col = possible_col[:(len(possible_col)) // 2]
            else:
                possible_col = possible_col[(len(possible_col)) // 2:]
        row = possible_row[0]
        col = possible_col[0]
        results.append(row*8+col)
    print(max(results))

    for i in results:
        if i+2 in results and i+1 not in results:
            print(i+1)

    exit(11037)  # you know the drill


main()
