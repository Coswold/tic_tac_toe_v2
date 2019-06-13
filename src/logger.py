class Logger(object):

    def __init__(self):
        pass

    def print_board(self, board):
        print('\033c')
        print('\x1b[36m\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n\n\x1b[0m
              {} | {} | {} \n    ===+===+===\n      {} | {} | {}\n
              ===+===+===\n      {} | {} | {}\n\x1b[36m\n/\/\/\/\/\/\/\/\/\/\
                      /\/\/\/\/\/\/\/\/\/\/\n\n\x1b[0m'.format(board.positions[0], boar))
