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
        cpu_move = cpu_move.lower().strip()
        user_move = user_move.lower().strip()

        if user_move == cpu_move: return None
        return True if cpu_move in win_conditions[user_move] else False
    
    def isnot_tie(self):
        return self.user_score != self.cpu_score
    
    def who_won(self):
       print("\nYOU WON THE MATCH!\n") if self.user_score > self.cpu_score else print("\nTHE COMPUTER DEFEATED YOU!\n")

    def tiebreaker(self):
        return True if abs(self.user_score - self.cpu_score) < 2 else False 
    
    def result(self, val):
        if val is True:
            print("Round Won!")
            self.apply_score(1)
        elif val is False:
            print("Round Lost!")
            self.apply_score(-1)
        else:
            print("Round Tied!")

    def find_position(self):
        if abs(self.user_score - self.cpu_score) == 0: return None
        return True if self.user_score > self.cpu_score else False
    
GAME_TEXT = {
    "welcome_msg" : "Welcome to RPSS! Each match is best of three — win 2 rounds to win the match. |TWIST|: If the match ends in a tie, the winner must have two more wins than losses.",
    "end_msg" : "THANKS FOR PLAYING! [Total Matches Played]:",
    "move" : "What will your move be?",
    "victory" : "YOU WON THE MATCH!",
    "tiebreaker" : "TIEBREAKER MATCH!",
    "defeat" : "THE COMPUTER DEFEATED YOU!",
    "won" : "Round Won!",
    "tie" : "Round Lost!",
    "lost" : "Round Tied!",
    "repeat" : "Play Again?"
}
