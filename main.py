from logic import Game
from ui import UI
from logic import GAME_MOVES

def run():
    ui = UI()
    ui.welcome_message()
    while True:
        game = Game()
        for i in range(1, 4):
            if game.user_score == 2 or game.cpu_score == 2:
                break
            
            ui.round_message(i)

            cpu_move = game.cpu_pick()
            user_move = ui.user_choice(GAME_MOVES)
            outcome = game.combination(user_move, cpu_move)
            
            ui.display_moves(user_move, cpu_move)

            result = game.result(outcome)
            ui.display_result(result)

        if game.isnot_tie():
            if game.user_won():
                ui.victory()
            else:
                ui.defeat()
        else:
            ui.tiebreaker_heading()
            not_first_round = False

            while game.tiebreaker():
                if not_first_round: 
                    boolean = game.find_position()
                    ui.show_position(boolean)
                cpu_move = game.cpu_pick()
                user_move = ui.user_choice(GAME_MOVES)
                tie_rounds = game.combination(user_move, cpu_move)
                
                ui.display_moves(user_move, cpu_move)

                result = game.result(tie_rounds)
                ui.display_result(result)
                not_first_round = True

            if game.user_won():
                ui.victory()
            else:
                ui.defeat()

        if not ui.play_again():
            ui.end_message(Game.total_matches)
            break

run()
