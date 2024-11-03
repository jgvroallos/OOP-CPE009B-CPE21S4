import sys
import math
from PyQt5.QtWidgets import *
import re


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clearLogs()

    def initUI(self):
        self.myWidget = QWidget()
        self.setCentralWidget(self.myWidget)

        grid = QGridLayout()
        self.textLine = QLineEdit()
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        names = [
            '^', 'sin', 'cos', 'C', '',
            '7', '8', '9', '/', '',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', ''
        ]

        positions = [(i, j) for i in range(1, 6) for j in range(5)]
        for position, name in zip(positions, names):
            if name:
                button = QPushButton(name)
                button.clicked.connect(self.onButtonClick)
                grid.addWidget(button, *position)

        self.myWidget.setLayout(grid)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveFileDialog)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.exitApp)

        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle('Calculator')

    def onButtonClick(self):
        sender = self.sender().text()
        current_text = self.textLine.text()

        if sender == 'C':
            self.textLine.clear()
        elif sender == '=':
            expression = self.textLine.text()

            expression = re.sub(r'(\d)(sin|cos)', r'\1*math.\2', expression)

            expression = re.sub(r'sin\s+(\d+)', r'math.sin(math.radians(\1))', expression)
            expression = re.sub(r'cos\s+(\d+)', r'math.cos(math.radians(\1))', expression)

            expression = expression.replace('^', '**')

            if expression.count('(') != expression.count(')'):
                self.textLine.setText("Syntax Error")
                return
            try:
                result = eval(expression)
                self.textLine.setText(str(result))
                self.logRecord(expression, result)
            except Exception as e:
                self.textLine.setText("Syntax Error")

        elif sender == '^':
            if current_text:
                self.textLine.setText(current_text + '^')
            else:
                self.textLine.setText("Syntax Error")

        elif sender == 'sin':
            if current_text and current_text[-1].isdigit():
                self.textLine.setText(current_text + '*sin ')
            else:
                self.textLine.setText(current_text + 'sin ')

        elif sender == 'cos':
            if current_text and current_text[-1].isdigit():
                self.textLine.setText(current_text + '*cos ')
            else:
                self.textLine.setText(current_text + 'cos ')

        else:
            self.textLine.setText(current_text + sender)

    def logRecord(self, expression, result):
        with open("operations_log.txt", "a") as file:
            file.write(f"{expression} = {result}\n")

    def clearLogs(self):
        with open("operations_log.txt", "w") as file:
            file.write("")

    def exitApp(self):
        self.clearLogs()
        self.close()

    def saveFileDialog(self):
        with open("operations_log.txt", "r") as file:
            content = file.read()
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Log File", "", "Text Files (*.txt);;All Files (*)")
        if save_path:
            with open(save_path, "w") as save_file:
                save_file.write(content)
            QMessageBox.information(self, "Saved", "Operations log saved successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
