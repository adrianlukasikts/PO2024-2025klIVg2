from chess.colors import Color
from piece import Piece


class Pawn(Piece):
    def __init__(self, color: Color = Color.WHITE):
        super().__init__(color)
        self.moved = False

    def get_moves_set(self, x: int, y: int) -> list[tuple[int, int]]:
        moves = [(x, y + self.color.value), (x - 1, y + self.color.value), (x + 1, y + self.color.value)]
        if not self.moved:
            moves.append((x, y + self.color.value * 2))
        return moves

    def __str__(self):
        return self.get_piece_color("Pawn")

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        if abs(y1 - y2) == 2:
            step = 1 if y2 > y1 else -1
            return [(x1, y1 + step)]
        else:
            return []
