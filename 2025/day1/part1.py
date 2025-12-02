with open('input.txt', 'r') as file:
    lines = file.readlines()
dial = [i for i in range(0, 100)]
start = 50
count = 0


def cyclic(lst, i):
    return lst[i % len(lst)]


for line in lines:
    print(line)
    line.rstrip('\n')
    if line.startswith('R'):
        start += int(line[1:])
        start = cyclic(dial, start)
    elif line.startswith('L'):
        start -= int(line[1:])
        start = cyclic(dial, start)

    if start == 0:
        count += 1
    print(start)
    print("count", count)

print(count)
