# CO3: Advanced CSP for Connect Four

ROWS = 6
COLS = 7

class ConnectFourCSP:

    def __init__(self):
        self.board = [['.' for _ in range(COLS)]
                      for _ in range(ROWS)]

    def display(self):

        print("\nBoard")

        for row in self.board:
            print(" ".join(row))

        print()

    def valid_column(self, col):

        if col < 0 or col >= COLS:

            print("Constraint Failed")
            print("Reason: Column outside board")

            return False

        return True

    def column_not_full(self, col):

        if self.board[0][col] != ".":

            print("Constraint Failed")
            print("Reason: Column is Full")

            return False

        return True

    def forward_checking(self):

        legal_moves = []

        for col in range(COLS):

            if self.board[0][col] == '.':
                legal_moves.append(col)

        return legal_moves

    def mrv(self):

        best_col = -1
        minimum_space = 999

        for col in range(COLS):

            count = 0

            for row in range(ROWS):

                if self.board[row][col] == '.':
                    count += 1

            if count > 0 and count < minimum_space:

                minimum_space = count
                best_col = col

        return best_col

    def place_piece(self, col, piece):

        if not self.valid_column(col):
            return False

        if not self.column_not_full(col):
            return False

        for row in range(ROWS - 1, -1, -1):

            if self.board[row][col] == '.':

                self.board[row][col] = piece

                print(f"\nPlaced {piece} in Column {col+1}")

                return True

        print("Backtracking...")
        return False


game = ConnectFourCSP()

print("INITIAL BOARD")
game.display()

game.place_piece(3, 'X')
game.place_piece(3, 'O')
game.place_piece(2, 'X')

game.display()

print("Forward Checking")

moves = game.forward_checking()

for move in moves:
    print("Column", move + 1)

print("\nMRV Suggested Column")

print(game.mrv() + 1)
