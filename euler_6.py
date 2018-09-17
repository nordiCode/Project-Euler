#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Sum from 1 to n
def sum_to_n(n):
    sum = (n*(1+n))*0.5
    return sum

def sum_of_squares(n):
    sos = (n*(n+1)*(2*n+1))*(0.16666666666666666)
    return int(sos)

ari_sum = sum_to_n(100)
ari_sum = ari_sum**2
print(ari_sum)
sos=sum_of_squares(100)
print(sos)
print("Difference is ", sos - ari_sum)
