import  sys
from PyQt5.QtWidgets import  QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import  Qt
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(450,100,500,500)
        self.setWindowIcon(QIcon(os.path.abspath('splash.png')))
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0,0, 500,100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7; "
                            "font-weight: bold;"
                            "font-style: italic;")

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()