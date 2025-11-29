from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # __file__ = location of your script
        # os.path.dirname(__file__) = directory containing your script.
        BASE_DIR = os.path.dirname(__file__)
        # builds a safe relative path
        IMG_PATH = os.path.join(BASE_DIR, "images/python.png")

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon(IMG_PATH))

        """
        label = QLabel("Python GUI Development", self)
        label.setText("New Text is here")
        label.move(100, 100)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet('color:red')
        
        #label.setText(str(12))
        label.setNum(12)
        label.clear()
        """

        label = QLabel(self)
        pixmap = QPixmap(IMG_PATH)
        label.setPixmap(pixmap)

        label = QLabel(self)
        movie = QMovie("images/sky.gif")
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
