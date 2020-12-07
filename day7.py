# no witty comments this time. im exhausted.

import inp  # my amazing and poggers input parser


def look_for_gold(color, rules, firstdive=False):
    # print('looking for gold in {}'.format(color)) if firstdive else print('')
    if color == 'shinygold':
        # print('no')
        return 0
    if 'otherbags.' in rules[color]:
        # print('dead end')
        return 0
    if 'shinygold' in rules[color]:
        # print('got one')
        return 1
    else:
        resp = 0
        # print('looking in other bags {}'.format(rules[color]))
        for bag in rules[color]:
            # print('checking sub bag {}'.format(bag))
            resp |= look_for_gold(bag, rules)
        return resp


def main():
    prompt = inp.parse_file_rules()  # refactored because connor told me to <3
    rules = {}
    for rule in prompt:
        outer_color = rule.split(' ')[0] + rule.split(' ')[1]
        # print(outer_color)
        inner_colors = rule.split('contain')[1].split(',')
        # print(inner_colors)
        just_colors = []

        for color in inner_colors:
            just_colors.append(color.split(' ')[2] + color.split(' ')[3])
        rules[outer_color] = just_colors
    hasgold = 0
    for key in rules.keys():
        if look_for_gold(key, rules, True) == 1:
            # print('         officially found gold bag in {}'.format(key))
            hasgold += 1
    return hasgold

def count_bags(color, rules):
    if 'otherbags.' == color or 'otherbags.' in rules[color]:
        return 0
    else:
        num = 0
        for rule in rules[color]:
            #print(rule)
            if int(rule[0]) == 0:
                return 0
            incr = int(rule[0]) + int(rule[0]) * count_bags(rule[1], rules)
            #print(incr)
            num += incr
        return num


def main2():
    prompt = inp.parse_file_rules()
    rules = {}
    for rule in prompt:
        outer_color = rule.split(' ')[0] + rule.split(' ')[1]
        # print(outer_color)
        inner_colors = rule.split('contain')[1].split(',')
        # print(inner_colors)
        just_colors = []

        for color in inner_colors:
            num = 0
            if color.split(' ')[1] != 'no':
                num = color.split(' ')[1]
            just_colors.append([num, color.split(' ')[2] + color.split(' ')[3]])

        rules[outer_color] = just_colors
    return count_bags('shinygold', rules)

print('there are {} types of bags that hold gold bags'.format(main()))
print('a gold bag holds {} bags.'.format(main2()))
