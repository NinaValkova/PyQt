from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QFont
from PyQt6.QtCore import QSize
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")
        IMG_Java_PATH = os.path.join(BASE_DIR, "images/java.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QCheckBox")
        self.setWindowIcon(QIcon(IMG_PATH))

        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QIcon(IMG_PATH))
        self.check1.setIconSize(QSize(40,40))
        self.check1.setFont(QFont("Sanserif", 13))
        self.check1.stateChanged.connect(self.item_selected)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QIcon(IMG_Java_PATH))
        self.check2.setIconSize(QSize(40,40))
        self.check2.setFont(QFont("Sanserif", 13))
        self.check2.stateChanged.connect(self.item_selected)

        self.label = QLabel("")
        self.label.setFont(QFont("Sanserif", 15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)

        hbox.addWidget(self.check1)
        hbox.addWidget(self.check2)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def item_selected(self):
        value = ""

        if self.check1.isChecked():
            value = self.check1.text()    
        if self.check2.isChecked():
            value = self.check2.text()
            
        self.label.setText("Your have selected: "+ value)    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
