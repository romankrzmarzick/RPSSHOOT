import random
from collections import Counter

CLASSICAL_MODE = ["rock", "paper", "scissors"]
NEW_MODE = ["rock", "paper", "scissors", "lizard", "spock"]

WINNING_MOVES = {
    "rock": {"scissors", "lizard"},
    "paper": {"rock", "spock"},
    "scissors": {"paper", "lizard"},
    "lizard": {"spock", "paper"},
    "spock": {"rock", "scissors"},
}


class Game:
    def __init__(self):
        self.user_score = 0
        self.cpu_score = 0
        self.total_matches = 0
        self.total_wins = 0 
        self.winning_moves = []
        self.best_move = ""
        self.game_moves = []
        self.rounds_played = 0
    def define_game_moves(self, answer):
        if answer == "classical":
            self.game_moves = CLASSICAL_MODE
        else: 
            self.game_moves = NEW_MODE
    
    def add_round(self):
        self.rounds_played += 1

    def win_match(self):
       self.total_wins += 1

    def matches_played(self):
       self.total_matches += 1

    def add_best_moves(self, outcome, move):
        if outcome == "win":
            self.winning_moves.append(move)

    def find_best_move(self):
        most_common = Counter(self.winning_moves).most_common(1)
        self.best_move = most_common[0][0] if most_common else None

    def best_move_win_pct(self):
        return round((len([x for x in self.winning_moves if self.best_move in x]) / (self.rounds_played)) * 100, 2)

    def cpu_pick(self):
        return random.choice(self.game_moves)

    def round_outcome(self, user_move, cpu_move):
        if user_move == cpu_move:
            return "tie"
        return "win" if cpu_move in WINNING_MOVES[user_move] else "lose"

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
    