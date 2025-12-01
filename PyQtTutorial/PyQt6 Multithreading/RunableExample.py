"""
By utilizing runnable and threadpool, can achive asynchronous execution of tasks in a separate thread pool
Thread pool handles the managment of threads including their creation, reuse, destruction

Usinf runnable on thread pool, the worker enables are executed asynchronously in separate threads managed by the thread pool
"""

import sys
import time
from random import randint
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QLabel,
)

class WorkerSignals(QObject):
    result_ready = pyqtSignal(int)

# Worker does not manage its own thread
# The thread pool decides where (in which thread) to run it.
class Worker(QRunnable):
    def __init__(self, worker_id, signals):
        super().__init__()
        self.worker_id = worker_id
        self.signals = signals

    def run(self):
        time.sleep(2)
        result = self.worker_id * 10
        self.signals.result_ready.emit(result)   


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRunnable")
        self.setFixedSize(300, 200)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_tasks)

        vbox.addWidget(self.button)

        self.scroll_area = QScrollArea()
        self.results_label = QLabel("Result: ")
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.results_label)

        vbox.addWidget(self.scroll_area)
        self.setLayout(vbox)

        self.thread_pool = QThreadPool()

    def start_tasks(self):
        self.button.setEnabled(False)

        signals = WorkerSignals()

        for i in range(1, 6):
            worker = Worker(i, signals)
            signals.result_ready.connect(self.collect_result)
            self.thread_pool.start(worker)

    # method is called every time a worker thread finishes and emits
    def collect_result(self, result):
        current_results = self.results_label.text()
        new_result = f"Worker Result: {result}"
        self.results_label.setText(current_results + "<br>" + new_result)

        scroll_bar = self.scroll_area.verticalScrollBar()
        if scroll_bar: 
            scroll_bar.setValue(scroll_bar.maximum())

        if self.thread_pool.activeThreadCount() == 0:
            self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
