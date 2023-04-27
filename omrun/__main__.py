import sys
from asyncio import set_event_loop

from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from .widget.mainwindow import MainWindow


def main() -> None:
    app = QApplication()
    loop = QEventLoop(app)
    set_event_loop(loop)
    with loop:
        mainwindow = MainWindow()
        mainwindow.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
