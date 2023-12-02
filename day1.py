# 1.1
with open('input.txt', 'r') as file:
    lines = file.readlines()

summa = 0
for line in lines:
    lst = []
    for each in line:
        if each.isdigit():
            lst += each

    # print(lst)
    a = lst[0] + lst[-1]
    # print(a)
    summa += int(a)
print(summa)


# 1.2
str_to_digits = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
lst_str_num = list(str_to_digits.keys())

with open('input.txt', 'r') as file:
    lines = file.readlines()

# lines = ['two1nine',
#          'eightwothree',
#          'abcone2threexyz',
#          'xtwone3four',
#          '4nineeightseven2',
#          'zoneight234',
#          '7pqrstsixteen']

# 'eighthree' 83

summa = 0
for line in lines:
    str_num = ''
    n = len(line)
    for i in range(n):
        new_line = line[i:]
        for word in lst_str_num:
            if new_line.startswith(word):
                str_num += str(str_to_digits[word])
                break
        if len(str_num) != 0:
            break

    for i in range(n):
        new_line = line[:len(line)-i]
        for word in lst_str_num:
            if new_line.endswith(word):
                str_num += str(str_to_digits[word])
                break
        if len(str_num) != 1:
            break
    # print(str_num)

    summa += int(str_num)
print(summa)
