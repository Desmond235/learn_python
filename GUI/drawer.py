from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton,
                             QSizePolicy)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import os
import  sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.top_bar = QWidget()
        self.to_bar_layout = QHBoxLayout(self.top_bar)
        self.menu_button = QPushButton("X")
        self.initUI()

    def initUI(self):
        # main window
        self.setGeometry(200, 100, 900, 600)
        self.setWindowIcon(QIcon(os.path.abspath("splash.png")))
        self.setCentralWidget(self.central_widget)

        # content area
        self.content.setStyleSheet("background-color: white; border-radius: 5px;")
        self.content_layout.addWidget(self.top_bar)

        #menu button
        self.to_bar_layout.addWidget(self.menu_button)
        self.to_bar_layout.setContentsMargins(0,0,0,0)
        self.to_bar_layout.setAlignment(Qt.AlignTop)

        self.menu_button.setContentsMargins(0,0,0,0)
        self.menu_button.setFixedSize(40,40)
        self.menu_button.setFont(QFont("Poppins", 18))
        self.menu_button.setStyleSheet(
            """
            QPushButton{
             background-color: transparent;
             border: none; 
             border-radius: 20px;
            }
            QPushButton:hover{
                background-color: #ecf0f1
            }
            """
        )

        # sidebar
        self.sidebar.setStyleSheet('background-color: #2c3e50; color: white;')
        self.sidebar.setFixedWidth(200)
        self.sidebar_layout.addWidget(QLabel("Menu", alignment= Qt.AlignCenter))
        for item in ['Dashboard', "Home", "Settings", "Logout"]:
            btn = QPushButton(item)
            btn.setStyleSheet("""
              QPushButton{
               background-color: #2c3e54;
               color: white;
              }
              QPushButton:hover{
                background-color: #34495e;
                opacity: 0.1px;
              }
            """)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.sidebar_layout.addWidget(btn)
        self.sidebar_layout.addStretch()

        # main layout
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content)

        self.menu_button.clicked.connect(self.toggle_sidebar)

    def toggle_sidebar(self):
       visible = not self.sidebar.isVisible()
       self.sidebar.setVisible(visible)

       if visible:
            self.menu_button.setText("X")
       else:
           self.menu_button.setText("☰")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()