# def get_answer(number):
#     match number:
#         case 1:
#             return 'It is certain'
#         case 2:
#             return 'It is decidedly so'
#         case 3:
#             return 'Yes'
#         case 5:
#             return 'Ask again later'
#         case 6:
#             return 'Concentrate and ask again'
#         case _:
#             return 'Reply hazy try again'

print('Magic 8 Ball')
import random
answers = [
    'It is certain',
    'It is decidedly so',
    'Yes',
    'Ask again later',
    'Concentrate and ask again',
    'Reply hazy try again'
]
# print(answers[random.randint(0,len(answers) - 1)])
# for run and debug to understand use code below 
# try using without - 1 for what happens without it
# also try print (len(answers)) to understand array length vs index length
x = random.randint(0,len(answers) - 1)
print (answers[x])