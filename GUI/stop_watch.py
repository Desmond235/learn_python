import os
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt6.QtCore import QTime, QTimer, Qt
from PyQt6.QtGui import QFont, QFontDatabase

class Stopwatch (QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
                           QLabel, QPushButton{
                               padding: 30px;
                           }
                           QLabel{
                               font-size:110px;
                                background-color: hsl(200,100%,85%);
                                border-radius: 20px;
                           }
                           QPushButton{
                               font-size: 30px;
                               background-color: hsl(359, 100%, 85%);
                               border-bottom-left-radius: 10px;
                               border-bottom-right-radius: 10px;
                               border-right: 2px solid hsl(0, 0%, 32%);
                               border-bottom: 2px solid hsl(0, 0%, 32%);
                           }
                           QPushButton:hover{
                               background-color: hsl(359, 100%, 90%);
                           }
                           """)
        
        hl = QHBoxLayout()
        hl.addWidget(self.start_button)
        hl.addWidget(self.stop_button)
        hl.addWidget(self.reset_button) 
        vbox.addLayout(hl)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
        self.load_custom_font()
    
    def start(self):
        self.timer.start(10)    
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
    
    def format_time(self, time:QTime):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        
        return f'{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}'
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        
    def load_custom_font(self):
        font_path = os.path.abspath("DS-DIGIT.TTF")
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 110)
        self.time_label.setFont(font)    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec())    