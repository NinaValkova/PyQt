from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel
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
        self.setWindowTitle("PyQT QGridLayout")
        self.setWindowIcon(QIcon(IMG_PATH))

        self.create_radio()

    def create_radio(self):
        BASE_DIR = os.path.dirname(__file__)
        IMG_PYTHON_PATH = os.path.join(BASE_DIR, "images/python.png")
        IMG_JAVA_PATH = os.path.join(BASE_DIR, "images/java.png")
        IMG_JAVASCIPT_PATH = os.path.join(BASE_DIR, "images/javascript.png")

        hbox = QHBoxLayout()

        rad1 = QRadioButton('Python')
        rad1.setIcon(QIcon(IMG_PYTHON_PATH))
        rad1.setIconSize(QSize(40,40))
        rad1.setFont(QFont("Times", 14))
        rad1.setChecked(True)
        # in push button there is clicked signal, but in radio button we have also toggled
        rad1.toggled.connect(self.radio_selected)

        rad2 = QRadioButton('Java')
        rad2.setIcon(QIcon(IMG_JAVA_PATH))
        rad2.setIconSize(QSize(40,40))
        rad2.setFont(QFont("Times", 14))
        rad2.toggled.connect(self.radio_selected)

        rad3 = QRadioButton('JavaScript')
        rad3.setIcon(QIcon(IMG_JAVASCIPT_PATH))
        rad3.setIconSize(QSize(40,40))
        rad3.setFont(QFont("Times", 14))
        rad3.toggled.connect(self.radio_selected)

        self.label = QLabel("")
        self.label.setFont(QFont("Sanserif", 15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        # Should be the main layout because it contains everything Label + hbox
        vbox.addLayout(hbox)

        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        hbox.addWidget(rad3)

        # make hbox the main layout of the window
        # hbox is child layout
        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()

        if isinstance(radio_btn, QRadioButton) and radio_btn.isChecked():
            self.label.setText("You have selected: {}".format(radio_btn.text()))    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
