def hello(name, age): # can do a default value age=21
    if age.isalnum() == True:
        print (f'Hello {name}, you are {age} years old!')
    else: 
        print ('No')

def get_answer(number):
    match number:
        case 1:
            return 'It is certain'
        case 2:
            return 'It is decidedly so'
        case 3:
            return 'Yes'
        case 5:
            return 'Ask again later'
        case 6:
            return 'Concentrate and ask again'
        case _:
            return 'Reply hazy try again'

#main
# print('Start Main')
# hello('Matt', input('What is your age?')) 
# print('End Main')

# import random
# get_answer(random.randint(1,6))


# add gst to an amount and return the result
def add_gst(amount):
    #sect local variable to the gst rate
    gst_rate = 0.1
    #calculate amount plus gst and return the result
    return subtotal + (subtotal * gst_rate)

#read subtotal from user and convert to float
subtotal = float (input ('Subtotal: $'))
# call add_gst, passing input subtotal as argument
# store returned result in a new variable called total
total = add_gst(subtotal)
# print out total
print(f'total: ${total:.2f}')