from piece import Piece


class Pawn(Piece):
    def __init__(self):
        self.moved = False

    def get_moves_set(self, x: int, y: int) -> list[tuple[int, int]]:
        moves = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        if not self.moved:
            moves.append((x, y + 2))
        return moves

    def __str__(self):
        return "Pawn"
