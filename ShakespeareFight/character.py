"""
Conor Weiss
12/04/22

Character class file
including move_select function for move selection
"""

import random as rand
import inputTools as it
import copy as c
import graphicsPlus as gp

'''
move_select function
chooses a move from the list of moves available to the character, returns a move without removing it from the list
parameters: move list
returns - move list element
'''
def move_select(list):
    for i in range(len(list)):
        print(i + 1, list[i][0])

    return list[it.bounded_integer_input_validation(len(list),1," ? ") - 1]

'''
damage_filter function
processes an image to show lost health as the battle continues
parameters: graphicsPlus image, character
returns - nothing
'''

def damage_filter(image, char):
    for i in range(int(image.getHeight()*(1 - char.hitPoints/char.max_hp))):
        for j in range(image.getWidth()):
            real_color = image.getPixel(j,i)
            grey_color = gp.color_rgb((real_color[0]+real_color[1]+real_color[2])//3,(real_color[0]+real_color[1]+real_color[2])//3,(real_color[0]+real_color[1]+real_color[2])//3)
            image.setPixel(j,i,grey_color)


class Character:
    '''
    This is a character class for a simple battle game
    Attributes: name, hitPoints, strength, weapon, armor, defense, moves, conditions, alive, smothers, image
    Methods: print, giveWeapon, give_armor, fight, take_damage, attack
    '''
    
    def __init__(self, name = "Ward", hitPoints = 5, strength = 5, defense = 0, moves = [["Normal",1,1],["Power",2,2]], image = None):
        '''
        Constructor -- creates an instance of the character class
        parameters: self (object being created), name, hitPoints (how much health they have), strength (how much damage they do), 
        weapon (what weapon is wielded), armor (what armor is worn), defense (damage mitigation), moves (what moves they can use), 
        conditions (what conditions they suffer from), alive (boolean status variable), smothers (number of rounds they have been smothered)
        image (image file), max_hp (original maximum HP)
        returns -- nothing
        '''
        self.name = name
        self.hitPoints = hitPoints
        self.strength = strength
        self.weapon = None
        self.armor = None
        self.defense = defense
        self.moves = moves
        self.conditions = []
        self.alive = True
        self.smothers = 0
        self.image = image
        self.max_hp = hitPoints

    def __str__(self):
        '''
        print method -- returns the essential info about a character
        '''
        return "Name: " + self.name + ", HP: " + str(self.hitPoints) + ", STR: " + str(self.strength) + ", wielding " + self.weapon.name + ", wearing " + self.armor.name

    def giveWeapon(self, weapon):
        '''
        giveWeapon method -- assigns a weapon to a character
        parameters: self, weapon to be given
        returns nothing
        '''
        self.weapon = weapon
        if weapon.moves != None:
            self.moves.append(weapon.moves)
        weapon.wielder = self

    def give_armor(self, armor):
        '''
        give_armor method -- assigns an armor to the characters
        parameters: self, armor to be worn
        returns nothing
        '''
        self.armor = armor
        if armor.move != None:
            self.moves.append(armor.move)
        armor.wearer = self

    def take_damage(self,damage):
        '''
        take_damage method -- when a character takes damage, reduce their hitpoints, with a minimum bound of zero.  Characters with zero hitpoints are dead.
        parameters: self, damage (amount taken)
        returns nothing
        '''
        
        if not "Invulnerable" in self.conditions:
            self.hitPoints -= damage
        else: self.conditions.remove("Invulnerable")
        
        if "Smothered" in self.conditions:
                self.smothers += 1
                self.conditions.remove("Smothered")
                if self.smothers>=3:
                    self.hitPoints = 0
            
        if self.hitPoints <= 0:
                    
            if "Resurrecting" in self.conditions:
                print(self.name + " was only sleeping!")
                self.hitPoints = 1
                self.conditions.remove("Resurrecting")
            else:
                self.hitPoints = 0
                self.alive = False
    
    def fight(self, opponent):
        '''
        fight method -- pits two characters against each other
        parameters: self, opponent
        returns winner of fight
        '''

        my_future_damage = 0
        op_future_damage = 0
        my_fate = 3
        op_fate = 3
        images = False
        
        if self.image != None and opponent.image != None:
            images = True
        
        if images == True:
            my_image = gp.Image(gp.Point(0,0),self.image)
            damage_filter(my_image,self)
            op_image = gp.Image(gp.Point(0,0),opponent.image)
            damage_filter(op_image,opponent)
            vs = gp.Text(gp.Point(0,0),"VS")
            vs.setTextColor("red")
            vs.setStyle("bold")
            vs.setSize(12)

            window = gp.GraphWin("Shakespearean Tragedy Battle Simulator",my_image.getWidth() + op_image.getWidth() + 25,max(my_image.getHeight(),op_image.getHeight()))
            my_image.move(my_image.getWidth() * 0.5,max(my_image.getHeight(),op_image.getHeight()) * 0.5)
            vs.move(my_image.getWidth() + 10, max(my_image.getHeight(),op_image.getHeight()) * 0.5)
            op_image.move(my_image.getWidth() + 25 + op_image.getWidth() * 0.5, max(my_image.getHeight(),op_image.getHeight()) * 0.5)
            my_image.draw(window)
            op_image.draw(window)
            vs.draw(window)

        round = 0

        while (self.alive and opponent.alive):
            round += 1
            print("\n~~~~~\n\nRound " + str(round) + "\n")
            print(self)
            print(opponent)

            if "Fated to Die" in self.conditions:
                my_fate -= 1
                if my_fate > 0:
                    print("\n" + self.name + " is fated to die in " + str(my_fate) + " rounds.")
                else: 
                    print("\n" + self.name + " will meet their doom at the end of this round.")
                    self.take_damage(self.hitPoints)

            if "Fated to Die" in opponent.conditions:
                op_fate -= 1
                if op_fate > 0:
                    print("\n" + opponent.name + " is fated to die in " + str(op_fate) + " rounds.")
                else:
                    print("\n" + opponent.name + " will meet their doom at the end of this round.")
                    opponent.take_damage(opponent.hitPoints)

            if not "Paralyzed" in self.conditions:
                print("\nWhat move will ", self.name, " use?")

                my_move = move_select(self.moves)
                if my_move[0] == "Fulfill the prophecy":
                    self.armor.take_damage(6)
                self.weapon.durability -= my_move[2]-1  #have to subtract one because of built in durability decrease in weapon.attack() method
                if len(my_move) > 3 and my_move[3] != "":
                    self.conditions.append(my_move[3])
                    print("\n" + self.name + " is " + my_move[3] + "!")
                if "Delayed" in self.conditions:
                    my_future_damage = (rand.randint(1,self.strength) + self.weapon.attack() + my_future_damage) * my_move[1]
                    my_damage = 0
                    self.conditions.remove("Delayed")
                else:
                    my_damage = (rand.randint(1,self.strength) + self.weapon.attack() + my_future_damage) * my_move[1]
                    my_future_damage = 0

            else:
                print("\n" + self.name + " is paralyzed by indecision!")
                self.conditions.remove("Paralyzed")
                self.strength = int(self.strength * 1.5)

            print("\nWhat move will ", opponent.name, " use?")

            if not "Paralyzed" in opponent.conditions:
                op_move = move_select(opponent.moves)
                if op_move[0] == "Fulfill the prophecy":
                    opponent.armor.take_damage(6)
                opponent.weapon.durability -= op_move[2] - 1
                if len(op_move) > 3 and op_move[3] != "":
                    opponent.conditions.append(op_move[3])
                    print("\n" + opponent.name + " is " + op_move[3] + "!")
                if "Delayed" in opponent.conditions:
                    op_future_damage = (rand.randint(1, opponent.strength) + opponent.weapon.attack()) * op_move[1]
                    op_damage = 0
                    opponent.conditions.remove("Delayed")
                else:
                    op_damage = (rand.randint(1, opponent.strength) + opponent.weapon.attack()) * op_move[1]
                    op_future_damage = 0
            else:
                print("\n" + opponent.name + " is paralyzed by indecision!")
                opponent.conditions.remove("Paralyzed")    
                opponent.strength *= 2

            if "Swapping" in self.conditions or "Swapping" in opponent.conditions:
                temp_me = c.copy(self.armor)
                temp_you = c.copy(opponent.armor)
                self.armor.name = "no armor"
                self.armor.take_damage(self.armor.durability)
                self.give_armor(temp_you)
                opponent.armor.name = "no armor"
                opponent.armor.take_damage(opponent.armor.durability)
                opponent.give_armor(temp_me)

            if "Disguised" in self.conditions or "Distracted" in opponent.conditions:
                miss = rand.randint(1,100)
                if miss > 50:
                    op_damage = 0
                    print ("\n" + opponent.name + " cannot focus on their opponent!")
                else:
                    print("\n" + opponent.name + " is no longer confused!")
                    if "Disguised" in self.conditions: self.conditions.remove("Disguised")
                    elif "Distracted" in opponent.conditions: opponent.conditions.remove("Distracted")

            if "Disguised" in opponent.conditions or "Distracted" in self.conditions:
                miss = rand.randint(1,100)
                if miss > 50:
                    my_damage = 0
                    print("\n" + self.name + " cannot focus on their opponent!")
                else:
                    print("\n" + self.name + " is no longer confused!")
                    if "Disguised" in opponent.conditions: opponent.conditions.remove("Disguised")
                    elif "Distracted" in self.conditions: self.conditions.remove("Distracted")
            
            if "Invulnerable" in self.conditions:
                print("\n" + opponent.name + " does " + str(op_damage) + " but " + self.name + " is invulnerable!")
            elif "Vulnerable" in self.conditions:
                print("\n" + opponent.name + " does " + str(op_damage) + " and " + self.name + " is vulnerable!")
            else:
                print("\n" + opponent.name + " does " + str(op_damage) + " but " + self.name + "'s defense blocks " + str(min(op_damage,self.defense + self.armor.defense)) + " of it!")
            if len(op_move) > 4 and not "Invulnerable" in self.conditions and not "Distracted" in opponent.conditions and not "Disguised" in self.conditions:
                self.conditions.append(op_move[4])
                print("\n" + self.name + " is " + op_move[4] + "!")
            if "Vulnerable" in self.conditions and op_damage > 0:
                self.take_damage(op_damage)
                self.conditions.remove("Vulnerable")
            else:
                self.take_damage(max(0,op_damage - (self.defense + self.armor.defense)))
                self.armor.take_damage(op_damage)
            
            
            if "Invulnerable" in  opponent.conditions:
                print("\n" + self.name + " does " + str(my_damage) + " but " + opponent.name + " is invulnerable!")
            elif "Vulnerable" in opponent.conditions:
                print("\n" + self.name + " does " + str(my_damage) + " and " + opponent.name + " is vulnerable!")
            else:
                print("\n" + self.name + " does " + str(my_damage) + " but " + opponent.name + "'s defense blocks " + str(min(my_damage,opponent.defense + opponent.armor.defense)) + " of it!") 
            if len(my_move) > 4 and not "Invulnerable" in opponent.conditions and not "Distracted" in self.conditions and not "Disguised" in opponent.conditions:
                opponent.conditions.append(my_move[4])
                print("\n" + opponent.name + " is " + my_move[4] + "!")
            if "Vulnerable" in  opponent.conditions and my_damage > 0:
                opponent.take_damage(my_damage)
                opponent.conditions.remove("Vulnerable")
            else:
                opponent.take_damage(max(0,my_damage - (opponent.defense + opponent.armor.defense)))
                opponent.armor.take_damage(my_damage)

            if images == True:
                damage_filter(my_image,self)
                damage_filter(op_image,opponent)
                my_image.undraw()
                op_image.undraw()
                my_image.draw(window)
                op_image.draw(window)

        if self.alive: 
            print("\n" + self.name, "has killed", opponent.name)
            window.close()
            if "Fated to Die" in self.conditions:
                self.conditions.remove("Fated to Die")
            return(self)
        
        if opponent.alive: 
            print("\n" + opponent.name, "has killed", self.name)
            window.close()
            if "Fated to Die" in opponent.conditions:
                opponent.conditions.remove("Fated to Die")
            return(opponent)
        
        if not self.alive and not opponent.alive: print("\nDouble Fatality!\n"+ self.name + " and " + opponent.name + " have both died")
        
        window.close()
            
