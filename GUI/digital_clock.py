import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(300, 250, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 105px; color: hsl(111, 100%, 50%)")

        self.setStyleSheet("background-color: black;")

        font_path = os.path.abspath("DS-DIGIT.TTF")
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
            if font_families:
                my_font = QFont(font_families, 150)
                self.time_label.setFont(my_font)
            else:
                print("Font loaded, but no families found.")
        else:
            print(f"Failed to load font from: {font_path}")
            self.time_label.setFont(QFont("Arial", 150))  # Fallback font

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()


    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())    
