from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT Stretch ")

        main_layout = QVBoxLayout()

        row1_layout = QHBoxLayout()
        label1 = QLabel("First Name: ")
        line1 = QLineEdit()
        row1_layout.addWidget(label1)
        row1_layout.addWidget(line1)

        row2_layout = QHBoxLayout()
        label2 = QLabel("Last Name: ")
        line2 = QLineEdit()
        row2_layout.addWidget(label2)
        row2_layout.addWidget(line2)

        row3_layout = QHBoxLayout()
        button = QPushButton("Submit")
        row3_layout.addWidget(button)

        main_layout.addLayout(row1_layout)
        main_layout.addLayout(row2_layout)
        main_layout.addLayout(row3_layout)
        
        self.setLayout(main_layout)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
