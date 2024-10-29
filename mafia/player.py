from status import Status


class Player:
    def __init__(self, nickname: str = None):
        self.nickname = nickname
        self.status = Status.ALIVE

