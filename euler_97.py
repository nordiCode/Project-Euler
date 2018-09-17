# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
#
# Find the last ten digits of this prime number.
import my_math as mm
last_digits = []
last = 10

while last < 10**11:
    print(((28433*2**7830457)+1)%last)
    last = last*10
