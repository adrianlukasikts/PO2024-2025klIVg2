from chess.bishop import Bishop
from chess.rook import Rook
from piece import Piece


class Queen(Piece):
    def get_moves_set(self, x: int, y: int) -> list[tuple[int, int]]:
        moves = []
        bishop = Bishop().get_moves_set(x, y)
        rook = Rook().get_moves_set(x, y)
        moves.extend(bishop)
        moves.extend(rook)
        return moves

    def __str__(self):
        return self.get_piece_color("Quee")

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        if x1 == x2 or y1 == y2:
            return Rook().get_moves_between(x1, y1, x2, y2)
        else:
            return Bishop().get_moves_between(x1,y1,x2,y2)
