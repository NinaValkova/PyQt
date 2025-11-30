from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QSpacerItem,
    QSizePolicy,
)
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQT Styling")

        vbox = QVBoxLayout()

        label = QLabel("Welcome to PyQt6 Course")
        vbox.addWidget(label)

        button = QPushButton("Add Spacer")
        button.clicked.connect(self.add_spacer)
        vbox.addWidget(button)

        self.setLayout(vbox)

    def add_spacer(self):
        spacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        layout = self.layout()

        if layout is not None:  
            layout.addItem(spacer)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
