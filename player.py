import random

class Character:
    def __init__(self, name):
        self.score = 0 
        self.name = name      

    def addpoint(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

class Player(Character):
    def __init__(self, name="Roman"):
        super().__init__(name)

class Robot(Character):
    def __init__(self, name="Computer"):
        super().__init__(name)
    
    def robot_move(self, moves):
        return random.choice(list(moves.keys()))
        
    