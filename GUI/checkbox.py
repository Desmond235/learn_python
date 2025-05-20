from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QApplication, QCheckBox,QDateTimeEdit
)
import sys
import os
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QDateTime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 500, 500)
        self.icon = os.path.abspath('splash.png')

        self.datetime_picker = QDateTimeEdit(self)

        #  date picker
        self.datetime_picker.setDateTime(QDateTime.currentDateTime())
        self.datetime_picker.setDisplayFormat('yyyy-MM-dd')
        self.datetime_picker.setCalendarPopup(True)
        self.datetime_picker.setFixedWidth(100)
        self.datetime_picker.setStyleSheet(
            """
            QDateTimeEdit{
            padding: 5px;
            font-size: 12px;
            background-color: white;
            color: black
            }
            
            QCalendarWidget QCalendar{
                background-color: red;
            }
           /* Tool buttons (month/year title, arrows) */
    QCalendarWidget QToolButton {
        background-color: #e6e6e6;
        color: black;
        font-size: 12px;
        padding-right: 20px;
        text-align: center;
        margin: 2px;
        border: none;
    }

    /* Dropdown menu for month selection */
    QCalendarWidget QMenu {
        background-color: white;
        color: black;
    }

    /* Spin box for year navigation */
    QCalendarWidget QSpinBox {
        color: black;
        font-size: 12px;
        padding: 2px;
    }

    /* Ensure dropdown arrow is visible and aligned */
    QCalendarWidget QToolButton::menu-indicator {
        subcontrol-origin: padding;
        subcontrol-position: right center;
        padding-left: 7px;
        width: 12px;
        height: 12px;
    }
            """
        )

        # Create checkboxes
        self.checkbox1 = QCheckBox("Male")
        self.checkbox2 = QCheckBox("Female")

        # Apply styling
        self.checkbox1.setFont(QFont("Arial", 15))
        self.checkbox2.setFont(QFont("Arial", 15))

        # Layout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.checkbox1)
        self.vbox.addWidget(self.checkbox2)
        self.vbox.addWidget(self.datetime_picker)

        #Alignment
        self.vbox.setAlignment(Qt.AlignTop)

        # Set central widget and layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.vbox)
        self.setCentralWidget(self.central_widget)

        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon(self.icon))

        self.checkbox1.stateChanged.connect(self.checked_male)
        self.checkbox2.stateChanged.connect(self.checked_female)

    def checked_female(self, state):
        print("You are a female" if state == Qt.Checked else 'You are not a female')
    def checked_male(self, state):
        print('You are a male' if state == Qt.Checked else "You are not a male")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
