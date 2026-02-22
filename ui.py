from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm
from rich.text import Text
from logic import GAME_MOVES
from logic import Game

GAME_TEXT = {
    "welcome_msg" : "Welcome to RPSS! Each match is best of three — win 2 rounds to win the match. |TWIST|: If the match ends in a tie, the winner must have two more wins than losses.",
    "end_msg" : "THANKS FOR PLAYING! [Total Matches Played]:",
    "move" : "What will your move be?",
    "victory" : "YOU WON THE MATCH!",
    "tiebreaker" : "TIEBREAKER MATCH!",
    "defeat" : "THE COMPUTER DEFEATED YOU!",
    "won" : "Round Won!",
    "tie" : "Round Lost!",
    "lost" : "Round Tied!",
    "repeat" : "Play Again?"
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
        return Prompt.ask(Text(GAME_TEXT["move"], style=self.theme["reg"]), choices=GAME_MOVES, console=self.cons)
    
    def round_message(self, val): 
        self.cons.print(f"| Round {val} |", style=self.theme["reg"])
    
    def end_message(self):
        print(f"{GAME_TEXT['end_msg']} {Game.total_matches}")
    
    def display_moves(self, user, cpu):
        self.cons.input(Text(f"| You Chose {user} | [E]", style=self.theme["reg"]))
        self.cons.input(Text(f"| The Computer Chose {cpu} | [E]", style=self.theme["reg"]))

    def play_again(self):
        return Confirm.ask(Text(GAME_TEXT["repeat"], style=self.theme["reg"]), console=self.cons)
    
    def show_position(self, value):
        if value is True:
            print("ONE MORE WIN AWAY FROM VICTORY!")
        elif value is False:
            print("THE COMPUTER IS BEATING YOU!")
        else:
            print("EVEN STEVEN!")
