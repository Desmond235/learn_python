import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, 
)

from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime

from timer_setter_dialog import TimeSetterDialog
    
class Clock(QWidget):
    def __init__(self):
        super().__init__()    
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.offest_secs = 0 
        self.initUI()
        
    def initUI(self): 
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Clock")
        self.setGeometry(300,250,300,100)
        vbox = QVBoxLayout()
        
        self.time_label.setStyleSheet(
            "color: hsl(111, 100%, 50%);"
            "font-size: 110px;"
            )
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.mousePressEvent = self.label_clicked
        
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.load_custom_font()
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        
        
    def update_time(self):
        """
        Updates the time label with the current system time in the format 'hh:mm:ss AM/PM'.

        This method retrieves the current time using QTime, formats it as a string with hours,
        minutes, seconds, and AM/PM indicator, and updates the associated QLabel to display
        the current time.
        """
        current_time = QTime.currentTime()
        ajusted_time = current_time.addSecs(self.offest_secs)
        current_time = ajusted_time.toString("hh:mm:ss AP")
        self.time_label.setText(current_time) 
        
    def label_clicked(self, event):
        """
        Handles the label click event to open a time setter dialog and update the clock offset.

        When the label is clicked, this method opens a TimeSetterDialog to allow the user to select a new time.
        If the user confirms the dialog, it retrieves the selected time, calculates the offset in seconds between
        the current time and the new time, updates the offset, and refreshes the displayed time accordingly.

        Args:
            event: The event object associated with the label click.
        """
        dialog = TimeSetterDialog(self)
        if dialog.exec_():
            new_time = dialog.get_time()
            now = QDateTime.currentDateTime()
            new_datetime = QDateTime(
                now.date(),
                QTime(new_time.hour(), new_time.minute(), new_time.second())
            )
            self.offest_secs = now.secsTo(new_datetime)
            self.update_time()
        
    def load_custom_font(self):
        """
        Loads a custom font from the "DS-DIGIT.TTF" file and applies it to the time label.
        If the custom font fails to load, falls back to using the Arial font.
        Steps:
            1. Resolves the absolute path to the "DS-DIGIT.TTF" font file.
            2. Attempts to add the font to the application's font database.
            3. If successful, retrieves the font family and sets it with a size of 110 to the time label.
            4. If the font cannot be loaded or no families are found, prints an error message and uses Arial instead.
        """
        font_path = os.path.abspath("DS-DIGIT.TTF")   
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        if font_id != -1:
            font_familes = QFontDatabase.applicationFontFamilies(font_id)[0]
            if font_familes:
                my_font = QFont(font_familes, 110)
                self.time_label.setFont(my_font)
            else:
                print("font loaded, but no families fond")   
        else:
            self.time_label.setFont(QFont("Arial", 110))   
                  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())     