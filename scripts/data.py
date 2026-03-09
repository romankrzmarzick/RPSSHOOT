from collections import Counter

class Data:
    def __init__(self):
        self.matches_played = 0
        self.matches_won = 0
        self.user_move_history = []
        self.round_history = {
            "win" : [],
            "tie" : [],
            "lose" : []
        }

    def add_move(self, user_move):
        self.user_move_history.append(user_move)

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
        
    def find_matches_lost(self):
        return (self.matches_played - self.matches_won)
    
    def find_rounds_won(self):
        return len(self.round_history['win'])

    def best_move(self):
        result = Counter(self.round_history["win"]).most_common(1)
        return result[0][0] if result else None
      
    def best_move_pct(self, best_move):
        winning_moves = self.round_history['win']
        
        if not best_move or not winning_moves:
            return 0.0
        
        best_move_count = winning_moves.count(best_move)

        raw_pct = best_move_count / len(winning_moves)
        return round((raw_pct * 100), 2)

    def worst_move(self):
        result = Counter(self.round_history["lose"]).most_common(1)
        return result[0][0] if result else None
    
    def worst_move_pct(self, worst_move):
        losing_moves = self.round_history['lose']

        if not worst_move or not losing_moves: 
            return 0.0

        worst_move_count = losing_moves.count(worst_move)

        raw_pct = worst_move_count / len(losing_moves)
        return round((raw_pct * 100), 2)
    
    def stat_summary(self):
        summary = {
            "matches_played" : self.matches_played, 
            "matches_won" : self.matches_won,
            "matches_lost" : self.find_matches_lost(), 
            "rounds_won" : self.find_rounds_won(),
            "best_move" : self.best_move(),
            "best_pct" : self.best_move_pct(self.best_move()),
            "worst_move" : self.worst_move(),
            "worst_pct" : self.worst_move_pct(self.worst_move())
        }
        return summary


       
