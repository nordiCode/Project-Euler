
num_list = []
for x in range(900,1000):
    for y in range(900,1000):
        num_list.append(list(str(x*y)))

for k in num_list:
    if k == k[::-1]:
        print(k)
