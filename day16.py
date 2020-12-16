import inp  # my [REDACTED] input parser

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

# I CANNOT STRESS HOW BAD THIS CODE IS. PLEASE DO NOT READ


def get_valids(rule_list):
    valids = []
    for rule in rule_list:
        # print(rule)
        actual_rules = rule.split(':')[1].split('or')
        for ar in actual_rules:
            low = int(ar.split('-')[0])
            high = int(ar.split('-')[1])
            valids += [x for x in range(low, high + 1)]
    return valids


def main():
    instream = inp.parse_file_tickets()
    rules = instream[0]
    my_ticket = instream[1]
    other_tickets = instream[2]
    valids = get_valids(rules)
    not_valid = []  # sorry sweaty you're not valid
    for ticket in other_tickets:
        for val in ticket:
            if val not in valids:
                not_valid.append(val)
    return sum(not_valid)


def get_valids_dict(rule_list):
    valids = {}
    valid_all = []
    for rule in rule_list:
        # print(rule)
        rule_title = rule.split(':')[0]
        valids[rule_title] = []
        actual_rules = rule.split(':')[1].split('or')
        for ar in actual_rules:
            low = int(ar.split('-')[0])
            high = int(ar.split('-')[1])
            valids[rule_title] += [x for x in range(low, high + 1)]
            valid_all += [x for x in range(low,high+1)]
    return valids, valid_all


def main2():
    instream = inp.parse_file_tickets()
    rules = instream[0]
    my_ticket = instream[1]
    other_tickets = instream[2]
    rule_set, rule_range = get_valids_dict(rules)
    valid_tickets = []
    for ticket in other_tickets:
        bad = False
        for val in ticket:
            if val not in rule_range:
                bad = True
                break
        if not bad:
            valid_tickets.append(ticket)
    num_fields = len(my_ticket)
    rules = [x for x in rule_set.keys()]
    pinned = []
    while len(pinned) != num_fields:
        for rule in rules:  # for each departure rule
            skip = False
            for f in pinned:
                if rule == f[0]:
                    skip = True
                    break
            if skip:
                continue
            hits = [0]*num_fields
            for i in range(num_fields):  # check each ticket's ith field
                skip2=False
                for f in pinned:
                    if i == f[1]:
                        skip2 = True
                        break
                if skip2:
                    continue
                bad = False
                for ticket in valid_tickets:  # check each ticket's values. if they all line up then good
                    if ticket[i] not in rule_set[rule]:
                        bad = True
                        break
                if not bad:
                    hits[i] += 1
            if sum(hits) == 1:
                print(f'{rule}, {hits}')
                index_num = hits.index(1)
                print(f'found meaning for field {rule} : {index_num}')
                pinned.append((rule, index_num))
    ans = 1
    for f in pinned:
        if 'departure' in f[0]:
            ans *= my_ticket[f[1]]
    return ans


print(f'part 1: {main()}')
print(f'part 2: {main2()}')  # i learned the power of python 3.6 format strings
