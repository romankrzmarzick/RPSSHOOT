from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.text import Text


GAME_TEXT = {
    "welcome_msg": (
        "Welcome to RPSS! Each match is best of three — "
        "win 2 rounds to win the match. "
        "|TWIST|: If the match ends in a tie, the winner must "
        "have two more wins than losses."
    ),
    "game_rules" : (
        "|Games Rules|\nThe user plays the amount of gamess selected, the first to get the best score from the rounds wins."
        "If scores are still tied, a tiebreaker game commences. In the tiebreaker, the winner must win two times before a loss."
        "Meaning back to back wins isn't required. A tie is meaningless. Example: Win-Tie-Win = Match Won"
        "User can also choose between a classical game or RPS with Spock and Lizard (search online for the rules if needed)."
    ),
    "end_msg" : "Thanks for playing and have a splendid day",

    # --- Match Decisions ---
    "victory": "YOU WON THE MATCH!",
    "defeat": "THE COMPUTER DEFEATED YOU!",
    "tiebreaker": "TIEBREAKER MATCH!",
   
    # --- Round Decisions --- 
    "win": "Round Won!",
    "lose": "Round Lost!",
    "tie": "Round Tied!",
    
    # --- Inputs ---
    "input": "|Exit[q]| |Rules[?]| | What will be your move? |",
    "replay": "Play Again?",
    "game_mode" : "Game Mode Selection",
    "games" : "|Pick the amount of rounds for the game|",
    
    # --- Tiebreaker Round ---
    "even": "EVEN STEVEN!",
    "cpu": "THE COMPUTER IS BEATING YOU!",
    "user": "ONE MORE WIN AWAY FROM VICTORY!",
}


class Interface:
    def __init__(self):
        self.cons = Console()
        self.styles = {
            "win": "bold green",
            "lose": "bold red",
            "tie": "yellow",
            "base": "white",
            "fyi": "dim bold",
            "main": "white bold"
        }   
    
    def welcome_message(self):
        self.cons.print(GAME_TEXT["welcome_msg"], style=self.styles["fyi"])

    def game_guide(self):
        self.cons.print(GAME_TEXT["game_rules"], style=self.styles["fyi"])

    def end_message(self, name):
        self.cons.print(f"\n{GAME_TEXT['end_msg']} {name}!", style=self.styles["base"])
    
    # --- Round Decisons ---
    def show_round_result(self, outcome):
        """The outcome variable will either contain the string 'win', 'lose', or 'tie' for the GAME_TEXT dictionary lookup."""
        self.cons.print(GAME_TEXT[outcome], style=self.styles[outcome])

    # --- Match Decisions
    def tiebreaker_heading(self):
        self.cons.print(GAME_TEXT["tiebreaker"], style=self.styles["main"])

    def victory(self):
        self.cons.print(GAME_TEXT["victory"], style=self.styles["win"])

    def defeat(self):
        self.cons.print(GAME_TEXT["defeat"], style=self.styles["lose"])

    # --- User Inputs ---
    def choose_replay(self):
        return Confirm.ask(Text(GAME_TEXT["replay"], style=self.styles["main"]), console=self.cons)

    def choose_move(self, moves):
        return (Prompt.ask(Text(GAME_TEXT["input"], style=self.styles["main"]), choices=[*moves, "q", "?"], case_sensitive=False, console=self.cons).lower().strip())
    
    def choose_rounds(self):
        choices = ["3", "5", "7"]
        return int(Prompt.ask(Text(GAME_TEXT["games"], style=self.styles["base"]), choices=[*choices], console=self.cons).lower().strip())

    def choose_mode(self):
        return (Prompt.ask(Text(GAME_TEXT["game_mode"], style=self.styles["base"]), choices=["Classical", "New"], case_sensitive=False, console=self.cons).lower().strip())
    
    # --- State/Stats ---
    def show_leader(self, leader):
        """The leader variable will either contain the string 'user', 'cpu', or 'even' for the GAME_TEXT dictionary lookup."""
        self.cons.print(GAME_TEXT[leader], style=self.styles["main"])

    def show_cpu_move(self, cpu_move):
        self.cons.print(f"Computer Chose --> {cpu_move}", style=self.styles["main"])
    
    def round_state(self, number, user_score, cpu_score):
        self.cons.print(f"|Round {number}| Score -> You: {user_score} | CPU: {cpu_score}", style=self.styles["base"])

    def stats(self, matches_played, matches_won, matches_lost, rounds_won, best_move, pct):
        self.cons.print(f"Games Played -> {matches_played}\nGames Won -> {matches_won}\nGames Lost -> {matches_lost}\nRounds Won -> {rounds_won}\nBest Move -> {pct}% of rounds won used {best_move}")
