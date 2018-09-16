def is_even(x):
    return x%2==0


def fibseq(limit):

    ##Fibonanci seq. a_n = a_n1 + a_n2
    term_1  = 1
    term_2 = 1
    previous = 0
    evens = []

    while previous < limit:

            previous = term_2 + term_1
            term_1 = term_2
            term_2 = previous
            if previous > limit:
                break
            #print(previous)
            if is_even(previous):
                evens.append(previous)


    return evens

def sum_even_fib(evens):
    x = 0
    sum = evens[0]

    while x < len(evens)-1:
        sum = sum + evens[x+1]
        #print(sum)
        x = x + 1

    return sum

print(sum_even_fib(fibseq(4000000)))
