"""
Conor Weiss
12/04/22
CS 5001, Fall 2022
Lab 9: Epic Battle Simulator Driver

Weapon class file
"""

class Weapon:

    '''
    This is a weapon class for a simple battle game
    Attributes: name, strength, durability, wielder, moves
    Methods: print, attack
    '''

    def __init__(self, name = 'generic dagger', strength = 1, durability = 2, moves = []):
        self.name = name
        self.strength = strength
        self.durability = durability
        self.moves = moves
        self.wielder = None

    def __str__(self):
        return "Weapon: " + self.name + ", str: " + str(self.strength) + ", dur: " + str(self.durability)

    def attack(self):
        if self.durability <= 0:
            if self.name != "nothing": print("Weapon breaks!")
            try:
                self.wielder.moves.remove(self.moves)
                self.wielder.weapon = Weapon("nothing", 0,0)
            except AttributeError: self.name = "nothing"
            except ValueError: self.wielder.weapon = Weapon("Nothing",0,0)
            return 0
        self.durability -= 1
        return self.strength
        
