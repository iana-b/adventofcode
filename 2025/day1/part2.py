with open('input.txt', 'r') as file:
    lines = file.readlines()
start = 50
count = 0

for line in lines:
    line = line.rstrip('\n')
    direction = line[0]
    number = int(line[1:])
    for i in range(number):
        if direction == "L":
            start -= 1
            if start == 0:
                count += 1
            if start == -1:
                start = 99
        elif direction == "R":
            start += 1
            if start == 100:
                start = 0
            if start == 0:
                count += 1

print(count)
