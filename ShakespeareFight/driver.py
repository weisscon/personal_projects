"""
Conor Weiss
12/04/22
CS 5001, Fall 2022
Lab 9: Epic Battle Simulator Driver"

This program uses character, weapon, armor, condition, and event class objects to run an epic battle simulator.

functions include list_select
"""

from character import Character
from weapon import Weapon
from armor import Armor
import inputTools as it


'''
list_select function
offers a list to a user for selection, removes their selection from the list and returns it
parameters - list
returns - selection
'''

def list_select(list):
    for i in range(len(list)):
        print(i + 1, list[i])

    return list.pop(it.bounded_integer_input_validation(len(list),1," ? ") - 1)

def main():

    #parameters: name, hitPoints (how much health they have), strength (how much damage they do), 
    #weapon (what weapon is wielded), armor (what armor is worn), defense (damage mitigation), moves(what moves they can do),
    #alive (boolean status variable)
        
    c1 = Character("Juliet",100,11,10,[["Normal",1,1],["Play Dead",0,0,"Invulnerable"]],"juliet.gif")
    c2 = Character("Hamlet",50,15,10,[["Normal",1,1],["Overthink",0,0,"Paralyzed"]],"hamlet.gif")
    c3 = Character("Othello",100,20,0,[["Normal",1,1]],"othello.gif")
    c4 = Character("Lady Macbeth",50,20,5,[["Normal",1,1],["Perform upon the unguarded",2,1,"Delayed","Vulnerable"]],"ladymacbeth.gif")
    char_list = [c1, c2, c3, c4]


    #Attributes: name, strength, durability, moves (move options they give to characters)

    w1 = Weapon("Poison",0,100,["Feign Death",0,30,"Resurrecting"])
    w2 = Weapon("Rapier",10,10,["Thrust",2,5])
    w3 = Weapon("Pillow",1,6,["Smother",1,1,"","Smothered"])
    w4 = Weapon("Bloody Dagger",5,10,None)
    weapon_list = [w1, w2, w3, w4]

    a1 = Armor("Masquerade Mask",2,50,["Disguise",0,0,"Disguised"])
    a2 = Armor("Antic Disposition",0,100,["Bait to self-betrayal",0,0,"","Distracted"])
    a3 = Armor("Handkerchief",1,10,["Deliver",0,0,"Swapping"])
    a4 = Armor("Boughs from Great Birnam Wood",10,20,["Fulfill the prophecy",0,0,"","Fated to Die"])
    armor_list = [a1, a2, a3, a4]

    print("\nWelcome to the Shakespearean Tragedy Battle Simulator!!!")

    print("\nFirst Character: ")

    for char in char_list:

        print(char.name)

        print("\nWhich weapon will " + char.name + " wield?")
        
        char.giveWeapon(list_select(weapon_list))

        print("\n" + char.name + " is wielding " + char.weapon.name)

        print("\n~~~~~\n")

        print("Which armor will " + char.name + " wear?")

        char.give_armor(list_select(armor_list))

        print("\n" + char.name + " is wearing " + char.armor.name)

        if len(weapon_list)>0: #since I'm iterating through elements, not an iterable variable, I'm going off a different list to check if I'm done.
            print("\nNext Character: ")
    
    while len(char_list) > 1:
        print("\n\n~~~~~\n\nChoose! Your! Character!\n")

        player_char = list_select(char_list)

        print("\nYou have chosen " + player_char.name)

        print("\n~~~~~\n\nChoose! Your! Opponent!")

        opponent = list_select(char_list)

        char_list.append(player_char.fight(opponent))

    print(char_list[0].name + " is the winner!")









main()