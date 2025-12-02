# 4.1
with open('inputs/4.txt', 'r') as file:
    lines = file.read().splitlines()

# lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
#          'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
#          'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
#          'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
#          'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
#          'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

answer = 0
for line in lines:
    split_lines = line.split('|')
    print(split_lines)
    win_num = list(filter(bool, split_lines[0].split(':')[1].split(' ')))
    print(win_num)
    my_num = list(filter(bool, split_lines[1].split(' ')))
    print(my_num)
    count = 0
    for n in win_num:
        if n in my_num:
            print(n)
            count += 1
    print(count)
    summa = 0
    if count == 1:
        summa += 1
    elif count > 1:
        summa = 1
        summa *= 2 ** (count - 1)
    elif count == 0:
        summa = 0
    print(summa)
    answer += summa
print(answer)

# 4.2

# lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
#          'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
#          'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
#          'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
#          'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
#          'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

a = len(lines)
lst = [1] * a
# print(lst)

for i in range(len(lines)):
    split_lines = lines[i].split('|')
    # print(split_lines)
    win_set = set(filter(bool, split_lines[0].split(':')[1].split(' ')))
    # print(win_set)
    my_set = set(filter(bool, split_lines[1].split(' ')))
    # print(my_set)
    common = win_set.intersection(my_set)
    c = len(common)
    # print(c)
    for cc in range(c):
        lst[i + cc + 1] += lst[i]
    # print(lst)

print(sum(lst))

