import random

class Player(object):

    def __init__(self, piece):
        self.piece = piece

    def move(self, board):
        m = input('Choose Open Position:\n')
        if board.is_valid(m):
            return m
        else:
            self.move(board)

class EasyCom(Player):

    def __init__(self, piece):
        super().__init__(piece)

    def move(self, board):
        m = random.randint(0, 8)
        if board.is_valid(m) == True:
            return m
        else:
            self.move(board)
