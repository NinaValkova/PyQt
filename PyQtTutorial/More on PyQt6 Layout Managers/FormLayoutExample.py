from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QFormLayout,QLineEdit
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QSplitter")

        main_layout = QVBoxLayout()

        form_layout = QFormLayout()

        label1 = QLabel("Name: ")
        line1 = QLineEdit()

        label2 = QLabel("Email: ")
        line2 = QLineEdit()

        label3 = QLabel("Phone: ")
        line3 = QLineEdit()

        form_layout.addRow(label1, line1)
        form_layout.addRow(label2, line2)
        form_layout.addRow(label3, line3)
        
        main_layout.addLayout(form_layout)
        
        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
