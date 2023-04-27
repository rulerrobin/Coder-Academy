class Person:

    # convention dictates should be at top of class
    # if python finds method with the name it will activate immediately, meaning during initialization will complete task
    # Is a Constructor - purpose is to initialize object
    def __init__(self, name):
        self.name = name # take value of name and create attribute with that value
        # during initialization of p1 = blah.blah can take in value


    def greet(self, prefix): # self is automatically generated due to implicit link to object p1 the next one is explicit parameter
        print(f'{prefix}, {self.name}')