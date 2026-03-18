from scripts.game_rules import Game
from scripts.ui import Interface
from scripts.player import Player
from scripts.player import Robot
from scripts.data import Data
from ai_modules.random_ai import RandomAI
from ai_modules.common_ai import CommonAI
from ai_modules.counter_ai import CounterAI
from ai_modules.markov_ai import MarkovChain
import sys

def play_round(context, game, ui, player, robot, data):
    while True:
        user_move = ui.choose_move(game.game_mode)
        if user_move != "question":
            break
        ui.game_guide()
        
    if user_move == "quit":
        sys.exit()
    # Uses context to access player data and the game mode to pick a desired move with the connected AI module. 
    cpu_move = robot.robot_move(context)

    # Decides who wins the current round.
    outcome = game.round_outcome(user_move, cpu_move)
    
    # adds rounds results to the data module.
    data.record_round(user_move, outcome)
    data.add_move(user_move) 
    
    if outcome == "win":
        player.addpoint()
    elif outcome == "lose":
        robot.addpoint()

    # Displays who won the the round and reveals the robot's move.
    ui.show_round_result(outcome)
    ui.show_cpu_move(cpu_move)

def finialize_result(game, player, robot, data, ui):
    winner = game.decide_winner(player.score, robot.score)
    if winner == "user":
        ui.victory()
        data.add_match_win()
    else:
        ui.defeat()


def run():
    game = Game()
    ui = Interface()
    data = Data()
   
    ai_models = {
        "random" : RandomAI,
        "common" : CommonAI,
        "counter" : CounterAI,
        "markov" : MarkovChain
    }
    
    robot = Robot(ai_models[ui.choose_ai()]())
    player = Player(ui.choose_name())

    ui.welcome_message()
    game_version = ui.choose_mode()
    chosen_rounds = ui.choose_rounds()
    game.change_mode(game_version)
    
    while True:
        context = {
            "rules" : game.game_mode,
            "data" : data.user_move_history,
            "user_score" : player.score,
            "cpu_score" : robot.score
        }

        for current_round in range(1, (chosen_rounds + 1)):
            if abs(player.score - robot.score) > ((chosen_rounds + 1) - current_round):
                break
            ui.round_state(current_round, player.score, robot.score)
            
            play_round(context, game, ui, player, robot, data)

        if not game.scores_tied(player.score, robot.score):
           finialize_result(game, player, robot, data, ui)
        else:
            ui.display_tiebreaker()
            first_round = True
            
            while abs(player.score - robot.score) < 2:
                if not first_round: ui.show_leader(game.find_leader(player.score, robot.score))

                play_round(context, game, ui, player, robot, data)
                first_round = False

            finialize_result(game, player, robot, data, ui)
        
        # adds match to the data module. 
        data.add_match()
       
        if not ui.choose_replay():
            ui.show_stats(**data.stat_summary())
            ui.end_message(player.name)
            break
       
        # Resets both scores before intializing a new match to ensure fairness.
        player.reset_score()
        robot.reset_score()


run()