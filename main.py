import random
from rich.prompt import Prompt
from rich.console import Console

console = Console()

GAME_MOVES = ["rock", "paper", "scissors"]

class Game:

    
    def __init__(self):
        self.user_score = 0
        self.cpu_score = 0
        self.cpu_move = []

    def score_adder(self, val):
        if val == True:
           self.user_score += 1
        if val is False:
            self.cpu_score +=1

    def cpu_num(self):
        self.cpu_move = random.choice(GAME_MOVES)

    def combination(self, user_move, cpu_move):
        if user_move == cpu_move:
            return None
        if (user_move == "paper" and cpu_move == "rock") or (user_move == "rock" and cpu_move == "scissors") or (user_move == "scissors" and cpu_move == "paper"):
            return True 
        else:
            return False

def welcome_message():
    print("Welcome to a classic game of RPSS. One match is three rounds; 2/3 of the rounds won = winner. |TWIST| If scores are tied, it goes until one side wins twice in a row!")

def user_choice():
    return Prompt.ask("What is your move going to be?", choices=GAME_MOVES, case_sensitive=False).lower().strip()

def run():
    welcome_message()
    while True:
        game = Game()
        
        game.cpu_num()
        print(game.cpu_move)
        answ = user_choice()
    
        print(answ)
    
        if answ == final_cpu:
            print("hello world")
       
       
       
run()