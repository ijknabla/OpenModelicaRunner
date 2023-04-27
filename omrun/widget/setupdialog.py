from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QWidget

from ..ui.setupdialog import Ui_SetupDialog


class SetupDialog(Ui_SetupDialog, QDialog):
    def __init__(
        self,
        parent: QWidget | None = None,
        f: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, f=f)
        self.setupUi(self)
