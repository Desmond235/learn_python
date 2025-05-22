import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,20, 200,30)
        self.line_edit.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter name")

        self.button.setStyleSheet("font-size: 15px; font-family: Arial; background-color: green; color: white;")
        self.button.setGeometry(210,20,100,30)
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())