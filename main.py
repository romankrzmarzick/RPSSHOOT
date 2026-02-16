import random
from rich.prompt import Prompt
from rich.console import Console

console = Console()




class Game:

    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.computer_number = None


    def cpu_num(self):
        self.computer_number = random.choices(self.moves)

    def combination(self, move):
       pass 

    

    