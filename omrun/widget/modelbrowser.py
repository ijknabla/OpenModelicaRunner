from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ..ui.modelbrowser import Ui_ModelBrowser


class ModelBrowser(Ui_ModelBrowser, QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        f: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, f=f)
        self.setupUi(self)
