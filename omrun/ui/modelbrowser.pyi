from PySide6.QtWidgets import QLabel, QPushButton, QWidget

class Ui_ModelBrowser(object):
    workDirectoryLabel: QLabel
    reloadPushButton: QPushButton
    openPushButton: QPushButton
    def setupUi(self, ModelBrowser: QWidget) -> None: ...
