# 2.1
# 12 red cubes, 13 green cubes, and 14 blue cubes

red = 12
green = 13
blue = 14

lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

with open('inputs/2.txt', 'r') as file:
    lines = file.readlines()

lst = []
for i in range(len(lines)):
    line = lines[i].split(":")[1].split(";")
    # print(line)
    for each in line:
        colors = each.split(",")
        # print(colors)
        for color in colors:
            one_color = color.split(",")
            # print(one_color)
            for number in one_color:
                num = number.split(" ")
                print(num)
                if ('red' in num[2] and int(num[1]) > red) or ('green' in num[2] and int(num[1]) > green) or ('blue' in num[2] and int(num[1]) > blue):
                    lst.append(i + 1)
print(lst)

p_list = []
summa = 0
for r in range(1, len(lines) + 1):
    if r not in lst:
        summa += r
        p_list.append(r)
print(summa)
print(p_list)

# 2.2

lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

with open('inputs/2.txt', 'r') as file:
    lines = file.readlines()

summa = 0

for line in lines:
    max_red = 0
    max_green = 0
    max_blue = 0
    one_line = line.split(":")[1].split(";")
    # print(one_line)
    for each in one_line:
        one = each.split(",")
        # print(one)
        for color in one:
            one_color = color.split(",")
            # print(one_color)
            for n in one_color:
                number = n.split(" ")[1]
                # print(number)
                if 'red' in n.split(" ")[2] and int(number) > max_red:
                    max_red = int(number)
                elif 'green' in n.split(" ")[2] and int(number) > max_green:
                    max_green = int(number)
                elif 'blue' in n.split(" ")[2] and int(number) > max_blue:
                    max_blue = int(number)
    print(max_red, max_green, max_blue)
    mult = max_red * max_green * max_blue
    summa += mult
print(summa)
