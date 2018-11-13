counter = 0
max = 0
starter = 0

for i in range(1, 1000000):
    counter = 1
    num_beg = i
    while i != 1:
        if i %2 ==0:
            i = i / 2
            counter +=1
        else:
            i = 3*i + 1
            counter +=1

    if counter > max:
        max = counter
        starter = num_beg

print("The max: ", starter, max)
