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

    def apply_score(self, val):
        if val == 1:
           self.user_score += 1
        elif val == -1:
            self.cpu_score += 1
    
    def cpu_pick(self):
        return random.choice(GAME_MOVES)

    def combination(self, user_move, cpu_move):
        win_conditions = {
            "rock" : {"scissors","lizard"},
            "paper" : {"rock", "spock"},
            "scissors" : {"paper", "lizard"},
            "lizard" : {"spock", "paper"},
            "spock" : {"rock", "scissors"}
        }
        
        if user_move == cpu_move: return "tie"
        return "won" if cpu_move in win_conditions[user_move] else "lost"
    
    def isnot_tie(self):
        return self.user_score != self.cpu_score
    
    def user_won(self):
       return self.user_score > self.cpu_score 

    def tiebreaker(self):
        return abs(self.user_score - self.cpu_score) < 2
    
    def result(self, val):
        if val == "won":
            self.apply_score(1)
            return "win" 
        elif val == "lost":
            self.apply_score(-1)
            return "lose"
        else:
            return "tie"
    def find_position(self):
        if abs(self.user_score - self.cpu_score) == 0: return None
        return self.user_score > self.cpu_score 
    
    