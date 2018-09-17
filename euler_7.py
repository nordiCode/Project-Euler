#What is the 10 001st prime number?

import my_math as mm

i = 1
count=0
while i < 10000000:
    if mm.is_prime(i):
        count +=1

    if count == 10001:
        print("This is the prime",count,i)
        break
    if count ==1:
        print("This is the first prime,",count,i)

    i +=1
