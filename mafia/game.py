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

            nominated = list(filter(lambda player: player.status.value, self.players))
            random.shuffle(nominated)
            nominated = nominated[0:3]

            for player in self.players:
                pass

            input()


game = Game(["p1", "p2", "p3", "p4", "p5", "p6"])
game.start()
