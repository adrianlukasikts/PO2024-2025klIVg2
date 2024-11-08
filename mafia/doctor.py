from citizen import Citizen


class WasProtected(Exception):
    pass


class Doctor(Citizen):

    def __init__(self, nickname: str = None):
        super().__init__(nickname)
        self.last_protected = None

    def protect_player(self, player: str):
        if player == self.last_protected:
            raise WasProtected()
        self.last_protected = player
