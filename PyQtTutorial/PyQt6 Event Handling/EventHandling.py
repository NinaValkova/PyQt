from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT Event Handling")
        
        button = QPushButton("Click Me")
        button.clicked.connect(self.handle_button_click)
        vbox = QVBoxLayout()
        vbox.addWidget(button)
        
        self.label = QLabel("No button click yet")
        vbox.addWidget(self.label)
        
        self.setLayout(vbox)
        
        self.installEventFilter(self)
        
    def handle_button_click(self):
        self.label.setText("Button Clicked")  
    
    def eventFilter(self, obj, event):
        if obj is self and event.type() == event.Type.KeyPress:
            print("Key Pressed", event.key())
            return True
        return super().eventFilter(obj, event) 
              

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
