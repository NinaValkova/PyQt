# using TCP server to create TCP server
# server lisen for incoming connection from the client and handles them

from email import message
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtNetwork import QTcpServer, QHostAddress
from PyQt6.QtNetwork import QTcpSocket
from typing import cast


class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Server")

        self.label = QLabel(self)
        self.setGeometry(50, 50, 200, 80)

        self.server = QTcpServer(self)
        self.server.newConnection.connect(self.new_connection)
        self.server.listen(QHostAddress("127.0.0.1"), 8888)

    def new_connection(self):
        client_socket = self.server.nextPendingConnection()
        # ready read signal is emmitted when there is a data availabe to be read from client socket
        if client_socket:
            client_socket.readyRead.connect(self.receive_message)

    def receive_message(self):
        client_socket = self.sender()  # returns QObject
        client_socket = cast(QTcpSocket, client_socket)

        if client_socket:
            message = client_socket.readAll().data().decode()
        self.label.setText(f"Received: {message}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec())
