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
    "end_msg": "THANKS FOR PLAYING! [Total Matches Played]:",
    "victory": "YOU WON THE MATCH!",
    "defeat": "THE COMPUTER DEFEATED YOU!",
    "tiebreaker": "TIEBREAKER MATCH!",
    "win": "Round Won!",
    "lose": "Round Lost!",
    "tie": "Round Tied!",
    "move": "What will your move be?",
    "repeat": "Play Again?",
    "even": "EVEN STEVEN!",
    "cpu_leads": "THE COMPUTER IS BEATING YOU!",
    "user_leads": "ONE MORE WIN AWAY FROM VICTORY!",
}


class UI:
    def __init__(self):
        self.console = Console()
        self.styles = {
            "win": "bold green",
            "lose": "bold red",
            "tie": "yellow blink",
            "base": "white",
            "heading": "dim bold",
        }

    def welcome_message(self):
        self.console.print(GAME_TEXT["welcome_msg"], style=self.styles["heading"])

    def user_choice(self, moves):
        return (
            Prompt.ask(
                Text(GAME_TEXT["move"], style=self.styles["base"]),
                choices=moves,
                case_sensitive=False,
                console=self.console,
            )
            .lower()
            .strip()
        )

    def round_message(self, number):
        self.console.print(f"| Round {number} |", style=self.styles["heading"])

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
        self.console.print(GAME_TEXT["tiebreaker"], style=self.styles["heading"])

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
            style=self.styles["heading"],
        )
