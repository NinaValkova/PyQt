from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStackedLayout,
    QPushButton,
)
import sys
import os
from PyQt6.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT Stretch ")

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        stacked_layout = QStackedLayout()

        view1 = QLabel("View 1")
        view1.setFont(QFont("Times", 20))
        view2 = QLabel("View 2")
        view2.setFont(QFont("Times", 20))
        view3 = QLabel("View 3")
        view3.setFont(QFont("Times", 20))

        stacked_layout.addWidget(view1)
        stacked_layout.addWidget(view2)
        stacked_layout.addWidget(view3)

        stacked_layout.setCurrentIndex(0)

        button1 = QPushButton("View 1")
        button2 = QPushButton("View 2")
        button3 = QPushButton("View 3")

        button1.clicked.connect(lambda: stacked_layout.setCurrentIndex(0))
        button2.clicked.connect(lambda: stacked_layout.setCurrentIndex(1))
        button3.clicked.connect(lambda: stacked_layout.setCurrentIndex(2))

        main_layout.addWidget(button1)
        main_layout.addWidget(button2)
        main_layout.addWidget(button3)

        main_layout.addLayout(stacked_layout)
        
        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
