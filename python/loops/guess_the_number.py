# Guess number game
# 6 Guesses to guess a number between 1 and 20

#pseudo
# import random module
import random
# assign a random number to variable
number = random.randint(1, 20)
# for guesses guesses_left in 6..1 pseduo has range as start..stop 
for guesses_left in range (6, 0, -1):
    # ask for a guess
    guess = int(input(f'Take a guess ({guesses_left})left:'))
    # display hint 'higher', 'lower', or 'correct
    if guess < number:
        print ('Too low!')
    elif guess > number:
        print ('Too high!')
     # if corret, end program
    else:
        print ('Correct!')
        break

    # if 6 incorrect guesses
if guess != number:
    print(f'Sorry! The number was {number}')

