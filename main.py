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
        if val == 1:
           self.user_score += 1
        elif val == -1:
            self.cpu_score += 1
    
    def cpu_pick(self):
        self.cpu_move = random.choice(GAME_MOVES)

    def combination(self, user_move):
        if user_move == self.cpu_move:
            return None
        if (user_move == "paper" and self.cpu_move == "rock") or (user_move == "rock" and self.cpu_move == "scissors") or (user_move == "scissors" and self.cpu_move == "paper"):
            return True 
        return False
    
    def isnot_tie(self):
        return self.user_score != self.cpu_score
    
    def who_won(self):
       print("\nYOU WON THE MATCH!\n") if self.user_score > self.cpu_score else print("\nTHE COMPUTER DEFEATED YOU!\n")
    
def welcome_message():
    print("Welcome to RPSS! Each match is best of three — win 2 rounds to win the match. |TWIST|: If the match ends in a tie, the winner must have two more wins than losses.")

def round_message(val): 
    print(f"| ROUND {val} |")

def user_choice():
    return Prompt.ask("What will your move be?", choices=GAME_MOVES)

def play_again():
    return Confirm.ask("Play again?")

def game_state(value):
    if value == 0: return "THE MATCH IS TIED."
    return "ONE MORE WIN AWAY!" if value > 0 else "THE COMPUTER ALMOST HAS YOU BEAT!"
    
def run():
    welcome_message()
    while True:
        game = Game()
        for i in range(1, 4):
            if game.user_score == 2 or game.cpu_score == 2:
                break
            
            round_message(i)

            game.cpu_pick()
            user_move = user_choice()
            outcome = game.combination(user_move)
            input(f"You Chose {user_move} [E]".upper())
            input("The Computer Chose... [E] ".upper())
            print(game.cpu_move.upper())

            if outcome is True:
                print("Round Won!")
                game.apply_score(1)
            elif outcome is False:
                print("Round Lost!")
                game.apply_score(-1)
            else:
                print("Round Tied!")
        

        if game.isnot_tie():
            game.who_won()
        else:
            print("\nTIEBREAKER MATCH!\n")
            
            tie_score = 0
            not_first_round = False

            while -2 < tie_score < 2:
                if not_first_round: 
                    print(game_state(tie_score))
                
                game.cpu_pick()
                user_move = user_choice
                tie_rounds = game.combination(user_move)

                input(f"You Chose {user_move} [E]".upper())
                input("The Computer Chose... [E]".upper())
                print(game.cpu_move.upper())

                if tie_rounds:
                    tie_score += 1
                    print("Round Won!")
                elif tie_rounds is False:
                    print("Round Lost!")
                    tie_score -=1
                elif tie_rounds is None:
                    print("Round Tied!")
                
                not_first_round = True

            print("YOU WON AGAINST THE COMPUTER!") if tie_score > 0 else print("THE COMPUTER BEAT YOU!")
            
        if not play_again():
            print(f"THANKS FOR PLAYING! [Total Matches Played]: {Game.total_matches}")
            break
    

run()
