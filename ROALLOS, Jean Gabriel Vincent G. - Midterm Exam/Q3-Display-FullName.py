import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.x = 200
        self.y = 200
        self.width = 450
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        # create label for full name
        self.FullNameLabel = QLabel("Enter your fullname:", self)
        self.FullNameLabel.move(30, 75)

        # create textbox for full name input
        self.FullNameText = QLineEdit(self)
        self.FullNameText.move(200, 75)
        self.FullNameText.resize(200,20)

        # create button to display full name
        self.DisplayButton = QPushButton('Click to display your full name', self)
        self.DisplayButton.move(25, 150)
        self.DisplayButton.clicked.connect(self.on_click)

        # create textbox for full name display
        self.FullNameDisplay = QLineEdit(self)
        self.FullNameDisplay.move(200, 150)
        self.FullNameDisplay.resize(200,20)

        self.show()

    def on_click(self):

        # clears the output textbox and displays new input
        self.FullNameDisplay.clear()
        FullName = self.FullNameText.text()
        self.FullNameDisplay.setText(FullName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
