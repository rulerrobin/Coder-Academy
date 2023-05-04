from calculator import square, cube

nums = [10, 14, 21, 50, 5, -6]

# # squared_values = map(square, nums) # moves list to new list (function(), iterable) produces a map object
# cubed_values = map(cube, nums)

squared_values = map(lambda num: num * num, nums) #lambda makes function as anonymous or no name | if two arguments it needs to be lambda ()
# squared_values = [square(x) for x in nums] 
# # square x for indexed value in num this is a list comprehension instead of below
# # for num in nums:
# #     squared_values.append(square(num))
    

# print(list(enumerate(nums))) # enumarate creates a new list in a tuple pairing with number next to it
# # enumarate works on any iterable
# print(list(squared_values)) # converted to list from map object
# print(list(cubed_values))

# # replaced with code below 
# # def add_prefix(tuple): # could not accept 2 values because map pases a single parameter so below code did not work
# def add_prefix(index, value):
# #     index, value = tuple 
#     return f'{index + 1}. {value.strip()}' 

# with open('shopping-list.txt') as f:
#     # print(list(enumerate(f)))
#     # numbered = map(add_prefix, list(enumerate(f))) # tuple
#     # numbered = [f'{index + 1}. {value.strip()}' for index, value in enumerate(f)] # replaced above by doing a normal for loop but instead of a body it puts expression before the for loop, this gets evaluated in each iteration
#     # all results are gathered in a list automatically
#     numbered = [add_prefix(index, value) for index, value in enumerate(f) if index % 2 ==0]
#     print(list(numbered))

students = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Gryffindor'},
    {'name': 'Hermione', 'house': 'Gryffindor'},
    {'name': 'Draco', 'house': 'Slytherin'}
    
]

# print([student['name']for student in students if student['house'] == 'Gryffindor'])

def is_gryffindor(student):
    return student['house'] == 'Gryffindor'

def get_name(student):
    return student['name']

print(list(map(get_name, filter(is_gryffindor, students)))) # filter takes a function that returns a boolean and can goes list to find
# if map is not used 