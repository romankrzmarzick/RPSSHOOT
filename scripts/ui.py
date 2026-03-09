from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.text import Text


GAME_TEXT = {
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
    "invalid" : "[Invalid answer: Enter a valid input]",

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
        easy_type = [(val, val[:2]) for val in moves] 
        easy_type.extend([("quit", "q"), ("question", "?")])
        while True:
            choice = Prompt.ask(Text(f"{GAME_TEXT['input']}", style=self.styles["main"])).lower().strip()
            for i in easy_type:
                if choice in i:
                    return i[0]
            self.cons.print(GAME_TEXT['invalid'], style=self.styles["lose"])
    
    def choose_name(self):
        while True:
            name = Prompt.ask(Text(GAME_TEXT["name"], style=self.styles["main"])).lower().strip()
            if len(name) <= 20:
                break
        return name
    
    def choose_ai(self):
        return (Prompt.ask(Text(GAME_TEXT["ai"], style=self.styles["main"]), choices=["random", "common", "counter", "markov"], console=self.cons).lower().strip())

    def choose_rounds(self):
        return int(Prompt.ask(Text(GAME_TEXT["games"], style=self.styles["base"]), choices=["3", "5", "7"], console=self.cons).lower().strip())

    def choose_mode(self):
        return (Prompt.ask(Text(GAME_TEXT["game_mode"], style=self.styles["base"]), choices=["Classical", "New"], case_sensitive=False, console=self.cons).lower().strip())
    
    # --- State/Stats ---
    def show_leader(self, leader):
        """The leader variable will either contain the string 'user', 'cpu', or 'even' for the GAME_TEXT dictionary lookup."""
        self.cons.print(GAME_TEXT[leader], style=self.styles["main"])

    def show_cpu_move(self, cpu_move):
        self.cons.print(f"Computer Chose --> {cpu_move}", style=self.styles["main"])
    
    def round_state(self, number, user_score, cpu_score):
        self.cons.print(f"|Round {number}| You: {user_score} | CPU: {cpu_score}", style=self.styles["base"])

    def stat_summary(self, matches_played, matches_won, matches_lost, rounds_won, best_move, best_pct, worst_move, worst_pct):
        self.cons.print(f"\nGames Played -> {matches_played}\nGames Won -> {matches_won}\nGames Lost -> {matches_lost}\nRounds Won -> {rounds_won}\nBest Move -> {best_pct}% of rounds won used {best_move}\nWorst Move -> {worst_pct}% of rounds lost used {worst_move}")
