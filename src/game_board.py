class GameBoard (object):

    def __init__(self):
        self.position = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.wins = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
                [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
                [0, 4, 8], [2, 4, 6] # Diagonals
                ]
        self.corners = [0, 2, 6, 8]
        self.spaces = [1, 3, 4, 5, 7]

    def is_valid(self, move):
        if self.position[move] == int(move):
            return True

        return False

    def check_win(self):
        for win in self.wins:
            i = 0
            while i < len(win):
                if win[i] >= 0 and win[i] <= 8:
                    i += 1
                    if i == 2:
                        return True
                else:
                    break

        return False

    def check_tie(self):
        i = 0
        while i < len(self.position):
            if self.position[i] == i:
                return False
            i += 1

        return True
