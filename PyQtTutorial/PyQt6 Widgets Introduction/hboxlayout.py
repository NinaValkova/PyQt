from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QHBoxLayout")
        self.setWindowIcon(QIcon(IMG_PATH))

        # - buttons are horizontal
        hbox = QHBoxLayout()

        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        
        hbox.addSpacing(100)
        # hbox.addStretch(5)

        # to set layout to window
        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
