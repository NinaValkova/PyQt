from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic
from PyQt6.uic.load_ui import loadUi

# loadUi inside the internal module load_ui


class UI(QWidget):
    def __init__(self):
        super().__init__()

        loadUi("WindowUI.ui", self)


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
