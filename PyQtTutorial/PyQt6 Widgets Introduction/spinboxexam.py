from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QSpinBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)
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
        self.setWindowTitle("PyQT QSpinBox")
        self.setWindowIcon(QIcon(IMG_PATH))

        hbox = QHBoxLayout()

        label = QLabel("Laptop Price: ")
        label.setFont(QFont("Times", 15))

        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)

        self.total_result = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)
    
    def spin_selected(self):
        if self.lineedit.text() != 0:
            price = int(self.lineedit.text())
            totalPrice = self.spinbox.value() * price
            
            self.total_result.setText(str(totalPrice))   
        else:
            print("Wrong value")    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
