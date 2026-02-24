from logic import Game, GAME_MOVES
from ui import UI


def run():
    ui = UI()
    ui.welcome_message()

    while True:
        selected_rounds = ui.amount_of_games()
        # ui.classic_or_new()
        game = Game()

        for round_number in range(1, selected_rounds + 1):
            if game.user_score > (selected_rounds / 2) or game.cpu_score > (selected_rounds / 2):
                break

            ui.round_message(round_number, game.user_score, game.cpu_score)

            cpu_move = game.cpu_pick()
            user_move = ui.user_choice(GAME_MOVES)

            outcome = game.round_outcome(user_move, cpu_move)
            game.apply_result(outcome)
            ui.display_result(outcome)
            ui.show_cpu_move(cpu_move)

        if not game.scores_tied():
            if game.user_won():
                ui.victory()
            else:
                ui.defeat()
        else:
            ui.tiebreaker_heading()
            first_round = True

            while game.tiebreaker_active():
                if not first_round:
                    ui.show_leader(game.find_leader())

                cpu_move = game.cpu_pick()
                user_move = ui.user_choice(GAME_MOVES)

                outcome = game.round_outcome(user_move, cpu_move)
                game.apply_result(outcome)
                ui.display_result(outcome)

                first_round = False

            if game.user_won():
                ui.victory()
            else:
                ui.defeat()

        if not ui.play_again():
            ui.end_message(Game.total_matches)
            break


run()