
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

def main() -> None:
    app = QApplication()
    mainwindow = QMainWindow()
    mainwindow.show()
    sys.exit(app.exec())
