from game_board import GameBoard
from player import Player, EasyCom
import unittest

class GameTest(unittest.TestCase):

    def test_board(self):
        gb = GameBoard()
        assert gb.is_valid(5) == True
        gb.position[0] = 'X'
        gb.position[1] = 'X'
        gb.position[2] = 'X'
        assert gb.check_win() == True
        assert gb.is_valid(1) == False
        assert gb.check_tie() == False
        gb.position[3] = 'X'
        gb.position[4] = 'X'
        gb.position[5] = 'X'
        gb.position[6] = 'X'
        gb.position[7] = 'X'
        gb.position[8] = 'X'
        assert gb.check_tie() == True

    def test_easycom(self):
        gb = GameBoard()
        player = EasyCom('X')
        m = player.move(gb)
        assert m >=0 and m <= 8
