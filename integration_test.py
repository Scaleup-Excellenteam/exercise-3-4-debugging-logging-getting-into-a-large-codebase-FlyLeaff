from fixtures import game_state_center, game_state_corner ,game_state_edge, game_state_empty
from Piece import  Pawn, Rook, King, Queen
from enums import Player
from ai_engine import chess_ai


def test_knight_get_valid_piece_moves_center_board(game_state_center):
    knight = game_state_center.get_piece(4, 4)
    expected_moves = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
    
    result = knight.get_valid_piece_moves(game_state_center)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_center.board[6][5] = Pawn('p', 6, 5, Player.PLAYER_2)
    
    expected_moves = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
    
    result = knight.get_valid_piece_moves(game_state_center)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    
def test_knight_get_valid_piece_moves_edge_board(game_state_edge):
    knight = game_state_edge.get_piece(0, 4)
    expected_moves = [(2, 3), (2, 5), (1, 2), (1, 6)]
    
    result = knight.get_valid_piece_moves(game_state_edge)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_edge.board[2][3] = Pawn('p', 2, 3, Player.PLAYER_2)
    
    expected_moves = [(2, 3), (2, 5), (1, 2), (1, 6)]
    
    result = knight.get_valid_piece_moves(game_state_edge)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    

def test_knight_get_valid_piece_moves_corner_board(game_state_corner):
    knight = game_state_corner.get_piece(0, 0)
    expected_moves = [(2, 1), (1, 2)]
    
    result = knight.get_valid_piece_moves(game_state_corner)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"
    
    game_state_corner.board[2][1] = Pawn('p', 2, 1, Player.PLAYER_2)
    
    expected_moves = [(2, 1), (1, 2)]
    
    result = knight.get_valid_piece_moves(game_state_corner)
    assert set(result) == set(expected_moves), f"Expected {expected_moves}, but got {result}"



# eval board tests
def test_eval_empty_board(game_state_empty):
    

    ai = chess_ai()
    score = ai.evaluate_board(game_state_empty, Player.PLAYER_2)
    
    # Calculating expected score manually
    expected_score = 0
    assert expected_score == score, f"Expected {expected_score}, but got {score}"


def test_eval_custom_state(game_state_empty):
    
    game_state_empty.board[0][0] = Rook('r', 0, 0, Player.PLAYER_1)
    game_state_empty.board[7][7] = Rook('r', 7, 7, Player.PLAYER_2)
    game_state_empty.board[3][3] = Queen('q', 3, 3, Player.PLAYER_1)
    game_state_empty.board[4][4] = King('k', 4, 4, Player.PLAYER_2)
    game_state_empty.white_pieces = [game_state_empty.board[0][0], game_state_empty.board[3][3]]
    game_state_empty.black_pieces = [game_state_empty.board[7][7], game_state_empty.board[4][4]]
    
    ai = chess_ai()
    score = ai.evaluate_board(game_state_empty, Player.PLAYER_2)
    
    # Calculating expected score manually
    expected_score = 50 + 100 - 1000 - 50  # Rook + Queen for Player 1, King 
    assert expected_score == score, f"Expected {expected_score}, but got {score}"
