from PyQt5.QtWidgets import  QLabel, QWidget
from PyQt5.QtGui import  QIcon
import  os

class second_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second")
        self.setGeometry(150,150,300,200)
        self.setWindowIcon(QIcon(os.path.abspath("splash.png")))
        label = QLabel("This is the second window", self)
        label.move(50,80)

