import random

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

    def cpu_pick(self):
        return random.choice(GAME_MOVES)

    def round_outcome(self, user_move, cpu_move):
        win_conditions = {
            "rock": {"scissors", "lizard"},
            "paper": {"rock", "spock"},
            "scissors": {"paper", "lizard"},
            "lizard": {"spock", "paper"},
            "spock": {"rock", "scissors"},
        }

        if user_move == cpu_move:
            return "tie"

        return "win" if cpu_move in win_conditions[user_move] else "lose"

    def apply_result(self, outcome):
        if outcome == "win":
            self.user_score += 1
        elif outcome == "lose":
            self.cpu_score += 1

    def scores_tied(self):
        return self.user_score == self.cpu_score

    def user_won(self):
        return self.user_score > self.cpu_score

    def tiebreaker_active(self):
        return abs(self.user_score - self.cpu_score) < 2

    def find_leader(self):
        if self.user_score == self.cpu_score:
            return None
        return self.user_score > self.cpu_score