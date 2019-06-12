from game_board import GameBoard
import unittest

class GameBoardTest(unittest.TestCase):

    def test_board(self):
        gb = GameBoard()
        assert gb.is_valid(5) == True
        gb.position[0] = 'X'
        gb.position[1] = 'X'
        gb.position[2] = 'X'
        assert gb.check_win() == True
