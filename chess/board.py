from chess.bishop import Bishop
from chess.field import Field
from chess.king import King
from chess.knight import Knight
from chess.pawn import Pawn
from chess.queen import Queen
from chess.rook import Rook

class InvalidMoveException(Exception):
    pass

class Board:
    def __init__(self):
        #Todo odwrocona szachownica o 90 stopni
        pieces = [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()]
        self.grid = [
            *[[Field(piece), Field(Pawn()), *[Field() for _ in range(6)]] for piece in pieces]
        ]

    def print_board(self):
        for row in range(7, -1, -1):
            print(row+1 , end=" ")

            for column in range(8):
                print(self.grid[column][row].get_piece_name(), end=" ")
            print()
        print("  ", end=" ")
        for i in range(8):
            print(chr(ord("A") + i), end="    ")
        print()


        # for index, row in enumerate(self.grid[::-1]):
        #     print(8 - index, end=" ")
        #     for field in row:
        #         print(field.get_piece_name(), end=" ")
        #     print()
        # print(" ", end=" ")
        # for i in range(8):
        #     print(chr(ord("A") + i), end="    ")
        # print()

    def is_valid_move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        if self.grid[x1][y1].piece is None:
            return False
        if self.grid[x2][y2].piece is not None:
            return False
        moves = self.grid[x1][y1].piece.get_moves_set(x1, y1)
        if not (x2, y2) in moves:
            return False
        moves_between = self.grid[x1][y1].piece.get_moves_between(x1, y1, x2, y2)
        for i, j in moves_between:
            if self.grid[i][j].piece is not None:
                return False
        return True

    def make_move(self, x1: int, y1: int, x2: int, y2: int):
        if self.is_valid_move(x1, y1, x2, y2):
            self.grid[x2][y2].piece = self.grid[x1][y1].piece
            self.grid[x1][y1].piece = None
        else:
            raise InvalidMoveException()

board = Board()
board.print_board()

assert board.is_valid_move(1,1,1,2)
assert not board.is_valid_move(5,0,3,2)
assert not board.is_valid_move(5,0,5,7)

try:
    board.make_move(1,1,1,2)
    board.print_board()
except InvalidMoveException:
    print("nuh uh")


# print(board.is_valid_move(1,1,1,2))
# print(board.is_valid_move(5,0,3,2))
# print(board.is_valid_move(5,0,5,7))