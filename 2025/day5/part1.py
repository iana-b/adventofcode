with open('input.txt', 'r') as file:
    lines = file.read()
data = lines.split('\n')
blank_line_index = data.index('')
ranges = data[:blank_line_index]
ids = list(map(int, data[blank_line_index + 1:]))
count = 0
for i in ids:
    for r in ranges:
        min_num = int(r.split('-')[0])
        max_num = int(r.split('-')[1])
        if min_num <= i <= max_num:
            count += 1
            break
print(count)
