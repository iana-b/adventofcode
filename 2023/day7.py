# 7.1

with open('inputs/7.txt', 'r') as file:
    lines = file.read().splitlines()

labels = 'AKQJT98765432'


def get_type(dct):
    if len(dct) == 1:
        return 7  # 'five_of_a_kind'
    elif len(dct) == 2 and any(value == 4 for value in dct.values()):
        return 6  # 'four_of_a_kind'
    elif len(dct) == 2 and all(value == 3 or value == 2 for value in dct.values()):
        return 5  # 'full_house'
    elif len(dct) == 3 and all(value != 2 for value in dct.values()):
        return 4  # 'tree_of_a_kind'
    elif len(dct) == 3 and all(value != 3 for value in dct.values()):
        return 3  # 'two_pair'
    elif len(dct) == 4:
        return 2  # 'one_pair'
    return 1  # 'high_card'


def count_cards(h):
    dct = {}
    for card in h:
        dct[card] = h.count(card)
    return dct


lst = []
for line in lines:
    hand = line.split(' ')[0]
    bid = int(line.split(' ')[1])

    d = count_cards(hand)

    d['type'] = get_type(d)
    d['hand'] = hand
    d['bid'] = bid
    # print(d)
    lst.append(d)

# print(lst)

sorted_list = sorted(lst, key=lambda x: (x['type'], list(map(labels[::-1].index, x['hand']))))
# print(sorted_list)

answer = 0
for e in range(len(sorted_list)):
    mult = sorted_list[e]['bid'] * (e + 1)
    answer += mult
print(answer)

# 7.2

labels = 'AKQT98765432J'

lst = []

for line in lines:
    hand = line.split(' ')[0]
    bid = int(line.split(' ')[1])

    d = count_cards(hand)
    new_hand = hand

    if 'J' in hand and hand != 'JJJJJ':
        hand_without_j = hand.replace('J', '')
        max_key = max(hand_without_j, key=hand_without_j.count)
        new_hand = hand.replace('J', max_key)

        d = count_cards(new_hand)

    d['type'] = get_type(d)
    d['hand'] = hand
    d['bid'] = bid
    lst.append(d)


sorted_list = sorted(lst, key=lambda x: (x['type'], list(map(labels[::-1].index, x['hand']))))

answer = 0
for e in range(len(sorted_list)):
    mult = sorted_list[e]['bid'] * (e + 1)
    answer += mult
print(answer)
