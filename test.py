from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.text import Text
console = Console()
from game_rules import Game
from ui import Interface
from player import Player
from player import Robot
from data import Data
from random_ai import RandomAI
import sys
ai_brain = RandomAI()
from collections import Counter
import random

game = Game()
ui = Interface()
p1 = Player()
robot = Robot(ai_brain)
data = Data()



class CommonAI:   

    def choose_move(self, context):
        rules = context["rules"]
        data = ["rock", "paper", "scissors", "scissors", "scissors", "scissors", "scissors", "scissors", "paper", "paper", "paper", "paper", "paper", "paper", "paper", "paper", "paper", "rock", "rock", "rock", "rock", "rock", "rock", "rock"]

        if not data:
            return random.choice(list(rules.keys()))
        
        common_move = Counter(data).most_common(1)[0][0]
        
        print(f"Common Move: {common_move}")
        
        
        
        for move in rules[common_move]:
            counter_moves.append(move)
            return random.choice()
    

context = {
    "rules" : game.game_mode,
    "data" : data.user_move_history,
    "user_score" : p1.score,
    "cpu_score" : robot.score
}

ai = CommonAI()
ai.choose_move(context)