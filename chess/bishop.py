from piece import Piece


class Bishop(Piece):
    def get_moves_set(self, x: int, y: int) -> list[tuple[int, int]]:
        moves = []
        for i in range(-7, 0):
            moves.append((x + i, y + i))
        for i in range(1, 8):
            moves.append((x + i, y + i))
        for i in range(-7, 0):
            moves.append((x + i, y - i))
        for i in range(1, 8):
            moves.append((x + i, y - i))
        return moves

    def __str__(self):
        return self.get_piece_color("Bish")

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        step_y = 1 if y1 < y2 else -1
        step_x = 1 if x1 < x2 else -1
        return [(i,j) for i, j in zip(range(x1 + step_x, x2, step_x), range(y1 + step_y, y2, step_y))]

