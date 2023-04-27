from functools import partial
from itertools import chain
from pathlib import Path
from typing import ClassVar

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QPushButton, QTreeWidgetItem, QWidget

from .. import BuiltModel
from ..ui.modelbrowser import Ui_ModelBrowser


class ModelBrowser(Ui_ModelBrowser, QWidget):
    workDirectoryChanged: ClassVar[Signal] = Signal(Path)
    modelSelected: ClassVar[Signal] = Signal(BuiltModel)
    __workDirectory: Path

    def __init__(
        self,
        parent: QWidget | None = None,
        f: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, f=f)
        self.setupUi(self)

        self.workDirectoryChanged.connect(self.on_workDirectoryChanged)

    def on_workDirectoryChanged(self, value: Path) -> None:
        self.__workDirectory = value
        self.workDirectoryLabel.setText(str(value))

        self.treeWidget.clear()
        builtmodels = {
            tuple(builtmodel.directory.name.split(".")): builtmodel
            for builtmodel in chain.from_iterable(map(BuiltModel.from_directory, value.iterdir()))
        }

        tree: dict[tuple[str, ...], QTreeWidgetItem] = {}
        for parts in (parts[:i] for parts in builtmodels for i, _ in enumerate(parts, start=1)):
            if parts in tree:
                continue
            tree[parts] = QTreeWidgetItem(tree.get(parts[:-1], self.treeWidget), [parts[-1]])

        for parts, builtmodel in builtmodels.items():
            item: QTreeWidgetItem = tree[parts]
            button = QPushButton("setup")
            button.pressed.connect(partial(self.modelSelected.emit, builtmodel))
            self.treeWidget.setItemWidget(item, 1, button)

        self.treeWidget.expandAll()
        self.treeWidget.resizeColumnToContents(0)
