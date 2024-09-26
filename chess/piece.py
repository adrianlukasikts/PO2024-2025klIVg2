from abc import ABC, abstractmethod

from chess.colors import Color


class Piece:
    def __init__(self, color: Color = Color.WHITE):
        self.color = color

    @abstractmethod
    def get_moves_set(self, x: int, y: int) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        pass
