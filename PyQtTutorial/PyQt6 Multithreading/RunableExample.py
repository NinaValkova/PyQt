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
        #This means:“I am done.Send the result to the main thread now
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
            # When result_ready is emitted in the future, call collect_result().
            # This line does NOT run collect_result().
            # It does NOT emit any signal.
            # It does NOT start any worker.
            signals.result_ready.connect(self.collect_result)
            # Qt, please take this worker task and run its run() method in a background thread from the pool
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

# The worker thread emits:
# result_ready.emit(30)

# Step 2
# Qt looks for any connected slot:
# signals.result_ready.connect(self.collect_result)

# Step 3
# Qt automatically calls:
# self.collect_result(30)
# in the main GUI thread


# ThreadPool runs multiple workers concurrently
# All workers run IN PARALLEL (as long as thread pool has free threads).
# Example:
# Worker 1 starts immediately
# Worker 2 also starts at the same time
# Worker 3 may start 1 ms later
# Worker 4 waits if no thread is free
# Worker 5 may start after Worker 3 finishes
# Order is NOT guaranteed.

# Visual Timeline (THIS IS EXACTLY WHAT HAPPENS)
# for i in range(5 workers):
# 1. connect signal → collect_result
# 2. add worker to thread_pool queue

# THREADPOOL begins running them:
# Worker 3 starts
# Worker 1 starts
# Worker 2 waits
# Worker 4 starts
# Worker 5 waits

# Worker 4 finishes → emit signal → collect_result(40)
# Worker 1 finishes → emit signal → collect_result(10)
# Worker 3 finishes → emit signal → collect_result(30)
# Worker 2 finishes → emit signal → collect_result(20)
# Worker 5 starts
# Worker 5 finishes → emit signal → collect_result(50)

# activeThreadCount == 0 → enable button

# Operation	What it does	When it happens
# .connect()	Registers what function to call later	Before thread starts
# .start(worker)	Schedules worker to run	Immediately after connect
# .emit(result)	Sends signal → calls collect_result()	When worker finishes
# collect_result() runs ONLY when the signal is emitted — NOT when it is connected.
