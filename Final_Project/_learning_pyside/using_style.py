import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
)


if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placeholder text")
    w.setAlignment(Qt.AlignCenter)

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
   
    w.show()
    sys.exit(app.exec())