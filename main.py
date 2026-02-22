from logic import Game
from ui import UI
from ui import GAME_TEXT

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
            user_move = ui.user_choice()
            outcome = game.combination(user_move, cpu_move)
            
            ui.display_moves(user_move, cpu_move)

            game.result(outcome)

        if game.isnot_tie():
            game.who_won()
        else:
            
            print(GAME_TEXT["tiebreaker"])
            not_first_round = False

            while game.tiebreaker():
                if not_first_round: 
                    boolean = game.find_position()
                    ui.show_position(boolean)
                cpu_move = game.cpu_pick()
                user_move = ui.user_choice()
                tie_rounds = game.combination(user_move, cpu_move)
                
                ui.display_moves(user_move, cpu_move)

                game.result(tie_rounds)
                
                not_first_round = True

            game.who_won()
            
        if not ui.play_again():
            ui.end_message()
            break

run()
