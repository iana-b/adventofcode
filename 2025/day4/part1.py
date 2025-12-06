with open('input.txt', 'r') as file:
    lines = file.readlines()
rolls_accessed = 0
new_lines = []
for line in lines:
    new_line = '.' + line.rstrip() + '.'
    new_lines.append(new_line)
size_x = len(new_lines[0])
new_lines.append('.' * size_x)
new_lines.insert(0, '.' * size_x)
size_y = len(new_lines)

for i in range(size_y):
    for j in range(size_x):
        if new_lines[i][j] == '@':
            count = 0
            if new_lines[i][j - 1] == '@':
                count += 1
            if new_lines[i][j + 1] == '@':
                count += 1
            if new_lines[i - 1][j - 1] == '@':
                count += 1
            if new_lines[i - 1][j] == '@':
                count += 1
            if new_lines[i - 1][j + 1] == '@':
                count += 1
            if new_lines[i + 1][j - 1] == '@':
                count += 1
            if new_lines[i + 1][j] == '@':
                count += 1
            if new_lines[i + 1][j + 1] == '@':
                count += 1
            if count < 4:
                rolls_accessed += 1
print(rolls_accessed)
