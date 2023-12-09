# 6.1
with open('inputs/6.txt', 'r') as file:
    lines = file.read().splitlines()

t = [int(x) for x in lines[0].split('Time:')[1].split()]
print(t)
d = [int(x) for x in lines[1].split('Distance:')[1].split()]
print(d)


def find_ways(time, dist):
    ways = 0
    for i in range(1, time):
        way = (time - i) * i
        if way > dist:
            ways += 1
    return ways


answer = 1
for j in range(len(t)):
    answer *= find_ways(t[j], d[j])
# print(answer)

# 6.2
new_time = ''
for each in t:
    new_time += str(each)
print(new_time)

new_dist = ''
for each in d:
    new_dist += str(each)
print(new_dist)

answer = find_ways(int(new_time), int(new_dist))
print(answer)
