"""
Conor Weiss
12/04/22
CS 5001, Fall 2022
Lab 9: Epic Battle Simulator Driver

Armor class file
"""

class Armor:
    '''
    Armor class
    Attributes: name, defense, durability, move, wearer
    methods: str, take_damage
    '''

    def __init__(self, name = "A Shirt", defense = 1, durability = 1, move = None):
        '''
        Constructor -- creates an instance of armor
        parameters: self, name, defense, durability, move
        returns nothing
        '''
        self.name = name
        self.defense = defense
        self.durability = durability
        self.move = move
        self.wearer = None

    def __str__(self):
        '''
        print -- prints the armor's details
        parameters: self
        returns printable string
        '''
        return self.name + ", Defense: " + str(self.defense) + ", Durability: " + str(self.durability)

    def take_damage(self, damage):
        '''
        take_damage -- reduces armor's durability when armor blocks damage.  When durability is used up, armor strength reduced to zero
        parameters: self, damage
        returns nothing
        '''
        self.durability -= damage
        if self.durability <= 0:
            if self.name != "no armor": print("Armor destroyed.")
            try:
                self.wearer.moves.remove(self.move)
                self.wearer.armor = Armor("no armor",0,0)
            except AttributeError: self.name = "no armor"
            except ValueError: self.wearer.armor = Armor("no armor",0,0)
            finally:
                self.durability = 0
                self.defense = 0

    
