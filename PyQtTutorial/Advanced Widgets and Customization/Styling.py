from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT Styling")

        button = QPushButton("Click Me")

        vbox = QVBoxLayout()

        vbox.addWidget(button)

        self.setLayout(vbox)

        button.setStyleSheet(
            """
        QPushButton{
            background-color:#4CAF50;
            color: white;
            font-size:18px;
            border:none;
            border-radius:10px;
        }
        
       QPushButton:hover {
        background-color: #4CAF49;
        }

        
        QPushButton:pressed{
            background-color: #367c39;
        }
        
        """
        )

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
