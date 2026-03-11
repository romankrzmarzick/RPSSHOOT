CLASSICAL = {
    "rock": {"scissors"}, 
    "paper" : {"rock"},
    "scissors" : {"paper"}
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

    def change_mode(self, mode):
        self.game_mode = MODES[mode]

    def round_outcome(self, user_move: str, cpu_move: str) -> str:
        if user_move == cpu_move:
            return "tie"
        return "win" if cpu_move in self.game_mode.get(user_move, "lose") else "lose"
    
    @staticmethod
    def scores_tied(user_score: int, cpu_score: int) -> bool:
        return user_score == cpu_score

    @staticmethod
    def decide_winner(user_score: int, cpu_score: int) -> str:
        return "user" if user_score > cpu_score else "cpu"
    
    @staticmethod
    def find_leader(user_score: int, cpu_score: int):
            if user_score == cpu_score:
                return "even" 
            return "user" if user_score > cpu_score else "cpu"
        