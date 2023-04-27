from PySide6.QtGui import QAction
from PySide6.QtWidgets import QGridLayout, QListWidget, QMainWindow, QTreeWidget

from ..widget.modelbrowser import ModelBrowser

class Ui_MainWindow(object):
    modelBroswerAction: QAction
    centralLayout: QGridLayout
    modelTree: QTreeWidget
    processWidget: QListWidget
    modelBrowser: ModelBrowser
    def setupUi(self, MainWindow: QMainWindow) -> None: ...
