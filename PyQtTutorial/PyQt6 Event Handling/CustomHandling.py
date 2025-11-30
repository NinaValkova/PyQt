from PyQt6.QtCore import Qt, QObject, QEvent, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

# Creates your own event type
class CustomEvent(QEvent):
    # reserves a new unique number for your event type.
    # Example: 1002, 1003, etc.
    event_type = QEvent.registerEventType()

    # create a real Qt event with your custom type.
    def __init__(self, message):
        super().__init__(CustomEvent.event_type)
        # event stores a message string
        self.message = message

class CustomEventEmitter(QObject):   
    # custom_event is a signal that carries a CustomEvent object
    custom_event = pyqtSignal(CustomEvent)

    # creates a new event and emits the signal
    def emit_custom_event(self, message):
        event = CustomEvent(message)
        self.custom_event.emit(event)

class MainWinow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Event Handling")
        self.label = QLabel("No custom event received yet", self)   

        self.label.setGeometry(5,5, 150, 150)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)   

    def custom_event_handler(self, event):
        self.label.setText(event.message)     

    def custom_event_filter(self, obj, event):
        if event.type() == CustomEvent.event_type:
            self.custom_event_handler(event)
            return True
        return False

app = QApplication(sys.argv)
window = MainWinow()
emitter = CustomEventEmitter()
# creates a connection
emitter.custom_event.connect(window.custom_event_handler)
# emit the signal
emitter.emit_custom_event("Custom Event Received")
window.show()
sys.exit(app.exec())
