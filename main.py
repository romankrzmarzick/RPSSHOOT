import random
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm

GAME_MOVES = ["rock", "paper", "scissors", "lizard", "spock"]

class Game:
    
    total_matches = 0

    def __init__(self):
        self.__class__.match_played()
        self.user_score = 0
        self.cpu_score = 0
        
    @classmethod
    def match_played(cls):
        cls.total_matches += 1

    def apply_score(self, val):
        if val == 1:
           self.user_score += 1
        elif val == -1:
            self.cpu_score += 1
    
    def cpu_pick(self):
        return random.choice(GAME_MOVES)

    def combination(self, user_move, cpu_move):
        win_conditions = {
            "rock" : {"scissors","lizard"},
            "paper" : {"rock", "spock"},
            "scissors " : {"paper", "lizard"},
            "lizard" : {"spock", "paper"},
            "spock" : {"rock", "scissors"}
        }
        if user_move == cpu_move: return None
        return True if cpu_move in win_conditions[user_move] else False
    
    def isnot_tie(self):
        return self.user_score != self.cpu_score
    
    def who_won(self):
       print("\nYOU WON THE MATCH!\n") if self.user_score > self.cpu_score else print("\nTHE COMPUTER DEFEATED YOU!\n")
    
    
def run():
    ui = UI()
    ui.welcome_message()
    while True:
        game = Game()
        for i in range(1, 4):
            if game.user_score == 2 or game.cpu_score == 2:
                break
            
            ui.round_message(i)

            cpu_move = game.cpu_pick()
            user_move = ui.user_choice()
            outcome = game.combination(user_move, cpu_move)
            
            ui.move_interface(user_move, cpu_move)

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
                    print(ui.game_state(tie_score))
                
                cpu_move = game.cpu_pick()
                user_move = ui.user_choice()
                tie_rounds = game.combination(user_move, cpu_move)
                ui.move_interface(user_move, cpu_move)


                if tie_rounds is True:
                    tie_score += 1
                    print("Round Won!")
                elif tie_rounds is False:
                    print("Round Lost!")
                    tie_score -=1
                else:
                    print("Round Tied!")
                
                not_first_round = True

            print("YOU WON AGAINST THE COMPUTER!") if tie_score > 0 else print("THE COMPUTER BEAT YOU!")
            
        if not ui.play_again():
            
            break
    

run()


GAME_TEXT = {
    "welcome_msg" : "Welcome to RPSS! Each match is best of three — win 2 rounds to win the match. |TWIST|: If the match ends in a tie, the winner must have two more wins than losses."
    ""   
}


class UI:
    def __init__(self):
        self.cons = Console()
        self.theme = {
            "won" : "bold green",
            "tie" : "yellow blink",
            "lost" : "bold red",
            "reg" : "white bold"
        }
    def welcome_message(self):
        self.cons.print(GAME_TEXT["welcome_msg"], style=self.theme["reg"])
           
    
    def user_choice(self):
        return Prompt.ask("What will your move be?", choices=GAME_MOVES)
    
    def round_message(self, val): 
        self.cons.print(f"| ROUND {val} |", style=self.theme["reg"])

    def game_state(self, value):
        if value == 0: return "THE MATCH IS TIED."
        return "ONE MORE WIN AWAY!" if value > 0 else "THE COMPUTER ALMOST HAS YOU BEAT!"
    
    def good_bye(self):
        print(f"THANKS FOR PLAYING! [Total Matches Played]: {Game.total_matches}")

    def move_interface(self, user, cpu):
        input(f"| You Chose {user} | [E]")
        input(f"| The computer chose {cpu} | [E]")
    
    def play_again(self):
        
        return Confirm.ask("Play again?")
    
      
def upper(func):
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        return output.upper()
    return wrapper