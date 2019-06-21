class Logger(object):

    def __init__(self):
        pass

    def print_board(self, board):
        print('\033c')
        print('\x1b[36m\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n\n\x1b[0m                {} | {} | {} \n               ===+===+===\n                {} | {} | {}\n               ===+===+===\n                {} | {} | {}\n\x1b[36m\n/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\n\n\x1b[0m'.format(board.position[0], board.position[1], board.position[2], board.position[3], board.position[4], board.position[5], board.position[6], board.position[7], board.position[8]))
