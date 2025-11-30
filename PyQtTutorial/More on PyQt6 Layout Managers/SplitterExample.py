from PyQt6.QtWidgets import QApplication, QWidget, QSplitter, QTextEdit, QVBoxLayout
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT QSplitter")
        
        main_layout = QVBoxLayout()
        
        splitter = QSplitter()
        
        edit1 = QTextEdit()
        edit2 = QTextEdit()
        
        splitter.addWidget(edit1)
        splitter.addWidget(edit2)
        splitter.setSizes([200, 300])
        
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
