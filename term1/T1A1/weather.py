# two variables available declared and must take in bool or int
raining = bool(input("Is it raining?(True/False)"))
temperature = int(input('What is the temperature?(input as a number)'))

#  If it’s raining and the temperature is less than 15 degrees, 
if raining == True and temperature < 15:
    print ('It’s wet and cold')
# if it is less than 15 but not raining
elif raining == False and temperature < 15:
    print ('It not raining but cold')
# If it’s greater than or equal to 15 but not raining
elif raining == False and temperature >= 15:
    print ('It’s warm but not raining')
# otherwise
else:
    print ('It\'s warm and raining')
