import random

class CounterAI:
    def choose_move(self, context):
        rules = context["rules"]
        data = context['data']
        if not data:
            return random.choice(list(rules.keys()))
        
        player_move = data[-1]  
        counter_moves = [val[0] for val in context['rules'].items() if player_move in val[1]]
        return random.choice(counter_moves)
        