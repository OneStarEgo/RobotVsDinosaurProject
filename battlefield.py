from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("BlackTooth", "Tail Whip", 75)
        self.robot = Robot("CX5")
        print("Now entering The Battle Zone")
    
    def run_game(self):
        self.display_welcome()
        self.introduce_fighters(self.robot, self.dinosaur)
        self.battle_phase()
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
        # if you call the dino and robot turns here it would make sense to have them in a while loop
        # while the dino health AND robot health are greater than 0 loop
        while self.dinosaur.hp > 0 and self.robot.hp > 0:
            self.robot_turn("CX5", "BlackTooth")
            if self.dinosaur.hp < 0:
                print("robot dead")
            # may need "if" to check that everybody is still alive before this step
            self.dinosaur_turn("BlackTooth", "CX5")
            if self.robot.hp < 0:
                print("dinosaur dead")


    def robot_turn(self, robot, dinosaur):
        self.robot.attack(dinosaur)
        if dinosaur.hp <= 0:
            print(f"{robot.name}'s hp is now {robot.hp}!")

    def dinosaur_turn(self, robot, dinosaur):
        self.dinosaur.attack(robot)
        if robot.hp <= 0:
            print(f"{dinosaur.name}'s hp is now {dinosaur.hp}!")
    



