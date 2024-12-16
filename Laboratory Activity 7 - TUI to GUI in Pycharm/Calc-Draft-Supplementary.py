import sys
import math
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit,QPushButton, QAction, QFileDialog, QApplication, QMenuBar, QTextEdit
from PyQt5.QtCore import pyqtSlot

class Scical(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('~ Scientific Calculator ~')
        self.setGeometry(300, 300, 400, 400)
        
        self.initUI()


    def initUI(self):
        mainWidget = QWidget(self)
        mainLayout = QVBoxLayout()
        self.textLine = QLineEdit(self)

        mainLayout.addWidget(self.textLine)
        grid = QGridLayout()
        self.textLine.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 10px;
                background-color: yellow;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
        """)
        mainLayout.addLayout(grid)

        butt = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sine', 'cosine', 'expo', 'Clear',
            'sqrt',]

        pos = [(i, j) for i in range(6) for j in range(4)]
        for position, name in zip(pos, butt):
            button = QPushButton(name)
            button.clicked.connect(self.onButtonClick)
            grid.addWidget(button, *position)
            button.setStyleSheet("""
                    QPushButton {
                        font-size: 16px;
                        padding: 20px;
                        background-color: #f0f0f0;
                        border: 2px solid black;
                        border-radius: 5px;
                        margin: 5px;
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;
                    }
                    QPushButton:pressed {
                        background-color: yellow;
                    }
                """)
        self.calculations = QTextEdit()
        self.calculations.setReadOnly(True)  
        self.calculations.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 10px;
                background-color: #f9f9f9;
                border: 2px solid #ccc;
                border-radius: 5px;
                margin-top: 10px;
            }
        """)

        mainLayout.addWidget(self.calculations)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
        self.createMenu()

    def createMenu(self):
        mainMenu = QMenuBar(self)
        fileMenu = mainMenu.addMenu('File')

        clearAction = QAction('Clear File', self)
        clearAction.setShortcut('Ctrl+C')
        clearAction.triggered.connect(self.Clearcalc)
        fileMenu.addAction(clearAction)

        openAction = QAction('Load File', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.Opencalc)
        fileMenu.addAction(openAction)

        saveAction = QAction('Save File', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.Savecalc)
        fileMenu.addAction(saveAction)

        exitAction = QAction('Exit File', self)
        exitAction.setShortcut('Ctrl+X')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        self.setMenuBar(mainMenu)

    def onButtonClick(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == 'Clear':
            self.Clearcalc()
        elif button_text == '=':
            self.evaluateExpression()
        elif button_text == 'sine':
            self.calculateTrig('sin')
        elif button_text == 'cosine':
            self.calculateTrig('cos')
        elif button_text == 'expo':
            self.textLine.setText(self.textLine.text() + '**')
        elif button_text == 'sqrt':
            self.textLine.setText('sqrt(' + self.textLine.text() + ')')
        else:
            current_text = self.textLine.text()
            self.textLine.setText(current_text + button_text)

    def isValidExpression(self, expression):
        # Regular expression to allow only valid math symbols and numbers
        valid_chars = re.compile(r'^[\d+\-*/().^sinecosqrt ]+$')
        # This checks if the expression contains only numbers and mathematical symbols
        if not valid_chars.match(expression):
            return False
        return True

    def evaluateExpression(self):
        expression = self.textLine.text().replace("^", "**")
        try:
            result = str(eval(expression))
            self.textLine.setText(result)
            self.calculations.append(f"{expression} = {result}")
        except Exception:
            self.textLine.setText("No input!")

    def calculateTrig(self, func):
        expression = self.textLine.text()
        try:
            value = float(expression)
            if func == 'sin':
                result = str(math.sin(math.radians(value)))
                self.calculations.append(f"sin({expression}) = {result}")
            elif func == 'cos':
                result = str(math.cos(math.radians(value)))
                self.calculations.append(f"cos({expression}) = {result}")
            self.textLine.setText(result)
        except ValueError:
            self.textLine.setText("Enter the number first!")

    def Savecalc(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.calculations.toPlainText())

    def Opencalc(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load File", "", "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.calculations.setText(data)

    def Clearcalc(self):
        self.textLine.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Scical()
    calculator.show()
    sys.exit(app.exec_())
