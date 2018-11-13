
numbers = []

for x in range(2,101):
    for y in range(2,101):
        num = x **y
        numbers.append(num)

set_num = set(numbers)

print(len(set_num))
