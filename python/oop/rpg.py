class Currency: # abstracting an idea
    def __init__(self, gold, silver, copper):
        self.gold = gold
        self.silver = silver
        self.copper = copper

        # Currency is subject to change in the future 
    def set(self, gold, silver, copper):
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def add(self, gold, silver, copper):
        self.gold += gold
        self.silver += silver
        self.copper += copper

    def add_currency(self, currency):
        self.add(currency.gold, currency.silver, currency.copper) #because method already exists above to add

# __repr__ Developer friend representation
    # def __repr_(self): # by using __repr__ it makes a new instance of what is returned e.g when this is printed it will be Currency()
    #     return f'Currency gold={self.gold}, silver={self.silver}, copper={self.copper}'

# End-user readable representation of the object
    def __str__(self):
        return f'{self.gold}G {self.silver}S {self.copper}C'

class Character:

    def __init__(self, name, race, health, attack,mana): # initialisation code
        self.race = race
        self.name = name
        # self.wallet = {'gold:' 0, 'silver:' 0, 'copper': 0} # still good sometimes 
        self.wallet = Currency(0, 0, 0) # this is called composition when different classes can use other things
        # self.gold = 0
        # self.silver = 0
        # self.copper = 0

#created attributes by hardcoding because wants initial amount to be set therefore we need a method that allows this to be changed

        self.health = health
        self.attack = attack
        self.mana = mana
    
    def battle(self, other):
        print(f'{self.name} attacks {other.name}')

class Mage(Character): # can declare new class in class to override parent class to do something different but inherit everything from parent class
    
    def __init__(self, name, race, health, attack,mana): # initialisation code # instead of writing all again can call `super()`
        super().__init__(name, race, health, attack)
        self.mana = mana

    def battle(self, other):
        print(f'{self.name} casts a wicked spell {other.name}')

    def portal(self, destination):
        print(f'{self.name} opens a portal to {destination}')

class Burglar(Character):
    def battle(self, other):
        print(f'{self.name} sneaks in a stealth attack {other.name}')
class Warlock(Mage):
    pass # inherits from MAGE which inherits from Character unless overridden by MAGE

class Chest:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.cash = Currency(gold, silver, copper)

    # transfer chest contents to character
    def loot(self, character):
        # character.gold += self.gold
        # character.silver += self.silver
        # character.copper += self.copper
        
        # do this instead of above 
        # character.wallet.add_currency(self.cash.gold, self.cash.silver, self.cash.copper)
        character.wallet.add_currency(self.cash)
        # access character wallet then access the add method 
        # then set looted chest to 0
        self.cash.set(0,0,0)
        # self.cash.gold = 0
        # self.cash.silver = 0
        # self.cash.copper = 0

