CLASSICAL = {
    "rock": "scissors", 
    "paper" :"scissors",
    "scissors" : "paper"
    }

RPSLS = {
    "rock": {"scissors", "lizard"},
    "paper": {"rock", "spock"},
    "scissors": {"paper", "lizard"},
    "lizard": {"spock", "paper"},
    "spock": {"rock", "scissors"},
}

MODES = {
    "classical" : CLASSICAL,
    "new" :  RPSLS
}


class Game:
    def __init__(self):
        self.game_mode = MODES["new"]
        self.rounds = 3

    def change_mode(self, mode):
        self.game_mode = MODES[mode]

    def change_rounds(self, num):
        self.rounds = num

    def round_outcome(self, user_move, cpu_move):
        if user_move == cpu_move:
            return "tie"
        return "win" if cpu_move in self.game_mode else "lose"

    def scores_tied(self, user_score, cpu_score):
        return user_score == cpu_score

    def tiebreaker_active(self, user_score, cpu_score):
        return abs(user_score - cpu_score) < 2

    def decide_winner(self, user_score, cpu_score):
        return "user" if user_score > cpu_score else "cpu"
   