cups = '586439172'


def round(loc):
    # print(loc)
    picked = loc[1:4]
    #print(f'picked: {picked}')
    loc = [loc[0]] + loc[4:]
    destination = loc[0] - 1
    while destination in picked or destination <= 0:
        destination -= 1
        if destination < min(loc):
            destination = max(loc)
    # print(f'Destination: {destination}')
    dest_index = loc.index(destination)
    loc = loc[:dest_index + 1] + picked + loc[dest_index + 1:]

    # shuffle shenanigans
    loc.append(loc.pop(0))
    return loc


def main():
    list_of_cups = [int(x) for x in cups]
    num_rounds = 0

    while num_rounds < 100:
        list_of_cups = round(list_of_cups)
        num_rounds += 1
    # print(list_of_cups)
    list_of_cups = list_of_cups[list_of_cups.index(1):] + list_of_cups[:list_of_cups.index(1)]
    return list_of_cups


class CupNode:
    def __init__(self, v):
        self.value = v
        self.next_cup = None

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f'{self.value} --> {self.next_cup.value}'


def round_but_speedy(doc, focus):
    # print(loc)
    #print(f'focus: {focus}')
    picked = [focus.next_cup, focus.next_cup.next_cup, focus.next_cup.next_cup.next_cup]
    focus.next_cup = picked[2].next_cup
    #print(f'picked: {picked}')
    # dangling : picked. still needs inserting
    destination = focus.value - 1
    while destination in [x.value for x in picked] or destination <= 0:
        destination -= 1
        if destination <= 0:
            destination = 1000000
    destination_cup = doc[destination]    #  dest -> next
    after_destination = destination_cup.next_cup
    destination_cup.next_cup = picked[0]  # dest -> picked[0] -> picked[1] -> picked[2]  next
    picked[2].next_cup = after_destination  # dest -> picked[0] -> picked[1] -> picked[2] ->  next

    focus = focus.next_cup
    return doc, focus


def main2():
    list_of_cups = [CupNode(int(x)) for x in cups]+ [CupNode(i) for i in range(10, 1000001)]
    for i in range(len(list_of_cups) - 1):
        list_of_cups[i].next_cup = list_of_cups[i + 1]
    list_of_cups[-1].next_cup = list_of_cups[0]
    dict_of_cups = dict(zip([x.value for x in list_of_cups], list_of_cups))
    #print(list_of_cups[:15], list_of_cups[999990:])
    num_rounds = 0
    focus = list_of_cups[0]
    while num_rounds < 10000000:
        #if num_rounds % 10000 == 0:
        #    print(f'round num {num_rounds}')
        # print(dict_of_cups)
        dict_of_cups,  focus = round_but_speedy(dict_of_cups, focus)
        num_rounds += 1
    # print(list_of_cups)
    print(dict_of_cups[1], dict_of_cups[1].next_cup, dict_of_cups[1].next_cup.next_cup)
    print(dict_of_cups[934001], dict_of_cups[934001].next_cup)
    #print(dict_of_cups)
    return dict_of_cups[1].next_cup.value * dict_of_cups[1].next_cup.next_cup.value


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')
