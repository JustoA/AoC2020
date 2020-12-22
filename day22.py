import inp


def play_round(p1, p2):
    if p1[0] > p2[0]:
        win = p1.pop(0)
        lose = p2.pop(0)
        p1 += [win, lose]
    elif p1[0] < p2[0]:
        win = p2.pop(0)
        lose = p1.pop(0)
        p2 += [win, lose]
    return p1, p2


def score(deck):
    deck_length = len(deck)
    score = 0
    for card in deck:
        score += card * deck_length
        deck_length -= 1
    return score


def main():
    instream = inp.parse_file_two_newline()
    p1 = [int(x) for x in instream[0].split('\n')[1:]]
    p2 = [int(x) for x in instream[1].split('\n')[1:]]
    while len(p1) > 0 and len(p2) > 0:
        p1, p2 = play_round(p1, p2)
    winner = p1 if len(p1) != 0 else p2
    return score(winner)


def play_recursive_combat(p1, p2, root=False):
    db = set()  # haha set go O(1) lookup (
    while len(p1) > 0 and len(p2) > 0:
        p1_p2 = str(p1)+str(p2)
        #print(p1_p2)
        if p1_p2 in db:
            if not root:
                return 1  # player 1 win
            else:
                return p1
        else:
            db.add(p1_p2)
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        if p1_card <= len(p1) and p2_card <= len(p2):
            winner = play_recursive_combat(p1[:p1_card], p2[:p2_card])
            if winner == 1:
                p1 += [p1_card, p2_card]
            elif winner == 2:
                p2 += [p2_card, p1_card]

        else:
            if p1_card>p2_card:
                p1 += [p1_card, p2_card]
            elif p2_card>p1_card:
                p2 += [p2_card, p1_card]
    if not root:
        return 1 if len(p1) > 0 else 2
    else:
        return p1 if len(p1) > 0 else p2


def main2():
    instream = inp.parse_file_two_newline()
    p1 = [int(x) for x in instream[0].split('\n')[1:]]
    p2 = [int(x) for x in instream[1].split('\n')[1:]]
    winner = play_recursive_combat(p1,p2,True)
    return score(winner)


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')
