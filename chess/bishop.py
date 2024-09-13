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
        return "Bish"
