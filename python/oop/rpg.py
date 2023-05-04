class Currency: # abstracting an idea
    def __init__(self, gold, silver, copper):
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper

        # Currency is subject to change in the future 
    def set(self, gold, silver, copper):
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper

    @property # Meaning it is considered a attri @property is a 'decoartor'
    def value(self):
        return self.__gold, self.__silver, self.__copper
    
    @value.setter
    def value(self, value_tuple):  # value(self, gold, silver, copper):
        gold, silver, copper = value_tuple
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper

    def add(self, gold, silver, copper):
        self.__gold += gold
        self.__silver += silver
        self.__copper += copper

    def __add__(self,other): # __add__ magic method is used to add the attributes of the class instance in this case currency attributes
        return Currency(
            gold=self.__gold + other.__gold,
            silver=self.__silver + other.__silver,
            copper=self.__copper + other.__copper
        )

    def __iadd__(self, other): # __iadd__ means += 
        if not isinstance(other, Currency): # if not a instance of Currency
            raise TypeError('Can only add Currency to Currency') # stops other from being anything
        
        return Currency(
            gold=self.__gold + other.__gold,
            silver=self.__silver + other.__silver,
            copper=self.__copper + other.__copper
        )

# __repr__ Developer friend representation
    # def __repr_(self): # by using __repr__ it makes a new instance of what is returned e.g when this is printed it will be Currency()
    #     return f'Currency gold={self.__gold}, silver={self.__silver}, copper={self.__copper}'

# End-user readable representation of the object
    def __str__(self):
        return f'{self.__gold}G {self.__silver}S {self.__copper}C'

class Character:

    def __init__(self, name, race, health, attack): # initialisation code
        self.race = race
        self._name = name
        # self.wallet = {'gold:' 0, 'silver:' 0, 'copper': 0} # still good sometimes 
        self.wallet = Currency(0, 0, 0) # this is called composition when different classes can use other things
        # self.__gold = 0
        # self.__silver = 0
        # self.__copper = 0

#created attributes by hardcoding because wants initial amount to be set therefore we need a method that allows this to be changed

        self.health = health
        self.attack = attack
    
    def battle(self, other):
        print(f'{self._name} attacks {other._name}')

class Mage(Character): # can declare new class in class to override parent class to do something different but inherit everything from parent class
    
    def __init__(self, name, race, health, attack,mana): # initialisation code # instead of writing all again can call `super()`
        super().__init__(name, race, health, attack)
        self.mana = mana

    def battle(self, other):
        print(f'{self._name} casts a wicked spell {other._name}')

    def portal(self, destination):
        print(f'{self._name} opens a portal to {destination}')

class Burglar(Character):
    def battle(self, other):
        print(f'{self._name} sneaks in a stealth attack {other._name}')
class Warlock(Mage):
    pass # inherits from MAGE which inherits from Character unless overridden by MAGE

class Chest:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.cash = Currency(gold, silver, copper)

    # transfer chest contents to character
    def loot(self, character):
        # character.__gold += self.__gold
        # character.__silver += self.__silver
        # character.__copper += self.__copper
        
        # do this instead of above 
        # character.wallet.add_currency(self.cash.__gold, self.cash.__silver, self.cash.__copper)
        character.wallet += self.cash
        # access character wallet then access the add method 
        # then set looted chest to 0
        self.cash.value = 0,0,0
        # self.cash.set (0,0,0) no longer needed as changed to attri
        # self.cash.__gold = 0
        # self.cash.__silver = 0
        # self.cash.__copper = 0

