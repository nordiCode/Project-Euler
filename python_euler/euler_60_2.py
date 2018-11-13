# The primes 3, 7, 109, and 673, are quite remarkable. 
# By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109,
# both 7109 and 1097 are prime. The sum of these four primes, 792,
# represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

import my_math as mm
limit = 15700
for i in range(1,limit):
    if mm.is_prime(i):
        first = i

        for j in range(first, limit):
            if mm.is_prime(j):
                if mm.is_prime(int(str(first) + str(j))) and mm.is_prime(int(str(j) + str(first))):
                    for k in range(j,limit):
                        if mm.is_prime(k):
                            if mm.is_prime(int(str(first) + str(k))) and mm.is_prime(int(str(k) + str(first))):
                                if mm.is_prime(int(str(k) + str(j))) and mm.is_prime(int(str(j) + str(k))):
                                    for l in range(k,limit):
                                        if mm.is_prime(l):
                                            if mm.is_prime(int(str(first) + str(l))) and mm.is_prime(int(str(l) + str(first))):
                                                if mm.is_prime(int(str(k) + str(l))) and mm.is_prime(int(str(l) + str(k))):
                                                    if mm.is_prime(int(str(j) + str(l))) and mm.is_prime(int(str(l) + str(j))):
                                                        for m in range(l,limit):
                                                            if mm.is_prime(m):
                                                                #print("Into fifth prime territory")
                                                                if mm.is_prime(int(str(first) + str(m))) and mm.is_prime(int(str(m) + str(first))):
                                                                    if mm.is_prime(int(str(k) + str(m))) and mm.is_prime(int(str(m) + str(k))):
                                                                        if mm.is_prime(int(str(j) + str(m))) and mm.is_prime(int(str(m) + str(j))):
                                                                            if mm.is_prime(int(str(l) + str(m))) and mm.is_prime(int(str(m) + str(l))):
                                                                                print("Five primes :", first,j,k,l,m)
                                                                                print("Five prime sum:", first + j + k + l + m)
                                                                                break
