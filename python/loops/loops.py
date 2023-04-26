# spam = 0 
# if spam < 5:
#     print ('Hello')
#     spam = spam + 1

# for i in range (1, 10, 3): # (start, end, steps)
#     #some functions do not allow for keyword arguemnts
#     print (i)

import random
count = int(input('How many random numbers? '))
for i in range (count):
    print (random.randint(1,100))