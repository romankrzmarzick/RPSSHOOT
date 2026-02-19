import random
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm
console = Console()

GAME_MOVES = ["rock", "paper", "scissors"]

class Game:
    
    total_matches = 0

    def __init__(self):
        self.__class__.match_played()
        self.user_score = 0
        self.cpu_score = 0
        self.cpu_move = ""
        
    @classmethod
    def match_played(cls):
        cls.total_matches += 1

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
        return False
    
    def isnot_tie(self):
        return True if self.user_score != self.cpu_score else False 
    
    def who_won(self):
       print("\nYOU WON THE MATCH!\n") if self.user_score > self.cpu_score else print("\nTHE COMPUTER DEFEATED YOU!\n")
    
def welcome_message():
    print("Welcome to RPSS! Each match is best of three — win 2 rounds to win the match. |TWIST|: If the match ends in a tie, the winner must score two consecutive wins.")

def round_message(val): 
    print(f"| ROUND {val} |")

def user_choice():
    return Prompt.ask("What will your move be?", choices=GAME_MOVES)

def play_agin():
    return Confirm.ask("Play again?")

def run():
    welcome_message()
    while True:
        game = Game()
        for i in range(1, 4):
            round_message(i)

            game.cpu_pick()
        
            outcome = game.combination(user_choice())
        
            if outcome:
                print("Round Won!")
                game.apply_score(1)
            elif outcome is False:
                print("Round Lost!")
                game.apply_score(-1)
            elif outcome is None:
                print("Round Tied!")
        

        if game.isnot_tie():
            game.who_won()
        else:
            print("TIEBREAKER MATCH!")
        


        if not play_agin():
            print(f"THANKS FOR PLAYING! [Total Matches Played]: {game.total_matches}")
            break

    
      
       
       
       
run()