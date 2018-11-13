def prime_list(limit):
    p_list =[]
    i = 2

    while i < limit:
        if is_prime(i):
            p_list.append(i)
        i = i +1
    #print(p_list)
    list(set(p_list))
    return p_list

def current_high(numbers,limit):
    current = 2

    i = 0
    j = 0
    counter = 2
    highest_counter=2
    while i < len(numbers):
        current = numbers[i]
        j = i
        while current < limit and (j+1) < len(numbers):
            current = current + numbers[j + 1]
            if highest_counter > (0.5 * len(numbers)):
                break
            if is_prime(current):
                if current < limit:
                    if counter > highest_counter:
                        highest_counter = counter
                        print(current)

            j= j+1
            counter= counter + 1
        counter = 1
        i = i + 1

    return sum_list
def sum_list(numbers,limit):
    #sum_list = []
    current = 2
    high = 0
    i = 0
    j = 0
    counter = 1

    while i < len(numbers):
        current = numbers[i]
        j = i
        while current < limit and (j+1) < len(numbers) :
            current = current + numbers[j + 1]
            counter = counter +1

            if is_prime(current):
                if current < limit:
                    if counter > high:
                        high = counter
                        print(current, counter)
                        #sum_list.append([current,counter])

            j= j+1

        counter = 1
        i = i + 1

    return sum_list

def highest(numbers):

    high = 0
    current = 0
    i = 0
    j=0
    p =2
    while i < len(numbers):
        current = numbers[i][1]
        if current > high:
            high = current
            p = i
        i = i +1
    print("Highest prime:", numbers[p], "Summands:", high)
    return None

def is_prime(number):
    i = 2
    while i < number:
        if number%i == 0:
            return False
        i = i + 1

    return True
#prime_list(1000))
#current_high(prime_list(1000000),1000000)
sum_list(prime_list(100000),1000000)
