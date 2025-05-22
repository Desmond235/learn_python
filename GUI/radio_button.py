from PyQt5.QtWidgets import (QMainWindow, QApplication, QRadioButton, QButtonGroup)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 900, 600)
        self.setWindowTitle("Checkbox")
        self.radio1 = QRadioButton("visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(10,0,300,50)
        self.radio2.setGeometry(10, 30, 300, 50)
        self.radio3.setGeometry(10, 60, 300, 50)
        self.radio4.setGeometry(10, 90, 300, 50)
        self.radio5.setGeometry(10, 120, 300, 50)

        self.setStyleSheet(
            """
            QRadioButton{
                font-size: 18px;
                font-family: Arial;
                padding: 10px;
            }
            """
        )

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed); self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed); self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f'{radio_button.text()} is selected')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()