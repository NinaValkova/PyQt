"""
Handling network request, interact with APIs is a capability
that allows developers to build applications that communicate with web severs and retrive or send data.
Create Http requests, send hem to server and process the responses
"""

# 1) QNetworkAccessManager
# Manages HTTP operations like GET, POST, PUT, DELETE.

# 2) QNetworkRequest
# Represents the request (URL, headers, etc.).

# 3) QNetworkReply
# The response from the server (success or error).

# URL https://jsonplaceholder.typicode.com/posts

from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)
import sys
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt6.QtCore import QUrl


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 REST API")

        vbox = QVBoxLayout()

        url_label = QLabel("URL: ")
        self.input = QLineEdit()
        send_button = QPushButton("Send Request")
        send_button.clicked.connect(self.send_request)

        response_label = QLabel("Response: ")
        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)

        vbox.addWidget(url_label)
        vbox.addWidget(self.input)
        vbox.addWidget(send_button)

        vbox.addWidget(response_label)
        vbox.addWidget(self.response_text)

        self.setLayout(vbox)

        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_response)

    def send_request(self):
        url = self.input.text()
        request = QNetworkRequest(QUrl(url))
        self.network_manager.get(request)

    def handle_response(self, reply):
        error = reply.error()

        if error == QNetworkReply.NetworkError.NoError:
            response = reply.readAll().data().decode("utf-8")
            self.response_text.setPlainText(response)
        else:
            error_message = reply.errorString()
            self.response_text.setPlainText(f"Error: {error_message}")

    # When the window closes
    def closeEvent(self, event):
        self.network_manager.deleteLater()
        super().closeEvent(event)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
