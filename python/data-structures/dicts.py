# my_cat = ['Pixel', 0.25, 'Tonkinese', 'Chocolate Solid']

my_cat = { 
    'name': 'Pixel',
    'breed' : 'Tonkinese', 
    'color' : 'Chocolate Solid', 
    'age': 25 }


# my_cat.update ({'age': 0.5, 'color': 'Cinnamon'})
## OR
# new_details = {'age': 0.5, 'color': 'Cinnamon'}
# my_cat.update (new_details)
## OR
# my_cat['age'] = 25

# x = my_cat.pop['breed']
# print (x)
# print (my_cat)

# del my_cat['breed'] also deletes


# print (my_cat.items())

# for k, v in my_cat.items():
#     print (f'{k} has the value: {v}')

# for value in my_cat:
#     print(value)

# print (f"{my_cat['name']} is a {my_cat['breed']}")
# if 'foo' in my_cat:
#     print (my_cat['foo'])
# else:
#     print('foo not found')

# print(my_cat[2])

people = [
    {'name': 'Matt', 'age': 50},
    {'name': 'John', 'age': 25},
    {'name': 'Mary', 'age': 34}
]

# for person in people:
#     print (f"{person['name']} is {person['age']} years old")

# Write a program to get a user input of a name. If that name is in the people list, print the details of that person, otherwise print an error message.

while True:
    # 1 Get input from the user
    name = input("Who are you searching for? (Nothing to exit)")
    if name == "": 
        break
    # 2 Compare name to list
    # 3 if Name is in people list print details
    # found = False # sets variable to check however due to else 
    for person in people: # to iterate over list
        if person['name'].lower() == name.lower(): #to check the 'name' field key
            # found = True # sets variable to True once person is found
            print (f"{person['name']} is {person['age']} years old")
            break # one match is found break the loop
    # else print error message

    # if not found:
    #     print(f"{name} not found!")
    # OR
    else: # else can be used as part of for and only be exexcuted if for loop finishes list
        print(f"{name} not found!")
        age = int(input(f'What is {name}\'s age?'))
        new_person = {'name': name, 'age': age}
        people.append(new_person)