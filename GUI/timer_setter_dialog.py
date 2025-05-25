from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QTimeEdit,
                             QPushButton)
from PyQt5.QtCore import QTime

class TimeSetterDialog(QDialog):
    """
    A dialog window for setting a new time using a QTimeEdit widget.
    Inherits from:
        QDialog
    Attributes:
        set_time (QTimeEdit): Widget for selecting the time.
        set_time_button (QPushButton): Button to confirm and set the selected time.
    # Methods:
        __init__(parent=None):
            Initializes the dialog, sets up the UI, and connects the button signal.
        get_time():
            Returns the currently selected time as a QTime object.
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Set new time")
        self.setGeometry(400,300,250,100)
        self.setStyleSheet(
            "background-color: #2c3e50;"
            "color: White;"
            
            )
        layout = QVBoxLayout(self)
        
        self.set_time = QTimeEdit(self)
        self.set_time.setDisplayFormat("hh:mm AP")
        self.set_time.setTime(QTime.currentTime())
        
        self.set_time_button = QPushButton("Set time")
        self.set_time_button.clicked.connect(self.accept)
        
        
        layout.addWidget(self.set_time)
        layout.addWidget(self.set_time_button)
        self.setLayout(layout)
        
    def get_time(self):
        return self.set_time.time()    