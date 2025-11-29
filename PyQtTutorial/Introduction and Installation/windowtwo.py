from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

# can access to QStatusBar, QToolBar, QMenubar
window = QMainWindow()


status = window.statusBar()  
if status:
    status.showMessage("Welcome to PyQt6 Course")
    
menu = window.menuBar()
if menu:
    menu.addMenu("File")    

window.show()

sys.exit(app.exec())
