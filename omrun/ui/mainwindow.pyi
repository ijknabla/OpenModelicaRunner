from PySide6.QtWidgets import QGridLayout, QMainWindow, QTreeWidget, QWidget

class Ui_MainWindow(object):
    centralLayout: QGridLayout
    modelTree: QTreeWidget
    def setupUi(self, MainWindow: QMainWindow) -> None: ...
