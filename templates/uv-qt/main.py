import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minimal Echo App")

        # Create widgets
        self.line_edit = QLineEdit()
        self.hello_button = QPushButton("Hello")
        self.goodbye_button = QPushButton("Goodbye")

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.hello_button)
        layout.addWidget(self.goodbye_button)

        # Connections
        self.hello_button.clicked.connect(
            lambda: self.line_edit.setText("hello")
        )
        self.goodbye_button.clicked.connect(
            lambda: self.line_edit.setText("goodbye")
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
