# f = open('shopping-list.txt') # can put full file name however if in same folder that can use name of file

# # Statements to work with the file

# data = f.read()
# print(data)

# f.close

# this is cleaner and closes file automatically
# with open('shopping-list.txt') as f:
#     for line in f:
#         print(f'Item: {line.strip()}') # reads line by line
#     # data = f.readline().strip()
#     # data = f.read(3) # reads first three chars
#     # spam = f.read(2) # reads next 2
#     # print(data.strip())
#     # print(spam)

shows = [
    'The Witcher'
    'The X Files'
    'Star Trek Picard'
    'The Mandalorian'
]

# WRITING FILES
# with open('tv-shows.txt', 'w') as f:
#     f.write('\n'.join(shows))
#     f.writelines('\n'.join(shows))
#     # f.write('The Witcher\n')
#     # f.write('The X Files\n')
#     # f.write('Star Trek Picard\n')

import csv

# with open ('people.csv') as f:
#     # reader = csv.reader(f) # Creates a reader object based on the file object and it is iterable
#     reader = csv.DictReader(f) # Creates a dict instead of list to index for data as we ll as using top row for keywords
#     # reader.__next__() # means go to next row e.g. without this it would include header row
#     for row in reader:
#         print(f"{row['name']} is {row['age']} years old and {row['height']} cm tall")

menu = [
    {'item':'Cappucino', 'price': 5.50},
    {'item':'English Breakfast Tea', 'price': 4},
    {'item': 'Blueberry Muffin', 'price': 6}
]

# with open('cafe-menu.csv', 'w') as f:
#     writer = csv.DictWriter(f, menu[0].keys()) # insttead of a hard code list it accesses the [0] item and gets they .keys from there
#     # writer = csv.DictWriter(f, ['item', 'price']) # accepts a list and writes it out as a CSV file | to ommit a column
#     # writer.writerow(['item', 'price'])
#     writer.writeheader() # because its a dict it will write keys as headers
#     writer.writerows(menu)

import json

# with open ('movies.json') as f:
#     movies = json.load(f) # parses json data into python objects of lists and dictionariees
#     print(movies[0])

with open ('cafe-menu.json', 'w') as f:
    json.dump(menu, f, indent=2) # first parameter is data structure to file, second is where it goes since `f` is opened as **file** indent = \n