# 9.1

with open('inputs/9.txt', 'r') as file:
    lines = file.read().splitlines()


def find_next(my_line):
    if all(num == 0 for num in my_line):
        return 0
    new_line = []
    for i in range(len(my_line) - 1):
        new_line.append(int(my_line[i + 1]) - int(my_line[i]))
    return int(my_line[-1]) + find_next(new_line)


summa = 0
for line in lines:
    ll = find_next(line.split(' '))
    summa += ll
print(summa)

# 9.2


def find_prev(my_line):
    if all(num == 0 for num in my_line):
        return 0
    new_line = []
    for i in reversed(range(1, len(my_line))):
        new_line.insert(0, int(my_line[i]) - int(my_line[i - 1]))
    return int(my_line[0]) - find_prev(new_line)


summa = 0
for line in lines:
    ll = find_prev(line.split(' '))
    summa += ll
print(summa)

# or

summa = 0
for line in lines:
    ll = find_next(line.split(' ')[::-1])
    summa += ll
print(summa)
