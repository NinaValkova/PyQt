from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QFont
from PyQt6.QtCore import QSize
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QLineEdit")
        self.setWindowIcon(QIcon(IMG_PATH))
        
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif", 15))
        # line_edit.setText("Default Text")
        # line_edit.setPlaceholderText("Please enter your username")
        # line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
