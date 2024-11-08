from random import randint

from mafia.citizen import Citizen
from mafia.doctor import Doctor
from mafia.mafioso import Mafioso
from mafia.police import Police
from mafia.status import Status
from player import Player
import random


class Game:
    def __init__(self, logins: list[str]):
        self.players_num = len(logins)
        self.mafiosos_num = self.players_num // 3
        self.citizens_num = self.players_num - self.mafiosos_num
        self.players: list[Player] = [
            Police(),
            Doctor(),
            *[Mafioso() for _ in range(self.mafiosos_num)],
            *[Citizen() for _ in range(self.citizens_num - 2)]
        ]
        random.shuffle(logins)
        for i in range(self.players_num):
            self.players[i].nickname = logins[i]

        mafiosos = list(filter(lambda player: isinstance(player, Mafioso), self.players))
        Mafioso.mafiosos = map(lambda mafioso: mafioso.nickname, mafiosos)

    def start(self):
        def game_not_finished():
            return 0 < self.mafiosos_num < self.citizens_num

        def print_info(round_count: int):
            return f"Round: {round_count}\n Number of citizens: {self.citizens_num}\n Number of mafiosos: {self.mafiosos_num}\n Doctor - {self.players[1].status.name.lower()}\n Policeman - {self.players[0].status.name.lower()}"

        round_counter = 0
        while game_not_finished():
            round_counter += 1

            alive_players = list(filter(lambda player: player.status.value, self.players))
            random.shuffle(alive_players)
            nominated = alive_players[0:3]
            nominated = map(lambda player: player.nickname, nominated)
            votes = {nominated[0]: 0, nominated[1]: 0, nominated[2]: 0}
            for player in alive_players:
                player.add_vote(votes)
            max_votes = 0
            is_unique = True
            max_votes_nickname = ""
            for nickname, num_votes in votes.items():
                if num_votes > max_votes:
                    max_votes = num_votes
                    max_votes_nickname = nickname
                    is_unique = True
                if num_votes == max_votes:
                    is_unique = False
            if is_unique:
                killed_player = list(filter(lambda player: max_votes_nickname == player.nickname, self.players))[0]
                killed_player.status = Status.DEAD
            else:
                print("Nobody was executed")
            doctor = list(filter(lambda player: isinstance(player, Doctor), self.players))[0]
            alive_players = list(filter(lambda player: player.status.value, self.players))
            doctor.protect_player(alive_players[randint(0, len(alive_players))])
            # TODO



game = Game(["p1", "p2", "p3", "p4", "p5", "p6"])
game.start()
