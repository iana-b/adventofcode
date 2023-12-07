# 5.1
import re
with open('inputs/5test.txt', 'r') as file:
    lines = file.read().splitlines()

maps = []
seeds = []
# print(lines)
for line in lines:
    # print(line)
    if line.endswith('map:'):
        maps.append([])
    elif line is lines[0]:
        seeds = [int(x) for x in lines[0].split(': ')[1].split(' ')]
    elif re.search(r'\d', line):
        maps[-1].append([int(x) for x in line.split()])
# print(seeds)
# print(maps)

for m in maps:
    for i in range(len(seeds)):
        for dest, src, leng in m:
            # print(dest, src, leng)
            if seeds[i] in range(src, src + leng):
                seeds[i] -= (src - dest)
                break
    # print(seeds)

answer = min(seeds)
# print(answer)

# 5.2
