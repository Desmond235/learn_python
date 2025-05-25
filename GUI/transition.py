import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QStackedWidget, QVBoxLayout, QLabel
)
from PyQt5.QtCore import QPropertyAnimation, QRect

class SlideTransition(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transition Animation")
        self.setGeometry(200, 200, 400, 300)

        self.stack = QStackedWidget(self)
        self.page1 = self.create_page("This is Page 1", "Go to Page 2", self.next_page)
        self.page2 = self.create_page("This is Page 2", "Back to Page 1", self.prev_page)

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        self.setLayout(layout)

    def create_page(self, text, button_text, slot):
        page = QWidget()
        label = QLabel(text, page)
        button = QPushButton(button_text, page)

        label.move(150, 100)
        button.move(130, 150)
        button.clicked.connect(slot)
        return page

    def next_page(self):
        self.animate_transition(self.page1, self.page2, direction='left')

    def prev_page(self):
        self.animate_transition(self.page2, self.page1, direction='right')

    def animate_transition(self, from_page, to_page, direction='left'):
        current_index = self.stack.indexOf(from_page)
        next_index = self.stack.indexOf(to_page)
        self.stack.setCurrentIndex(next_index)

        width = self.stack.frameGeometry().width()

        if direction == 'left':
            start_rect = QRect(width, 0, width, self.height())
            end_rect = QRect(0, 0, width, self.height())
        else:  # 'right'
            start_rect = QRect(-width, 0, width, self.height())
            end_rect = QRect(0, 0, width, self.height())

        to_page.setGeometry(start_rect)

        animation = QPropertyAnimation(to_page, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(start_rect)
        animation.setEndValue(end_rect)
        animation.start()
        self.animation = animation  # prevent garbage collection

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SlideTransition()
    win.show()
    sys.exit(app.exec_())
