import person # the class
# from person import Person # imports only specific classes

p1 = person.Person('John') # if from is imported only need Person()
p2 = person.Person('Mary')

# Unnecessary due to __init__ function
# p1.name = 'John'
# p2.name = 'Mary'

# wants to create an instance of the class because not usable as another file, need to create an object to represent it and what you are using
# person.Person means importedmodule.classCalled

p1.greet('Hello')
p2.greet('Goodbye')
# print(p2.name)