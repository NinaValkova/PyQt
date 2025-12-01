"""
Multithreading refers to the ability of a program to execute
multiple threads concurrently.
A thread is a sequence of instructions that can run independently
and concurrently with other threads.

Developers can perform time consuming tasks and a background without
blocking the main thread - that is responsible for handling user interface
GUI does not freeze or become unresponsible
"""

from re import I
import sys
from PyQt6.QtCore import QThread, pyqtSignal
import time
from PyQt6.QtWidgets import QApplication,   QPushButton, QVBoxLayout, QWidget, QLabel

# WorkerThread is a custom thread
# It has a signal called progress_updated which sends an int.
class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)
    
    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.progress_updated.emit(i)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Example")
        self.setFixedSize(300, 200)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        # button is disabled so you don't start the thread twice
        self.button.clicked.connect(self.start_thread)

        vbox.addWidget(self.button) 

        self.progress_label = QLabel("Progress: ")
        vbox.addWidget(self.progress_label)  

        self.setLayout(vbox)    

        # Create the thread and connect its signals:
        # update_progress(value) runs in the GUI thread
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_updated.connect(self.update_progress)

    def start_thread(self):
        self.button.setEnabled(False)    
        self.worker_thread.start()

    def update_progress(self, value):  
        self.progress_label.setText(f"Progress: {value}%")

        if value == 100:
            self.button.setEnabled(True)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
