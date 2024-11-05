from status import Status
from abc import abstractmethod


class Player:
    def __init__(self, nickname: str = None):
        self.nickname = nickname
        self.status = Status.ALIVE

    def __repr__(self):
        return self.nickname

    @abstractmethod
    def add_vote(self, votes: dict[str, int]):
        pass
