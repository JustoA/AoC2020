import inp  # my [REDACTED] input parser
import re

def parse_rules(rule_list):
    ret = {}
    # print(rule_list)
    for rule in rule_list:
        # print(rule)
        key = rule.split(':')[0]
        rules = rule.split(':')[1]
        ret[key] = rules
    return ret


def check_incomplete_sub(string):
    return re.search(r'[0-9]', string)

 # 8: 42 | 42 8
            # match: 42
            # match: 42 42 42 42 42 42 42 42 42 42 42..
            # (42)+
            # baaaabbbabbabbbabbbaababaaabaabababababbbaabababbbbaaaabaababababbabbbbaabbbaaab

            # 11: 42 31 | 42 11 31
            # 42 31 | 42 42 31 31 | 42 42 42 31 31 31

def unholy_abomination():
    ans = ''
    for x in range(1,7):
        ans += (('42 '*x) + ('31 '*x) + '|')
    ans = ans[:-1]
    #print(ans)
    return ans

def create_regex(rules):
    base = rules['0']
    print(base)
    while check_incomplete_sub(base):
        s, e = re.search(r'[0-9]+', base).span()

        if rules[base[s:e]] in ['a', 'b']:
            base = base[:s] + rules[base[s:e]] + base[e:]
        else:
            base = base[:s] + '(' + rules[base[s:e]] + ')' + base[e:]
        # print(base)
    base = base.replace('\"', '').replace(' ', '').replace('(a)','a').replace('(b)','b')
    #print(base)
    return base


def main():
    instream = inp.parse_file_not_regex()
    ans = 0
    rules = parse_rules(instream[0])
    the_regex = create_regex(rules)
    for string in instream[1]:
        if re.fullmatch(the_regex, string):
            ans += 1

    return ans


def main2():
    instream = inp.parse_file_not_regex()
    ans = 0
    rules = parse_rules(instream[0])
    rules['8'] = '(42)+'
    rules['11'] = f'({unholy_abomination()})'
    the_regex = create_regex(rules)

    for string in instream[1]:
        if re.fullmatch(the_regex, string):
            ans += 1

    return ans


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')
