import sys
from PyQt5.QtWidgets import  QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        self.resize(600,20)
        self.initUI()

    def initUI(self):
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        # self.central_widget.setLayout(self.layout)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 18px;
                font-family : Arial;
                padding: 10px 15px;
                margin: 15px;
                border: 2px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: hsl(0, 85%, 64%);
                color: white;
            }
             QPushButton#button2{
                background-color: hsl(122, 100%, 64%);
                color: white;
            }
             QPushButton#button3{
                background-color: hsl(285, 91%, 66%);
                color: white;
            }
            QPushButton#button1:hover{
                background-color: hsl(0, 85%, 84%);
                color: white;
            }
             QPushButton#button2:hover{
                background-color: hsl(122, 100%, 84%);
                color: white;
            }
             QPushButton#button3:hover{
                background-color: hsl(285, 91%, 86%);
                color: white;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())