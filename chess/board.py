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


board = Board()
board.print_board()
