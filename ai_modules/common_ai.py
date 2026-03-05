import random
from collections import Counter

class CommonAI:   

    def choose_move(self, context):
        rules = context["rules"]
        data = context['data']
        if not data:
            return random.choice(list(rules.keys()))
        
        common_move = Counter(data).most_common(1)[0][0]
        counter_moves = [val[0] for val in context['rules'].items() if common_move in val[1]]
        print(counter_moves)
        return random.choice(counter_moves)
        