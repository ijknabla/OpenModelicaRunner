from PySide6.QtWidgets import QLabel, QPushButton, QTreeWidget, QWidget

class Ui_ModelBrowser(object):
    workDirectoryLabel: QLabel
    reloadPushButton: QPushButton
    openPushButton: QPushButton
    treeWidget: QTreeWidget
    def setupUi(self, ModelBrowser: QWidget) -> None: ...
