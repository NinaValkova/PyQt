# using TCP socket class to create TCP client
# client connect to server to exchange data
"""sockets ar building blocks of network communication packet
provides the TCP socket and YDP socket classes. This classes
allows you to establish connections, send, recive data.


Signal and slots mechanism for handing a networking programming
Signal are emitted when specific network events occur, such as new connection or data ready to be read

Data serialization - serialize and deserialize the data to ensure compatibility between different platforms and programming languages
Data serialization through different formats includeing JSON, XML, binary format
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import sys
from PyQt6.QtNetwork import QTcpSocket


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Client")

        self.line = QLineEdit(self)
        self.line.setGeometry(50, 50, 150, 50)

        button = QPushButton("Send", self)
        button.setGeometry(50, 100, 100, 30)
        button.clicked.connect(self.send_message)

        self.client_socket = QTcpSocket()
        self.client_socket.connected.connect(self.connected)
        self.client_socket.readyRead.connect(self.receive_message)
        self.client_socket.disconnected.connect(self.disconnected)
        self.client_socket.errorOccurred.connect(self.display_error)

        self.client_socket.connectToHost("localhost", 8888)

    def send_message(self):
        message = self.line.text()
        self.client_socket.write(message.encode())

    def connected(self):
        print("Connected to server")

    def receive_message(self):
        message = self.client_socket.readAll().data().decode()
        print(f"Received: {message}")

    def disconnected(self):
        print("Disconnected from server")

    def display_error(self, socket_error):
        print(f"Socket error occured: {socket_error}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec())
