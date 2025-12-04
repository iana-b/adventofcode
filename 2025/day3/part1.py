with open('input.txt', 'r') as file:
    lines = file.readlines()
answer = 0
for line in lines:
    numbers = [int(n) for n in line.rstrip()]
    first_number = max(numbers[:len(numbers) - 1])
    first_number_index = numbers.index(first_number)
    second_number = max(n for n in numbers[first_number_index + 1:])
    second_number_index = numbers.index(second_number)
    joltage = int(str(first_number) + str(second_number))
    answer += joltage
print(answer)

