from PySide6.QtWidgets import QGridLayout, QMainWindow, QWidget

class Ui_MainWindow(object):
    centralWidget: QWidget
    centralLayout: QGridLayout
    def setupUi(self, MainWindow: QMainWindow) -> None: ...
