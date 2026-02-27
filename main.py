from logic import Game
from ui import UI
from computer import ai
import data

def run():
    game = Game()
    ui = UI()
    ui.welcome_message()
    while True:
        selected_rounds = ui.amount_of_games()
        game_version = ui.classic_or_new()
        game.define_game_moves(game_version)


        for round_number in range(1, selected_rounds + 1):
            if game.user_score > (selected_rounds / 2) or game.cpu_score > (selected_rounds / 2):
                break

            ui.round_message(round_number, game.user_score, game.cpu_score)
            while True:
                user_move = ui.user_choice(game.game_moves)
                if user_move == "?":
                    ui.game_guide()
                else: 
                    break
            if user_move == "q":
                break
            cpu_move = game.cpu_pick()

            outcome = game.round_outcome(user_move, cpu_move)
            
            data.store_move(user_move, outcome) 
            
            game.apply_result(outcome)
            ui.display_result(outcome)
            
            ui.show_cpu_move(cpu_move)
            
            game.add_round()
        if user_move == "q":
            break

        if not game.scores_tied():
            if game.user_won():
                ui.victory()
                game.win_match()
            else:
                ui.defeat()
        else:
            ui.tiebreaker_heading()
            first_round = True

            while game.tiebreaker_active():
                if not first_round:
                    ui.show_leader(game.find_leader())

                cpu_move = game.cpu_pick()
                user_move = ui.user_choice(game.game_moves)

                outcome = game.round_outcome(user_move, cpu_move)
                game.apply_result(outcome)
                ui.display_result(outcome)

                first_round = False

            if game.user_won():
                ui.victory()
                game.win_match()
            else:
                ui.defeat()

        game.matches_played()
       

        if not ui.play_again():
            game.find_best_move()
            ui.end_message(game.total_matches, game.total_wins, game.best_move, game.best_move_win_pct())
            break
            
        game.cpu_score = 0
        game.user_score = 0


run()