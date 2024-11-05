import random

from player import Player


class Citizen(Player):
    def add_vote(self, votes: dict[str, int]):
        for key in votes.keys():
            if key != self.nickname and random.randint(0, 1) == 1:
                votes[key] += 1
