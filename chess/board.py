from chess.bishop import Bishop
from chess.field import Field
from chess.king import King
from chess.knight import Knight
from chess.pawn import Pawn
from chess.queen import Queen
from chess.rook import Rook


class Board:
    def __init__(self):
        self.grid = [
            [Field(Rook()), Field(Knight()), Field(Bishop()), Field(Queen()), Field(King()), Field(Bishop()),
             Field(Knight()), Field(Rook())],
            [Field(Pawn()) for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
        ]

    def print_board(self):
        for index, row in enumerate(self.grid[::-1]):
            print(8 - index, end=" ")
            for field in row:
                print(field.get_piece_name(), end=" ")
            print()
        print(" ", end=" ")
        for i in range(8):
            print(chr(ord("A") + i), end="    ")

    def is_valid_move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        if self.grid[x1][y1].piece is None:
            return False
        if self.grid[x2][y2].piece is not None:
            return False
        moves = self.grid[x1][y1].piece.get_moves_set(x1, y1)
        if not (x2, y2) in moves:
            return False
        # Todo

board = Board()
board.print_board()
