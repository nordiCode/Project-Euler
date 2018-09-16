import my_math as mm

num = 2**1000
new_num = list(str(num))
sum = []
x=0
# print(new_num)
# print(len(new_num))
while x < len(new_num):
    print(new_num[x])
    sum.append(int(new_num[x]))
    x+=1


print(mm.sum_list(sum))
