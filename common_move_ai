import random
from collections import Counter

class CommonAI:   

    def choose_move(self, context):
        rules = context["rules"]
        data = context['data']
        if not data:
            return random.choice(list(rules.keys()))
        
        common_move = Counter(data).most_common(1)[0][0]
        counter_moves = []
        for move in rules[common_move]:
            counter_moves.append(move)
            return random.choice()
        