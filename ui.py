from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.text import Text

# |Exit[q]| |Rules[?]| 
GAME_TEXT = {
    "welcome_msg": (
        "Welcome to RPSS! Each match is best of three — "
        "win 2 rounds to win the match. "
        "|TWIST|: If the match ends in a tie, the winner must "
        "have two more wins than losses."
    ),
    "what_game" : "[Game Selection]",
    "games" : "|What do you want the match to be best out of?|",
    "end_msg": "THANKS FOR PLAYING! [Total Matches Played]:",
    "victory": "YOU WON THE MATCH!",
    "defeat": "THE COMPUTER DEFEATED YOU!",
    "tiebreaker": "TIEBREAKER MATCH!",
    "win": "Round Won!",
    "lose": "Round Lost!",
    "tie": "Round Tied!",
    "input": "| What will be your move? |",
    "repeat": "Play Again?",
    "even": "EVEN STEVEN!",
    "cpu_leads": "THE COMPUTER IS BEATING YOU!",
    "user_leads": "ONE MORE WIN AWAY FROM VICTORY!",
    "game_rules" : (
        "|Games Rules|\nThe user plays the amount of gamess selected, the first to get the best score from the rounds wins."
        "If scores are still tied, a tiebreaker game commences. In the tiebreaker, the winner must win two times before a loss."
        "Meaning back to back wins isn't required. A tie is meaningless. Example: Win-Tie-Win = Match Won"
        "User can also choose between a classical game or RPS with Spock and Lizard (search online for the rules if needed)."
    )
}


class UI:
    def __init__(self):
        self.console = Console()
        self.styles = {
            "win": "bold green",
            "lose": "bold red",
            "tie": "yellow blink",
            "base": "white",
            "info": "dim bold",
            "subheading": "white bold"
        }   

    def welcome_message(self):
        self.console.print(GAME_TEXT["welcome_msg"], style=self.styles["info"])

    def user_choice(self, moves):
        return (
            Prompt.ask(
                Text(GAME_TEXT["input"], style=self.styles["base"]),
                choices=moves,
                case_sensitive=False,
                console=self.console,
            )
            .lower()
            .strip()
        )

    def show_cpu_move(self, cpu_move):
        self.console.print(f"Computer Chose --> {cpu_move}", style=self.styles["subheading"])
    def round_message(self, number, user_score, cpu_score):
        self.console.print(f"|Round {number}| Score -> You: {user_score} | CPU: {cpu_score}", style=self.styles["subheading"])

    def display_result(self, outcome):
        self.console.print(
            GAME_TEXT[outcome],
            style=self.styles[outcome],
        )

    def show_leader(self, leader):
        if leader is True:
            self.console.print(GAME_TEXT["user_leads"], style=self.styles["win"])
        elif leader is False:
            self.console.print(GAME_TEXT["cpu_leads"], style=self.styles["lose"])
        else:
            self.console.print(GAME_TEXT["even"], style=self.styles["tie"])

    def tiebreaker_heading(self):
        self.console.print(GAME_TEXT["tiebreaker"], style=self.styles["subheading"])

    def victory(self):
        self.console.print(GAME_TEXT["victory"], style=self.styles["win"])

    def defeat(self):
        self.console.print(GAME_TEXT["defeat"], style=self.styles["lose"])

    def play_again(self):
        return Confirm.ask(
            Text(GAME_TEXT["repeat"], style=self.styles["base"]),
            console=self.console,
        )

    def end_message(self, matches):
        self.console.print(
            f"{GAME_TEXT['end_msg']} {matches}",
            style=self.styles["subheading"],
        )

    def game_guide(self):
        self.console.print(GAME_TEXT[""], style=self.styles["info"])

    def amount_of_games(self):
        return int(
            Prompt.ask(
                Text(GAME_TEXT["games"], style=self.styles["base"]),
                choices=["3", "5", "7"],
                console=self.console,
            )
            .lower()
            .strip()
        )

    def classic_or_new(self):
        return (
            Prompt.ask(
                Text(GAME_TEXT["what_games"], style=self.styles["base"]),
                choices=["Classical", "New"],
                case_sensitive=False,
                console=self.console,
            )
            .lower()
            .strip()
        )
