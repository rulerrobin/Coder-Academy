import person # the class
# from person import Person # imports only specific classes

p1 = person.Person('John', 40) # if from is imported only need Person()
p2 = person.Person(age = 25,name = 'Mary') # order doesnt matter with keyword arguments (matches class attr)

# Unnecessary due to __init__ function
# p1.name = 'John'
# p2.name = 'Mary'

# wants to create an instance of the class because not usable as another file, need to create an object to represent it and what you are using
# person.Person means importedmodule.classCalled

# p1.greet('Hello')
# p2.greet('Goodbye')
# print(p2.name)

import rpg

aragorn = rpg.Character('Aragorn', 'Human', 100, 50, )
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75, 200)
frodo = rpg.Burglar('Frodo', 'Hobbit', 50, 25)

galadriel.wallet.set(10, 5, 2)


chest = rpg.Chest (['longsword', 'iron helm'], 2, 50, 10)

# print (aragorn.__dict__)
# print (frodo.__dict__)
# print (chest.__dict__)

print (galadriel.__dict__)
chest.loot(galadriel)
print('')
print (galadriel.wallet) #instead of dict by using __repr__ it returns str rep of python memory location
# print(chest.__dict__)
print (galadriel.__dict__)
# print (galadriel.wallet.__dict__)
# print (chest.__dict__)

galadriel.battle(frodo)
frodo.battle(aragorn)
galadriel.portal('Minas Tirith') # Beacons are lit