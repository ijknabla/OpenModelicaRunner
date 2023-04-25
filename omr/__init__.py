import sys

from PySide6.QtWidgets import QApplication, QMainWindow


def main() -> None:
    app = QApplication()
    mainwindow = QMainWindow()
    mainwindow.show()
    sys.exit(app.exec())
