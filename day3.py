# 3.1
import re

with open('inputs/3.txt', 'r') as file:
    lines = file.read().splitlines()

# lines = ['467..114..',
#          '...*......',
#          '..35..633.',
#          '......#...',
#          '617*......',
#          '.....+.58.',
#          '..592.....',
#          '......755.',
#          '...$.*....',
#          '.664.598..']

summa = 0
for i in range(len(lines)):
    for match in re.finditer(r"\d+", lines[i]):
        y = i
        xs = list(range(match.start(), match.end()))
        around = []
        for x in xs:
            for n in range(-1, 2):
                for m in range(-1, 2):
                    new_x = x + m
                    new_y = y + n
                    if [new_y, new_x] not in around and not ((new_x in xs) and (new_y == y)) and (new_x >= 0 and new_y >= 0):
                        around.append([new_y, new_x])
        # print(around)

        is_valid = False

        for each in around:
            x = each[1]
            y = each[0]
            try:
                current = lines[y][x]
                if current != '.':
                    is_valid = True
            except IndexError:
                pass
        if is_valid:
            summa += int(match.group(0))

            # print(match.group(0))

print(summa)

# 3.2
# lines = ['467..114..',
#          '...*......',
#          '..35..633.',
#          '......#...',
#          '617*......',
#          '.....+.58.',
#          '..592.....',
#          '......755.',
#          '...$.*....',
#          '.664.598..']

asterisks = []
for i in range(len(lines)):
    for match in re.finditer(r"\*", lines[i]):
        asterisks.append([i, match.start()])
# print(asterisks)

numbers = []

for i in range(len(lines)):
    for match in re.finditer(r"\d+", lines[i]):
        y = i
        xs = list(range(match.start(), match.end()))
        around = []
        for x in xs:
            for n in range(-1, 2):
                for m in range(-1, 2):
                    new_x = x + m
                    new_y = y + n
                    if [new_y, new_x] not in around and not ((new_x in xs) and (new_y == y)) and (new_x >= 0 and new_y >= 0):
                        around.append([new_y, new_x])
        num = int(match.group(0))
        numbers.append({'number': num, 'around': around})
# print(numbers)

summa = 0
for a in asterisks:
    count = 0
    score = 1
    for n in numbers:
        if a in n['around']:
            count += 1
            score *= n['number']
    # print(score)
    # print(count)

    if count == 2:
        summa += score
print(summa)
