spam = ['cat', 'dog', 'bird']
eggs = [12, 78, 100, 54, 42]


# print (eggs[0:-1]) prints all but 42 as not inclusive and -1 ends at 42 since no start value provided
foo = [12.5, 1.78, 3.14159]
person = ['Matt', 50, 185.0]


# tic_tac_toe = [['', '0', ''],['x ', '0', ''],['', 'x', '']]
# print (tic_tac_toe[1][1]) # first [] is outer list second [] is inner list

tic_tac_toe = [
   ['', '0', ''],
   ['x', '0', ''],
   ['', 'x', '']]
# print (tic_tac_toe[1][1])

# index = 1
# for animal in enumerate(spam):
#     print (f'{index}. {animal}')
#     index += 1

import random
print (random.choice(spam))