from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QPushButton")
        self.setWindowIcon(QIcon(IMG_PATH))

        self.create_button()

    def  create_button(self):
        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        btn = QPushButton("Click", self)
        btn.setGeometry(100, 100, 130, 130)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold)) 
        btn.setIcon(QIcon(IMG_PATH))
        btn.setIconSize(QSize(36, 36))

        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:blue')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
