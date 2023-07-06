

    
    @value.setter
    def value(self, value_tuple): 
        gold, silver, copper = value_tuple
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper

    def add(self, gold, silver, copper):
        self.__gold += gold
        self.__silver += silver
        self.__copper += copper

    def __add__(self,other): 
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

    def __str__(self):
        return f'{self.__gold}G {self.__silver}S {self.__copper}C'


class Mage(Character):
    
    def __init__(self, name, race, health, attack,mana): 
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
    pass

class Chest:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.cash = Currency(gold, silver, copper)

    # transfer chest contents to character
    def loot(self, character):
        character.wallet += self.cash
        self.cash.value = 0,0,0


# main


aragorn = rpg.Character('Aragorn', 'Human', 100, 50, )
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75, 200)
frodo = rpg.Burglar('Frodo', 'Hobbit', 50, 25)

galadriel.wallet.value = 10, 5, 2
aragorn.wallet.value = 20, 50, 80
frodo.wallet.value = 5, 25, 20


chest = rpg.Chest (['longsword', 'iron helm'], 2, 50, 10)


print (galadriel.__dict__)
chest.loot(galadriel)
print('')
print (galadriel.wallet) 

print (galadriel.__dict__)


galadriel.battle(frodo)
frodo.battle(aragorn)
galadriel.portal('Minas Tirith') 
aragorn.wallet += frodo.wallet 

print (aragorn.wallet)
print (frodo.wallet)