# 7.1

with open('inputs/7.txt', 'r') as file:
    lines = file.read().splitlines()

labels = 'AKQJT98765432'

lst = []
for line in lines:
    hand = line.split(' ')[0]
    bid = int(line.split(' ')[1])

    d = {}

    for i in range(len(hand)):
        d[hand[i]] = hand.count(hand[i])

    if len(d) == 1:
        d['type'] = 7  # 'five_of_a_kind'
    elif len(d) == 2 and any(d[hand[x]] == 4 for x in range(len(hand))):
        d['type'] = 6  # 'four_of_a_kind'
    elif len(d) == 2 and all(d[hand[x]] == 3 or d[hand[x]] == 2 for x in range(len(hand))):
        d['type'] = 5  # 'full_house'
    elif len(d) == 3 and all(value != 2 for value in d.values()):
        d['type'] = 4  # 'tree_of_a_kind'
    elif len(d) == 3 and all(value != 3 for value in d.values()):
        d['type'] = 3  # 'two_pair'
    elif len(d) == 4:
        d['type'] = 2  # 'one_pair'
    elif len(d) == 5:
        d['type'] = 1  # 'high_card'
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

    d = {}

    for i in range(len(hand)):
        d[hand[i]] = hand.count(hand[i])
    new_hand = hand

    if 'J' in hand and hand != 'JJJJJ':
        hand_without_j = hand.replace('J', '')
        print(hand)
        print(hand_without_j)
        max_key = max(hand_without_j, key=hand_without_j.count)
        print(max_key)
        new_hand = hand.replace('J', max_key)
        print(new_hand)

        d = {}
        for each in new_hand:
            d[each] = new_hand.count(each)

        print(d)

    if len(d) == 1:
        d['type'] = 7  # 'five_of_a_kind'
    elif len(d) == 2 and any(d[new_hand[x]] == 4 for x in range(len(new_hand))):
        d['type'] = 6  # 'four_of_a_kind'
    elif len(d) == 2 and all(d[new_hand[x]] == 3 or d[new_hand[x]] == 2 for x in range(len(new_hand))):
        d['type'] = 5  # 'full_house'
    elif len(d) == 3 and all(value != 2 for value in d.values()):
        d['type'] = 4  # 'tree_of_a_kind'
    elif len(d) == 3 and all(value != 3 for value in d.values()):
        d['type'] = 3  # 'two_pair'
    elif len(d) == 4:
        d['type'] = 2  # 'one_pair'
    elif len(d) == 5:
        d['type'] = 1  # 'high_card'
    d['hand'] = hand
    d['bid'] = bid
    # print(d)
    lst.append(d)

print(lst)

sorted_list = sorted(lst, key=lambda x: (x['type'], list(map(labels[::-1].index, x['hand']))))
print(sorted_list)

answer = 0
for e in range(len(sorted_list)):
    mult = sorted_list[e]['bid'] * (e + 1)
    answer += mult
print(answer)
