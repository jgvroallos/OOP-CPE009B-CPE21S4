import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 200
        self.y = 200
        self.width = 350
        self.height = 350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        # create button
        self.button = QPushButton('Click to Change Color', self)
        self.button.move(120, 150)
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.button.setStyleSheet("background-color : yellow")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
