from character import Character
from weapon import Weapon
import unittest

class CharacterTest(unittest.TestCase):
    def test_init_char1(self):
        c1 = Character()
        self.assertEqual(c1.name, "Ward")
        self.assertEqual(c1.hitPoints,5)
        self.assertEqual(c1.strength,5)
        
    def test_init_char2(self):
        c1 = Character("Jane", 1, 2)
        self.assertEqual(c1.name, "Jane")
        self.assertEqual(c1.hitPoints,1)
        self.assertEqual(c1.strength,2)
        
    def test_take_damage(self):
        c1 = Character()
        c1.take_damage(1)
        self.assertEqual(c1.hitPoints,4)
        
    def test_take_damage_zero(self):
        c1 = Character()
        c1.take_damage(25)
        self.assertEqual(c1.hitPoints,0)
        self.assertEqual(c1.alive, False)
        
    def test_init_weapon(self):
        w1 = Weapon()
        self.assertEqual(w1.name, "generic dagger")
        self.assertEqual(w1.strength, 1)
        self.assertEqual(w1.durability,2)
        
    def test_give_weapon(self):
        c1 = Character()
        w1 = Weapon()
        c1.giveWeapon(w1)
        self.assertEqual(c1.weapon.name, "generic dagger")

    def test_weapon_durability(self):
        w1 = Weapon("pool noodle", 1, 1)
        w1.attack()
        self.assertEqual(w1.attack(), 0)

def main():
    unittest.main(verbosity = 3)

main()