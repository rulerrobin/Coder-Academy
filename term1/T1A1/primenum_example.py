
# iterate inclusive 1-100 prime numbers 101 to be inclusive with 100
for num in range (1, 101):
    # check if num is above 1 because 1 is not a primer numbers can only be positive
    if num > 1: 
        is_prime = True 
        # Check if current num is mod == 0 with any numbers so far except itself
        for i in range(2, num):
            # if yes then it is not a prime and go to next loop
            if (num % i) == 0:
                is_prime = False
                break
        # else loop will finish and num will be declared a prime and printed
        if is_prime:
            print(num, end=' ') # end to make it all one line

