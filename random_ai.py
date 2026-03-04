import random

class RandomAI:
    def choose_move(self, context):
        rules = context["rules"]
        return random.choice(list(rules.keys()))
        


    

        
