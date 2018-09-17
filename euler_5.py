
#Did this question just using a calculator and what it meant to be a divisor

import my_math as mm


i = 20
divisible =[]
while i < 300000000:
    check = True
    for j in range(1,21):
        if i%j !=0:
            check = False
            break
    if check ==True:
        print(i)
    i +=1
print(divisible)
