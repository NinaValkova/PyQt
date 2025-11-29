from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
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

        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()

        label = QLabel("Select Accoutn Type:") 
        label.setFont(QFont("Times", 15))

        self.combo = QComboBox()
        self.combo.addItem("Current Account")
        self.combo.addItem("Deposite Account")
        self.combo.addItem("Saving Account")
        self.combo.currentTextChanged.connect(self.combo_changed)
        
        vbox = QVBoxLayout()
        self.label_result = QLabel("")
        self.label_result.setFont(QFont("Times", 15))
        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)

        hbox.addWidget(label) 
        hbox.addWidget(self.combo)
        
        self.setLayout(vbox)
    
    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Account Type Is: "+ item)    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
