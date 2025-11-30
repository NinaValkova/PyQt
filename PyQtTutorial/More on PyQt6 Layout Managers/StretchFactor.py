from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel
)
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT Stretch ")

        vbox = QVBoxLayout()

        label1= QLabel("Strtchable Label")
        label2 = QLabel("Fixed Label")

        vbox.addWidget(label1)
        vbox.addWidget(label2)

        # Stretch factors tell Qt how to distribute extra vertical space.
        # label1 grows 5× more than label2
        # stretch = 1 requests some extra space., stretch = 0 requests no extra space.
        vbox.setStretch(0,5)
        vbox.setStretch(1,0)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
