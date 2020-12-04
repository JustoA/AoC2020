import inp  # my kooky and crazy input parser

# i did this while crying over an anime so expect nothing in terms of code quality :)

"""
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
"""


def main():
    prompt = inp.parse_file_str()  # parses the input into a list of rows
    height = len(prompt)  # how high is the input
    ans = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        trees = 0
        x, y = 0, 0
        dx, dy = slope
        while y < height - 1:
            x += dx
            x %= len(prompt[1])  # i love u modulo
            y += dy
            if prompt[y][x] == '#':
                trees += 1
        print('{} trees hit on slope {}'.format(trees, slope))
        ans *= trees

    print('answer is {}'.format(ans))
    exit(11037)  # im quirky and exit code 0 is for losers


main()
