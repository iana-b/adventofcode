with open('input.txt', 'r') as file:
    lines = file.read()
answer = 0
for line in lines.split(','):
    start = int(line.split('-')[0])
    end = int(line.split('-')[1])
    for n in range(start, end + 1):
        str_n = str(n)
        size = len(str_n)
        if size % 2 == 0:
            half_size = int(size / 2)
            first_half = int(str_n[:half_size])
            second_half = int(str_n[half_size:])
            if first_half == second_half:
                answer += n
print(answer)
