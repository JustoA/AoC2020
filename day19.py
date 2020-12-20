import inp  # my [REDACTED] input parser

######
# Abandoning this... it's a nightmare to debug and I can likely leverage existing regex better to solve this
######


def parse_rules(rule_list):
    ret = {}
    # print(rule_list)
    for rule in rule_list:
        # print(rule)
        key = rule.split(':')[0]
        rules = [x.strip().strip("\"") for x in rule.split(':')[1].split('|')]
        new_rules = []
        for s in rules:
            new_rules.append(s.split(' '))
        ret[key] = new_rules
    return ret


def check_rule(rule, rules, string, root=False, level=0):
    total_eaten = 0
    if rules[rule] == [['a']]:
        return string[0] == 'a', 1
    elif rules[rule] == [['b']]:
        return string[0] == 'b', 1
    else:
        good = False
        for r in rules[rule]:
            test_str = string
            for sr in r:
                print('  '*level + f'checking rule {sr} = {rules[sr]} on {"".join(test_str)}')
                if len(test_str) == 0:  # if we run out of things to parse and still have sub-rules, bad
                    good = False
                    break
                good, eaten = check_rule(sr, rules, test_str, level=level+1)
                if good:
                    total_eaten += eaten
                    print('  '*level + f'matched {"".join(test_str[:eaten])}')
                    test_str = test_str[eaten:]
                else:
                    break
            if good:
                break
        if not root:
            if not good:
                print('  '*level + f'no match for rule {rule}')
            return good, total_eaten
        else:
            #print(test_str)
            return len(test_str) == 0


def main():
    instream = inp.parse_file_not_regex()
    ans = 0
    rules = parse_rules(instream[0])
    for string in instream[1]:
        if check_rule('0', rules, list(string), True):
            ans += 1
        else:
            print(f'{string}')
    return ans



def main2():
    instream = inp.parse_file_not_regex()
    ans = 0
    rules = parse_rules(instream[0])
    return ans


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')
