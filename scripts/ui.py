from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.text import Text


GAME_TEXT = {
    # --- infomational ---
    "welcome_msg" : ("""\
Welcome to RPSS!

Each match is played as a best-of-three series, meaning the first player to win
two rounds wins the match.

| TWIST |
If the match ends in a tie, a tiebreaker begins. During the tiebreaker, the
winner must have two more wins than losses to claim victory.
"""
),
    "game_rules" : ("""\
|Game Rules|
Play the selected number of rounds. Best score wins.
If tied, a tiebreaker starts: win two rounds before a loss.
Ties don't count. Example: Win-Tie-Win = Match won.
Modes: Classic RPS or RPS with Lizard & Spock.
Moves -> rock(ro), paper(pa), scissors(sc), lizard(li), spock(sp)
"""
    ),
    "end_msg" : "Thanks for playing and have a splendid day",

    # --- Match Decisions ---
    "victory" : "YOU WON THE MATCH!",
    "defeat" : "THE COMPUTER DEFEATED YOU!",
    "tiebreaker" : "TIEBREAKER MATCH!",
   
    # --- Round Decisions --- 
    "win" : "Round Won!",
    "lose" : "Round Lost!",
    "tie" : "Round Tied!",
    
    # --- Inputs ---
    "input": "|Exit[q]| |Rules[?]| | What will be your move? |",
    "replay": "Play Again?",
    "game_mode" : "Game Mode Selection",
    "games" : "How many rounds?",
    "name" : "How should we call you?",
    "ai" : "Choose the ai you want to face",

    # --- Tiebreaker Round ---
    "even" : "EVEN STEVEN!",
    "cpu" : "THE COMPUTER IS BEATING YOU!",
    "user" : "ONE MORE WIN AWAY FROM VICTORY!",
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

    def end_message(self, name: str):
        self.cons.print(f"\n{GAME_TEXT['end_msg']} {name}!", style=self.styles["base"])
    
    # --- Round Decisons ---
    def show_round_result(self, outcome: str):
        """The outcome variable will either contain the string 'win', 'lose', or 'tie' for the GAME_TEXT dictionary lookup."""
        self.cons.print(GAME_TEXT[outcome], style=self.styles[outcome])

    # --- Match Decisions
    def display_tiebreaker(self):
        self.cons.print(GAME_TEXT["tiebreaker"], style=self.styles["main"])

    def victory(self):
        self.cons.print(GAME_TEXT["victory"], style=self.styles["win"])

    def defeat(self):
        self.cons.print(GAME_TEXT["defeat"], style=self.styles["lose"])

    # --- User Inputs ---
    def choose_replay(self):
        return Confirm.ask(Text(GAME_TEXT["replay"], style=self.styles["main"]), console=self.cons)

    def choose_move(self, moves):
        possibilities = {
           "quit" : ["quit", "q"],
           "question" : ["question", "?"],
        }
        possibilities.update({val : [val, val[:2]] for val in moves})
        
        selection = [item for sublist in possibilities.values() for item in sublist]
        output = Prompt.ask(Text(GAME_TEXT['input'], style=self.styles["main"]), show_choices=False, case_sensitive=False, choices=selection, console=self.cons).lower().strip()
        return next((key for key, value_list in possibilities.items() if output in value_list), "?")

    def choose_name(self) -> str:
        while True:
            name = Prompt.ask(Text(GAME_TEXT["name"], style=self.styles["main"])).lower().title()
            
            if 0 < len(name) <= 21:
                break
            elif not len(name):
                self.cons.print("Name is Empty: enter a valid one please.", style=self.styles["lose"])
            else:
                self.cons.print("Name is over 20 Characters: enter a new one please.", style=self.styles["lose"])
        
        return name
    
    def choose_ai(self) -> str:
        return (Prompt.ask(Text(GAME_TEXT["ai"], style=self.styles["main"]), case_sensitive=False, choices=["random", "common", "counter", "markov"], console=self.cons).lower().strip())

    def choose_rounds(self) -> int:
        return int(Prompt.ask(Text(GAME_TEXT["games"], style=self.styles["base"]), choices=["3", "5", "7"], console=self.cons).lower().strip())

    def choose_mode(self) -> str:
        return (Prompt.ask(Text(GAME_TEXT["game_mode"], style=self.styles["base"]), choices=["Classical", "New"], case_sensitive=False, console=self.cons).lower().strip())
    
    # --- State/Stats ---
    def show_leader(self, leader: str):
        """The leader variable will either contain the string 'user', 'cpu', or 'even' for the GAME_TEXT dictionary lookup."""
        self.cons.print(GAME_TEXT[leader], style=self.styles["main"])

    def show_cpu_move(self, cpu_move: str):
        self.cons.print(f"Computer Chose --> {cpu_move}", style=self.styles["main"])
    
    def round_state(self, number: int, user_score: int, cpu_score: int):
        self.cons.print(f"|Round {number}| You: {user_score} | CPU: {cpu_score}", style=self.styles["base"])

    def show_stats(self, matches_played: int, matches_won: int, matches_lost: int, rounds_won: int, best_move: str, best_pct: float, worst_move: str, worst_pct: float):
        self.cons.print(f"\n+----------------------------------------+\nGames Played -> {matches_played}\nGames Won -> {matches_won}\nGames Lost -> {matches_lost}\nRounds Won -> {rounds_won}\nBest Move -> {best_pct}% of rounds won used {best_move}\nWorst Move -> {worst_pct}% of rounds lost used {worst_move}\n+----------------------------------------+")
