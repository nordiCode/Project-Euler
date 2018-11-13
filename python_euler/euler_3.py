import math
def factor(x):
    factors = []

    for num in range(1,int(math.sqrt(x)+1)):
        if x%num==0:
            factors.append(num)
    factors.append(x)
    return factors

def is_prime(x):

    for y in range(2,int(math.sqrt(x))):
        if x%y == 0:
            return False
    return True

def prime_factors(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) == True:
            primes.append(num)


    return primes



print(factor(600851475143))
print(prime_factors(factor(600851475143)))

#print(int(math.sqrt(600851475143)))
