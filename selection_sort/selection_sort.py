from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


class SelectionSort(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interface()

    def interface(self):
        self.resize(300, 100)
        self.setWindowTitle("selection sort")
        self.show()
        etykieta1 = QLabel("liczby", self)
        etykieta2 = QLabel("wynik", self)

        self.liczba1Edt = QLineEdit()
        self.wynikEdt = QLineEdit()
        self.wynikEdt.setReadOnly(True)
        self.sortBtn = QPushButton("&sort", self)

        sortBtn = self.sortBtn
        sortBtn.clicked.connect(self.actions)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.wynikEdt, 1, 1)
        ukladT.addWidget(sortBtn)

        self.setLayout(ukladT)

    def selection_sort(self, elements: list[int]):
        for i in range(len(elements)):
            minimum_index = i
            for j in range(i + 1, len(elements)):
                if elements[j] < elements[minimum_index]:
                    minimum_index = j

            elements[minimum_index], elements[i] = elements[i], elements[minimum_index]

    def actions(self):
        reciver = self.sender()
        try:
            numbers = self.liczba1Edt.text()
            numbers = numbers.split(",")
            numbers = list(map(lambda number: int(number),numbers))
            self.selection_sort(numbers)

            self.wynikEdt.setText(str(numbers))

        except ValueError:
            print("ni ma")



app = QApplication(sys.argv)
okno = SelectionSort()
sys.exit(app.exec_())
