import pytest
from unittest.mock import MagicMock
from Piece import Knight, Pawn
from enums import Player
from chess_engine import game_state  # Import your game_state class

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



# Peaceful moves tests
    
def test_knight_get_valid_peaceful_moves_center_board(game_state_center):
    knight = game_state_center.get_piece(4, 4)
    expected_moves = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
    
    result = knight.get_valid_peaceful_moves(game_state_center)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_center.board[6][5] = Pawn('p', 6, 5, Player.PLAYER_2)
    
    expected_moves = [(6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
    
    result = knight.get_valid_peaceful_moves(game_state_center)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"


def test_knight_get_valid_peaceful_moves_edge_board(game_state_edge):
    knight = game_state_edge.get_piece(0, 4)
    expected_moves = [(2, 3), (2, 5), (1, 2), (1, 6)]
    
    result = knight.get_valid_peaceful_moves(game_state_edge)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_edge.board[2][3] = Pawn('p', 2, 3, Player.PLAYER_2)
    
    expected_moves = [(2, 5), (1, 2), (1, 6)]
    
    result = knight.get_valid_peaceful_moves(game_state_edge)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"

def test_knight_get_valid_peaceful_moves_corner_board(game_state_corner):
    knight = game_state_corner.get_piece(0, 0)
    expected_moves = [(2, 1), (1, 2)]
    
    result = knight.get_valid_peaceful_moves(game_state_corner)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_corner.board[2][1] = Pawn('p', 2, 1, Player.PLAYER_2)
    
    expected_moves = [(1, 2)]
    
    result = knight.get_valid_peaceful_moves(game_state_corner)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"


# Take move tests

def test_knight_get_valid_piece_takes_center_board(game_state_center):
    knight = game_state_center.get_piece(4, 4)
    expected_moves = []  # No takes on an empty board
    
    result = knight.get_valid_piece_takes(game_state_center)
    assert result == expected_moves, f"Expected {expected_moves}, but got {result}"
    
    game_state_center.board[6][5] = Pawn('p', 6, 5, Player.PLAYER_2)
    expected_moves = [(6,5)]
    result = knight.get_valid_piece_takes(game_state_center)
    assert result == expected_moves, f"Expected {expected_moves}, but got {result}"
    

def test_knight_get_valid_piece_takes_edge_board(game_state_edge):
    knight = game_state_edge.get_piece(0, 4)
    expected_moves = []
    
    result = knight.get_valid_piece_takes(game_state_edge)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_edge.board[1][6] = Pawn('p', 1, 6, Player.PLAYER_2)
    
    expected_moves = [(1,6)]
    
    result = knight.get_valid_piece_takes(game_state_edge)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"


def test_knight_get_valid_piece_takes_corner_board(game_state_corner):
    knight = game_state_corner.get_piece(0, 0)
    expected_moves = []
    
    result = knight.get_valid_piece_takes(game_state_corner)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_corner.board[2][1] = Pawn('p', 2, 1, Player.PLAYER_2)
    game_state_corner.board[1][2] = Pawn('p', 1, 2, Player.PLAYER_2)

    expected_moves = [(2, 1), (1, 2)]
    
    result = knight.get_valid_piece_takes(game_state_corner)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"