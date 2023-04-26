import sys
from asyncio import set_event_loop

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from qasync import QEventLoop

from .ui.mainwindow import Ui_MainWindow


def main() -> None:
    app = QApplication()
    loop = QEventLoop(app)
    set_event_loop(loop)
    with loop:
        mainwindow = MainWindow()
        mainwindow.show()
        sys.exit(app.exec())


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(
        self,
        parent: QWidget | None = None,
        flags: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
