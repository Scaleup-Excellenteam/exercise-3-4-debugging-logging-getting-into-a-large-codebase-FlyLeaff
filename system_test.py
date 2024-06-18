import pytest
from chess_engine import game_state

def test_fools_mate():
    gs = game_state()
    
    
    gs.move_piece((1, 2), (3, 2), False)  
    gs.move_piece((6, 3), (4, 3), False)  
    
    
    gs.move_piece((1, 1), (3, 1), False) 
    gs.move_piece((7, 4), (3, 0), False)  #  checkmate

    # Check if black wins (checkmate)
    assert gs.checkmate_stalemate_checker() == 0, "Expected Black to win (checkmate) but it didn't happen."

if __name__ == "__main__":
    pytest.main()
