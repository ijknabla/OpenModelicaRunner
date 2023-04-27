from PySide6.QtWidgets import QGridLayout, QListWidget, QMainWindow, QTreeWidget

class Ui_MainWindow(object):
    centralLayout: QGridLayout
    modelTree: QTreeWidget
    processWidget: QListWidget
    def setupUi(self, MainWindow: QMainWindow) -> None: ...
