from random import randint
from citizen import Citizen
from doctor import Doctor, WasProtected
from mafioso import Mafioso
from police import Police
from status import Status
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

        def nominated_players(alive_players: list[Player]) -> dict[str, int]:
            random.shuffle(alive_players)
            nominated = alive_players[0:3]
            nominated = list(map(lambda player: player.nickname, nominated))
            return {nominated[0]: 0, nominated[1]: 0, nominated[2]: 0}

        def print_info(round_count: int):
            return f"Round: {round_count}\n Number of citizens: {self.citizens_num}\n Number of mafiosos: {self.mafiosos_num}\n Doctor - {self.players[1].status.name.lower()}\n Policeman - {self.players[0].status.name.lower()}"

        def player_vote_phase() -> None:
            alive_players = self.get_alive_players()
            votes = nominated_players(alive_players)
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
                elif num_votes == max_votes:
                    is_unique = False
            print(votes, is_unique)
            if is_unique:
                killed_player = list(filter(lambda player: max_votes_nickname == player.nickname, self.players))[0]
                killed_player.status = Status.DEAD
                print(f"{killed_player.nickname} has been banished.")
                if isinstance(killed_player, Mafioso):
                    self.mafiosos_num -= 1
                else:
                    self.citizens_num -= 1
            else:
                print("Nobody was executed")

        def doctor_phase() -> str:
            doctor = self.get_doctor()
            if doctor:
                alive_players = self.get_alive_players()
                random_player = random.choice(alive_players)
                try:
                    doctor.protect_player(random_player)
                    return random_player.nickname
                except WasProtected:
                    alive_players.remove(random_player)
                    random_player = random.choice(alive_players)
                    doctor.protect_player(random_player)
                    return random_player.nickname

        def mafia_phase(protected_player_nick: str):
            citizen_players = list(filter(lambda player: not isinstance(player, Mafioso), self.get_alive_players()))

            to_be_executed: Citizen = random.choice(citizen_players)
            if to_be_executed.nickname == protected_player_nick:
                print("nobody died")
            else:
                to_be_executed.status = Status.DEAD
                self.citizens_num -= 1
                print(f"Player: {to_be_executed.nickname} died.")

        round_counter = 0
        while game_not_finished():
            round_counter += 1

            player_vote_phase()

            if self.mafiosos_num == 0:
                break

            protected_player_nick = doctor_phase()

            mafia_phase(protected_player_nick)

            print(f"Mafiosos: {list(filter(lambda mafioso: mafioso.status.value, self.get_mafiosos()))}")
            input()

        if self.mafiosos_num == 0:
            print("Citizens won!")
        else:
            print("Mafiosos won!")

    def get_doctor(self) -> Doctor:
        doc: Doctor = list(filter(lambda player: isinstance(player, Doctor), self.players))[0]
        return doc if doc.is_alive() else None

    def get_mafiosos(self) -> list[Mafioso]:
        return list(filter(lambda player: isinstance(player, Mafioso), self.players))

    def get_alive_citizens(self) -> list[Citizen]:
        return list(filter(lambda player: isinstance(player, Citizen) and player.is_alive(), self.players))

    def get_alive_players(self) -> list[Player]:
        return list(filter(lambda player: player.is_alive(), self.players))


game = Game(["p1", "p2", "p3", "p4", "p5", "p6"])
game.start()
