
class Dinosaur:
    
    def __init__(self, name, attack_name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.attack_name = attack_name
        self.hp = 300
    
    def attack(self, robot):
        print(f"{self.name} lands a vicious {self.attack_name} on it opponent for {self.attack_power} damage!")
        robot.hp -= self.attack_power
        print(f"{robot.name}'s hp is now {robot.hp}")


