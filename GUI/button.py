import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QWidget, QPushButton, QLabel, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtCore import Qt
from second_window import  second_window

class HoverShadowButton(QPushButton):
    """QPushButton that shows a drop-shadow only on hover."""
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        # Change the cursor to a pointing hand
        self.setCursor(QCursor(Qt.PointingHandCursor))
        # Set stylesheet with hover effects
        self.setStyleSheet("""
                    QPushButton {
                        font-size: 18px;
                        background-color: red;
                        color: white;
                        line-height: 10px;
                        border-radius: 10px;
                    }
                    QPushButton:hover {
                        background-color: darkred;
                        color: white;
                    }
                """)
        self._shadow = QGraphicsDropShadowEffect(self)
        self._shadow.setBlurRadius(15)
        self._shadow.setOffset(5,5)
        self._shadow.setColor(QColor(0,0,0,20))
        self._shadow.setEnabled(False)
        self.setGraphicsEffect(self._shadow)

    def enterEvent(self, event):
        self._shadow.setEnabled(True)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._shadow.setEnabled(False)
        super().leaveEvent(event)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = HoverShadowButton("Submit", self)
        self.second_window = second_window()
        self.label = QLabel("Hello",self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle("Hover Button Example")
        self.setStyleSheet("background-color: white;")
        self.button.setGeometry(150, 200, 200, 100)
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("""
          QLabel{font-size: 18px;}
        """)


        self.button.clicked.connect(self.open_second_window)

    def open_second_window(self):
        # self.second_window.show()
        print("submitted")
        self.button.setText("Submitted")
        # self.button.setDisabled(True)
        self.label.setText("Good Evening")
        # self.hide()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
