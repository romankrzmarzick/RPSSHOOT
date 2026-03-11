from scripts.game_rules import Game
from scripts.data import Data
import pytest
from unittest.mock import patch
from scripts.ui import Interface

@pytest.fixture
def classical_game():
    game = Game()
    game.change_mode("classical")
    return game


def test_classical_tie(classical_game):
    outcome = classical_game.round_outcome("rock", "rock")

    assert outcome == "tie"


def test_classical_edge_case(classical_game):
    outcome = classical_game.round_outcome("sc", "rock")

    assert outcome == "lose"

def test_classic_win_record(classical_game):
    data = Data()

    outcome = classical_game.round_outcome("rock", "scissors")

    data.record_round("rock", outcome)

    assert outcome == "win"
    assert len(data.round_history["win"]) == 1
    assert type(data.round_history["win"][0]) == str

@patch("scripts.ui.Prompt.ask")
def test_choose_rounds_int(mock_ask):
    mock_ask.return_value = "5"
    ui = Interface()
    result = ui.choose_rounds()

    assert result == 5
    assert type(result) == int

@patch("scripts.ui.Prompt.ask")
def test_choose_moves(mock_ask):
    mock_ask.side_effect = ["bad_input", "?"]
    ui = Interface()
    game = Game()
    game.change_mode("classical")
    result = ui.choose_move(game.game_mode)

    assert type(result) == str
    assert result == "?"

def test_round_outcome_edge_case_computer(classical_game):
    outcome = classical_game.round_outcome("scissors", "ro")
    
    assert outcome == "lose"