from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)

# i have only close button, without maximize and minimize bitton
window = QDialog()

window.show()

sys.exit(app.exec())
