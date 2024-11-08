from player import Player


class Mafioso(Player):

    mafiosos = []

    def add_vote(self, votes: dict[str, int]):
        for key in votes.keys():
            if key not in self.mafiosos:
                votes[key] += 1


