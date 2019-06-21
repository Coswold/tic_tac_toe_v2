from player import EasyCom

class Game(object):

    def __init__(self, logger, board, player1, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.logger = logger

    def choose_player(self):
        go = True
        while go:
            print('\033c')
            response = int(input('Choose Game Type:\n1 - [ManVman]\n2 - [ManVCom]\n'))
            self.logger.print_board(self.board)
            if response == 1:
                self.player2 = Player('O')
                return
            else:
                self.player2 = EasyCom('O')
                return

    def play(self):
        player = self.player1
        go = True
        while go:
            if self.board.check_win() == False and self.board.check_tie() == False:
                if player == self.player1:
                    move = self.player1.move(self.board)
                    self.board.position[int(move)] = player.piece
                    self.logger.print_board(self.board)
                    player = self.player2
                else:
                    move = self.player2.move(self.board)
                    self.board.position[int(move)] = player.piece
                    self.logger.print_board(self.board)
                    player = self.player1
            else:
                play_again = int(input('Would you like to playe again?\n1 - [Yes]\n2 - [No]\n'))
                if play_again == 1:
                    self.board.clear()
                    self.play()
                else:
                    return


