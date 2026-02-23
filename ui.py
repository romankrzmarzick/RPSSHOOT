from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm
from rich.text import Text

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
            "reg" : "white bold",
            "heading" : "dim bold",
            "subheading" : "white"
        }   

    def welcome_message(self):
        self.cons.print(GAME_TEXT["welcome_msg"], style=self.theme["heading"])
           
    def user_choice(self, moves):
        return Prompt.ask(Text(GAME_TEXT["move"], style=self.theme["reg"]), choices=moves, console=self.cons, case_sensitive=False).lower().strip()
    
    def round_message(self, val): 
        self.cons.print(f"| Round {val} |", style=self.theme["reg"])
    
    def end_message(self, matches):
        self.cons.print(f"{GAME_TEXT['end_msg']} {matches}", style=self.theme["reg"])
    
    def display_moves(self, user, cpu):
        self.cons.input(Text(f"| You Chose {user} | [E]", style=self.theme["subheading"]))
        self.cons.input(Text(f"| The Computer Chose {cpu} | [E]", style=self.theme["subheading"]))

    def play_again(self):
        return Confirm.ask(Text(GAME_TEXT["repeat"], style=self.theme["reg"]), console=self.cons)
    
    def tiebreaker_heading(self):
        self.cons.print(GAME_TEXT["tiebreaker"], style=self.theme["heading"])

    def victory(self):
        self.cons.print(GAME_TEXT["victory"], style=self.theme["won"])

    def defeat(self):
          self.cons.print(GAME_TEXT["defeat"], style=self.theme["lost"])

    def show_position(self, value):
        if value is True:
            self.cons.print("ONE MORE WIN AWAY FROM VICTORY!", style=self.theme["won"])
        elif value is False:
            self.cons.print("THE COMPUTER IS BEATING YOU!", style=self.theme["lost"])
        else:
            self.cons.print("EVEN STEVEN!", style=self.theme["tie"])

    def display_result(self, result):
        if result == "tie":
            self.cons.print("Round Tied!", style=self.theme["tie"])
        elif result == "win":
            self.cons.print("Round Won!", style=self.theme["won"])
        else:
            self.cons.print("Round Lost!", style=self.theme["lost"])

     
