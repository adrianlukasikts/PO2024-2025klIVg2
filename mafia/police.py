import random

from citizen import Citizen


class Police(Citizen):
    def __init__(self, nickname: str = None):
        super().__init__(nickname)
        self.checked: dict[str, bool] = {}

    def add_vote(self, votes: dict[str, int]):
        for username in votes.keys():
            if self.checked.get(username):
                if self.checked[username]:
                    votes[username] +=1
            else:
                if username != self.nickname and random.randint(0, 1) == 1:
                    votes[username] += 1