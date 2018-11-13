#First fibonacci term with over 1000 digits

term_1  = 1
term_2 = 1
previous = 1
limit = 100000000

count =1

while previous < 10**999:
    count +=1
    previous = term_2 + term_1
    term_1 = term_2
    term_2 = previous
    #print(previous)
    if previous > 10**999:
        print(count)
