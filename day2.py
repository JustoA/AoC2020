import inp  # my kooky and crazy input parser

def main():
    prompt = inp.parse_file_str()
    valid = 0
    for pw in prompt:
        # valid+= check_pw_part1(pw)
        valid += check_pw_part2(pw)
    print('{} passwords are fine'.format(valid))
    exit(11037)  # im quirky and exit code 0 is for losers


def check_pw_part1(password_to_chec):
    requirement, passw = password_to_chec.strip('\n').split(':')
    req1, req2 = requirement.split(' ')
    low, high = req1.split('-')
    occur = 0
    for character in passw:  # i never bothered to learn regex :(
        if character == req2:
            occur += 1
    return 1 if occur in range(int(low), int(high)+1) else 0


def check_pw_part2(password_to_chec):
    requirement, passw = password_to_chec.strip('\n').split(':')
    passw = passw.strip(' ')
    req1, req2 = requirement.split(' ')
    low, high = req1.split('-')
    low = int(low) - 1
    high = int(high) - 1
    good = (passw[low] == req2) ^ (passw[high] == req2)  # big brain xor time
    return 1 if good else 0


main()
