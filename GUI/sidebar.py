from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QHBoxLayout, QSizePolicy
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sidebar with Menu Icon")
        self.setGeometry(200, 100, 900, 600)
        self.setWindowIcon(QIcon(os.path.abspath('splash.png')))

        # Main widget & layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #2c3e50; color: white;")
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        self.sidebar_layout.addWidget(QLabel("Menu", alignment=Qt.AlignCenter))
        for item in ["Dashboard", "Settings", "Logout"]:
            btn = QPushButton(item)
            btn.setStyleSheet("color: white; background-color: #34495e;")
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.sidebar_layout.addWidget(btn)
        self.sidebar_layout.addStretch()

        # Content area
        self.content = QWidget()
        self.content.setStyleSheet("background-color: white;")
        self.content_layout = QVBoxLayout(self.content)

        # Top bar with menu icon
        self.top_bar = QWidget()
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_layout.setAlignment(Qt.AlignTop)


        self.menu_button = QPushButton("X")  # Unicode fallback icon
        self.menu_button.setFixedSize(40, 40)
        self.menu_button.setContentsMargins(0,0,0,0)
        self.menu_button.setFont(QFont("Arial", 18))
        self.menu_button.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #ecf0f1;
            }
        """)
        self.menu_button.clicked.connect(self.toggle_sidebar)

        self.top_bar_layout.addWidget(self.menu_button)
        self.top_bar_layout.addStretch()

        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(QLabel("Main content goes here..."))

        # Add to main layout
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content)

    def toggle_sidebar(self):
        visible = not self.sidebar.isVisible()
        self.sidebar.setVisible(visible)

        if visible:
            self.menu_button.setText("X")
        else:
            self.menu_button.setText("☰")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
