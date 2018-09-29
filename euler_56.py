# Considering natural numbers of the form, ab,
#  where a, b < 100, what is the maximum digital sum?

num = 0
sum = 0
max = 0


for i in range(1,100):
    for j in range(1,100):
        sum = 0
        num = i**j
        num = list(str(num))
        for x in range(0, len(num)):
            sum += int(num[x])

        if sum > max:
            max = sum

print(max)
