ROWS = 6
COLS = 7

class CSP:

    def __init__(self, board):
        self.board = board

    def forward_check(self):
        return [c for c in range(COLS) if self.board[0][c] == '.']

    def mrv(self):
        return min(self.forward_check())

    def valid(self, col):
        if col not in self.forward_check():
            print("Constraint Failed")
            return False
        return True