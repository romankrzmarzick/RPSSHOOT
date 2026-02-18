import random
from rich.prompt import Prompt
from rich.console import Console

console = Console()

GAME_MOVES = ["rock", "paper", "scissors"]

class Game:

    
    def __init__(self):
        self.user_score = 0
        self.cpu_score = 0
        self.cpu_move = ""
        self.rounds = 0
    def apply_score(self, val):
        if val > 0:
           self.user_score += val
        if val < 0:
            self.cpu_score += abs(val)
        

    def cpu_pick(self):
        self.cpu_move = random.choice(GAME_MOVES)

    def combination(self, user_move):
        if user_move == self.cpu_move:
            return None
        if (user_move == "paper" and self.cpu_move == "rock") or (user_move == "rock" and self.cpu_move == "scissors") or (user_move == "scissors" and self.cpu_move == "paper"):
            return True 
        else:
            return False
    
    def tiebreaker(self):
        pass



    def add_round(self):
        self.rounds += 1



    
    
def welcome_message():
    print("Welcome to a classic game of RPSS. One match is three rounds; if 2/3 of the rounds are won = winner. |TWIST| If scores are tied, one must win twice in a row!")

def user_choice():
    return Prompt.ask("What will your move be?", choices=GAME_MOVES)

def round_message(val): 
    print(f"| ROUND {val} |")

def run():
    welcome_message()
    game = Game()
    for i in range(1, 4):
        round_message(i)

        game.cpu_pick()
        print(f"Debugger {game.cpu_move}")
        outcome = game.combination(user_choice())
        print(f"Debugger {outcome}")
        if outcome:
            print("You Won")
            game.apply_score(1)
        
        if outcome is False:
            print("You Lost!")
            game.apply_score(-1)
        
        if outcome is None:
            print("You Tied!")
        

    
      
       
       
       
run()