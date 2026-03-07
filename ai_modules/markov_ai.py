import random

class MarkovChain: 
    
    def __init__(self):
        self.transitions = {}
    
    def figure_markov(self, rules): 
        for i in rules:
            self.transitions[i] = {}
            for val in rules:
                self.transitions[i][val] = 1
    
    def add_pair(self, data):
        if len(data) >= 2:
            prev_move, curr_move = data[-2:]
            self.transitions[prev_move][curr_move] += 1
            return curr_move
        elif len(data) >= 1:
            return data[-1]
    
    def weighted_random(self, move):
        curr_move = move if move else "rock"
        possibilites = list(self.transitions[curr_move].keys())
        weights = list(self.transitions[curr_move].values())
        return random.choices(possibilites, weights)[0]

    def counter_move(self, predicted_move, game_rules):
        counter_moves = [val[0] for val in game_rules.items() if predicted_move in val[1]]
        return random.choice(counter_moves)

    def choose_move(self, context):
        rules = context["rules"]
        data = context["data"]
        if not self.transitions:
            self.figure_markov(rules)
        current_move = self.add_pair(data)
        return self.counter_move(self.weighted_random(current_move), rules)
        