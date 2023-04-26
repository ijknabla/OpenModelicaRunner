import sys
from asyncio import create_subprocess_exec, set_event_loop
from collections.abc import Iterable
from contextlib import suppress
from functools import partial
from itertools import chain
from pathlib import Path
from typing import ClassVar

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)
from qasync import QEventLoop

from . import AsyncSlot, BuiltModel, find_free_port, get_omedit_work_directory
from .ui.mainwindow import Ui_MainWindow


def main() -> None:
    app = QApplication()
    loop = QEventLoop(app)
    set_event_loop(loop)
    with loop:
        mainwindow = MainWindow()
        mainwindow.show()
        sys.exit(app.exec())


class MainWindow(Ui_MainWindow, QMainWindow):
    workDirectoryUpdated: ClassVar[Signal] = Signal(Path)

    def __init__(
        self,
        parent: QWidget | None = None,
        flags: Qt.WindowType = Qt.WindowType(0),
    ) -> None:
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.workDirectoryUpdated.connect(self.on_workDirectoryUpdated)
        self.showMaximized()

        self.workDirectoryUpdated.emit(get_omedit_work_directory())

    def on_workDirectoryUpdated(self, directory: Path) -> None:
        self.modelTree.clear()

        self.add_builtmodels(
            self.modelTree, chain.from_iterable(map(BuiltModel.from_directory, directory.iterdir()))
        )

        self.modelTree.expandAll()
        self.modelTree.resizeColumnToContents(0)

    @staticmethod
    def add_builtmodels(tree: QTreeWidget, builtmodels: Iterable[BuiltModel]) -> None:
        elements: dict[tuple[str, ...], QTreeWidget | QTreeWidgetItem]
        elements = {(): tree}

        def add_builtmodel(
            key: tuple[str, ...],
            builtmodel: BuiltModel | None = None,
        ) -> QTreeWidget | QTreeWidgetItem:
            with suppress(KeyError):
                return elements[key]

            parent = add_builtmodel(key[:-1])

            item = QTreeWidgetItem(parent)
            item.setText(0, key[-1])

            if builtmodel is not None:
                button = QPushButton()

                @AsyncSlot()
                async def clicked(builtmodel: BuiltModel) -> None:
                    port = find_free_port()
                    process = await create_subprocess_exec(
                        f"{builtmodel.executable}", f"-port={port}", cwd=builtmodel.directory
                    )
                    await process.wait()
                    print(f"{builtmodel.executable} done!")

                button.clicked.connect(partial(clicked, builtmodel))
                tree.setItemWidget(item, 1, button)

            elements[key] = item
            return item

        for builtmodel in builtmodels:
            add_builtmodel(tuple(builtmodel.directory.name.split(".")), builtmodel)
