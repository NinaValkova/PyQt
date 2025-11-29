# in PyQt everyting is divided into module and modules are divided into different classes
from PyQt6.QtWidgets import QApplication, QWidget
import sys

# creating the object of the QApplication
app = QApplication(sys.argv)

# base class of all user interface-it recives mouse, keyboard events
window = QWidget()

window.show()

# execute app
sys.exit(app.exec())
