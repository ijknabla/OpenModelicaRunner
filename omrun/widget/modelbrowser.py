from pathlib import Path
from typing import ClassVar

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

from ..ui.modelbrowser import Ui_ModelBrowser


class ModelBrowser(Ui_ModelBrowser, QWidget):
    workDirectoryChanged: ClassVar[Signal] = Signal(Path)

    def __init__(
        self,
        parent: QWidget | None = None,
        f: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, f=f)
        self.setupUi(self)

        self.workDirectoryChanged.connect(lambda p: self.workDirectoryLabel.setText(str(p)))
