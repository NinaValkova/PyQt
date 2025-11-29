from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout
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
        self.setWindowTitle("PyQT QLineEdit")
        self.setWindowIcon(QIcon(IMG_PATH))
        
        vbox = QVBoxLayout()
        
        self.list_widget = QListWidget()
        
        self.list_widget.insertItem(0, "Python")
        self.list_widget.insertItem(1, "Java")
        self.list_widget.insertItem(2, "C++")
        
        self.list_widget.setFont(QFont("Times", 15))
        self.list_widget.setStyleSheet("background-color:grey")
        
        self.list_widget.clicked.connect(self.item_clicked)
        
        self.label = QLabel()
        self.label.setFont(QFont("Times", 15))

        vbox.addWidget((self.list_widget))
        vbox.addWidget(self.label)
        
        vbox.addWidget(self.list_widget)
        
        self.setLayout(vbox)
    
    def item_clicked(self):
        item = self.list_widget.currentItem()
        
        if item:
            self.label.setText("You have selected: "+ str(item.text()))    
        


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
