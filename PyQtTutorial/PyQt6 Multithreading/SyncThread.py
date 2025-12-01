"""
When multiple threads are involved, it is crucial to ensure that data ans signals are exchanged in a thread safe manner.
Using signals and slots ensures that the communication between threads is synchronized and avoids issues such as race conditions or data corruption.
Signals and slots enable asynchronous processing where time cosuming tasks can be executed concurrently in separate threads.
"""

import sys
import time
from random import randint
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QLabel,
)


class Worker(QThread):
    # You define a signal called result_ready.
    # This signal can send an int value to the main thread.
    result_ready = pyqtSignal(int)

    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id

    def run(self):
        time.sleep(randint(1, 5))
        result = self.worker_id * 10
        self.result_ready.emit(result)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Example")
        self.setFixedSize(300, 200)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_tasks)

        vbox.addWidget(self.button)

        self.scrol_area = QScrollArea()
        self.results_label = QLabel("Result: ")
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrol_area.setWidgetResizable(True)
        self.scrol_area.setWidget(self.results_label)

        vbox.addWidget(self.scrol_area)
        self.setLayout(vbox)

        self.worker_threads = []

    def start_tasks(self):
        self.button.setEnabled(False)

        for i in range(1, 6):
            worker = Worker(i)
            worker.result_ready.connect(self.collect_result)
            self.worker_threads.append(worker)
            worker.start()

    def collect_result(self, result):
        current_results = self.results_label.text()
        new_result = f"Worker Result: {result}"
        self.results_label.setText(current_results + "\n" + new_result)

        if len(self.worker_threads) == len(
            [t for t in self.worker_threads if not t.isRunning()]
        ):
            # if all threads funished then it enables the button to allow further user interaction
            self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# Each worker does one task
# Produces one result
# Finishes
# Sends one notification

# For example:
# Worker #1
# ➡ Sleeps 2 seconds
# ➡ Computes 10
# ➡ Emits 10
# ➡ Ends
# Worker #2
# ➡ Sleeps 5 seconds
# ➡ Computes 20
# ➡ Emits 20
# ➡ Ends
