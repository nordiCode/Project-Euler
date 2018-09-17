# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import my_math as mm

for m in range(0,500):
    for n in range(0,500):
        z = 1000 -m-n
        #print(m, n,z)
        if (m*m + n*n) == z*z:
            print("Found them: ",m,n,z)
            print(m+n+z)
