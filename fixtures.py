import pytest
from Piece import Knight
from enums import Player
from chess_engine import game_state  # Import your game_state class



@pytest.fixture
def game_state_empty():
    gs = game_state()
    # Overwrite the board with a blank 8x8 matrix
    gs.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    return gs

@pytest.fixture
def game_state_center():
    gs = game_state()
    # Overwrite the board with a blank 8x8 matrix
    gs.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight('n', 4, 4, Player.PLAYER_1)
    gs.board[4][4] = knight

    return gs

@pytest.fixture
def game_state_edge():
    gs = game_state()
    # Overwrite the board with a blank 8x8 matrix
    gs.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight('n', 0, 4, Player.PLAYER_1)
    gs.board[0][4] = knight

    return gs

@pytest.fixture
def game_state_corner():
    gs = game_state()
    # Overwrite the board with a blank 8x8 matrix
    gs.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight('n', 0, 0, Player.PLAYER_1)
    gs.board[0][0] = knight

    return gs
