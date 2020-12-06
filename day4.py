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

import inp  # my amazing and poggers input parser
import re  # god have mercy on me

VALID_EYES = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']  # thank you python for `in`


def check_hair(hcl):  # a HELPER function?? In MY AoC solution???
    if hcl[0] == '#' and len(hcl) == 7:
        return re.match('#[a-f0-9]', hcl) is not None  # regex go BRRRRRRRRRRRRRRR


def check_pid(passpid):  # it's more likely than you think!
    if len(passpid) == 9:
        return re.match('[0-9]+', passpid) is not None  # regex also go bRRRRR


def main():
    prompt = inp.parse_file_two_eol()  # parses the input into a list of rows
    # part 1

    valid = 0
    for passp in prompt:
        if 'byr' in passp and 'iyr' in passp and 'eyr' in passp and 'hgt' in passp \
                and 'hcl' in passp and 'ecl' in passp and 'pid' in passp:
            valid += 1
    print(valid)

    # part 2
    valid = 0
    for passp in prompt:
        if 'byr' in passp and 'iyr' in passp and 'eyr' in passp and 'hgt' in passp \
                and 'hcl' in passp and 'ecl' in passp and 'pid' in passp:
            fields = passp.split(' ')
            passp_data = {}
            for field in fields:
                if field != '':
                    name = field.split(':')[0]
                    value = field.split(':')[1]
                    passp_data[name] = value
            # sorry for this
            if 1920 <= int(passp_data['byr']) <= 2002 and len(passp_data['byr']) == 4:
                if 2010 <= int(passp_data['iyr']) <= 2020 and len(passp_data['iyr']) == 4:
                    if 2020 <= int(passp_data['eyr']) <= 2030 and len(passp_data['eyr']) == 4:
                        height_unit = passp_data['hgt'][-2:]
                        if height_unit in ['cm', 'in']:
                            hgt_meas = int(passp_data['hgt'][:-2])
                            if (height_unit == 'cm' and 150 <= hgt_meas <= 193) or (
                                    height_unit == 'in' and 59 <= hgt_meas <= 76):  # short people aren't valid i guess
                                if check_hair(passp_data['hcl']):
                                    if passp_data['ecl'] in VALID_EYES:
                                        if check_pid(passp_data['pid']):
                                            valid += 1
    print(valid)
    exit(11037)  # this is a danganronpa reference sorry


main()
