from game_rules import Game
from ui import Interface
from player import Player
from player import Robot
from data import Data
import sys

def run():
    game = Game()
    ui = Interface()
    p1 = Player()
    robot = Robot()
    data = Data()

    ui.welcome_message()
    
    selected_rounds = ui.choose_rounds()
    game_version = ui.choose_mode()
    game.change_mode(game_version)
    game.change_rounds(selected_rounds)
    
    while True:
        for current_round in range(1, (selected_rounds + 1)):
            if abs(p1.score - robot.score) > ((selected_rounds + 1) - current_round):
                break

            ui.round_state(current_round, p1.score, robot.score)

            while True:
                user_move = ui.choose_move(game.game_mode)
                if user_move != "?":
                    break
                ui.game_guide()
                
            if user_move == "q":
                sys.exit()
            
            # Computer Chooses its move.       
            cpu_move = robot.robot_move(game.game_mode)

            # Decides who wins the current round.
            outcome = game.round_outcome(user_move, cpu_move)
            
            # Data Functions
            data.record_round(user_move, outcome) 
            data.add_round()
            
            if outcome == "win":
                p1.addpoint()
            elif outcome == "lose":
                robot.addpoint()

            # Displays who won the the round and reveals the robot's move.
            ui.show_round_result(outcome)
            ui.show_cpu_move(cpu_move)


        if not game.scores_tied(p1.score, robot.score):
            winner = game.decide_winner(p1.score, robot.score)
            if winner == "user":
                ui.victory()
                data.add_match_win()
            else:
                ui.defeat()
        else:
            ui.tiebreaker_heading()
            
            first_round = True

            while game.tiebreaker_active(p1.score, robot.score):
                if not first_round:
                    ui.show_leader(data.find_leader(p1.score, robot.score))

                cpu_move = robot.robot_move(game.game_mode)
                user_move = ui.choose_move(game.game_mode)

                outcome = game.round_outcome(user_move, cpu_move)
                
                if outcome == "win":
                    p1.addpoint()
                elif outcome == "lose":
                    robot.addpoint()
                
                ui.show_round_result(outcome)

                first_round = False

            winner = game.decide_winner(p1.score, robot.score)
            if winner == "user":
                ui.victory()
                data.add_match_win()
            else:
                ui.defeat()

        data.add_match()
       

        if not ui.choose_replay():
            best_move = data.find_best_move()
            ui.stats(data.matches_played, data.matches_won, data.find_games_lost(), best_move, data.best_move_win_pct(best_move))
            ui.end_message(p1.name)
            break
            
        p1.reset_score()
        robot.reset_score()


run()