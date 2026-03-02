from collections import Counter

class Data:
    def __init__(self):
        self.matches_played = 0
        self.rounds_played = 0
        self.matches_won = 0
        self.round_history = {
            "win" : [],
            "tie" : [],
            "lose" : []
        }

    def add_round(self):
        self.rounds_played += 1

    def add_match_win(self):
        self.matches_won += 1

    def add_match(self):
        self.matches_played += 1

    def record_round(self, move, outcome):
        self.round_history[outcome].append(move)

    # --- Specific Stats ---
    def find_leader(self, user_score, cpu_score):
            if user_score == cpu_score:
                return "even" 
            return "user" if user_score > cpu_score else "cpu"
        
    def find_best_move(self):
        best_move = Counter(self.round_history["win"]).most_common(1)
        return best_move[0][0] if best_move else None
        
    def best_move_win_pct(self, best_move):
        
        raw_pct = len([x for x in self.round_history['win'] if best_move in x]) / (self.rounds_played)
        return round((raw_pct * 100), 2)

    def find_games_lost(self):
        return (self.matches_played - self.matches_won)