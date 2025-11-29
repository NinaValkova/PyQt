from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QSlider,
    QHBoxLayout,
    QLabel
)
from PyQt6.QtGui import QIcon, QFont, QFont
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QSlider")
        self.setWindowIcon(QIcon(IMG_PATH))

        hbox = QHBoxLayout()

        self.slider = QSlider() 
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(10)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changed_slider)

        self.label = QLabel("")
        self.label.setFont(QFont("Times", 15))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))  

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
