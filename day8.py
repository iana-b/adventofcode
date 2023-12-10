# 8.1
from math import gcd

with open('inputs/8.txt', 'r') as file:
    lines = file.read().splitlines()

leftright = lines[0]
lines.remove(lines[0])
lines.remove(lines[0])

d = {}
for line in lines:
    a = line.split(" ")[0]
    b = line.split("(")[1].split(",")[0]
    c = line.split(" ")[3].split(")")[0]
    d[a] = (b, c)

current = 'AAA'
count = 0

while current != 'ZZZ':
    for direction in leftright:
        count += 1
        if direction == 'L':
            current = d[current][0]
        elif direction == 'R':
            current = d[current][1]
print(count)

# 8.2

currents = [i for i in d.keys() if i[-1] == 'A']
counts = [0 for i in d.keys() if i[-1] == 'A']
count = 0

while any(c == 0 for c in counts):
    for direction in leftright:
        if all(c != 0 for c in counts):
            break
        count += 1
        if direction == 'L':
            currents = [d[c][0] for c in currents]
        elif direction == 'R':
            currents = [d[c][1] for c in currents]
        for i in range(len(currents)):
            if currents[i].endswith('Z'):
                counts[i] = count

lcm = 1
for c in counts:
    lcm = lcm * c // gcd(lcm, c)
print(lcm)
