from logger import Logger
from player import Player, EasyCom
from game_board import GameBoard
from game import Game

def run_game():
    logger = Logger()
    gb = GameBoard()
    p1 = Player('X')
    game = Game(logger, gb, p1)
    game.choose_player()
    game.play()

if __name__ == '__main__':
    run_game()
