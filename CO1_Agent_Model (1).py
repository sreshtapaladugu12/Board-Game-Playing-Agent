from dataclasses import dataclass
from typing import List

ROWS = 6
COLS = 7

@dataclass
class State:
    board: List[List[str]]

class ConnectFour:

    def __init__(self):
        self.board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

    def display(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(" ".join(row))

    def valid_actions(self):
        return [c for c in range(COLS) if self.board[0][c] == '.']

    def transition(self, col, piece):
        for row in range(ROWS-1, -1, -1):
            if self.board[row][col] == '.':
                self.board[row][col] = piece
                return True
        return False