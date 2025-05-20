from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QLabel, QScrollArea, QSizePolicy
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

PREVIEW_W = 300   # width of the preview image


class ImageSingleViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pick ONE image & replace preview")
        self.resize(550, 400)

        # -------- central widget & vertical layout --------
        central = QWidget(); self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        # -- pick-file button --
        pick_btn = QPushButton("Choose image…")
        pick_btn.clicked.connect(self.open_file_dialog)
        vbox.addWidget(pick_btn)

        # -- scroll area (keeps UI consistent with your original) --
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        vbox.addWidget(self.scroll)

        self.scroll_content = QWidget()
        self.scroll.setWidget(self.scroll_content)

        # layout inside scroll area
        self.scroll_content_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content_layout.setAlignment(Qt.AlignTop)

        # a single QLabel placeholder for preview (created once)
        self.preview_lbl = QLabel("No image selected")
        self.preview_lbl.setAlignment(Qt.AlignCenter)
        self.preview_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scroll_content_layout.addWidget(self.preview_lbl)

    # ------------- pick ONE image & replace preview -------------
    def open_file_dialog(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an image file",
            "",
            "Images (*.png *.jpeg *.jpg *.gif *.bmp);;All files (*)"
        )
        if not path:            # user cancelled
            return

        pix = QPixmap(path)
        if pix.isNull():
            self.preview_lbl.setText("Selected file is not a valid image.")
            return

        # replace the existing preview
        self.preview_lbl.setPixmap(
            pix.scaledToWidth(PREVIEW_W, Qt.SmoothTransformation))
        self.preview_lbl.setText("")   # clear placeholder text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageSingleViewer()
    window.show()
    sys.exit(app.exec_())
