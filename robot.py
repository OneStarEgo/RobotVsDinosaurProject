from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.hp = 300
        self.active_weapon = Weapon("Laser pistol", 75)

    def attack(self, dinosaur):
        print(f"{self.name} blasts its opponent with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage.")
        dinosaur.hp -= self.active_weapon.attack_power
        print(f"{dinosaur.name}'s hp is now {dinosaur.hp}.")
        