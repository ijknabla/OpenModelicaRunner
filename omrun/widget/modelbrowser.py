from functools import partial
from itertools import chain
from pathlib import Path
from typing import ClassVar

from bidict import bidict
from PySide6.QtCore import QPoint, Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QPushButton, QTreeWidgetItem, QWidget

from .. import BuiltModel
from ..ui.modelbrowser import Ui_ModelBrowser
from .setupdialog import SetupDialog
from .util import get_tree_path, make_tree


class ModelBrowser(Ui_ModelBrowser, QWidget):
    modelSelected: ClassVar[Signal] = Signal(BuiltModel)

    models: bidict[tuple[str, ...], BuiltModel]
    modelPath: tuple[str, ...]

    def __init__(
        self,
        parent: QWidget | None = None,
        f: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, f=f)
        self.setupUi(self)

        self.models = bidict()
        self.modelPath = ()
        self.treeWidget.currentItemChanged.connect(
            lambda item, previous: setattr(self, "modelPath", get_tree_path(item))
        )

        self.workDirectoryChanged.connect(lambda d: self.workDirectoryLabel.setText(str(d)))
        self.workDirectoryChanged.connect(self.update_tree)

        self.reloadPushButton.pressed.connect(
            lambda: self.workDirectoryChanged.emit(self.workDirectory)
        )

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

    workDirectoryChanged: ClassVar[Signal] = Signal(Path)

    @property
    def workDirectory(self) -> Path:
        return self.__workDirectory

    @workDirectory.setter
    def workDirectory(self, value: Path) -> None:
        self.__workDirectory = value
        self.workDirectoryChanged.emit(value)

    __workDirectory: Path

    def update_tree(self, directory: Path) -> None:
        self.models = bidict(
            (tuple(builtmodel.directory.name.split(".")), builtmodel)
            for builtmodel in chain.from_iterable(
                map(BuiltModel.from_directory, directory.iterdir())
            )
        )

        self.treeWidget.clear()
        tree = make_tree(self.treeWidget, self.models)

        for path, model in self.models.items():
            item: QTreeWidgetItem = tree[path]
            button = QPushButton("setup")
            button.pressed.connect(partial(self.modelSelected.emit, model))
            self.treeWidget.setItemWidget(item, 1, button)

        self.treeWidget.expandAll()
        self.treeWidget.resizeColumnToContents(0)

    def contextMenu(self, point: QPoint) -> None:
        try:
            model = self.models[self.modelPath]
        except KeyError:
            return

        menu = QMenu(self)

        setupAction = QAction("Setup", self)

        @setupAction.triggered.connect
        def setup() -> None:
            print(model)
            dialog = SetupDialog(self)
            dialog.exec()

        menu.addAction(setupAction)

        menu.exec(self.mapToGlobal(point))
