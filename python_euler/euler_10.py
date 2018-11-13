# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import my_math as mm
sum =0

for i in range(1,2000001):
    if mm.is_prime(i):
        sum = sum + i

print(sum)
