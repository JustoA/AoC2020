import inp


def main():
    all_ingredients = set([])
    allergens = {}
    instream = inp.parse_file_str()
    ans = 0
    for food in instream:
        ingredients = set(food.split('(')[0].strip().split(' '))  #
        all_ingredients |= ingredients
        aller = food.split('(')[1][9:].split(',')
        # print(aller)
        aller = [a.strip(' ').strip(')') for a in aller]
        # print(aller)
        for a in aller:
            if a in allergens.keys():
                allergens[a] = allergens[a].intersection(ingredients)
            else:
                allergens[a] = ingredients
    safe = all_ingredients - set().union(*[a for a in allergens.values()])
    # print(set().union(*[a for a in allergens.values()]))
    # print(allergens)
    everything = ' ' + ''.join(instream).replace(')', ' ').replace('(', '').replace('\n', ' ')  # ay carumba
    # print(everything)
    # print(safe)
    for ing in safe:
        ans += everything.count(' ' + ing + ' ')
    return ans


def done(allergens):
    for a in allergens.keys():
        if len(allergens[a]) != 1:
            return False
    return True


def shortest(allergens):
    all_names = allergens.keys()
    shor = list(allergens.keys())[0]
    for a in all_names:
        if len(allergens[shor]) > len(allergens[a]):
            shor = a
    return shor


def main2():
    all_ingredients = set([])
    allergens = {}
    instream = inp.parse_file_str()
    for food in instream:
        ingredients = set(food.split('(')[0].strip().split(' '))  #
        all_ingredients |= ingredients
        aller = food.split('(')[1][9:].split(',')
        aller = [a.strip(' ').strip(')') for a in aller]
        for a in aller:
            if a in allergens.keys():
                allergens[a] = allergens[a].intersection(ingredients)
            else:
                allergens[a] = ingredients
    ret = []
    while len(allergens.keys()):
        short = shortest(allergens)
        #print(f'Shortest = {short} with list {allergens[short]}')
        for allergen in allergens.keys():
            if allergen != short:
                allergens[allergen] -= allergens[short]
        ret.append((short, allergens[short].pop()))
        del allergens[short]
    print(ret)
    print(sorted(ret, key=lambda x: x[0]))
    actual_ret = [x[1] for x in sorted(ret, key=lambda x: x[0])]
    print(actual_ret)
    actual_actual_ret = ','.join(list(actual_ret))
    return actual_actual_ret


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')

# {'soy': {'glf', 'mtnh', 'mptbpz', 'vlblq'}, 'fish': {'vlblq', 'cxsvdm', 'rsbxb', 'txdmlzd'}, 'eggs': {'xbnmzr', 'glf', 'mptbpz'}, 'wheat': {'mptbpz', 'txdmlzd'}, 'dairy': {'cxsvdm', 'mptbpz'}, 'peanuts': {'txdmlzd'}, 'sesame': {'vlblq', 'mptbpz'}, 'nuts': {'xbnmzr', 'vlblq', 'txdmlzd'}}


#cxsvdm,glf,rsbxb,xbnmzr,txdmlzd,vlblq,mptbpz
#cxsvdm,glf,rsbxb,xbnmzr,txdmlzd,vlblq,mtnh,mptbpz