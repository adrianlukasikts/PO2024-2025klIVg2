from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel
import random

class Die:
    def __init__(self, value: int):
        self.value = value
        self.pixmap = QPixmap(f"inf04czerwiec/{value}.png")
        self.pixmap = self.pixmap.scaled(100, 100)

def rand_die() -> int:
    return random.randint(1, 6)


class DiceGame(QWidget):
    NUM_DICE = 5
    INITIAL_VALUE_DIE = 0
    def __init__(self):
        super().__init__()
        self.dice: list[Die] = [Die(DiceGame.INITIAL_VALUE_DIE) for _ in range(DiceGame.NUM_DICE)]
        self.labels = [QLabel(self) for _ in range(DiceGame.NUM_DICE)]
        self.layout = QHBoxLayout()
        self.interface()

    def rollDice(self):
        self.dice = [Die(rand_die()) for _ in range(DiceGame.NUM_DICE)]
        self.add_dice_label()
        print(list(map(lambda die: die.value, self.dice)))

    def interface(self):
        self.resize(100, 100)
        self.setWindowTitle("Gra w kości")
        roll_dice = QPushButton("&RollDice", self)
        roll_dice.setFixedSize(200, 100)
        roll_dice.clicked.connect(self.rollDice)

        self.layout.addWidget(roll_dice)
        self.add_dice_label()
        self.setLayout(self.layout)

        self.show()

    def add_dice_label(self):
        for i in range(len(self.dice)):
            self.labels[i].setPixmap(self.dice[i].pixmap)
            self.layout.addWidget(self.labels[i])


    def calculate_points(self, dices: list[int]) -> int:
        dices.sort()
        counter = 1
        current_dice = dices[0]
        result = 0
        for dice in dices[1:]:
            if current_dice == dice:
                counter += 1
            else:
                if counter >= 2:
                    result += (counter * current_dice)
                current_dice = dice
                counter = 1
        if counter >= 2:
            result += (counter * current_dice)
        return result


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = DiceGame()
    sys.exit(app.exec_())
