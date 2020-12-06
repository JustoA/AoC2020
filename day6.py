import inp  # my amazing and poggers input parser

the_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']  # woah


def checkq(group, a):
    for people in group.split('\n'):
        if a not in people:
            return False
    return True


def main():
    prompt = inp.parse_file_two_eol()  # refactored because connor told me to <3
    ans = 0
    for question in prompt:
        ans += len(set(question))
    print(ans)

    # part two
    prompt = inp.parse_file_questionaire()  # not so lucky with this one, need to keep line breaks
    ans = 0
    for group in prompt:
        for question in the_alphabet:
            if checkq(group, question):
                ans += 1

    print(ans)
    exit(11037)  # you know the drill


main()
