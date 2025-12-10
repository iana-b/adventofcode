with open('input.txt', 'r') as file:
    lines = file.readlines()
lst = []
for line in lines:
    column = []
    for sign in line.split():
        column.append(sign)
    lst.append(column)
total = 0
new_lst = list(zip(*lst))
for each in new_lst:
    operator = each[-1]
    numbers = each[:-1]
    answer = 0
    if operator == '*':
        answer = 1
        for number in numbers:
            answer *= int(number)
    elif operator == '+':
        for number in numbers:
            answer += int(number)
    total += answer
print(total)
