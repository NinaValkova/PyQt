from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton 
from PyQt6.QtGui import QIcon
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QGridLayout")
        self.setWindowIcon(QIcon(IMG_PATH))

        grid = QGridLayout()

        btn1 = QPushButton("One")
        btn2 = QPushButton("Two")
        btn3 = QPushButton("Three")
        btn4 = QPushButton("Four")
        btn5 = QPushButton("Five")
        btn6 = QPushButton("Six")
        btn7 = QPushButton("Seven")
        btn8 = QPushButton("Eight")

        # grid layout
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)
        
        self.setLayout(grid)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
