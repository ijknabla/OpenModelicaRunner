import sys

from PySide6.QtWidgets import QApplication

from .view import MainWindow


def main() -> None:
    app = QApplication()
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
