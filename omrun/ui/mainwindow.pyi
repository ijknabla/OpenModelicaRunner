from PySide6.QtGui import QAction
from PySide6.QtWidgets import QGridLayout, QListWidget, QMainWindow, QTreeWidget

class Ui_MainWindow(object):
    modelBroswerAction: QAction
    centralLayout: QGridLayout
    modelTree: QTreeWidget
    processWidget: QListWidget
    def setupUi(self, MainWindow: QMainWindow) -> None: ...
