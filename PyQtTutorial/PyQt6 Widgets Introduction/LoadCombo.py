from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox
import sys
from PyQt6 import uic
from PyQt6.uic.load_ui import loadUi

# loadUi inside the internal module load_ui


class UI(QWidget):
    def __init__(self):
        super().__init__()

        loadUi("ComboDemo.ui", self)
        
        self.label_result = self.findChild(QLabel, "label_result")
        
        self.combo = self.findChild(QComboBox, "comboBox")
        
        self.combo.currentTextChanged.connect(self.combo_canged)
        
    def combo_canged(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Favorite Language: "+ item)
                 
        


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
