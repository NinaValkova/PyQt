from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QVBoxLayout")
        self.setWindowIcon(QIcon(IMG_PATH))

        # vbox layout - buttons are vertically
        vbox = QVBoxLayout()

        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Clcik Two")
        btn3 = QPushButton("Clcik Three")
        btn4 = QPushButton("Clcik Four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        vbox.addSpacing(100)
        vbox.addStretch(5)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
