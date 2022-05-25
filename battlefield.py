from robot import Robot
from dinosaur import Dinosaur

dinosaur = Dinosaur("BlackTooth", "Tail Whip", 75)
robot = Robot("CX5")
class Battlefield:
    def __init__(self):
        print("Now entering The Battle Zone")
    
    def run_game(self):
        self.display_welcome()
        self.introduce_fighters(robot, dinosaur)
        self.battle_phase()
        self.robot_turn(robot, dinosaur)
        self.dinosaur_turn(robot, dinosaur)
        # self.display_winner()
    
    def display_welcome(self):
        print("-------Welcome! This evening we have a treat for you all!-------")
        print("-------We will finally put the age old question to rest-------.")
        print("-------What would win in a fight between a robot and a dinosaur?-------")
        print("-------Tonight we get our answer! Strap in and prepare for-------")
        print("-------------ROBOTS vs DINOSAURS-------------")    

    def introduce_fighters(self, robot, dinosaur):
        print(f"In the red corner, we have {robot.name}, the Mechanical Monstrosity!")
        print(f"In the blue corner, we have {dinosaur.name}, the Prince of Dinos!")
    
    def battle_phase(self):
        print("Let the battle begin")

    def robot_turn(self, robot, dinosaur):
        robot.attack
        if dinosaur.hp <= 0:
            print(f"{robot.name}'s hp is now {robot.hp}!")

    def dinosaur_turn(self, robot, dinosaur):
        dinosaur.attack
        if robot.hp <= 0:
            print(f"{dinosaur.name}'s hp is now {dinosaur.hp}!")
    



