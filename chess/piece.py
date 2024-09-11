from abc import ABC, abstractmethod

class Piece:
    @abstractmethod
    def get_moves_set(self, x: int, y: int) -> list[tuple[int, int]]:
        pass