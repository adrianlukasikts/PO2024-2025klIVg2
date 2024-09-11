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